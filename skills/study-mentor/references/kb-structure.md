# Knowledge base structure

A git repository of plain markdown, readable on its own and renderable by a static site generator.
Every file should make sense to a human reading it directly — it is his notes, not a machine log.

## Before creating anything here

**This is a route through ideas, indexed by question — not a library, a reference or a course.**
Completeness is not a goal; it is the failure mode. A knowledge base 40% complete and densely
cross-linked is worth more than one 95% complete and flat, because the missing 55% is in the
textbooks and the connections are nowhere else.

Four questions, and they apply to a refactor or a convention as much as to a page:

1. **Whose is it?** Someone else's text is not a knowledge base entry. Cite it, or adapt it.
2. **Which live question does it serve?** Name it. "For completeness" is not an answer.
3. **Does it make something easier to find, or just add something to find?**
4. **Would a human reading it in six months be better off?**

If a proposal fails these, say so rather than building it. The failure mode of a knowledge base is
silent: a bad structure still renders, and only stops paying six months later when nothing can be
found in it. The four recurring pulls to resist are **accumulate**, **restate**, **seed** and
**systematise** — each is expanded, with examples, in the repository's `AGENTS.md`.

The knowledge base root is `docs/` — everything below is relative to it, and it is what the
published site is built from. Paths named bare elsewhere in these skills (`profile.md`, `topics/`)
mean relative to this root, not to the repository root.

```
study-kb/
  docs/                     # <- the knowledge base root, and the site
    index.md                # the site front door
    questions.md            # open questions — the index, and where each one lives
    path.md                 # the learning path — the one page written before the work
    profile.md              # background, notation habits, what he knows cold
    log.md                  # dated sessions, newest first, next step at the top
    resources/              # evaluated materials, one file per subject
    topics/<topic>.md       # one per topic: the trajectory through it
    practice/<topic>.md     # attempts, mistakes, what each mistake revealed
    adapted/<topic>-<src>.md  # external material rewritten into the form he learns from
    notes/<subject>/        # his own exposition. Material, not record.
  skills/                   # these skills. Not published.
  adapted-private/          # adaptations of all-rights-reserved sources. Gitignored.
  mkdocs.yml                # site config
```

`sources/<slug>/` — the downloaded material itself — is **not here**. It lives in the
[library repository](https://github.com/Claptar/knowledge-base-library) with its converted
markdown and the two skills that fetch and convert it. A `sources/<slug>` path in a catalogue
entry resolves there; the slug is the same in both repositories.

**A new question goes in `questions.md` first, with no page behind it.** That is the normal resting
state of a question. A topic file is written after a session, not before one.

Topic slugs are lowercase and hyphenated: `martingales.md`, `chemical-master-equation.md`,
`spectral-clustering.md`. Practice files mirror topic slugs so the pair is obvious.

## profile.md

Seeded from `references/background.md`, then maintained. Holds what is durable: mathematical
background, working context, notation preferences, recurring anchors, and study habits learned
over time. Update when something *changes*, not every session.

## path.md

The one page written *before* the work: a concept dependency map from what he already holds to a
named destination. It answers "what should I study next" without pretending anything has been
studied.

```markdown
# Learning path

**Destination:** what he will be able to do, not what he will have covered.
**Designed:** YYYY-MM-DD

> **Provenance.** Designed, not harvested. Nothing here is evidence of understanding.

## Layer N — <what this layer is for>

### <n>. <Concept>

**Needs** <node numbers>.  **[live]** — if it is already in questions.md

The question that would force this concept, in two or three lines.

**Anchor.** The specific existing thing it attaches to — same standard as a topic file.
**Source.** A link into `resources/`, never a verdict restated here.

Optional, only where there is something real to say:
**Trap to watch.** A false analogy the node invites.
**Conjecture to test.** What the node should turn out to show — phrased so it can fail.
**Connects to.** A topic file this node bears on.
**Decision point.** What to do if the node comes out empty, including deleting a layer.

## What this path deliberately leaves out

Named, so the absence is a decision rather than an oversight.
```

Rules, because this page inverts the repo's usual one:

- **No `Status` field, no markers, nothing that reads as evidence.** Planned is not held.
- **A node is not a page.** Completing one does not create `topics/<node>.md`; a session does, and
  most nodes never get a file.
- **Its questions are proposed, not asked.** They stay out of the `questions.md` Live table until
  he holds one without re-reading the node. The reverse move — an already-live question acquiring
  a path node — is the normal direction.
- **One path page only.** A second plan is a layer in this one, or nowhere.
- **Delete nodes that turn out to be wrong**, and say so in `log.md`. That is the page working.

## topics/<topic>.md

The heart of the knowledge base. Records the path through a topic, not a summary of it.

```markdown
# <Topic>

**Status:** open | resting | solid
**Opened:** YYYY-MM-DD  **Last touched:** YYYY-MM-DD

## The question that opened it
What problem made this topic necessary. Ideally a question he can still feel the force of.

## Attached to
Inbound: existing knowledge this built on, and how. Be specific about the connection — "related
to linear algebra" is worthless; "the covariance operator is the Gram matrix of centred features,
so the spectral story is the same one as in PCA" is the actual content.

## Where else this shows up
Outbound, and deliberately across domains — physics, optimisation, machine learning, biology,
engineering. Added whenever a connection is noticed, never filled in at creation.

## How I could have come up with this
His own answer, in his own words, for each central definition or result. Absent here means
not yet understood, regardless of how well the derivation went.

## Still loose
Open threads with enough context to resume cold — what he tried, where it broke down.

## Derived / proved myself
What he worked out rather than read, with dates, each marked `**Derived unaided.**`. This is the
record of what he owns rather than recognizes, and the evidence goal 4 runs on.
```

`Status: solid` is earned by the "how I could have come up with this" section being filled in,
not by having covered the material.

**Both connection sections matter, and the outbound one is the half usually skipped.** His own
example: a derivative tied only to limits and the surrounding analysis is not yet understood;
tied to physics, optimisation and machine learning, it is. Connections inside a subject are the
cheap ones.

## practice/<topic>.md

**An attempt log, not a mistake log.** It records what he *could* do as carefully as what he could
not. The blocker for goal 4 is fear rather than competence, and a file that accumulates only errors
works against that goal — so the unaided fields are not decoration, they are the point.

```markdown
# <Topic> — practice

## YYYY-MM-DD
**Problem:** statement or a pointer to it
**Worked unaided up to:** how far he got with no help. Be precise and generous — "unaided as far
as setting up the exchange step" is a real result and belongs on the record
**Where I asked for a hint:** which rung of the ladder, and what unstuck him
**Attempt:** what he tried
**Outcome:** solved / solved unconvincingly / stuck
**What it revealed:** the underlying gap — a definition held only formally, a false analogy from a
neighbouring topic, a missing intuition — *or* the capability, when the thing revealed is that he
could do it
**Revisit:** when and what to try again
```

Mark an unaided result `**Derived unaided.**` so it is greppable and counts.

Record near-misses too: right answer by an unconvincing route is a gap, not a success. That rule
survives unchanged — honesty about a shaky route is not in tension with recording capability, and
inflating either field destroys the value of both.

## adapted/<topic>-<source>.md

External material — a book chapter, lecture notes, slides, a paper — rewritten motivation-first
with what he holds cold cut out and the proofs converted to exercises. Produced by the
`adapt-material` skill, which carries the full shape and the rules; `adapted/_template.md` is the
working copy.

These are **material**, not record. A topic file is his trajectory through a subject and stays the
source of truth for what he understands; an adapted document is a text he now owns a better
version of. Keep them separate even when they cover the same ground, and link the adaptation from
the topic file rather than folding one into the other.

Source slugs identify the text, not just the author: `martingales-williams-ch10.md`,
`cme-gorin-pachter-2023.md`.

## notes/<subject>/

His own expository writing — the explanation he would give if he had to teach the thing.

Three kinds of object, kept distinct:

| | Holds | Earned by |
| --- | --- | --- |
| `topics/` | the **record** of his trajectory | a session; `Status: solid` needs *How I could have come up with this* in his words |
| `notes/` | **material he wrote** — exposition aimed at a reader | writing it |
| `adapted/` | **someone else's material**, rewritten motivation-first | a source going through `adapt-material` |

**A note is not evidence of understanding.** A clean exposition can be produced without having
derived anything, and several of these were written with an AI assistant — each carries a
provenance banner saying so. When a note's subject is worked through in a session, the session
produces a *topic file* that links the note as material. Never promote a note by bolting a
`Status` field onto it.

## log.md

Newest first. The top of the file is what the next session reads.

```markdown
## Next
One or two concrete next steps, specific enough to start cold.

---

## YYYY-MM-DD — <topic>
Mode: socratic | motivate-then-prove | guided
What was covered, what clicked, what didn't. Two to five lines. Link to the topic file rather
than duplicating its content.
```

**It holds `Next` plus the current year.** A session log is the one file here that grows without
bound — an entry per session, forever — so past roughly 400 lines, entries from finished years move
to `log/<year>.md` and `log.md` keeps only `Next` and the year in progress. Create the archive when
the threshold is crossed, not in advance, and add the new file to the site nav.

`log.md` stays the entry point either way: **always read the top of `log.md`, never an archive
file**, which is history rather than state. Do not split the log per session — entries are two to
five lines, and a directory of hundreds of them destroys the one thing the log is for, which is
skimming recent history in a single pass.

## resources/

A directory, one file per subject, indexed by `resources/index.md`. Each entry gets a verdict —
including what is wrong with the source — because that judgement is the expensive part and the
reason not to re-search the same ground later.

```markdown
### <slug> — <Author, Title> { #<slug> }

**Kind:** book · **Access:** local · `sources/<slug>/book.pdf`
**Licence:** all rights reserved — adaptation stays unpublished
**Status:** unvetted · **Adapted:** none · **Work:** topics/<topic>.md, practice/<topic>.md

The verdict in prose: what it is good for, what is weak, whether it motivates or merely states.
```

The explicit `{ #slug }` anchor matters: the slug is the source's identity everywhere — the
catalogue entry, the `sources/<slug>/` directory, and the `adapted/<topic>-<slug>.md` filename —
so it must be linkable directly rather than through a generated heading slug.

Three fields carry the weight:

- **`Access`** — `fetchable` / `local` / `private-host` / `unreadable`. It answers whether an agent
  can actually open the source. An out-of-reach source is to be reported as such, **never**
  reconstructed from memory.
- **`Licence`** — decides where an adaptation may live. CC-licensed sources adapt into
  `adapted/` and carry the same licence; all-rights-reserved ones adapt into `adapted-private/`,
  which is gitignored. Unclear licence goes private.
- **`Work`** — points at `topics/` and `practice/` files. His own notes and worked sessions on a
  source are **record**, so they live in the knowledge base and are committed; they never go in
  `sources/`, which is gitignored and would lose them. Practice is organised by *topic*, not by
  book, because understanding is topic-shaped.

`sources/<slug>/` holds the material itself, normalised at ingest to one layout regardless of
publisher, with a `_manifest.csv` mapping back to the original filenames. The full convention is in
`resources/index.md`; the scripts are in the library repo's `skills/collect-materials/scripts/`.

## Update rules

- Update at natural stopping points and at the end of a session, not continuously — interrupting
  a derivation to write notes breaks the thing the session is for.
- Preserve his phrasing for insights. The value is in how *he* formulated it.
- Never mark a topic solid to tidy the record. An honest open thread is worth more than a clean
  status field.
- In chat mode with no filesystem access, produce complete updated files plus the commit
  commands. Don't hand over fragments he has to splice in by hand.
