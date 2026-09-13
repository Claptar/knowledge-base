---
title: Notes
---

# Notes

My own expository writing — the explanation I'd give if I had to teach the thing. This is a
different kind of object from the rest of the knowledge base, and the distinction is worth keeping
sharp:

| | Holds | Earned by |
| --- | --- | --- |
| **Topics** | the **record** of my trajectory through a subject — none yet | a session. `Status: solid` requires *How I could have come up with this* in my own words |
| **Notes** (here) | **material** I wrote — exposition, aimed at a reader | writing it |
| **Adapted** | someone else's material, rewritten motivation-first — nothing filed yet | a source going through `adapt-material` |

**A note is not evidence of understanding.** These were written with an AI assistant, and a clean
exposition can be produced without having derived anything. Every note carries a provenance banner
saying so. When a note's subject actually gets worked through in a session, that produces a *topic
file*, and the note is linked from it as material — the two are not merged.

Imported on 2026-09-13 from [Claptar/math-notes](https://github.com/Claptar/math-notes), with
Jekyll front matter stripped, `\(…\)` converted to `$…$` so the maths renders here, and filenames
normalised.

## Structures

A single sequence, from binary operations to σ-algebras. In the source repository it was split
across two folders and the numbering looked broken in both; it is one built course and is kept
together here.

| | |
| --- | --- |
| [01 Binary operations and associativity](structures/01-binary-operations-and-associativity.md) | where the whole hierarchy starts |
| [02 Semigroups and monoids](structures/02-semigroups-and-monoids.md) | |
| [03 Groups and reversibility](structures/03-groups-and-reversibility.md) | |
| [04 Symmetries and groups](structures/04-symmetries-and-groups.md) | |
| [05 Commutativity and abelian groups](structures/05-commutativity-and-abelian-groups.md) | |
| [06 Rings and distributivity](structures/06-rings-and-distributivity.md) | |
| [07 Fields and scalars](structures/07-fields-and-scalars.md) | |
| [08 Vector spaces](structures/08-vector-spaces.md) | |
| [09 Algebras over fields](structures/09-algebras-over-fields.md) | |
| [10 σ-algebras](structures/10-sigma-algebras.md) | the bridge to measure theory, and to [probability](#probability) |
| [11 Map of structures](structures/11-map-of-structures.md) | the whole hierarchy in one place |

## Linear algebra

Standalone notes, heavily diagrammed — 31 figures.

- [Linear subspaces](linear-algebra/linear-subspaces.md)
- [Basis and coordinates](linear-algebra/basis-coordinates.md)
- [Change of basis](linear-algebra/change-of-basis.md)
- [Isomorphism](linear-algebra/isomorphism.md)
- [Direct sums and complements](linear-algebra/direct-sums-and-complements.md)
- [Quotient spaces](linear-algebra/quotient-spaces.md)

## Probability

Two subjects, each written twice by different routes. Both versions are kept: comparing two
expositions of one idea is worth more than picking a winner, and which framing lands is itself
information.

| Subject | Treatments |
| --- | --- |
| Gaussian vectors and covariance geometry | [Source of the confusion](probability/gaussian-vectors-covariance-geometry.md) · [The conceptual problem](probability/gaussian-vectors-covariance-geometry-alt.md) |
| Sample variance as a quadratic form | [The main point](probability/sample-variance-quadratic-form.md) · [Main question](probability/sample-variance-quadratic-form-geometry.md) |

These connect directly to the PCA-as-Gram-matrix anchor in [profile](../profile.md) — the covariance
operator as a Gram matrix in $L^2(\Omega)$ is the same spectral story, which makes them the most
load-bearing notes here for what comes next.

## Written elsewhere

Work of mine that lives in its own repository and is deliberately not absorbed:

| | Why it stays out |
| --- | --- |
| [Claptar/design-patterns](https://github.com/Claptar/design-patterns) — 14 patterns, each with a motivation-first chapter and three exercise/solution pairs (114 markdown, 95 Python) | Software craft, not mathematics or computational biology. Folding it in would widen what every skill here has to handle |
| [Claptar/play_around_find_out](https://github.com/Claptar/play_around_find_out) — 10 notebooks: statistics, probability, machine learning, bioinformatics, information theory | A notebook's value is that it runs. Rendering it to a static page keeps the prose and throws away the thing that made it worth writing |
