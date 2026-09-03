# Japan Trip HTML Build Specification

## 1. Objective

Build a mobile-first, visually polished, operational trip guide for Tokyo for 11-13 September 2026. The page must work well on a phone during the trip and should minimize the need to search for information manually.

The traveler is staying at Section L Residence Asakusa East and traveling with one male colleague, sharing the room. Arrival is at Narita Airport Terminal 2 and departure is from Narita Airport Terminal 2 to San Francisco.

## 2. Confirmed flight details

- 10 Sep 2026: Hyderabad (HYD) → Bengaluru (BLR), JL9619 / operated by IndiGo, depart 21:25, arrive 22:45.
- 11 Sep 2026: Bengaluru (BLR) → Tokyo Narita (NRT), JL754, depart 02:20, arrive 14:35, Terminal 2.
- 13 Sep 2026: Tokyo Narita (NRT) → San Francisco (SFO), JL58, depart 18:15, Terminal 2.
- Booking reference in the supplied itinerary: FD9L9L.

Use the uploaded itinerary as the source of truth for flight times. Never invent or silently change flight numbers or times.

## 3. Hotel

Section L Residence Asakusa East
4 Chome-13-6 Higashikomagata, Sumida City, Tokyo 130-0005

Known access points:
- Honjo-azumabashi Station, Exit A2: about 5 minutes on foot.
- Asakusa Station: about 15 minutes on foot.
- Tokyo Skytree: about 7-8 minutes on foot.
- Tokyo Solamachi: about 6 minutes on foot.
- Senso-ji: about 18 minutes on foot.
- Check-in: 15:00.
- Check-out: 11:00.

## 4. Core sightseeing priorities

The itinerary should prioritize:
1. Senso-ji and Kaminarimon
2. Sumida River / Azumabashi
3. Ueno Park
4. Ameyoko
5. Akihabara
6. Kappabashi Kitchen Town
7. Tokyo Skytree

The route should favor walking when the walk is reasonable and use short rail trips when they save significant time or energy.

## 5. Food requirements

Every meal mentioned in the itinerary should have at least one practical food option.

At least one lunch must be Indian and close to the sightseeing route. The selected option is Chennai Spice near Ueno/Inaricho on Day 2.

Preferred additional food options:
- Day 1 dinner: Gonpachi Asakusa Azumabashi or Asakusa Udon.
- Day 2 lunch: Chennai Spice.
- Day 2 dinner: Tokyo Solamachi restaurant area.
- Day 3 breakfast: Asakusa Udon.

For restaurants, show approximate price per person in INR and JPY when reliable. Always warn that menus/hours can change.

## 6. Day-by-day operational itinerary

### Day 1, Friday 11 Sep

14:35 land at Narita T2.
15:45-16:05 move to Keisei/Narita Sky Access station.
~16:05 target a Keisei Access Express / through-service train toward the Toei Asakusa Line and Honjo-azumabashi.
~17:05 reach Honjo-azumabashi and use Exit A2.
~17:15 check into hotel and reset.
18:10 walk to Sumida River / Azumabashi.
18:40 walk to Kaminarimon.
19:00 Senso-ji grounds and Nakamise. Do not rely on entering the main hall after 17:00.
20:00 dinner near Azumabashi/Asakusa.
21:00 return to hotel.

### Day 2, Saturday 12 Sep

07:15 leave hotel.
07:45-08:45 Senso-ji main hall and grounds.
08:45 walk to Asakusa Metro station.
09:00 Ginza Line Asakusa G19 → Ueno G16, direction Shibuya. About 5 minutes, IC fare around ¥178.
09:10-10:45 Ueno Park.
10:45-12:10 Ameyoko.
12:10-13:05 Chennai Spice Indian lunch.
13:05-13:25 walk to Inaricho Station.
13:25-15:15 Ginza Line toward Shibuya, Inaricho G17 → Suehirocho G14, then explore Akihabara.
15:15-15:35 use Ginza Line back toward Asakusa, Suehirocho G14 → Tawaramachi G18.
15:35-17:00 Kappabashi Kitchen Town.
17:00-17:35 return toward hotel/Asakusa.
17:35-20:15 Tokyo Skytree. Aim to arrive before sunset and stay into the night.
20:15-21:15 dinner at Tokyo Solamachi.
21:15 return to hotel.

### Day 3, Sunday 13 Sep

07:15 short final Asakusa/Sumida walk.
08:00-09:00 breakfast at Asakusa Udon.
09:00-10:30 pack and prepare.
11:00 checkout.
11:10-11:25 walk to Honjo-azumabashi A2.
11:30-ish take a Narita-bound Asakusa Line / Keisei through-service train.
Target Narita T2 arrival around 13:00-14:30. Keep a large airport buffer.
18:15 JL58 departs NRT T2 for SFO.

## 7. Train instructions

Do not hard-code a single train as if it is guaranteed. Give the user:
- line name
- station code where useful
- direction
- platform/track only when confirmed by a current official source
- approximate ride time
- fare
- first-choice route
- fallback route
- official timetable link
- Google Maps live route link

For every route, explicitly state what to do if the train is missed. Example: "Take the next train in the same direction. The linked timetable updates with the current service."

### Key rail routes

Narita T2 → Honjo-azumabashi:
- Keisei Access Express / through service to Toei Asakusa Line.
- No limited express supplement for Access Express.
- Hotel says the airport journey to Honjo-azumabashi is about 1 hour.
- Keisei reference fares from Narita T2-3: ¥1,290 to Asakusa and ¥1,170 to Oshiage. Exact Honjo-azumabashi fare should be read from the IC gate/fare table rather than guessed.

Asakusa G19 → Ueno G16:
- Tokyo Metro Ginza Line.
- Direction Shibuya.
- 3 stops, about 5 minutes.
- IC ¥178, ticket ¥180.

Inaricho G17 → Suehirocho G14:
- Tokyo Metro Ginza Line.
- Direction Shibuya.
- Get off at Suehirocho for Akihabara.

Suehirocho G14 → Tawaramachi G18:
- Tokyo Metro Ginza Line.
- Direction Asakusa.
- Get off at Tawaramachi for Kappabashi.

Honjo-azumabashi → Narita T2:
- Use the official Toei Asakusa Line weekend timetable and choose a service showing Narita Airport / 成田空港 where possible.
- Prefer through service over unnecessary transfers.
- If the first train is missed, take the next suitable Narita-bound service.

## 8. Attraction timing optimization

Senso-ji:
- Use early morning on Day 2 for the main hall and quieter photography.
- Use Day 1 evening for illuminated exterior and atmosphere.
- Official main hall opening in September is 06:00-17:00.

Ueno Park:
- Morning before midday.

Ameyoko:
- Late morning after Ueno Park.

Akihabara:
- Early-to-mid afternoon. Allow around 1.5-2 hours.

Kappabashi:
- Daytime only. Do not put it late in the evening because individual stores can close around 17:00-18:00.

Tokyo Skytree:
- Arrive before sunset and remain into the night. This gives daylight, twilight and city-night views in one admission.
- Verify the date-specific opening hours and ticket inventory immediately before the trip.

Narita departure:
- The international flight is at 18:15.
- Do not add a distant sightseeing activity after hotel checkout unless it has a very strong time buffer.
- Target airport arrival around 13:00-14:30.

## 9. Maps

Every major transfer must have a direct Google Maps URL using the directions API format where possible.

Examples:
- Hotel → Senso-ji
- Hotel → Skytree
- Asakusa → Ueno
- Ameyoko → Chennai Spice
- Inaricho → Suehirocho
- Suehirocho → Tawaramachi
- Tawaramachi → Kappabashi
- Honjo-azumabashi → Narita T2

Google Maps links should be live navigation links rather than screenshots. If a static map image is used, clearly label it as a reference rather than live navigation.

## 10. Images

The HTML should include a 5-6 image carousel at the top covering the major places. Images should be medium-size and optimized for mobile.

Preferred subjects:
- Senso-ji / Kaminarimon
- Akihabara
- Kappabashi
- Ueno Park
- Sumida River / Azumabashi
- Tokyo Skytree

Use legally appropriate image sources. Prefer official tourism sites, Wikimedia Commons, Unsplash, Pexels or properly attributed public sources. Do not imply that a random web image is a Google image.

## 11. UX requirements

The page must:
- be mobile-first
- load quickly
- use large tap targets
- have a sticky navigation bar
- have a top summary table
- show a visual carousel
- have day-by-day hour-by-hour timelines
- show train routes and fallback rules
- show costs in JPY and INR where available
- have one-tap Google Maps buttons
- have official attraction/ticket links
- have restaurant options with maps
- have a packing/travel checklist
- have a "what to do if you miss the train" rule
- have a "verify on the day" warning for changing schedules
- avoid requiring a build step or framework if possible

## 12. Cost optimization

Optimize for value rather than luxury:
- walk between nearby hotel/Asakusa/Skytree places
- use Tokyo Metro for short cross-town trips
- use IC card rather than buying paper tickets when practical
- avoid taxis unless needed for a safety/time reason
- avoid paid attractions except Tokyo Skytree unless the user explicitly wants them
- buy Skytree tickets online if a meaningful price/availability advantage exists
- choose restaurants in the ¥1,000-¥2,000 range for most meals, with one optional higher-cost dinner

## 13. Currency

Show JPY first and INR second. For example: ¥1,000 ≈ ₹600 when using the planning rate. For live trip-day conversions, use a current FX source rather than relying on the planning rate.

## 14. Reliability rules

The AI building or maintaining this page must not fabricate:
- train departure times
- platform numbers
- restaurant opening hours
- ticket prices
- attraction hours
- Google Maps screenshots

If an exact value is not available, label it as approximate and provide the official source for verification.

## 15. Recommended page structure

1. Hero / trip title
2. Quick summary cards
3. Places summary table
4. 5-6 image carousel
5. Day 1 detailed timeline
6. Day 2 detailed timeline
7. Day 3 detailed timeline
8. Train playbook
9. Food guide
10. One-tap Google Maps
11. Ticket/official links
12. Travel checklist
13. Important warnings and backup rules
14. Sources

## 16. Final quality checklist

Before publishing:
- Verify all flight details against the supplied itinerary.
- Verify hotel address and check-in/out.
- Verify Senso-ji hours.
- Verify Tokyo Skytree date-specific hours.
- Verify weekend Asakusa Line timetable.
- Verify restaurant hours on the morning of the visit.
- Verify all Google Maps links open correctly.
- Check the page on a phone-sized viewport.
- Check that every button is easy to tap.
- Check that no route requires an unrealistic transfer.
- Ensure Day 3 has a large airport buffer.
- Make sure the HTML remains useful offline for information that does not require live data, while clearly marking links that need internet.

## 17. Useful source links

- Section L hotel: https://section-l.co/hello-asakusa-east/
- Senso-ji: https://www.senso-ji.jp/
- Tokyo Metro: https://www.tokyometro.jp/lang_en/
- Toei airport access: https://www.kotsu.metro.tokyo.jp/eng/guides/airportaccess/
- Keisei Access Express fares: https://www.keisei.co.jp/keisei/tetudou/skyliner/us/traffic/express_fares.php
- Tokyo Skytree: https://www.tokyo-skytree.jp/
- Tokyo Skytree tickets: https://www.tokyo-skytree.jp/en/ticket/
- GO TOKYO Kappabashi: https://www.gotokyo.org/en/spot/59/index.html

The current repository page is intentionally self-contained HTML with no framework dependency. If the page is later expanded, keep the same information architecture and preserve all operational links.
