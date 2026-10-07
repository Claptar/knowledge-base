# NMF — practice

Attempts from the session in [topics/nmf.md](../topics/nmf.md), what I could do as carefully as
what I could not.

## 2026-10-06 — every factorisation of the same $X$

**Problem:** given $X = WH$ with $\operatorname{rank} X = K$, characterise every other exact
factorisation $X = W'H'$ with $K$ programs.
**Worked unaided up to:** the whole characterisation — $H' = SH$, $W = W'S$, another factorisation
exists iff $S$ is invertible. **Derived unaided.**
**Where I asked for a hint:** the dimension sandwich
($K = \dim \mathrm{row}(X) \le \dim \langle h \rangle \le K$) was supplied as a first move;
"collect the coefficients into a matrix" named the technique.
**Attempt:** wrote each cell in both bases and compared coefficients, using that coordinates in a
basis are unique.
**Outcome:** solved.
**What it revealed:** change-of-basis reasoning is live. Two slips with one root each: "S should be
orthogonal" — PCA's orthonormal *convention* held as a fact about the problem; and the transposed
$2 \times 2$ matrix — my [change-of-basis note](../notes/linear-algebra/change-of-basis.md) puts a
new vector's coordinates in a *column* ($e' = eC$), while programs here are stacked as *rows*, so
$S = C^\top$ (checked against the note, 2026-10-06).
**Revisit:** whenever basis vectors are stacked as rows, write the shape next to the equation.

## 2026-10-06 — which $S$ survive $W, H \ge 0$

**Problem:** for the shear $h'_2 = h_1 + h_2$, when does $W' = WS^{-1}$ stay non-negative; then,
what stops an arrow swinging outward.
**Worked unaided up to:** cells lie in $\mathrm{cone}(H)$ ("it's really inside of the cone"), and
an outward swing $h_1 - t h_2$ is blocked by a gene with $h_{1j} = 0$. **Derived unaided.** — the
condition $h_{2j} > 0$ was missing.
**Where I asked for a hint:** the cone picture was supplied after the session jumped from algebra
to cones without a route — a session failure, not a gap; the second constraint, $H' \ge 0$, was
pointed at.
**Attempt:** read $W' \ge 0$ as containment of the cells in the new cone.
**Outcome:** solved, with scaffolding.
**What it revealed:** once the objects were named, the geometry was immediate ("I see it from the
picture"). What was missing was the motivation for caring about $S$ at all.
**Revisit:** —

## 2026-10-06 — a pure cell pins the cone from inside

**Problem:** show that a pure cell for program $k$ forces row $k$ of $S^{-1}$ to be non-negative.
**Worked unaided up to:** $\alpha (S^{-1})_{kl} \ge 0$ for every $l$, by my own route.
**Derived unaided.** — I did not recognise it as the result until it was pointed out.
**Where I asked for a hint:** how to compute in a non-standard inner product (the recipe from
$e$-components to $h$-coordinates was supplied).
**Attempt:** first, "$w_{ij} \ge 0 \Leftrightarrow \langle x_i, h_j \rangle \ge 0$ … to get outside
of the cone you have to go in at least one $-h_j$ direction, no?" — which gave an angle bound
instead of an inclusion. Then built the inner product in which the $h$'s are orthonormal, so that
projections become coordinates, and pushed the pure cell through it.
**Outcome:** solved unconvincingly, then solved.
**What it revealed:** the orthonormal reflex, second appearance — so a pattern. Coordinates are
(projections)$\cdot G^{-1}$ with $G = HH^\top$; the inner-product condition describes the *dual*
cone, and for non-negative vectors it is vacuous. The intuition is exactly right in the
$e$-basis, where the orthant is its own dual — which is where it was learned. Capability shown:
changing the metric until the intuition became true.
**Revisit:** whenever a basis appears — is it orthonormal? If not, what computes coordinates?

## 2026-10-06 — marker genes pin the cone from outside

**Problem:** show that marker genes for every program force $S \ge 0$.
**Worked unaided up to:** complete, by transposing: $X^\top = H^\top W^\top$ makes a marker gene a
pure point in cell space, so the previous problem applies with $W$ and $H$ swapped.
**Derived unaided.**
**Where I asked for a hint:** none.
**Attempt:** as above; the index came out as $S_{kl}$ where $W = W'S$ gives $S_{lk}$.
**Outcome:** solved.
**What it revealed:** seeing the symmetry — cleaner than the gene-entry route that was proposed.
Row/column bookkeeping again.
**Revisit:** —

## 2026-10-06 — non-negative with a non-negative inverse

**Problem:** $S \ge 0$ and $S^{-1} \ge 0$ imply $S$ is a permutation times a positive diagonal.
**Worked unaided up to:** $S^{-1}S = I$ written entrywise; then claimed "only diagonal" with no
argument.
**Where I asked for a hint:** top rung — the full proof, on request. **Not yet derived.**
**Attempt:** —
**Outcome:** stuck.
**What it revealed:** a characterisation asserted without testing the smallest case:
$\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ satisfies everything and is not diagonal.
**Revisit:** next session, $2 \times 2$ first, then the general argument.

## 2026-10-06 — the loss as a noise model

**Problem:** which noise model makes maximum likelihood least squares; the Poisson negative
log-likelihood; how each treats a zero and a large count.
**Worked unaided up to:** Gaussian with one $\sigma^2$. **Derived unaided.** The Poisson
expansion. **Derived unaided.** as far as setting it up.
**Where I asked for a hint:** "one $\lambda$ per entry, observed once"; "evaluate the derivatives at
the expansion point". The analysis of cNMF's variance-scaling patch was handed over on request.
**Not yet derived.**
**Attempt:** wrote the likelihood for $n$ draws sharing one $\lambda$, then substituted
$\lambda_{ij}$; wrote "maximize" for the negative log-likelihood.
**Outcome:** solved, with corrections.
**What it revealed:** the likelihood came from a template before the generative model was written
down. Near-miss: "$\lambda^2$ — more penalty" than $\lambda$ holds only for $\lambda > 1$; the
meaningful comparison is shape.
**Revisit:** state the model in words first — "each entry has its own mean, observed once".

## 2026-10-07 — sort the differences between two runs

**Problem:** two runs $(W, H)$ and $(W', H')$ on the same $\tilde X$: sort every difference into
not real, the optimiser's fault and the data's fault; for each, say whether it is an $S$ and how to
recognise it from the runs alone.
**Worked unaided up to:** the optimiser's bin completely: no $S$ relates the runs, and their
likelihoods differ. **Derived unaided.** The not-real bin partly, as "an orthogonal $S$": right
for permutations, wrong for rotations, and rescaling missed — a near-miss, not unaided work.
**Where I asked for a hint:** none; the other bins were completed by the mentor after I switched to
motivate-then-prove for pace.
**Attempt:** not-real differences "could be traced by looking for an orthogonal S that would align
those"; for the data's bin, "looking if there are pure cells and genes for each of the program. If
there are few such, then I would assume that something is going very wrong".
**Outcome:** partly solved.
**What it revealed:** the orthonormal reflex, third appearance. "Orthogonal" lets in rotations,
which are either invalid or genuine alternatives, and leaves out rescaling, which is harmless
($\operatorname{diag}(2,1)$ is the counterexample). Rescaling was missed altogether. The data's bin
got a test on one run instead of a comparison between runs, and pins are sufficient, not necessary,
so their absence is not a verdict (Proposition B in
[the cNMF note](../notes/matrix-factorisation/cnmf-consensus.md) is the counterexample).
**Revisit:** before naming the group of harmless $S$, test one $2 \times 2$ element of each
candidate: $\operatorname{diag}(2,1)$ and a $45^\circ$ rotation.

## 2026-10-07 — not attempted

**Problem:** the proofs set at stops 1–4: the $2 \times 2$ table of four $S$; the monomial lemma
($2 \times 2$ first); Propositions A ($t \le 3/7$) and B; $E(K+1) \le E(K)$ and the continuum at
$K = K^* + 1$; uniqueness of the usage refit; what an entry of $H^{\mathrm{TPM}}$ means.
**Worked unaided up to:** —
**Where I asked for a hint:** —
**Attempt:** none; I chose pace over proofs, and the answers were given.
**Outcome:** not attempted.
**What it revealed:** nothing about the material yet: the explanations had almost no equations to
work against.
**Revisit:** next session, from the cNMF note, before opening the folded proofs.
