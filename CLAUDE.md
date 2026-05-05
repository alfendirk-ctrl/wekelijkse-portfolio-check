# Aandelen Briefing — Claude Code Routine

Je genereert elke maandag om 08:00 een HTML e-mail briefing over de aandelen op de watchlist.
Het resultaat schrijf je weg als `email_final.html` in de root van deze repo, en je commit en pusht naar GitHub.

---

## Stap 1 — Lees de watchlist

Lees `watchlist.json`. Dit zijn de aandelen waarvoor je de briefing genereert.

---

## Stap 2 — Haal data op via web search

Gebruik web search voor actuele informatie. Zoek per sectie:

**Sectie 1 – Stock Screener**
Zoek naar: "undervalued stocks strong fundamentals low debt earnings growth [huidige maand jaar]"
Filter de watchlist: welke aandelen hebben momenteel:
- Lage P/E of PEG ratio (< 1.5 is aantrekkelijk)
- Lage debt-to-equity (< 0.5 is sterk)
- Positieve recente earnings (beat of in lijn)
- Consistente omzet- of winstgroei

Noem maximaal 5 aandelen uit de watchlist die het sterkst scoren. Geef per aandeel: ticker, naam, 2-3 concrete metrics, en 1 zin analyse.

**Sectie 2 – Sectortrends**
Zoek naar: "sector performance this week [huidige datum]" en "sector rotation outlook [huidige maand jaar]"
Analyseer de sectoren relevant voor de watchlist:
- Technology (NVDA, MSFT, CRWD, QLYS, ASML, LOGN)
- Consumer Discretionary (TSLA, SHOP, SPOT, RDDT)
- Healthcare (UNH)
- Industrials / Defense (LMT, AIR)
- Financials / Crypto (CRCL)
- Consumer Staples (NESN)
- Enterprise Software (CRM, ASML, WKL)

Geef per sector: wekelijkse performance (%), momentum-signaal (sterk / neutraal / zwak), en 1 zin toelichting.

**Sectie 3 – Earnings Tracker**
Zoek naar earnings voor elk aandeel op de watchlist in de komende 4 weken.
Zoek per aandeel: "[TICKER] earnings date Q[kwartaal] [jaar]"
Geef per aandeel met aankomende earnings: datum, verwacht EPS, en een signaal (Beat verwacht / Neutraal / Miss risico) op basis van analyst consensus en recente trend.
Aandelen zonder aankomende earnings in de komende 4 weken sla je over.

**Sectie 4 – Spotlight**
Kies één aandeel van de watchlist dat deze week de meeste aandacht verdient.
Criteria: meest beweging, sterkste catalyst, of interessantste set-up technisch of fundamenteel.
Schrijf een analyse van ~150 woorden: wat speelt er, wat zijn de bull/bear argumenten, en wat is jouw verwachting op korte termijn.

---

## Stap 3 — Genereer email_final.html

Schrijf het volledige HTML-bestand hieronder beschreven. Gebruik uitsluitend inline CSS (geen externe stylesheets, geen CDN). De e-mail moet correct renderen in Gmail.

### HTML structuur

```
<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width"></head>
<body style="margin:0;padding:0;background:#f4f4f0;font-family:Georgia,serif;">
  <table width="100%" cellpadding="0" cellspacing="0">
    <tr><td align="center" style="padding:24px 16px;">
      <table width="640" cellpadding="0" cellspacing="0" style="max-width:640px;width:100%;">

        <!-- HEADER -->
        <tr><td style="background:#0C2340;padding:28px 32px 20px;border-radius:12px 12px 0 0;">
          <p style="margin:0 0 6px;font-size:11px;letter-spacing:0.12em;text-transform:uppercase;color:#7BA7C9;font-family:Arial,sans-serif;">[DAG] [DATUM] · Wekelijkse briefing</p>
          <h1 style="margin:0 0 4px;font-size:24px;font-weight:400;color:#ffffff;">Aandelen Analyse</h1>
          <p style="margin:0;font-size:13px;color:#7BA7C9;font-family:Arial,sans-serif;">Screener · Sectortrends · Earnings · Spotlight</p>
        </td></tr>

        <!-- MARKTBALK -->
        <tr><td style="background:#0F2D50;padding:12px 32px;">
          <table width="100%" cellpadding="0" cellspacing="0">
            <tr>
              <td style="font-family:Arial,sans-serif;font-size:12px;color:#7BA7C9;padding-right:20px;">S&amp;P 500 <span style="color:[KLEUR_SP];">[SP500]</span></td>
              <td style="font-family:Arial,sans-serif;font-size:12px;color:#7BA7C9;padding-right:20px;">NASDAQ <span style="color:[KLEUR_NQ];">[NASDAQ]</span></td>
              <td style="font-family:Arial,sans-serif;font-size:12px;color:#7BA7C9;padding-right:20px;">AEX <span style="color:[KLEUR_AEX];">[AEX]</span></td>
              <td style="font-family:Arial,sans-serif;font-size:12px;color:#7BA7C9;padding-right:20px;">VIX <span style="color:#ffffff;">[VIX]</span></td>
              <td style="font-family:Arial,sans-serif;font-size:12px;color:#7BA7C9;">10Y <span style="color:#ffffff;">[RENTE]%</span></td>
            </tr>
          </table>
        </td></tr>

        <!-- SECTIE 1: SCREENER -->
        <tr><td style="background:#ffffff;padding:24px 32px;border-bottom:1px solid #eee;">
          <p style="margin:0 0 8px;font-size:10px;letter-spacing:0.15em;text-transform:uppercase;color:#999;font-family:Arial,sans-serif;">Sectie 1 · Stock Screener</p>
          <h2 style="margin:0 0 16px;font-size:16px;font-weight:500;font-family:Arial,sans-serif;color:#1a1a1a;">Ondergewaardeerde aandelen — watchlist picks</h2>
          [SCREENER_KAARTJES]
          <p style="margin:12px 0 0;font-size:13px;line-height:1.7;color:#444;">[SCREENER_ANALYSE]</p>
        </td></tr>

        <!-- SECTIE 2: SECTORTRENDS -->
        <tr><td style="background:#ffffff;padding:24px 32px;border-bottom:1px solid #eee;">
          <p style="margin:0 0 8px;font-size:10px;letter-spacing:0.15em;text-transform:uppercase;color:#999;font-family:Arial,sans-serif;">Sectie 2 · Sectortrends</p>
          <h2 style="margin:0 0 16px;font-size:16px;font-weight:500;font-family:Arial,sans-serif;color:#1a1a1a;">Momentum per sector</h2>
          [SECTOR_RIJEN]
          <p style="margin:12px 0 0;font-size:13px;line-height:1.7;color:#444;">[SECTOR_ANALYSE]</p>
        </td></tr>

        <!-- SECTIE 3: EARNINGS -->
        <tr><td style="background:#ffffff;padding:24px 32px;border-bottom:1px solid #eee;">
          <p style="margin:0 0 8px;font-size:10px;letter-spacing:0.15em;text-transform:uppercase;color:#999;font-family:Arial,sans-serif;">Sectie 3 · Earnings Tracker</p>
          <h2 style="margin:0 0 16px;font-size:16px;font-weight:500;font-family:Arial,sans-serif;color:#1a1a1a;">Aankomende rapporten — watchlist</h2>
          [EARNINGS_TABEL]
        </td></tr>

        <!-- SECTIE 4: SPOTLIGHT -->
        <tr><td style="background:#ffffff;padding:24px 32px;">
          <p style="margin:0 0 8px;font-size:10px;letter-spacing:0.15em;text-transform:uppercase;color:#999;font-family:Arial,sans-serif;">Sectie 4 · Spotlight</p>
          <h2 style="margin:0 0 4px;font-size:16px;font-weight:500;font-family:Arial,sans-serif;color:#1a1a1a;">[SPOTLIGHT_TICKER] — [SPOTLIGHT_NAAM]</h2>
          <p style="margin:0 0 14px;font-size:13px;color:#185FA5;font-family:Arial,sans-serif;">[SPOTLIGHT_SUBTITEL]</p>
          <p style="margin:0;font-size:14px;line-height:1.8;color:#333;">[SPOTLIGHT_TEKST]</p>
        </td></tr>

        <!-- FOOTER -->
        <tr><td style="background:#f4f4f0;padding:16px 32px;border-radius:0 0 12px 12px;">
          <p style="margin:0;font-size:11px;color:#999;font-family:Arial,sans-serif;">Gegenereerd door Claude Code · Elke maandag 08:00 · alfendirk-ctrl/aandelen-briefing</p>
        </td></tr>

      </table>
    </td></tr>
  </table>
</body>
</html>
```

### Invulregels

**[SCREENER_KAARTJES]**: Genereer per geselecteerd aandeel een inline tabel-kaartje:
```html
<table style="display:inline-table;margin:0 8px 8px 0;background:#f8f8f6;border-radius:8px;padding:10px 14px;vertical-align:top;">
  <tr><td style="font-family:Arial,sans-serif;font-size:13px;font-weight:600;color:#1a1a1a;">[TICKER]</td></tr>
  <tr><td style="font-family:Arial,sans-serif;font-size:11px;color:#666;padding-bottom:6px;">[NAAM]</td></tr>
  <tr><td>
    <span style="font-size:10px;background:#EAF3DE;color:#3B6D11;padding:2px 7px;border-radius:20px;margin-right:4px;">[BADGE1]</span>
    <span style="font-size:10px;background:#E6F1FB;color:#185FA5;padding:2px 7px;border-radius:20px;">[BADGE2]</span>
  </td></tr>
</table>
```
Gebruik groene badges voor positieve metrics (lage P/E, goede groei), blauwe badges voor neutrale metrics.

**[SECTOR_RIJEN]**: Genereer per sector een rij met naam, gekleurde tekst voor percentage, en 1-zin toelichting:
```html
<table width="100%" cellpadding="0" cellspacing="4" style="margin-bottom:8px;">
  <tr>
    <td width="160" style="font-family:Arial,sans-serif;font-size:13px;color:#1a1a1a;">[SECTOR]</td>
    <td width="60" style="font-family:Arial,sans-serif;font-size:13px;font-weight:600;color:[KLEUR];">[PCT]%</td>
    <td style="font-family:Arial,sans-serif;font-size:12px;color:#666;">[TOELICHTING]</td>
  </tr>
</table>
```
Kleur: #3B6D11 voor positief, #A32D2D voor negatief, #854F0B voor neutraal.

**[EARNINGS_TABEL]**: HTML tabel met kolommen: Ticker | Naam | Datum | EPS verwacht | Signaal
Signaal-badges:
- Beat verwacht: `background:#EAF3DE;color:#3B6D11`
- Neutraal: `background:#f4f4f0;color:#666`
- Miss risico: `background:#FCEBEB;color:#A32D2D`

**Kleuren marktbalk**: #5DCAA5 voor positief, #F09595 voor negatief.

---

## Stap 4 — Commit en push

Nadat email_final.html is geschreven:

```bash
git config user.email "claude-routine@anthropic"
git config user.name "Claude Routine"
git add email_final.html
git commit -m "briefing: aandelen analyse $(date +'%Y-%m-%d')"
git push origin main
```

Gebruik de `GH_PAT` environment variable als dat nodig is voor authenticatie:
```bash
git remote set-url origin https://x-access-token:${GH_PAT}@github.com/alfendirk-ctrl/aandelen-briefing.git
```

---

## Foutafhandeling

- Als web search geen data oplevert voor een aandeel: vermeld "geen data beschikbaar" en ga door.
- Als git push mislukt: schrijf de fout naar `error_log.txt` en commit dat bestand.
- Schrijf nooit een leeg of onvolledig email_final.html weg.
