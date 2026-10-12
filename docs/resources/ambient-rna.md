---
title: Ambient RNA
---

# Ambient RNA and background noise in droplet single-cell data

Methods for separating a droplet's own transcripts from the cell-free RNA it was sequenced with. A
form of technical noise next to the capture losses at the learning path's
[node 17](../path.md#17-technical-noise-as-a-thinning-layer). The 2026-10-10 session
([topics/ambient-rna.md](../topics/ambient-rna.md)) derived the shared likelihood from the
physics: ambient RNA is a second Poisson source, passed through the same capture thinning as the
cell's own molecules.

> **Provenance.** The first seven entries were supplied by hand on 2026-10-02. The rest were added
> on 2026-10-10 from the reading list of the session that first worked with this page. All are
> *(unvetted)*: the session used them, it did not judge them as reading. Where a description
> repeats what the session took from a paper, it says so and has not been checked.

> **Licences.** Checked on 2026-10-02 for the first seven and on 2026-10-12 for the rest. Most are
> CC BY, so an adaptation may go to `docs/adapted/` under the same licence. Four may not be
> adapted publicly, and their adaptations stay in `adapted-private/`:
>
> - CellBender — its journal version is closed and its preprint is CC BY-NC-ND.
> - souporcell — its journal version is closed and its preprint is CC BY-ND.
> - scAR — its preprint is CC BY-NC-ND.
> - Caglayan et al. — Elsevier, all rights reserved.

**Suggested reading order.** This was the assistant's suggestion at the 2026-10-10 session and is
not yet tested:

1. [Gorin & Goodman](#gorin-goodman-2026-empty-drops) and [EmptyDrops](#lun-2019-emptydrops)
2. [SoupX](#young-behjati-2020-soupx)
3. [DecontX](#yang-2020-decontx)
4. [CellSweep](#caskey-rich-2026-cellsweep), read alongside DecontX
5. [CellBender](#fleming-2023-cellbender)'s Supplementary Methods
6. [souporcell](#heaton-2020-souporcell)
7. [Janssen](#janssen-2023-background-noise)
8. The three [benchmarks](#benchmarks)

## Measurement model

### lun-2019-emptydrops — Lun et al. 2019, *EmptyDrops: distinguishing cells from empty droplets in droplet-based single-cell RNA sequencing data* { #lun-2019-emptydrops }

**Kind:** paper · **Access:** fetchable — *Genome Biology* is open access
**Licence:** **CC BY 4.0** — PMC's licence record. Adaptations publishable with attribution and the same licence
**Status:** unvetted · **Adapted:** none · **Work:** [topics/ambient-rna.md](../topics/ambient-rna.md)
[DOI](https://doi.org/10.1186/s13059-019-1662-y)

*(unvetted)* Calls cells by testing each barcode against the ambient profile estimated from
low-count barcodes. This is the formal version of "the ambient profile comes from empties", with a
Dirichlet-multinomial null.

### gorin-goodman-2026-empty-drops — Gorin & Goodman 2026, *Empty drops in scRNA-seq uncover the surprising prevalence of sequestered neuropeptide mRNA and pervasive sequencing artifacts* { #gorin-goodman-2026-empty-drops }

**Kind:** paper · **Access:** fetchable — bioRxiv preprint
**Licence:** **CC BY 4.0** — bioRxiv's own record (`api.biorxiv.org`). Adaptations publishable with attribution and the same licence
**Status:** unvetted · **Adapted:** none · **Work:** [topics/ambient-rna.md](../topics/ambient-rna.md)
[DOI](https://doi.org/10.64898/2026.02.13.705850)

*(unvetted)* Empty droplets used as internal controls, to calibrate count models and to catch
sequencing artefacts. What the session took from it, not checked:

- empty droplets are close to Poisson, which is the empirical support for the likelihood;
- many of the outliers are kb pseudoalignment artefacts that vanish with Cell Ranger.

### griffiths-2018-barcode-swapping — Griffiths et al. 2018, *Detection and removal of barcode swapping in single-cell RNA-seq data* { #griffiths-2018-barcode-swapping }

**Kind:** paper · **Access:** fetchable — *Nature Communications* is open access
**Licence:** **CC BY 4.0** — PMC's licence record. Adaptations publishable with attribution and the same licence
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1038/s41467-018-05083-x)

*(unvetted)* Quantifies barcode swapping on patterned Illumina flow cells and removes swapped
molecules from 10x data. Together with Farouni et al., it describes the channel that operates after
partitioning, which is what CellBender's swapping term and CellSweep's bulk term model.

### farouni-2020-index-hopping — Farouni et al. 2020, *Model-based analysis of sample index hopping reveals its widespread artifacts in multiplexed single-cell RNA-sequencing* { #farouni-2020-index-hopping }

**Kind:** paper · **Access:** fetchable — *Nature Communications* is open access
**Licence:** **CC BY 4.0** — PMC's licence record. Adaptations publishable with attribution and the same licence
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1038/s41467-020-16522-z)

*(unvetted)* A statistical model of sample index hopping in multiplexed droplet libraries, and
of the phantom molecules it produces.

## Methods

### young-behjati-2020-soupx — Young & Behjati 2020, *SoupX removes ambient RNA contamination from droplet-based single-cell RNA sequencing data* { #young-behjati-2020-soupx }

**Kind:** paper · **Access:** fetchable — *GigaScience* is open access
**Licence:** **CC BY 4.0** — stated in the article's own licence block. Adaptations publishable with attribution and the same licence
**Status:** unvetted · **Adapted:** none · **Work:** [topics/ambient-rna.md](../topics/ambient-rna.md), [practice/ambient-rna.md](../practice/ambient-rna.md)
**Library:** [summary and full text](https://claptar.github.io/knowledge-base-library/papers/omics-statistics/young-behjati-2020-soupx/)
[DOI](https://doi.org/10.1093/gigascience/giaa151)

*(unvetted)* Estimates the ambient-RNA profile from empty droplets and subtracts a cell-specific
fraction of it.

### yang-2020-decontx — Yang et al. 2020, *Decontamination of ambient RNA in single-cell RNA-seq with DecontX* { #yang-2020-decontx }

**Kind:** paper · **Access:** fetchable — *Genome Biology* is open access
**Licence:** **CC BY 4.0** — stated in the article's own licence block. Adaptations publishable with attribution and the same licence
**Status:** unvetted · **Adapted:** none · **Work:** [topics/ambient-rna.md](../topics/ambient-rna.md)
**Library:** [summary and full text](https://claptar.github.io/knowledge-base-library/papers/omics-statistics/yang-2020-decontx/)
[DOI](https://doi.org/10.1186/s13059-020-1950-6)

*(unvetted)* A Bayesian mixture model splitting each cell's counts into native and contaminating
parts.

### fleming-2023-cellbender — Fleming et al. 2023, *Unsupervised removal of systematic background noise from droplet-based single-cell experiments using CellBender* { #fleming-2023-cellbender }

**Kind:** paper · **Access:** local — supplied by hand; *Nature Methods* is closed
**Licence:** publisher's copyright; its bioRxiv preprint [10.1101/791699](https://doi.org/10.1101/791699) is CC BY-NC-ND, which forbids an adaptation. Adaptations stay in `adapted-private/`
**Status:** unvetted · **Adapted:** none · **Work:** [topics/ambient-rna.md](../topics/ambient-rna.md)
**Library:** [summary](https://claptar.github.io/knowledge-base-library/papers/omics-statistics/fleming-2023-cellbender/)
[DOI](https://doi.org/10.1038/s41592-023-01943-7)

*(unvetted)* An unsupervised deep generative model of the whole droplet-count process, background
included. The model itself is in the Supplementary Methods, not in the main text.

### wang-2024-sccdc — Wang et al. 2024, *scCDC: a computational method for gene-specific contamination detection and correction in single-cell and single-nucleus RNA-seq data* { #wang-2024-sccdc }

**Kind:** paper · **Access:** fetchable — *Genome Biology* is open access
**Licence:** **CC BY 4.0** — stated in the article's own licence block. Adaptations publishable with attribution and the same licence
**Status:** unvetted · **Adapted:** none
**Library:** [summary and full text](https://claptar.github.io/knowledge-base-library/papers/omics-statistics/wang-2024-sccdc/)
[DOI](https://doi.org/10.1186/s13059-024-03284-w)

*(unvetted)* Detects and corrects contamination gene by gene rather than cell by cell.

### caskey-rich-2026-cellsweep — Caskey, Rich et al. 2026, *Single-Cell Genomics Decontamination with CellSweep* { #caskey-rich-2026-cellsweep }

**Kind:** paper · **Access:** fetchable — bioRxiv preprint
**Licence:** **CC BY 4.0** — bioRxiv's own record (`api.biorxiv.org`). Adaptations publishable with attribution and the same licence
**Status:** unvetted · **Adapted:** none · **Work:** [topics/ambient-rna.md](../topics/ambient-rna.md)
**Library:** [summary and full text](https://claptar.github.io/knowledge-base-library/papers/omics-statistics/caskey-rich-2026-cellsweep/)
[DOI](https://doi.org/10.64898/2026.03.04.709349)

*(unvetted)* Decontamination without the neural-network and variational-inference machinery the
other tools use. From the Pachter lab, whose [CME work](cme-transcription.md) is the end of the
learning path.

### heaton-2020-souporcell — Heaton et al. 2020, *Souporcell: robust clustering of single-cell RNA-seq data by genotype without reference genotypes* { #heaton-2020-souporcell }

**Kind:** paper · **Access:** fetchable — PMC author manuscript (PMC7617080); *Nature Methods* is closed
**Licence:** publisher's terms; its bioRxiv preprint [10.1101/699637](https://doi.org/10.1101/699637) is CC BY-ND, which forbids an adaptation. Adaptations stay in `adapted-private/`
**Status:** unvetted · **Adapted:** none · **Work:** [topics/ambient-rna.md](../topics/ambient-rna.md)
[DOI](https://doi.org/10.1038/s41592-020-0820-1)

*(unvetted)* Clusters cells by genotype without reference genotypes and calls cross-genotype
doublets. It also estimates the ambient fraction from cross-genotype allele counts, which is the
subject of the topic's souporcell problem.

### sheng-2022-scar — Sheng et al. 2022, *Probabilistic modeling of ambient noise in single-cell omics data* { #sheng-2022-scar }

**Kind:** paper · **Access:** fetchable — bioRxiv preprint
**Licence:** **CC BY-NC-ND** — bioRxiv's own record (`api.biorxiv.org`). ND forbids an adaptation. Adaptations stay in `adapted-private/`
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1101/2022.01.14.476312)

*(unvetted)* scAR: one model of the ambient signal across droplet modalities, covering mRNA,
protein (CITE-seq) and sgRNA counts. The benchmarks below disagree about it.

Named in the session but not catalogued:

- Vireo (Huang et al. 2019), a demultiplexing contrast to souporcell;
- FastCAR, a further decontamination method;
- CellClear, a further decontamination method, which one of the benchmarks faults.

## Benchmarks

### janssen-2023-background-noise — Janssen et al. 2023, *The effect of background noise and its removal on the analysis of single-cell expression data* { #janssen-2023-background-noise }

**Kind:** paper · **Access:** fetchable — *Genome Biology* is open access
**Licence:** **CC BY 4.0** — stated in the article's own licence block. Adaptations publishable with attribution and the same licence
**Status:** unvetted · **Adapted:** none
**Library:** [summary and full text](https://claptar.github.io/knowledge-base-library/papers/omics-statistics/janssen-2023-background-noise/)
[DOI](https://doi.org/10.1186/s13059-023-02978-x)

*(unvetted)* Measures how much background noise droplet data carry and how well CellBender,
DecontX and SoupX remove it. It uses a genotype-based ground truth (mouse kidney), which is the
bridge between souporcell and the decontamination tools.

### cargnelli-2026-benchmarking-decontamination — Cargnelli et al. 2026, *Benchmarking computational decontamination of ambient RNA* { #cargnelli-2026-benchmarking-decontamination }

**Kind:** paper · **Access:** fetchable — bioRxiv preprint, and since published open access
**Licence:** **CC BY 4.0** — bioRxiv's own record (`api.biorxiv.org`). Adaptations publishable with attribution and the same licence
**Status:** unvetted · **Adapted:** none
**Library:** [summary and full text](https://claptar.github.io/knowledge-base-library/papers/omics-statistics/cargnelli-2026-benchmarking-decontamination/)
[DOI](https://doi.org/10.64898/2026.01.13.699237) · published as *Frontiers in Bioinformatics* 6:1844838, [DOI](https://doi.org/10.3389/fbinf.2026.1844838). The title, authors and abstract are the same as the preprint's; the journal's licence block was not checked

*(unvetted)* An independent benchmark of seven decontamination methods. The abstract finds no
single winner, with CellBender, DecontX and SoupX generally good. What the session took from it,
not checked:

- ambient RNA is about 11.8% in snRNA-seq against 7.8% in scRNA-seq;
- the top 10% most frequently expressed features make up about 82% of the ambient RNA.

### schroeder-2026-ambient-benchmark — Schroeder, Gerber & Ruffini 2026, *Benchmarking ambient RNA removal across droplet and well-plate platforms reveals artificial count generation as a critical failure mode of scAR and CellClear* { #schroeder-2026-ambient-benchmark }

**Kind:** paper · **Access:** fetchable — bioRxiv preprint
**Licence:** **CC BY 4.0** — bioRxiv's own record (`api.biorxiv.org`). Adaptations publishable with attribution and the same licence
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.64898/2026.04.08.717130)

*(unvetted)* Six tools on droplet and well-plate data. Its primary criterion is the integrity of
the count matrix rather than removal sensitivity alone. By that criterion scAR and CellClear
generate artificial counts, and CellBender and SoupX are reliable.

### gse337237-ambient-benchmark — GEO GSE337237, *Systematic Benchmarking of Ambient RNA decontamination Tools to Advance Precision in Single-Cell transcriptomic analysis* { #gse337237-ambient-benchmark }

**Kind:** dataset record — no paper linked yet · **Access:** fetchable — GEO, public 2026-08-10
**Licence:** none stated; only the series summary has been seen
**Status:** unvetted · **Adapted:** none

*(unvetted)* Seven tools against well-defined ground truth. The summary reports:

- CellBender and scCDC are the most accurate at estimating contamination;
- SoupX is the most robust, and the most sensitive for rare subtypes;
- scAR balances robustness and accuracy best at the cell-type level.

This contradicts [Schroeder et al.](#schroeder-2026-ambient-benchmark) on scAR.

## Why it matters

### caglayan-2022-neuronal-ambient — Caglayan, Liu & Konopka 2022, *Neuronal ambient RNA contamination causes misinterpreted and masked cell types in brain single-nuclei datasets* { #caglayan-2022-neuronal-ambient }

**Kind:** paper · **Access:** fetchable — PMC author manuscript (PMC9789184); *Neuron* is closed
**Licence:** Elsevier, all rights reserved. Adaptations stay in `adapted-private/`
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1016/j.neuron.2022.09.010)

*(unvetted)* Neuronal ambient RNA in brain snRNA-seq. Glial nuclei contaminated with it had been
annotated as distinct cell types, immature oligodendrocytes among them.

### arora-2025-ambient-mrna — Arora, James & Charoensawan 2025, *Understanding and mitigating the impact of ambient mRNA contamination in single-cell RNA-sequencing analysis* { #arora-2025-ambient-mrna }

**Kind:** paper · **Access:** fetchable — *PLoS One* is open access
**Licence:** **CC BY** — the article's own licence statement. Adaptations publishable with attribution and the same licence
**Status:** unvetted · **Adapted:** none
[DOI](https://doi.org/10.1371/journal.pone.0332440)

*(unvetted)* Ambient transcripts appear among differentially expressed genes and enriched
pathways, before and after correction with CellBender and SoupX.
