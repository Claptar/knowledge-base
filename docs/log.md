# Study log

Newest first. The top of this file is what the next session reads.

This file holds **`Next` plus the current year**. Past roughly 400 lines, entries from finished
years move to `log/<year>.md` and this file keeps only `Next` and the year in progress — so it
stays skimmable however long the habit lasts, and `Next` never drifts below the fold. The archive
is created when the threshold is actually crossed, not in advance.

## Next
- **Shears first** ([topic](topics/shear.md)) — the most recent thread. Optional warm-up, a
  cold-check of what was given: with one linear function fixed, what is the composite of two shears
  along the same hyperplane, and where does it matter that both slides lie in that hyperplane? Then
  Problem 2(d): fix the slide and vary the linear function instead — how do these compose, and what
  plays the role the hyperplane played? Then the question left open in Cowork: without an inner
  product, what does a single coordinate of a vector actually depend on?
- **Then the size of a map** ([topic](topics/size-of-a-map.md), Road 3 §10). Using maps only, and
  only the wish — a non-constant polynomial size that respects composition — what is forced on a
  stretch, on a map that is not invertible, and on a map with a basis of eigenvectors? Which maps
  does that leave out (try a shear and the quarter-turn), and what would reaching them take? And:
  given two shears, is there an invertible map carrying one to the other by conjugation, and what
  would that say about the size of a shear?
- **The determinant from two row rules** ([topic](topics/where-the-determinant-comes-from.md)) —
  set twice, not yet tried. If all I know about a function of the rows is how it reacts to scaling
  one row and to adding a multiple of one row to another, plus its value on the identity, how much
  of it is already decided? This is where linearity in each row would stop being something I "can
  accept, but not defend out loud".
- **The destination of that thread**: for which $p$ is $\operatorname{diag}(p) - pp^\top$ singular,
  and what is its determinant? — the χ² question it came from ([questions](questions.md#live)).
- **Ambient RNA** ([topic](topics/ambient-rna.md)). First the cold-check still owed: from
  independent cell and soup counts, conditioned on the droplet total, rebuild the per-gene
  probabilities and the per-UMI source label without looking. Then Problem 2 steps 3–4 as posed in
  the topic's *Still loose*. Then CellSweep's bulk term, forward from the physics, with the paper's
  equation only at the end — and, before any model, how PCR chimeras form, in my own words.
- **Older threads, waiting**: redo cNMF equation-first, in the order listed in the NMF topic's
  [*Still loose*](topics/nmf.md#still-loose).
  [Path node 1](path.md#1-conditional-expectation-as-an-orthogonal-projection): can the tower
  property be had as a statement about nested projections, without computing an integral? Then
  [node 3](path.md#3-martingale), or [nodes 4](path.md#4-markov-property-in-continuous-time) and
  [5](path.md#5-jump-chain-and-holding-times) if Layer 1 stalls.

---

## 2026-11-23 — filed six weeks of sessions from their transcripts

Not a study session. The sessions from 2026-10-20 to 2026-11-14 ran on claude.ai and in Cowork
without repository access, and none of them reached `docs/`. Filed from their transcripts: the
entries below, three new topics with practice files —
[where the determinant comes from](topics/where-the-determinant-comes-from.md),
[the size of a map](topics/size-of-a-map.md), [shears](topics/shear.md) — and seven
[Live questions](questions.md#live). Dates inside a session come from the transcripts' headers and
the files' timestamps, not from per-turn dates. The 2026-10-20 ambient-RNA session is filed from
verbatim excerpts in an audit only; its transcript is not on disk. The statistics sessions on
DeGroot & Schervish chapters 9–10 — χ², the Kolmogorov–Smirnov test, rank tests, robust
estimation; undated, before 2026-10-23 — survive only as a project-memory summary, so they are
filed as two questions in its paraphrase and nothing else. Material Claude wrote in these
sessions — *Determinants from the question up*, *Four roads to the determinant*, the Road 3 note,
the shear recap, the explainer video — is not in the repository.

---

## 2026-11-03 to 14 — Shears: maps that fix a hyperplane

Mode: socratic; I asked for the plan to be kept out of view · Skill: not visible in the transcript
· Where: claude.ai, project *Statistics and Probability theory*
From the question the Road 3 dictation opened — what does adding a column "change"? —
[topics/shear.md](topics/shear.md), [practice/shear.md](practice/shear.md). Derived the general form
of a map that fixes a hyperplane, the case split by $\varphi(w)$, the shear's inverse, the
non-invertible case, and what the one number $s$ measures; my own recap page organised it.
Problem 2 half done, (d) not started. Then stopped: "I need to first get the whole idea of what is
going on before I approach the problems myself" — an explainer video was made.
Teaching — keep: direct corrections; working inside my own route in 1(b); restating a problem in
full when asked. · change: the plan was written together with its answers, so hiding it left no
map at all; a compressed claim ("Wat?"); a problem that pointed back at symbols from much earlier
("I don't remember what was the t1 and t2").

---

## 2026-11-03 — Shears, a first session in Cowork

Mode: socratic · Skill: not available in Cowork · Where: Cowork
The vectors a column operation fixes, and how the rest move, from my board —
[topics/shear.md](topics/shear.md). Stopped at the next question: without an inner product, what
does a coordinate depend on?
Teaching — keep: building the route before playing with the operator, as I asked. · change: the
first question came before any route.

---

## 2026-11-01 to 03 — Road 3 rethought for maps

Mode: my own notes, organised · Skill: not visible in the transcript · Where: claude.ai, project
*Statistics and Probability theory*
Rewrote Road 3 — the determinant as the size of a map — by hand, for maps rather than matrices:
[topics/size-of-a-map.md](topics/size-of-a-map.md), [practice](practice/size-of-a-map.md). The
question and its three sub-questions were mine; derived what multiplicativity gives for free;
dictated the reason to ask (a scale factor, a derivative, a density, a volume free of the basis).
Opened the [shear](topics/shear.md) question. Didn't: 4.1 for maps and the volume line came whole;
the §10 problem is untouched. The dictation is dated by the notes made from it, 2026-11-03.
Teaching — keep: organising my notes in my structure, with my questions kept as questions.
· change: maps and matrices mixed until I asked for hats.

---

## 2026-10-23 to 26 — From the Levi-Civita symbol to the determinant: Steps 1–2, and four roads

Mode: socratic, then direct corrections at my request · Skill: not visible; the project memory was
rewritten during the session · Where: claude.ai, project *Statistics and Probability theory*
Resumed from my 3D Levi-Civita work:
[topics/where-the-determinant-comes-from.md](topics/where-the-determinant-comes-from.md),
[practice](practice/where-the-determinant-comes-from.md). Derived: dependent rows give zero, the
$n$-dimensional uniqueness page, the sign's parity from the inversion count, the existence pairing,
all of Step 2. Given: the converse, and on my request the ladder of motivation and four routes to
the determinant. Ended on the determinant as the size of a map, which became its own question.
Step 3, the χ² destination, not reached. The last date is the Road 3 note's 26 October version.
Teaching — keep: after the retrospective, one well-posed problem per turn with its goal — Step 2
went through whole. · change: "It's been almost a full day and we are still at step 1." — chains of
small leading questions with their purpose hidden; corrections by counter-question ("you are here
just picking on my words"); properties motivated by later results ("you can't just ask
EVERYTHING"); a route that guessed the determinant and checked it.

---

## 2026-10-20 — Ambient RNA: CellSweep's bulk term, PCR chimeras, the UMI majority vote

Mode: socratic, resumed from my uploaded notes · Skill: no sign it was loaded · Where: claude.ai,
project *Biophysics*
Filed on 2026-11-23 from verbatim excerpts only; the transcript is not on disk —
[topic](topics/ambient-rna.md), [practice](practice/ambient-rna.md). Opened on CellSweep's equation
as a premise, which I objected to. How chimeras form, and the majority-vote flip, were given on
request; a cycle-$k$ copy's share of the family was mine. Ended: "Okay, it seems like I got tired
at this point."
Teaching — keep: conceding the right part of my pushback on the cell count, with the precise
relation; the answer given at once when I asked. · change: a paper's equation as the opening
premise; a model asked for before I had the mechanism; three-part questions in consecutive turns.

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
