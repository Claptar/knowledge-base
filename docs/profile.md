# Profile

Background, habits and anchors. Updated when something changes, not every session.

## Mathematical background

- Linear algebra held deeply, in the Russian tradition (Kostrikin, Gelfand): bilinear and
  quadratic forms, spectral theory, tensor constructions.
- Wrote my own Russian-language lecture notes on tensor analysis (Markdown/LaTeX).
- PCA worked through from the foundations — covariance as a Gram matrix, L² geometry,
  eigendecomposition.
- Probability and statistics: Murphy's probabilistic ML series; ISL vs ESL compared;
  HMMs via Rabiner and Durbin et al.
- Convex optimization via Boyd & Vandenberghe (EE364A).
- Algorithms practice on the side, so complexity arguments are available as anchors.
- Read Russian fluently — Russian textbooks are in play when they are the better text.

## Working context

- Bioinformatician at the Wellcome Sanger Institute, Cambridge.
- Nextflow pipeline reprocessing public 10x Genomics data at scale: chemistry inference, QC,
  validation, sample assembly.
- Single-cell genomics across modalities — scRNA-seq, scATAC-seq, multiome, Xenium, Visium.
- Production Python, containerization, pipeline engineering.
- Building educational content in maths and bioinformatics — explanations that work are ones
  I could adapt and teach.

## Notation and conventions

_To fill in as they come up: index conventions, measure-theoretic vs elementary phrasing,
where I want rigour and where I don't._

## Anchors worth building on

- **Inner products, projections, spectra, low-rank structure** -> PCA as Gram-matrix / L^2 geometry.
- **Structure carried along a map or a flow** -> tensor analysis notes.
- **Latent variable models, filtering, inference over sequences** -> HMMs (Rabiner, Durbin).
- **Birth-death and jump processes** -> chemical master equation, stochastic transcription
  (Gorin & Pachter).
- **Sampling artifacts, noise models, count data** -> 10x chemistry and daily QC work.

**The gap next to the last two:** convex optimisation theory is held (EE364A), but *formulation* is
not — how a real problem becomes $\min_x c^T x$ subject to $Ax \le b$ in the first place. Named
here because it is a recurring one, not specific to any topic.

## Current directions

- Stochastic processes, aimed at the Pachter lab biophysics curriculum.
- Statistics and probability theory proper, not only the ML-facing slices.

## How I study

**This section is the point of the whole repository.** Everything else here — the topic files, the
practice log, the adapted material, the skills — exists to serve it, and a change that does not
serve it does not belong.

### The criterion

There is a saying: *if I can't build it then I don't understand it.* Mine is a version of that:

> I can say that I understand something only when I can answer the question **how could I come up
> with this solution / problem / question / approach on my own?**

That is only possible once the concept has a place in my world-picture rather than sitting beside
it. So understanding is not recall and it is not being able to follow a proof — it is having
**fitted a new perspective into my existing world perspective**, which means connecting it to what
I already hold.

**Connections inside the subject are not enough.** Derivatives are naturally tied to limits and to
the rest of the analysis you meet on the way, but to really appreciate a derivative you have to
connect it to physics, to optimisation methods, to machine learning. That outward reach is what
makes a concept real rather than merely learned.

### The four goals

**1. Learn practice-first, from motivation and connection.** Hands-on, building intuition. The
common maths book feels artificial to me: it gives definitions and concepts with no motivation, and
then proves theorems in whatever way is convenient to reach the result. I get a deeper feeling for
a topic by doing the proofs myself and by feeling the connections between concepts.

**2. Adapt good material into that form.** Sources I actually like are rare — Pevzner's
bioinformatics algorithms course is the example of one that is already right. Everything else needs
reshaping before it is worth my time, which is why adapting material is a first-class activity here
and not a side effect.

**3. Keep track of what I have learned and what I currently hold.** This is what *makes* the
adaptation possible: you cannot rebuild an explanation around my anchors without knowing what the
anchors are. But the record is **not exhaustive** — I am not trying to record everything known to
humanity. I am recording connections between concepts, and intuition.

**4. Become confident doing mathematics independently.** Confidence goes hand in hand with
competence. Right now I get scared whenever I see a problem that needs me to produce a proof, even
though I think I am competent enough to solve it — and the fear, not the difficulty, is what stops
me. What fixes that is evidence: a record of me having worked on proofs and problems independently,
and enough intuition about the concepts that I can extend and improvise rather than only reuse what
I already have. The Socratic approach should work well here.

### In practice

- Proofs are mine to do. A handed-over proof removes the point.
- Connections between topics matter more than coverage of any one of them.
- No introductory material — substantive sources only.
- Default session mode: Socratic, but ask me each time.
