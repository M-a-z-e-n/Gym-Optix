import xml.etree.ElementTree as ET

def generate_highlevel_transparent_drawio(file_path):
    root = ET.Element('mxfile', host='app.diagrams.net', modified='2026-10-29', agent='drawio-skill', version='24.0.0')
    diagram = ET.SubElement(root, 'diagram', name='AS-IS High-Level Architecture', id='asis_highlevel')
    model = ET.SubElement(diagram, 'mxGraphModel', dx='1600', dy='900', grid='1', gridSize='10', guides='1', tooltips='1', connect='1', arrows='1', fold='1', page='1', pageScale='1', pageWidth='1600', pageHeight='900', math='0', shadow='0')
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
    # 0. TITLE HEADER (Clean & Minimalist)
    # -------------------------------------------------------------
    add_node('hdr_title',
             '<b style="font-size:18px;color:#0f172a;letter-spacing:0.5px;">AS-IS Architecture — High-Level System Overview</b><br/>'
             '<span style="font-size:12px;color:#475569;">Real-Time Exercise Recognition and Repetition Counting System (Nicolas Ivan Cridlig Thesis)</span>',
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=none;strokeColor=#334155;strokeWidth=1.5;align=center;',
             40, 20, 1520, 55, parent='1')

    # Common Hollow/Transparent Styles
    box_style = 'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=none;strokeColor=#1e293b;strokeWidth=1.5;align=center;fontSize=11;fontColor=#0f172a;'
    box_dashed = 'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=none;strokeColor=#475569;strokeWidth=1.5;strokeDashed=1;align=center;fontSize=11;fontColor=#0f172a;'
    lane_style = 'swimlane;startSize=28;horizontal=0;html=1;whiteSpace=wrap;fillColor=none;strokeColor=#334155;strokeWidth=1.8;rounded=1;fontStyle=1;fontSize=11;fontColor=#0f172a;container=1;collapsible=0;pointerEvents=0;'

    # -------------------------------------------------------------
    # 1. TIER 1: VIDEO CAPTURE & INPUT SOURCES
    # -------------------------------------------------------------
    add_node('t1_lane', '<b>TIER 1: VIDEO INPUT SOURCES</b>',
             lane_style, 40, 95, 230, 520, parent='1')

    add_node('in_rtsp',
             '<b>RTSP IP Camera</b><br/><span style="font-size:10px;color:#475569;">Monocular Gym Surveillance Stream</span>',
             box_style, 25, 60, 180, 80, parent='t1_lane')

    add_node('in_webcam',
             '<b>Browser Webcam</b><br/><span style="font-size:10px;color:#475569;">Athlete Live Device Capture</span>',
             box_style, 25, 200, 180, 80, parent='t1_lane')

    add_node('in_file',
             '<b>Recorded Video File</b><br/><span style="font-size:10px;color:#475569;">Pre-recorded MP4 / Benchmark</span>',
             box_style, 25, 340, 180, 80, parent='t1_lane')

    # -------------------------------------------------------------
    # 2. TIER 2: FASTAPI BACKEND & VIDEO PROCESSING
    # -------------------------------------------------------------
    add_node('t2_lane', '<b>TIER 2: BACKEND & STREAMING ENGINE (FastAPI)</b>',
             lane_style, 300, 95, 330, 520, parent='1')

    add_node('be_factory',
             '<b>Video Source Factory</b><br/><span style="font-size:10px;color:#475569;">Source Selection & Input Adapter</span>',
             box_style, 25, 60, 280, 70, parent='t2_lane')

    add_node('be_pipeline',
             '<b>Frame Ingestion & Queue Buffer</b><br/><span style="font-size:10px;color:#475569;">Frame Processor & Bounded Queues</span>',
             box_style, 25, 160, 280, 70, parent='t2_lane')

    add_node('be_workers',
             '<b>Asynchronous Worker Pool</b><br/><span style="font-size:10px;color:#475569;">Drives In-Process Inference Threads</span>',
             box_style, 25, 260, 280, 70, parent='t2_lane')

    add_node('be_gateway',
             '<b>Communication Gateway</b><br/><span style="font-size:10px;color:#475569;">WebSocket Hub & REST API Routers</span>',
             box_style, 25, 360, 280, 70, parent='t2_lane')

    # -------------------------------------------------------------
    # 3. TIER 3: CORE AI / COMPUTER VISION PIPELINE
    # -------------------------------------------------------------
    add_node('t3_lane', '<b>TIER 3: AI PROCESSING PIPELINE (In-Process Models)</b>',
             lane_style, 660, 95, 380, 520, parent='1')

    add_node('ai_pose',
             '<b>1. Pose Estimation (MediaPipe)</b><br/><span style="font-size:10px;color:#475569;">Extracts 33 3D Keypoints & Bounding Box</span>',
             box_style, 25, 55, 330, 75, parent='t3_lane')

    add_node('ai_feat',
             '<b>2. Feature Engineering</b><br/><span style="font-size:10px;color:#475569;">Computes 14 Joint Angles & 14 Visibility Scores</span>',
             box_style, 25, 155, 330, 75, parent='t3_lane')

    add_node('ai_tcn',
             '<b>3. Exercise Classification (TCN)</b><br/><span style="font-size:10px;color:#475569;">Temporal Convolutional Net (16 Exercise Classes)</span>',
             box_style, 25, 255, 330, 75, parent='t3_lane')

    add_node('ai_repnet',
             '<b>4. Repetition Counting (RepNet)</b><br/><span style="font-size:10px;color:#475569;">Temporal Self-Similarity <i>[Runs Asynchronously]</i></span>',
             box_dashed, 25, 360, 330, 80, parent='t3_lane')

    add_node('ai_note',
             '<i style="font-size:9.5px;color:#64748b;">Pipeline executes embedded inside backend workers (not standalone microservices)</i>',
             'shape=rectangle;rounded=0;html=1;whiteSpace=wrap;fillColor=none;strokeColor=none;align=center;',
             25, 465, 330, 30, parent='t3_lane')

    # -------------------------------------------------------------
    # 4. TIER 4: STORAGE & CLIENT APPLICATION
    # -------------------------------------------------------------
    add_node('t4_lane', '<b>TIER 4: STORAGE & APPLICATION CLIENT</b>',
             lane_style, 1070, 95, 490, 520, parent='1')

    # Sub-block: Database
    add_node('db_box',
             '<b>PostgreSQL Database (Cloud SQL)</b><br/>'
             '<span style="font-size:10px;color:#475569;">'
             '• <code>exercise_plan</code> (Target routines & sets)<br/>'
             '• <code>log</code> (Completed sets, reps & timestamps)'
             '</span>',
             box_style, 30, 60, 430, 110, parent='t4_lane')

    # Sub-block: React Frontend
    add_node('fe_box',
             '<b>React 19 Frontend Client (Web SPA)</b><br/>'
             '<span style="font-size:10px;color:#475569;line-height:1.4;">'
             '• Bootstrap 5 • React Router 7 • <code>useWebSocket.js</code><br/>'
             '• Routes: <code>/</code> (Main), <code>/user</code>, <code>/admin</code>, <code>/demo</code><br/>'
             '• Live Video Overlay, Real-time Exercise & Repetition Display'
             '</span>',
             box_style, 30, 230, 430, 150, parent='t4_lane')

    # -------------------------------------------------------------
    # 5. TIER 5: DEPLOYMENT & CLOUD INFRASTRUCTURE (BOTTOM)
    # -------------------------------------------------------------
    add_node('t5_lane', '<b>TIER 5: CLOUD DEPLOYMENT & INFRASTRUCTURE (Google Cloud Platform & IaC)</b>',
             'swimlane;startSize=28;horizontal=0;html=1;whiteSpace=wrap;fillColor=none;strokeColor=#475569;strokeWidth=1.8;strokeDashed=1;rounded=1;fontStyle=1;fontSize=11;fontColor=#0f172a;container=1;collapsible=0;pointerEvents=0;',
             40, 635, 1520, 235, parent='1')

    add_node('inf_tf',
             '<b>Terraform (IaC)</b><br/><span style="font-size:10px;color:#475569;">Automated Cloud Provisioning</span>',
             box_style, 30, 65, 200, 80, parent='t5_lane')

    add_node('inf_docker',
             '<b>Docker Containers</b><br/><span style="font-size:10px;color:#475569;">Backend & Frontend Images</span>',
             box_style, 260, 65, 200, 80, parent='t5_lane')

    add_node('inf_cr_be',
             '<b>Cloud Run (Backend)</b><br/><span style="font-size:10px;color:#475569;">Serverless FastAPI & WebSockets</span>',
             box_style, 500, 65, 240, 80, parent='t5_lane')

    add_node('inf_cr_fe',
             '<b>Cloud Run (Frontend)</b><br/><span style="font-size:10px;color:#475569;">Serverless Static SPA Hosting</span>',
             box_style, 770, 65, 240, 80, parent='t5_lane')

    add_node('inf_vpc',
             '<b>Serverless VPC Connector</b><br/><span style="font-size:10px;color:#475569;">Private Internal Tunnel</span>',
             box_style, 1040, 65, 210, 80, parent='t5_lane')

    add_node('inf_sql',
             '<b>Cloud SQL (PostgreSQL)</b><br/><span style="font-size:10px;color:#475569;">Private Relational DB</span>',
             box_style, 1280, 65, 200, 80, parent='t5_lane')

    # -------------------------------------------------------------
    # EDGES / CONNECTORS (Hollow / Minimalist Line Style)
    # -------------------------------------------------------------
    edge_solid = 'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1e293b;strokeWidth=1.5;fontSize=10;fontColor=#0f172a;labelBackgroundColor=none;'
    edge_dash = 'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1e293b;strokeWidth=1.5;strokeDashed=1;fontSize=10;fontColor=#0f172a;labelBackgroundColor=none;'
    edge_infra = 'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#64748b;strokeWidth=1.5;strokeDashed=1;fontSize=9.5;fontColor=#475569;labelBackgroundColor=none;'

    # 1. Inputs -> Backend Factory
    add_edge('e_rtsp', 'RTSP Stream', edge_solid, 'in_rtsp', 'be_factory', exit_port=(1, 0.5), entry_port=(0, 0.4))
    add_edge('e_webcam', 'Webcam Frames', edge_solid, 'in_webcam', 'be_factory', waypoints=[(260, 335), (260, 190)], exit_port=(1, 0.5), entry_port=(0, 0.5))
    add_edge('e_file', 'Video File', edge_solid, 'in_file', 'be_factory', waypoints=[(275, 475), (275, 190)], exit_port=(1, 0.5), entry_port=(0, 0.6))

    # 2. Inside Backend Flow
    add_edge('e_fac_pipe', 'Selected Stream', edge_solid, 'be_factory', 'be_pipeline', exit_port=(0.5, 1), entry_port=(0.5, 0))
    add_edge('e_pipe_work', 'Buffered Frames', edge_solid, 'be_pipeline', 'be_workers', exit_port=(0.5, 1), entry_port=(0.5, 0))

    # 3. Backend Workers -> AI Pipeline
    add_edge('e_work_pose', 'Frame Stream', edge_solid, 'be_workers', 'ai_pose', waypoints=[(610, 390), (645, 390), (645, 187)], exit_port=(1, 0.5), entry_port=(0, 0.5))
    add_edge('e_work_repnet', 'Video Batch (Async)', edge_dash, 'be_workers', 'ai_repnet', waypoints=[(610, 390), (645, 390), (645, 495)], exit_port=(1, 0.5), entry_port=(0, 0.5))

    # 4. Sequential AI Pipeline
    add_edge('e_pose_feat', '33 Keypoints', edge_solid, 'ai_pose', 'ai_feat', exit_port=(0.5, 1), entry_port=(0.5, 0))
    add_edge('e_feat_tcn', 'Angles & Visibility', edge_solid, 'ai_feat', 'ai_tcn', exit_port=(0.5, 1), entry_port=(0.5, 0))

    # 5. AI Outputs -> Gateway
    add_edge('e_tcn_gw', '16-Class Prediction', edge_solid, 'ai_tcn', 'be_gateway', waypoints=[(675, 387), (645, 387), (645, 480), (610, 480)], exit_port=(0, 0.4), entry_port=(1, 0.3))
    add_edge('e_repnet_gw', 'Repetition Count', edge_solid, 'ai_repnet', 'be_gateway', waypoints=[(675, 495), (635, 495), (635, 500), (610, 500)], exit_port=(0, 0.5), entry_port=(1, 0.7))

    # 6. Backend <-> Database & Frontend (Clean Corridors avoiding AI boxes)
    add_edge('e_gw_db', 'SQL Queries (Plans & Logs)', edge_solid, 'be_gateway', 'db_box', waypoints=[(610, 465), (645, 465), (645, 620), (1055, 620), (1055, 210)], exit_port=(1, 0.2), entry_port=(0, 0.5))
    add_edge('e_gw_fe_ws', 'WebSocket (Live Stream & Predictions)', edge_solid, 'be_gateway', 'fe_box', waypoints=[(610, 500), (635, 500), (635, 625), (1060, 625), (1060, 380)], exit_port=(1, 0.8), entry_port=(0, 0.6))
    add_edge('e_gw_fe_rest', 'REST API (Plans, History, Admin)', edge_solid, 'be_gateway', 'fe_box', waypoints=[(610, 480), (640, 480), (640, 615), (1050, 615), (1050, 340)], exit_port=(1, 0.5), entry_port=(0, 0.3))

    # 7. Deployment / Cloud Relationships (Bottom)
    add_edge('e_tf_prov', 'Provisions Infrastructure', edge_infra, 'inf_tf', 'inf_docker', exit_port=(1, 0.5), entry_port=(0, 0.5))
    add_edge('e_dkr_run', 'Deploys Containers', edge_infra, 'inf_docker', 'inf_cr_be', exit_port=(1, 0.5), entry_port=(0, 0.5))
    add_edge('e_cr_fe', '', edge_infra, 'inf_cr_be', 'inf_cr_fe', exit_port=(1, 0.5), entry_port=(0, 0.5))
    add_edge('e_cr_vpc', 'Secure Tunnel', edge_infra, 'inf_cr_be', 'inf_vpc', waypoints=[(740, 810), (1040, 810)], exit_port=(1, 0.5), entry_port=(0, 0.5))
    add_edge('e_vpc_sql', 'Private Access', edge_infra, 'inf_vpc', 'inf_sql', exit_port=(1, 0.5), entry_port=(0, 0.5))

    # Save to file
    tree = ET.ElementTree(root)
    ET.indent(tree, space='  ', level=0)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)
    print(f"Generated High-Level Transparent Draw.io diagram: {file_path}")

if __name__ == '__main__':
    generate_highlevel_transparent_drawio('AS_IS_Architecture_HighLevel.drawio')
    # Also overwrite the primary AS_IS_Thesis_Architecture.drawio with this high-level transparent version
    generate_highlevel_transparent_drawio('AS_IS_Thesis_Architecture.drawio')
