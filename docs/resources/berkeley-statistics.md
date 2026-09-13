---
title: Berkeley statistics
---

# UC Berkeley statistics courses

Course sites and their GitHub repositories. Collected 2026-09-13 by the `collect-materials` skill;
the harvesting recipe is in that skill's `references/berkeley.md`.

> **Provenance.** These are *located*, not judged. Every entry is `unvetted`: nothing here has been
> read, and a list is not a verdict. The useful work this page does today is saying which courses
> have public material and which do not.

> **Licence is per offering, and it is not where you would look for it.** Berkeley makes no
> institution-wide grant, so it varies course by course and *year by year* — the same course can be
> CC BY in one semester and unlicensed the next.
>
> The declaration is usually a **`license.qmd` page inside the repo**, not a `LICENSE` file. GitHub
> cannot classify it, reports the repo as `NOASSERTION`, and an agent reading the API's licence
> field concludes "no licence" for material that is in fact CC BY 4.0. Verified 2026-09-13 by
> reading every cloned repo: **11 offerings are CC BY 4.0**, one is CC BY-NC 4.0, one CC0, one
> BSD-3-Clause, and the rest genuinely carry nothing.
>
> The opposite trap also holds: every `berkeley-stat<num>.github.io` repo reports `MIT`, which is
> the licence of the *Jekyll theme* — its copyright line names the template's author, not Berkeley.
> Both traps are recorded so nobody trusts either field twice.

## What is actually in the repositories

All 30 content repositories were cloned and inspected on 2026-09-13. **A public repo is not the
same as public material**, and the split is sharp:

| | Repos | What is in them |
| --- | --- | --- |
| **Real material** | 153 (all 5 offerings), 243 (all 12), 158 Spring 2026, 156 Fall 2024, 230A Spring 2025 | 30–90 PDFs each, notebooks, labs, problem sets. Stat 243 Fall 2019 alone has 42 PDFs |
| **Scaffolding only** | 201A, 201B, 205A, 206A, 206B Spring 2025, 158 Spring 2025, 230A Spring 2026 | a Quarto site and nothing else: `index`, `syllabus`, `schedule`, `staff`, `license`, a stylesheet and a logo. **No notes, no problem sets** |
| **Thin** | 150, 205B, 206B Spring 2026 | ~28 files, one notebook. A shell with a little in it |

**The theory courses' repos are the empty ones.** Probability and statistical theory — 201, 205,
206 — put their material on bCourses and publish only a syllabus. The applied and computational
courses — 153, 243, 158, 210A — put everything in the open.

**But an empty repo does not mean an unavailable course**, and this is the correction that matters:
Berkeley has a second, older publishing system that the `stat<num>` sites do not index at all.
Instructor pages under `stat.berkeley.edu/~<user>/` carry complete notes and problem sets for
exactly the courses whose repos are scaffolds:

| Course | Repo | What the instructor page has |
| --- | --- | --- |
| 205A / 205B | scaffold | Sinho Chewi's **full scribe notes for both halves**, plus a Brownian motion book and the Diaconis–Freedman paper — `~aldous/` |
| 201A | scaffold | Guntuboyina's **complete lecture notes**, Fall 2019 and Fall 2022 — `~aditya/resources/` |
| 210B | scaffold | Guntuboyina's **complete Spring 2018 notes** — same page |
| 150 | bCourses | Benson Au's **five offerings of problem sets, with LaTeX source** — `~bensonau/` |

So the value of this page is not the four applied courses. It is that **every course in it now has
material except 206 and the Public Health cross-listings.**

There is an irony worth naming, because it will mislead anyone scanning licences: **the CC BY
licence sits mostly on the empty repositories.** Stat 201A is CC BY 4.0 and contains nothing;
Stat 243's content-rich legacy years are unlicensed. A permissive licence on a scaffold grants
nothing worth having.

## How to read these entries

| | Means |
| --- | --- |
| `local` | cloned into `sources/<org>/<term>/`, and it contains actual material |
| `fetchable` | the repo is public, but holds only site scaffolding — clone it and you get a syllabus |
| `unreadable` | the material is behind **bCourses**, Berkeley's Canvas. Not reachable, and no mirror exists |

## Probability and stochastic processes

### berkeley-stat150 — Stat 150, *Stochastic Processes* { #berkeley-stat150 }

**Kind:** course · **Access:** local · `sources/berkeley-stat150/` — 222 files from 7 offerings
**Licence:** unresolved — instructor pages carry no statement; the Spring 2026 repo none
**Status:** unvetted · **Adapted:** none
<https://stat150.berkeley.edu/> · <https://github.com/berkeley-stat150/spring-2026>

*(unvetted)* Vadim Gorin, Spring 2026. Random walks, discrete-time Markov chains, Poisson
processes, then continuous-time chains, queueing, point processes, branching, renewal, stationary
and Gaussian processes. The page names the instructor and the syllabus; the material itself is on
bCourses. Directly on the route in [path.md](../path.md) — nodes 4 and 5 — which makes the
inaccessibility worth a login rather than a shrug.

### berkeley-stat205a — Stat C205A, *Probability Theory* { #berkeley-stat205a }

**Kind:** course · **Access:** local · `sources/berkeley-stat205a/aldous-legacy/` — Chewi's full scribe notes
**Licence:** **CC BY 4.0** on the (empty) course repo; the Aldous page carries no statement
**Status:** unvetted · **Adapted:** none
<https://stat205a.berkeley.edu/> · also listed as Math C218A

*(unvetted)* Measure-theoretic probability, the first half of a year course, for students whose
research will involve rigorous proofs in probability. Durrett is the usual text. The **legacy pages
under `~aldous/205A` carry lecture notes and scribe notes** that the current site does not, and are
the better starting point: <https://www.stat.berkeley.edu/~aldous/205A>.

### berkeley-stat205b — Stat C205B, *Probability Theory* { #berkeley-stat205b }

**Kind:** course · **Access:** local · `sources/berkeley-stat205b/aldous-legacy/` — 13 files incl. a Brownian motion book
**Licence:** unresolved — no statement on either the repo or the Aldous page
**Status:** unvetted · **Adapted:** none
<https://stat205b.berkeley.edu/> · also listed as Math C218B

*(unvetted)* Second half of the C205 sequence — martingales, Brownian motion, weak convergence.
Aldous's 205B page carries per-lecture PDFs including a measure-theory recap:
<https://www.stat.berkeley.edu/~aldous/205B>. Relevant to [path node 3](../path.md#3-martingale).

### berkeley-stat206a — Stat C206A, *Advanced Topics in Probability* { #berkeley-stat206a }

**Kind:** course · **Access:** fetchable — **scaffolding only**, no material in the repo
**Licence:** **CC BY 4.0** — on a repo containing only a syllabus
**Status:** unvetted · **Adapted:** none
<https://stat206a.berkeley.edu/> · also listed as Math C223A

*(unvetted)* Topics course; content varies by offering, so the year matters more than the number.

### berkeley-stat206b — Stat C206B, *Advanced Topics in Probability* { #berkeley-stat206b }

**Kind:** course · **Access:** fetchable — thin; Spring 2025 is scaffolding only
**Licence:** unresolved — no declaration in either offering
**Status:** unvetted · **Adapted:** none
<https://stat206b.berkeley.edu/> · also listed as Math C223B

*(unvetted)* Two offerings held, Spring 2025 and Spring 2026. Topics course, as C206A.

## Statistical theory

### berkeley-stat201a — Stat 201A, *Introduction to Probability at an Advanced Level* { #berkeley-stat201a }

**Kind:** course · **Access:** local · `sources/berkeley-guntuboyina-notes/` — full lecture notes, 2019 and 2022
**Licence:** **CC BY 4.0** on the (empty) course repo; Guntuboyina's notes carry no statement
**Status:** unvetted · **Adapted:** none
<https://stat201a.berkeley.edu/>

*(unvetted)* **This is the live replacement for Stat 200A.** The 200A–B sequence was revamped into
201A–B in 2012–13 and, per the department's
[notice](https://statistics.berkeley.edu/courses/notices/noticeAbout200ABand201AB), 200A–B *"will
not be taught in the near future"*. Seven weeks rather than a semester. Search results still return
200A pages; they are archive, not current.

### berkeley-stat201b — Stat 201B, *Introduction to Statistics at an Advanced Level* { #berkeley-stat201b }

**Kind:** course · **Access:** fetchable — **scaffolding only**, no material in the repo
**Licence:** **CC BY 4.0** — on a repo containing only a syllabus
**Status:** unvetted · **Adapted:** none
<https://stat201b.berkeley.edu/>

*(unvetted)* The inference half, and the live replacement for Stat 200B. Estimation with emphasis on
maximum likelihood and exponential families, testing, linear models, Bayesian approaches. Named as
the prerequisite by the Dudoit genomics syllabi below, which makes it the entry point to that
sequence.

### berkeley-stat200ab — Stat 200A–B, *Advanced Introduction to Probability and Statistics* (retired) { #berkeley-stat200ab }

**Kind:** course · **Access:** fetchable — archive pages only
**Licence:** unresolved
**Status:** unvetted · **Adapted:** none
<https://www.stat.berkeley.edu/~rice/200B/>

*(unvetted)* **Retired.** Recorded so its absence is a decision rather than an oversight, and so the
archive pages that searches still surface are not mistaken for a current course. Use
[201A](#berkeley-stat201a) and [201B](#berkeley-stat201b). Rice's 200B page persists and holds real
material, which is the only reason to keep the entry.

### berkeley-stat210a — Stat 210A, *Theoretical Statistics* { #berkeley-stat210a }

**Kind:** course · **Access:** local · `sources/berkeley-stat210a/` — **211 PDFs** across three offerings
**Licence:** **CC BY 4.0** — all three offerings. Adaptable *and* publishable with attribution
**Status:** unvetted · **Adapted:** none
<https://stat210a.berkeley.edu/> · <https://github.com/berkeley-stat210a>

*(unvetted)* **The best-licensed substantial holding in this catalogue.** Fall 2024, 2025 and 2026,
each a complete course: 55–80 PDFs per offering, 829 MB in total. Decision theory, exponential
families, sufficiency, estimation, testing — the measure-theoretic treatment of inference rather
than the methods survey.

Unlike almost everything else here, the CC BY licence sits on repositories that **actually contain
the material**, which makes this the one Berkeley course where an adaptation could go straight to
`docs/adapted/` and be published.

### berkeley-stat210b — Stat 210B, *Theoretical Statistics* { #berkeley-stat210b }

**Kind:** course · **Access:** local · `sources/berkeley-stat210b/spring-2025/` — scaffolding, but see the notes below
**Licence:** **CC BY 4.0** on the repo; Guntuboyina's notes carry no statement
**Status:** unvetted · **Adapted:** none
<https://stat210b.berkeley.edu/> · notes: `sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf`

*(unvetted)* The Spring 2025 repo is a scaffold. The material is **Aditya Guntuboyina's complete
Spring 2018 lecture notes**, a single 1.0 MB PDF from his teaching page — asymptotics, empirical
process theory, minimax lower bounds. Second half of the 210 sequence.

### berkeley-guntuboyina-notes — Guntuboyina, complete lecture notes for 201A, 210B and 248 { #berkeley-guntuboyina-notes }

**Kind:** lecture notes · **Access:** local · `sources/berkeley-guntuboyina-notes/`
**Licence:** unresolved — no statement on the page or in the PDFs
**Status:** unvetted · **Adapted:** none
<https://www.stat.berkeley.edu/~aditya/styled/index.html>

*(unvetted)* Four self-contained PDFs, each a whole course written out: **201A** (Fall 2019 and Fall
2022), **210B** (Spring 2018), **248 Time Series** (Spring 2022). None of these are reachable from
the corresponding `stat<num>` course sites — the 201A repo is an empty scaffold while the notes for
the same course run to 820 KB.

Catalogued as one entry because it is one page's worth of output by one author, and splitting it
per course would imply four sources where there is one.

### berkeley-stat230a — Stat 230A, *Linear Models* { #berkeley-stat230a }

**Kind:** course · **Access:** local · `sources/berkeley-stat230a/spring-2025/` — thin; Spring 2026 is scaffolding only
**Licence:** Spring 2026 **CC BY 4.0** (scaffolding); Spring 2025 unlicensed
**Status:** unvetted · **Adapted:** none
<https://stat230a.berkeley.edu/>

*(unvetted)* Two offerings held, Spring 2025 and Spring 2026. The `NOASSERTION` needs the LICENSE
file opened before any adaptation.

## Applied and computational

### berkeley-stat243 — Stat 243, *Introduction to Statistical Computing* { #berkeley-stat243 }

**Kind:** course · **Access:** local · `sources/berkeley-stat243/` — 12 offerings, 30–53 PDFs each
**Licence:** **varies by offering** — 2024/2025/2026 CC BY 4.0; `stat243-fall-2021` CC0; `stat243-fall-2023` BSD-3-Clause; 2014–2020 and 2022 unlicensed
**Status:** unvetted · **Adapted:** none
<https://stat243.berkeley.edu/>

*(unvetted)* **The richest holding in this list by a distance** — sixteen repositories running from
Fall 2014 to Fall 2026, so the course can be read as it changed. Statistical computing: numerical
methods, optimisation, simulation, reproducibility, working in R and Python.

**The two licensed years are the only Berkeley material here that may be adapted into
`docs/adapted/` and published.** `stat243-fall-2021` is CC0 — public domain — and
`stat243-fall-2023` is BSD-3-Clause. Every other year is unlicensed and goes to `adapted-private/`.

### berkeley-stat153 — Stat 153, *Introduction to Time Series* { #berkeley-stat153 }

**Kind:** course · **Access:** local · `sources/berkeley-stat153/` — 5 offerings, 91 PDFs in Fall 2024 alone
**Licence:** Fall 2024 **CC BY 4.0**; the other four offerings unlicensed
**Status:** unvetted · **Adapted:** none
<https://stat153.berkeley.edu/>

*(unvetted)* Five offerings from Fall 2024 to Fall 2026 — the second-richest holding, and the only
one where consecutive semesters are all present.

### berkeley-stat158 — Stat 158, *The Design and Analysis of Experiments* { #berkeley-stat158 }

**Kind:** course · **Access:** local · `sources/berkeley-stat158/spring-2026/` — 46 PDFs, 513 files
**Licence:** Spring 2025 **CC BY 4.0** (but that offering is scaffolding only); Spring 2026 unlicensed
**Status:** unvetted · **Adapted:** none
<https://stat158.berkeley.edu/>

*(unvetted)* Two offerings, Spring 2025 and Spring 2026. Design of experiments is the half of
modelling judgement that the deleted modelling topic file gestured at and never covered.

### berkeley-stat157 — Stat 157, *Seminar on Topics in Probability and Statistics* { #berkeley-stat157 }

**Kind:** course · **Access:** unresolved — org holds the site theme and no content
**Licence:** unresolved
**Status:** unvetted · **Adapted:** none
<https://stat157.berkeley.edu/>

*(unvetted)* The org `berkeley-stat157` contains only the `.github.io` theme repo — no semester
repositories. Topics vary by offering; check `classes.berkeley.edu` for whether it currently runs.

## Causal inference

### berkeley-stat156-256 — Stat 156 / Stat 256, *Causal Inference* { #berkeley-stat156-256 }

**Kind:** course · **Access:** local · `sources/berkeley-stat156/fall-2024/` — 11 PDFs incl. the 256 syllabus
**Licence:** **CC BY-NC 4.0** — adaptable and publishable with attribution, non-commercial
**Status:** unvetted · **Adapted:** none
<https://stat156.berkeley.edu/> · syllabus: <https://stat156.berkeley.edu/fall-2024/stat256-syllabus.pdf>

*(unvetted)* **156 and 256 are the same course at two levels**, co-taught, and 256 has no site of
its own — its syllabus lives under the 156 domain, which is why `stat256.berkeley.edu` does not
resolve. Amanda Coston, Fall 2024. Potential-outcomes framework: randomised experiments,
observational studies, instrumental variables, principal stratification, mediation.

This is the **successor to Stat C239A / Pol Sci C236A**, so both of those numbers resolve here.

### berkeley-stat239a — Stat C239A, *The Statistics of Causal Inference in the Social Sciences* (retired) { #berkeley-stat239a }

**Kind:** course · **Access:** unreadable — department archive pages only
**Licence:** unresolved
**Status:** unvetted · **Adapted:** none

*(unvetted)* **Retired**, cross-listed with Political Science C236A, last offered around 2013.
Succeeded by [Stat 256](#berkeley-stat156-256). Recorded so the number resolves to its successor
rather than to a dead search result.

### berkeley-stat241b — Stat C241B, *Statistical Learning Theory* { #berkeley-stat241b }

**Kind:** course · **Access:** unresolved — org holds the site theme and no content
**Licence:** unresolved
**Status:** unvetted · **Adapted:** none
<https://stat241b.berkeley.edu/>

*(unvetted)* Both `berkeley-stat241a` and `berkeley-stat241b` exist as orgs holding only the theme
repo. `stat241a.berkeley.edu` does not resolve at all.

## Statistical genomics — the Public Health cross-listings

These do **not** use the `stat<num>` system. They are cross-listed with Public Health, taught by
Sandrine Dudoit, and their material is on her pages under `stat.berkeley.edu/~sandrine/` — where
directory listing is disabled, so files are reachable only by exact URL.

Both syllabi below are from 2018 and were read directly; whether the courses still run needs
`classes.berkeley.edu`. Neither has a required textbook — *"lecture notes and references will be
provided on the class website"*, which means bCourses.

### berkeley-stat245c-leishi — Stat C245C, *Computational Statistics with Applications in Biology and Medicine* (Lei Shi, Fall 2021) { #berkeley-stat245c-leishi }

**Kind:** course · **Access:** local · `sources/berkeley-stat-c245c-leishi/` — 24 files: 11 lecture PDFs, 3 labs with R code, 2 homework sets **with solutions**, datasets
**Licence:** **unresolved** — no statement on the site. Adaptations stay in `adapted-private/`
**Status:** unvetted · **Adapted:** none
<https://leishi-rocks.github.io/courses/ph240c/ph240c-materials.html> · [schedule](https://leishi-rocks.github.io/courses/ph240c/ph240c-schedule.html)

*(unvetted)* **The one complete, public offering of a C245 course.** Lei Shi, Fall 2021, on a
personal GitHub Pages site rather than anything the department links. Dudoit's offerings of the same
course are on bCourses; this one is not.

Lectures: GLM and SVM, empirical risk minimisation and kernel methods, metric learning, CART,
bagging and boosting, semi-supervised learning, neural networks, streaming data in electronic
medical records, design of experiments, adaptive clinical trials and reinforcement learning.
Two lectures (deep learning, Mendelian randomisation) have no PDF on the schedule.

**Homework with solutions is the rare part.** Most of the catalogue is notes without exercises or
exercises without answers; this has both, plus the datasets to run them on.

Note the drift in what "C245C" means: this offering is machine-learning-shaped, where Dudoit's is
classical computational statistics. Same course code, materially different course — the year and
instructor matter more than the number.

### berkeley-stat245cd-dudoit — Stat C245C–D, *Computational Statistics with Applications in Biology and Medicine* (Dudoit) { #berkeley-stat245cd-dudoit }

**Kind:** syllabus · **Access:** unreadable — notes on the class website (bCourses); syllabus public
**Licence:** unresolved
**Status:** unvetted · **Adapted:** none
Also listed as PB HLTH C240C–D · syllabus: <https://www.stat.berkeley.edu/~sandrine/Teaching/syllabus_PHC240C_F18.pdf>

*(unvetted)* Sandrine Dudoit. High-dimensional, computer-intensive statistics on data from
state-of-the-art biological assays, in R, with computational reproducibility as an explicit theme.
Syllabus topics: PCA and MDS, cluster analysis, loss-based estimation, GLMs, CART, SVM, smoothing
and splines, ridge/LASSO/LARS, EM, cross-validation, the bootstrap, bagging and boosting, MCMC and
importance sampling, **Markov and hidden Markov models**, multiple hypothesis testing, dynamic
programming. Prerequisite Stat 201A–B.

Overlaps heavily with what is already held — PCA, HMMs, spectral methods — which makes it a
*connective* source rather than a new one: the same machinery aimed at assay data.

**Only the syllabus is reachable**, so this entry is a topic map, not material. Its value is as a
curriculum to work through using sources that *are* public.

### berkeley-stat245ab-vanderlaan — Stat C245A–B, *Modern Biostatistical Theory* and *Survival Analysis and Causality* { #berkeley-stat245ab-vanderlaan }

**Kind:** course notes · **Access:** local · `sources/berkeley-stat-c245b-vanderlaan/` — 16 files
**Licence:** **all rights reserved** — the site footer reads "© 2018-2021. All rights reserved." Adaptations stay in `adapted-private/`
**Status:** unvetted · **Adapted:** none
<https://vanderlaan-lab.org/teaching/>

*(unvetted)* Mark van der Laan's teaching archive, and the substantial public half of the C245
sequence. Full course notes, not syllabi: *Survival Analysis and Causality* (2004), the *Marginal
Structural Models* lecture, *Causal Inference* (2004) with its syllabus, *Theoretical Statistics
210B* notes with the loss-based estimation lecture, *Computational Biology* (2001), and
*Multivariate Statistical Methods in Genomics* (2007).

The notes are old and unpolished — typos, steps left half-worked. That is arguably the point: the
reasoning is still visible rather than compressed into a theorem sequence, which is the failure
mode a finished textbook has by construction.

Nonparametric models, loss-based estimation, asymptotic linearity, **influence functions**, the
bootstrap, and TMLE. The influence-function material is the theoretical spine, and the papers below
are the better entry point into it.

### berkeley-stat245ef — Stat C245E–F, *Statistical Genomics I and II* { #berkeley-stat245ef }

**Kind:** course · **Access:** unreadable — notes on the class website (bCourses); syllabus public
**Licence:** unresolved
**Status:** unvetted · **Adapted:** none
Also listed as PB HLTH C240E–F · syllabus: <https://www.stat.berkeley.edu/~sandrine/Teaching/syllabus_PHC240F_S18.pdf>

*(unvetted)* **The closest thing in this list to the day job.** Dudoit, with Kelly Street as reader.
High-throughput microarray and sequencing assays: transcription (RNA-Chip / RNA-Seq),
protein–nucleic acid interactions (ChIP-Seq), DNA methylation (methyl-Seq), copy number (CGH).

The Spring 2018 offering *"will first discuss the statistical analysis of meiosis and then focus on
**single-cell transcriptome sequencing (scRNA-Seq)**"*. Part I covers meiosis, population genetics
and genetic mapping.

## The way into C245A — papers, because the course notes are not the best route

The influence-function machinery under C245A is one of the places where the primary literature is
simply better than the course material: the notes assume the construction, and the papers derive
it. Catalogued here rather than in [statistics](statistics.md) because this is the trail from the
course, and that is the thing worth not losing.

### hines-2021-demystifying-eif — Hines, Dukes, Diaz-Ordaz & Vansteelandt 2021, *Demystifying statistical learning based on efficient influence functions* { #hines-2021-demystifying-eif }

**Kind:** paper · **Access:** fetchable · <https://arxiv.org/abs/2107.00681>
**Licence:** arXiv — check the per-paper licence before adapting
**Status:** unvetted · **Adapted:** none

*(unvetted)* Derives the efficient influence function as a Gâteaux derivative of the target
functional, then uses the von Mises expansion to show why the plug-in bias correction is *forced*
rather than clever. That is precisely a **how could I have come up with this?** answer for an object
normally introduced by assertion — which is why it is here rather than the course notes.

The stated problem is the one worth holding: data-adaptive methods are tuned for minimal prediction
error, not minimal mean squared error of an estimator, and the bias that follows does not shrink
fast enough for inference. Short, and it defers the tangent-space geometry elsewhere.

### fisher-kennedy-influence-functions — Fisher & Kennedy, *Visually Communicating and Teaching Intuition for Influence Functions* { #fisher-kennedy-influence-functions }

**Kind:** paper · **Access:** fetchable · <https://arxiv.org/abs/1810.03260>
**Licence:** arXiv — check the per-paper licence before adapting
**Status:** unvetted · **Adapted:** none

*(unvetted)* The geometric companion to the above: the influence function as a direction in
$L^2(P)$. Should land quickly given the PCA-as-Gram-matrix and $L^2$ picture already held — it is
the same geometry with a different object in it, which makes it a candidate for the *Attached to*
section of a topic file before it is even read.

### dudoit-multiple-testing-genomics — Dudoit & van der Laan, *Multiple Testing Procedures with Applications to Genomics* { #dudoit-multiple-testing-genomics }

**Kind:** book · **Access:** fetchable · <https://www.stat.berkeley.edu/~sandrine/MTBook/>
**Licence:** all rights reserved — Springer
**Status:** unvetted · **Adapted:** none

*(unvetted)* The book behind the multiple-testing half of the courses above, with a companion page
on Dudoit's site. Multiple testing is the piece of the genomics statistics stack most often applied
without being understood, which makes it a candidate for a session rather than a skim.

## Not found

Recorded so their absence is a decision:

| Course | Why |
| --- | --- |
| `Stat C247C`, *Longitudinal Data Analysis* | Cross-listed with Public Health, offered in **even-numbered years only**. No vanity domain, no GitHub org, no public syllabus located. Mixed models versus GEE for repeated-measures data |
| `Stat 230B` | No vanity domain and no org — only 230A exists in the system |
| `Stat C241A` | Org holds the theme repo only; the domain does not resolve |
