# Agent Roles for Claude

## Konzept

Anstatt separate LLM Agents mit eigenen API Calls zu haben, übernimmt **Claude dynamisch verschiedene Rollen** während des Research-Prozesses.

Jede Rolle hat:
- **Klare Verantwortlichkeiten**
- **Spezifische Tools/Methoden**
- **Output-Format**

Claude wechselt zwischen Rollen basierend auf der aktuellen Phase des Research.

## Verfügbare Rollen

1. **Query Analyzer** - Verstehe und strukturiere die Research-Anfrage
2. **Web Researcher** - Suche und bewerte Web-Quellen
3. **Content Extractor** - Hole und parse relevante Inhalte
4. **Domain Expert** - Analysiere mit Fach-Expertise
5. **Synthesizer** - Kombiniere und strukturiere Findings
6. **Report Writer** - Erstelle finale Reports

Jede Rolle hat eine eigene Datei mit detaillierten Prompts/Guidelines.
