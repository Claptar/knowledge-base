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

## Foundations — the CME and its approximations

### gillespie-1976-ssa — Gillespie 1976, *A general method for numerically simulating the stochastic time evolution of coupled chemical reactions* { #gillespie-1976-ssa }

**Kind:** paper · **Access:** unreadable — institutional access only
**Status:** unvetted · **Adapted:** none
[DOI](<https://doi.org/10.1016/0021-9991(76)90041-3>)

*(unvetted)* The SSA. The original, so it argues for the algorithm rather than presenting it; that
argument is the reason to read it here rather than a modern summary.

### gillespie-2000-cle — Gillespie 2000, *The chemical Langevin equation* { #gillespie-2000-cle }

**Kind:** paper · **Access:** unreadable — institutional access only
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1063/1.481811)

*(unvetted)* Derives the CLE from the CME under two explicit timescale conditions. Valuable
precisely because the conditions are stated as conditions rather than absorbed into an expansion.

### gillespie-2001-tau-leaping — Gillespie 2001, *Approximate accelerated stochastic simulation* { #gillespie-2001-tau-leaping }

**Kind:** paper · **Access:** unreadable — institutional access only
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1063/1.1378322)

*(unvetted)* $\tau$-leaping. Read after [1976](#gillespie-1976-ssa), for where the exactness is
traded away.

### gardiner-chaturvedi-1977-poisson-representation — Gardiner & Chaturvedi 1977, *The Poisson Representation I* { #gardiner-chaturvedi-1977-poisson-representation }

**Kind:** paper · **Access:** unreadable — institutional access only
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1007/BF01014349)

*(unvetted)* Expands the distribution over Poissons with a quasi-probability weight — which may be
negative or complex, and that latitude is the point — turning master equations into Fokker–Planck
and SDE form. The likely bridge to why count data is mixed-Poisson rather than Poisson.

### munsky-khammash-2006-fsp — Munsky & Khammash 2006, *The finite state projection algorithm* { #munsky-khammash-2006-fsp }

**Kind:** paper · **Access:** unreadable — institutional access only
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1063/1.2145882)

*(unvetted)* Truncation of the state space with an error bound.

### jahnke-huisinga-2007-monomolecular — Jahnke & Huisinga 2007, *Solving the CME for monomolecular reaction systems analytically* { #jahnke-huisinga-2007-monomolecular }

**Kind:** paper · **Access:** unreadable — institutional access only
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1007/s00285-006-0034-x)

*(unvetted)* The exact solution for the monomolecular case, as a convolution of multinomial and
product-Poisson distributions. This is the paper that marks the boundary of what is solvable.

### vastola-holmes-2020-path-integral-cle — Vastola & Holmes 2020, *Chemical Langevin equation: a path-integral view* { #vastola-holmes-2020-path-integral-cle }

**Kind:** paper · **Access:** unreadable — institutional access only
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1103/PhysRevE.101.032417)

*(unvetted)* A third derivation of the CLE, explicitly compared with the system-size route. Use as
the cross-check on whether the routes agree.

### paulsson-2004-summing-up-noise — Paulsson 2004, *Summing up the noise in gene networks* { #paulsson-2004-summing-up-noise }

**Kind:** paper · **Access:** unreadable — institutional access only
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1038/nature02257)

*(unvetted)* Fluctuation–dissipation applied to gene expression noise; unifies scattered earlier
results.

### thomas-2014-conditional-lna — Thomas et al. 2014, *Phenotypic switching in gene regulatory networks* { #thomas-2014-conditional-lna }

**Kind:** paper · **Access:** unreadable — institutional access only
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1073/pnas.1400049111)

*(unvetted)* Conditional LNA — i.e. where the plain LNA fails.

## Transcription models

### peccoud-ycart-1995-telegraph — Peccoud & Ycart 1995, *Markovian modeling of gene-product synthesis* { #peccoud-ycart-1995-telegraph }

**Kind:** paper · **Access:** unreadable — institutional access only
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1006/tpbi.1995.1027)

*(unvetted)* The telegraph model and its analytical steady state. The origin of the two-state
picture everything downstream assumes.

### shahrezaei-swain-2008-analytical-distributions — Shahrezaei & Swain 2008, *Analytical distributions for stochastic gene expression* { #shahrezaei-swain-2008-analytical-distributions }

**Kind:** paper · **Access:** unreadable — institutional access only
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1073/pnas.0803850105)

*(unvetted)* Protein distributions via mRNA/protein timescale separation.

### singh-bokes-2012-mrna-transport — Singh & Bokes 2012, *Consequences of mRNA transport on stochastic variability in protein levels* { #singh-bokes-2012-mrna-transport }

**Kind:** paper · **Access:** unreadable — institutional access only
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1016/j.bpj.2012.07.015)

*(unvetted)* The bursty model solved by generating functions — the worked example of the technique,
more than the biological conclusion.

### grima-2012-feedback-loop — Grima et al. 2012, *Steady-state fluctuations of a genetic feedback loop* { #grima-2012-feedback-loop }

**Kind:** paper · **Access:** unreadable — institutional access only
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1063/1.4736721)

*(unvetted)* An exact steady state with feedback, i.e. beyond the monomolecular boundary.

## Pachter lab — the destination

### gorin-pachter-2022-bursty-splicing — Gorin & Pachter 2022, *Modeling bursty transcription and splicing with the chemical master equation* { #gorin-pachter-2022-bursty-splicing }

**Kind:** paper · **Access:** unreadable — institutional access only
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1016/j.bpj.2022.02.004)

*(unvetted)* The unspliced/spliced two-species model, and the joint distribution the identifiability
argument turns on.

### gorin-2022-interpretable-tractable — Gorin, Vastola, Fang & Pachter 2022, *Interpretable and tractable models of transcriptional noise* { #gorin-2022-interpretable-tractable }

**Kind:** paper · **Access:** fetchable — Nature Communications is open access
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1038/s41467-022-34857-7)

*(unvetted)* Tractability treated as a modelling criterion in its own right. That claim — that what
is solvable shapes what is modelled — is what the path's inference layer is meant to test.

### gorin-pachter-2020-intrinsic-extrinsic — Gorin & Pachter 2020, *Intrinsic and extrinsic noise are distinguishable in a synthesis–export–degradation model* { #gorin-pachter-2020-intrinsic-extrinsic }

**Kind:** paper · **Access:** fetchable — bioRxiv preprint
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1101/2020.09.25.312868)

*(unvetted)* The model-level version of a distinction usually defined by experiment.

### gorin-2022-transient-delay-cme — Gorin, Yoshida & Pachter 2022, *Transient and delay chemical master equations* { #gorin-2022-transient-delay-cme }

**Kind:** paper · **Access:** fetchable — bioRxiv preprint
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1101/2022.10.17.512599)

*(unvetted)* What it costs to leave the exponential-holding-time assumption behind.

### pachter-biophysics-docs — Pachter Lab, *Biophysics* documentation { #pachter-biophysics-docs }

**Kind:** site · **Access:** fetchable · <https://biophysics.readthedocs.io/>
**Status:** unvetted · **Adapted:** none

*(unvetted)* The lab's own tool table and reading list, and the source of this section. Also the
entry point to Monod, biVI, meK-Means and Chronocell.

## The measurement layer

### tang-2023-capture-efficiency — Tang et al. 2023, *Modelling capture efficiency of single-cell RNA-sequencing data* { #tang-2023-capture-efficiency }

**Kind:** paper · **Access:** fetchable — *Bioinformatics* is open access
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1093/bioinformatics/btad395)

*(unvetted)* Telegraph model plus binomial capture, and a four-way comparison of inference methods
(MLE, MME, ABC, neural). The comparison is the valuable part.

### tang-2020-baynorm — Tang et al. 2020, *bayNorm* { #tang-2020-baynorm }

**Kind:** paper · **Access:** fetchable — *Bioinformatics* is open access
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1093/bioinformatics/btz726)

*(unvetted)* Binomial capture inside a Bayesian normalisation method; read for the model, not the
tool.
