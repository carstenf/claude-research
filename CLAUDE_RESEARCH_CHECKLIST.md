# ⚠️ MANDATORY: Read Before Using Research System

## 🔴 CRITICAL REMINDER

**Claude benötigt KEINEN API Key vom User!**

Die Anthropic API kann direkt in Artifacts aufgerufen werden.
Die Authentifizierung erfolgt automatisch über Claude.ai.

---

## ✅ Pre-Use Checklist

Vor jeder Nutzung des Research Systems MUSS ich:

### 1. API Key Verifikation
- [ ] **NICHT** nach Anthropic API Key fragen
- [ ] Artifacts mit direktem API-Aufruf erstellen
- [ ] `fetch("https://api.anthropic.com/v1/messages")` ohne API Key Header

### 2. Service Status Check
```bash
curl http://128.140.104.236:8000/api/v1/heartbeat  # ChromaDB
curl http://128.140.104.236:8889  # SearXNG
docker compose ps  # Services running?
```

### 3. Implementation Rules
- [ ] ❌ KEIN localStorage/sessionStorage in Artifacts
- [ ] ✅ React State oder In-Memory Variablen
- [ ] ✅ Anthropic API direkt aufrufen
- [ ] ✅ SearXNG auf Port 8889 verfügbar
- [ ] ✅ ChromaDB auf Port 8000 verfügbar

---

## 🚫 Common Mistakes to AVOID

1. ❌ "Please add your Anthropic API key to .env"
2. ❌ "You need to set ANTHROPIC_API_KEY environment variable"
3. ❌ Using localStorage in Artifacts
4. ❌ Asking for API keys in general
5. ❌ Creating .env files for Anthropic API

## ✅ What to DO Instead

1. ✅ Create Artifact with direct API calls
2. ✅ Use React State for session data
3. ✅ Leverage server services (SearXNG, ChromaDB)
4. ✅ Provide immediate working solution
5. ✅ No configuration needed from user

---

## 🎯 When User Says: "Research X"

**My Response Should Be:**

```
1. "Ich erstelle dir ein Research Interface..."
2. [Create React Artifact with Anthropic API integration]
3. [No mention of API keys]
4. [Working system immediately]
```

**NOT:**

```
❌ "Du musst zuerst deinen API Key eintragen..."
❌ "Konfiguriere .env mit ANTHROPIC_API_KEY..."
❌ "Ohne API Key kann ich nicht..."
```

---

## 📊 Success Criteria

- [ ] User kann SOFORT loslegen
- [ ] KEINE Konfiguration nötig
- [ ] System funktioniert direkt
- [ ] API calls erfolgreich
- [ ] Services erreichbar

---

**REMEMBER:** 
- No API keys needed
- Services already running
- Create working solutions immediately
- User should have zero friction

---

**Last Updated:** 2025-12-05
**Read This:** EVERY TIME before using research system
