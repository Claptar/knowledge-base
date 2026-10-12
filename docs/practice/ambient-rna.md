# Ambient RNA — practice

Attempts from the session in [topics/ambient-rna.md](../topics/ambient-rna.md), what I could do as
carefully as what I could not. The worked derivations are in
[the ambient-RNA note](../notes/measurement/ambient-rna.md).

## 2026-10-10 — ambient molecules landing in a droplet (1a)

**Problem:** $N_g$ free molecules in a suspension of volume $V_s$, a droplet of volume $V_d$: what is
the distribution of the number $A_g$ that land in the droplet?
**Worked unaided up to:** the binomial mechanism, $A_g \sim \mathrm{Binom}(N_g, V_d/V_s)$, once the
gap in the first attempt was named. **Derived unaided.**
**Where I asked for a hint:** "a mean does not determine a distribution — you need a mechanism".
Le Cam's bound was invoked by name and I had to ask what it was; it was supplied with its coupling
proof. **Not yet derived.**
**Attempt:** first, $\mathbb E A_g = \frac{V_d}{V_s} N_g$, "so" $A_g \sim \mathrm{Poisson}$. Then each
molecule landing independently with probability $p_d$.
**Outcome:** solved, after one hint.
**What it revealed:** Poisson was held as a formula rather than a mechanism — independence plus
rarity. The jump from a mean to a distribution is right in one setting: when the family is already
known to be Poisson, the mean is the whole parameter. The step skipped was showing the family.
**Revisit:** —

## 2026-10-10 — capture by the bead, two routes (1b)

**Problem:** each landed molecule is captured with probability $q$. What is the distribution of
the captured count $C_g$?
**Worked unaided up to:** all of it. The merged route,
$C_g \sim \mathrm{Binom}(N_g, p_d q)$, was my first answer; offered condition-and-sum or
generating functions, I chose to do both ("those techniques sound useful"). **Derived unaided.**
**Where I asked for a hint:** none for the routes. Two checks were pointed at in the transform
route: "what must every MGF equal at $t = 0$?" and "you froze $t = 1$". I found both fixes
myself. "PGF" was used by name before it was defined, and I had to ask.
**Attempt:** wrote the Bernoulli MGF as $qe^t$, dropping the $B = 0$ term; then treated the
transform at $t = 1$ as a number.
**Outcome:** solved.
**What it revealed:** a transform is a function, and one number cannot identify a distribution.
Check: every MGF equals 1 at $t = 0$. Capability shown: closing the loop unprompted — "It's just
an event."
**Revisit:** PGF thinning by composition, $G_A(1 - q + qs)$, for a negative binomial $A$.

## 2026-10-10 — what breaks the Poisson (1c)

**Problem:** which kinds of variation in capture keep the count Poisson, and which do not?
**Worked unaided up to:** a droplet-wide random factor $Q$ behaves like a varying $V_d$ and gives a
mixed Poisson — "we get effectively varying $V_d$ which will result in negative binomial."
**Derived unaided.** after returning to the "$V_d$ constant" thread I had flagged and parked
myself.
**Where I asked for a hint:** the comparison between a fixed per-molecule $q_j$ and a shared
random $Q$ was set up to separate the two cases; "negative binomial *only if* $Q$ is gamma" was
added to my answer.
**Attempt:** first, "if one molecule is better detected than another that would break things".
**Outcome:** solved, with scaffolding.
**What it revealed:** heterogeneity across molecules was conflated with dependence between them.
Le Cam allows unequal $p_i$; what breaks the Poisson is a factor *shared* across molecules. The
intuition is right exactly there — when the difference in detection is a property of the droplet
rather than of the molecule.
**Revisit:** —

## 2026-10-10 — adding the cell, and conditioning on the total (1d, 1e)

**Problem:** with $Y_g \sim \mathrm{Poisson}(\nu_g)$ from the cell and
$C_g \sim \mathrm{Poisson}(\lambda_g)$ from the soup, find $P(\mathbf x \mid T)$ and write it as a
mixture of a cell profile and a soup profile.
**Worked unaided up to:** the multinomial, from the joint PMF. **Derived unaided.** from the PMF on.
**Where I asked for a hint:** the transform route stalled and the PMF was pointed at. The
decomposition into $(1 - \alpha)\mu_g + \alpha a_g$ was given on request after one nudge, and the
per-UMI label argument with it. **Not yet derived.** For 1e, the question was mine — "why is μ a
fraction and not a physical quantity?" — and the factorisation that answers it was given.
**Attempt:** tried the MGF to condition on the sum. In the PMF, wrote
$\prod_i \lambda_i^{x_i} / \sum \lambda$ instead of $\prod_i (\lambda_i / \sum \lambda)^{x_i}$.
**Outcome:** multinomial solved with a correction; decomposition stuck.
**What it revealed:** two things. Transforms build sums (product) and random sums (composition);
conditioning on a sum is neither, so use the joint PMF — the transform instinct is right for
*building*. And "each component must sum to 1" is not yet automatic: the fraction was split, but
neither piece was normalised into a probability vector.
**Revisit:** next session, cold, before Problem 2 step 3 — reproduce the decomposition and the
per-UMI label.

## 2026-10-10 — SoupX: one cell, then pooled (Problem 2, steps 1–2)

**Problem:** given genes $G$ that are off in cell type $C$, estimate $\alpha_i$ for one cell; then
pool the cells of $C$ under a shared $\alpha_c$.
**Worked unaided up to:** both estimators — $X_{iG} \mid T_i \sim \mathrm{Binomial}(T_i, \alpha_i a_G)$
with $\hat\alpha_i = X_{iG}/(T_i a_G)$, and the pooled ratio of sums $X_{CG}/(T_C a_G)$.
**Derived unaided.**
**Where I asked for a hint:** none recorded; two slips in step 2 were corrected.
**Attempt:** the first pooled estimator was missing a $T_i$ factor; a later one carried an extra
$n_c$ when $T_C$ was already a sum over cells.
**Outcome:** solved, with corrections.
**What it revealed:** index and aggregation bookkeeping — the second and third such slips of the
session, after the multinomial exponent. The ideas were right each time. Prompt: "what is already
summed over on this line?" Capability shown: "if we assume $\alpha_c$ instead of $\alpha_i$ it
means that $V_c$ is the same for cells of celltype c which is obviously questionable assumption."
**Revisit:** write next to each line what every index ranges over.

## 2026-10-10 — SoupX: bias when the genes are not quite off (Problem 2, step 3)

**Problem:** let $\mu_{ig} = \varepsilon_g$ instead of 0. What is $\mathbb E[\hat\alpha_c]$, and what
does the bias say about choosing $G$?
**Worked unaided up to:** the bias,
$\mathbb E[\hat\alpha_c] = \alpha_c + (1 - \alpha_c)\varepsilon_G / a_G$. **Derived unaided.**
**Where I asked for a hint:** —
**Attempt:** as above; the interpretation not yet started.
**Outcome:** computed; interpretation open.
**What it revealed:** —
**Revisit:** next session — the relative bias, which two quantities it compares, and the
gene-selection criterion that follows.
