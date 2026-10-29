import xml.etree.ElementTree as ET

def create_as_is_diagram(file_path):
    root = ET.Element('mxfile', host='app.diagrams.net', modified='2026-10-29', agent='GymOptix', version='24.0.0')
    diagram = ET.SubElement(root, 'diagram', name='GymOptix - AS-IS Architecture', id='as_is_arch_001')
    model = ET.SubElement(diagram, 'mxGraphModel', dx='1600', dy='1000', grid='1', gridSize='10', guides='1', tooltips='1', connect='1', arrows='1', fold='1', page='1', pageScale='1', pageWidth='1750', pageHeight='1200', math='0', shadow='1')
    root_cell = ET.SubElement(model, 'root')
    ET.SubElement(root_cell, 'mxCell', id='0')
    ET.SubElement(root_cell, 'mxCell', id='1', parent='0')

    def add_cell(id_val, val, style, x, y, w, h, parent='1', vertex=1):
        c = ET.SubElement(root_cell, 'mxCell', id=str(id_val), parent=str(parent), style=style, value=val, vertex=str(vertex))
        geo = ET.SubElement(c, 'mxGeometry', x=str(x), y=str(y), width=str(w), height=str(h))
        geo.set('as', 'geometry')
        return c

    def add_edge(id_val, val, style, src, tgt, pts=None, parent='1'):
        c = ET.SubElement(root_cell, 'mxCell', id=str(id_val), parent=str(parent), style=style, value=val, edge='1', source=str(src), target=str(tgt))
        geo = ET.SubElement(c, 'mxGeometry', relative='1')
        geo.set('as', 'geometry')
        if pts:
            arr = ET.SubElement(geo, 'Array')
            arr.set('as', 'points')
            for px, py in pts:
                ET.SubElement(arr, 'mxPoint', x=str(px), y=str(py))
        return c

    # Title & Header
    add_cell('title_box', 
             '<b style="font-size:20px;">AS-IS Architectural Design: Conventional Resistance Training & Tracking Environment</b><br/><span style="font-size:12px;color:#555555;">Baseline Architecture Prior to Proposed GymOptix AI Coaching System | Current Fitness Practices, Wearables, Passive Cameras & Limitations</span>', 
             'html=1;whiteSpace=wrap;fillColor=#f8f9fa;strokeColor=#495057;strokeWidth=1.5;rounded=1;shadow=1;align=center;', 
             50, 20, 1600, 65)

    # Swimlanes / Layers
    # Layer 1: Actors & Physical Gym Environment
    add_cell('lane1', 
             '<b>LAYER 1: ACTORS & PHYSICAL TRAINING ENVIRONMENT</b>', 
             'swimlane;startSize=30;horizontal=0;html=1;whiteSpace=wrap;fillColor=#EBF3FA;strokeColor=#3182CE;strokeWidth=2;rounded=1;fontStyle=1;fontSize=12;fontColor=#2B6CB0;', 
             50, 110, 1180, 150)

    # Layer 2: Input & Data Capture Tier
    add_cell('lane2', 
             '<b>LAYER 2: DATA ACQUISITION & SENSING TIER</b>', 
             'swimlane;startSize=30;horizontal=0;html=1;whiteSpace=wrap;fillColor=#EDFDFD;strokeColor=#319795;strokeWidth=2;rounded=1;fontStyle=1;fontSize=12;fontColor=#234E52;', 
             50, 285, 1180, 165)

    # Layer 3: Processing & Existing Technology Tier
    add_cell('lane3', 
             '<b>LAYER 3: PROCESSING & ANALYSIS TIER (CURRENT STATE)</b>', 
             'swimlane;startSize=30;horizontal=0;html=1;whiteSpace=wrap;fillColor=#FAF5FF;strokeColor=#805AD5;strokeWidth=2;rounded=1;fontStyle=1;fontSize=12;fontColor=#553C9A;', 
             50, 475, 1180, 230)

    # Layer 4: Output, Storage & Outcome Tier
    add_cell('lane4', 
             '<b>LAYER 4: OUTPUT, FEEDBACK & CLINICAL OUTCOMES</b>', 
             'swimlane;startSize=30;horizontal=0;html=1;whiteSpace=wrap;fillColor=#FFF5F5;strokeColor=#E53E3E;strokeWidth=2;rounded=1;fontStyle=1;fontSize=12;fontColor=#9B2C2C;', 
             50, 730, 1180, 175)

    # Right Swimlane: Architectural Bottlenecks & Gaps
    add_cell('lane_gaps', 
             '<b>SYSTEMIC GAPS & ARCHITECTURAL LIMITATIONS (AS-IS PAIN POINTS)</b>', 
             'swimlane;startSize=35;horizontal=1;html=1;whiteSpace=wrap;fillColor=#FFFBEB;strokeColor=#D69E2E;strokeWidth=2;rounded=1;fontStyle=1;fontSize=13;fontColor=#744210;', 
             1260, 110, 390, 795)

    # Layer 1 Components (Actors)
    add_cell('trainee', 
             '<b>Gym Trainee / Athlete</b><br/><span style="font-size:10px;">• Performs exercises (Squat, Deadlift, Bench)<br/>• Lacks continuous posture awareness<br/>• Prone to biomechanical errors</span>', 
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#ffffff;strokeColor=#3182CE;strokeWidth=1.5;align=left;spacingLeft=10;', 
             110, 145, 230, 90)

    add_cell('pt', 
             '<b>Human Personal Trainer (PT)</b><br/><span style="font-size:10px;">• Visual observation (Subjective)<br/>• High cost ($50-$100/session)<br/>• 1-on-1 only, scarce availability</span>', 
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#ffffff;strokeColor=#3182CE;strokeWidth=1.5;align=left;spacingLeft=10;', 
             480, 145, 230, 90)

    add_cell('gym_env', 
             '<b>Gym Physical Environment</b><br/><span style="font-size:10px;">• Free-weight racks & machines<br/>• Wall mirrors for self-checking<br/>• Passive surveillance security grid</span>', 
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#ffffff;strokeColor=#3182CE;strokeWidth=1.5;align=left;spacingLeft=10;', 
             850, 145, 240, 90)

    # Layer 2 Components (Input & Sensing)
    add_cell('mirror', 
             '<b>Gym Wall Mirrors</b><br/><span style="font-size:10px;color:#4A5568;">Visual self-reflection; requires turning head during lift → cervical spine danger</span>', 
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#E6FFFA;strokeColor=#319795;strokeWidth=1.5;align=left;spacingLeft=8;', 
             110, 320, 210, 85)

    add_cell('wearable', 
             '<b>Wearables / Smartwatches</b><br/><span style="font-size:10px;color:#4A5568;">• IMU / Accelerometer / PPG<br/>• Measures: Heart Rate, Calories<br/>• <b style="color:#C53030;">Blind to joint kinematics</b></span>', 
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#E6FFFA;strokeColor=#319795;strokeWidth=1.5;align=left;spacingLeft=8;', 
             360, 320, 210, 85)

    add_cell('passive_cctv', 
             '<b>Passive CCTV Cameras</b><br/><span style="font-size:10px;color:#4A5568;">• Fixed ceiling cameras (RTSP/IP)<br/>• 1080p stream for security<br/>• <b style="color:#C53030;">No AI / Zero trainee feedback</b></span>', 
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#E6FFFA;strokeColor=#319795;strokeWidth=1.5;align=left;spacingLeft=8;', 
             630, 320, 220, 85)

    add_cell('mobile_cam', 
             '<b>Smartphone RGB Camera</b><br/><span style="font-size:10px;color:#4A5568;">• Handheld / tripod capture<br/>• 2D standard video feed<br/>• Variable lighting & occlusions</span>', 
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#E6FFFA;strokeColor=#319795;strokeWidth=1.5;align=left;spacingLeft=8;', 
             900, 320, 210, 85)

    # Layer 3 Components (Processing Tier)
    add_cell('manual_app', 
             '<b>Manual Logging Apps</b><br/><i>(e.g., Hevy, Strong, Notes)</i><br/><span style="font-size:10px;color:#553C9A;">• User manually inputs sets/reps<br/>• Post-workout subjective entry<br/>• No biomechanical tracking</span>', 
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#F3E8FF;strokeColor=#805AD5;strokeWidth=1.5;align=left;spacingLeft=8;', 
             110, 520, 210, 125)

    add_cell('nvr_storage', 
             '<b>Passive NVR / DVR Server</b><br/><span style="font-size:10px;color:#553C9A;">• Closed-circuit video recorder<br/>• Siloed security footage storage<br/>• Completely isolated from workouts</span>', 
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#F3E8FF;strokeColor=#805AD5;strokeWidth=1.5;align=left;spacingLeft=8;', 
             360, 520, 210, 125)

    # Baseline CV Pipeline Container (Sub-group inside Layer 3)
    add_cell('baseline_box', 
             '<b>Conventional Computer Vision Pipeline (Academic Baseline / Early Apps)</b><br/><i style="font-size:10px;color:#744210;">Reference SOTA (e.g., Cridlig Thesis, RepNet, Basic VAY Sports)</i>', 
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#FEFCBF;strokeColor=#D69E2E;strokeWidth=1.5;align=center;verticalAlign=top;spacingTop=6;', 
             610, 500, 560, 185)

    add_cell('pose_est', 
             '<b>2D Human Pose Estimation</b><br/><span style="font-size:9.5px;">MediaPipe Pose / OpenPose<br/>Extracts 33 body landmarks (x,y,z)</span>', 
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#ffffff;strokeColor=#D69E2E;strokeWidth=1.2;align=center;', 
             630, 550, 160, 65)

    add_cell('action_cls', 
             '<b>Action Classification</b><br/><span style="font-size:9.5px;">TCN / LSTM / CNN<br/>Identifies exercise type (Squat vs Curl)</span>', 
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#ffffff;strokeColor=#D69E2E;strokeWidth=1.2;align=center;', 
             810, 550, 160, 65)

    add_cell('rep_counter', 
             '<b>Blind Repetition Counter</b><br/><span style="font-size:9.5px;">RepNet / Periodicity detection<br/>Counts full repetition cycles</span>', 
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#ffffff;strokeColor=#D69E2E;strokeWidth=1.2;align=center;', 
             990, 550, 160, 65)

    add_cell('missing_block', 
             '<b>❌ MISSING CRITICAL STAGES IN AS-IS PIPELINE:</b><br/><span style="font-size:9.5px;color:#C53030;">No Biomechanical Angle Math • No Form Error Classifier (Knee Valgus, Lumbar Flexion) • No Explainable Audio/Visual Feedback Engine</span>', 
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#FED7D7;strokeColor=#E53E3E;strokeWidth=1.2;strokeDashed=1;align=center;', 
             630, 625, 520, 45)

    # Layer 4 Components (Output & Clinical Impacts)
    add_cell('out_blind_count', 
             '<b>Quantity-Only Metric Output</b><br/><span style="font-size:10px;">• "4 Reps Completed"<br/>• <b style="color:#C53030;">Counts bad & dangerous reps</b><br/>• False sense of mastery</span>', 
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#ffffff;strokeColor=#E53E3E;strokeWidth=1.5;align=left;spacingLeft=8;', 
             110, 770, 240, 95)

    add_cell('out_intermittent_pt', 
             '<b>Delayed / Subjective PT Cues</b><br/><span style="font-size:10px;">• Post-set verbal comments<br/>• Inconsistent biomechanical thresholds<br/>• Absent when training alone</span>', 
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#ffffff;strokeColor=#E53E3E;strokeWidth=1.5;align=left;spacingLeft=8;', 
             410, 770, 240, 95)

    add_cell('out_injury_risk', 
             '<b>Elevated Injury & Chronic Strain Risk</b><br/><span style="font-size:10px;color:#9B2C2C;">• 2.4 - 5.3 injuries / 1000 training hours<br/>• Uncorrected knee valgus → Patellofemoral strain<br/>• Rounded spine → Lumbar disc herniation</span>', 
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#FFF5F5;strokeColor=#E53E3E;strokeWidth=1.8;align=left;spacingLeft=8;', 
             710, 770, 280, 95)

    add_cell('out_silo_data', 
             '<b>Isolated, Unstructured Gym Data</b><br/><span style="font-size:10px;">• Gym owners lack member motion stats<br/>• Equipment usage untracked<br/>• Paper / manual logs lost</span>', 
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#ffffff;strokeColor=#718096;strokeWidth=1.5;align=left;spacingLeft=8;', 
             1030, 770, 180, 95)

    # Right Lane Content (Bottlenecks & Limitations)
    gap_style = 'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#ffffff;strokeColor=#DD6B20;strokeWidth=1.5;align=left;spacingLeft=8;'
    
    add_cell('gap1', 
             '<b style="color:#C05621;">GAP 1: Form-Agnostic Rep Counting</b><br/><span style="font-size:10px;color:#4A5568;">Conventional vision & wearable models treat every rep equally. Performing 4 squats with knees collapsing inward is reported as "4 successful reps", reinforcing poor movement patterns.</span>', 
             gap_style, 
             1280, 160, 350, 95)

    add_cell('gap2', 
             '<b style="color:#C05621;">GAP 2: Sensor Inadequacy & Blindness</b><br/><span style="font-size:10px;color:#4A5568;">Smartwatches & IMU bands only capture wrist acceleration or heart rate. They cannot measure multi-segment kinematic chains (e.g. knee flexion angle, trunk inclination, cervical spine alignment).</span>', 
             gap_style, 
             1280, 275, 350, 105)

    add_cell('gap3', 
             '<b style="color:#C05621;">GAP 3: Dormant Surveillance Infrastructure</b><br/><span style="font-size:10px;color:#4A5568;">Gyms invest thousands in CCTV cameras, yet they operate purely as dumb security recording devices. None of this optical sensor data is harnessed for member biomechanical coaching.</span>', 
             gap_style, 
             1280, 400, 350, 95)

    add_cell('gap4', 
             '<b style="color:#C05621;">GAP 4: High Economic Barrier of PTs</b><br/><span style="font-size:10px;color:#4A5568;">Certified 1-on-1 personal training costs $50-$100/hr, making continuous expert supervision unaffordable for &gt;85% of regular gym goers, forcing novices to train unguided.</span>', 
             gap_style, 
             1280, 515, 350, 95)

    add_cell('gap5', 
             '<b style="color:#C05621;">GAP 5: Zero Real-Time Explainable Cues</b><br/><span style="font-size:10px;color:#4A5568;">Even when automated systems count reps, they do not explain *why* a rep was flawed (e.g., "Rep 2: Knee Valgus detected at peak depth"), leaving users unable to correct form mid-set.</span>', 
             gap_style, 
             1280, 630, 350, 95)

    add_cell('solution_banner', 
             '<b style="font-size:12px;color:#2B6CB0;">➔ The GymOptix Justification (TO-BE Target):</b><br/><span style="font-size:10px;color:#2D3748;">GymOptix transforms this AS-IS paradigm into a camera-based AI coaching pipeline that integrates form error assessment, joint angle kinematics, and real-time audio/visual corrections.</span>', 
             'shape=rectangle;rounded=1;html=1;whiteSpace=wrap;fillColor=#BEE3F8;strokeColor=#3182CE;strokeWidth=1.5;align=center;', 
             1280, 745, 350, 115)

    # Connecting Edges
    edge_style = 'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#4A5568;strokeWidth=1.5;'
    dashed_edge = 'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#E53E3E;strokeWidth=1.5;strokeDashed=1;'

    # Trainee -> Sensing
    add_edge('e1', 'Visual Self-Check', edge_style, 'trainee', 'mirror')
    add_edge('e2', 'Wrist Wearable', edge_style, 'trainee', 'wearable')
    add_edge('e3', 'Performs Exercise in View', edge_style, 'trainee', 'passive_cctv')
    add_edge('e4', 'Records Self', edge_style, 'trainee', 'mobile_cam')

    # PT -> Trainee
    add_edge('e_pt', 'Manual Visual Observation & Intermittent Verbal Coaching', edge_style, 'pt', 'trainee')

    # Sensing -> Processing
    add_edge('e5', 'Manual Entry Post-Set', edge_style, 'trainee', 'manual_app', [(225, 250), (215, 520)])
    add_edge('e6', 'RTSP Video Stream', edge_style, 'passive_cctv', 'nvr_storage')
    add_edge('e7', 'Video Feed', edge_style, 'mobile_cam', 'baseline_box')

    # Inside Baseline CV Pipeline
    add_edge('e_cv1', '', edge_style, 'pose_est', 'action_cls')
    add_edge('e_cv2', '', edge_style, 'action_cls', 'rep_counter')

    # Processing -> Outputs
    add_edge('e8', 'Quantity Only', dashed_edge, 'rep_counter', 'out_blind_count')
    add_edge('e9', 'Subjective Feedback', edge_style, 'pt', 'out_intermittent_pt', [(600, 250), (600, 750), (530, 770)])
    add_edge('e10', 'Lack of Form Correction', dashed_edge, 'out_blind_count', 'out_injury_risk')
    add_edge('e11', 'Unutilized Archival', edge_style, 'nvr_storage', 'out_silo_data', [(465, 660), (465, 715), (1120, 715), (1120, 770)])

    # Gaps associations
    add_edge('egap1', '', dashed_edge, 'rep_counter', 'gap1')
    add_edge('egap2', '', dashed_edge, 'wearable', 'gap2')
    add_edge('egap3', '', dashed_edge, 'passive_cctv', 'gap3')

    # Write output file
    tree = ET.ElementTree(root)
    ET.indent(tree, space='  ', level=0)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)
    print(f'Successfully generated {file_path}')

if __name__ == '__main__':
    create_as_is_diagram('AS-IS_Architecture.drawio')

