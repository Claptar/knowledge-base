---
name: adapt-material
description: Rewrites public lecture materials, course notes, book chapters and paper sections into the form this user actually learns from — the problem before the definition, his own knowledge as the starting point, proofs left for him to do. Use when he supplies or points at a source and wants it reshaped rather than explained live: "adapt this chapter", "rewrite these lecture notes for me", "here are the slides / the transcript / the PDF", "make this into something I can work through", "turn this into notes I could teach from", "give me a route through this book". Produces a document filed in the study knowledge base, not a conversation. Use the study-mentor skill instead when he wants to be taught interactively.
---

# Adapt Material

## What this is for

He reads a lot of material that is good but written for someone else. A lecture course assumes a
cohort he isn't in; a textbook chapter spends twenty pages on linear algebra he holds cold and
four lines on the one move that actually matters; a paper's supplement contains the derivation but
states it in the order that was convenient to write. The content is worth having. The shape is
wrong.

This skill takes such a source and rewrites it into the form he learns from. The output is a
**document**, filed in the knowledge base — something he can work through offline, return to, and
adapt into teaching material of his own.

The governing criterion is the same one as everywhere else in this repo: after reading the
adaptation, he should be able to answer **"how could I have come up with this?"** for every
central definition and result. A rewrite that is clearer, better organised and still leaves that
unanswerable has failed.

**What this is not.** Not a summary, not a simplification, not a study guide. The adaptation is
usually *longer* than the source, because the motivation the source omitted has to go somewhere.
If your output is shorter and smoother than the input, you have almost certainly done the wrong
thing.

## Step 1 — get the source, whole

Do not start rewriting from a partial read. Whatever the form:

- **A file he supplies** — PDF chapter, slide deck, scanned notes, markdown. Read all of it,
  including the exercises; they often reveal what the author thought the point was.
- **A URL** — course page, lecture notes, arXiv paper, blog series. Fetch it. Follow the one or
  two links that carry the actual content (the notes behind a course index, the supplement behind
  a paper).
- **A lecture video** — work from the transcript plus the slides if both exist. Note timestamps
  for the parts you keep, so he can go back to the moment rather than the hour.
- **A book chapter he names but doesn't have** — say plainly that you're working from the
  literature about it rather than the text, and offer to adapt properly once he supplies it.
  Reconstructing a chapter from memory and presenting it as adapted is the worst failure mode
  available here.

If the source is long, ask which part he wants adapted before spending the session on chapter one.

## Step 2 — load the reader

Read `profile.md` at the knowledge base root — that is the current state of what he knows and how
he wants to be taught. Then read, in the neighbouring skill:

- `../study-mentor/references/background.md` — durable background and the anchors
  worth building on, if `profile.md` is thin.
- `../study-mentor/references/taste.md` — what counts as good exposition to him.
  Read this one every time; it is the difference between a rewrite that lands and one that is
  merely tidy.

Also read the `topics/` file for this subject if it exists. If he has already been through
neighbouring material, the adaptation should attach to what is recorded there rather than
re-establishing it.

## Step 3 — choose the depth

Ask which he wants. One line, not a menu:

- **Full rewrite** (the default) — the source restructured motivation-first, everything he holds
  cold cut, proofs converted to exercises.
- **Delta only** — he already knows most of this; give him what is genuinely new or non-obvious in
  this treatment, and say what the rest of it is so he can skip with confidence.
- **Teaching draft** — shaped for him to deliver: the route, the worked motivation, the questions
  to put to an audience, the places where a class will predictably get stuck.

## Step 4 — diagnose before rewriting

Work this out explicitly before writing a line of the adaptation. It is most of the value.

1. **Find the spine.** What is this chapter actually for — the one question it answers? Most
   sources bury it. Everything in the adaptation gets ordered by its distance from that question.
2. **Mark what he holds cold.** Spectral theory, quadratic forms, tensor constructions, PCA and
   L² geometry, convex duality, the HMM forward-backward machinery. These get cut to a pointer,
   not explained. Cutting them is what buys the room for the rest.
3. **Mark the genuine prerequisites he may lack.** Different from the above and easy to confuse.
   Name them at the top rather than silently assuming them.
4. **Locate the unmotivated joints.** The definitions that arrive from nowhere; the conditions in
   a theorem that exist only to make the proof go through; the trick in step three. These are the
   points the adaptation exists to fix. List them before you start.
5. **Find the anchors.** For each central object, the nearest thing he already believes. The
   anchor list in `profile.md` is the starting point, not the limit — a good anchor found fresh is
   worth more than a stock one applied loosely.
6. **Judge the source.** What is it strong at, what is it weak at, is it worth his time at all. If
   a better treatment of the same material exists, say so up front — adapting a mediocre source
   well is a waste when a good one is available.

## Step 5 — write the adaptation

### Required shape

```markdown
# <Topic> — adapted from <source>

**Source:** <author, title, section; link; timestamps if a lecture>
**Adapted:** YYYY-MM-DD  **Depth:** full | delta | teaching
**Assumed known:** what was cut as already held — listed so the cuts are visible
**Prerequisites:** what the source assumes that isn't in the list above
**Anchors used:** the existing knowledge this is built on

## The problem this exists to solve
The question that makes the whole chapter necessary, put so he can feel its force before any
machinery appears. If the source never states it, reconstruct it and mark it as supplied.

## What you already hold that this attaches to
The anchors, made explicit and specific. Not "related to linear algebra" — the actual connection.

## The route
The content, reordered so each object arrives as the answer to a question already standing.
Keep a pointer back to the source (§, page, timestamp) at each part, so he can check the original.

## Where the source is artificial
The unmotivated joints from the diagnosis, named, with what the natural route would have been —
historically or conceptually. He trusts this more than a smooth presentation, and the real
intuition is usually here.

## Proofs left to you
Statements only, with escalating hints behind <details>. Never the finished proof.

## How you could have come up with this
Left blank, for him. One prompt per central definition or result.

## What I cut, and why
Every omission, one line each, so nothing disappears silently.
```

### Rules that are not negotiable

**Never hand over a proof.** Every proof in the source becomes a statement plus a hint ladder, in
the escalation the study-mentor skill uses — anchor, then obstacle, then technique named but not
applied, then first move only. Put each rung behind its own `<details>` block so he chooses when
to open it:

```markdown
<details><summary>Hint 1 — where to start</summary>
What does this remind you of from the L² picture?
</details>
```

The full derivation goes in a final `<details>` marked as such, or is left out entirely when the
source's own proof is available at the pointer you gave.

**Mark provenance.** Motivation you supplied rather than found in the source is marked:

```markdown
> **Supplied.** The source states the definition flat. This is my reconstruction of what forces it.
```

He needs to know which parts are the author's reasoning and which are yours, because the two carry
different authority and he will want to check the second.

**Cut for redundancy, never for difficulty.** The only licence to remove something is that he
already holds it. Removing a hard argument because it is hard destroys the document's reason to
exist.

**Don't smooth over trouble.** If the source is unclear, or you think it is wrong, or a step
genuinely doesn't follow — say so in place. A flagged gap is useful; a plausible bridge you
invented is a trap, and he will hit it later at the worst moment.

**Preserve the source's notation** unless it fights his conventions. If you change it, put the
translation in one small table near the top rather than leaving him to infer it mid-derivation.

**Write for a working researcher.** No on-ramps, no "intuitively speaking", no recap of what a
random variable is. Maths in LaTeX, `$…$` and `$$…$$`, so it renders on his Jekyll site.

## Step 6 — file it

- Save as `adapted/<topic>-<source-slug>.md` — for example
  `adapted/martingales-williams-ch10.md`. Start from `adapted/_template.md`.
- Add the source to `resources/` with the verdict from step 4.6. The judgement is the expensive
  part; it is why that file exists.
- If the topic has a `topics/` file, link the adaptation from it. If it doesn't and this opens a
  real topic, create one — the adaptation is material, the topic file is his trajectory through
  it, and they are not the same record.
- If working through it should be the next thing, put that at the top of `log.md` as a concrete
  step: which sections, which proofs to attempt.

Show him a summary of what changed rather than the whole document twice, and let him commit.

## Reference files

Shared with the `study-mentor` skill, which is the authority on how he is taught:

- `../study-mentor/references/taste.md` — what "excellent" means to him. Read before
  every adaptation.
- `../study-mentor/references/background.md` — durable background and anchors.
- `../study-mentor/references/kb-structure.md` — where the output goes and why.
