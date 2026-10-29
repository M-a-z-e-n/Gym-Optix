import xml.etree.ElementTree as ET

def generate_spacious_drawio(file_path):
    root = ET.Element('mxfile', host='app.diagrams.net', modified='2026-10-29', agent='drawio-skill', version='24.0.0')
    diagram = ET.SubElement(root, 'diagram', name='AS-IS High-Level Architecture (Spacious)', id='asis_spacious')
    model = ET.SubElement(diagram, 'mxGraphModel', dx='2200', dy='1100', grid='1', gridSize='10', guides='1', tooltips='1', connect='1', arrows='1', fold='1', page='1', pageScale='1', pageWidth='2200', pageHeight='1100', math='0', shadow='0')
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
             '<b style="font-size:19px;color:#0f172a;letter-spacing:0.5px;">AS-IS System Architecture — High-Level Conceptual Overview</b><br/>'
             '<span style="font-size:12px;color:#475569;">Real-Time Exercise Recognition and Repetition Counting System (Nicolas Ivan Cridlig Master\'s Thesis)</span>',
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=none;strokeColor=#1e293b;strokeWidth=1.8;align=center;',
             60, 20, 2080, 60, parent='1')

    # Common Hollow/Transparent Styles
    box_style = 'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=none;strokeColor=#0f172a;strokeWidth=1.8;align=center;fontSize=11;fontColor=#0f172a;'
    box_dashed = 'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=none;strokeColor=#475569;strokeWidth=1.8;strokeDashed=1;align=center;fontSize=11;fontColor=#0f172a;'
    lane_style = 'swimlane;startSize=30;horizontal=0;html=1;whiteSpace=wrap;fillColor=none;strokeColor=#334155;strokeWidth=2;rounded=1;fontStyle=1;fontSize=12;fontColor=#0f172a;container=1;collapsible=0;pointerEvents=0;'

    # -------------------------------------------------------------
    # 1. TIER 1: VIDEO INPUT SOURCES (Width: 280)
    # -------------------------------------------------------------
    add_node('t1_lane', '<b>TIER 1: VIDEO INPUT SOURCES</b>',
             lane_style, 60, 105, 280, 635, parent='1')

    add_node('in_rtsp',
             '<b>RTSP IP Camera</b><br/><span style="font-size:10px;color:#475569;">• Fixed ceiling/wall gym surveillance<br/>• Monocular H.264 RTSP feed</span>',
             box_style, 30, 70, 220, 95, parent='t1_lane')

    add_node('in_webcam',
             '<b>Browser Webcam</b><br/><span style="font-size:10px;color:#475569;">• Athlete personal user device<br/>• HTML5 getUserMedia live feed</span>',
             box_style, 30, 240, 220, 95, parent='t1_lane')

    add_node('in_file',
             '<b>Recorded Video File</b><br/><span style="font-size:10px;color:#475569;">• Offline MP4 / AVI benchmarks<br/>• Repeatable research validation</span>',
             box_style, 30, 410, 220, 95, parent='t1_lane')

    # -------------------------------------------------------------
    # 2. TIER 2: FASTAPI BACKEND (Width: 360, Gap from Tier 1: 90px)
    # -------------------------------------------------------------
    add_node('t2_lane', '<b>TIER 2: BACKEND & STREAMING ENGINE (FastAPI)</b>',
             lane_style, 430, 105, 360, 635, parent='1')

    add_node('be_factory',
             '<b>Video Source Factory</b><br/><span style="font-size:10px;color:#475569;">Adapter Selection & Ingestion Lifecycle</span>',
             box_style, 30, 65, 300, 80, parent='t2_lane')

    add_node('be_pipeline',
             '<b>Frame Preprocessor & Bounded Queues</b><br/><span style="font-size:10px;color:#475569;">Resize, BGR➔RGB, and Flow Backpressure Buffer</span>',
             box_style, 30, 190, 300, 80, parent='t2_lane')

    add_node('be_workers',
             '<b>Asynchronous Worker Pool</b><br/><span style="font-size:10px;color:#475569;">Multi-threaded In-Process AI Task Dispatcher</span>',
             box_style, 30, 315, 300, 80, parent='t2_lane')

    add_node('be_gateway',
             '<b>Communication Gateway</b><br/><span style="font-size:10px;color:#475569;">WebSocket Hub & REST API Controller</span>',
             box_style, 30, 440, 300, 85, parent='t2_lane')

    # -------------------------------------------------------------
    # 3. TIER 3: CORE AI PIPELINE (Width: 390, Gap from Tier 2: 90px)
    # -------------------------------------------------------------
    add_node('t3_lane', '<b>TIER 3: AI PROCESSING PIPELINE (In-Process Models)</b>',
             lane_style, 880, 105, 390, 635, parent='1')

    add_node('ai_pose',
             '<b>1. Pose Estimation (MediaPipe)</b><br/><span style="font-size:10px;color:#475569;">Extracts 33 3D Keypoints & Bounding Box</span>',
             box_style, 30, 65, 330, 85, parent='t3_lane')

    add_node('ai_feat',
             '<b>2. Feature Engineering</b><br/><span style="font-size:10px;color:#475569;">Computes 14 Joint Angles & 14 Visibility Scores</span>',
             box_style, 30, 185, 330, 85, parent='t3_lane')

    add_node('ai_tcn',
             '<b>3. Exercise Classification (TCN)</b><br/><span style="font-size:10px;color:#475569;">Temporal Convolutional Net (16 Exercise Categories)</span>',
             box_style, 30, 305, 330, 90, parent='t3_lane')

    add_node('ai_repnet',
             '<b>4. Repetition Counting (RepNet)</b><br/><span style="font-size:10px;color:#475569;">Temporal Self-Similarity Network <i>[Runs Asynchronously]</i></span>',
             box_dashed, 30, 430, 330, 95, parent='t3_lane')

    add_node('ai_note',
             '<i style="font-size:9.5px;color:#64748b;">Note: In-process models avoid serialization overhead (not standalone microservices)</i>',
             'shape=rectangle;rounded=0;html=1;whiteSpace=wrap;fillColor=none;strokeColor=none;align=center;',
             30, 555, 330, 40, parent='t3_lane')

    # -------------------------------------------------------------
    # 4. TIER 4: STORAGE & CLIENT (Width: 440, Gap from Tier 3: 90px)
    # -------------------------------------------------------------
    add_node('t4_lane', '<b>TIER 4: STORAGE & APPLICATION CLIENT</b>',
             lane_style, 1360, 105, 440, 635, parent='1')

    add_node('db_box',
             '<b>PostgreSQL Relational Database (Cloud SQL)</b><br/>'
             '<span style="font-size:10.5px;color:#475569;line-height:1.5;">'
             '• <b><code>exercise_plan</code> Table:</b> Workout routines, planned sets, reps<br/>'
             '• <b><code>log</code> Table:</b> Completed workout records, detected IDs, timestamps'
             '</span>',
             box_style, 30, 65, 380, 150, parent='t4_lane')

    add_node('fe_box',
             '<b>React 19 Frontend Client (Web SPA)</b><br/>'
             '<span style="font-size:10.5px;color:#475569;line-height:1.5;">'
             '• Bootstrap 5 • React Router 7 • <code>useWebSocket.js</code><br/>'
             '• <b>Client Routes:</b> <code>/</code> (Main), <code>/user</code>, <code>/admin</code>, <code>/demo</code><br/>'
             '• <b>Features:</b> Live Video Stream + Skeletal Pose Overlay,<br/>'
             '  Real-time Exercise Classification, Repetition Count Badge'
             '</span>',
             box_style, 30, 265, 380, 250, parent='t4_lane')

    # -------------------------------------------------------------
    # LEGEND BOX (Width: 280, Gap from Tier 4: 60px)
    # -------------------------------------------------------------
    add_node('legend_lane', '<b>DIAGRAM LEGEND & DATAFLOW</b>',
             lane_style, 1860, 105, 280, 635, parent='1')

    add_node('legend_content',
             '<b>Arrow Semantics:</b><br/><br/>'
             '<span style="font-size:10px;line-height:1.6;">'
             '━━━▶ <b>Solid Line:</b><br/>'
             'Direct Runtime Data Flow<br/><br/>'
             '┄ ┄ ┄▶ <b>Dashed Line:</b><br/>'
             'Asynchronous Decoupled Flow<br/>'
             'or Cloud Deployment Link<br/><br/>'
             '⮂ ⮂ ⮂▶ <b>Dual Direction:</b><br/>'
             'Bidirectional Socket / REST Call'
             '</span><br/><br/>'
             '<b>Design Attributes:</b><br/>'
             '<span style="font-size:10px;color:#475569;line-height:1.5;">'
             '• <b>Hollow Style:</b> Clean, transparent academic presentation.<br/>'
             '• <b>Corridors:</b> 90px spacing prevents line overlaps.<br/>'
             '• <b>Label Badges:</b> Dataflow labels sit on white bordered badges for maximum legibility.'
             '</span>',
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=none;strokeColor=#cbd5e1;strokeWidth=1;align=left;spacingLeft=12;spacingTop=10;verticalAlign=top;fontSize=10;',
             20, 55, 240, 550, parent='legend_lane')

    # -------------------------------------------------------------
    # 5. TIER 5: DEPLOYMENT & CLOUD (Bottom Lane: Width: 2080)
    # -------------------------------------------------------------
    add_node('t5_lane', '<b>TIER 5: CLOUD DEPLOYMENT & INFRASTRUCTURE (Google Cloud Platform & IaC)</b>',
             'swimlane;startSize=28;horizontal=0;html=1;whiteSpace=wrap;fillColor=none;strokeColor=#475569;strokeWidth=2;strokeDashed=1;rounded=1;fontStyle=1;fontSize=12;fontColor=#0f172a;container=1;collapsible=0;pointerEvents=0;',
             60, 775, 2080, 265, parent='1')

    add_node('inf_tf',
             '<b>Terraform (IaC)</b><br/><span style="font-size:10px;color:#475569;">Declarative HCL Scripts<br/>Cloud Provisioning</span>',
             box_style, 40, 80, 230, 95, parent='t5_lane')

    add_node('inf_docker',
             '<b>Docker Containers</b><br/><span style="font-size:10px;color:#475569;">Multi-stage Images for<br/>FastAPI & React Frontend</span>',
             box_style, 330, 80, 250, 95, parent='t5_lane')

    add_node('inf_cr_be',
             '<b>Cloud Run (Backend)</b><br/><span style="font-size:10px;color:#475569;">Serverless Container for<br/>FastAPI with WebSockets</span>',
             box_style, 660, 80, 290, 95, parent='t5_lane')

    add_node('inf_cr_fe',
             '<b>Cloud Run (Frontend)</b><br/><span style="font-size:10px;color:#475569;">Serverless Static Hosting for<br/>React Single Page App</span>',
             box_style, 1020, 80, 290, 95, parent='t5_lane')

    add_node('inf_vpc',
             '<b>Serverless VPC Connector</b><br/><span style="font-size:10px;color:#475569;">Private IP Internal Tunnel<br/>Subnet Interconnect</span>',
             box_style, 1380, 80, 290, 95, parent='t5_lane')

    add_node('inf_sql',
             '<b>Cloud SQL (PostgreSQL)</b><br/><span style="font-size:10px;color:#475569;">Fully Managed Private DB<br/>Isolated from Public Internet</span>',
             box_style, 1740, 75, 290, 105, parent='t5_lane')

    # -------------------------------------------------------------
    # PROMINENT DATAFLOW EDGES (Thicker lines & White Badge Labels)
    # -------------------------------------------------------------
    # Clean high-contrast edge styles with white bordered badges for labels
    edge_solid = 'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#0f172a;strokeWidth=2;fontSize=10;fontColor=#0f172a;labelBackgroundColor=#ffffff;labelBorderColor=#94a3b8;spacing=3;'
    edge_dash = 'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#0f172a;strokeWidth=2;strokeDashed=1;fontSize=10;fontColor=#0f172a;labelBackgroundColor=#ffffff;labelBorderColor=#94a3b8;spacing=3;'
    edge_infra = 'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#475569;strokeWidth=1.8;strokeDashed=1;fontSize=10;fontColor=#475569;labelBackgroundColor=#ffffff;labelBorderColor=#cbd5e1;spacing=3;'

    # 1. Inputs -> Backend Factory (Through Corridor 1: x=340..430)
    add_edge('e_rtsp', 'RTSP Video Stream', edge_solid, 'in_rtsp', 'be_factory', exit_port=(1, 0.5), entry_port=(0, 0.4))
    add_edge('e_webcam', 'Webcam Frames (Live)', edge_solid, 'in_webcam', 'be_factory', waypoints=[(365, 392), (365, 215)], exit_port=(1, 0.5), entry_port=(0, 0.5))
    add_edge('e_file', 'Offline Video Feed', edge_solid, 'in_file', 'be_factory', waypoints=[(395, 562), (395, 215)], exit_port=(1, 0.5), entry_port=(0, 0.6))

    # 2. Inside FastAPI Backend Flow
    add_edge('e_fac_pipe', 'Selected Source Stream', edge_solid, 'be_factory', 'be_pipeline', exit_port=(0.5, 1), entry_port=(0.5, 0))
    add_edge('e_pipe_work', 'Buffered & Normalized Frames', edge_solid, 'be_pipeline', 'be_workers', exit_port=(0.5, 1), entry_port=(0.5, 0))

    # 3. Backend Workers -> AI Pipeline (Through Corridor 2: x=790..880)
    add_edge('e_work_pose', 'Live Frame Stream', edge_solid, 'be_workers', 'ai_pose', waypoints=[(815, 460), (815, 212)], exit_port=(1, 0.5), entry_port=(0, 0.5))
    add_edge('e_work_repnet', 'Raw Video Sub-sequences (Async)', edge_dash, 'be_workers', 'ai_repnet', waypoints=[(825, 460), (825, 582)], exit_port=(1, 0.5), entry_port=(0, 0.5))

    # 4. Sequential AI Pipeline
    add_edge('e_pose_feat', '33 Body Landmarks & Bounding Box', edge_solid, 'ai_pose', 'ai_feat', exit_port=(0.5, 1), entry_port=(0.5, 0))
    add_edge('e_feat_tcn', '14 Joint Angles + 14 Visibility Scores', edge_solid, 'ai_feat', 'ai_tcn', exit_port=(0.5, 1), entry_port=(0.5, 0))

    # 5. AI Outputs back to Gateway (Using right lane x=855 of Corridor 2)
    add_edge('e_tcn_gw', '16-Category Class Probabilities', edge_solid, 'ai_tcn', 'be_gateway', waypoints=[(855, 460), (855, 565)], exit_port=(0, 0.5), entry_port=(1, 0.2))
    add_edge('e_repnet_gw', 'Asynchronous Repetition Counts', edge_solid, 'ai_repnet', 'be_gateway', waypoints=[(845, 582), (845, 580)], exit_port=(0, 0.5), entry_port=(1, 0.4))

    # 6. Backend <-> Database & Frontend (Parallel horizontal channels at y=750, 760, 770)
    add_edge('e_gw_db', 'SQL Queries (Exercise Plans & Set Logs)', edge_solid, 'be_gateway', 'db_box', waypoints=[(790, 595), (805, 595), (805, 750), (1315, 750), (1315, 245)], exit_port=(1, 0.6), entry_port=(0, 0.5))
    add_edge('e_gw_fe_ws', 'WebSocket (Live Stream & Predictions)', edge_solid, 'be_gateway', 'fe_box', waypoints=[(790, 610), (800, 610), (800, 760), (1335, 760), (1335, 495)], exit_port=(1, 0.8), entry_port=(0, 0.6))
    add_edge('e_gw_fe_rest', 'REST API (CRUD Plans, Workout History)', edge_solid, 'be_gateway', 'fe_box', waypoints=[(790, 625), (795, 625), (795, 770), (1350, 770), (1350, 430)], exit_port=(1, 0.95), entry_port=(0, 0.3))

    # 7. Deployment / Cloud Relationships (Bottom)
    add_edge('e_tf_prov', 'Provisions GCP Infrastructure', edge_infra, 'inf_tf', 'inf_docker', exit_port=(1, 0.5), entry_port=(0, 0.5))
    add_edge('e_dkr_run', 'Deploys Backend Image', edge_infra, 'inf_docker', 'inf_cr_be', exit_port=(1, 0.5), entry_port=(0, 0.5))
    add_edge('e_cr_fe', 'Deploys Static SPA', edge_infra, 'inf_cr_be', 'inf_cr_fe', exit_port=(1, 0.5), entry_port=(0, 0.5))
    add_edge('e_cr_vpc', 'Private Tunnel', edge_infra, 'inf_cr_be', 'inf_vpc', waypoints=[(950, 975), (1380, 975)], exit_port=(1, 0.8), entry_port=(0, 0.8))
    add_edge('e_vpc_sql', 'Internal VPC Subnet', edge_infra, 'inf_vpc', 'inf_sql', exit_port=(1, 0.5), entry_port=(0, 0.5))

    # Save to file
    tree = ET.ElementTree(root)
    ET.indent(tree, space='  ', level=0)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)
    print(f"Generated Spacious Transparent Draw.io diagram: {file_path}")

if __name__ == '__main__':
    generate_spacious_drawio('AS_IS_Architecture_HighLevel.drawio')
    generate_spacious_drawio('AS_IS_Thesis_Architecture.drawio')
