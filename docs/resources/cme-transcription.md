---
title: CME and transcription
---

# Chemical master equation and stochastic transcription

The primary literature the [learning path](../path.md) terminates in. These are papers, not courses
— each one is a single move, and the path is what says where each belongs.

> **Provenance.** Taken from the Pachter Lab's own
> [Foundations](https://biophysics.readthedocs.io/en/latest/foundations.html) and
> [Contributions](https://biophysics.readthedocs.io/en/latest/contributions.html) pages on
> 2026-09-13 — the lab's reading list, not my judgement of it. All *(unvetted)* until worked with.

> **Access here means *agent* reachability, not mine.** Most of these are journal articles behind
> publisher paywalls that a Sanger login opens and an agent cannot. `unreadable` on this page
> usually means "fetch it yourself and drop it in `sources/`", not "unavailable". Preprints and
> open-access articles are marked `fetchable` because an agent really can read them.

> **Licences are unresolved on this page**, so every adaptation of one of these goes to
> `adapted-private/` until the licence is checked and recorded here. Open access is not a licence:
> a Nature Communications article and a bioRxiv preprint each carry a specific one, and which it is
> decides whether a derivative may be published. Resolve before adapting, never in the adapting.

## Foundations — the CME and its approximations

### gillespie-1976-ssa — Gillespie 1976, *A general method for numerically simulating the stochastic time evolution of coupled chemical reactions* { #gillespie-1976-ssa }

**Kind:** paper · **Access:** unreadable — institutional access only
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[DOI](<https://doi.org/10.1016/0021-9991(76)90041-3>)

*(unvetted)* The SSA. The original, so it argues for the algorithm rather than presenting it; that
argument is the reason to read it here rather than a modern summary.

### gillespie-2000-cle — Gillespie 2000, *The chemical Langevin equation* { #gillespie-2000-cle }

**Kind:** paper · **Access:** unreadable — institutional access only
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1063/1.481811)

*(unvetted)* Derives the CLE from the CME under two explicit timescale conditions. Valuable
precisely because the conditions are stated as conditions rather than absorbed into an expansion.

### gillespie-2001-tau-leaping — Gillespie 2001, *Approximate accelerated stochastic simulation* { #gillespie-2001-tau-leaping }

**Kind:** paper · **Access:** unreadable — institutional access only
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1063/1.1378322)

*(unvetted)* $\tau$-leaping. Read after [1976](#gillespie-1976-ssa), for where the exactness is
traded away.

### gardiner-chaturvedi-1977-poisson-representation — Gardiner & Chaturvedi 1977, *The Poisson Representation I* { #gardiner-chaturvedi-1977-poisson-representation }

**Kind:** paper · **Access:** unreadable — institutional access only
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1007/BF01014349)

*(unvetted)* Expands the distribution over Poissons with a quasi-probability weight — which may be
negative or complex, and that latitude is the point — turning master equations into Fokker–Planck
and SDE form. The likely bridge to why count data is mixed-Poisson rather than Poisson.

### munsky-khammash-2006-fsp — Munsky & Khammash 2006, *The finite state projection algorithm* { #munsky-khammash-2006-fsp }

**Kind:** paper · **Access:** unreadable — institutional access only
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1063/1.2145882)

*(unvetted)* Truncation of the state space with an error bound.

### jahnke-huisinga-2007-monomolecular — Jahnke & Huisinga 2007, *Solving the CME for monomolecular reaction systems analytically* { #jahnke-huisinga-2007-monomolecular }

**Kind:** paper · **Access:** unreadable — institutional access only
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1007/s00285-006-0034-x)

*(unvetted)* The exact solution for the monomolecular case, as a convolution of multinomial and
product-Poisson distributions. This is the paper that marks the boundary of what is solvable.

### vastola-holmes-2020-path-integral-cle — Vastola & Holmes 2020, *Chemical Langevin equation: a path-integral view* { #vastola-holmes-2020-path-integral-cle }

**Kind:** paper · **Access:** unreadable — institutional access only
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1103/PhysRevE.101.032417)

*(unvetted)* A third derivation of the CLE, explicitly compared with the system-size route. Use as
the cross-check on whether the routes agree.

### paulsson-2004-summing-up-noise — Paulsson 2004, *Summing up the noise in gene networks* { #paulsson-2004-summing-up-noise }

**Kind:** paper · **Access:** unreadable — institutional access only
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1038/nature02257)

*(unvetted)* Fluctuation–dissipation applied to gene expression noise; unifies scattered earlier
results.

### thomas-2014-conditional-lna — Thomas et al. 2014, *Phenotypic switching in gene regulatory networks* { #thomas-2014-conditional-lna }

**Kind:** paper · **Access:** unreadable — institutional access only
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1073/pnas.1400049111)

*(unvetted)* Conditional LNA — i.e. where the plain LNA fails.

## Transcription models

### peccoud-ycart-1995-telegraph — Peccoud & Ycart 1995, *Markovian modeling of gene-product synthesis* { #peccoud-ycart-1995-telegraph }

**Kind:** paper · **Access:** unreadable — institutional access only
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1006/tpbi.1995.1027)

*(unvetted)* The telegraph model and its analytical steady state. The origin of the two-state
picture everything downstream assumes.

### shahrezaei-swain-2008-analytical-distributions — Shahrezaei & Swain 2008, *Analytical distributions for stochastic gene expression* { #shahrezaei-swain-2008-analytical-distributions }

**Kind:** paper · **Access:** unreadable — institutional access only
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1073/pnas.0803850105)

*(unvetted)* Protein distributions via mRNA/protein timescale separation.

### singh-bokes-2012-mrna-transport — Singh & Bokes 2012, *Consequences of mRNA transport on stochastic variability in protein levels* { #singh-bokes-2012-mrna-transport }

**Kind:** paper · **Access:** unreadable — institutional access only
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1016/j.bpj.2012.07.015)

*(unvetted)* The bursty model solved by generating functions — the worked example of the technique,
more than the biological conclusion.

### grima-2012-feedback-loop — Grima et al. 2012, *Steady-state fluctuations of a genetic feedback loop* { #grima-2012-feedback-loop }

**Kind:** paper · **Access:** unreadable — institutional access only
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1063/1.4736721)

*(unvetted)* An exact steady state with feedback, i.e. beyond the monomolecular boundary.

## Pachter lab — the destination

### gorin-pachter-2022-bursty-splicing — Gorin & Pachter 2022, *Modeling bursty transcription and splicing with the chemical master equation* { #gorin-pachter-2022-bursty-splicing }

**Kind:** paper · **Access:** unreadable — institutional access only
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1016/j.bpj.2022.02.004)

*(unvetted)* The unspliced/spliced two-species model, and the joint distribution the identifiability
argument turns on.

### gorin-2022-interpretable-tractable — Gorin, Vastola, Fang & Pachter 2022, *Interpretable and tractable models of transcriptional noise* { #gorin-2022-interpretable-tractable }

**Kind:** paper · **Access:** fetchable — Nature Communications is open access
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1038/s41467-022-34857-7)

*(unvetted)* Tractability treated as a modelling criterion in its own right. That claim — that what
is solvable shapes what is modelled — is what the path's inference layer is meant to test.

### gorin-pachter-2020-intrinsic-extrinsic — Gorin & Pachter 2020, *Intrinsic and extrinsic noise are distinguishable in a synthesis–export–degradation model* { #gorin-pachter-2020-intrinsic-extrinsic }

**Kind:** paper · **Access:** fetchable — bioRxiv preprint
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1101/2020.09.25.312868)

*(unvetted)* The model-level version of a distinction usually defined by experiment.

### gorin-2022-transient-delay-cme — Gorin, Yoshida & Pachter 2022, *Transient and delay chemical master equations* { #gorin-2022-transient-delay-cme }

**Kind:** paper · **Access:** fetchable — bioRxiv preprint
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1101/2022.10.17.512599)

*(unvetted)* What it costs to leave the exponential-holding-time assumption behind.

### pachter-biophysics-docs — Pachter Lab, *Biophysics* documentation { #pachter-biophysics-docs }

**Kind:** site · **Access:** fetchable · <https://biophysics.readthedocs.io/>
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none

*(unvetted)* The lab's own tool table and reading list, and the source of this section. Also the
entry point to Monod, biVI, meK-Means and Chronocell.

## The measurement layer

### tang-2023-capture-efficiency — Tang et al. 2023, *Modelling capture efficiency of single-cell RNA-sequencing data* { #tang-2023-capture-efficiency }

**Kind:** paper · **Access:** fetchable — *Bioinformatics* is open access
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1093/bioinformatics/btad395)

*(unvetted)* Telegraph model plus binomial capture, and a four-way comparison of inference methods
(MLE, MME, ABC, neural). The comparison is the valuable part.

### tang-2020-baynorm — Tang et al. 2020, *bayNorm* { #tang-2020-baynorm }

**Kind:** paper · **Access:** fetchable — *Bioinformatics* is open access
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1093/bioinformatics/btz726)

*(unvetted)* Binomial capture inside a Bayesian normalisation method; read for the model, not the
tool.

## Pachter lab theses — the same work, in long form

Six CaltechTHESIS dissertations from Lior Pachter's group. A thesis is the one place the route to
an idea survives at length: the papers above are the compressed results, and the thesis is the
chapter that says which alternative was tried first and why it was abandoned. Each also carries a
bibliography assembled by someone working on exactly this — an expert's reading list, and a source
in its own right.

> **Not yet fetched.** CaltechTHESIS refuses automated requests from here — both `curl` and an
> agent fetch time out or are refused, while `github.com`, `pypi.org` and `ocw.mit.edu` answer
> normally. The metadata below came through before the block. **Download the PDFs by hand** into
> the library repo's `sources/` under the slug each entry names; everything downstream then
> works. The recipe is that repo's `skills/collect-materials/references/caltech-thesis.md`.

> **Licence unresolved for all six.** The rights row on each record could not be read before the
> block, and CaltechTHESIS records vary: some carry a Creative Commons grant, many carry "no
> commercial reproduction, distribution, display or performance rights". A thesis is converted
> like any other public material, but an *adaptation* is a derivative work governed by the
> licence — so adaptations stay in `adapted-private/` until a row is read. Open access is not a
> licence.

### gorin-2023-scrnaseq-foundations — Gorin 2023, *Stochastic Foundations for Single-Cell RNA Sequencing* { #gorin-2023-scrnaseq-foundations }

**Kind:** thesis · **Access:** unreadable — fetch by hand to `sources/gorin-2023-scrnaseq-foundations/`
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[Record](https://thesis.library.caltech.edu/16062/) · [PDF](https://thesis.library.caltech.edu/16062/03/gg_thesis_230602.pdf)

*(unvetted)* **Biophysical — the central one.** Gorin is the first author of four entries above
([bursty splicing](#gorin-pachter-2022-bursty-splicing),
[interpretable and tractable](#gorin-2022-interpretable-tractable),
[intrinsic and extrinsic](#gorin-pachter-2020-intrinsic-extrinsic),
[transient and delay CME](#gorin-2022-transient-delay-cme)), so this is those papers with the
connective argument restored. From the record's abstract: generic strategies for modelling the
biological and technical components of sequencing experiments, with case studies motivating them.
Advisor Pachter.

### fang-2025-biophysical-normalisation — Fang 2025, *A Biophysical Approach to Normalization and Trajectory Inference in Single-Cell RNA Sequencing Data Analysis* { #fang-2025-biophysical-normalisation }

**Kind:** thesis · **Access:** unreadable — fetch by hand to `sources/fang-2025-biophysical-normalisation/`
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[Record](https://thesis.library.caltech.edu/17389/) · [DOI](https://doi.org/10.7907/asek-t904)

*(unvetted)* **Biophysical.** The record's abstract names the CME as the theoretical foundation for
stochastic gene expression models and claims a gap in the uniform approximations — which is
directly the question the [approximations section](#gillespie-2000-cle) above circles. Then two
mechanistic models for normalisation and trajectory inference, both of which are normally done by
heuristics with no mechanistic grounding. Advisor Pachter; committee Thomson, Bois, Chong.

### felce-2026-biophysical-evolution — Felce 2026, *Biophysical Modeling for Gene Expression and Evolution* { #felce-2026-biophysical-evolution }

**Kind:** thesis · **Access:** unreadable — fetch by hand to `sources/felce-2026-biophysical-evolution/`
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[Record](https://thesis.library.caltech.edu/17880/) · [PDF](https://thesis.library.caltech.edu/17880/01/Thesis_final_CF.pdf)

*(unvetted)* **Biophysical.** Joint models of chromatin accessibility (ATAC-seq) and protein counts
alongside transcriptomic counts — the multi-modal extension of the single-modality models above —
then the same machinery pushed into phylogenetics to test competing mechanistic hypotheses for how
gene expression evolves. Advisor Pachter.

### carilli-2026-expression-regulation — Carilli 2026, *Genetic Interrogation of Expression Regulation* { #carilli-2026-expression-regulation }

**Kind:** thesis · **Access:** unreadable — fetch by hand to `sources/carilli-2026-expression-regulation/`
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[Record](https://thesis.library.caltech.edu/18729/) · [PDF](https://thesis.library.caltech.edu/18729/02/Thesis_Carilli_Maria.pdf)

*(unvetted)* **Biophysical.** Accelerated inference for biophysical models of scRNA-seq, a genetic
testing framework, and an application across eight tissues in eight mouse strains. The abstract's
framing — moving past average expression to transcription, splicing and degradation as processes —
is the same move as the bursty-splicing paper, so read it against that.

### luebbert-2024-transcriptomic-complexity — Luebbert 2024, *Complexity of Transcriptomic Data Analysis and Implications for Biological Discovery* { #luebbert-2024-transcriptomic-complexity }

**Kind:** thesis · **Access:** unreadable — fetch by hand to `sources/luebbert-2024-transcriptomic-complexity/`
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[Record](https://thesis.library.caltech.edu/16368/) · [DOI](https://doi.org/10.7907/xnw5-v914)

*(unvetted)* **Not biophysical** — software tools, references for organisms without good genomes,
and virus identification from scRNA-seq. Lower priority for the CME track. Kept catalogued because
the bibliography is still a Pachter-lab reading list.

### galvez-merchan-2023-mrna-degradation — Gálvez Merchán 2023, *Studies of mRNA Expression and Degradation* { #galvez-merchan-2023-mrna-degradation }

**Kind:** thesis · **Access:** unreadable — fetch by hand to `sources/galvez-merchan-2023-mrna-degradation/`
**Licence:** unresolved — adaptation stays in `adapted-private/` until checked
**Status:** unvetted · **Adapted:** none
[Record](https://thesis.library.caltech.edu/16081/) · [DOI](https://doi.org/10.7907/esxk-ch24)

*(unvetted)* **Mostly not biophysical** — nonsense-mediated decay and the Commons Cell Atlas. The
degradation half touches the same rate constants the CME models carry, so it may be worth the
chapter rather than the thesis. Advisors Pachter and Voorhees.
