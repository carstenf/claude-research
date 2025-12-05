# Agent Roles Guide

## Konzept: Claude als Multi-Role Agent

Anstatt mehrere separate LLM Agents mit eigenen API Calls zu haben, **übernimmt Claude dynamisch verschiedene spezialisierte Rollen** während des Research-Prozesses.

## 🎭 Die 6 Agent-Rollen

```
User Question
      ↓
[1] Query Analyzer ← Verstehe & strukturiere die Anfrage
      ↓
[2] Web Researcher ← Finde & bewerte Quellen (SearXNG)
      ↓
[3] Content Extractor ← Hole & parse Inhalte (web_fetch)
      ↓
[4] Domain Expert ← Analysiere mit Fach-Expertise
      ↓
[5] Synthesizer ← Kombiniere zu kohärentem Output
      ↓
[6] Report Writer ← Finalisiere für optimale Lesbarkeit
      ↓
User erhält Report
```

## 📁 Rolle-Dateien

Jede Rolle hat eine detaillierte Beschreibung in `agent_roles/`:

1. **[01_query_analyzer.md](agent_roles/01_query_analyzer.md)**
   - Verstehe User-Intent
   - Zerlege komplexe Fragen
   - Erstelle Suchbegriffe
   - Definiere Erfolgs-Kriterien

2. **[02_web_researcher.md](agent_roles/02_web_researcher.md)**
   - Iterative Suche via SearXNG
   - Quellen-Qualität bewerten
   - Result-Ranking
   - Selection Strategy

3. **[03_content_extractor.md](agent_roles/03_content_extractor.md)**
   - Content Fetching (web_fetch)
   - Information Extraction
   - Strukturierte Daten
   - Quality Check

4. **[04_domain_expert.md](agent_roles/04_domain_expert.md)**
   - Cross-Source Analysis
   - Critical Evaluation
   - Practical Insights
   - Recommendations

5. **[05_synthesizer.md](agent_roles/05_synthesizer.md)**
   - Information Integration
   - Structure Creation
   - Quality Control
   - Output Templates

6. **[06_report_writer.md](agent_roles/06_report_writer.md)**
   - Format Optimization
   - Readability Enhancement
   - User Experience
   - Final Quality Check

## 💡 Wie Claude die Rollen nutzt

### Beispiel: "Recherchiere RSI Mean Reversion mit Backtests"

**Phase 1: Query Analyzer**
```
🎯 Intent: Comparative Analysis
📊 Domain: Trading Strategies
🔍 Sub-queries:
  - RSI mean reversion basics
  - Optimal parameters
  - Backtest results
```

**Phase 2: Web Researcher**
```
🔍 Search: "RSI mean reversion backtest"
📈 Found: 47 results
✅ Selected: 8 high-quality sources
   - 3 academic papers
   - 3 trading blogs
   - 2 forum discussions
```

**Phase 3: Content Extractor**
```
🌐 Fetching: 8 URLs via web_fetch
📄 Extracting:
   - Performance metrics
   - Parameter values
   - Methodology details
```

**Phase 4: Domain Expert**
```
🧠 Analysis:
   - Consensus: 30/70 thresholds (4/5 sources)
   - Red flag: One source claims 45% CAGR (unrealistic)
   - Practical: Requires 50+ positions for diversification
```

**Phase 5: Synthesizer**
```
📋 Combining findings:
   - Performance: 12-15% CAGR, Sharpe 1.5-2.0
   - Parameters: 30/70 thresholds, 1-5 days holding
   - Caveats: Underperforms in trends
```

**Phase 6: Report Writer**
```
✍️ Chat Response: Concise summary (300 words)
📁 Full Report: Saved to /reports/rsi_mean_reversion_20251205.md
```

## 🎯 Vorteile dieses Ansatzes

| Aspect | Multi-Agent LLM System | Claude Multi-Role |
|--------|------------------------|-------------------|
| **API Costs** | 5-6 API calls per research | €0 (Claude already here) |
| **Context Loss** | Between agents | Preserved across roles |
| **Flexibility** | Fixed workflow | Adaptive based on query |
| **Quality Control** | Automated | Human-in-the-loop |
| **Debugging** | Complex logs | Direct conversation |

## 📖 Für Claude: Wie die Rollen nutzen

**Beim Research-Task:**

1. **Lies die relevante Rolle-Datei** bevor du loslegst
2. **Folge dem Framework** in der Rolle-Beschreibung
3. **Nutze die Tools** wie in der Rolle dokumentiert
4. **Wechsle zur nächsten Rolle** nach Abschluss der Phase

**Beispiel:**
```
User: "Recherchiere RSI Mean Reversion"

Claude (intern):
1. [Lese 01_query_analyzer.md]
2. [Analysiere Query nach Framework]
3. [Wechsel zu Web Researcher]
4. [Lese 02_web_researcher.md]
5. [Führe Suche durch]
...
```

## 🔧 Anpassung der Rollen

**Für neue Domains:**
- Füge domain-spezifische Guidelines hinzu
- Erweitere Evaluation Checklists
- Ergänze Output-Templates

**Für neue Tools:**
- Update Tool-Sections in relevanten Rollen
- Dokumentiere Best Practices
- Ergänze Beispiele

## 📝 Best Practices

### Für Claude:
- **Transparenz:** Zeige welche Rolle du gerade nutzt (optional, bei komplexen Tasks)
- **Flexibility:** Skip Rollen die nicht nötig sind
- **Quality:** Folge den Checklists
- **Efficiency:** Nicht jeder Task braucht alle 6 Rollen

### Für den User:
- **Specificity:** Je klarer die Frage, desto besser
- **Feedback:** Sag wenn Output nicht passt
- **Iteration:** Research kann verfeinert werden

## 🚀 Einsatzbereit

Das Agent-Roles-System ist dokumentiert und ready to use!

**Für die erste Research-Aufgabe:**
Gib mir einfach eine Frage, und ich wende die Rollen-Frameworks automatisch an!

---

**Version:** 1.0.0  
**Last Updated:** 2025-12-05  
**Location:** `/home/carsten/research/agent_roles/`
