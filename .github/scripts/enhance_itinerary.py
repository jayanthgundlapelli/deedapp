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

# Keep paid alternatives out of the core itinerary, but make the section actionable.
# Prices are planning estimates in INR using ¥1 ≈ ₹0.60. The exact JPY price and same-day hours should be rechecked on the official site.
paid_section = '''<section id="paid"><div class="title"><h2>Paid attractions &amp; route alternatives</h2><p>These are NOT added to the core itinerary automatically. Each option shows the approximate adult price in INR, current published opening hours, and exactly where it fits if you choose to swap it into the route.</p></div><div class="note"><strong>Planning rate:</strong> INR figures use approximately ¥1 = ₹0.60. Treat these as budget numbers, not card-settlement amounts. Recheck the official ticket page on the day.</div><div class="grid g2" style="margin-top:16px">
<div class="card"><span class="pill paid">CORE PLAN · DAY 2</span><h3>Tokyo Skytree · ~₹1,080–₹1,800</h3><p><strong>JPY:</strong> ¥1,800+ for Tembo Deck or ¥3,000+ for Deck + Galleria online. <strong>Hours on Sat Sep 12:</strong> plan around 09:00-22:00; exact date hours should be checked on the official calendar.</p><p><strong>Best fit:</strong> Saturday 17:35 onward. This is already in the route and is the best use of paid sightseeing time because you can see daylight, sunset around 18:07 and the night skyline.</p><a class="btn" href="https://www.tokyo-skytree.jp/ticket/" target="_blank">Official tickets</a></div>
<div class="card"><span class="pill paid">BEST ADD-ON · DAY 2</span><h3>Sumida Aquarium · ~₹1,500</h3><p><strong>Adult:</strong> ¥2,500. <strong>Weekend hours:</strong> 09:00-21:00, last entry 60 minutes before closing.</p><p><strong>Best fit:</strong> Saturday in the Skytree area. Best as a swap for part of Skytree time, for example Skytree 17:35-19:00 → Aquarium 19:00-20:00 → dinner. It adds almost no transport.</p><a class="btn" href="https://www.gotokyo.org/en/spot/67/index.html" target="_blank">Current details</a></div>
<div class="card"><span class="pill paid">BEST VALUE CULTURE · DAY 2</span><h3>Edo-Tokyo Museum · ~₹480</h3><p><strong>Permanent exhibition:</strong> ¥800. <strong>Hours:</strong> 09:30-17:30 on most days, until 19:30 on Saturdays. Closed Mondays.</p><p><strong>Best fit:</strong> Saturday morning, replacing Ueno Park. It is in Ryogoku, so it is a small route change from Asakusa, but it gives much more historical context for Tokyo.</p><a class="btn" href="https://www.edo-tokyo-museum.or.jp/en/information/guide/" target="_blank">Official tickets</a><a class="btn map" href="https://www.google.com/maps/search/?api=1&query=Edo-Tokyo+Museum" target="_blank">Map</a></div>
<div class="card"><span class="pill paid">BEST UENO SWAP · DAY 2</span><h3>National Museum of Nature &amp; Science · ~₹378</h3><p><strong>Permanent admission:</strong> ¥630. <strong>Hours:</strong> 09:00-17:00, last admission 30 minutes before close.</p><p><strong>Best fit:</strong> Saturday 09:10-10:30, replacing most of Ueno Park. It is inside Ueno Park, so it has virtually no extra transport cost.</p><a class="btn" href="https://www.kahaku.go.jp/english/riyou/nyukan-annai/" target="_blank">Official admission</a><a class="btn map" href="https://www.google.com/maps/search/?api=1&query=National+Museum+of+Nature+and+Science+Tokyo" target="_blank">Map</a></div>
<div class="card"><span class="pill paid">ART SWAP · DAY 2</span><h3>Tokyo National Museum · ~₹600</h3><p><strong>Collection exhibition:</strong> ¥1,000. <strong>Hours:</strong> 09:30-17:00, with Friday/Saturday extended hours to 20:00. Last admission 30 minutes before closing.</p><p><strong>Best fit:</strong> Saturday morning in Ueno, replacing Ueno Park. This is the strongest paid choice if Japanese art and history matter more to you than the park walk.</p><a class="btn" href="https://www.tnm.jp/modules/r_free_page/index.php?id=113&amp;lang=en" target="_blank">Official admission</a><a class="btn map" href="https://www.google.com/maps/search/?api=1&query=Tokyo+National+Museum" target="_blank">Map</a></div>
<div class="card"><span class="pill paid">LOW-COST ART · DAY 2</span><h3>National Museum of Western Art · ~₹300</h3><p><strong>Permanent exhibition:</strong> ¥500. <strong>Hours:</strong> 09:30-17:30, extended to 20:00 on Fridays and Saturdays. Last admission 30 minutes before closing.</p><p><strong>Best fit:</strong> Saturday morning in Ueno, replacing part of Ueno Park. Very low entry cost and zero meaningful route detour.</p><a class="btn" href="https://www.gotokyo.org/en/spot/120/index.html" target="_blank">Current details</a><a class="btn map" href="https://www.google.com/maps/search/?api=1&query=National+Museum+of+Western+Art+Tokyo" target="_blank">Map</a></div>
<div class="card"><span class="pill paid">IMMERSIVE ART · DAY 2 ONLY</span><h3>teamLab Borderless · ~₹2,280+</h3><p><strong>Adult:</strong> from ¥3,800 on the current GO TOKYO listing, with dynamic/date-based pricing. <strong>Hours:</strong> generally 09:00-21:00, last entry 20:00.</p><p><strong>Best fit:</strong> Saturday only if you replace Akihabara + Kappabashi. It is in Azabudai Hills and is not a sensible add-on to the existing east-Tokyo route.</p><a class="btn" href="https://www.teamlab.art/e/tokyo/" target="_blank">Official details</a><a class="btn map" href="https://www.google.com/maps/search/?api=1&query=teamLab+Borderless+Tokyo" target="_blank">Map</a></div>
<div class="card"><span class="pill paid">VIEWPOINT ALTERNATIVE · DAY 2</span><h3>SHIBUYA SKY · ~₹1,620–₹2,040</h3><p><strong>Online adult:</strong> ¥2,700 before 15:00 or ¥3,400 from 15:00. <strong>Hours:</strong> 10:00-22:30, last admission 21:20.</p><p><strong>Best fit:</strong> Saturday afternoon/evening only if you replace Akihabara + Kappabashi. Official guidance recommends going around 30 minutes before sunset, but this would duplicate the Skytree viewpoint experience.</p><a class="btn" href="https://www.shibuya-scramble-square.com/sky/ticket/" target="_blank">Official tickets</a><a class="btn map" href="https://www.google.com/maps/search/?api=1&query=SHIBUYA+SKY+Tokyo" target="_blank">Map</a></div>
<div class="card"><span class="pill paid">VIEWPOINT ALTERNATIVE · DAY 2</span><h3>Tokyo Tower · ~₹900</h3><p><strong>Main Deck:</strong> ¥1,500. <strong>Hours:</strong> 09:00-23:00, last admission 22:30.</p><p><strong>Best fit:</strong> Saturday only if you replace Akihabara + Kappabashi. It is farther from your Asakusa/Ueno route and overlaps with Skytree, so I would not add it.</p><a class="btn" href="https://www.gotokyo.org/en/spot/4/index.html" target="_blank">Current details</a><a class="btn map" href="https://www.google.com/maps/search/?api=1&query=Tokyo+Tower" target="_blank">Map</a></div>
</div><div class="note" style="margin-top:16px"><strong>My ranking for this trip:</strong> 1) Skytree, already included. 2) Sumida Aquarium, easiest add-on. 3) Edo-Tokyo Museum, best cheap cultural swap. 4) National Museum of Nature &amp; Science or Tokyo National Museum, best Ueno swaps. 5) teamLab Borderless. 6) SHIBUYA SKY. 7) Tokyo Tower. I would not try to squeeze all of these into 2.5 days.</div></section>'''

html = re.sub(r'<section id="paid">.*?</section>', paid_section, html, count=1, flags=re.S)

path.write_text(html, encoding="utf-8")
print("Enhanced itinerary rows and refreshed paid-attraction options with INR pricing and route fit.")
