# Study log

Newest first. The top of this file is what the next session reads.

This file holds **`Next` plus the current year**. Past roughly 400 lines, entries from finished
years move to `log/<year>.md` and this file keeps only `Next` and the year in progress — so it
stays skimmable however long the habit lasts, and `Next` never drifts below the fold. The archive
is created when the threshold is actually crossed, not in advance.

## Next
- **cNMF, the consensus step** ([topic](topics/nmf.md)) — what does a median over many NMF local
  optima estimate? First move: sort run-to-run differences into those consensus can remove
  (different local optima) and those it cannot (a pin the data lacks). Optional ten-minute warm-up
  before reading anything: rebuild the identifiability theorem's three steps from a blank page.
- [Path node 1](path.md#1-conditional-expectation-as-an-orthogonal-projection) — conditional
  expectation as orthogonal projection. Specific first move: derive the tower property as a
  statement about nested projections in $L^2$, without computing an integral. If that works, the
  PCA anchor is real and Layer 1 is cheap; if it does not, the anchor is wrong and the path needs
  rewriting before node 3.
- Then [node 3, martingales](path.md#3-martingale): what problem forces the definition, before
  touching optional stopping.
- Parallel branch, if Layer 1 stalls: [node 4](path.md#4-markov-property-in-continuous-time) then
  [node 5](path.md#5-jump-chain-and-holding-times) — why the holding time must be exponential.
  Node 4 needs only node 1, and this branch is what unlocks Layer 3.

---

## 2026-10-06 — NMF: identifiability and the loss as a noise model

Mode: socratic
A detour from `Next`, reading Kotliar et al. 2019 (cNMF). Derived the separable identifiability
theorem except its lemma, and read the NMF losses as noise models — [topics/nmf.md](topics/nmf.md),
with [practice/nmf.md](practice/nmf.md) and [a note](notes/matrix-factorisation/nmf-identifiability-and-loss.md).
Clicked: the cone picture, and the outside pin by transposing. Didn't: the first half had no stake
and no route, so "why do we even care about S?" came late — a session failure, not a gap.

---

## 2026-09-13 — cleared out what was seeded rather than harvested
Not a study session. Deleted `topics/mathematical-modelling.md`: it was seeded from an external
reading guide and was mostly a restatement of it, which is the one thing a topic file is not for.
The one line in it that was mine — convex optimisation held as theory, formulation missing — moved
to [profile.md](profile.md#anchors-worth-building-on), and its two questions stay live with no page.

Moved the martingale and generator questions out of the [Live table](questions.md#live): neither
had been started, and both were the path's phrasing rather than mine. They remain as
[nodes 3](path.md#3-martingale) and [6](path.md#6-generator-and-semigroup). Live is now two
questions and `topics/` is empty — which is the honest state before any session has happened.

---

## 2026-09-13 — learning path laid down
Not a study session. Added [path.md](path.md): an 18-node concept dependency map from conditional
expectation to the Pachter-lab transcription models, with the measurement layer as the part that
is mine. Sources for the terminal nodes added to
[resources/cme-transcription.md](resources/cme-transcription.md), all unvetted.
Nothing here is studied — the path is a plan, and the first thing it should do is turn out to be
wrong somewhere.

---
