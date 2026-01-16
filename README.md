# core-video-ingestion
Built a core-advanced automated video ingestion platform to validate partner metadata and video codecs (H.264/AAC) using Python, FFmpeg, and REST APIs, improving ingestion reliability and partner visibility.
This project demonstrates clean architecture, domain-driven design, asynchronous processing, and media compliance validation using industry-standard tools.

---

##  Key Capabilities

- Automated metadata ingestion supporting JSON and XML partner payloads
- Contract-driven metadata validation with strict schema enforcement
- FFmpeg (ffprobe)-based video compliance validation (H.264 video, AAC audio)
- Asynchronous, non-blocking ingestion using background worker threads
- State-machine driven ingestion lifecycle management
- Partner-facing REST APIs for ingestion submission and status tracking
- Clean, production-ready, modular architecture

---

##  Architecture Overview

Client / Partner  
→ REST API (Flask)  
→ Ingestion Controller  
→ Async Worker Pool  
→ Ingestion Pipeline  
→ Validators (Metadata + Video)  
→ Persistent Status Store  

---

##  Project Structure
core-video-ingestion/
├── api/ # HTTP routes & API schemas
├── adapters/ # JSON / XML input adapters
├── core/
│ ├── domain/ # Core business entities & states
│ ├── contracts/ # Metadata contracts
│ ├── validators/ # Validation strategies
│ ├── pipeline/ # Ingestion workflow engine
│ ├── storage/ # Persistence abstraction
│ └── observability/ # Logging & tracing
├── data/ # Local runtime data (ignored in Git)
├── samples/ # Sample metadata files
├── app.py # Application entry point
├── requirements.txt
├── README.md
└── LICENSE


---

## 🔌 API Endpoints

### Ingest Metadata
POST /ingest?type=json
POST /ingest?type=xml



**Request**
- Multipart form-data
- `file`: Metadata file (JSON or XML)

**Response**
```json
{
  "ingestion_id": "uuid"
}
```
**Check Ingestion Status**
GET /status/{ingestion_id}

**Response**
{
  "partner_id": "PARTNER_001",
  "state": "PASSED",
  "reason": null
}

⚙️ Technology Stack

Language: Python 3

Framework: Flask

Media Inspection: FFmpeg (ffprobe)

Architecture: Domain-Driven Design

Concurrency: Background worker threads

APIs: REST

🛠️ Setup & Run Locally
Prerequisites

Python 3.9+

FFmpeg installed (ffprobe must be available)

**Installation**
Install Dependencies
```bash
pip install -r requirements.txt
```
Run Application
```bash
python app.py
```

