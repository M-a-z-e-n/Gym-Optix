import xml.etree.ElementTree as ET

def create_thesis_architecture_drawio(file_path):
    root = ET.Element('mxfile', host='app.diagrams.net', modified='2026-10-29', agent='GymOptix', version='24.0.0')
    diagram = ET.SubElement(root, 'diagram', name='AS-IS Thesis Architecture', id='thesis_asis_001')
    model = ET.SubElement(diagram, 'mxGraphModel', dx='2000', dy='1200', grid='1', gridSize='10', guides='1', tooltips='1', connect='1', arrows='1', fold='1', page='1', pageScale='1', pageWidth='2050', pageHeight='1180', math='0', shadow='1')
    root_cell = ET.SubElement(model, 'root')
    ET.SubElement(root_cell, 'mxCell', id='0')
    ET.SubElement(root_cell, 'mxCell', id='1', parent='0')

    def add_cell(cid, val, style, x, y, w, h, parent='1', vertex=1):
        c = ET.SubElement(root_cell, 'mxCell', id=str(cid), parent=str(parent), style=style, value=val, vertex=str(vertex))
        geo = ET.SubElement(c, 'mxGeometry', x=str(x), y=str(y), width=str(w), height=str(h))
        geo.set('as', 'geometry')
        return c

    def add_edge(eid, val, style, src, tgt, pts=None, parent='1'):
        c = ET.SubElement(root_cell, 'mxCell', id=str(eid), parent=str(parent), style=style, value=val, edge='1', source=str(src), target=str(tgt))
        geo = ET.SubElement(c, 'mxGeometry', relative='1')
        geo.set('as', 'geometry')
        if pts:
            arr = ET.SubElement(geo, 'Array')
            arr.set('as', 'points')
            for px, py in pts:
                ET.SubElement(arr, 'mxPoint', x=str(px), y=str(py))
        return c

    # ==========================================
    # 0. TITLE HEADER
    # ==========================================
    add_cell('title_banner',
             '<b style="font-size:18px;letter-spacing:0.5px;">AS-IS Architecture — Real-Time Exercise Recognition and Repetition Counting System</b><br/>'
             '<span style="font-size:12px;color:#475569;">Baseline Monocular Gym Video Pipeline | Master\'s Thesis Architecture (N. I. Cridlig)</span>',
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#F8FAFC;strokeColor=#475569;strokeWidth=1.5;shadow=1;align=center;',
             30, 20, 1980, 55)

    # ==========================================
    # 1. LAYER CONTAINERS (SWIMLANES / BOUNDARIES)
    # ==========================================
    # Layer 1: Video Input Sources
    add_cell('lane_inputs',
             '<b>LAYER 1: VIDEO INPUT SOURCES</b>',
             'swimlane;startSize=28;horizontal=0;html=1;whiteSpace=wrap;fillColor=#F1F5F9;strokeColor=#64748B;strokeWidth=1.8;rounded=1;fontStyle=1;fontSize=11;fontColor=#334155;',
             30, 95, 220, 680)

    # Layer 2: FastAPI Backend
    add_cell('lane_backend',
             '<b>LAYER 2: BACKEND & VIDEO PROCESSING (FastAPI)</b>',
             'swimlane;startSize=28;horizontal=0;html=1;whiteSpace=wrap;fillColor=#F0F9FF;strokeColor=#0284C7;strokeWidth=2;rounded=1;fontStyle=1;fontSize=11;fontColor=#0369A1;',
             270, 95, 430, 680)

    # Layer 3: AI Processing Pipeline
    add_cell('lane_ai',
             '<b>LAYER 3: AI PROCESSING PIPELINE (Embedded Models)</b>',
             'swimlane;startSize=28;horizontal=0;html=1;whiteSpace=wrap;fillColor=#FFFBEB;strokeColor=#D97706;strokeWidth=2;rounded=1;fontStyle=1;fontSize=11;fontColor=#B45309;',
             720, 95, 450, 680)

    # Layer 4A: Database Layer
    add_cell('lane_db',
             '<b>LAYER 4A: DATA STORAGE</b>',
             'swimlane;startSize=28;horizontal=0;html=1;whiteSpace=wrap;fillColor=#ECFDF5;strokeColor=#059669;strokeWidth=2;rounded=1;fontStyle=1;fontSize=11;fontColor=#047857;',
             1190, 95, 380, 290)

    # Layer 4B: React Frontend
    add_cell('lane_frontend',
             '<b>LAYER 4B: FRONTEND APPLICATION (React 19)</b>',
             'swimlane;startSize=28;horizontal=0;html=1;whiteSpace=wrap;fillColor=#EEF2FF;strokeColor=#4F46E5;strokeWidth=2;rounded=1;fontStyle=1;fontSize=11;fontColor=#4338CA;',
             1190, 405, 380, 370)

    # Legend Container (Top-Right)
    add_cell('lane_legend',
             '<b>ARCHITECTURE LEGEND</b>',
             'swimlane;startSize=28;horizontal=0;html=1;whiteSpace=wrap;fillColor=#FFFFFF;strokeColor=#94A3B8;strokeWidth=1.5;rounded=1;fontStyle=1;fontSize=11;fontColor=#334155;',
             1590, 95, 420, 680)

    # Layer 5: Deployment & Infrastructure Zone
    add_cell('lane_infra',
             '<b>LAYER 5: DEPLOYMENT & CLOUD INFRASTRUCTURE (Google Cloud Platform & IaC)</b>',
             'swimlane;startSize=28;horizontal=0;html=1;whiteSpace=wrap;fillColor=#FAFAFA;strokeColor=#64748B;strokeWidth=2;strokeDashed=1;rounded=1;fontStyle=1;fontSize=12;fontColor=#1E293B;',
             30, 800, 1980, 240)

    # ==========================================
    # LAYER 1: VIDEO INPUT COMPONENTS
    # ==========================================
    input_style = 'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#FFFFFF;strokeColor=#64748B;strokeWidth=1.5;align=center;'

    add_cell('in_rtsp',
             '<b>RTSP IP Camera</b><br/><span style="font-size:10px;color:#475569;">• Monocular ceiling/wall gym cam<br/>• Real-time RTSP H.264 stream<br/>• Low latency protocol</span>',
             input_style, 70, 150, 160, 85)

    add_cell('in_webcam',
             '<b>Browser Webcam</b><br/><span style="font-size:10px;color:#475569;">• Client user device camera<br/>• HTML5 getUserMedia stream<br/>• Uploaded via WebSocket</span>',
             input_style, 70, 330, 160, 85)

    add_cell('in_file',
             '<b>Video File</b><br/><span style="font-size:10px;color:#475569;">• Pre-recorded benchmark video<br/>• MP4 / AVI local or remote<br/>• Offline testing & evaluation</span>',
             input_style, 70, 510, 160, 85)

    # ==========================================
    # LAYER 2: FASTAPI BACKEND COMPONENTS
    # ==========================================
    be_comp_style = 'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#FFFFFF;strokeColor=#0284C7;strokeWidth=1.5;align=center;'

    add_cell('be_factory',
             '<b>Video Source Factory</b><br/><span style="font-size:9.5px;color:#0369A1;">Selects, initializes & instantiates<br/>appropriate input adapter (RTSP/Webcam/File)</span>',
             be_comp_style, 310, 150, 180, 65)

    add_cell('be_frame_proc',
             '<b>Frame Processor</b><br/><span style="font-size:9.5px;color:#0369A1;">Frame ingestion, resolution normalization,<br/>colorspace conversion (BGR → RGB)</span>',
             be_comp_style, 310, 260, 180, 65)

    add_cell('be_queues',
             '<b>Bounded Frame Queues</b><br/><span style="font-size:9.5px;color:#0369A1;">Thread-safe memory buffers<br/>Prevents latency buildup & frame drop</span>',
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#E0F2FE;strokeColor=#0284C7;strokeWidth=1.5;align=center;',
             310, 370, 180, 60)

    add_cell('be_workers',
             '<b>Asynchronous Workers</b><br/><span style="font-size:9.5px;color:#0369A1;">Background asyncio/threading workers<br/>Drives AI pipeline execution</span>',
             be_comp_style, 310, 475, 180, 65)

    add_cell('be_streaming',
             '<b>Frame Streaming & Processing</b><br/><span style="font-size:9.5px;color:#0369A1;">Overlays landmarks & predictions<br/>Encodes JPEG frame stream for client</span>',
             be_comp_style, 510, 370, 175, 75)

    add_cell('be_ws',
             '<b>WebSocket Communication</b><br/><span style="font-size:9.5px;color:#0369A1;">Bidirectional real-time channel<br/>Streaming annotated frames & live counts</span>',
             be_comp_style, 510, 530, 175, 70)

    add_cell('be_rest',
             '<b>REST API Endpoints</b><br/><span style="font-size:9.5px;color:#0369A1;">FastAPI Routers: <code>/plans</code>, <code>/logs</code><br/>CRUD for exercise plans & workout history</span>',
             be_comp_style, 510, 210, 175, 70)

    # ==========================================
    # LAYER 3: AI PROCESSING PIPELINE COMPONENTS
    # ==========================================
    ai_box_style = 'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#FFFFFF;strokeColor=#D97706;strokeWidth=1.5;align=center;'

    add_cell('ai_stage1',
             '<b>1. Pose Estimation</b><br/>'
             '<span style="font-size:10px;color:#92400E;"><b>MediaPipe / BlazePose</b></span><br/>'
             '<span style="font-size:9.5px;color:#475569;">• Extracts 33 3D body landmarks (x,y,z)<br/>• Generates subject Bounding Box<br/>• Real-time per-frame inference</span>',
             ai_box_style, 760, 140, 370, 85)

    add_cell('ai_stage2',
             '<b>2. Feature Engineering</b><br/>'
             '<span style="font-size:9.5px;color:#475569;">• Calculates <b>14 Joint Angles</b> (Elbows, Knees, Hips, Shoulders)<br/>'
             '• Calculates <b>14 Landmark Visibility Scores</b><br/>'
             '• Vectorizes spatio-temporal kinematic features</span>',
             ai_box_style, 760, 260, 370, 80)

    add_cell('ai_stage3',
             '<b>3. Exercise Classification</b><br/>'
             '<span style="font-size:10px;color:#92400E;"><b>Temporal Convolutional Network (TCN)</b></span><br/>'
             '<span style="font-size:9.5px;color:#475569;">• Processes temporal sliding windows of joint angles<br/>'
             '• <b>Classifies 16 Exercise Categories</b> (Squat, Deadlift, Bench...)<br/>'
             '• Synchronous classification output</span>',
             ai_box_style, 760, 375, 370, 95)

    add_cell('ai_stage4',
             '<b>4. Repetition Counting (Asynchronous)</b><br/>'
             '<span style="font-size:10px;color:#B45309;"><b>RepNet (Temporal Self-Similarity Network)</b></span><br/>'
             '<span style="font-size:9.5px;color:#475569;">• Processes raw video frame sequences<br/>'
             '• Evaluates periodic motion & temporal similarity matrix<br/>'
             '• <b>Runs Asynchronously</b> to prevent blocking real-time stream</span>',
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#FEF3C7;strokeColor=#D97706;strokeWidth=2;align=center;',
             760, 520, 370, 100)

    add_cell('ai_note',
             '<i style="font-size:9px;color:#78350F;">Note: Models run as embedded in-process pipeline stages within backend execution, NOT standalone microservices.</i>',
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#FFFDF5;strokeColor=#FDE68A;strokeWidth=1;align=center;',
             760, 640, 370, 35)

    # ==========================================
    # LAYER 4A: DATABASE (POSTGRESQL / CLOUD SQL)
    # ==========================================
    db_style = 'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#FFFFFF;strokeColor=#059669;strokeWidth=1.5;align=center;'

    add_cell('db_pg',
             '<b>PostgreSQL Relational Database</b><br/><span style="font-size:9.5px;color:#047857;">Managed in Cloud via Google Cloud SQL</span>',
             'shape=cylinder;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#D1FAE5;strokeColor=#059669;strokeWidth=1.5;align=center;fontStyle=1;',
             1220, 140, 320, 65)

    add_cell('db_tbl_plans',
             '<b>Table: <code>exercise_plan</code></b><br/><span style="font-size:9.5px;color:#475569;">Stores scheduled workouts, target sets, reps, and exercise categories</span>',
             db_style, 1220, 220, 320, 65)

    add_cell('db_tbl_logs',
             '<b>Table: <code>log</code></b><br/><span style="font-size:9.5px;color:#475569;">Stores completed set logs, timestamps, counted reps, and recognized exercise IDs</span>',
             db_style, 1220, 300, 320, 65)

    # ==========================================
    # LAYER 4B: REACT 19 FRONTEND APPLICATION
    # ==========================================
    fe_style = 'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#FFFFFF;strokeColor=#4F46E5;strokeWidth=1.5;align=center;'

    add_cell('fe_stack',
             '<b>React 19 Application Stack</b><br/><span style="font-size:9.5px;color:#4338CA;">Bootstrap 5 • React Router 7 • Custom Hook: <code>useWebSocket.js</code></span>',
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#E0E7FF;strokeColor=#4F46E5;strokeWidth=1.5;align=center;',
             1220, 445, 320, 50)

    add_cell('fe_pages',
             '<b>Frontend Application Routes:</b><br/>'
             '<span style="font-size:9.5px;color:#334155;line-height:1.4;">'
             '• <code>/</code> : Main Application Page<br/>'
             '• <code>/user</code> : User Interface & Personal Workout View<br/>'
             '• <code>/admin</code> : Administration & System Configuration<br/>'
             '• <code>/demo</code> : Live Demonstration & Testing View'
             '</span>',
             fe_style, 1220, 510, 320, 95)

    add_cell('fe_features',
             '<b>Client UI Capabilities:</b><br/>'
             '<span style="font-size:9.5px;color:#334155;">'
             '• Live Video Display with Pose Skeletal Overlay<br/>'
             '• Real-Time Exercise Recognition Display<br/>'
             '• Asynchronous Repetition Count Badge & Progress<br/>'
             '• Historical Workout Logs & Exercise Plan Controls'
             '</span>',
             fe_style, 1220, 620, 320, 115)

    # ==========================================
    # ARCHITECTURE LEGEND BOX (TOP-RIGHT)
    # ==========================================
    add_cell('legend_content',
             '<b>Diagram Semantics & Conventions</b><br/><br/>'
             '<b>Arrow Types:</b><br/>'
             '<span style="font-size:10px;color:#1E293B;">'
             '━━━▶ <b>Solid Arrow:</b> Runtime Application Data Flow<br/>'
             ' - - - ▶ <b>Dashed Arrow:</b> Deployment / IaC Provisioning<br/>'
             '⮂⮂⮂▶ <b>Dual Direction:</b> Bidirectional Socket / REST Call<br/>'
             '</span><br/>'
             '<b>Layer Color Scheme:</b><br/>'
             '<span style="font-size:10px;">'
             '◽ <b style="color:#64748B;">Slate:</b> Video Input Sources<br/>'
             '◽ <b style="color:#0284C7;">Sky Blue:</b> FastAPI Backend Processing<br/>'
             '◽ <b style="color:#D97706;">Amber:</b> AI / Deep Learning Pipeline<br/>'
             '◽ <b style="color:#059669;">Emerald:</b> Relational Database Tier<br/>'
             '◽ <b style="color:#4F46E5;">Indigo:</b> React 19 Frontend Client<br/>'
             '◽ <b style="color:#475569;">Dashed Gray:</b> GCP Infrastructure & Deployment'
             '</span><br/><br/>'
             '<b>Key Thesis Highlights:</b><br/>'
             '<span style="font-size:9.5px;color:#475569;">'
             '• <b>Monocular RGB Only:</b> No wearable IMUs or depth sensors.<br/>'
             '• <b>Asynchronous RepNet:</b> Prevents video stuttering while counting reps.<br/>'
             '• <b>In-Process AI Pipeline:</b> Models run inside worker threads to minimize inter-service overhead.'
             '</span>',
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#F8FAFC;strokeColor=#CBD5E1;strokeWidth=1.2;align=left;spacingLeft=12;spacingTop=10;verticalAlign=top;',
             1630, 140, 360, 595)

    # ==========================================
    # LAYER 5: DEPLOYMENT & CLOUD INFRASTRUCTURE
    # ==========================================
    infra_style = 'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#FFFFFF;strokeColor=#64748B;strokeWidth=1.5;align=center;'

    add_cell('inf_terraform',
             '<b>Terraform (IaC)</b><br/><span style="font-size:9.5px;color:#475569;">Declarative HCL scripts<br/>Automated infrastructure provisioning</span>',
             infra_style, 70, 880, 190, 80)

    add_cell('inf_docker',
             '<b>Docker Containers</b><br/><span style="font-size:9.5px;color:#475569;">Multi-stage build images for:<br/>• FastAPI Backend (Python 3.10+)<br/>• React 19 Frontend (Node/Nginx)</span>',
             infra_style, 300, 880, 230, 80)

    add_cell('inf_gcp_box',
             '<b>Google Cloud Platform (GCP Environment)</b>',
             'swimlane;startSize=25;horizontal=0;html=1;whiteSpace=wrap;fillColor=#F8FAFC;strokeColor=#475569;strokeWidth=1.8;rounded=1;fontStyle=1;fontSize=11;fontColor:#334155;',
             570, 840, 1420, 175)

    add_cell('inf_cloud_run_be',
             '<b>Google Cloud Run (Backend)</b><br/><span style="font-size:9.5px;color:#0284C7;">Serverless container execution<br/>FastAPI server instance with WebSocket support</span>',
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#E0F2FE;strokeColor=#0284C7;strokeWidth=1.5;align=center;',
             620, 885, 270, 75)

    add_cell('inf_cloud_run_fe',
             '<b>Google Cloud Run (Frontend)</b><br/><span style="font-size:9.5px;color:#4F46E5;">Serverless container execution<br/>Serves compiled React SPA assets</span>',
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#EEF2FF;strokeColor=#4F46E5;strokeWidth=1.5;align=center;',
             930, 885, 260, 75)

    add_cell('inf_vpc',
             '<b>Serverless VPC Access Connector</b><br/><span style="font-size:9.5px;color:#475569;">Private IP tunneling between Cloud Run and Cloud SQL</span>',
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#F1F5F9;strokeColor=#64748B;strokeWidth=1.2;align=center;',
             1230, 885, 270, 75)

    add_cell('inf_cloud_sql',
             '<b>Google Cloud SQL (PostgreSQL)</b><br/><span style="font-size:9.5px;color:#059669;">Fully managed relational database<br/>Private VPC subnet access only</span>',
             'shape=cylinder;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#D1FAE5;strokeColor=#059669;strokeWidth=1.5;align=center;fontStyle=1;',
             1540, 875, 260, 95)

    # ==========================================
    # CONNECTING EDGES & DATA FLOW
    # ==========================================
    edge_app = 'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#0284C7;strokeWidth=1.8;fontSize=9;fontColor=#0369A1;'
    edge_ai = 'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#D97706;strokeWidth=1.8;fontSize=9;fontColor=#B45309;'
    edge_db = 'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#059669;strokeWidth=1.8;fontSize=9;fontColor=#047857;'
    edge_fe = 'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#4F46E5;strokeWidth=1.8;fontSize=9;fontColor=#4338CA;'
    edge_infra = 'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#64748B;strokeWidth=1.5;strokeDashed=1;fontSize=9;fontColor=#475569;'

    # 1. Inputs to Factory / Processor
    add_edge('e_rtsp_fac', 'RTSP Stream', edge_app, 'in_rtsp', 'be_factory')
    add_edge('e_webcam_fac', 'Webcam Frames', edge_app, 'in_webcam', 'be_factory')
    add_edge('e_file_fac', 'File Stream', edge_app, 'in_file', 'be_factory')

    # 2. Factory to Processor to Queues to Workers
    add_edge('e_fac_proc', 'Instantiated Stream', edge_app, 'be_factory', 'be_frame_proc')
    add_edge('e_proc_q', 'Raw Frames', edge_app, 'be_frame_proc', 'be_queues')
    add_edge('e_q_work', 'Dequeued Batch', edge_app, 'be_queues', 'be_workers')

    # 3. Workers to AI Pipeline
    add_edge('e_work_pose', 'Frame Array', edge_ai, 'be_workers', 'ai_stage1', [(500, 510), (500, 180), (760, 180)])

    # 4. Sequential AI Pipeline (Pose -> Features -> TCN)
    add_edge('e_pose_feat', '33 Landmarks & BBox', edge_ai, 'ai_stage1', 'ai_stage2')
    add_edge('e_feat_tcn', '14 Angles + 14 Visibilities', edge_ai, 'ai_stage2', 'ai_stage3')

    # 5. Asynchronous RepNet Branch
    add_edge('e_work_repnet', 'Raw Video Frames (Async)', edge_ai, 'be_workers', 'ai_stage4', [(500, 510), (500, 570), (760, 570)])

    # 6. AI Results back to Frame Streaming & WebSocket
    add_edge('e_tcn_stream', '16-Class Probabilities', edge_ai, 'ai_stage3', 'be_streaming', [(760, 420), (700, 420), (685, 410)])
    add_edge('e_repnet_stream', 'Repetition Count Updates', edge_ai, 'ai_stage4', 'be_ws', [(760, 580), (700, 580), (685, 570)])
    add_edge('e_stream_ws', 'Annotated Frames', edge_app, 'be_streaming', 'be_ws')

    # 7. Backend to Database (REST API / Worker to PostgreSQL)
    add_edge('e_be_db_sql', 'SQL Read / Write (Plans & Logs)', edge_db, 'be_rest', 'db_pg')
    add_edge('e_work_log_db', 'Auto-log Sets & Reps', edge_db, 'be_workers', 'db_tbl_logs', [(500, 520), (500, 750), (1160, 750), (1160, 335), (1220, 335)])

    # 8. React Frontend <--> FastAPI Backend Communication
    add_edge('e_fe_ws', 'WebSocket (Live Stream, Landmark Overlays, Real-Time Predictions)', edge_fe, 'be_ws', 'fe_stack', [(695, 560), (1150, 560), (1150, 470), (1220, 470)])
    add_edge('e_fe_rest', 'REST API (CRUD Plans, History, Configs via HTTP)', edge_fe, 'be_rest', 'fe_stack', [(695, 245), (1170, 245), (1170, 460), (1220, 460)])

    # 9. Deployment Relationships (Layer 5)
    add_edge('e_tf_infra', 'Provisions Cloud Resources via HCL', edge_infra, 'inf_terraform', 'inf_gcp_box')
    add_edge('e_dkr_be', 'Builds & Deploys Backend Image', edge_infra, 'inf_docker', 'inf_cloud_run_be')
    add_edge('e_dkr_fe', 'Builds & Deploys Frontend Image', edge_infra, 'inf_docker', 'inf_cloud_run_fe', [(415, 870), (415, 850), (1060, 850), (1060, 885)])
    add_edge('e_run_vpc', 'Secure Tunnel', edge_infra, 'inf_cloud_run_be', 'inf_vpc')
    add_edge('e_vpc_sql', 'Cloud SQL Connection', edge_infra, 'inf_vpc', 'inf_cloud_sql')

    # 10. Vertical Mapping between Application Layers and Cloud Infrastructure (Dashed anchors)
    add_edge('e_be_run_map', 'Hosted on Cloud Run', edge_infra, 'be_frame_proc', 'inf_cloud_run_be', [(400, 330), (280, 330), (280, 830), (750, 830), (750, 885)])
    add_edge('e_db_sql_map', 'Managed by Cloud SQL', edge_infra, 'db_pg', 'inf_cloud_sql', [(1380, 210), (1380, 385), (1560, 385), (1560, 875)])
    add_edge('e_fe_run_map', 'Hosted on Cloud Run', edge_infra, 'fe_stack', 'inf_cloud_run_fe', [(1380, 500), (1380, 780), (1060, 780), (1060, 885)])

    # Write output file
    tree = ET.ElementTree(root)
    ET.indent(tree, space='  ', level=0)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)
    print(f'Successfully generated {file_path}')

if __name__ == '__main__':
    create_thesis_architecture_drawio('AS_IS_Thesis_Architecture.drawio')

