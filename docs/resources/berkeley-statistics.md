---
title: Berkeley statistics
---

# UC Berkeley statistics courses

Course sites and their GitHub repositories. Collected 2026-09-13 by the `collect-materials` skill;
the harvesting recipe is in that skill's `references/berkeley.md`.

> **Provenance.** These are *located*, not judged. Every entry is `unvetted`: nothing here has been
> read, and a list is not a verdict. The useful work this page does today is saying which courses
> have public material and which do not.

> **No blanket licence.** Unlike [MIT OCW](courses.md), Berkeley makes no institution-wide CC grant.
> The default is all rights reserved, so adaptations go to `adapted-private/` unless an entry below
> names a real licence. Two do.
>
> The `berkeley-stat<num>.github.io` repos all report `MIT` through GitHub's API. That is the
> licence of the *Jekyll theme* — its copyright line names the template's author, not Berkeley — and
> it says nothing about course content. It is recorded here so nobody trusts it twice.

## How to read these entries

`Access: local` never appears yet — nothing has been downloaded. The distinction that matters:

| | Means |
| --- | --- |
| `fetchable` | the GitHub repo is public and has content in it |
| `unreadable` | the material is behind **bCourses**, Berkeley's Canvas. Not reachable, and no mirror exists |
| `unresolved` | the course exists but where its material lives has not been established |

## Probability and stochastic processes

### berkeley-stat150 — Stat 150, *Stochastic Processes* { #berkeley-stat150 }

**Kind:** course · **Access:** unreadable — Spring 2026 runs on bCourses
**Licence:** unresolved — no licence on the content repo
**Status:** unvetted · **Adapted:** none
<https://stat150.berkeley.edu/> · <https://github.com/berkeley-stat150/spring-2026>

*(unvetted)* Vadim Gorin, Spring 2026. Random walks, discrete-time Markov chains, Poisson
processes, then continuous-time chains, queueing, point processes, branching, renewal, stationary
and Gaussian processes. The page names the instructor and the syllabus; the material itself is on
bCourses. Directly on the route in [path.md](../path.md) — nodes 4 and 5 — which makes the
inaccessibility worth a login rather than a shrug.

### berkeley-stat205a — Stat C205A, *Probability Theory* { #berkeley-stat205a }

**Kind:** course · **Access:** fetchable · <https://github.com/berkeley-stat205a/fall-2024>
**Licence:** unresolved — content repo carries no licence
**Status:** unvetted · **Adapted:** none
<https://stat205a.berkeley.edu/> · also listed as Math C218A

*(unvetted)* Measure-theoretic probability, the first half of a year course, for students whose
research will involve rigorous proofs in probability. Durrett is the usual text. The **legacy pages
under `~aldous/205A` carry lecture notes and scribe notes** that the current site does not, and are
the better starting point: <https://www.stat.berkeley.edu/~aldous/205A>.

### berkeley-stat205b — Stat C205B, *Probability Theory* { #berkeley-stat205b }

**Kind:** course · **Access:** fetchable · <https://github.com/berkeley-stat205b/spring-2026>
**Licence:** unresolved
**Status:** unvetted · **Adapted:** none
<https://stat205b.berkeley.edu/> · also listed as Math C218B

*(unvetted)* Second half of the C205 sequence — martingales, Brownian motion, weak convergence.
Aldous's 205B page carries per-lecture PDFs including a measure-theory recap:
<https://www.stat.berkeley.edu/~aldous/205B>. Relevant to [path node 3](../path.md#3-martingale).

### berkeley-stat206a — Stat C206A, *Advanced Topics in Probability* { #berkeley-stat206a }

**Kind:** course · **Access:** fetchable · <https://github.com/berkeley-stat206a/fall-2024>
**Licence:** unresolved
**Status:** unvetted · **Adapted:** none
<https://stat206a.berkeley.edu/> · also listed as Math C223A

*(unvetted)* Topics course; content varies by offering, so the year matters more than the number.

### berkeley-stat206b — Stat C206B, *Advanced Topics in Probability* { #berkeley-stat206b }

**Kind:** course · **Access:** fetchable · <https://github.com/berkeley-stat206b/spring-2026>
**Licence:** unresolved
**Status:** unvetted · **Adapted:** none
<https://stat206b.berkeley.edu/> · also listed as Math C223B

*(unvetted)* Two offerings held, Spring 2025 and Spring 2026. Topics course, as C206A.

## Statistical theory

### berkeley-stat201a — Stat 201A, *Introduction to Probability at an Advanced Level* { #berkeley-stat201a }

**Kind:** course · **Access:** fetchable · <https://github.com/berkeley-stat201a/fall-2024>
**Licence:** unresolved
**Status:** unvetted · **Adapted:** none
<https://stat201a.berkeley.edu/>

*(unvetted)* **This is the live replacement for Stat 200A.** The 200A–B sequence was revamped into
201A–B in 2012–13 and, per the department's
[notice](https://statistics.berkeley.edu/courses/notices/noticeAbout200ABand201AB), 200A–B *"will
not be taught in the near future"*. Seven weeks rather than a semester. Search results still return
200A pages; they are archive, not current.

### berkeley-stat201b — Stat 201B, *Introduction to Statistics at an Advanced Level* { #berkeley-stat201b }

**Kind:** course · **Access:** fetchable · <https://github.com/berkeley-stat201b/fall-2024>
**Licence:** unresolved
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

### berkeley-stat230a — Stat 230A, *Linear Models* { #berkeley-stat230a }

**Kind:** course · **Access:** fetchable · <https://github.com/berkeley-stat230a/spring-2026>
**Licence:** unresolved — `NOASSERTION` on the 2026 repo, unread
**Status:** unvetted · **Adapted:** none
<https://stat230a.berkeley.edu/>

*(unvetted)* Two offerings held, Spring 2025 and Spring 2026. The `NOASSERTION` needs the LICENSE
file opened before any adaptation.

## Applied and computational

### berkeley-stat243 — Stat 243, *Introduction to Statistical Computing* { #berkeley-stat243 }

**Kind:** course · **Access:** fetchable · <https://github.com/berkeley-stat243>
**Licence:** **varies by year** — `stat243-fall-2021` is CC0-1.0, `stat243-fall-2023` is BSD-3-Clause, the rest unlicensed
**Status:** unvetted · **Adapted:** none
<https://stat243.berkeley.edu/>

*(unvetted)* **The richest holding in this list by a distance** — sixteen repositories running from
Fall 2014 to Fall 2026, so the course can be read as it changed. Statistical computing: numerical
methods, optimisation, simulation, reproducibility, working in R and Python.

**The two licensed years are the only Berkeley material here that may be adapted into
`docs/adapted/` and published.** `stat243-fall-2021` is CC0 — public domain — and
`stat243-fall-2023` is BSD-3-Clause. Every other year is unlicensed and goes to `adapted-private/`.

### berkeley-stat153 — Stat 153, *Introduction to Time Series* { #berkeley-stat153 }

**Kind:** course · **Access:** fetchable · <https://github.com/berkeley-stat153>
**Licence:** unresolved — `NOASSERTION` on fall-2024, none on the rest
**Status:** unvetted · **Adapted:** none
<https://stat153.berkeley.edu/>

*(unvetted)* Five offerings from Fall 2024 to Fall 2026 — the second-richest holding, and the only
one where consecutive semesters are all present.

### berkeley-stat158 — Stat 158, *The Design and Analysis of Experiments* { #berkeley-stat158 }

**Kind:** course · **Access:** fetchable · <https://github.com/berkeley-stat158/spring-2026>
**Licence:** unresolved — `NOASSERTION` on spring-2025
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

**Kind:** course · **Access:** fetchable · <https://github.com/berkeley-stat156/fall-2024>
**Licence:** unresolved — `NOASSERTION` on fall-2024
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

### berkeley-stat245cd — Stat C245C–D, *Computational Statistics with Applications in Biology and Medicine* { #berkeley-stat245cd }

**Kind:** course · **Access:** unreadable — notes on the class website (bCourses); syllabus public
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
