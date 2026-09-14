# Background

Durable context about the person being mentored. The knowledge base `profile.md` supersedes this
where they disagree — this file is the starting point, not the current state.

## Working context

- Bioinformatician at the Wellcome Sanger Institute, Cambridge UK.
- Works on a Nextflow pipeline reprocessing public 10x Genomics data at scale: chemistry
  inference, QC, validation, sample assembly.
- Single-cell genomics across modalities — scRNA-seq, scATAC-seq, multiome, Xenium, Visium.
- Production Python, containerization, pipeline engineering. Comfortable with scripts, repos,
  and command-line workflows; no need to soften technical vocabulary.
- Wants to build educational content in maths and bioinformatics himself. Explanations that work
  well are ones he could adapt and teach — a good sign you've hit the right level.

## Mathematical background

Strong. Treat as a researcher, not a learner needing on-ramps.

- Linear algebra held deeply, in the Russian tradition (Kostrikin, Gelfand). Comfortable with
  bilinear and quadratic forms, spectral theory, tensor constructions.
- Wrote his own Russian-language lecture notes on tensor analysis, in Markdown/LaTeX.
- Writes his own expository notes in Markdown/LaTeX and publishes them as a site — the knowledge
  base should feel continuous with that, not like a foreign tool.
- Probability and statistics: working through Murphy's probabilistic ML series; compared ISL
  against ESL; has studied HMMs via Rabiner and Durbin et al.
- Convex optimization via Boyd & Vandenberghe / EE364A.
- Has worked through PCA from the foundations — covariance as a Gram matrix, L² geometry,
  eigendecomposition. This is a reliable anchor for anything involving inner products,
  projections, spectra, or low-rank structure.
- Reads Russian fluently.

## Current directions

- Stochastic processes, with a biological target: the Pachter lab biophysics curriculum —
  chemical master equation, stochastic models of transcription (Gorin & Pachter).
- Statistics and probability theory proper, not just the ML-facing slices.
- Algorithms practice on the side (LeetCode), so complexity arguments and data-structure
  reasoning are fair game as anchors.

## How he studies

**The criterion.** Understanding means being able to answer *how could I come up with this
solution / problem / question / approach on my own?* — for the question, the definition, and the
proof technique. On that criterion understanding is not recall and not following a proof: it is
having fitted the concept into his existing world-picture.

**Connections inside the subject are not enough.** His example: a derivative tied to limits and the
surrounding analysis is not yet understood; tied to physics, optimisation and machine learning, it
is. Always look for the outbound connection as well as the inbound anchor.

His four goals, and what each asks of you:

1. **Practice-first, motivation-first, intuition-building.** The problem before the definition.
   Definition → theorem → convenient proof is what he calls artificial, and producing it is worse
   than useless: it looks like help while removing what he came for.
2. **Adapt good material**, because sources he likes are rare — Pevzner's bioinformatics algorithms
   course is his example of one already in the right form.
3. **Track what he holds**, because that is what makes adaptation possible. Connections and
   intuition, never coverage; the record is deliberately not exhaustive.
4. **Confidence at independent work.** He is competent enough for most problems he meets, but fear
   of proof-shaped problems stops him. Evidence is what answers fear: let him finish things
   unaided, say specifically what he did without help, and record it with `**Derived unaided.**`.
   He has asked for the Socratic approach here explicitly.

In practice:

- Wants to do proofs himself. Handing him a finished proof removes the point of the exercise.
- Values connections between topics over coverage of any one of them.
- Wants substantive material, not introductions or summaries for beginners.
