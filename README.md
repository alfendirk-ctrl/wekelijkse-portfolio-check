# aandelen-briefing

Wekelijkse aandelen analyse per e-mail, gegenereerd door Claude Code Routines.

## Wat doet dit?

Elke maandag om 08:00 draait een Claude Code Routine die:
1. De watchlist leest (`watchlist.json`)
2. Actuele marktdata ophaalt via web search
3. Een HTML e-mail genereert (`email_final.html`) met:
   - Stock Screener — ondergewaardeerde picks van de watchlist
   - Sectortrends — momentum per sector
   - Earnings Tracker — aankomende rapporten
   - Spotlight — één aandeel diep uitgelicht
4. De HTML commit en pusht naar GitHub

Om 08:15 stuurt een GitHub Action de e-mail via Gmail SMTP.

## Setup

### 1. GitHub Secrets instellen

Ga naar `Settings → Secrets → Actions` en voeg toe:
- `GMAIL_USER` — jouw Gmail-adres
- `GMAIL_APP_PASSWORD` — Gmail App Password (spaties worden automatisch gestript)

### 2. Cloud Environment in Claude Code

Maak een nieuwe Cloud Environment aan met naam `aandelen-briefing` en voeg toe:
- `GH_PAT` — GitHub Personal Access Token met `repo` scope
- `GMAIL_USER` — zelfde als hierboven
- `GMAIL_APP_PASSWORD` — zelfde als hierboven

### 3. Routine aanmaken in Claude Code

Ga naar [claude.ai/code/routines](https://claude.ai/code/routines) en maak een nieuwe routine:
- **Repository**: `alfendirk-ctrl/aandelen-briefing`
- **Environment**: `aandelen-briefing`
- **Trigger**: Weekly, maandag 08:00
- **Prompt**: zie hieronder

### Routine prompt

```
Voer de instructies uit in CLAUDE.md.
```

Dat is genoeg — CLAUDE.md bevat alle stappen.

### 4. Watchlist aanpassen

Bewerk `watchlist.json` om aandelen toe te voegen of te verwijderen.

## Bestanden

| Bestand | Doel |
|---|---|
| `watchlist.json` | Aandelen op de watchlist |
| `CLAUDE.md` | Instructies voor de Claude Code Routine |
| `send_email.py` | Verstuurt email_final.html via Gmail SMTP |
| `.github/workflows/send_email.yml` | GitHub Action (maandag 08:15) |
| `email_final.html` | Gegenereerde briefing (wordt elke week overschreven) |
