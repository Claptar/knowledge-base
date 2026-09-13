# Knowledge base structure

A git repository of plain markdown, readable on its own and renderable by a static site generator.
Every file should make sense to a human reading it directly — it is his notes, not a machine log.

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
    resources.md            # evaluated materials with verdicts
    topics/<topic>.md       # one per topic: the trajectory through it
    practice/<topic>.md     # attempts, mistakes, what each mistake revealed
    adapted/<topic>-<src>.md  # external material rewritten into the form he learns from
  skills/                   # these skills. Not published.
  sources/                  # downloaded source material. Gitignored, never published.
  mkdocs.yml                # site config
```

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
**Source.** A link into resources.md, never a verdict restated here.

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
Existing knowledge this connects to, and how. Be specific about the connection — "related to
linear algebra" is worthless; "the covariance operator is the Gram matrix of centred features,
so the spectral story is the same one as in PCA" is the actual content.

## How I could have come up with this
His own answer, in his own words, for each central definition or result. Absent here means
not yet understood, regardless of how well the derivation went.

## Still loose
Open threads with enough context to resume cold — what he tried, where it broke down.

## Derived / proved myself
Short list of what he worked out rather than read, with dates. This is the record of what he
owns rather than recognizes.
```

`Status: solid` is earned by the "how I could have come up with this" section being filled in,
not by having covered the material.

## practice/<topic>.md

```markdown
# <Topic> — practice

## YYYY-MM-DD
**Problem:** statement or a pointer to it
**Attempt:** what he tried
**Outcome:** solved / solved unconvincingly / stuck
**What the mistake revealed:** the underlying gap — a definition held only formally, a false
analogy from a neighbouring topic, a missing intuition. This field is the reason the file exists.
**Revisit:** when and what to try again
```

Record near-misses too: right answer by an unconvincing route is a gap, not a success.

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

## resources.md

Grouped by topic. Each entry gets a verdict, including what's wrong with it — that judgement is
the expensive part and the reason not to re-search the same ground later.

```markdown
## <Topic>
- **<Author, Title>** (book/notes/paper/course) — what it's good for; what's weak about it;
  whether it motivates or just states. Link.
```

## Update rules

- Update at natural stopping points and at the end of a session, not continuously — interrupting
  a derivation to write notes breaks the thing the session is for.
- Preserve his phrasing for insights. The value is in how *he* formulated it.
- Never mark a topic solid to tidy the record. An honest open thread is worth more than a clean
  status field.
- In chat mode with no filesystem access, produce complete updated files plus the commit
  commands. Don't hand over fragments he has to splice in by hand.
