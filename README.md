# Trading Strategy Research System

Agentic AI Research System für Trading-Strategien mit Hybrid RAG + Live Web Search.

## 🏗️ Architektur

**Hybrid-Ansatz:**
- **Docker Services:** SearXNG (Search) + ChromaDB (Vector DB)
- **Native Python:** Research Agents (während Development)
- **Storage:** Domains mit PDFs, Vector Data, Metadata

## 🚀 Quick Start

### 1. Prerequisites

```bash
# Docker & Docker Compose installiert
docker --version
docker-compose --version

# Python 3.11+
python3 --version
```

### 2. Setup

```bash
# Clone/Navigate to directory
cd /home/carsten/research

# Copy environment template
cp .env.example .env

# Edit .env und füge deine API Keys ein
nano .env

# Install Python dependencies
pip install --break-system-packages -r requirements.txt

# Start Docker services
docker-compose up -d

# Verify services
docker ps
curl http://localhost:8888  # SearXNG
curl http://localhost:8000/api/v1/heartbeat  # ChromaDB
```

### 3. Initialize Database

```bash
python3 scripts/init_db.py
```

### 4. Run Research

```bash
python3 scripts/researcher.py "Recherchiere RSI Momentum Strategien"
```

## 📁 Directory Structure

```
/home/carsten/research/
├── docker-compose.yml           # Docker services
├── requirements.txt             # Python dependencies
├── .env                         # Configuration (not in git)
├── .gitignore
├── README.md
│
├── scripts/                     # Python code
│   ├── researcher.py           # Main research agent
│   ├── init_db.py              # Database initialization
│   └── config.py               # Configuration
│
├── domains/                     # Research domains (auto-created)
│   ├── trading_strategies/
│   │   ├── pdfs/
│   │   ├── vector_db/
│   │   └── metadata.db
│   └── [weitere domains...]
│
├── reports/                     # Generated reports
├── searxng/                     # SearXNG config
└── chroma_data/                 # ChromaDB data
```

## 🔧 Development

### Services verwalten

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f searxng
docker-compose logs -f chromadb

# Restart services
docker-compose restart
```

### Python Development

```bash
# Code bearbeiten
nano scripts/researcher.py

# Direkt ausführen (kein Docker rebuild nötig)
python3 scripts/researcher.py "Query"

# Debuggen mit pdb
python3 -m pdb scripts/researcher.py
```

## 📊 System Status

```bash
# Check services
curl http://localhost:8888/search?q=test&format=json
curl http://localhost:8000/api/v1/heartbeat

# Database size
du -sh domains/
du -sh chroma_data/

# Docker stats
docker stats
```

## 🎯 Next Steps

1. ✅ Services laufen (SearXNG + ChromaDB)
2. 🔧 Implement LangGraph Workflow
3. 🔧 Add Domain Auto-Detection
4. 🔧 Integrate MCP Server
5. 🚀 Production: Full Docker Stack

## 📚 Documentation

- [Concept PDF](docs/Trading_Research_System_Konzept.pdf)
- [Architecture](docs/architecture.md) (TODO)
- [API Reference](docs/api.md) (TODO)

## 🐛 Troubleshooting

**SearXNG nicht erreichbar:**
```bash
docker logs research_searxng
docker restart research_searxng
```

**ChromaDB Issues:**
```bash
docker logs research_chromadb
# Check permissions
ls -la chroma_data/
```

**Python Dependencies:**
```bash
pip install --break-system-packages --upgrade -r requirements.txt
```

## 📝 Status

- [x] Project Setup
- [x] Docker Services
- [ ] Python Research Agent
- [ ] LangGraph Integration
- [ ] Domain Management
- [ ] MCP Server Integration
- [ ] Production Docker Image

---

**Version:** 0.1.0 (Development)  
**Status:** 🚧 In Development  
**Deployment:** When stable → GitHub Repository
