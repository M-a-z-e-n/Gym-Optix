import xml.etree.ElementTree as ET
import os

def build_perfect_drawio(file_path):
    root = ET.Element('mxfile', host='app.diagrams.net', modified='2026-10-29', agent='drawio-skill', version='24.0.0')
    diagram = ET.SubElement(root, 'diagram', name='AS-IS Thesis Architecture', id='asis_thesis_arch')
    model = ET.SubElement(diagram, 'mxGraphModel', dx='2000', dy='1200', grid='1', gridSize='10', guides='1', tooltips='1', connect='1', arrows='1', fold='1', page='1', pageScale='1', pageWidth='1920', pageHeight='1080', math='0', shadow='1')
    root_cell = ET.SubElement(model, 'root')
    ET.SubElement(root_cell, 'mxCell', id='0')
    ET.SubElement(root_cell, 'mxCell', id='1', parent='0')

    def add_node(nid, val, style, x, y, w, h, parent='1'):
        c = ET.SubElement(root_cell, 'mxCell', id=str(nid), parent=str(parent), style=style, value=val, vertex='1')
        geo = ET.SubElement(c, 'mxGeometry', x=str(x), y=str(y), width=str(w), height=str(h))
        geo.set('as', 'geometry')
        return c

    def add_edge(eid, val, style, src, tgt, waypoints=None, exit_port=None, entry_port=None):
        edge_style = style
        if exit_port:
            edge_style += f"exitX={exit_port[0]};exitY={exit_port[1]};exitDx=0;exitDy=0;"
        if entry_port:
            edge_style += f"entryX={entry_port[0]};entryY={entry_port[1]};entryDx=0;entryDy=0;"
        c = ET.SubElement(root_cell, 'mxCell', id=str(eid), parent='1', style=edge_style, value=val, edge='1', source=str(src), target=str(tgt))
        geo = ET.SubElement(c, 'mxGeometry', relative='1')
        geo.set('as', 'geometry')
        if waypoints:
            arr = ET.SubElement(geo, 'Array')
            arr.set('as', 'points')
            for px, py in waypoints:
                ET.SubElement(arr, 'mxPoint', x=str(px), y=str(py))
        return c

    # -------------------------------------------------------------
    # 0. HEADER TITLE
    # -------------------------------------------------------------
    add_node('hdr_title',
             '<b style="font-size:17px;color:#1e293b;">AS-IS Architecture — Real-Time Exercise Recognition and Repetition Counting System</b><br/>'
             '<span style="font-size:11px;color:#64748b;">Academic Software Architecture based on Master\'s Thesis (Nicolas Ivan Cridlig) | Monocular Gym Video Analysis</span>',
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#f8fafc;strokeColor=#475569;strokeWidth=1.5;align=center;shadow=1;',
             40, 15, 1850, 50, parent='1')

    # -------------------------------------------------------------
    # 1. LAYER 1: VIDEO INPUT SOURCES (CONTAINER)
    # -------------------------------------------------------------
    add_node('c_lane1', '<b>LAYER 1: VIDEO INPUT SOURCES</b>',
             'swimlane;startSize=28;horizontal=0;html=1;whiteSpace=wrap;fillColor=#f8fafc;strokeColor=#64748b;strokeWidth=2;rounded=1;fontStyle=1;fontSize=11;fontColor=#334155;container=1;collapsible=0;pointerEvents=0;',
             40, 80, 220, 670, parent='1')

    in_style = 'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#ffffff;strokeColor=#64748b;strokeWidth=1.5;align=center;fontSize=10;'

    add_node('in_rtsp',
             '<b>RTSP IP Camera</b><br/><span style="color:#64748b;font-size:9.5px;">• Gym ceiling/wall mount<br/>• Monocular RTSP stream<br/>• Low latency H.264 feed</span>',
             in_style, 25, 60, 170, 85, parent='c_lane1')

    add_node('in_webcam',
             '<b>Browser Webcam</b><br/><span style="color:#64748b;font-size:9.5px;">• Athlete user device<br/>• HTML5 getUserMedia<br/>• Real-time client capture</span>',
             in_style, 25, 250, 170, 85, parent='c_lane1')

    add_node('in_file',
             '<b>Video File</b><br/><span style="color:#64748b;font-size:9.5px;">• Recorded MP4 / AVI<br/>• Benchmark datasets<br/>• Offline testing & eval</span>',
             in_style, 25, 440, 170, 85, parent='c_lane1')

    # -------------------------------------------------------------
    # 2. LAYER 2: FASTAPI BACKEND (CONTAINER)
    # -------------------------------------------------------------
    add_node('c_lane2', '<b>LAYER 2: BACKEND & VIDEO PROCESSING (FastAPI)</b>',
             'swimlane;startSize=28;horizontal=0;html=1;whiteSpace=wrap;fillColor=#f0f9ff;strokeColor=#0284c7;strokeWidth=2;rounded=1;fontStyle=1;fontSize=11;fontColor=#0369a1;container=1;collapsible=0;pointerEvents=0;',
             290, 80, 380, 670, parent='1')

    be_style = 'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#ffffff;strokeColor=#0284c7;strokeWidth=1.5;align=center;fontSize=10;'

    add_node('be_factory',
             '<b>Video Source Factory</b><br/><span style="font-size:9px;color:#0369a1;">Selects, initializes & instantiates<br/>appropriate input adapter</span>',
             be_style, 25, 60, 150, 65, parent='c_lane2')

    add_node('be_processor',
             '<b>Frame Processor</b><br/><span style="font-size:9px;color:#0369a1;">Normalization, resize,<br/>BGR ➔ RGB conversion</span>',
             be_style, 25, 180, 150, 65, parent='c_lane2')

    add_node('be_queues',
             '<b>Bounded Frame Queues</b><br/><span style="font-size:9px;color:#0369a1;">Thread-safe memory buffers<br/>Prevents latency & frame drop</span>',
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#e0f2fe;strokeColor=#0284c7;strokeWidth=1.5;align=center;fontSize=10;',
             25, 300, 150, 65, parent='c_lane2')

    add_node('be_workers',
             '<b>Asynchronous Workers</b><br/><span style="font-size:9px;color:#0369a1;">Background worker threads<br/>Executes AI pipelines</span>',
             be_style, 25, 420, 150, 65, parent='c_lane2')

    add_node('be_rest',
             '<b>REST API Endpoints</b><br/><span style="font-size:9px;color:#0369a1;">FastAPI Routers: <code>/plans</code>, <code>/logs</code><br/>CRUD for routines & history</span>',
             be_style, 205, 60, 150, 65, parent='c_lane2')

    add_node('be_streaming',
             '<b>Frame Streaming</b><br/><span style="font-size:9px;color:#0369a1;">Overlays landmarks & labels<br/>Encodes JPEG live stream</span>',
             be_style, 205, 300, 150, 65, parent='c_lane2')

    add_node('be_ws',
             '<b>WebSocket Server</b><br/><span style="font-size:9px;color:#0369a1;">Bidirectional real-time hub<br/>Delivers predictions & video</span>',
             be_style, 205, 420, 150, 65, parent='c_lane2')

    # -------------------------------------------------------------
    # 3. LAYER 3: AI PROCESSING PIPELINE (CONTAINER)
    # -------------------------------------------------------------
    add_node('c_lane3', '<b>LAYER 3: AI PROCESSING PIPELINE (Embedded Models)</b>',
             'swimlane;startSize=28;horizontal=0;html=1;whiteSpace=wrap;fillColor=#fffbeb;strokeColor=#d97706;strokeWidth=2;rounded=1;fontStyle=1;fontSize=11;fontColor=#b45309;container=1;collapsible=0;pointerEvents=0;',
             700, 80, 390, 670, parent='1')

    ai_style = 'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#ffffff;strokeColor=#d97706;strokeWidth=1.5;align=center;fontSize=10;'

    add_node('ai_pose',
             '<b>1. Pose Estimation</b><br/>'
             '<b style="color:#b45309;font-size:10px;">MediaPipe / BlazePose</b><br/>'
             '<span style="font-size:9.5px;color:#475569;">• Extracts 33 3D body keypoints (x,y,z)<br/>• Generates subject Bounding Box<br/>• Real-time per-frame inference</span>',
             ai_style, 25, 60, 340, 90, parent='c_lane3')

    add_node('ai_feat',
             '<b>2. Feature Engineering</b><br/>'
             '<span style="font-size:9.5px;color:#475569;">• Computes <b>14 Joint Angles</b> (Knees, Hips, Elbows...)<br/>'
             '• Computes <b>14 Landmark Visibility Scores</b><br/>'
             '• Vectorizes spatio-temporal features for classifier</span>',
             ai_style, 25, 190, 340, 85, parent='c_lane3')

    add_node('ai_tcn',
             '<b>3. Exercise Classification</b><br/>'
             '<b style="color:#b45309;font-size:10px;">Temporal Convolutional Network (TCN)</b><br/>'
             '<span style="font-size:9.5px;color:#475569;">• Sliding temporal window of angle sequences<br/>'
             '• <b>Classifies 16 Exercise Categories</b> synchronously<br/>'
             '• Outputs real-time softmax class probabilities</span>',
             ai_style, 25, 320, 340, 95, parent='c_lane3')

    add_node('ai_repnet',
             '<b>4. Repetition Counting (Asynchronous)</b><br/>'
             '<b style="color:#b45309;font-size:10px;">RepNet (Temporal Self-Similarity Network)</b><br/>'
             '<span style="font-size:9.5px;color:#475569;">• Evaluates periodic motion across video frames<br/>'
             '• Generates self-similarity temporal matrices<br/>'
             '• <b>Decoupled asynchronously</b> to prevent stream stutter</span>',
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#fef3c7;strokeColor=#d97706;strokeWidth=2;align=center;fontSize=10;',
             25, 460, 340, 105, parent='c_lane3')

    add_node('ai_note',
             '<i style="font-size:9px;color:#92400e;">Architectural Note: All models run in-process within backend worker threads; not isolated microservices.</i>',
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#fffdf5;strokeColor=#fde68a;strokeWidth=1;align=center;',
             25, 595, 340, 40, parent='c_lane3')

    # -------------------------------------------------------------
    # 4A. LAYER 4A: DATA STORAGE (CONTAINER)
    # -------------------------------------------------------------
    add_node('c_lane4a', '<b>LAYER 4A: DATA STORAGE</b>',
             'swimlane;startSize=28;horizontal=0;html=1;whiteSpace=wrap;fillColor=#ecfdf5;strokeColor=#059669;strokeWidth=2;rounded=1;fontStyle=1;fontSize=11;fontColor=#047857;container=1;collapsible=0;pointerEvents=0;',
             1120, 80, 360, 300, parent='1')

    db_style = 'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#ffffff;strokeColor=#059669;strokeWidth=1.5;align=center;fontSize=10;'

    add_node('db_pg',
             '<b>PostgreSQL Database</b><br/><span style="font-size:9.5px;color:#047857;">Managed via Google Cloud SQL</span>',
             'shape=cylinder3;whiteSpace=wrap;html=1;size=12;fillColor=#d1fae5;strokeColor=#059669;strokeWidth=1.5;align=center;fontStyle=1;fontSize=10;',
             25, 50, 310, 60, parent='c_lane4a')

    add_node('db_plans',
             '<b>Table: <code>exercise_plan</code></b><br/><span style="font-size:9.5px;color:#475569;">Routines, target exercise IDs, sets, rep targets</span>',
             db_style, 25, 125, 310, 65, parent='c_lane4a')

    add_node('db_logs',
             '<b>Table: <code>log</code></b><br/><span style="font-size:9.5px;color:#475569;">Completed set logs, timestamps, recognized IDs, counted reps</span>',
             db_style, 25, 205, 310, 65, parent='c_lane4a')

    # -------------------------------------------------------------
    # 4B. LAYER 4B: REACT 19 FRONTEND (CONTAINER)
    # -------------------------------------------------------------
    add_node('c_lane4b', '<b>LAYER 4B: FRONTEND APPLICATION (React 19)</b>',
             'swimlane;startSize=28;horizontal=0;html=1;whiteSpace=wrap;fillColor=#eef2ff;strokeColor=#4f46e5;strokeWidth=2;rounded=1;fontStyle=1;fontSize=11;fontColor=#4338ca;container=1;collapsible=0;pointerEvents=0;',
             1120, 400, 360, 350, parent='1')

    fe_style = 'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#ffffff;strokeColor=#4f46e5;strokeWidth=1.5;align=center;fontSize=10;'

    add_node('fe_stack',
             '<b>React 19 Application Core</b><br/><span style="font-size:9px;color:#4338ca;">Bootstrap 5 • React Router 7 • Custom Hook: <code>useWebSocket.js</code></span>',
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#e0e7ff;strokeColor=#4f46e5;strokeWidth=1.5;align=center;fontSize=10;',
             25, 45, 310, 50, parent='c_lane4b')

    add_node('fe_pages',
             '<b>Application Routes:</b><br/>'
             '<span style="font-size:9.5px;color:#334155;">'
             '• <code>/</code> : Main Application Page<br/>'
             '• <code>/user</code> : User Workout & Personal Routine View<br/>'
             '• <code>/admin</code> : Administrative & Camera Configuration<br/>'
             '• <code>/demo</code> : Live Demonstration & Benchmark View'
             '</span>',
             fe_style, 25, 110, 310, 90, parent='c_lane4b')

    add_node('fe_features',
             '<b>Client Capabilities:</b><br/>'
             '<span style="font-size:9.5px;color:#334155;">'
             '• Live Video Feed with Skeletal Pose Overlay<br/>'
             '• Real-time 16-Category Exercise Classifier Badge<br/>'
             '• Asynchronous Repetition Count & Velocity Updates<br/>'
             '• Workout History Log Review & Exercise Plan Controls'
             '</span>',
             fe_style, 25, 215, 310, 110, parent='c_lane4b')

    # -------------------------------------------------------------
    # LEGEND CONTAINER (RIGHT SIDE)
    # -------------------------------------------------------------
    add_node('c_legend', '<b>ARCHITECTURE LEGEND & CONVENTIONS</b>',
             'swimlane;startSize=28;horizontal=0;html=1;whiteSpace=wrap;fillColor=#ffffff;strokeColor=#94a3b8;strokeWidth=1.5;rounded=1;fontStyle=1;fontSize=11;fontColor=#334155;container=1;collapsible=0;pointerEvents=0;',
             1510, 80, 380, 670, parent='1')

    add_node('legend_info',
             '<b>Arrow Semantics:</b><br/>'
             '<span style="font-size:10px;color:#1e293b;">'
             '━▶ <b>Solid Blue/Amber:</b> Synchronous Application Data Flow<br/>'
             '┄▶ <b>Dashed Amber:</b> Asynchronous Pipeline Decoupling (RepNet)<br/>'
             '━▶ <b>Purple:</b> Client-Server Communication (REST & WebSocket)<br/>'
             '┄▶ <b>Dashed Slate:</b> Deployment / IaC Provisioning<br/>'
             '</span><br/>'
             '<b>Color Groupings:</b><br/>'
             '<span style="font-size:10px;">'
             '▫ <b style="color:#475569;">Slate Gray:</b> Video Input Sources<br/>'
             '▫ <b style="color:#0284c7;">Sky Blue:</b> FastAPI Video Ingestion & Workers<br/>'
             '▫ <b style="color:#d97706;">Amber:</b> Deep Learning Pipeline (Pose, TCN, RepNet)<br/>'
             '▫ <b style="color:#059669;">Emerald:</b> Relational Database (PostgreSQL)<br/>'
             '▫ <b style="color:#4f46e5;">Indigo:</b> React 19 Client SPA<br/>'
             '▫ <b style="color:#64748b;">Cloud Zone:</b> Google Cloud Platform Services'
             '</span><br/><br/>'
             '<b>Thesis Architectural Rationale:</b><br/>'
             '<span style="font-size:9.5px;color:#475569;line-height:1.4;">'
             '1. <b>Monocular RGB:</b> Pure single-camera input without requiring wearable IMUs or specialized depth sensors.<br/>'
             '2. <b>Bounded Queues:</b> Buffers video frames to prevent memory explosion and maintain real-time frame rates.<br/>'
             '3. <b>Async RepNet:</b> 3D temporal convolutions run out-of-band so video streaming never stutters.<br/>'
             '4. <b>In-Process Pipeline:</b> TCN and BlazePose execute inside worker threads to eliminate inter-process latency.'
             '</span>',
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#f8fafc;strokeColor=#cbd5e1;strokeWidth=1;align=left;spacingLeft=10;spacingTop=8;verticalAlign=top;fontSize=10;',
             20, 50, 340, 590, parent='c_legend')

    # -------------------------------------------------------------
    # 5. LAYER 5: DEPLOYMENT & CLOUD INFRASTRUCTURE (CONTAINER)
    # -------------------------------------------------------------
    add_node('c_lane5', '<b>LAYER 5: DEPLOYMENT & CLOUD INFRASTRUCTURE (Google Cloud Platform & IaC)</b>',
             'swimlane;startSize=28;horizontal=0;html=1;whiteSpace=wrap;fillColor=#fafafa;strokeColor=#64748b;strokeWidth=2;strokeDashed=1;rounded=1;fontStyle=1;fontSize=11;fontColor=#1e293b;container=1;collapsible=0;pointerEvents=0;',
             40, 770, 1850, 280, parent='1')

    inf_style = 'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#ffffff;strokeColor=#64748b;strokeWidth=1.5;align=center;fontSize=10;'

    add_node('inf_tf',
             '<b>Terraform (IaC)</b><br/><span style="font-size:9.5px;color:#475569;">Declarative HCL scripts<br/>Automates cloud provisioning</span>',
             inf_style, 30, 80, 180, 80, parent='c_lane5')

    add_node('inf_docker',
             '<b>Docker Containers</b><br/><span style="font-size:9.5px;color:#475569;">Container images for:<br/>• FastAPI Backend (Python)<br/>• React 19 Frontend (Nginx)</span>',
             inf_style, 240, 80, 210, 80, parent='c_lane5')

    # GCP Nested Sub-container
    add_node('c_gcp', '<b>Google Cloud Platform (GCP Environment)</b>',
             'swimlane;startSize=25;horizontal=0;html=1;whiteSpace=wrap;fillColor=#f8fafc;strokeColor=#475569;strokeWidth=1.8;rounded=1;fontStyle=1;fontSize=11;fontColor=#334155;container=1;collapsible=0;pointerEvents=0;',
             480, 40, 1340, 210, parent='c_lane5')

    add_node('inf_cr_be',
             '<b>Google Cloud Run (Backend)</b><br/><span style="font-size:9px;color:#0284c7;">Serverless container execution<br/>FastAPI server instance with WebSocket</span>',
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#e0f2fe;strokeColor=#0284c7;strokeWidth=1.5;align=center;fontSize=10;',
             40, 65, 270, 75, parent='c_gcp')

    add_node('inf_cr_fe',
             '<b>Google Cloud Run (Frontend)</b><br/><span style="font-size:9px;color:#4f46e5;">Serverless container execution<br/>Serves compiled React SPA assets</span>',
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#eef2ff;strokeColor=#4f46e5;strokeWidth=1.5;align=center;fontSize=10;',
             350, 65, 270, 75, parent='c_gcp')

    add_node('inf_vpc',
             '<b>Serverless VPC Access Connector</b><br/><span style="font-size:9px;color:#475569;">Private IP tunneling between Cloud Run and Cloud SQL</span>',
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#f1f5f9;strokeColor=#64748b;strokeWidth=1.2;align=center;fontSize=10;',
             660, 65, 280, 75, parent='c_gcp')

    add_node('inf_sql',
             '<b>Google Cloud SQL (PostgreSQL)</b><br/><span style="font-size:9px;color:#059669;">Fully managed relational database<br/>Private VPC subnet access only</span>',
             'shape=cylinder3;whiteSpace=wrap;html=1;size=12;fillColor=#d1fae5;strokeColor=#059669;strokeWidth=1.5;align=center;fontStyle=1;fontSize=10;',
             980, 50, 310, 100, parent='c_gcp')

    # -------------------------------------------------------------
    # EDGES & ROUTING (CLEAN ORTHOGONAL CONNECTIONS)
    # -------------------------------------------------------------
    # Base edge styles
    s_blue = 'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#0284c7;strokeWidth=1.8;fontSize=9;fontColor=#0369a1;labelBackgroundColor=#ffffff;'
    s_amber = 'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#d97706;strokeWidth=1.8;fontSize=9;fontColor=#b45309;labelBackgroundColor=#ffffff;'
    s_amber_dash = 'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#d97706;strokeWidth=1.8;strokeDashed=1;fontSize=9;fontColor=#b45309;labelBackgroundColor=#ffffff;'
    s_green = 'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#059669;strokeWidth=1.8;fontSize=9;fontColor=#047857;labelBackgroundColor=#ffffff;'
    s_purple = 'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#4f46e5;strokeWidth=1.8;fontSize=9;fontColor=#4338ca;labelBackgroundColor=#ffffff;'
    s_infra = 'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#64748b;strokeWidth=1.5;strokeDashed=1;fontSize=9;fontColor=#475569;labelBackgroundColor=#ffffff;'

    # 1. Inputs -> Factory (Distinct vertical x corridors to prevent crossing)
    add_edge('e1_rtsp', 'RTSP Stream', s_blue, 'in_rtsp', 'be_factory', exit_port=(1, 0.5), entry_port=(0, 0.5))
    add_edge('e1_webcam', 'Webcam Frames', s_blue, 'in_webcam', 'be_factory', waypoints=[(255, 372), (255, 172)], exit_port=(1, 0.5), entry_port=(0, 0.6))
    add_edge('e1_file', 'Video File Feed', s_blue, 'in_file', 'be_factory', waypoints=[(270, 562), (270, 172)], exit_port=(1, 0.5), entry_port=(0, 0.7))

    # 2. FastAPI Internal Video Pipeline
    add_edge('e2_fac_proc', 'Instantiated Adapter', s_blue, 'be_factory', 'be_processor', exit_port=(0.5, 1), entry_port=(0.5, 0))
    add_edge('e2_proc_q', 'Normalized Frames', s_blue, 'be_processor', 'be_queues', exit_port=(0.5, 1), entry_port=(0.5, 0))
    add_edge('e2_q_work', 'Dequeued Batch', s_blue, 'be_queues', 'be_workers', exit_port=(0.5, 1), entry_port=(0.5, 0))

    # 3. Workers -> AI Pipeline (Through vertical channel x=685 between Lane 2 & 3)
    add_edge('e3_work_pose', 'Frame Array', s_amber, 'be_workers', 'ai_pose', waypoints=[(470, 500), (680, 500), (680, 185)], exit_port=(1, 0.5), entry_port=(0, 0.5))
    add_edge('e3_work_repnet', 'Raw Video Frames (Async)', s_amber_dash, 'be_workers', 'ai_repnet', waypoints=[(470, 500), (690, 500), (690, 592)], exit_port=(1, 0.5), entry_port=(0, 0.5))

    # 4. Sequential AI Steps
    add_edge('e4_pose_feat', '33 Body Landmarks & BBox', s_amber, 'ai_pose', 'ai_feat', exit_port=(0.5, 1), entry_port=(0.5, 0))
    add_edge('e4_feat_tcn', '14 Joint Angles + 14 Visibilities', s_amber, 'ai_feat', 'ai_tcn', exit_port=(0.5, 1), entry_port=(0.5, 0))

    # 5. AI Predictions back to Backend Streaming & WS
    add_edge('e5_tcn_stream', '16-Class Probabilities', s_amber, 'ai_tcn', 'be_streaming', waypoints=[(715, 447), (715, 412)], exit_port=(0, 0.5), entry_port=(1, 0.5))
    add_edge('e5_repnet_ws', 'Repetition Count Updates', s_amber, 'ai_repnet', 'be_ws', waypoints=[(715, 592), (715, 532)], exit_port=(0, 0.5), entry_port=(1, 0.5))
    add_edge('e5_stream_ws', 'Annotated JPEG Frames', s_blue, 'be_streaming', 'be_ws', exit_port=(0.5, 1), entry_port=(0.5, 0))

    # 6. Database Connections (Clear top corridor y=70 under header)
    add_edge('e6_rest_db', 'SQL Queries (Plans & Routines)', s_green, 'be_rest', 'db_pg', waypoints=[(645, 172), (665, 172), (665, 72), (1110, 72), (1110, 160)], exit_port=(1, 0.5), entry_port=(0, 0.5))
    add_edge('e6_work_log', 'Auto-log Completed Sets', s_green, 'be_workers', 'db_logs', waypoints=[(460, 520), (460, 755), (1105, 755), (1105, 317)], exit_port=(1, 0.7), entry_port=(0, 0.5))

    # 7. Frontend <-> Backend Dual Channels
    add_edge('e7_ws', 'WebSocket (Live Stream & Real-time Predictions)', s_purple, 'be_ws', 'fe_stack', waypoints=[(645, 532), (670, 532), (670, 765), (1115, 765), (1115, 470)], exit_port=(1, 0.7), entry_port=(0, 0.5))
    add_edge('e7_rest', 'REST API (CRUD Plans, Logs, Admin via HTTP)', s_purple, 'be_rest', 'fe_stack', waypoints=[(645, 160), (675, 160), (675, 745), (1100, 745), (1100, 455)], exit_port=(1, 0.4), entry_port=(0, 0.3))

    # 8. Infrastructure Connections (Layer 5)
    add_edge('e8_tf', 'Provisions Cloud Resources via HCL', s_infra, 'inf_tf', 'c_gcp', exit_port=(1, 0.5), entry_port=(0, 0.5))
    add_edge('e8_dkr_be', 'Builds & Deploys Backend Image', s_infra, 'inf_docker', 'inf_cr_be', waypoints=[(450, 930), (510, 930), (510, 912)], exit_port=(1, 0.5), entry_port=(0, 0.5))
    add_edge('e8_dkr_fe', 'Builds & Deploys Frontend Image', s_infra, 'inf_docker', 'inf_cr_fe', waypoints=[(450, 930), (465, 930), (465, 820), (820, 820), (820, 912)], exit_port=(1, 0.5), entry_port=(0, 0.5))
    add_edge('e8_run_vpc', 'Secure Tunnel', s_infra, 'inf_cr_be', 'inf_vpc', exit_port=(1, 0.5), entry_port=(0, 0.5))
    add_edge('e8_vpc_sql', 'Private IP Connection', s_infra, 'inf_vpc', 'inf_sql', exit_port=(1, 0.5), entry_port=(0, 0.5))

    # Save to file
    tree = ET.ElementTree(root)
    ET.indent(tree, space='  ', level=0)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)
    print(f"Generated clean Draw.io architecture file: {file_path}")

if __name__ == '__main__':
    build_perfect_drawio('AS_IS_Thesis_Architecture.drawio')
