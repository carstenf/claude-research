# Claude Research System

## 🎯 Konzept

**Ein Research-System OHNE teure API-Kosten - Claude übernimmt die intelligente Komponente!**

Anstatt eines autonomen Systems mit LLM API Keys ist dies ein **Claude-assisted Research System**:
- **Du** gibst mir Research-Aufgaben
- **Ich (Claude)** nutze die Tools auf deinem Server
- **Du** erhältst strukturierte, analysierte Reports

```
You → "Recherchiere XYZ" → Claude
                            ↓
                    [SearXNG: Web Search]
                    [ChromaDB: Document Storage]
                    [web_fetch: Content Extraction]
                            ↓
                    Analysis & Synthesis
                            ↓
You ← Structured Report ← Claude
```

## ✅ Status: Vollständig Einsatzbereit

**Was läuft:**
- ✅ **Docker v29.1.2** installiert
- ✅ **SearXNG** (Port 8889) - Privacy-respecting meta-search engine
- ✅ **ChromaDB** (Port 8000) - Vector database for documents
- ✅ **Python Helper Scripts** - Tools for Claude to use
- ✅ **Trading Strategies Domain** - Initialized and ready

**Deployed:**
- ✅ Code auf GitHub: https://github.com/carstenf/claude-research
- ✅ Services laufen auf Hetzner Server (128.140.104.236)
- ✅ Vollständige Dokumentation vorhanden

## 🎯 Vorteile dieses Ansatzes

| Feature | Traditional Autonomous System | This Claude-Assisted System |
|---------|------------------------------|----------------------------|
| **API Costs** | €50-200/Monat | €0 (Claude is already here) |
| **Quality Control** | Automated, hit-or-miss | Human-in-the-loop with Claude |
| **Flexibility** | Fixed workflow | Interactive, adaptable |
| **Context Understanding** | Limited by prompts | Full conversational context |
| **Privacy** | Data sent to APIs | All on your server |
| **Debugging** | Complex logs | Direct conversation |

## 🚀 Wie es funktioniert

### 1. Du gibst mir eine Aufgabe

**Beispiele:**
- "Recherchiere RSI Mean Reversion Strategien mit Backtest-Ergebnissen"
- "Finde Papers über Momentum Trading in Crypto-Märkten"
- "Analysiere aktuelle Entwicklungen bei 0DTE Options Trading"
- "Fasse dieses PDF zusammen" (+ Upload)

### 2. Ich nutze die Tools

```python
# Web Search via SearXNG
python3 scripts/research_workflow.py search "RSI mean reversion backtest"

# Content Extraction
web_fetch(url)

# Storage in ChromaDB
store_content(collection="trading_strategies", content=..., metadata=...)
```

### 3. Ich analysiere & synthetisiere

- Bewerte Quellen-Qualität
- Extrahiere Key Findings
- Strukturiere die Informationen
- Erstelle Code-Beispiele (wenn relevant)

### 4. Du erhältst einen Report

- Zusammenfassung
- Key Findings
- Quellen mit Links
- Praxisrelevante Insights

## 📂 Projekt-Struktur

```
/home/carsten/research/
├── docker-compose.yml          # Services (SearXNG, ChromaDB)
├── requirements.txt            # Python dependencies
├── .env.example               # Configuration template
├── Makefile                   # Convenience commands
│
├── scripts/
│   ├── search_helper.py       # SearXNG wrapper
│   ├── storage_helper.py      # ChromaDB wrapper
│   ├── research_workflow.py   # Main workflow
│   ├── init_db.py            # Database initialization
│   └── config.py             # Configuration
│
├── domains/
│   └── trading_strategies/   # Research domain (initialized)
│
├── reports/                  # Generated reports
├── searxng/                  # SearXNG config & data
└── chroma_data/              # ChromaDB storage

Documentation:
├── README.md                 # This file
├── CLAUDE_WORKFLOW.md        # Detailed workflow guide
├── STATUS.md                 # Current system status
└── GITHUB_DEPLOYMENT.md      # Deployment guide
```

## 🔧 Quick Commands

### Services verwalten
```bash
# Status prüfen
sudo docker ps

# Logs ansehen
sudo docker logs research_searxng
sudo docker logs research_chromadb

# Services neustarten
cd /home/carsten/research
sudo docker compose restart

# Services stoppen/starten
sudo docker compose down
sudo docker compose up -d
```

### Research durchführen
```bash
# Suche starten
cd /home/carsten/research
python3 scripts/research_workflow.py search "your query"

# Direkt als JSON
python3 scripts/search_helper.py "your query"
```

### Domains verwalten
```bash
# Neue Domain erstellen
mkdir -p domains/new_topic
python3 scripts/init_db.py new_topic

# Aktuelle Domains
ls -l domains/
```

## 📋 Typischer Research-Flow

**Beispiel: Trading Strategy Research**

1. **Du:** "Finde Papers über RSI Mean Reversion mit empirischen Backtest-Ergebnissen"

2. **Ich (Claude):**
   - Suche via SearXNG: "RSI mean reversion empirical backtest results"
   - Fetche Top 5-10 URLs mit web_fetch
   - Analysiere Methodologie, Parameter, Performance
   - Extrahiere Key Findings

3. **Du erhältst:**
   ```markdown
   # RSI Mean Reversion Strategy Research
   
   ## Zusammenfassung
   [Kompakte Übersicht der Findings]
   
   ## Key Findings
   - Optimale RSI-Schwellenwerte: 30/70 vs 20/80
   - Performance-Metriken aus 5 Studies
   - Asset Class Unterschiede
   
   ## Quellen
   1. [Paper Title](url) - Key takeaway
   2. [Blog Post](url) - Implementation details
   ...
   
   ## Code-Beispiel (wenn relevant)
   ```python
   # Implementation
   ```
   ```

## 🎯 Use Cases

### Primary (70%): Trading Strategy Research
- Backtest-Results für verschiedene Strategien
- Paper-Analysen zu Momentum, Mean Reversion, etc.
- Performance-Vergleiche
- Implementation Details

### Secondary (30%): General Research
- VW Turbo-Prämie Details
- Health Insurance Tariff Analysis
- Technical Documentation
- iOS Development Workflows

## 🔐 Sicherheit & Privacy

- ✅ Alle Services laufen auf deinem eigenen Server
- ✅ Keine Daten gehen zu externen LLM APIs
- ✅ SearXNG respektiert Privacy (keine Tracking)
- ✅ Sensitive Daten in `.gitignore` ausgeschlossen
- ✅ `.env` mit Secrets nicht im Git

## 📊 System Requirements

**Minimal (aktuell):**
- Docker: ~500MB RAM für beide Services
- Disk: ~1GB für Images + Data
- CPU: Minimal (Search ist I/O-bound)

**Dein Server:**
- 32GB Speicher verfügbar
- Ubuntu 24
- Docker v29.1.2
- Python 3.12.3

## 🚀 Deployment

Das System ist bereits deployed und läuft!

**Services:**
- SearXNG: http://128.140.104.236:8889
- ChromaDB: http://localhost:8000

**Für Updates:**
```bash
cd /home/carsten/research
git add .
git commit -m "Update: description"
git push
```

## 📖 Weitere Dokumentation

- **[CLAUDE_WORKFLOW.md](CLAUDE_WORKFLOW.md)** - Detaillierter Workflow-Guide
- **[STATUS.md](STATUS.md)** - Aktueller System-Status
- **[GITHUB_DEPLOYMENT.md](GITHUB_DEPLOYMENT.md)** - Deployment-Anleitung

## 💡 Warum dieser Ansatz?

**Claude ist bereits verfügbar** - warum sollte man zusätzlich für LLM API Calls bezahlen?

Stattdessen:
- Ich nutze die Tools auf deinem Server
- Du behältst volle Kontrolle
- Wir können iterativ verfeinern
- Bessere Qualität durch Kontext-Verständnis
- Null zusätzliche Kosten

Das System bietet mir (Claude) die Werkzeuge, die ich brauche, um für dich zu recherchieren. Es ist wie ein Research-Assistent, der Zugang zu einer Bibliothek und dem Internet hat.

## 🎉 Ready to Use!

**Das System ist einsatzbereit!**

Gib mir einfach eine Research-Aufgabe und ich lege los!

---

**Version:** 1.0.0  
**Status:** ✅ Production Ready  
**Last Updated:** 2025-12-05  
**Repository:** https://github.com/carstenf/claude-research
