from pathlib import Path
import re

path = Path("japan-trip/index.html")
html = path.read_text(encoding="utf-8")

# Add a small legend and visual treatment to every detailed itinerary row.
css = r'''<style id="itinerary-types">
.type-legend{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0 4px;padding:10px 12px;background:#f8f9fc;border:1px solid #e2e6ef;border-radius:12px}
.type-chip{display:inline-flex;align-items:center;gap:5px;padding:5px 9px;border-radius:999px;font-size:11px;font-weight:850;line-height:1;border:1px solid #dfe3ec;background:#fff}
.type-badge{display:inline-flex;align-items:center;gap:5px;margin:0 0 7px;padding:5px 9px;border-radius:999px;font-size:11px;font-weight:900;letter-spacing:.02em;border:1px solid #dfe3ec;background:#f7f8fb}
.row.type-transit .type-badge{background:#eef0ff;color:#414dcc;border-color:#d9ddff}
.row.type-sightseeing .type-badge{background:#eaf8ef;color:#14744e;border-color:#cdebd9}
.row.type-food .type-badge{background:#fff1e7;color:#a85d00;border-color:#f3d5bb}
.row.type-break .type-badge{background:#fff8df;color:#8a6500;border-color:#eedfa8}
.row.type-sleep .type-badge{background:#eeeafd;color:#5b43a5;border-color:#ddd4fb}
.row.type-hotel .type-badge{background:#f0f3f8;color:#455266;border-color:#dce2eb}
.row.type-flight .type-badge{background:#e9f5ff;color:#17648f;border-color:#cbe5f7}
.row.type-shopping .type-badge{background:#fff0f5;color:#a23d68;border-color:#f0cede}
.row.type-walk .type-badge{background:#eef8f7;color:#176c67;border-color:#d1eae8}
.row.type-other .type-badge{background:#f2f4f7;color:#596273;border-color:#e0e4ea}
@media(max-width:820px){.type-legend{gap:6px}.type-chip{font-size:10px;padding:5px 7px}.type-badge{font-size:10px}}
</style>'''

if 'id="itinerary-types"' not in html:
    html = html.replace('</head>', css + '</head>', 1)

legend = '''<div class="type-legend" aria-label="Itinerary activity legend">
<span class="type-chip">🚆 Transit</span><span class="type-chip">📍 Sightseeing</span><span class="type-chip">🍜 Food</span><span class="type-chip">☕ Break / prep</span><span class="type-chip">🛏️ Sleep</span><span class="type-chip">🏨 Hotel</span><span class="type-chip">✈️ Flight / airport</span><span class="type-chip">🛍️ Shopping</span><span class="type-chip">🚶 Walk</span><span class="type-chip">ℹ️ Other</span>
</div>'''

# Put the legend at the start of each day card, without changing the itinerary content.
if html.count('class="type-legend"') == 0:
    html = html.replace('<div class="card day"><h3>Keep arrival day local</h3>', '<div class="card day"><h3>Keep arrival day local</h3>' + legend, 1)
    html = html.replace('<div class="card day"><h3>Asakusa → Ueno → Ameyoko → Akihabara → Kappabashi → Skytree</h3>', '<div class="card day"><h3>Asakusa → Ueno → Ameyoko → Akihabara → Kappabashi → Skytree</h3>' + legend, 1)
    html = html.replace('<div class="card day"><div class="timeline">', '<div class="card day">' + legend + '<div class="timeline">', 1)

# Classification is intentionally based on the action title, not the explanatory text.
def classify(title: str):
    t = title.lower().strip()
    if any(x in t for x in ['jl754', 'jl58', 'land at narita', 'narita t2 arrival']):
        return ('flight', '✈️', 'FLIGHT / AIRPORT')
    if any(x in t for x in ['dinner', 'lunch', 'breakfast', 'udon']):
        return ('food', '🍜', 'FOOD STOP')
    if any(x in t for x in ['check-in', 'checkout', 'hotel →', 'return to hotel']):
        return ('hotel', '🏨', 'HOTEL')
    if any(x in t for x in ['pack and prepare']):
        return ('break', '☕', 'BREAK / PREP')
    if any(x in t for x in ['walk to', 'walk back', 'walk toward', 'short final asakusa / sumida walk']):
        return ('walk', '🚶', 'WALK')
    if any(x in t for x in ['access express', 'ginza line', 'honjo-azumabashi →', 'honjo → narita', '→ narita t2', 'suehirocho g14 →', 'inaricho g17 →']):
        return ('transit', '🚆', 'TRANSIT')
    if any(x in t for x in ['ueno park', 'ameyoko', 'senso-ji', 'sumida river', 'azumabashi', 'kaminarimon', 'akihabara', 'kappabashi', 'tokyo skytree']):
        return ('sightseeing', '📍', 'SIGHTSEEING')
    if any(x in t for x in ['sleep', 'bed', 'rest']):
        return ('sleep', '🛏️', 'SLEEP')
    if any(x in t for x in ['shopping']):
        return ('shopping', '🛍️', 'SHOPPING')
    return ('other', 'ℹ️', 'OTHER')

# Each row has <div class="time"> then the content div. Insert badge at top of content.
pattern = re.compile(r'(<div class="row">\s*<div class="time">.*?</div>\s*<div>\s*)(<strong>(.*?)</strong>)', re.S)

def repl(m):
    prefix, strong_html, title = m.group(1), m.group(2), re.sub('<[^>]+>', '', m.group(3))
    kind, icon, label = classify(title)
    # Avoid double insertion if the workflow is manually rerun against an already-enhanced source.
    if 'type-badge' in prefix:
        return m.group(0)
    badge = f'<div class="type-badge" aria-label="{label}">{icon} {label}</div>'
    # Add type class to the nearest row opening.
    start = prefix.rfind('<div class="row">')
    prefix2 = prefix[:start] + prefix[start:].replace('<div class="row">', f'<div class="row type-{kind}">', 1)
    return prefix2 + badge + strong_html

html = pattern.sub(repl, html)
path.write_text(html, encoding="utf-8")
print("Enhanced itinerary rows with activity type badges.")
