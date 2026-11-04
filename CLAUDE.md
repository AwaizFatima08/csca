# Prep Simulator for CSCA (HomiLabs) — project notes

Flutter Android app for international students preparing for the CSCA (China Scholastic Competency Assessment,
来华留学本科入学学业水平测试), the undergraduate admission test for Chinese universities: 20 full-length mocks each for
Mathematics, Physics and Chemistry, study notes and practice for every topic, and a guide (registration, test day,
tips, formula sheets). No login, offline. Package `csca_prep`, app id `com.homilabs.csca_prep` (locked after the first
Play upload). Launcher name "CSCA Prep". Built on the NLE/NTS engine plus the GRE app's lessons.

## Locations
- Code: `/mnt/storage/projects/csca` · GitHub `AwaizFatima08/csca` (PUBLIC repo: no secrets)
- Local backup: `/mnt/storage/project_backups/csca_backup` · Google Drive: https://drive.google.com/drive/folders/1fdWpK1grbU1DZ325AME-SdBaMphdiR9C
- Backups: `bash scripts/backup.sh` (all three layers)
- Site: https://csca.homilabs.org (Hostinger `public_html/csca`, an SSH git checkout of the `deploy` branch), source in `website/`, `bash scripts/publish-site.sh`

## Exam format (csca.cn, checked 4 Nov 2026; details in docs/research/csca-research.md)
Maths, Physics, Chemistry: 48 single-answer MCQs, 60 min, 0-100, no calculator, English or Chinese. Professional
Chinese (80 q / 90 min, Chinese only) is covered by the guide only (Homi, 4 Nov 2026). CSC publishes no topic weights,
option count, negative marking or scaling: our weights are in `tool/make_blueprint.py`, mocks use 4 options, and the
app's score is percent correct, shown as "estimated" with a 50/100 reference line (no national pass mark).

## Content
- `content/bank/<subject>/<topic>.jsonl` (format in `docs/content-schema.md`, quality bar `docs/writer-brief.md`),
  notes in `content/lessons/<subject>/<topic>.json` (`docs/lesson-format.md`), guide source `content/guide_src.py`
  (run it to rebuild `content/guide.json`; dated facts live there: sessions, fees, rules).
- `python3 tool/validate.py`, `python3 tool/build_content.py` (fixed seeds: papers stay stable), `tool/blind.py`
  (independent answer check). `flutter test test/content` checks the built papers.
- Every item is original HomiLabs work. Never copy CSCA/CSC material, the official syllabus text (copyrighted), gaokao
  papers or prep sites. Items for a human look: `docs/review-flags.md`.
- Re-check `content/guide_src.py` facts (sessions, fees, score release) before each release.

## Ads
Ids in `config/admob.json`. Banner on Home tabs only; interstitial when leaving results or a practice set, 5 minutes
apart. Never on mock, review or practice question screens. Debug builds use Google test units;
`bash scripts/check-release-ad-ids.sh` before a release build.

## Gate before commit
```
dart format --set-exit-if-changed lib test
flutter analyze
flutter test
```
Heavy jobs follow `~/.claude/heavy-jobs.md`: use `jobq`, then `./gradlew --stop`.
