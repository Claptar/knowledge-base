# Ambient RNA: the likelihood from the physics, and SoupX's estimator

> **Written with an AI assistant.** Written by me with Claude from the study session of
> 2026-10-10. It is *material*, not evidence of understanding: what I derived, what was given to
> me, and where I went wrong are recorded in [topics/ambient-rna.md](../../topics/ambient-rna.md)
> and [practice/ambient-rna.md](../../practice/ambient-rna.md). The one step I have not derived is
> folded so it can be tried first. Sources and their DOIs are in
> [resources/ambient-rna.md](../../resources/ambient-rna.md).

**The question.** Every ambient-RNA tool fits some version of one model. Where does that model come
from physically, why can it not be fitted from one droplet, and what does each tool add to make it
fittable? Section 2 works through the simplest answer, SoupX, as far as its bias.

---

## 0 The shared model, and why one droplet cannot fix it

$$
\mathbf{x}_i \mid T_i \sim \mathrm{Mult}\!\left(T_i,\ (1-\alpha_i)\,\boldsymbol{\mu}_i + \alpha_i\,\mathbf{a}\right)
$$

| Symbol | Meaning |
| --- | --- |
| $\mathbf x_i$, $T_i$ | counts of droplet $i$ over genes, and their total |
| $\boldsymbol\mu_i$ | native profile — the cell's own composition, as seen through capture |
| $\mathbf a$ | ambient profile — the soup's composition, as seen through capture |
| $\alpha_i$ | contamination fraction |

CellBender and CellSweep add a third, swapping or bulk component. From one droplet the model is
**not identifiable**: $\alpha_i = 0$, $\boldsymbol\mu_i = \mathbf x_i / T_i$ always maximises the
likelihood. So each tool is an answer to *what side information breaks the degeneracy?*

1. Empty droplets fix the **shape** of $\mathbf a$ — not the amount.
2. Genes known to be off in a cell type fix $\alpha$ (SoupX).
3. Cells of one type share $\boldsymbol\mu$, so contamination is the shift toward $\mathbf a$
   (DecontX, CellSweep).
4. $\boldsymbol\mu_i$ lives on a low-dimensional manifold — a VAE prior (CellBender, scAR).
5. Native allele fractions are discrete, $\{0, \tfrac12, 1\}$; ambient pulls them toward the pool
   average (souporcell).

---

## 1 Where the likelihood comes from

### 1a Ambient molecules landing in a droplet

$N_g$ free molecules of gene $g$ in a suspension of volume $V_s$; a droplet of volume $V_d$. A mean
alone, $\mathbb E A_g = \frac{V_d}{V_s} N_g$, does not fix a distribution — the mechanism does.
Each molecule lands in the droplet with probability $p_d = V_d / V_s$, so

$$
A_g \sim \mathrm{Binom}(N_g,\ p_d) \;\approx\; \mathrm{Poisson}(p_d N_g).
$$

"Uniformly distributed" hides two assumptions:

- **marginal** — each molecule lands with probability $p_d$;
- **independence** — molecules land independently of each other. This is what the binomial needs,
  and what would fail if transcripts travelled in clumps (membrane debris, say).

Physical check: a droplet is $\lesssim 1$ nL against tens of µL loaded, so $p_d \sim 10^{-5}$.

**Le Cam's bound.** For independent $X_i \sim \mathrm{Bernoulli}(p_i)$, $S = \sum_i X_i$ and
$\lambda = \sum_i p_i$,

$$
d_{TV}\big(\mathcal L(S),\ \mathrm{Poisson}(\lambda)\big)\le \sum_i p_i^2 \qquad(\text{equal } p:\ Np^2=\lambda p).
$$

Some sources carry a factor 2: the $\ell_1$ convention.

??? note "Proof idea — coupling"
    Couple each $\mathrm{Bernoulli}(p_i)$ with a $\mathrm{Poisson}(p_i)$ so that they disagree with
    probability at most $p_i^2$. The sum of the Poissons is exactly $\mathrm{Poisson}(\lambda)$,
    and a union bound over $i$ gives the result.

Consequences:

- no $N \to \infty$ is needed — it is a finite-sample statement;
- the $p_i$ may differ — **uniformity is barely needed; independence and rarity carry the weight.**

### 1b Capture by the bead

**Merged route.** Each molecule lands *and* is captured with probability $p_d q$:

$$
C_g \sim \mathrm{Binom}(N_g,\ p_d q)\approx \mathrm{Poisson}(p_d q N_g).
$$

**Route (a) — condition and sum**, with $\lambda = p_d N_g$:

$$
P(C_g=x)=\sum_{i\ge x}\binom{i}{x}q^x(1-q)^{i-x}e^{-\lambda}\frac{\lambda^i}{i!}
=e^{-\lambda}\frac{(\lambda q)^x}{x!}\sum_{m\ge0}\frac{(\lambda(1-q))^m}{m!}
=e^{-\lambda q}\frac{(\lambda q)^x}{x!}.
$$

It works only because a binomial inside a Poisson telescopes into the exponential series — a
coincidence of the pair.

**Route (b) — transforms.** $C_g = \sum_{j=1}^{A_g} B_j$ with $B_j \sim \mathrm{Bernoulli}(q)$:

$$
\varphi_B(t)=1-q+qe^t,\qquad \varphi_A(t)=e^{\lambda(e^t-1)},
$$

$$
\mathbb E[e^{tC}\mid A=n]=\varphi_B(t)^n,\qquad
\mathbb E[e^{tC}]=\varphi_A\big(\ln\varphi_B(t)\big)=e^{\lambda q(e^t-1)}\ \Rightarrow\ C_g\sim\mathrm{Poisson}(\lambda q).
$$

The general law for **random sums** holds for any $A$ and $B$. In PGF coordinates it needs no
logarithm:

$$
G_C(s)=G_A\big(G_B(s)\big)=G_A(1-q+qs)\quad(\text{thinning}).
$$

Thinning a Poisson gives a Poisson **exactly**, not approximately.

Why it had to work: a captured molecule is just another event — a compound one, still independent
across molecules and still rare — so Le Cam applies again.

### PGF, MGF and characteristic function

The same object in different coordinates: $M_X(t) = G_X(e^t)$ and $\varphi_X(t) = G_X(e^{it})$.
For counts, $s$ is the natural variable:

- **The distribution is the series:** $p_k = G^{(k)}(0)/k!$. Numerically, evaluate $G$ on the unit
  circle and apply an FFT — the way Pachter-lab papers get PMFs for bursty and telegraph models
  from a closed-form $G$.
- **It always exists** for $|s| \le 1$. The MGF can fail for heavy tails; the CF is just $G$ on the
  unit circle.
- **Counting operations become algebra:** a sum is a product; thinning is $G(1-q+qs)$; a random
  sum is composition. In the CME, multiplying by $n$ becomes $s\,\partial_s$ and the shift
  $n \to n-1$ becomes multiplication by $s$, so the master equation becomes one linear PDE — the
  learning path's [node 9](../../path.md#9-generating-functions).
- **Factorial moments:** $G^{(k)}(1) = \mathbb E[X(X-1)\cdots(X-k+1)]$; a Poisson gives
  $\lambda^k$.
- **Why the $\ln$ appeared in route (b):** $M = G \circ \exp$, so the composition rule reads
  $M_C(t) = M_A(\ln M_B(t))$.

The MGF is natural for continuous variables, cumulants and Chernoff bounds; the CF for proofs over
all distributions (CLT, Lévy continuity) and for Fourier inversion of densities.

### 1c What breaks the Poisson

| Variation | Effect |
| --- | --- |
| **Molecule to molecule:** a fixed capture $q_j$ (length, poly-A, sequence) | Harmless: still $\mathrm{Poisson}\big(\sum_j p_d q_j\big)$ — only the mean changes |
| **Droplet to droplet:** a shared random factor $Q$ (bead efficiency), or a varying $V_d$ | Given $Q$, $\mathrm{Poisson}(\lambda Q)$. Marginally the molecules are positively correlated through $Q$, independence fails, and the count is a **mixed Poisson** |

- A negative binomial arises **only if** $Q$ (or $V_d$) is gamma — chosen for the closed form
  (gamma–Poisson conjugacy), not forced by the physics. CellBender's NB plausibly comes from here;
  whether its supplement argues for the gamma or assumes it is an open thread in the topic file.
- A testable signature of a shared droplet factor is **correlation across genes** in empty
  droplets, not just per-gene overdispersion.

### 1d Adding the cell, and conditioning on the total

Cell: $Y_g \sim \mathrm{Poisson}(\nu_g)$; soup: $C_g \sim \mathrm{Poisson}(\lambda_g)$; all
independent. Then $X_g = Y_g + C_g \sim \mathrm{Poisson}(\nu_g + \lambda_g)$ (a product of
transforms) and $T = \sum_g X_g$.

Transforms build sums; they do not condition on one. The joint PMF does:

$$
P(\mathbf x\mid T)=\frac{\prod_g e^{-m_g}m_g^{x_g}/x_g!}{e^{-\sum m}\,(\sum m)^T/T!}
=\binom{T}{x_1,\dots,x_G}\prod_g\left(\frac{m_g}{\sum_h m_h}\right)^{x_g},\qquad m_g=\nu_g+\lambda_g.
$$

**Try before opening:** write $p_g = m_g / \sum_h m_h$ as a mixture of two *probability vectors*,
one for the cell and one for the soup. With $V = \sum_g \nu_g$ and $\Lambda = \sum_g \lambda_g$:

??? question "The decomposition"
    $$
    p_g=\frac{\nu_g+\lambda_g}{V+\Lambda}
    =\underbrace{\frac{V}{V+\Lambda}}_{1-\alpha}\cdot\underbrace{\frac{\nu_g}{V}}_{\mu_g}
    +\underbrace{\frac{\Lambda}{V+\Lambda}}_{\alpha}\cdot\underbrace{\frac{\lambda_g}{\Lambda}}_{a_g}.
    $$

What each piece is:

- $\mu_g$ — the cell's native composition, as seen through capture.
- $a_g$ — the soup's composition, as seen through capture. In an empty droplet $V = 0$, so
  $p_g = a_g$ exactly — why every tool estimates $\mathbf a$ from empties.
- $\alpha = \Lambda / (V + \Lambda)$ with $\Lambda = p_d q \sum_g N_g$ — set by droplet volume,
  soup concentration and capture, not by the cell. **The physical quantity is the ambient
  *amount* $\Lambda$; the fraction is derived.** Small cells get a larger $\alpha$, so a global
  $\rho$ (SoupX's default, souporcell) is mis-specified when cell sizes vary.

Three tests of the parametrisation:

- $\nu_g, \lambda_g \to Q\nu_g, Q\lambda_g$: **$Q$ cancels.** Conditioning on $T$ removes
  droplet-wide factors — bead efficiency, depth.
- $V_d$ scales $\Lambda$ but not $V$, so it does **not** cancel. It appears as per-cell variation
  in $\alpha_i$ — one physical justification for a per-cell $\alpha_i$ (DecontX, CellSweep).
- A gene-specific $q_g$ multiplies both $\nu_g$ and $\lambda_g$, so it enters $\mu$ and $a$
  identically and is measured consistently in empties — harmless.

??? question "The per-UMI label"
    Each counted molecule independently comes from the cell with probability $V / (V + \Lambda)$ or
    from the soup with probability $\Lambda / (V + \Lambda)$, and is then gene $g$ with probability
    $\mu_g$ or $a_g$. That per-UMI label $z$ is the latent variable DecontX and CellSweep do
    inference on.

### 1e Why fractions and not rates

The exact factorisation of independent Poissons:

$$
\prod_g\mathrm{Pois}(x_g;\nu_g+\lambda_g)=\underbrace{\mathrm{Pois}(T;V+\Lambda)}_{\text{scale}}\cdot
\underbrace{\mathrm{Mult}(\mathbf x;T,\mathbf p)}_{\text{composition}}.
$$

- The composition term sees only ratios, so a model built on it can estimate only $\mu$, $a$ and
  $\alpha$.
- $\nu_g = q_g n_g$ is not physical either: without spike-ins, capture and molecule number are
  confounded.
- **The cost:** $T$ is not pure nuisance. If $\Lambda$ is roughly constant, estimate it from the
  empties' totals; then $\alpha_i \approx \Lambda / T_i$. Conditioning on $T$ throws away exactly
  the "amount, not fraction" information. Caveat: $\Lambda$ with a cell present may differ —
  displaced volume, competition for capture.
- **CellBender does not condition.** It models raw counts with absolute means: a cell-size term
  times the native profile, plus an empty-size term times the ambient profile, with a prior on the
  empty size fitted from empties. (Written structurally; not checked against its Supplementary
  Methods.) SoupX, DecontX and CellSweep work in compositional coordinates.

---

## 2 SoupX's contamination estimator

Side information: a gene set $G$ not expressed in cell type $C$, $\mu_{ig} = 0$ for $g \in G$ and
$i \in C$ — haemoglobin genes in non-erythroid cells, immunoglobulin genes in non-B cells. Notation
map to the paper: $\rho_c \leftrightarrow \alpha_i$, $b_g \leftrightarrow a_g$,
$N_c \leftrightarrow T_i$.

### Step 1 — one cell

Collapse the multinomial onto "in $G$" and "not in $G$". With $a_G = \sum_{g \in G} a_g$:

$$
X_{iG}\mid T_i\sim\mathrm{Binomial}(T_i,\ \alpha_i a_G),\qquad \hat\alpha_i=\frac{X_{iG}}{T_i\,a_G}.
$$

- The MLE exists for a single cell ($k/n$); the problem is **variance** — $X_{iG}$ is typically a
  handful of counts.
- $\mu_{ig} = 0$ is an *assumption*, not a measurement, and the estimator is only as good as it.

### Step 2 — pooling with a shared $\alpha_c$

With $p = \alpha_c a_G$, the log-likelihood is
$\ell = \sum_{i \in C}\big[X_{iG}\ln p + (T_i - X_{iG})\ln(1-p)\big] + \text{const}$, so

$$
\hat\alpha_c=\frac{X_{CG}}{T_C\,a_G},\qquad X_{CG}=\sum_{i\in C}X_{iG},\quad T_C=\sum_{i\in C}T_i.
$$

- Shortcut: binomials with a shared $p$ add up to one binomial,
  $X_{CG} \sim \mathrm{Bin}(T_C, \alpha_c a_G)$ — the cells behave as one big cell.
- A **ratio of sums**, not a mean of ratios: each molecule counts once, so large cells weigh more;
  a mean of ratios lets the noisy small-$T$ cells dominate the variance.
- A shared $\alpha_c$ implies an equal $V$ across the cells of $C$, given a fixed $\Lambda$ — a
  questionable assumption.

### Step 3 — bias when the genes are not quite off

Let $\mu_{ig} = \varepsilon_g$ and $\varepsilon_G = \sum_{g \in G} \varepsilon_g$. Then

$$
\mathbb E[X_{CG}]=T_C\big[(1-\alpha_c)\varepsilon_G+\alpha_c a_G\big]
\ \Rightarrow\
\mathbb E[\hat\alpha_c]=\alpha_c+(1-\alpha_c)\frac{\varepsilon_G}{a_G}.
$$

The bias is positive, so SoupX **overestimates** contamination and over-corrects: native $G$ counts
are booked as soup, and dividing by $a_G$ converts them into units of $\alpha$.

### Open — not yet worked

- **Step 3, read.** Write the *relative* bias $(\mathbb E[\hat\alpha_c] - \alpha_c)/\alpha_c$. Which
  two quantities does it compare? What, in biological terms, makes a good or a bad gene set $G$ for
  a cell type $C$?
- **Step 4.** If $\alpha_i \approx \Lambda / T_i$, what does the pooled ratio-of-sums estimator
  actually estimate, and what happens when that single value is applied to every cell in $C$?

---

## 3 The five tools at a glance

> **Unverified.** Read from the papers by the assistant during the session, not checked by me.
> CellSweep's expected-profile equation did not render in the fetched text, and CellBender's model
> is written structurally — both are open threads in the topic file.

| Tool | Native $\boldsymbol\mu_i$ | Ambient $\mathbf a$ from | Amount | Inference | Output |
| --- | --- | --- | --- | --- | --- |
| SoupX | cluster-level | low-UMI barcodes | global $\rho$ (or per-cell) | moment estimator | subtracted counts |
| DecontX | cluster-level | mixture of *other* clusters (newer versions can use empties) | per-cell, Beta prior | variational | corrected counts |
| CellBender | per-cell, VAE decoder | learned jointly from the raw matrix | per-droplet amount + global swapping | SVI (Pyro), amortised | FPR-controlled counts (`--fpr`) + cell calls |
| souporcell | genotype per cluster | experiment-average allele fraction | single global $\rho$ | mixture clustering + Stan | assignments, doublets, $\rho$; no corrected counts |
| CellSweep | cluster-level, labels fixed up front (CellTypist) | empties (or a mixture of clusters) | per-cell $\alpha_i$ + global bulk $\beta$ | closed-form EM | corrected counts + $\alpha_i$ as QC |

- **SoupX** — a moment estimator on one biological assumption; `autoEstCont` exists because "off"
  may be "low".
- **DecontX** — the ambient profile is built from observed clusters, so it breaks when the soup's
  composition differs from the captured composition (mitochondrial transcripts over-represented in
  the soup, for instance).
- **CellBender** — cell calling and ambient removal as one inference; the VAE prior stops
  $\boldsymbol\mu_i$ absorbing $\mathbf a$. The output is not the posterior mean but an
  FPR-controlled estimate, so "removes the fewest counts" partly reflects a chosen operating point.
- **souporcell** — a demultiplexer, for which ambient RNA is a nuisance it must model. The
  strongest identifiability of the five, but only a global $\rho$. Its main value here is as a
  ruler for the other tools.
- **CellSweep** — DecontX's mixture, plus an ambient profile pinned from empties, plus a bulk term,
  fitted by exact EM. Watch: fixed labels remove the within-cluster heterogeneity that points
  toward $\mathbf a$; the benchmarks are self-reported and treat "removes more" as better; it
  recommends the alternative model below 10,000 non-cellular barcodes.
