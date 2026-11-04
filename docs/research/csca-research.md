# CSCA (China Scholastic Competency Assessment): research report

Research date: 4 Nov 2026. Prepared for the CSCA prep Android app (topics, practice questions, 20 mocks, guidance).

## How the official facts were collected

The official site **www.csca.cn** (it redirects to csca.cn) is a JavaScript single-page app, so ordinary page fetches return only "CSCA". The page text was read straight from the site's public content API, which the site itself calls (`https://csca.cn/sv/open/zyxx/list`, `/sv/open/getConfByCode`, `/sv/open/getGGXX`). Each block has a "last published" timestamp, quoted below as **(csca.cn, published YYYY-MM-DD)**. The blocks are shown on these pages:

- Candidate guidelines (home-based / computer-based / paper tabs): https://csca.cn/about/examnotice
- Registration process (photo, ID, payment): https://csca.cn/about/registprocess
- Test prep (syllabus downloads): https://csca.cn/about/testprep
- Home page session cards: https://csca.cn/home
- News: https://csca.cn/articles/news

The 2025 syllabus PDFs for Maths, Physics and Chemistry were downloaded from csca.cn's test-prep page. The two Professional Chinese syllabi were not in that list; they were read from a university mirror of the official CSC PDFs (Zhejiang Sci-Tech University).

> **Copyright warning for the app.** Every official syllabus PDF carries this notice: "This Syllabus may not be published, commercially used, or disseminated without prior authorization from the China Scholarship Council (CSC)." Do not ship the syllabus text or the PDFs in the app. Write your own topic list that maps to the syllabus.

---

## 0. What "CSCA" means

- In this context **CSCA = China Scholastic Competency Assessment**. The official Chinese name is **来华留学本科入学学业水平测试**, with **水平**, not 能力. That is the `nameZh` string in csca.cn's own code, and university notices use the same wording (e.g. GZUCM notice, 14 Nov 2025: https://studyoverseas.gzucm.edu.cn/__local/2/D7/7A/D6614E437B4CA69B78FC146F107_76A695CB_164BE.pdf). The name 学业**能力**测试 in the brief is a mistranslation. Use 学业水平测试 in the app.
- Other credentials called "CSCA" have nothing to do with this exam. The main one is **ISCEA Certified Supply Chain Analyst (CSCA)**, a supply-chain certification (https://www.credly.com/org/muhakat/badge/iscea-csca-certified-supply-chain-analyst). There is also a "Certified in Strategy and Competitive Analysis" course on Udemy (https://www.udemy.com/course/csca-certified-in-strategy-and-competitive-analysis-2024/). Store SEO should say "China CSCA" or "CSCA China undergraduate test" to avoid confusion.

## 1. Organisers, purpose, who must take it, score use

- **Organiser:** the China Scholarship Council (CSC, 国家留学基金委), with the papers developed jointly with experts from Chinese universities (Shanghai govt FAQ, 18 Dec 2025: https://english.shanghai.gov.cn/en-FAQs-StudyinShanghai/20251218/134bb78943f640519e2185ff83051f5d.html). **Test delivery** is run by **Beijing Liujin Dongfang International Education Technology Co., Ltd.** (东方国际), a wholly owned CSC company commissioned to handle test centres, administration and tech support (csca.cn "About Us", published 2026-10-27). A Shanghai Jiao Tong page says the CSCA Maths requirement is "regulated by China's Ministry of Education" (https://gift.sjtu.edu.cn/en/develop/10185, undated). No direct MOE notice was found; the official site names only CSC.
- **Official contacts:** support@csca.cn (refunds), it_support@csca.cn (test software) (csca.cn). Shanghai govt gives cscasupport@cscdf.org.
- **Purpose:** a standardised test of the language proficiency and academic readiness of international students applying for **bachelor's** programmes in China (Shanghai FAQ; USTB, 1 Nov 2025: https://isc.ustb.edu.cn/bmsq/24c2fa7600ad419cbdceb2bd72b5de89.htm).
- **Eligibility:** non-Chinese citizens only. Holders of Chinese passports or Hong Kong, Macao or Taiwan residence permits cannot register. There is no age limit; under-18s need parental consent (csca.cn FAQ, published 2026-10-13).
- **Who must take it:**
  - From the **2026/2027 academic year**, all international applicants to undergraduate programmes at **Chinese Government Scholarship (CGS) universities** must take the CSCA and submit scores before applying (Shanghai FAQ, Dec 2025; Shanghai guide, 5 Aug 2026: https://english.shanghai.gov.cn/en-Editor'sPick-StudyinShanghai/20260805/abaaa73bb6a743a1a9c73c9a6eae4ead.html).
  - Many universities apply it to **all** their undergraduate applicants, self-funded included. Examples: GZUCM (14 Nov 2025), Beijing Forestry University, BLCU ("All international undergraduate applicants are required to take CSCA from 2026", 12 Dec 2025: https://admission.blcu.edu.cn/en/2025/1212/c1587a3032/page.htm), and NWPU, which rejects applications without scores by the last batch deadline (2027 intake guide: https://studyat.nwpu.edu.cn/info/1089/10371.htm).
  - It applies **only to bachelor's programmes**, not master's, PhD, non-degree or associate programmes (CUCAS, updated 4 Oct 2026: https://www.cucas.cn/csca).
  - **The "2028: mandatory for all" claim is unconfirmed.** Times Higher Education (14 Jan 2026: https://www.timeshighereducation.com/node/740793) reports that it will be phased in until it is mandatory for all international undergraduate applicants by 2028, but names no official source. CUCAS calls this "planned". No CSC or MOE document was found.
- **How scores are used:** the official wording is "an important reference for undergraduate admissions… and **required** for the evaluation of Chinese Government Scholarships" (csca.cn score page, 2026-10-08). Elsewhere csca.cn says scores are "not the sole criterion and do not guarantee admission". Universities set their own cut-offs. Through the official verification system they can check a report and see the candidate's **global percentile ranking** (csca.cn FAQ Q29).

## 2. Subjects, which are compulsory, test language

| Subject | Who takes it | Language |
|---|---|---|
| **Mathematics** | **Compulsory for all programmes**, humanities and English-taught included | Chinese **or** English, chosen per subject |
| **Physics** | Optional. Science, engineering, agriculture and medicine applicants must take **at least one** of Physics or Chemistry | Chinese or English |
| **Chemistry** | As Physics | Chinese or English |
| **Professional Chinese – Humanities (文科中文)** | Chinese-taught humanities/social-science programmes | **Chinese only** |
| **Professional Chinese – STEM (理科中文)** | Chinese-taught STEM programmes | **Chinese only** |

Sources: Shanghai guide (5 Aug 2026); csca.cn FAQ Q8 ("Professional Chinese subjects are offered in Chinese only"; each foundational subject's language can be chosen separately); NWPU.

- **Exemptions:** fully English-taught programmes skip Professional Chinese. Applicants to Chinese Language programmes *may* skip it with a valid **HSK 4** but must still take Maths (Shanghai; BLCU). NWPU reportedly asks for HSK 5 (CUCAS).
- There is no limit on subjects per session (csca.cn FAQ Q7). There is **no Biology or general/comprehensive paper**.
- Universities decide which subjects each programme needs. Examples:
  - NWPU: Business is Maths only; engineering is Maths + Physics; Biotechnology is Maths + Chemistry; Chinese-taught Software Engineering is STEM Chinese + Maths + Physics.
  - BLCU: English-taught programmes are Maths only.
  - USTB: Maths in English for some programmes, in Chinese for others.
  - SUSTech: Maths + Physics in English. Guangxi Medical (MBBS): Maths + Chemistry in English (CUCAS).
  - **App implication:** for a Pakistani or other MBBS/engineering audience, the core is **Maths + Physics + Chemistry in English**. Professional Chinese is a separate audience (Chinese-taught programmes).

## 3. Each paper

All papers are **single-answer multiple choice**, scored **0–100**, taken on a computer with the mouse. You can review and change answers until time runs out, and the paper is auto-submitted at the end; early submission is not allowed (csca.cn exam-day pages, 2026-10-14; syllabi).

| | Maths | Physics | Chemistry | Prof. Chinese (Humanities / STEM) |
|---|---|---|---|---|
| Duration | 60 min | 60 min | 60 min | 90 min |
| Questions | 48 | 48 | 48 | 80 |
| Type | 单项选择题 (single-answer MCQ) | same | same | single-answer MCQ in 6 item types |
| Full marks | 100 | 100 | 100 | 100 |
| Pace | 75 s/question | 75 s/question | 75 s/question | 67.5 s/question |

**Not officially stated anywhere I could find:**
- **Options per question:** no official source gives the number. Third-party mocks use A–D. Treat 4 options as likely but unconfirmed.
- **Negative marking:** none mentioned in any official text. The 100-point scale over 48 items means about 2.08 points per question if items are weighted equally. Whether scores are raw or scaled has not been published. Universities also see a percentile.
- **Calculators: NOT allowed.** The home-test rules list "calculators" as strictly prohibited, along with any device for "calculation, artificial intelligence, or smart assistance". The test-centre rules also ban calculators (csca.cn rules, published 2026-10-14 and 2026-09-16). **No on-screen calculator is mentioned.** Mocks in the app should be calculator-free.
- **Scratch work:** at home, only a small whiteboard or a blank sheet inside a clear sleeve, with an erasable marker. At a centre, the centre provides scratch paper and it must be returned.

**Difficulty:** officially, the target is first-year undergraduate readiness. Third parties describe it as Chinese senior high school (Grade 12) level (Mandarin Zone, Dec 2025: https://www.mandarinzone.com/csca-exam-guide/). Myanmar test-takers reported basic junior and senior high school questions (CUCAS). Commercial CrossLine blogs claim later sessions were harder and more conceptual; that is unverified.

### 3.1 Mathematics syllabus (CSCA Mathematics Examination Syllabus, 2025 edition, official English PDF)

Four modules:
1. **Sets & inequalities:** definition, operations and representation of sets; properties of inequalities and how to solve them (quadratic and rational/fractional inequalities).
2. **Functions:** concept and properties (domain, range, monotonicity, parity/odd–even); basic elementary functions (power, exponential, logarithmic, trigonometric); **sequences** (general term and sums of arithmetic and geometric sequences); **intro to derivatives and calculus** (definition, geometric meaning, simple applications).
3. **Geometry & algebra:** plane analytic geometry (lines, circles, ellipses, hyperbolas, parabolas: equations and properties); vectors (operations) and complex numbers (four arithmetic operations); solid geometry (3-D rectangular coordinates, properties of simple solids).
4. **Probability & statistics:** classical probability; numerical features of data (mean, variance); basic concepts of the normal distribution.

Topics test-takers recalled seeing (CUCAS): arithmetic and geometric sequences, ellipse, slope, eccentricity, special trig values, inverse functions, odd/even functions, standard circle equation. Students also mention trig induction formulas and log properties (CrossLine, unverified).

### 3.2 Physics syllabus (CSCA 物理考试大纲, 2025, Chinese PDF; the English paper presumably follows it)

1. **Mechanics:** kinematics (displacement, velocity, acceleration, uniformly accelerated motion, free fall); Newton's laws and their uses; momentum, impulse and conservation of momentum; work, energy and conservation of mechanical energy; circular motion and universal gravitation; simple harmonic motion and mechanical waves.
2. **Electromagnetism:** electrostatics (Coulomb's law, field strength, potential); DC circuits (Ohm's law, series and parallel); magnetic field (B, Ampère force, Lorentz force); EM induction (Faraday's law, Lenz's law).
3. **Thermal physics:** kinetic molecular theory; ideal gas equation of state; first law of thermodynamics.
4. **Optics:** geometric optics (reflection, refraction); physical optics (interference, diffraction).
5. **Modern physics:** photoelectric effect; atomic structure; basics of nuclear physics.

### 3.3 Chemistry syllabus (CSCA 化学考试大纲, 2025)

1. **Basic concepts & calculations:** classification of matter and changes of state; chemical terms and writing equations; solution concentration and pH; amount-of-substance (mole) calculations; using the ideal gas equation.
2. **Properties & reactions:** common inorganic substances (elements, oxides, acids, bases, salts); basic organic compounds (hydrocarbons and derivatives); identifying redox reactions; ionic reactions and tests for ions.
3. **Theory & laws:** atomic structure and the periodic law; chemical bonds and intermolecular forces; reaction rate and equilibrium; electrolyte solutions.
4. **Lab & applications:** lab safety and apparatus; preparation and testing of common gases; separation and purification; industrial process analysis (e.g. ammonia synthesis).

Recalled topics: molecular formulas, identifying oxides, reaction products (CUCAS).

### 3.4 Professional Chinese (文科中文 / 理科中文 syllabi, 2025, via https://admission.zstu.edu.cn/upfile/csca/)

- 90 min, 100 points, single-answer MCQ in six item types: **识解汉字** (character recognition), **选词填空** (cloze), **辨析词语** (word discrimination), **选词成段** (sentence ordering into a paragraph), **补全语句** (sentence completion), **阅读理解** (reading comprehension).
- **Humanities** passages cover literature, philosophy, law, education, history and art, and more broadly politics, sociology, journalism, foreign languages, music, design, etc. The goal is to follow first-year humanities lectures in Chinese, take notes, and skim and scan specialised texts.
- **STEM** passages cover maths symbols and formulas, physical laws, chemical equations, lab terms, basic calculus, university physics, chemistry and programming terms, describing experiments, reading charts, and reading papers.
- Per-section question counts are **not official**. Mandarin Zone estimates about 10 characters, 15 cloze, 15 word discrimination, 10 paragraph ordering, 10 sentence completion, 20 reading (unverified).

### 3.5 Official sample questions

- csca.cn's test-prep page currently lists **only the syllabus PDFs** (Physics, Chemistry and Maths in Chinese, plus Maths in English; block published 2026-09-13). I found no official sample paper on csca.cn.
- The Shanghai FAQ (Dec 2025) says the site offers "exam outlines, test materials, and simulation tests". CrossLine claims "Official Sample Questions" were released, but its download sits behind a Discord login; unverified. CUCAS also refers to "official sample questions".
- The only official "mock" confirmed is the **Home-based Proctored Mock Test**, a mandatory system rehearsal before the real test.

## 4. Test format, equipment and rules

**Delivery modes** (csca.cn exam-choice block, 2026-10-09):
- **Remote-proctored Home-based Test (RHT):** worldwide, using your own devices, with live remote proctoring.
- **Computer-based test (CBT) at test centres:** csca.cn now says "currently available in **selected cities in mainland China**".
- **Paper-based:** not offered for the 21 Dec 2025 session; reinstatement "will be announced" (csca.cn, 2026-09-17).
- All modes have the same content, duration and scoring.
- **Conflict:** Shanghai govt (Aug 2026), BLCU and USTB say the first overseas centres opened in **Vietnam and Thailand** in Dec 2025. The current csca.cn text lists only mainland China centres. CUCAS says that if a centre exists in your area you cannot choose the home test (unverified).

**Home test requirements** (csca.cn device and environment blocks, 2026-09-16 and 2026-10-13):
- **Primary device:** a **Windows** PC (Win 10/11, or Win 7 SP1+, 64-bit, genuine). **macOS is not supported.**
  - Physical machine only, single monitor, no remote desktop or cloud PC.
  - Virtualisation must be off (Hyper-V, Sandbox, WSL, VBS). Some Surface models have problems.
  - At least 1366×768 resolution, at least 4 GB RAM, at least 2 GB free (not on C:), webcam above the screen (720p minimum, 1080p recommended).
  - No wireless earbuds, no external monitor, no privacy filter. Keep it plugged in.
- **Secondary device:** a phone or tablet running a browser-based "Secondary Camera Portal". It sits on a tripod about **45° behind and to the side**, slightly above shoulder height, showing your upper body, screen and hands. Plugged in, in Do Not Disturb, with "Airplane mode + Wi-Fi" recommended.
- **Network:** at least 20 Mbps symmetric and a sustained 500 KB/s to the test system. Wired is strongly recommended. Have a 4G hotspot as backup. **VPNs and proxies are banned.**
- **Room:** a private, quiet, enclosed, well-lit room with nobody else present. Banned places include cafés, open offices, school computer labs and dorms.
  - Sit in a corner with the desk against two walls, facing the wall.
  - Use a standard desk and chair, not a bed or sofa. No hat or head covering in camera view (religious coverings are allowed in the photo if the face is fully visible).
- **Banned items:** phones, smartwatches, smart glasses, calculators, translators, books, notes, sticky notes, tissues, pens and pencils.
- **Mandatory before test day:** (1) the Equipment & Software Check, and (2) at least one **Proctored Mock Test**. If you skip either and then can't test, there is no refund.
- **Software:** download the latest test client ZIP each session, delete old versions, run it without installing, and read the Handbook and setup video (admission-ticket notes, 2026-11-03).

**Check-in at home** (csca.cn, 2026-10-14):
- Login opens **60 min** before the test; log in **no later than 30 min** before.
- Steps: system check, log in with ticket number and password, face recognition, scan a QR code to link the second camera, show your passport to the proctor, 360° room scan, show a blank whiteboard, accept the rules.
- No entry once the test starts.
- At the end, wipe the whiteboard on camera. Do not delete the client until scores are out.

**Check-in at a test centre:**
- Arrive **40 min** early with your **original passport and a printed admission ticket**.
- Allowed: a black gel pen, and clear water if the centre approves.
- The restroom is escorted. If the system fails, extra time can be given.

**Breaks:** each subject is a separate sitting. In 2026–27, Day 1 has Chinese then Maths with a 1.5 h gap; Day 2 has Physics then Chemistry with a 1.5 h gap. There are no breaks inside a paper; you may not leave your seat at home.

**ID:** **only an original, valid, booklet-type ordinary passport.** It must stay valid from registration until scores are released. No national ID, e-copies or diplomatic passports (csca.cn ID page, 2026-10-10).

**Misconduct:** penalties range from cancelling a subject score up to a 2-year ban, cancelling all scores, notifying universities, a permanent ban, or referral to police.

## 5. Dates, registration, fees, scores

**Past sessions:**
- 12 Oct 2025: a first test for prep-university/CGS students (CUCAS).
- **21 Dec 2025:** first global session. Registration ran 10–28 Nov 2025 (CUCAS). Times were Chinese 13:00, Maths 15:30, Physics 17:30, Chemistry 19:30 Beijing time.
- 25 Jan 2026 and 15 Mar 2026 (CUCAS, Shanghai FAQ Jan 2026). In 2026 the plan was 5 sessions a year (Jan, Mar, Apr, Jun, Dec) on a single day.

**Current official timetable, Nov 2026 – Jun 2027** (csca.cn news "CSCA Test Schedule for November 2026 – June 2027", published 2026-09-24, updated 2026-10-15; home-page cards read 4 Nov 2026). **Each session now spans 2 days**: Day 1 is Professional Chinese + Maths, Day 2 is Physics + Chemistry.

| Session | Day 1 (Beijing time) | Day 2 (Beijing time) | Registration |
|---|---|---|---|
| Nov 2026 | 14 Nov: Chinese 14:00–15:30, Maths 17:00–18:00 | 15 Nov: Physics 14:00–15:00, Chemistry 16:30–17:30 | 15 Oct 15:00 – 21 Oct 23:59 (**closed**; tickets out 4 Nov) |
| Dec 2026 | 19 Dec: 08:00–09:30, 11:00–12:00 | 20 Dec: 08:00–09:00, 10:30–11:30 | not yet open |
| Jan 2027 | 23 Jan: 14:00 / 17:00 | 24 Jan: 14:00 / 16:30 | not yet open |
| Mar 2027 | 13 Mar: 14:00 / 17:00 | 14 Mar: 14:00 / 16:30 | not yet open |
| Apr 2027 | 24 Apr: 14:00 / 17:00 | 25 Apr: 14:00 / 16:30 | not yet open |
| Jun 2027 | 26 Jun: 08:00 / 11:00 | 27 Jun: 08:00 / 10:30 | not yet open |

The Nov 2026 window was only **7 days**. The app should push registration alerts.

**Registration steps** (csca.cn):
1. Create an account at csca.cn with a long-term personal email (one email per candidate).
2. Fill in your details exactly as in your passport.
3. Upload the ID photo: 33×48 mm, JPG 40–200 KB, white background, taken in the last 6 months, no filters or AI edits. It is used for face recognition.
4. Choose the mode, session and subjects (and the language per subject).
5. Pay online. You get a confirmation email.
6. Download the admission ticket when emailed, and print it on A4.

**Fees:** **RMB 450 for one subject, RMB 700 for two or more** (≈ US$64 for one). Sources: Shanghai Aug 2026; NWPU 2027 guide; USTB. The fee is settled in CNY. **Payment:** Visa or Mastercard credit, debit or prepaid cards issued outside mainland China (international payments enabled), WeChat Pay, Alipay (csca.cn payment page, 2026-10-10). Third parties also list UnionPay.

**Changes and refunds** (csca.cn refund policy, 2026-10-13):
- No transfers or changes of subject, date, mode or place.
- You may cancel **before the refund deadline / before the admission ticket is generated**, and get the fee back minus charges. The whole order only; no partial refunds.
- After that, refunds only for force majeure, applying within 7 business days with evidence to support@csca.cn.
- Data corrections are possible only before the ticket is generated.

**Score release:**
- **Official now: within 10 working days** (csca.cn score page changed "7 → 10 working days", 2026-10-08; this applies from the Nov 2026 session).
- Older sources (Shanghai, USTB, BLCU, NWPU) still say 7 days (CBT/home) and 14 days (paper).
- CUCAS says the Dec 2025 results actually came out around 2 Jan 2026.
- Possible statuses: Absent, Invalid, or Pending (review takes 4–6 weeks).

**Validity:** **2 years from the test date** (csca.cn). **Retakes:** unlimited. You can send your best valid score, subject to each university's rules (FAQ Q11).

**Sending scores:** download the e-score report and submit it to universities yourself. There is no separate score-sending order. Universities verify reports online and see your percentile (FAQ Q28–29). All subjects appear on one report (CUCAS).

**Special arrangements:** apply at least 30 business days before the test with medical evidence.

## 6. Reported score requirements

- **CSC sets no national minimum.** Universities set their own (USTB; THE, Jan 2026: "pass thresholds have not been standardised").
- Reported cut-offs, unverified, all from CUCAS (Oct 2026):
  - **Zhengzhou University:** at least 50/100 per subject.
  - **Dalian Jiaotong University:** above 50 per subject *or* top 60% percentile.

  I could not confirm either on the universities' own sites.
- Fuzhou University called 2026 a "transitional year" with scores used for reference only (search snippet of oce.fzu.edu.cn).
- Deadlines tie scores to intakes:
  - SJTU: scores due by **30 June 2026** for Sept 2026 entry.
  - NWPU 2027 batches run 1 Nov 2026 – 20 May 2027, and NWPU suggests sitting in Nov/Dec 2026 or Jan/Mar/Apr 2027.
  - CGS embassy deadlines for 2026 entry were about 8–10 Feb 2026, which made the Dec and Jan sessions the critical ones.

## 7. Pitfalls, tips and prep resources

**Pitfalls** (official unless marked):
- The passport is the only ID, and its details must match exactly. Mistakes can't be fixed after the ticket is generated.
- macOS is not supported, and VPNs are banned.
- Missing the system check or mock test means no refund.
- Logging in later than T-30 min can cost you the test.
- Calculators and paper are banned.
- Choosing the wrong language: take the language your target programme requires.
- Registration windows are short (7 days in Oct 2026). Tickets lock the details.
- CSCA warns that no agent is authorised to register for you.
- Chinese-medium STEM papers are full of technical terms, so students taking Maths or Chemistry in Chinese were surprised (CUCAS/Zhihu anecdote).

**Tips:**
- The Shanghai prep guide (7 Jan 2026: https://english.shanghai.gov.cn/en-FAQs-StudyinShanghai/20260107/32663f024608488391ef105048656e8f.html) recommends a three-phase plan (foundation → intensification → sprint with full mocks), an error log, and timed practice from 3 weeks out with a full mock a week before.
- Mandarin Zone suggests: start 3–6 months ahead; spend no more than 2 min per question; leave about 10 min to check; use a wired connection; install nothing new 2–3 days before.
- Pacing for the app: Maths/Physics/Chemistry is 75 s per question. Chinese is 67.5 s per question.

**Resources mentioned:**
- Official: syllabi on csca.cn; Chinese senior-high textbooks and videos (Shanghai guide).
- Commercial or third-party:
  - CUCAS prep course: https://www.cucas.cn/csca
  - csca.app (1,170+ bilingual maths questions): https://csca.app/en/math/practice
  - cscaprep.academy
  - Gumroad mock volumes (kaiguo0)
  - CrossLine blogs
  - A ResearchGate maths review PDF

  These are competitors for the app.

## 8. Uncertainties and conflicts

| Topic | Conflict |
|---|---|
| Chinese name | Brief: 学业**能力**测试. Official (csca.cn code, university notices): 学业**水平**测试 |
| Who must take it | Official/Shanghai: CGS universities' undergrad applicants from 2026/27. BLCU, GZUCM, NWPU, BJFU: all their undergrad applicants. THE/CUCAS: all international undergrads by **2028** (unsourced/"planned") |
| Score release | csca.cn now: **10 working days** (from Nov 2026). Shanghai/USTB/BLCU/NWPU: 7 days (CBT/home), 14 days (paper). BLCU also says "two weeks". CUCAS: paper 10 days |
| Session months | 2026 plan: Jan, Mar, Apr, Jun, Dec, single day. 2026–27 timetable: Nov, Dec, Jan, Mar, Apr, Jun, 2-day sessions. BLCU and Mandarin Zone mention "May" (outdated or wrong) |
| Session times | Dec 2025 used 13:00 / 15:30 / 17:30 / 19:30 on one day. From Nov 2026 it is 08:00 or 14:00 starts over two days |
| Test centres | Shanghai, BLCU, USTB: Vietnam and Thailand from Dec 2025. csca.cn (Oct 2026): "selected cities in mainland China" only |
| Paper-based | Listed by the Shanghai and university pages. csca.cn: not offered since Dec 2025, pending notice |
| ID | Old university pages say "valid identification". csca.cn: **passport only** |
| Options/question, negative marking, raw vs scaled scoring, Chinese section counts | Not officially published |
| Official sample papers | Shanghai and CrossLine/CUCAS say they exist. Not found on csca.cn's test-prep page (syllabi only) |
| Fee | 450/700 RMB is consistent across sources from 2025 to 2027, but the live fee shows only at checkout ("subject to change") |
| Under-age consent | csca.cn: under 18 needs a parent. CUCAS: under 14 |
