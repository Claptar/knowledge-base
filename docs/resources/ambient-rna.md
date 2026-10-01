---
title: Ambient RNA
---

# Ambient RNA and background noise in droplet single-cell data

Methods for separating a droplet's own transcripts from the cell-free RNA it was sequenced with. A
form of technical noise, like the capture losses at the learning path's
[node 17](../path.md#17-technical-noise-as-a-thinning-layer) — but whether it fits that node is
not yet settled, and nothing here claims it does.

> **Provenance.** Supplied by hand on 2026-10-02, not yet worked with. All *(unvetted)*; the
> one-line descriptions say what each paper is about, never what it is worth.

> **Licences were checked on 2026-10-02.** Six are CC BY, so their full text is in the library and
> an adaptation may go to `docs/adapted/` under the same licence. CellBender's journal version is
> closed and its preprint is CC BY-NC-ND, so it is a summary and adaptations stay in
> `adapted-private/`.

## Methods

### young-behjati-2020-soupx — Young & Behjati 2020, *SoupX removes ambient RNA contamination from droplet-based single-cell RNA sequencing data* { #young-behjati-2020-soupx }

**Kind:** paper · **Access:** fetchable — *GigaScience* is open access
**Licence:** **CC BY 4.0** — stated in the article's own licence block. Adaptations publishable with attribution and the same licence
**Status:** unvetted · **Adapted:** none
**Library:** [summary and full text](https://claptar.github.io/knowledge-base-library/papers/omics-statistics/young-behjati-2020-soupx/)
[DOI](https://doi.org/10.1093/gigascience/giaa151)

*(unvetted)* Estimates the ambient-RNA profile from empty droplets and subtracts a cell-specific
fraction of it.

### yang-2020-decontx — Yang et al. 2020, *Decontamination of ambient RNA in single-cell RNA-seq with DecontX* { #yang-2020-decontx }

**Kind:** paper · **Access:** fetchable — *Genome Biology* is open access
**Licence:** **CC BY 4.0** — stated in the article's own licence block. Adaptations publishable with attribution and the same licence
**Status:** unvetted · **Adapted:** none
**Library:** [summary and full text](https://claptar.github.io/knowledge-base-library/papers/omics-statistics/yang-2020-decontx/)
[DOI](https://doi.org/10.1186/s13059-020-1950-6)

*(unvetted)* A Bayesian mixture model splitting each cell's counts into native and contaminating
parts.

### fleming-2023-cellbender — Fleming et al. 2023, *Unsupervised removal of systematic background noise from droplet-based single-cell experiments using CellBender* { #fleming-2023-cellbender }

**Kind:** paper · **Access:** local — supplied by hand; *Nature Methods* is closed
**Licence:** publisher's copyright; its bioRxiv preprint [10.1101/791699](https://doi.org/10.1101/791699) is CC BY-NC-ND, which forbids an adaptation. Adaptations stay in `adapted-private/`
**Status:** unvetted · **Adapted:** none
**Library:** [summary](https://claptar.github.io/knowledge-base-library/papers/omics-statistics/fleming-2023-cellbender/)
[DOI](https://doi.org/10.1038/s41592-023-01943-7)

*(unvetted)* An unsupervised deep generative model of the whole droplet-count process, background
included.

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
**Status:** unvetted · **Adapted:** none
**Library:** [summary and full text](https://claptar.github.io/knowledge-base-library/papers/omics-statistics/caskey-rich-2026-cellsweep/)
[DOI](https://doi.org/10.64898/2026.03.04.709349)

*(unvetted)* Decontamination without the neural-network and variational-inference machinery the
other tools use. From the Pachter lab, whose [CME work](cme-transcription.md) is the end of the
learning path.

## Benchmarks

### janssen-2023-background-noise — Janssen et al. 2023, *The effect of background noise and its removal on the analysis of single-cell expression data* { #janssen-2023-background-noise }

**Kind:** paper · **Access:** fetchable — *Genome Biology* is open access
**Licence:** **CC BY 4.0** — stated in the article's own licence block. Adaptations publishable with attribution and the same licence
**Status:** unvetted · **Adapted:** none
**Library:** [summary and full text](https://claptar.github.io/knowledge-base-library/papers/omics-statistics/janssen-2023-background-noise/)
[DOI](https://doi.org/10.1186/s13059-023-02978-x)

*(unvetted)* Measures how much background noise droplet data carry and how well CellBender,
DecontX and SoupX remove it.

### cargnelli-2026-benchmarking-decontamination — Cargnelli et al. 2026, *Benchmarking computational decontamination of ambient RNA* { #cargnelli-2026-benchmarking-decontamination }

**Kind:** paper · **Access:** fetchable — bioRxiv preprint
**Licence:** **CC BY 4.0** — bioRxiv's own record (`api.biorxiv.org`). Adaptations publishable with attribution and the same licence
**Status:** unvetted · **Adapted:** none
**Library:** [summary and full text](https://claptar.github.io/knowledge-base-library/papers/omics-statistics/cargnelli-2026-benchmarking-decontamination/)
[DOI](https://doi.org/10.64898/2026.01.13.699237)

*(unvetted)* An independent benchmark of the decontamination methods above.
