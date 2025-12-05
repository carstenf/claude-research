# Anthropic API Usage Guide for Claude Research System

## 🔑 Key Concept: No API Key Required

**Claude kann die Anthropic API direkt nutzen OHNE dass der User einen API Key bereitstellen muss.**

Dies funktioniert wenn:
- Claude Artifacts (HTML/React) erstellt
- Claude die API innerhalb des Artifacts aufruft
- Die Authentifizierung wird automatisch von Claude.ai gehandhabt

## 📋 API Usage in Artifacts

### Basic Setup (React Artifact)

```javascript
const response = await fetch("https://api.anthropic.com/v1/messages", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    // KEIN API KEY benötigt! Claude.ai handled das automatisch
  },
  body: JSON.stringify({
    model: "claude-sonnet-4-20250514",
    max_tokens: 1000,
    messages: [
      { role: "user", content: "Your prompt here" }
    ],
  })
});

const data = await response.json();
```

### Response Format

```javascript
{
  content: [
    {
      type: "text",
      text: "Claude's response here"
    }
    // Mögliche andere types: tool_use, tool_result, image, document
  ],
}
```

## ⚠️ Critical Rules

### Was NICHT funktioniert:
- ❌ `localStorage` / `sessionStorage` in Artifacts
- ❌ Browser storage APIs
- ❌ Cookies

### Was funktioniert:
- ✅ React State (`useState`, `useReducer`)
- ✅ In-Memory Variablen
- ✅ Fetch zu externen APIs
- ✅ Anthropic API ohne Key

### Error Handling

```javascript
try {
  const response = await fetch("https://api.anthropic.com/v1/messages", {...});
  
  if (!response.ok) {
    throw new Error(`API Error: ${response.status}`);
  }
  
  const data = await response.json();
  const fullText = data.content
    .filter(item => item.type === "text")
    .map(item => item.text)
    .join("\n");
    
} catch (error) {
  console.error("Claude API error:", error);
}
```

## 🎯 Workflow Checkliste

**Bevor ich das Research System nutze, muss ich:**

1. ✅ Prüfen ob Artifact-Ansatz sinnvoll ist
2. ✅ Kein API Key vom User verlangen
3. ✅ Anthropic API direkt im Artifact nutzen
4. ✅ SearXNG/ChromaDB auf Server (128.140.104.236) verfügbar
5. ✅ Structured outputs via JSON prompt engineering
6. ✅ Error handling implementieren
7. ✅ Kein localStorage verwenden

---

**Last Updated:** 2025-12-05
**Version:** 1.0
**Author:** Claude (for Carsten)
