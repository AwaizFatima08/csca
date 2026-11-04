# Release and hosting kit: Prep Simulator for CSCA

## Build
- Package `com.homilabs.csca_prep` (locked after the first Play upload). Version 1.0.0 (versionCode 1).
- Build: `jobq run --name csca-release-aab -- flutter build appbundle --release`, then `./gradlew --stop` in `android/`.
- Before every release: `bash scripts/check-release-ad-ids.sh`, `python3 tool/validate.py`, `flutter test`, and re-check the dated facts in `content/guide_src.py` against csca.cn.
- Signing: upload key created 4 Nov 2026: `.secrets/csca-upload.keystore` (alias `csca-upload`, RSA 2048, valid 10,000 days), passwords in `.secrets/csca-upload-keystore-credentials.txt`, read by `android/key.properties`. Certificate SHA-256 `7F:00:42:4A:D5:19:1C:8E:1B:81:5A:9D:EF:0D:07:95:50:5C:EF:31:A1:85:A2:5A:86:E4:50:FC:6E:33:AA:7B`. `.secrets/` goes to the local and Drive backups, never GitHub. Losing it means asking Play support for an upload-key reset.
- Release 1.0.0+1 built 4 Nov 2026: `releases/1.0.0+1/csca-prep-1.0.0+1.aab` (upload this to Play) and `.apk` (sideload test). Mock flow, results, review and ads smoke-tested on the emulator (debug build); Practice, notes and Guide covered by widget tests.

## Website: https://csca.homilabs.org
- Hostinger: subdomain `csca.homilabs.org` (folder `public_html/csca`, created 4 Nov 2026). The folder is a git checkout of this repo's `deploy` branch (cloned over SSH, as for gre/nts; hPanel's one Git slot for homilabs.org belongs to the games site).
- Change `website/`, commit, then `bash scripts/publish-site.sh` (pushes `deploy`, then pulls it on the server over SSH). Flush the CDN cache in hPanel if pages look stale.
- Pages: landing, `/privacy.html`, `/terms.html`, `/app-ads.txt`.
- After Play launch: replace "Coming soon on Google Play" with the Play link, and add the app to homilabs.org.

## AdMob (account homilabs.smc@gmail.com)
- Created 4 Nov 2026: app "Prep Simulator for CSCA", App ID `ca-app-pub-2087846699268567~6011252769`; units banner `csca_home_banner` and interstitial `csca_results_interstitial` (ids in `config/admob.json`). Debug builds use Google test units.
- "Limited ad serving" until the Play listing is live. After it is live: AdMob → Apps → this app → Add store (com.homilabs.csca_prep). `app-ads.txt` is already in `website/`.
- Privacy & messaging: European regulations messages are per app, not account-wide. "Prep Simulator for CSCA consent" (this app only, privacy URL https://csca.homilabs.org/privacy.html, "Do not consent" on for all countries) published 4 Nov 2026 for the app's Google UMP request.

## Play Console
| Item | Value |
|---|---|
| App icon 512×512 | `store-assets/icon-512.png` |
| Feature graphic | `store-assets/feature-graphic.png` |
| Privacy policy URL | https://csca.homilabs.org/privacy.html |
| Website | https://csca.homilabs.org |
| Contact email | homilabs.smc@gmail.com |
| Ads | Yes (AdMob banner on home tabs; one interstitial after results or practice) |
| App access | All functionality available without login |
| Data safety | Collected and shared: Device or other IDs (advertising ID) and app activity via the ads SDK, purpose Advertising, shared with Google AdMob; encrypted in transit. Attempts stay on the device |
| Content rating | Reference/educational; No to violence, sexuality, language, drugs, gambling, purchases, user interaction |
| Target audience | 16+ (applicants are typically 17-20; choose 16-17 and 18+) |
| Category | Education |

**App name** (23 characters): `Prep Simulator for CSCA`

**Short description** (80 max): `China CSCA mocks for Maths, Physics, Chemistry. 60 tests, every answer explained`

**Full description**:
```
Applying to a bachelor's programme in China or for the Chinese Government Scholarship? Prepare for the CSCA (China Scholastic Competency Assessment) the way it feels on the day.

60 FULL-LENGTH MOCK TESTS
• 20 mocks each for Mathematics, Physics and Chemistry.
• 48 single-answer questions in 60 minutes per paper, spread across the whole syllabus.
• No calculator needed, just like the real test: clean numbers you work by hand.
• Countdown timer, flags and a question map.
• An estimated score out of 100, your weakest topics, and a worked solution for every question.

EVERY TOPIC COVERED
• Study notes for 33 topics with worked examples, traps and shortcuts.
• Maths: sets and inequalities, functions, exponents and logarithms, trigonometry, sequences, derivatives, lines, circles and conics, vectors and complex numbers, solid geometry, probability and statistics.
• Physics: kinematics, Newton's laws, momentum, energy, circular motion and gravitation, waves, electrostatics, circuits, magnetism, induction, thermal physics, optics, modern physics.
• Chemistry: chemical language, the mole, inorganic and organic chemistry, redox, ionic reactions, atomic structure and the periodic table, bonding, rates and equilibrium, acids and bases, lab and industrial chemistry.
• Practice questions with instant answers. They never appear in the mocks.

GUIDANCE, TIPS AND TRICKS
• Which subjects you need, test language, fees, registration step by step and the 2026-27 sessions.
• Home-based test setup, test-day check-in and rules, scores, validity and retakes.
• A 12-week study plan, MCQ strategy without a calculator, time management, mental maths and formula sheets.

PRIVATE AND OFFLINE
• No account. Everything works offline and your scores stay on your phone.
• Free, with light ads, never during a mock or a practice question.

Prep Simulator for CSCA is independent practice material by HomiLabs. It is not affiliated with, endorsed by or connected to the China Scholarship Council (CSC), csca.cn or any university. All questions are original practice material, not real or recalled papers, and scores are practice estimates. Always check csca.cn for official dates, fees and rules.
```

## Before production (open items)
- Homi reviews the guide (dated facts), a sample of questions per subject and `docs/review-flags.md`.
- Trademark: "CSCA" is used descriptively, with the not-affiliated notice in the About screen, listing and website.
- Phone screenshots (2-8) for the listing.
