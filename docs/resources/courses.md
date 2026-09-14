---
title: Courses
---

# Courses

MIT OpenCourseWare exports, held locally in `sources/`. All are **CC BY-NC-SA**, so adaptations
may be published in `docs/adapted/` with attribution — and carry the same licence, because
share-alike propagates.

Each export was unpacked to content only: lecture notes, problem sets and transcripts, with the
HTML site shell dropped and duplicate transcript encodings removed. The original archives are kept
in `sources/_archives/`.

> **Reachability.** `sources/` is gitignored, so these exist only on the machine that downloaded
> them. Every entry records the OCW course page so the export can be re-acquired.

**Transcripts are OCW's own**, published as caption files beside the videos — nothing here was
produced by speech-to-text. Three of the six courses have them; the other three have no recordings
at all, so there is nothing to transcribe. A recording without published captions would need a
speech-to-text pass first, which is a separate job with its own failure modes — see
`skills/adapt-recordings/SKILL.md`.

## Probability

### ocw-6041sc — MIT 6.041SC, *Probabilistic Systems Analysis and Applied Probability* { #ocw-6041sc }

**Kind:** course · **Access:** local · `sources/ocw-6041sc/`
**Converted:** [452 pages in the reference library](https://claptar.github.io/knowledge-base-library/probability/mit-ocw/6041sc/) — lectures, recitations and transcripts
**Instructor:** John Tsitsiklis · Fall 2013
**Licence:** CC BY-NC-SA — adaptations publishable with attribution and the same licence
**Status:** unvetted · **Adapted:** none
**Holds:** 249 PDFs, 152 transcript files covering **76 recordings**
<https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/>

*(unvetted)* The largest transcript corpus here by a wide margin, and the reason the
`adapt-recordings` skill exists: Tsitsiklis lectures plus short problem-walkthrough clips, all as
text. Likely below the level needed as a course — it is an undergraduate first course in
probability — but the recorded problem sessions are a different kind of object from a textbook, and
the worked-example clips are the part worth mining. Judge before adapting: the lecture set may be
redundant with DeGroot, while the clips may not be.

## Computational and systems biology

### ocw-6047 — MIT 6.047, *Computational Biology* { #ocw-6047 }

**Kind:** course · **Access:** local · `sources/ocw-6047/`
**Instructor:** Manolis Kellis · Fall 2015
**Licence:** CC BY-NC-SA
**Status:** unvetted · **Adapted:** none
**Holds:** 19 PDFs — 13 lecture notes, 5 problem sets, plus a compiled full-course PDF. No recordings
<https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/>

*(unvetted)* Lecture notes only, but complete ones — the compiled PDF is the whole course as a
single document. Closest of these to daily work, so the useful question is which parts say
something the working knowledge does not already cover.

### ocw-7091j — MIT 7.91J, *Foundations of Computational and Systems Biology* { #ocw-7091j }

**Kind:** course · **Access:** local · `sources/ocw-7091j/`
**Instructors:** Christopher Burge, David Gifford, Ernest Fraenkel · Spring 2014
**Licence:** CC BY-NC-SA
**Status:** unvetted · **Adapted:** none
**Holds:** 67 PDFs, 44 transcripts
<https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/>

*(unvetted)* Three instructors, so expect unevenness rather than one voice. Both notes and
recordings, which makes it a reasonable second test of the transcript pipeline after 6.041SC.

## Statistical physics of biological systems

The layer between the mathematics and the [CME literature](cme-transcription.md) — where stochastic
descriptions are derived from mechanism rather than assumed.

### ocw-8592j — MIT 8.592J, *Statistical Physics in Biology* { #ocw-8592j }

**Kind:** course · **Access:** local · `sources/ocw-8592j/`
**Instructors:** Mehran Kardar, Leonid Mirny · Spring 2011
**Licence:** CC BY-NC-SA
**Status:** unvetted · **Adapted:** none
**Holds:** 24 PDFs — lecture notes and problem sets. No recordings
<https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/>

*(unvetted)* Kardar's statistical mechanics applied to biological systems. On the evidence of the
file list this is the most likely of the six to be directly load-bearing for the
[learning path](../path.md): it sits exactly where van Kampen sits, between microscopic mechanism
and macroscopic description, and Kardar is a careful writer. Notes are terse — they are lecture
notes, not a textbook.

### ocw-8591j-2014 — MIT 8.591J, *Systems Biology* { #ocw-8591j-2014 }

**Kind:** course · **Access:** local · `sources/ocw-8591j-2014/`
**Instructor:** Jeff Gore · Fall 2014
**Licence:** CC BY-NC-SA
**Status:** unvetted · **Adapted:** none
**Holds:** 40 PDFs, 48 transcripts
<https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/>

*(unvetted)* Physics-department systems biology, with recordings. Gore works on population dynamics
and stochastic effects in small populations, which is adjacent to the noise questions in the CME
literature.

### ocw-8591j-2004 — MIT 8.591J, *Systems Biology* (2004) { #ocw-8591j-2004 }

**Kind:** course · **Access:** local · `sources/ocw-8591j-2004/`
**Instructor:** Alexander van Oudenaarden · Fall 2004
**Licence:** CC BY-NC-SA
**Status:** unvetted · **Adapted:** none
**Holds:** 34 PDFs. No recordings
<https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/>

*(unvetted)* The earlier version of the same course under a different instructor, and van
Oudenaarden's own experimental work is on stochastic gene expression — so this may be closer to the
CME material than the 2014 version despite being a decade older. Worth comparing against
`ocw-8591j-2014` rather than assuming the newer supersedes it.
