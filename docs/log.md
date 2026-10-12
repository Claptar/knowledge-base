# Study log

Newest first. The top of this file is what the next session reads.

This file holds **`Next` plus the current year**. Past roughly 400 lines, entries from finished
years move to `log/<year>.md` and this file keeps only `Next` and the year in progress — so it
stays skimmable however long the habit lasts, and `Next` never drifts below the fold. The archive
is created when the threshold is actually crossed, not in advance.

## Next
- **Ambient RNA, Problem 2 step 3** ([topic](topics/ambient-rna.md),
  [note §2](notes/measurement/ambient-rna.md#2-soupxs-contamination-estimator)). First the cold-check
  owed: reproduce $p_g = (1-\alpha)\mu_g + \alpha a_g$ and the per-UMI label argument without
  looking — both were given, not derived. Then read the bias already computed,
  $\mathbb E[\hat\alpha_c] = \alpha_c + (1-\alpha_c)\varepsilon_G/a_G$: write the *relative*
  bias, say which two quantities it compares, and decide what makes a good or a bad gene set $G$ for
  a cell type, in biological terms. Then step 4 (what the ratio of sums estimates if
  $\alpha_i \approx \Lambda/T_i$), then Problems 3–5 in the topic file.
- **Redo cNMF equation-first** ([note](notes/matrix-factorisation/cnmf-consensus.md),
  [topic](topics/nmf.md)) — the 2026-10-07 session covered it in prose without equations, so
  nothing past stop 1's first answer is mine yet. In order, before opening any folded proof: the
  $2 \times 2$ table of $S$; the monomial lemma, $2 \times 2$ first; Proposition B;
  $E(K+1) \le E(K)$ and the continuum at $K = K^* + 1$; the usage refit's uniqueness and what
  $H^{\mathrm{TPM}}_{kj}$ means. Then close the loop: how could I have come up with cNMF?
- Optional, hands-on: experiment A of the cNMF note (simulator, runs A1–A3), predictions written
  into [practice](practice/nmf.md) before running.
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

## 2026-10-10 — Ambient RNA: the likelihood from the physics, and SoupX's estimator

Mode: socratic
New topic — [topics/ambient-rna.md](topics/ambient-rna.md),
[practice/ambient-rna.md](practice/ambient-rna.md), [a note](notes/measurement/ambient-rna.md).
Derived the droplet likelihood: landing as a binomial, capture as thinning by two routes, a shared
droplet factor as the source of the mixed Poisson, conditioning on $T$ to the multinomial; then
SoupX's estimator as far as its bias. Clicked: "It's just an event"; my question "why is μ a
fraction and not a physical quantity?" carried the session. Didn't: the mixture decomposition
(given on request); Le Cam and PGFs had to be supplied by name. Ran on claude.ai with a stale
installed skill missing its `references/`; filed here on 2026-10-12.

---

## 2026-10-07 — cNMF: consensus, K and refits

Mode: socratic, then motivate-then-prove for pace
From `Next`: the consensus step, the choice of $K$, the refits — [topics/nmf.md](topics/nmf.md),
[practice/nmf.md](practice/nmf.md), [a note](notes/matrix-factorisation/cnmf-consensus.md). Derived:
runs at different local optima are not related by any $S$, so compare likelihoods; the rest was
given. Corrected the NMF note's §5 and §8 (iii). Didn't: the form — maths in words, almost no
equations, too much per message. A session failure, not a gap; it ran on a stale installed skill.

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
