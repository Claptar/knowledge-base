---
title: Resources
---

# Resources

Evaluated materials. Every entry carries a **verdict** — what it is good for and what is wrong
with it — and a **reachability**, which says whether the thing can actually be opened right now.
The verdict is the expensive part; it is why this exists rather than a bookmark folder.

## By subject

| | |
| --- | --- |
| [Courses](courses.md) | MIT OCW course exports held locally — lecture notes, problem sets, transcripts |
| [Doing mathematics](doing-mathematics.md) | process and heuristics rather than content |
| [Analysis](analysis.md) | real and complex |
| [Linear algebra](linear-algebra.md) | sources of *problems*, not courses |
| [Probability](probability.md) | |
| [Statistics](statistics.md) | inference, modelling judgement, experimental design |
| [Stochastic processes](stochastic-processes.md) | the probability map and the mechanism map |
| [CME and transcription](cme-transcription.md) | the primary literature the [learning path](../path.md) terminates in |
| [Modelling](modelling.md) | modelling craft, optimisation, validation and uncertainty |

## Entry format

Each entry is a `###` heading whose slug is the source's identity across the whole repo, so it can
be linked to directly — `resources/stochastic-processes.md#van-kampen-sppc` — rather than restated.

```markdown
### van-kampen-sppc — van Kampen, *Stochastic Processes in Physics and Chemistry* { #van-kampen-sppc }

**Kind:** book · **Access:** local · `sources/van-kampen-sppc/book.pdf`
**Licence:** all rights reserved — adaptation stays unpublished
**Status:** unvetted · **Adapted:** none

The verdict, in prose: what it is good for, what is weak, whether it motivates or merely states.
```

That one slug ties every place a source appears, and the directory name **is** the slug:

```
docs/resources/stochastic-processes.md#van-kampen-sppc   the entry and the verdict
sources/van-kampen-sppc/                                 the local copy, gitignored
docs/adapted/<topic>-van-kampen-sppc.md                  the adaptation, if one exists
docs/topics/…, docs/practice/…                           what he actually did with it
```

## How a source folder is laid out

Sources arrive from different places with incompatible naming — MIT OCW alone uses four schemes
across six courses. They are normalised **once at ingest** so that everything downstream reads one
layout instead of learning each publisher's conventions:

```
sources/<slug>/
  lectures/       01-slides.pdf  01-transcript.pdf  01-captions.srt
  recitations/    2014-02-11-slides.pdf        # dated material keeps its date
  psets/          03-questions.pdf
  solutions/      exams/  tutorials/  lecture-outlines/
  worked-examples/  coupon-collector-transcript.pdf
  recordings/     video-derived files with no better name than their id
  other/          genuinely miscellaneous
  _manifest.csv   every file's original publisher filename
  book.pdf        for a book rather than a course
```

Filenames are `<index-or-slug>-<artefact type>.<ext>`. An **index** is used where the title carries
nothing ("Lecture 4"); a **slugified title** is kept where it does, because for a worked-example
clip the title is the content and `07` would throw that away; a **date** is used where the source
dates rather than numbers its material, since inventing an index there produces four different
recitations all claiming to be number 2.

**`_manifest.csv` is not optional.** It maps every normalised path back to the publisher's original
filename, which is the only route back to the thing on their site. Without it a renamed file cannot
be checked against its source, and the rule that every claim is checkable would be broken. It also
makes the rename reversible, which is how two bugs in this repo's own normaliser were caught and
fixed without data loss.

Scripts live in `skills/adapt-recordings/scripts/` — `course_inventory.py` to see what a source
holds, `organise_course.py` to sort a flat export into the folders above, `normalise_names.py` to
rename, and `transcript_text.py` to turn a `.srt`/`.vtt` caption file into readable timestamped
prose. Only the two that move files take `--apply`, and neither does anything without it;
the other two only read.

The original publisher archives stay in `sources/_archives/`. With `_manifest.csv` they are what
makes the normalisation reversible — the zip is the source of truth for what a file was called
before this repo renamed it.

## Access — can this actually be opened?

The field that decides whether an agent can use an entry at all. **An agent must never work around
this by reconstructing a source from memory.** If a source is out of reach, the honest move is to
say so.

| Value | Means | What an agent does |
| --- | --- | --- |
| `fetchable` | public, stable URL | read it now |
| `local` | file in `sources/` | read it if present — `sources/` is gitignored, so it exists only on the machine that downloaded it. The URL is recorded too, for re-acquisition |
| `private-host` | on the home media server, over VPN | read it when the VPN is up; otherwise report unreachable |
| `unreadable` | physical copy, DRM, or paywalled with no copy held | **say so.** Cite it, never quote it |

## Licence — can an adaptation be published?

This site is public, and an adaptation of a source is a derivative work. The licence decides where
the adaptation is allowed to live.

| Licence | Adaptation goes to |
| --- | --- |
| CC BY-NC-SA (MIT OCW), CC BY, public domain | `docs/adapted/` — **published**, with attribution, and the file carries the same licence, since share-alike propagates |
| all rights reserved — textbooks, paywalled papers, unlicensed course pages | `adapted-private/` — gitignored, never published |
| unclear | `adapted-private/`, and say the licence is unresolved. Never guess in the publishing direction |

Raw sources are never committed under any licence — see [`sources/README.md`](https://github.com/Claptar/knowledge-base/blob/main/sources/README.md).

## Status

| Value | Means |
| --- | --- |
| `unvetted` | a recommendation, not a judgement. A recommendation repeated is not a verdict earned |
| `reading` | in progress |
| `worked` | actually used — the verdict below is mine |

> **Provenance.** Most book entries came from an external reading guide (2026-09-13) and the CME
> papers from the Pachter Lab's own reading list, not from my reading. They are candidates. The
> `unvetted` status is not decoration — it marks the difference between a list and a judgement.

## When this outgrows a file

A subject file past roughly thirty entries should split by sub-topic rather than grow. The index
above is the only place that needs to change.
