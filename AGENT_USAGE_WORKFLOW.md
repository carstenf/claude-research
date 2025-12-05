# Agent Usage Workflow für Claude

## 🎯 Mandatory Reading Order

**BEVOR ich das Research System nutze, muss ich IMMER diese Dokumente in dieser Reihenfolge lesen:**

### 1. CLAUDE_RESEARCH_CHECKLIST.md ⚠️ (HIGHEST PRIORITY)
- **Wann:** Vor JEDER Research-Aufgabe
- **Warum:** Verhindert API-Key Fehler
- **Inhalt:** 
  - Kein API Key vom User nötig!
  - Service Status Check
  - Implementation Rules
  - Common Mistakes

### 2. AGENT_ROLES_GUIDE.md 🎭
- **Wann:** Beim Start einer Research-Aufgabe
- **Warum:** Verstehe welche Rollen ich nutze
- **Inhalt:**
  - 6 Agent Rollen Overview
  - Wann welche Rolle nutzen
  - Best Practices

### 3. Spezifische Rollen-Dateien (je nach Phase)
- **Wann:** Bei Eintritt in jeweilige Phase
- **Dateien:** `agent_roles/01_query_analyzer.md` bis `06_report_writer.md`
- **Warum:** Detaillierte Anweisungen für Phase

### 4. ANTHROPIC_API_GUIDE.md 📚
- **Wann:** Beim Erstellen von Artifacts mit API-Calls
- **Warum:** Technische Details der API-Nutzung
- **Inhalt:**
  - API Call Examples
  - Error Handling
  - Integration Patterns

---

## 📋 Complete Workflow Example

### User fragt: "Recherchiere Mean Reversion Strategien mit RSI"

#### Step 1: Pre-Flight Check
```markdown
✅ Lese CLAUDE_RESEARCH_CHECKLIST.md
   - Kein API Key nötig? ✓
   - Services running? ✓
   - Artifact oder Script? → Artifact (UI nötig)
```

#### Step 2: Role Framework Activation
```markdown
✅ Lese AGENT_ROLES_GUIDE.md
   - 6 Rollen identifiziert
   - Workflow verstanden
   - Wechsel zu Phase 1
```

#### Step 3: Phase 1 - Query Analysis
```markdown
✅ Lese agent_roles/01_query_analyzer.md
   - Intent: Research + Comparison
   - Domain: Trading Strategies
   - Sub-queries definiert
   - Success criteria festgelegt
```

#### Step 4: Phase 2 - Web Research
```markdown
✅ Lese agent_roles/02_web_researcher.md
   - SearXNG nutzen auf Port 8889
   - Search terms: "RSI mean reversion backtest"
   - Quality filtering
   - Top 5-10 Quellen auswählen
```

#### Step 5: Phase 3-6
```markdown
✅ Content Extraction (03_content_extractor.md)
✅ Domain Expert Analysis (04_domain_expert.md)
✅ Synthesis (05_synthesizer.md)
✅ Report Writing (06_report_writer.md)
```

#### Step 6: Implementation
```markdown
✅ Lese ANTHROPIC_API_GUIDE.md
   - Erstelle React Artifact
   - API Calls integriert
   - KEIN API Key vom User
   - Services auf 128.140.104.236:8889/8000
```

---

## 🚦 Decision Tree

```
User Request
    │
    ├─> Einfache Frage? (keine UI nötig)
    │   └─> Direkt antworten, keine Rollen nötig
    │
    ├─> Research-Aufgabe?
    │   ├─> 1. Lese CLAUDE_RESEARCH_CHECKLIST.md
    │   ├─> 2. Lese AGENT_ROLES_GUIDE.md
    │   ├─> 3. Folge 6 Rollen-Workflow
    │   └─> 4. Bei Artifact: Lese ANTHROPIC_API_GUIDE.md
    │
    └─> Technische Implementierung?
        └─> Lese ANTHROPIC_API_GUIDE.md für Details
```

---

## 📁 File Structure & Purpose

```
/home/carsten/research/
│
├── CLAUDE_RESEARCH_CHECKLIST.md    ← START HERE (immer!)
├── AGENT_ROLES_GUIDE.md             ← Then read this
├── AGENT_USAGE_WORKFLOW.md          ← This file (reference)
├── ANTHROPIC_API_GUIDE.md           ← Technical API details
│
├── agent_roles/                     ← Detailed role descriptions
│   ├── 01_query_analyzer.md
│   ├── 02_web_researcher.md
│   ├── 03_content_extractor.md
│   ├── 04_domain_expert.md
│   ├── 05_synthesizer.md
│   └── 06_report_writer.md
│
├── STATUS.md                        ← Current system status
├── IRON_CONDOR_ANALYSIS_PLAN.md     ← Specific project
└── README.md                        ← User documentation
```

---

## ✅ Quality Checklist

**Vor jeder Response check ich:**

- [ ] CLAUDE_RESEARCH_CHECKLIST.md gelesen?
- [ ] Kein API Key vom User verlangt?
- [ ] Richtige Rollen identifiziert?
- [ ] Services verfügbar geprüft?
- [ ] Artifact vs Script Entscheidung getroffen?
- [ ] Error Handling implementiert?
- [ ] User bekommt sofort funktionierendes System?

---

## 🎯 Success Metrics

**Guter Research Output wenn:**
- ✅ User muss NICHTS konfigurieren
- ✅ System funktioniert sofort
- ✅ Alle 6 Rollen wurden sinnvoll angewandt
- ✅ Ergebnis ist konkret und umsetzbar
- ✅ Quellen sind hochwertig und relevant

---

## 📝 Template für Claude's Interne Notizen

```
=== RESEARCH TASK START ===

[✓] CHECKLIST gelesen
[✓] Services: ChromaDB ✓, SearXNG ✓
[✓] Approach: React Artifact mit API integration

PHASE 1 - Query Analysis:
  Intent: [...]
  Domain: [...]
  Sub-queries: [...]

PHASE 2 - Web Research:
  Search: [...]
  Sources: [...]
  
[... weitere Phasen ...]

=== RESEARCH TASK COMPLETE ===
```

---

**Version:** 1.0  
**Last Updated:** 2025-12-05  
**Purpose:** Master guide für Claude's research workflow
