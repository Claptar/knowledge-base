# NMF: what the data pins down, and what the loss assumes

> **Written with an AI assistant.** Written by me with Claude from the study session of
> 2026-10-06, while reading Kotliar et al. 2019 (cNMF). It is *material* — my own exposition — not
> evidence of understanding: what I actually derived, and where I went wrong, is recorded in
> [topics/nmf.md](../../topics/nmf.md) and [practice/nmf.md](../../practice/nmf.md).

**For whom.** You know bases, rank and change of basis, and what a likelihood is. You have seen
non-negative matrix factorisation (NMF) used on single-cell data, and wondered whether the
"programs" it returns are facts about the cells or artefacts of the algorithm.

**The two questions.** (1) NMF returns one pair $(W, H)$. If other pairs fit equally well, what
does the data actually determine? (2) NMF minimises some loss. Which noise model is that loss
secretly assuming, and is it honest for counts?

---

## 1 The model, and why not just cluster

Take a count matrix $X$ with $N$ cells as rows and $G$ genes as columns. Suppose there are $K$
*gene expression programs* $h_1, \dots, h_K \in \mathbb{R}^G_{\ge 0}$, and each cell is a
non-negative mixture of them:

$$
x_i = \sum_{k=1}^K w_{ik} h_k, \qquad\text{i.e.}\qquad X = WH, \quad W \in \mathbb{R}^{N\times K}_{\ge 0},\; H \in \mathbb{R}^{K \times G}_{\ge 0}.
$$

Entry by entry, $x_{ij} = \sum_k w_{ik} h_{kj}$: the expression of gene $j$ in cell $i$ is a sum of
one contribution per program. Because the model is linear,
$h_{kj} = \partial x_{ij} / \partial w_{ik}$ — the amount of gene $j$ that program $k$ produces
per unit of usage, the same in every cell. A recipe picture works: $h_k$ is an ingredient list for
one batch, $w_{ik}$ is how many batches cell $i$ cooks.

**Clustering is the special case** where every row of $W$ has exactly one non-zero entry. Then the
best $H$ is the matrix of cluster means, and the problem is $k$-means. NMF relaxes the one-hot
constraint, so a cell can be 70% one cell type plus 20% cell cycle, and a doublet can be half and
half. Kotliar et al. split programs into *identity* programs (a cell type) and *activity* programs
(cell cycle, hypoxia, a stimulus response) that ride on top of many identities. Keep the activity
programs in mind: they are where section 5 bites.

## 2 What the data alone determines

Work in the exact case, $X = WH$ with $\operatorname{rank} X = K$, so that noise cannot hide the
question.

**The rows of $H$ are a basis of $\mathrm{row}(X)$.** Every row of $X$ is a combination of the rows
of $H$, so $\mathrm{row}(X) \subseteq \langle h_1, \dots, h_K \rangle$. Dimensions sandwich it:
$K = \dim \mathrm{row}(X) \le \dim \langle h_1, \dots, h_K \rangle \le K$. Equal dimensions, nested
subspaces, so they are equal, and $K$ vectors spanning a $K$-dimensional space are independent.
The row $w_i$ is then cell $i$'s *coordinates* in that basis.

**Every other exact factorisation** $X = W'H'$ (same $K$) also has rows of $H'$ forming a basis of
the same subspace. Writing each $h'_k$ in the old basis gives a $K \times K$ matrix $S$:

$$
H' = SH, \qquad W' = WS^{-1}, \qquad S \in GL(K).
$$

Conversely, any invertible $S$ gives $W'H' = WS^{-1}SH = X$. So the solutions form one orbit of
$GL(K)$ acting by $S \cdot (W, H) = (WS^{-1}, SH)$. The inverse sits on $W$ so that applying $T$
after $S$ is the action of $TS$; without it, composition comes out in the wrong order. The data
identifies the orbit and nothing inside it: $K^2$ free parameters, all fitting perfectly. In
statistical language the parameters are *not identifiable*. Label switching in mixture models and
HMMs is the small version of the same thing, with the permutation group in place of $GL(K)$.

**What PCA does with this freedom.** It picks one point of the orbit by convention: orthonormal
rows of $H$, orthogonal columns of $W$. That is convenient for linear algebra and says nothing about
biology, which is why principal components come out as mixtures of the true programs (Kotliar et
al., Fig. 2).

??? question "Exercise — why $S^{-1}$ on $W$?"
    Define the alternative "action" $S \star (W, H) = (WS, SH)$. Check whether
    $T \star (S \star (W, H)) = (TS) \star (W, H)$. What goes wrong, and what does that say about
    which combinations are legitimate group actions?

## 3 Non-negativity, geometrically

Three spaces are in play, and it pays to name them.

| Space | A vector is | What lives there |
| --- | --- | --- |
| gene space $\mathbb{R}^G$ | one number per gene | cells $x_i$ (rows of $X$), programs $h_k$ (rows of $H$) |
| program space $\mathbb{R}^K$ | one number per program | usages $w_i$ (rows of $W$) |
| cell space $\mathbb{R}^N$ | one number per cell | a gene across cells (columns of $X$), a program's usage across cells (columns of $W$) |

The map $w \mapsto wH$ sends program space injectively onto $\mathrm{row}(X)$, a $K$-dimensional
slice of gene space. Inside that slice:

- $\mathrm{cone}(H) = \{\sum_k c_k h_k : c \ge 0\}$ is the image of the non-negative orthant of
  program space. So **$w_i \ge 0$ is the same statement as $x_i \in \mathrm{cone}(H)$.**
- $\mathrm{row}(X) \cap \mathbb{R}^G_{\ge 0}$ — call it the *wedge* — is the set of vectors in the
  slice with no negative gene entry. **$H \ge 0$ says every arrow $h_k$ lies in the wedge.**

So a non-negative factorisation is a choice of $K$ arrows in the wedge whose cone contains every
cell, and every alternative is squeezed between two walls:

$$
\{\text{cells}\} \;\subseteq\; \mathrm{cone}(H') \;\subseteq\; \mathrm{row}(X) \cap \mathbb{R}^G_{\ge 0}.
$$

Uniqueness is the question of whether there is room to move between them.

**A worked case, $K = 2$.** Replace $h_2$ by $h_1 + h_2$, keeping $h_1$:
$S = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$, $S^{-1} = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}$.

- $H' = SH \ge 0$ automatically, since $S \ge 0$. The new cone is *narrower*: the second arrow has
  swung toward the first.
- A cell's new coordinates are $w_i S^{-1} = (w_{i1} - w_{i2},\; w_{i2})$. So $W' \ge 0$ needs
  $w_{i1} \ge w_{i2}$ for **every** cell. One cell near the old $h_2$ edge, say $(0, 2)$, breaks
  it: it falls outside the narrower cone.

*Narrowing is blocked by cells near the edges.* Now swing outward instead, $h'_1 = h_1 - t h_2$
with $t > 0$. The cone gets wider, so every cell stays inside. But entry $j$ of the new arrow is
$h_{1j} - t h_{2j}$, which is negative for every $t > 0$ exactly when $h_{1j} = 0 < h_{2j}$: a gene
made by program 2 and not by program 1. *Widening is blocked by genes that only one program
makes.* Both blocks are made precise in the next section.

## 4 When the factorisation is forced

> **Theorem (separable case).** Let $X = WH$ with $W, H \ge 0$ and $\operatorname{rank} X = K$.
> Suppose
>
> - **(P) pure cells:** for every program $k$ some cell $p_k$ has $w_{p_k} = \alpha_k e_k$,
>   $\alpha_k > 0$;
> - **(M) marker genes:** for every program $k$ some gene $j_k$ has column
>   $H_{:, j_k} = \beta_k e_k$, $\beta_k > 0$.
>
> Then every non-negative factorisation $X = W'H'$ with $K$ programs is $H' = DPH$,
> $W' = WP^\top D^{-1}$, for a permutation $P$ and a positive diagonal $D$: the same programs,
> relabelled and rescaled.

Relabelling and rescaling are always possible, so this is as unique as an NMF can be. By section
2, $H' = SH$ and $W' = WS^{-1}$ for some invertible $S$; the proof shows the two pins force $S$
into that shape.

??? note "Step 1 — pure cells give $S^{-1} \ge 0$ (inside pin)"
    The pure cell's row of $W'$ is $w_{p_k} S^{-1} = \alpha_k\, e_k S^{-1}$, which is $\alpha_k$
    times row $k$ of $S^{-1}$. It must be $\ge 0$ and $\alpha_k > 0$, so row $k$ of $S^{-1}$ is
    non-negative. A pure cell for every program gives $S^{-1} \ge 0$.

    Geometrically: $H = S^{-1}H'$ writes each old arrow as a non-negative combination of the new
    ones, so $\mathrm{cone}(H) \subseteq \mathrm{cone}(H')$. The pure cell sits *on* the arrow
    $h_k$, and every cell has to be inside every valid cone.

??? note "Step 2 — marker genes give $S \ge 0$ (outside pin)"
    Column $j_k$ of $H' = SH$ is $S\,H_{:,j_k} = \beta_k\,(\text{column } k \text{ of } S)$. It must
    be $\ge 0$, so column $k$ of $S$ is non-negative; markers for every program give $S \ge 0$.

    The same thing seen another way: transpose. $X^\top = H^\top W^\top$ swaps the roles — genes
    become the points (in cell space), columns of $W$ become the arrows, and a marker gene is a
    *pure point*. Step 1 then applies verbatim with $W$ and $H$ exchanged.

    Geometrically: marker genes make the wedge *equal* to $\mathrm{cone}(H)$ — a vector in
    $\mathrm{row}(X)$ with no negative entries has its $h$-coordinates readable at the marker genes,
    hence non-negative. So $\mathrm{cone}(H') \subseteq \mathrm{cone}(H)$.

??? note "Step 3 — a non-negative matrix with a non-negative inverse is monomial"
    Suppose $S \ge 0$ and $S^{-1} \ge 0$.

    1. For $i \ne j$, $\sum_m (S^{-1})_{im} S_{mj} = 0$ with every term $\ge 0$, so every term is
       zero.
    2. Fix row $m$ of $S$; it is not zero, so pick $l$ with $S_{ml} > 0$. By 1 with $j = l$,
       $(S^{-1})_{im} = 0$ for all $i \ne l$. Column $m$ of $S^{-1}$ is not zero either, so
       $(S^{-1})_{lm} > 0$.
    3. If also $S_{ml'} > 0$ for some $l' \ne l$, the same argument gives $(S^{-1})_{lm} = 0$ —
       contradiction. So row $m$ of $S$ has exactly one positive entry, at a column $\sigma(m)$.
    4. If $\sigma(m) = \sigma(m')$ with $m \ne m'$, two rows of $S$ are multiples of the same unit
       vector and $S$ is singular. So $\sigma$ is a permutation, and $S = DP$.

    The deeper reading: these are exactly the invertible linear maps that send the non-negative
    orthant onto itself — its symmetries. Without assumptions, the valid $S$ are
    $\{S : SH \ge 0,\ WS^{-1} \ge 0\}$; the two pins cut that set down to the orthant's symmetries.

The conditions are sufficient, not necessary: weaker "sufficiently scattered" conditions also give
uniqueness (Fu et al. 2019 survey).

??? question "Exercise — two genuinely different NMFs"
    Let $X = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$. Find two non-negative factorisations
    with $K = 2$ that are not related by a permutation and scaling. For each, which pin is
    missing?

    ??? tip "Answer"
        $X = X \cdot I$ and $X = I \cdot X$, i.e. $(W, H) = (X, I)$ and $(W', H') = (I, X)$, related
        by $S = X$, which is not monomial. The first has marker genes ($H = I$) but no pure cells;
        the second has pure cells ($W' = I$) but no marker genes. Each pair satisfies one pin,
        never both — as the theorem requires.

## 5 Why activity programs are the hard case

An activity program never appears alone: a dividing cell is still some cell type. So there is no
pure cell for it, and the inside pin is missing for that arrow. It can tilt toward the identity
programs it always co-occurs with, absorbing some of their genes or leaking some of its own. This
is the geometry behind the paper's observation that the activity program is recovered in about 30%
to 100% of simulations as its signal strengthens (Kotliar et al., Fig. 2d), while identity
programs are found far more reliably. Note what consensus over many runs can and cannot fix: it
averages out *which local optimum* a run lands in. It cannot restore a pin the data does not
contain.

## 6 A trap: coordinates are not projections

A natural thought: "to leave the cone you must go in a $-h_j$ direction, so $x \in \mathrm{cone}(H)$
iff $\langle x, h_j \rangle \ge 0$ for all $j$." The first half is true about *coordinates* —
outside the cone means some $w_j < 0$. The second half is false, because the $h$'s are not
orthogonal:

$$
\langle x_i, h_j \rangle = \sum_k w_{ik} \langle h_k, h_j \rangle
\quad\Longrightarrow\quad
W = (XH^\top)\, G^{-1}, \qquad G = HH^\top .
$$

Coordinates equal projections only when $G = I$. Counterexample in $\mathbb{R}^2$:
$h_1 = (1, 0)$, $h_2 = (1, 1)$, $x = (0.1, 1)$. Both projections are positive ($0.1$ and $1.1$),
yet $x = -0.9\,h_1 + h_2$ lies outside the cone. Worse, for non-negative vectors every inner
product is $\ge 0$, so the condition rules out nothing at all. The set
$\{x : \langle x, h_k \rangle \ge 0\ \forall k\}$ is a real object — the *dual cone* — and it is
bigger than the cone.

The intuition is exactly right in two settings. In the standard basis, coordinates are
projections, and the orthant equals its own dual. And in the metric
$\langle u, v \rangle_H = a \cdot b$, where $a, b$ are $h$-coordinates, the $h$'s are
orthonormal and the projection test becomes correct — but then $H' = SH$ needs its own metric,
and $H'$ is orthonormal in $\langle \cdot, \cdot \rangle_H$ only when $SS^\top = I$. So the
metric route computes the same thing as coordinates; it cannot see further.

## 7 The loss is a noise model

To fit NMF to real data you minimise a loss. Each of the usual NMF losses is a negative
log-likelihood in disguise, and the likelihood is where the assumptions show.

**Squared error is Gaussian noise with one variance.** If $X_{ij} = (WH)_{ij} + \varepsilon_{ij}$
with $\varepsilon_{ij} \sim \mathcal{N}(0, \sigma^2)$ independent, then

$$
-\log L = \frac{1}{2\sigma^2} \sum_{ij} \big(X_{ij} - (WH)_{ij}\big)^2 + \text{const}.
$$

The mean $(WH)_{ij}$ varies by entry; the variance does not. UMI counts disagree: their variance
grows with the mean, roughly variance $\approx$ mean at low expression.

**KL-divergence is Poisson noise.** With $X_{ij} \sim \mathrm{Poisson}(\lambda_{ij})$,
$\lambda_{ij} = (WH)_{ij}$, each entry having its own mean and observed once:

$$
-\log L = \sum_{ij} \Big[ (WH)_{ij} - X_{ij} \ln (WH)_{ij} \Big] + \sum_{ij} \ln X_{ij}!
$$

Adding the constant $X\ln X - X$ gives the generalised KL divergence
$D(X \,\|\, WH) = \sum_{ij} \big[X_{ij} \ln \tfrac{X_{ij}}{(WH)_{ij}} - X_{ij} + (WH)_{ij}\big] \ge 0$,
zero only at $WH = X$. Poisson maximum likelihood and "KL-NMF" are the same fit.

**How each treats a count.** Expand one Poisson term around its minimum $\lambda = x > 0$: the
first derivative $1 - x/\lambda$ vanishes there, the second derivative $x/\lambda^2$ equals $1/x$,
so

$$
\lambda - x \ln \lambda \;\approx\; (x - x\ln x) + \frac{(\lambda - x)^2}{2x}.
$$

Locally, the Poisson loss is a Gaussian loss with $\sigma^2 = x$: weighted least squares, weight
$1/x$. A miss of 10 on a count of 1000 costs about as much as a miss of 0.3 on a count of 1. Away
from the minimum the two differ in shape. At $x = 0$ the Poisson term is just $\lambda$, linear,
so small spurious predictions on zeros keep being pushed down, while squared error is flat there.
For $x > 0$ and $\lambda \to 0$ the Poisson term goes to $+\infty$ — you cannot explain an observed
molecule with a rate of zero — while squared error stays finite.

??? question "Exercise — the per-entry minimum"
    Show that $\lambda - x \ln \lambda$ is convex on $\lambda > 0$ and minimised at $\lambda = x$.
    Then explain, from the shape of the two terms, why the Poisson loss is asymmetric around the
    minimum.

## 8 The cNMF patch: variance scaling plus squared error

cNMF divides each gene by its standard deviation $s_j$ across cells and then uses squared error
(Kotliar et al., Methods). With $D = \operatorname{diag}(s_j)$ and $\tilde X = XD^{-1}$,

$$
\|\tilde X - \tilde W \tilde H\|_F^2 = \sum_{ij} \frac{\big(X_{ij} - (\tilde W \tilde H D)_{ij}\big)^2}{s_j^2},
$$

and $H = \tilde H D$ is a non-negativity-preserving relabelling. So the patch is **weighted least
squares with one weight per gene**, $1/s_j^2$; the Poisson loss has **one weight per entry**,
about $1/\lambda_{ij}$.

- **What it gets roughly right.** By the law of total variance,
  $s_j^2 \approx \operatorname{Var}_i(\lambda_{ij}) + \bar\mu_j$: biological spread plus Poisson
  noise at the gene's mean. For a noise-dominated gene $1/s_j^2 \approx 1/\bar\mu_j$ — Poisson's
  weight at the average count. Highly expressed genes no longer dominate.
- **What it misses.** (i) Within a gene, a count of 0 and a count of 200 get the same weight. (ii)
  Library size: if $\lambda_{ij} = c_i \mu_{ij}$, cell $i$'s expected noise contribution is
  $\sum_j \lambda_{ij}/s_j^2 \propto c_i$ under the patch, but
  $\sum_j \lambda_{ij}/\lambda_{ij} = G$ for every cell under Poisson — deep cells get their
  noise fitted. (iii) $s_j^2$ includes the biological signal, so a strongly program-specific gene
  is down-weighted for being informative (softened by cNMF first keeping only the 2000 most
  over-dispersed genes). (iv) Near zero the loss is still flat and symmetric.

Its real advantage is speed: squared error is cheap to optimise. The cNMF code also offers the KL
loss (`beta_loss='kullback-leibler'`).

## 9 Where this goes next

- **Fitting.** The joint problem is not convex — already $f(w, h) = (1 - wh)^2$ has the hyperbola
  $wh = 1$ as its set of minimisers — but it is convex in $H$ for fixed $W$ and vice versa, so
  algorithms alternate. The Lee–Seung multiplicative updates are gradient steps with a per-entry
  step size; the KL version is EM over hidden per-program counts
  $Z_{ijk} \sim \mathrm{Poisson}(w_{ik} h_{kj})$, $X_{ij} = \sum_k Z_{ijk}$.
- **Local optima.** NMF is NP-hard in general (Vavasis) but tractable under separability (Arora et
  al.) — the same condition as section 4. Different runs land in different optima, which is the
  problem cNMF's consensus step addresses.
- **Overdispersion.** UMI counts are better described by a negative binomial,
  variance $\approx \mu + \mu^2/\theta$, which bursty transcription produces directly.

## References

- Kotliar D, Veres A, Nagy MA, Tabrizi S, Hodis E, Melton DA, Sabeti PC. *Identifying gene
  expression programs of cell-type identity and cellular activity with single-cell RNA-Seq.*
  eLife 8:e43803 (2019). Code: <https://github.com/dylkot/cNMF>.
- The following are cited from recall and have not yet been checked. **Unverified.**
  Lee & Seung, *Nature* 1999 and NIPS 2001 (NMF and its multiplicative updates); Donoho & Stodden,
  NIPS 2003 (when NMF gives a correct decomposition into parts); Vavasis, *SIAM J. Optim.* 2009
  (complexity of NMF); Arora, Ge, Kannan & Moitra, STOC 2012 (provable NMF under separability);
  Févotte & Idier, *Neural Computation* 2011 ($\beta$-divergence NMF); Fu, Huang, Sidiropoulos & Ma,
  *IEEE Signal Processing Magazine* 2019 (identifiability survey); Gillis, *Nonnegative Matrix
  Factorization*, SIAM 2020.
