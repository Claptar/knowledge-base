#!/usr/bin/env python3
"""Create the study knowledge base skeleton.

Usage:
    python init_kb.py <path>

Creates directories and seed files. Never overwrites an existing file — safe to re-run on a
partially built knowledge base.
"""

import sys
from datetime import date
from pathlib import Path

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

**Access:** `fetchable` / `local` / `private-host` / `unreadable`. An out-of-reach source is
reported as such, never reconstructed from memory.

**Licence:** decides where an adaptation may live — `adapted/` for CC-licensed sources (carrying
the same licence), `adapted-private/` for everything else.
"""

TOPIC_TEMPLATE = """# <Topic>

**Status:** open
**Opened:** {today}  **Last touched:** {today}

## The question that opened it

## Attached to

## How I could have come up with this

## Still loose

## Derived / proved myself
"""

PRACTICE_TEMPLATE = """# <Topic> — practice

## {today}
**Problem:**
**Attempt:**
**Outcome:**
**What the mistake revealed:**
**Revisit:**
"""

ADAPTED_TEMPLATE = """# <Topic> — adapted from <source>

**Source:** <author, title, section; link; timestamps if a lecture>
**Adapted:** {today}  **Depth:** full | delta | teaching
**Assumed known:** <cut as already held — listed so the cuts are visible>
**Prerequisites:** <what the source assumes beyond that>
**Anchors used:** <the existing knowledge this is built on>

## The problem this exists to solve

## What you already hold that this attaches to

## The route

## Where the source is artificial

## Proofs left to you

**Statement.**

<details><summary>Hint 1 — where to start</summary>

</details>

## How you could have come up with this

## What I cut, and why
"""

README = """# Study knowledge base

Topics, practice, resources and learning trajectories. Maintained together with the
`study-mentor` and `adapt-material` skills.

- `profile.md` — durable background and study habits
- `log.md` — session log, newest first, next step at the top
- `resources.md` — evaluated materials with verdicts
- `topics/` — one file per topic: the path through it, not a summary of it
- `practice/` — attempts and what the mistakes revealed
- `adapted/` — external material rewritten into the form I learn from
"""


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__.strip())
        return 1

    root = Path(sys.argv[1]).expanduser().resolve()
    today = date.today().isoformat()

    files = {
        root / "README.md": README,
        root / "profile.md": PROFILE,
        root / "log.md": LOG,
        root / "questions.md": QUESTIONS,
        root / "resources" / "index.md": RESOURCES_INDEX,
        root / "topics" / "_template.md": TOPIC_TEMPLATE.format(today=today),
        root / "practice" / "_template.md": PRACTICE_TEMPLATE.format(today=today),
        root / "adapted" / "_template.md": ADAPTED_TEMPLATE.format(today=today),
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
