import json

arch_data = {
  "schema_version": 1,
  "diagram_type": "architecture",
  "meta": {
    "title": "AS-IS Architecture — Real-Time Exercise Recognition and Repetition Counting System",
    "subtitle": "Baseline Monocular Gym Video Pipeline | Master's Thesis Architecture (N. I. Cridlig)",
    "output": "AS_IS_Thesis_Architecture.html",
    "quality_profile": "showcase"
  },
  "components": [
    # Layer 1: Video Input Sources
    { "id": "cam_rtsp", "type": "external", "label": "RTSP IP Camera", "sublabel": "Gym Fixed Camera", "pos": [40, 160], "size": [150, 60] },
    { "id": "cam_webcam", "type": "external", "label": "Browser Webcam", "sublabel": "User Device Stream", "pos": [40, 260], "size": [150, 60] },
    { "id": "cam_file", "type": "external", "label": "Video File", "sublabel": "MP4 Evaluation File", "pos": [40, 360], "size": [150, 60] },

    # Layer 2: FastAPI Backend
    { "id": "be_factory", "type": "backend", "label": "Video Source Factory", "sublabel": "Adapter Selector", "pos": [240, 260], "size": [160, 60] },
    { "id": "be_processor", "type": "backend", "label": "Frame Processor", "sublabel": "Preprocessing & BGR2RGB", "pos": [440, 260], "size": [160, 60] },
    { "id": "be_queue", "type": "messagebus", "label": "Bounded Frame Queues", "sublabel": "Buffer Latency Control", "pos": [640, 260], "size": [170, 60] },
    { "id": "be_workers", "type": "backend", "label": "Async Workers", "sublabel": "Thread Execution", "pos": [850, 260], "size": [150, 60] },
    { "id": "be_streaming", "type": "backend", "label": "Frame Streaming", "sublabel": "Overlay Annotator", "pos": [1040, 260], "size": [150, 60] },
    { "id": "be_ws", "type": "backend", "label": "WebSocket Server", "sublabel": "Live Stream & Predictions", "pos": [1230, 260], "size": [160, 60] },
    { "id": "be_rest", "type": "backend", "label": "REST API Routers", "sublabel": "/plans & /logs CRUD", "pos": [1040, 130], "size": [150, 60] },

    # Layer 3: AI Processing Pipeline (Embedded in-process)
    { "id": "ai_pose", "type": "backend", "label": "Pose Estimation", "sublabel": "MediaPipe / BlazePose (33)", "pos": [850, 390], "size": [180, 60], "tag": "33 Landmarks" },
    { "id": "ai_feat", "type": "backend", "label": "Feature Engineering", "sublabel": "14 Angles + 14 Visibility", "pos": [850, 490], "size": [180, 60] },
    { "id": "ai_tcn", "type": "backend", "label": "Exercise Classifier", "sublabel": "TCN (16 Categories)", "pos": [1070, 490], "size": [170, 60] },
    { "id": "ai_repnet", "type": "backend", "label": "Repetition Counter", "sublabel": "RepNet (Asynchronous)", "pos": [850, 600], "size": [180, 60], "tag": "Async Reps" },

    # Layer 4A: Database Layer
    { "id": "db_postgres", "type": "database", "label": "PostgreSQL DB", "sublabel": "exercise_plan & log", "pos": [1460, 130], "size": [160, 60] },

    # Layer 4B: Frontend Layer
    { "id": "fe_react", "type": "frontend", "label": "React 19 Frontend", "sublabel": "Bootstrap 5 & Router 7", "pos": [1460, 260], "size": [160, 60], "tag": "useWebSocket" },
    { "id": "fe_routes", "type": "frontend", "label": "Routes & UI", "sublabel": "/, /user, /admin, /demo", "pos": [1460, 370], "size": [160, 60] },

    # Layer 5: Cloud Infrastructure
    { "id": "infra_tf", "type": "security", "label": "Terraform (IaC)", "sublabel": "Cloud Provisioning", "pos": [240, 750], "size": [160, 60] },
    { "id": "infra_docker", "type": "security", "label": "Docker Containers", "sublabel": "FastAPI & React Images", "pos": [440, 750], "size": [170, 60] },
    { "id": "infra_run_be", "type": "cloud", "label": "Cloud Run (Backend)", "sublabel": "FastAPI Serverless", "pos": [660, 750], "size": [170, 60] },
    { "id": "infra_run_fe", "type": "cloud", "label": "Cloud Run (Frontend)", "sublabel": "React SPA Static Hosting", "pos": [870, 750], "size": [170, 60] },
    { "id": "infra_vpc", "type": "cloud", "label": "Serverless VPC Access", "sublabel": "Private Tunnel", "pos": [1080, 750], "size": [170, 60] },
    { "id": "infra_sql", "type": "cloud", "label": "Cloud SQL (PostgreSQL)", "sublabel": "Managed DB Instance", "pos": [1290, 750], "size": [170, 60] }
  ],
  "boundaries": [
    { "kind": "region", "label": "FastAPI Backend Service (Process Space)", "wraps": ["be_factory", "be_processor", "be_queue", "be_workers", "be_streaming", "be_ws", "be_rest"] },
    { "kind": "region", "label": "Embedded AI Processing Pipeline", "wraps": ["ai_pose", "ai_feat", "ai_tcn", "ai_repnet"] },
    { "kind": "region", "label": "Google Cloud Platform Production Environment", "wraps": ["infra_run_be", "infra_run_fe", "infra_vpc", "infra_sql"] }
  ],
  "connections": [
    # Inputs -> Factory
    { "id": "rtsp-to-fac", "from": "cam_rtsp", "to": "be_factory", "label": "RTSP" },
    { "id": "webcam-to-fac", "from": "cam_webcam", "to": "be_factory", "label": "Stream" },
    { "id": "file-to-fac", "from": "cam_file", "to": "be_factory", "label": "File" },

    # Backend ingestion pipeline
    { "id": "fac-to-proc", "from": "be_factory", "to": "be_processor" },
    { "id": "proc-to-q", "from": "be_processor", "to": "be_queue", "label": "Raw Frames" },
    { "id": "q-to-work", "from": "be_queue", "to": "be_workers", "label": "Dequeue" },

    # Workers -> AI Pipeline
    { "id": "work-to-pose", "from": "be_workers", "to": "ai_pose", "label": "Frames", "fromSide": "bottom", "toSide": "top" },
    { "id": "pose-to-feat", "from": "ai_pose", "to": "ai_feat", "label": "33 Landmarks" },
    { "id": "feat-to-tcn", "from": "ai_feat", "to": "ai_tcn", "label": "Angles & Vis" },
    { "id": "work-to-repnet", "from": "be_workers", "to": "ai_repnet", "label": "Async Frames", "variant": "dashed", "fromSide": "bottom", "toSide": "left" },

    # AI outputs -> Streaming & WS
    { "id": "tcn-to-stream", "from": "ai_tcn", "to": "be_streaming", "label": "16 Classes", "fromSide": "top", "toSide": "bottom" },
    { "id": "repnet-to-stream", "from": "ai_repnet", "to": "be_streaming", "label": "Rep Counts", "fromSide": "right", "toSide": "bottom" },
    { "id": "stream-to-ws", "from": "be_streaming", "to": "be_ws", "label": "Overlaid" },

    # Backend <-> Database
    { "id": "rest-to-db", "from": "be_rest", "to": "db_postgres", "label": "SQL CRUD" },

    # Frontend <-> Backend
    { "id": "ws-to-fe", "from": "be_ws", "to": "fe_react", "label": "WebSocket", "variant": "emphasis" },
    { "id": "rest-to-fe", "from": "be_rest", "to": "fe_react", "label": "REST API", "fromSide": "right", "toSide": "left" },
    { "id": "fe-to-routes", "from": "fe_react", "to": "fe_routes" },

    # Infrastructure relationships
    { "id": "tf-to-infra", "from": "infra_tf", "to": "infra_docker", "label": "Automates", "variant": "dashed" },
    { "id": "dkr-to-run", "from": "infra_docker", "to": "infra_run_be", "label": "Deploy", "variant": "dashed" },
    { "id": "run-to-vpc", "from": "infra_run_be", "to": "infra_vpc", "label": "Tunnel", "variant": "dashed" },
    { "id": "vpc-to-sql", "from": "infra_vpc", "to": "infra_sql", "label": "Private IP", "variant": "dashed" }
  ],
  "cards": [
    { "dot": "cyan", "title": "Layer 1 & 2: Ingestion", "items": ["Factory dynamically abstracts RTSP, Webcam, or local Video Files", "Bounded Queues prevent frame drops & backpressure"] },
    { "dot": "amber", "title": "Layer 3: AI Pipeline", "items": ["BlazePose extracts 33 landmarks -> 14 joint angles", "TCN performs synchronous action classification", "RepNet executes asynchronously to prevent stream stutter"] },
    { "dot": "emerald", "title": "Layer 4 & 5: App & Cloud", "items": ["React 19 SPA with useWebSocket for real-time video overlay", "Serverless GCP Cloud Run + Cloud SQL via VPC Connector"] }
  ]
}

with open('AS_IS_Thesis_Architecture.json', 'w', encoding='utf-8') as f:
    json.dump(arch_data, f, indent=2)

print("Saved AS_IS_Thesis_Architecture.json")
