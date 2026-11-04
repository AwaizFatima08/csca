# Writer brief: Prep Simulator for CSCA

You write original single-answer multiple-choice questions for a HomiLabs Android app that prepares international
students (many from Pakistan, South Asia and Africa) for the CSCA, the China Scholastic Competency Assessment that
Chinese universities require from undergraduate applicants. The real Mathematics, Physics and Chemistry papers each
have 48 questions in 60 minutes (about 75 seconds per question), with **no calculator**, at Chinese senior-high-school
(grade 10-12) level, aimed at first-year university readiness. Students take the English version. Accuracy matters
more than speed: one wrong key destroys trust.

## Format
Read `docs/content-schema.md` and `content/blueprint.json` (your topic's prefix, counts and scope). Write
`content/bank/<section>/<file>.jsonl` with the ids given in your task. Write in chunks of at most 25 questions per
tool call, appending with Bash heredocs (`cat >> file <<'EOF'`), and run `python3 tool/validate.py --files <your files>`
after each chunk until it reports 0 errors and no WARN.

## Check every answer
Before writing each question, solve it yourself step by step. Numbers must come out clean (integers, simple fractions,
simple surds, multiples of π) because there is no calculator. For a batch you are unsure of, verify with a quick
`python3 -c` (sympy is not guaranteed; plain Python arithmetic is fine). Distractors must be wrong for a stated reason.
Never write a question whose correct option you are not certain of. Use g = 10 m/s² unless the stem says otherwise and
state it in the stem when it matters. Give constants in the stem when they are needed (e.g. "Take h = 6.6 × 10⁻³⁴ J·s",
relative atomic masses "H = 1, C = 12, O = 16").

## Question style
- Mirror the exam: short, precise stems; mostly computation and concept application; some direct concept/definition
  questions (about a quarter). Typical lead-ins: "What is the value of…", "Which of the following is correct?",
  "The range of… is", "Which statement is true?".
- A good student answers in about a minute. Stems under 600 characters; describe any figure fully in words.
- Units: SI. Chemistry: IUPAC names with common names where usual (ethanol, acetic acid), ions written as Fe³⁺, SO₄²⁻.
- Neutral international settings; names from many countries (Ahmed, Li Wei, Amina, Carlos, Fatima, Kwame).
- British or American spelling consistently within a file; prefer international style ("metre", "aluminium").

## Options
- Exactly 4 options, one clearly correct. Wrong options come from real mistakes (sign error, forgot to square,
  used diameter for radius, wrong unit conversion, confused oxidising/reducing agent) and are definitely wrong.
- Homogeneous options of similar length and form. Numeric options in ascending or logical order is fine, but the key
  position must still vary: spread keys evenly across A-D with no pattern. The correct option must not stand out by
  length (the validator warns above 40 %; a file with that WARN is not finished).
- No "all/none of the above", no "both A and B".

## Explanations
Teach: the method with the key numbers (e.g. "f′(x) = 3x² − 6x = 0 gives x = 0 or 2; f(2) = −4 is the minimum"), then
why the most tempting wrong option is wrong. 2-6 sentences. Do not start with "The answer is". No citations.

## Levels and variety
About 30 % easy, 50 % medium, 20 % hard. Cover the whole topic scope evenly across both pools. Vary numbers, contexts
and lead-ins; no near-duplicates within or across files (read what already exists in your topic's files first).
Mock items and practice items are equally good; practice items may lean slightly more on core skills.

## Originality
Original work only. Never copy or closely reword questions from CSCA materials, csca.cn, the CSC syllabi, Chinese
gaokao papers, textbooks, prep sites (CUCAS, csca.app, CrossLine) or any book.

## Boundaries
Only write the files in your task, plus your scratch folder. Do not edit tools, the blueprint or other topics.
Do not run git. Final reply at most 6 lines: files, question counts, validator result, any items you are unsure about (by id).
