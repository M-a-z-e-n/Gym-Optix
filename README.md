# GymOptix 🏋️‍♂️👁️
### A Camera-Based AI Fitness Coaching System for Real-Time Exercise Recognition, Repetition Counting, and Form Assessment

---

## 📌 Project Overview
**GymOptix** is an AI-powered fitness monitoring and coaching platform designed to elevate resistance training through intelligent computer vision. Unlike conventional fitness tracking solutions that merely count raw repetitions regardless of execution quality, GymOptix evaluates **biomechanical exercise form**, provides **real-time explainable corrections**, and prevents exercise-induced injuries—all using standard monocular RGB cameras (smartphones, webcams, or gym surveillance cameras) without requiring wearable sensors or costly depth hardware.

---

## 🏛️ System Architecture

The repository contains both conceptual and reference architectural designs modeled after academic resistance training benchmarks (e.g., Nicolas Ivan Cridlig's Master's thesis on real-time gym exercise analysis):

### 1. High-Level Tiers:
* **Tier 1 — Video Input Sources:** Monocular RTSP IP surveillance cameras, browser webcams (HTML5 `getUserMedia`), and offline benchmark video datasets.
* **Tier 2 — FastAPI Streaming Backend:** Video Source Factory, frame preprocessing, bounded queue flow buffers to prevent backpressure, asynchronous worker pools, and WebSocket/REST gateways.
* **Tier 3 — Embedded AI Processing Pipeline:**
  1. *Human Pose Estimation:* MediaPipe / BlazePose extracting 33 3D skeletal landmarks.
  2. *Feature Engineering:* Computation of 14 kinematic joint angles and 14 visibility confidence metrics.
  3. *Action Classification:* Temporal Convolutional Network (TCN) recognizing 16 distinct exercise categories synchronously.
  4. *Repetition Counting:* RepNet (Temporal Self-Similarity Network) decoupled asynchronously to maintain $\ge 25\text{ FPS}$ streaming without video stutter.
* **Tier 4 — Storage & Client Application:** PostgreSQL database (`exercise_plan`, `log`) and a React 19 Single Page Application (SPA).
* **Tier 5 — Cloud Deployment & Infrastructure:** Terraform IaC automating deployment to Google Cloud Run, Serverless VPC Access Connector, and Google Cloud SQL.

---

## 📂 Repository Contents

```text
├── AS_IS_Architecture_HighLevel.drawio    # High-level clean wireframe architecture
├── AS_IS_Thesis_Architecture.drawio      # Comprehensive reference thesis architecture
├── AS_IS_Thesis_Architecture.html        # Interactive standalone HTML diagram
├── DFD.excalidraw                        # Data Flow Diagrams (DFD Level 0 & Level 1)
├── ERD.drawio                            # Entity Relationship Diagram
├── documentation/                        # Project chapters, research review, & datasets
├── Papers/                               # Core academic reference papers
├── System Arc/                           # System design documents & diagrams
├── .gitignore                            # Ignoring Old directories and secret files
└── README.md                             # Project overview and documentation
```

---

## 🛠️ Tech Stack

* **Computer Vision & AI:** Python, MediaPipe / BlazePose, PyTorch, TCN, RepNet, OpenCV.
* **Backend:** FastAPI, Uvicorn, WebSockets, Asyncio.
* **Frontend:** React 19, Bootstrap 5, React Router 7.
* **Database:** PostgreSQL / Google Cloud SQL.
* **Infrastructure & DevOps:** Docker, Terraform, Google Cloud Platform (Cloud Run, Cloud SQL, VPC).

---

## 📜 License & Acknowledgments
Developed as a Graduation Project. All academic papers and reference theses are credited to their respective authors.
