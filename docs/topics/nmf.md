# NMF — if many factorisations fit, do the programs mean anything?

**Status:** open
**Opened:** 2026-10-06  **Last touched:** 2026-10-06

Practice: [practice/nmf.md](../practice/nmf.md) · Material:
[the NMF note](../notes/matrix-factorisation/nmf-identifiability-and-loss.md) · Read alongside
Kotliar et al. 2019 (cNMF), eLife 8:e43803.

## The question that opened it

The paper reads the rows of $H$ as biological programs — identity and activity. Half an hour in,
the question that actually became live was mine, not the paper's:

> "Why do we even care actually about some transformation matrix S preserving this feature? We're
> kind of really interested in just getting the factorization matrices themselves. And do we really
> care about like those other possible factorizations that we could get potentially?"

What it forced: if a second $(W', H')$ fits exactly as well, the gene list attached to a program is
an accident of which solution the algorithm landed on. "Which $S$ survive the constraints?" is the
question "is the answer unique, and can I read anything into it?"

## Attached to

- [Change of basis](../notes/linear-algebra/change-of-basis.md): the rows of $H$ are a basis of
  $\mathrm{row}(X)$ and $W$ is the coordinates, so every exact factorisation is $H' = SH$,
  $W' = WS^{-1}$ — the note's "basis and coordinates move in opposite directions" (§5). The note
  writes $e' = eC$ with the new vectors' coordinates in the *columns* of $C$; with programs stacked
  as rows, the same matrix appears transposed, $S = C^\top$.
- [Quotient spaces](../notes/linear-algebra/quotient-spaces.md) and
  [symmetries and groups](../notes/structures/04-symmetries-and-groups.md): the data identifies
  only an orbit of $GL(K)$; what survives the sign constraints is the orthant's symmetry group,
  permutations times positive diagonals.
- HMM label switching (Rabiner, Durbin): the small case of "identifiable only up to a group".
- PCA — as the source of a false analogy, not a support: its orthonormal convention was held as a
  fact about the problem, twice ([practice](../practice/nmf.md)).
- Poisson likelihood: the NMF loss is a noise model, which is the measurement layer of the
  [path](../path.md) arriving from an unexpected side.

## Where else this shows up

*Not asked yet* — the outbound question was skipped this session. Candidates raised by the mentor,
not yet mine, are listed under *Still loose*.

## How I could have come up with this

*Not yet.* Prompt for next time: starting only from "the data fixes an orbit of $GL(K)$, and the
constraints are $SH \ge 0$ and $WS^{-1} \ge 0$", could I have predicted that the natural
conditions are pure cells and marker genes, acting on $S^{-1}$ and $S$ respectively? What would
have made me look at the transpose first?

## Still loose

- *How I could have come up with this*, above.
- The monomial lemma ($S \ge 0$ and $S^{-1} \ge 0$ force a permutation times a positive diagonal).
  I claimed "only diagonal" and missed permutations; the proof was handed over.
  **Not yet derived.** Redo it, $2 \times 2$ first.
- What cNMF's variance-scaling patch assumes (gene-weighted least squares; what $s_j^2$ contains).
  The derivations were handed over on request. **Not yet derived.**
- Separability is sufficient, not necessary; weaker "sufficiently scattered" conditions exist
  (Fu et al. 2019). **Unverified.** Not read.
- The activity-program case quantitatively: what exactly is lost when only some programs have pure
  cells, beyond "the inside pin is missing for that arrow".
- Overdispersion: UMI variance is closer to $\mu + \mu^2/\theta$ than $\mu$; bursty transcription
  produces the negative binomial, so the honest loss links back to the CME thread.
- Outbound candidates raised by the mentor, not yet mine: label switching in mixture models; topic
  models (LDA) as the multinomial version; mutational signatures (Alexandrov 2013), where cNMF's
  consensus step comes from.
- **Parked by choice, 2026-10-06:** how NMF is fitted (multiplicative updates; KL updates as EM
  over hidden per-program counts — the Baum–Welch anchor), NP-hardness, Bayesian Poisson
  factorisation. Not needed for cNMF.
- Traps hit, with what each revealed: [practice/nmf.md](../practice/nmf.md).

## Derived / proved myself

- 2026-10-06 — every exact rank-$K$ factorisation is $(WS^{-1}, SH)$ for an invertible $S$, and
  every such pair is one. **Derived unaided.** after a nudge to collect the coefficients into a
  matrix; the dimension sandwich that makes the rows of $H$ a basis was supplied.
- 2026-10-06 — $W \ge 0$ says every cell lies in $\mathrm{cone}(H)$: "it's really inside of the
  cone". **Derived unaided.** once the $K = 2$ picture was on the page.
- 2026-10-06 — an outward swing $h_1 - t h_2$ is blocked by a gene with $h_{1j} = 0 < h_{2j}$.
  **Derived unaided.** as far as $h_{1j} = 0$; the condition $h_{2j} > 0$ was missing.
- 2026-10-06 — inside pin: a pure cell for program $k$ forces row $k$ of $S^{-1}$ to be
  non-negative, through an inner product of my own in which the $h$'s are orthonormal.
  **Derived unaided.** — I did not recognise it as the result until it was pointed out.
- 2026-10-06 — outside pin: marker genes force $S \ge 0$, by transposing ("now let's take a look at
  this from the other side"). **Derived unaided.**
- 2026-10-06 — Gaussian noise with one $\sigma^2$ makes maximum likelihood least squares.
  **Derived unaided.**
- 2026-10-06 — the Poisson negative log-likelihood and its local form $(\lambda - x)^2 / 2x$.
  **Derived unaided.** as far as setting up the expansion; a one-$\lambda$ template slip and the
  evaluation of the coefficients were corrected.
