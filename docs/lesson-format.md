# Study notes and guide articles

## Study notes: `content/lessons/<section>/<topic>.json` (one per blueprint topic, opened from the topic screen)
```json
{"section":"math","topic":"functions","title":"Functions, exponents and logarithms","minutes":12,"lines":["..."]}
```
## Guide: `content/guide.json`
```json
{"articles":[{"id":"about","group":"Start here","title":"What is the CSCA?","lines":["..."]}]}
```
Groups in order: "Start here", "Registration and test day", "Tips and tricks", plus one group per subject for formula sheets.

## Line syntax (notes and guide)
| Line starts with | Shows as |
|---|---|
| `## ` | heading |
| `- ` | bullet |
| `> ` | example box (worked example); consecutive `> ` lines form one box |
| `! ` | tip box (a shortcut, a trick or a trap to avoid) |
| anything else | paragraph |
Plain Unicode maths (x², √, π, ≤), no LaTeX, no Markdown tables, no bold/italic markers.

A topic's notes teach every subtopic in its blueprint scope: the key facts and formulas, a worked example per
subtopic (no calculator, like the exam), the traps the CSCA sets, and quick no-calculator tricks. 900-1800 words.
Never copy or reword the official CSC syllabus text (it is copyrighted); write the topic list in your own words.
