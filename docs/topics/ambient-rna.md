# Ambient RNA — what lets a tool tell soup from cell?

**Status:** open
**Opened:** 2026-10-10  **Last touched:** 2026-10-10

Practice: [practice/ambient-rna.md](../practice/ambient-rna.md) · Material:
[the ambient-RNA note](../notes/measurement/ambient-rna.md) · Sources:
[resources/ambient-rna.md](../resources/ambient-rna.md)

## The question that opened it

I wanted to understand how ambient RNA is modelled — in general, and in five tools specifically:
SoupX, DecontX, CellBender, souporcell and CellSweep.

What it forced: all five fit some version of one multinomial mixture,
$\mathbf x_i \mid T_i \sim \mathrm{Mult}\big(T_i, (1-\alpha_i)\boldsymbol\mu_i + \alpha_i \mathbf a\big)$,
and from one droplet it is not identifiable — $\alpha_i = 0$, $\boldsymbol\mu_i = \mathbf x_i/T_i$
always wins. So each tool is an answer to *what side information breaks the degeneracy?* (§0 of
[the note](../notes/measurement/ambient-rna.md#0-the-shared-model-and-why-one-droplet-cannot-fix-it)).
That framing was the mentor's; it organised all five tools and I kept using it.

Two questions then carried the session:

- Where does that multinomial come from physically? (Problem 1.)
- My own, unprompted: **"why is μ a fraction and not a physical quantity?"** It led to the most
  useful structural point of the session — the Poisson factorises exactly into a scale term and a
  composition term, and conditioning on $T$ throws away the ambient *amount*, which is the physical
  quantity ([note §1e](../notes/measurement/ambient-rna.md#1e-why-fractions-and-not-rates)).

## Attached to

- **EM for mixtures, and HMMs (Durbin).** At the molecule level this is a two-component mixture
  with a latent per-UMI source label; CellSweep is literally that EM.
- **MGFs** — my default transform. PGFs were new this session and arrived as the same object in
  other coordinates, $M_X(t) = G_X(e^t)$; the $\ln$ in the MGF composition rule
  $M_C(t) = M_A(\ln M_B(t))$ is the trace of that change of variable.
- **Daily 10x QC.** The kb vs Cell Ranger artefacts in empty droplets (Gorin & Goodman 2026) bear
  directly on FASTQ → kb work.
- Not an anchor: **Le Cam's bound** was invoked by name and had to be supplied — see *Still loose*.

## Where else this shows up

From the session's anchors; the outbound question was not asked separately.

- **The CME.** PGFs are the main tool for the CME and telegraph derivations: thinning is
  $G(1-q+qs)$, a random sum is composition, and $n \to n-1$ becomes multiplication by $s$ —
  [path node 9](../path.md#9-generating-functions). This was the first real use of them.
- **The measurement layer.** Problem 1 is a small instance of
  [path node 17](../path.md#17-technical-noise-as-a-thinning-layer): capture is a thinning, and
  ambient RNA is a second Poisson source passed through the same thinning.
- **Overdispersion.** A droplet-wide random factor turns the Poisson into a mixed Poisson, and the
  negative binomial only if that factor is gamma — the same object as the NB fitted daily.

## How I could have come up with this

- **Thinning keeps a Poisson.** "It's just an event." The precise version: a captured molecule is
  a compound event — lands *and* is captured — still independent across molecules and still rare,
  so Le Cam applies again.
- **SoupX.** "so the idea is to estimate $\alpha_i$ through the 'ground truth'" — genes known to be
  off in a cell type. Partial: says what SoupX uses, not yet why that choice was forced.
- **The mixture decomposition and the per-UMI label.** *Not yet* — both were given on request.
  Prompt for next time: starting from $p_g \propto \nu_g + \lambda_g$, what has to be true of each
  piece for the sum to read as "pick a source, then pick a gene"?

## Still loose

- **Cold-check owed before building on it:** reproduce
  $p_g = (1-\alpha)\mu_g + \alpha a_g$ and the per-UMI label argument without looking. Both were
  given after one nudge — the step that wasn't automatic was normalising each piece into a
  probability vector. **Not yet derived.**
- Le Cam's bound and its coupling proof were supplied. **Not yet derived.**
- **Problem 2, step 3 — interpretation.** I computed
  $\mathbb E[\hat\alpha_c] = \alpha_c + (1-\alpha_c)\varepsilon_G/a_G$ but have not read it yet:
  write the *relative* bias, say which two quantities it compares, and from that decide what makes
  a good or a bad gene set $G$ for a cell type $C$, in biological terms.
- **Problem 2, step 4.** If $\alpha_i \approx \Lambda/T_i$, what does the pooled ratio-of-sums
  estimator actually estimate, and what happens when that single value is applied to every cell in
  $C$?
- **Problems 3–5, set but not started.**
  - *CellSweep.* Write the E-step responsibilities for one UMI of gene $g$ in cell $i$ across the
    three sources (cell type, ambient, bulk). Why are the E- and M-steps closed form here, and what
    does CellBender's VAE destroy that makes them not closed form?
  - *souporcell.* Why is $\rho$ identifiable from allele counts when it is not from expression?
    Which biological phenomenon would quietly break it? Model: observed allele fraction
    $= (1-\rho)\,g_{kl} + \rho\,\bar a_l$ with $g_{kl} \in \{0, \tfrac12, 1\}$ and one global
    $\rho$.
  - *Benchmarks.* List the design choices that could make scAR look best in one benchmark and
    pathological in another — the April 2026 preprint and GSE337237 disagree on exactly this
    ([resources](../resources/ambient-rna.md#benchmarks)).
- **CellBender.** Does the Supplementary Methods justify the gamma behind its NB, or assume it, and
  how is its scale term used? Its model is written in the note structurally, not from the
  supplement. **Unverified.**
- **CellSweep.** Is idempotency necessary, sufficient, either? Its expected-profile equation did
  not render in the fetched text — check the paper. **Unverified.**
- **$\alpha_i \approx \Lambda/T_i$** from the empties' totals assumes $\Lambda$ is the same with a
  cell present; displaced volume and competition for capture could change it. **Unverified.**
- **A test on my own data:** cross-gene correlation in empty droplets as the signature of a shared
  droplet factor, as opposed to per-gene overdispersion. Could be checked on our 10x runs.
- Practice owed: negative-binomial thinning by PGF composition (one line), and Poisson thinning by
  PGFs.
- Traps hit, with what each revealed: [practice/ambient-rna.md](../practice/ambient-rna.md).

## Derived / proved myself

- 2026-10-10 — the ambient count is $\mathrm{Binom}(N_g, p_d) \approx \mathrm{Poisson}(p_d N_g)$,
  from each molecule landing independently with probability $p_d = V_d/V_s$.
  **Derived unaided.** once "a mean does not fix a distribution" was named; Le Cam's bound was
  supplied.
- 2026-10-10 — capture: merge landing and capture into one event,
  $C_g \sim \mathrm{Binom}(N_g, p_d q)$. My first answer. **Derived unaided.**
- 2026-10-10 — the same Poisson by both routes, condition-and-sum and transforms; I chose to do
  both ("those techniques sound useful"). **Derived unaided.** Two slips in the transform route —
  the Bernoulli MGF written as $qe^t$, and $t$ frozen at 1 — I found and fixed myself after a check
  ("what must every MGF equal at $t = 0$?").
- 2026-10-10 — a shared droplet factor acts like a varying droplet volume and makes the count a
  mixed Poisson: "we get effectively varying $V_d$ which will result in negative binomial."
  **Derived unaided.** after returning to the "$V_d$ constant" thread I had parked myself; the
  qualification "negative binomial only if the factor is gamma" was added.
- 2026-10-10 — conditioning independent Poissons on their total gives the multinomial.
  **Derived unaided.** from the joint PMF on, once it was pointed out that transforms build sums
  rather than condition on them; a missing exponent on the denominator was corrected.
- 2026-10-10 — SoupX for one cell: collapse to $\mathrm{Binomial}(T_i, \alpha_i a_G)$ and
  $\hat\alpha_i = X_{iG}/(T_i a_G)$. **Derived unaided.**
- 2026-10-10 — SoupX pooled: the shared-$\alpha_c$ MLE is a ratio of sums, $X_{CG}/(T_C a_G)$.
  **Derived unaided.** with two bookkeeping slips corrected (a missing $T_i$, an extra $n_c$ on an
  already-summed $T_C$). In my words: "if we assume $\alpha_c$ instead of $\alpha_i$ it means that
  $V_c$ is the same for cells of celltype c which is obviously questionable assumption".
- 2026-10-10 — the bias under leaky expression,
  $\mathbb E[\hat\alpha_c] = \alpha_c + (1-\alpha_c)\varepsilon_G/a_G$. **Derived unaided.** The
  reading of it is still open.
