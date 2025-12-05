# Claude-Assisted Research System

## 🎯 Konzept

**Du fragst → Ich recherchiere → Ich liefere**

Anstatt eines autonomen Systems mit API Keys übernehme **ich (Claude)** die intelligente Komponente. Das System bietet mir Tools, die ich für dich nutze:

- **SearXNG** (Port 8889): Meta-Search Engine
- **ChromaDB** (Port 8000): Vector Storage für PDFs/Dokumente
- **Python Scripts**: Helper-Tools für meine Recherche

## 🔧 Workflow

### 1. Du gibst mir eine Research-Aufgabe
Beispiel: *"Recherchiere RSI Mean Reversion Strategien mit Backtests"*

### 2. Ich nutze die Tools
```python
# Web Search via SearXNG
python3 scripts/research_workflow.py search "RSI mean reversion backtest"

# Content aus ChromaDB abrufen
python3 scripts/storage_helper.py search "trading_strategies" "RSI"
```

### 3. Ich analysiere & synthetisiere
- Lese die Suchergebnisse
- Hole relevante URLs mit web_fetch
- Extrahiere Key Information
- Strukturiere die Findings

### 4. Ich liefere dir einen Report
- Zusammenfassung
- Key Findings
- Quellen
- Code-Beispiele (wenn relevant)

## 📋 Verfügbare Commands

### Web Search
```bash
# Via Python
cd /home/carsten/research
python3 scripts/research_workflow.py search "your query"

# Direkt als JSON
python3 scripts/search_helper.py "your query"
```

### Storage (ChromaDB)
```python
from storage_helper import store_content, search_content

# Store PDF content
store_content(
    collection="trading_strategies",
    content="Paper content...",
    metadata={"title": "...", "author": "..."},
    url="https://..."
)

# Search stored content
results = search_content(
    collection="trading_strategies",
    query="RSI mean reversion",
    n_results=5
)
```

### Services Management
```bash
# Status prüfen
sudo docker ps

# Logs anzeigen
sudo docker logs research_searxng
sudo docker logs research_chromadb

# Services neustarten
cd /home/carsten/research
sudo docker compose restart
```

## 📊 Typical Research Flow

```
1. Du: "Recherchiere Paper über RSL Momentum Strategie"
   ↓
2. Ich: [nutze search_helper.py]
   ↓
3. Ich: [fetche relevante URLs mit web_fetch]
   ↓
4. Ich: [analysiere Inhalte]
   ↓
5. Ich: [speichere in ChromaDB wenn relevant]
   ↓
6. Ich: [erstelle strukturierten Report]
   ↓
7. Du: Erhältst kompakten Report mit Sources
```

## 🎯 Vorteile dieser Lösung

✅ **Keine API-Kosten**: Ich bin eh hier, warum extra API Keys?  
✅ **Flexible Kontrolle**: Du kannst jederzeit eingreifen  
✅ **Bessere Quality**: Ich kann Quellen besser bewerten  
✅ **Interaktiv**: Du kannst Rückfragen stellen  
✅ **Privacy**: Läuft alles auf deinem Server  

## 📝 Domain Organization

Domains werden manuell erstellt wenn ein neues Themenfeld auftaucht:

```bash
# Neue Domain erstellen
mkdir -p domains/new_topic
python3 scripts/init_db.py new_topic
```

Aktuelle Domains:
- `trading_strategies/` - Trading Research
- (weitere werden bei Bedarf erstellt)

## 🚀 Quick Commands für dich

```bash
# Search starten
cd /home/carsten/research
python3 scripts/research_workflow.py search "query"

# Services prüfen  
sudo docker ps

# Reports ansehen
ls -lh reports/

# Storage nutzen (via Python)
python3 -c "from scripts.storage_helper import *; ..."
```

## 💡 Usage Examples

### Beispiel 1: Trading Strategy Research
**Du:** "Finde Papers über RSI Mean Reversion mit empirischen Results"

**Ich:**
1. Suche via SearXNG: "RSI mean reversion empirical results backtest"
2. Fetche Top 5 URLs
3. Extrahiere Key Findings
4. Report: Parameter, Performance, Quellen

### Beispiel 2: PDF Processing
**Du:** "Lies dieses Paper und fasse die Strategie zusammen" + PDF Upload

**Ich:**
1. Extrahiere Text aus PDF
2. Speichere in ChromaDB
3. Analysiere Methodologie
4. Liefere strukturierte Zusammenfassung

---

**Status:** ✅ Operational  
**Services:** SearXNG (8889), ChromaDB (8000)  
**Updated:** 2025-12-05
