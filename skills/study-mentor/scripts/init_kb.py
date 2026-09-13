#!/usr/bin/env python3
"""Create the study knowledge base skeleton.

Usage:
    python init_kb.py <path>

<path> is the **knowledge base root** — the directory that holds profile.md, topics/ and the
rest. In a repo that also publishes a site that is `docs/`, so pass `docs/`, not the repo root.

Creates directories and seed files. Never overwrites an existing file — safe to re-run on a
partially built knowledge base.

Deliberately not generated: the site config (mkdocs.yml) and the CI workflow. Publishing is a
separate decision from having a knowledge base, and a generated half-config is worse than none.
"""

import sys
from pathlib import Path

INDEX = """# Study knowledge base

What is recorded here is the **trajectory**: which question opened a topic, what it attached to,
where it clicked, and what is still loose. A clean restatement of the material is available in any
textbook and is deliberately not stored.

- **Looking for what's live?** -> [Open questions](questions.md). The index is questions, not
  subjects; subjects are how textbooks index, and the textbooks already exist.
- **Resuming?** -> [Study log](log.md). Newest first, next step at the top.
- **Wondering what comes next?** -> [Learning path](path.md). A plan, not a record.
- **Looking something up?** -> [Resources](resources/index.md) for verdicts, or
  [Profile](profile.md) for background and anchors.
- **Want an explanation rather than a record?** -> [Notes](notes/index.md).
"""

PROFILE = """# Profile

Background, habits and anchors. Updated when something changes, not every session.

## Mathematical background

## Working context

## Notation and conventions

## Anchors worth building on

## How I study
- Understanding means being able to answer "how could I come up with this?"
- Proofs are mine to do; a handed-over proof removes the point.
- Connections between topics matter more than coverage of one.
"""

LOG = """# Study log

Newest first. The top of this file is what the next session reads.

## Next
_Nothing queued yet._

---
"""

QUESTIONS = """# Open questions

The front door. This knowledge base is indexed by **question**, not by subject — subjects are what
textbooks index, and the textbooks already exist.

A question earns a place here the moment it is asked properly. It earns a *page* only once a
session has been spent on it: harvest, don't design.

## Live

| Question | Status | Where |
| --- | --- | --- |

## Status vocabulary

| Status | Means |
| --- | --- |
| `open` | live — the next session could pick it up |
| `parked` | a real question, deliberately not being worked now |
| `answered` | a topic file answers it in my own words |

## Markers

`**Not yet derived.**` for something taken on trust from a source; `**Unverified.**` for something
inferred rather than checked. Their count is the honest progress metric.

```bash
grep -rn "Not yet derived\\|Unverified" topics/ adapted/ practice/ | wc -l
```
"""

PATH = """# Learning path

**Destination:** what I will be able to *do*, not what I will have covered.
**Designed:** YYYY-MM-DD

> **Provenance.** Designed, not harvested. Every other page here is written after a session; this
> one is written before, which makes it a different kind of object. Nothing here is evidence that
> anything has been understood.

## Plan, not record

A node is not a page: completing one creates no file, and most nodes never get one. Its question is
a reconstruction of what *would* force the concept, and it reaches the `questions.md` Live table
only once I hold it without re-reading the node. Delete nodes that stop biting, and say so in
`log.md` — that is this page working.

**No `Status` field, no markers, nothing that reads as evidence. One path page only.**

## Layer 1 — <what this layer is for>

### 1. <Concept>

**Needs** nothing.

The question that would force this concept, in two or three lines.

**Anchor.** The specific existing thing it attaches to — same standard as a topic file.
**Source.** A link into `resources/`, never a verdict restated here.

## What this path deliberately leaves out

Named, so the absence is a decision rather than an oversight.
"""

RESOURCES_INDEX = """# Resources

Evaluated materials, one file per subject. Every entry carries a verdict — what it's good for and
what's wrong with it — and a reachability, which says whether the source can actually be opened.

## Entry format

```markdown
### <slug> — <Author, Title> { #<slug> }

**Kind:** book · **Access:** local · `sources/<slug>/book.pdf`
**Licence:** all rights reserved — adaptation stays unpublished
**Status:** unvetted · **Adapted:** none · **Work:** topics/<topic>.md

The verdict in prose.
```

The explicit `{ #slug }` anchor matters: the slug is the source's identity everywhere — this entry,
the `sources/<slug>/` directory, and the `adapted/<topic>-<slug>.md` filename.

**Access:** `fetchable` / `local` / `private-host` / `unreadable`. An out-of-reach source is
reported as such, never reconstructed from memory.

**Licence:** decides where an adaptation may live — `adapted/` for CC-licensed sources (carrying
the same licence), `adapted-private/` for everything else. Unclear licence goes private; never
guess in the publishing direction.
"""

NOTES_INDEX = """# Notes

My own expository writing — the explanation I'd give if I had to teach the thing. A different kind
of object from the rest of the knowledge base:

| | Holds | Earned by |
| --- | --- | --- |
| `topics/` | the **record** of my trajectory | a session; `Status: solid` needs *How I could have come up with this* in my own words |
| `notes/` | **material I wrote** — exposition aimed at a reader | writing it |
| `adapted/` | **someone else's material**, rewritten motivation-first | a source going through `adapt-material` |

**A note is not evidence of understanding.** A clean exposition can be produced without deriving
anything. When a note's subject is worked through in a session, that produces a *topic file* which
links the note as material — never promote a note by bolting a `Status` field onto it.
"""

TOPIC_TEMPLATE = """# <Topic>

**Status:** open
**Opened:** YYYY-MM-DD  **Last touched:** YYYY-MM-DD

## The question that opened it

## Attached to

## How I could have come up with this

## Still loose

## Derived / proved myself
"""

PRACTICE_TEMPLATE = """# <Topic> — practice

## YYYY-MM-DD
**Problem:**
**Attempt:**
**Outcome:**
**What the mistake revealed:**
**Revisit:**
"""

ADAPTED_TEMPLATE = """# <Topic> — adapted from <source>

**Source:** <author, title, section; link; timestamps if a lecture>
**Catalogue:** <the source's entry, e.g. [ocw-6041sc](../resources/courses.md#ocw-6041sc)>
**Licence:** <the source's licence, and therefore this file's — see below>
**Adapted:** YYYY-MM-DD  **Depth:** full | delta | teaching
**Assumed known:** <cut as already held — listed so the cuts are visible>
**Prerequisites:** <what the source assumes beyond that>
**Anchors used:** <the existing knowledge this is built on>

## The problem this exists to solve

## What you already hold that this attaches to

## The route

<!-- Keep a pointer back to the source (§, page, timestamp) at each part. -->
<!-- Mark reconstructed motivation:  > **Supplied.** ... -->

## Where the source is artificial

## Proofs left to you

**Statement.**

<details><summary>Hint 1 — where to start</summary>

</details>

<details><summary>Hint 2 — the obstacle</summary>

</details>

<details><summary>Hint 3 — the technique, not applied</summary>

</details>

<details><summary>Hint 4 — the first move</summary>

</details>

## How you could have come up with this

<!-- Left blank on purpose. One prompt per central definition or result; I fill these in. -->

## What I cut, and why

---

<!-- Required for a CC-licensed source. Delete only if this file is in adapted-private/. -->
*Adapted from <author, title>, <course/publisher>, licensed <licence>. This adaptation is a
derivative work and is offered under the same licence.*
"""

README = """# Study knowledge base

Topics, practice, resources and learning trajectories. Maintained together with the
`study-mentor`, `adapt-material` and `adapt-recordings` skills.

- `index.md` — the front door
- `questions.md` — open questions; the index, and where each one lives
- `path.md` — the learning path: the one page written before the work rather than after it
- `profile.md` — durable background, anchors and study habits
- `log.md` — session log, newest first, next step at the top
- `resources/` — evaluated materials with verdicts, one file per subject
- `topics/` — one file per topic: the path through it, not a summary of it
- `practice/` — attempts and what the mistakes revealed
- `adapted/` — external material rewritten into the form I learn from
- `notes/` — my own exposition. Material, not evidence of understanding

The index is **questions**, not subjects. A new question goes in `questions.md` first, with no page
behind it; that is the normal resting state, not a gap to be filled.
"""


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__.strip())
        return 1

    root = Path(sys.argv[1]).expanduser().resolve()

    files = {
        root / "README.md": README,
        root / "index.md": INDEX,
        root / "profile.md": PROFILE,
        root / "log.md": LOG,
        root / "questions.md": QUESTIONS,
        root / "path.md": PATH,
        root / "resources" / "index.md": RESOURCES_INDEX,
        root / "notes" / "index.md": NOTES_INDEX,
        root / "topics" / "_template.md": TOPIC_TEMPLATE,
        root / "practice" / "_template.md": PRACTICE_TEMPLATE,
        root / "adapted" / "_template.md": ADAPTED_TEMPLATE,
    }

    created, skipped = [], []
    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            skipped.append(path)
            continue
        path.write_text(content, encoding="utf-8")
        created.append(path)

    for path in created:
        print(f"created  {path.relative_to(root)}")
    for path in skipped:
        print(f"skipped  {path.relative_to(root)} (exists)")

    print(f"\nKnowledge base ready at {root}")
    if created:
        print("Next: fill profile.md, then `git init && git add -A && git commit -m 'init kb'`")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
