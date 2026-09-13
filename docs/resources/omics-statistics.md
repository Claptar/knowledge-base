---
title: Omics statistics
---

# Statistics for omics data

Courses that teach statistical inference *on the data he actually works with* — proteomics, bulk
and single-cell RNA-seq — rather than on generic examples. Collected 2026-09-13.

> **Provenance.** Located, not judged. Every entry is `unvetted`. Three of the four came from him
> directly rather than from a search, so the discovery judgement is his; what this page adds is the
> licence, the reachability and what is actually in each repository.

This is the closest material in the whole catalogue to the day job, which cuts both ways: the
anchors are strong, and the risk of reading something he already holds is higher than usual. The
useful question for these is not *what does it cover* but *which parts does it motivate that he
currently does by habit*.

## The statOmics group — Ghent University

Lieven Clement's group, and the authors of the methods rather than teachers of them: `tradeSeq`,
`satuRn`, `stageR` and `msqrob2` are all theirs, and all in the `statOmics` org alongside the
courses. That makes these courses unusually close to their primary literature — the lecture and the
paper have the same author, which is exactly the pairing worth harvesting together.

### statomics-sga2020 — *Statistical Genomics Analysis 2020* { #statomics-sga2020 }

**Kind:** course · **Access:** local · `sources/statomics-sga2020-ghpages/` — 229 files: 57 HTML tutorials, 44 Rmd, 14 PDF
**Licence:** **unresolved** — no licence file on any branch. Adaptations stay in `adapted-private/`
**Status:** unvetted · **Adapted:** none
<https://statomics.github.io/SGA2020/> · <https://github.com/statOmics/SGA2020>

*(unvetted)* Statistical concepts in preprocessing, quantification and differential analysis of
high-throughput omics, in R/Bioconductor. Three parts: **quantitative proteomics** (identification,
FDR and the target–decoy approach, label-free preprocessing, factorial designs, stagewise testing);
**next-generation sequencing** (GLMs, complex designs, differential expression, transcript-level
analysis); **single-cell RNA-seq** (workflow, trajectory analysis, differential transcript usage).

**The content is on the `gh-pages` branch**, not `master` — `master` holds five files. Two further
branches, `data` (697 MB) and `data-rnaseq` (143 MB), carry the datasets that make the tutorials
runnable. Both are cloned; neither is needed to read the material.

### statomics-sga21 — *Statistical Genomics Analysis 2021* { #statomics-sga21 }

**Kind:** course · **Access:** local · `sources/statomics-sga21/` — 148 files: 35 Rmd, 19 PDF
**Licence:** **unresolved** — no licence file
**Status:** unvetted · **Adapted:** none
<https://github.com/statOmics/SGA21>

*(unvetted)* The following year's offering of [SGA2020](#statomics-sga2020), and structured
normally — content on the default branch, no `gh-pages` split.

Worth cataloguing separately rather than as a newer copy, because its `docs/` directory carries
**background papers as PDFs** — Martens on proteomics bioinformatics, an Illumina sequencing
primer, and others. That is a reading list assembled by the people who wrote the methods, which is
the expensive judgement and the thing a course website usually omits.

### statomics-statistiekcursusnotas — *Cursus Statistiek 2019–2020* { #statomics-statistiekcursusnotas }

**Kind:** course notes · **Access:** local · `sources/statomics-statistiekcursusnotas-ghpages/` — 15 HTML chapters
**Licence:** **unresolved** — no licence file
**Status:** unvetted · **Adapted:** none
<https://statomics.github.io/statistiekCursusNotas/>

*(unvetted)* **Written in Dutch** — *"Hoofdstuk 6: Enkelvoudige lineaire regressie"*. A bookdown
statistics course: study design, ANOVA, linear regression, the standard first-course sequence.

Flagged rather than recommended. The language is a real barrier where Russian is not, and the
material is introductory — which [his profile](../profile.md#how-i-study) rules out on its own. It
is catalogued because he supplied it and because the `statOmics` connection may make it worth more
than it looks, not because the contents argue for it. Content is on `gh-pages`; `master` holds only
a README.

## Gulbenkian Training Programme in Bioinformatics

### gtpb-psls20 — *Practical Statistics for the Life Sciences 2020* { #gtpb-psls20 }

**Kind:** course · **Access:** local · `sources/gtpb-psls20/` — 125 files: 49 Rmd, 40 HTML
**Licence:** **CC BY 4.0** — adaptable *and* publishable with attribution
**Status:** unvetted · **Adapted:** none
<https://gtpb.github.io/PSLS20/> · <https://github.com/GTPB/PSLS20>

*(unvetted)* GTPB, Oeiras, Portugal — a training programme running since 1999. A `theory/`
directory of worked chapters: data exploration, multiple regression, non-parametric statistics
(Wilcoxon–Mann–Whitney), categorical data analysis, each as paired Rmd source and rendered HTML.

**The best-licensed entry on this page.** GTPB states the intent explicitly — *"licensed so that
the training materials are fully reusable, while proper acknowledgement is given to the authors"* —
and the licence is a real CC BY 4.0 grant in `License.md`. GitHub reports the repo as
`NOASSERTION`, which would have read as "unlicensed" to anyone trusting the API field.

Alongside [Stat 210A](berkeley-statistics.md#berkeley-stat210a), this is one of only two
substantial holdings in the catalogue whose adaptation could go to `docs/adapted/` and be
published.

## What is missing here

The statOmics courses teach the *analysis* of single-cell data. The [learning
path](../path.md) is about the *generative model* underneath it — the chemical master equation, the
telegraph model, capture efficiency as a thinning layer. Those meet at
[node 17](../path.md#17-technical-noise-as-a-thinning-layer) and nowhere earlier.

Neither of these is the other's prerequisite, and treating this page as a shortcut into the path
would be the wrong read. It is the other direction: the path explains where the data he analyses
comes from.
