# Resources

Evaluated materials, grouped by topic. Every entry carries a verdict — what it is good for and
what is wrong with it. The verdict is the expensive part; it is why this file exists rather than
a bookmark folder.

> **Provenance note.** Most entries below came in as recommendations from an external reading
> guide (2026-09-13), not from my own reading. They are candidates, not judgements. Verdicts are
> marked *(unvetted)* until I have actually worked with the text and can say what is wrong with
> it — a recommendation repeated is not a verdict earned.

## Template

- **Author, Title** (book | notes | paper | course) — what it is good for; what is weak about it;
  whether it motivates or merely states. Link.

## Doing mathematics — process and heuristics

- **Lakatos, *Proofs and Refutations*** (book) — *(unvetted)* not a textbook; a dialogue on how
  mathematics actually develops: conjecture, attempted proof, counterexample, broken proof,
  revised definition, deeper structure. Aimed squarely at the complaint that polished textbook
  proofs hide the process that produced them. Weakness: gives no machinery, so it pairs with a
  technical text rather than replacing one.
- **Pólya, *How to Solve It* / *Mathematics and Plausible Reasoning*** (book) — *(unvetted)*
  companion to Lakatos on heuristic reasoning and how conjectures get formed in the first place.

## Real analysis

- **Abbott, *Understanding Analysis*** (book) — *(unvetted)* recommended as the first choice:
  questions posed before the formal result, heavy use of counterexamples, motivates *why*
  completeness, compactness, uniform convergence and continuity are formulated as they are.
  Likely too introductory in places given my background — treat as a motivation source, not a
  course.
- **Pugh, *Real Mathematical Analysis*** (book) — *(unvetted)* the step after Abbott: geometric
  intuition, unusual examples, reaches multivariable analysis, function spaces and measure-adjacent
  topics.
- **Hairer & Wanner, *Analysis by Its History*** (book) — *(unvetted)* read alongside the above for
  how analysis actually arose, rather than the modern logical structure presented as if it were
  always there.

Suggested route: Abbott → Pugh, with Hairer & Wanner in parallel for historical motivation.

## Complex analysis

- **Needham, *Visual Complex Analysis*** (book) — *(unvetted)* geometry first; complex functions as
  transformations; Cauchy's theorem, Möbius transformations, winding numbers and harmonic functions
  given geometric meaning. The flagship example of a book asking what the mathematics *means*.
- **Stein & Shakarchi, *Complex Analysis*** (book) — *(unvetted)* the rigour-and-connections
  counterpart: Fourier analysis, zeta functions, elliptic functions, number theory.

Pairing: Needham for geometry and intuition, Stein–Shakarchi for rigour and connections.

## Linear algebra

Note: linear algebra is already held deeply (Kostrikin/Gelfand tradition — see
[profile.md](profile.md)), so these are relevant only as sources of *problems*, not as courses.

- **Halmos, *Linear Algebra Problem Book*** (book) — *(unvetted)* the closest match to a
  discover-the-theory-yourself approach: question → think → hint → solution. Inquiry-based rather
  than expository.
- **Treil, *Linear Algebra Done Wrong*** (book) — *(unvetted)* useful for connections outward to
  geometry, analysis and probability. Use when a systematic explanation is wanted; Halmos first.

## Probability

- **Blitzstein & Hwang, *Introduction to Probability*** (book) — *(unvetted)* stories and paradoxes,
  problems before machinery, strong on connections between distributions; exercises are core to the
  book. Aimed at building a mental model rather than technique recall — but likely below the level
  I need given the Murphy/ISL/ESL background.
- **Williams, *Probability with Martingales*** (book) — *(unvetted)* the advanced transition:
  measure theory introduced *because probability needs it*, martingales as the organising principle,
  exercises central. Bridge toward stochastic processes. Already the target of an open thread — see
  [log.md](log.md).

## Mathematical statistics

- **DeGroot & Schervish, *Probability and Statistics*** (book) — current main text. Formal
  definitions, derivations, sampling distributions, estimation, likelihood, Bayesian methods,
  testing, linear models, exercises. Machinery, not meaning.
- **Cox, *Principles of Statistical Inference*** (book) — *(unvetted)* recommended as the single
  best companion to DeGroot: what statistical evidence *is*, why likelihood, what confidence
  procedures actually mean, why tests have the structure they do, how Fisherian/frequentist/Bayesian
  reasoning differ. Division of labour: DeGroot = machinery, Cox = meaning of inference.
- **Efron & Hastie, *Computer Age Statistical Inference*** (book) — *(unvetted)* the intellectual
  map of modern statistics: classical inference through empirical Bayes, James–Stein, bootstrap,
  cross-validation, regularisation, multiple testing, forests, boosting. Best dipped into for
  "where does this classical idea lead?", not read linearly.
- **Freedman, *Statistical Models: Theory and Practice*** (book) — *(unvetted)* for modelling
  judgement and criticism: why IID, why Gaussian, why linear, why should this coefficient be
  causal, where did the sample come from. The counterweight to DeGroot's "given this model…".
- **Gelman, Hill & Vehtari, *Regression and Other Stories*** (book) — *(unvetted)* regression as a
  modelling activity rather than a formula: assumptions, diagnostics, predictive simulation,
  residual analysis, model checking, cross-validation, interpretation.
- **Box, Hunter & Hunter, *Statistics for Experimenters*** (book) — *(unvetted)* experimental
  design — choosing what data to collect next, and designing experiments that discriminate between
  competing explanations. The half of modelling that is not fitting.

## Stochastic processes

- **Resnick, *Adventures in Stochastic Processes*** (book) — *(unvetted)* organised around concrete
  processes rather than abstract machinery: Markov chains, renewal theory, point processes,
  continuous-time Markov chains, Brownian motion, random walks. Motivation before abstraction, and
  explicit about which arguments are rigorous and which are plausibility. This is the
  probability-theory map.
- **van Kampen, *Stochastic Processes in Physics and Chemistry*** (book) — *(unvetted)* the
  mechanism map, not the probability map: microscopic randomness → transition rates → master
  equations → macroscopic behaviour and fluctuations, with the jump process → master equation →
  Fokker–Planck ↔ Langevin chain made explicit. Directly relevant to the chemical master equation
  and stochastic gene expression. Likely the most valuable single book here given current
  direction.
- **Ross, *Introduction to Probability Models*** (book) — *(unvetted)* applied probability: Markov
  chains, queueing, reliability. Weaker than van Kampen on *why* a stochastic description follows
  from the mechanism; use for worked applications only.

Resnick and van Kampen answer different questions — "how do these objects behave mathematically?"
versus "where do these equations come from?" — and are complements, not alternatives.

## Mathematical modelling

See [topics/mathematical-modelling.md](topics/mathematical-modelling.md) for the methodology these
support.

- **Meerschaert, *Mathematical Modeling*** (book) — *(unvetted)* recommended as the best single
  starting book if the goal is to learn modelling explicitly: optimisation, dynamical systems and
  stochastic models treated as one activity, with the full loop from problem formulation through
  sensitivity and robustness.
- **Bender, *An Introduction to Mathematical Modeling*** (book) — *(unvetted)* real problems, model
  construction, and sustained criticism of assumptions — deciding whether a model is *useful*
  rather than whether it is solvable.
- **Gershenfeld, *The Nature of Mathematical Modeling*** (book) — *(unvetted)* a broad map: ODEs,
  PDEs, variational methods, stochastic processes, numerics, finite elements, inference, density
  estimation, state estimation, HMMs, time series. Value is in showing these belong to one
  enterprise; too thin to be a sole technical text on any of them.
- **Mahajan, *Street-Fighting Mathematics*** (book) — *(unvetted)* dimensional analysis, limiting
  cases, lumping, scaling, order-of-magnitude reasoning, successive approximation, analogy. Short
  and practical. The habit it trains — ask what must be true on dimensional or asymptotic grounds
  before computing — is one of the most transferable in applied maths. Barenblatt on scaling is the
  advanced continuation.

## Optimisation

- **H. P. Williams, *Model Building in Mathematical Programming*** (book) — *(unvetted)* covers the
  part most optimisation books omit: turning a real problem into an optimisation problem —
  choosing decision variables, constructing constraints and objectives, linearisation, integer
  variables, and the computational consequences of formulation choices.
- **Boyd & Vandenberghe, *Convex Optimization*** (book) — already worked through via EE364A; the
  theory side, to be used after the formulation question rather than instead of it.

## Verification, validation, uncertainty, inverse problems

- **Oberkampf & Roy, *Verification and Validation in Scientific Computing*** (book) — *(unvetted)*
  code verification, solution verification, model validation, prediction, comparison with
  experimental data. The reference for the verification/validation distinction.
- **Smith, *Uncertainty Quantification: Theory, Implementation, and Applications*** (book) —
  *(unvetted)* parameter uncertainty, sensitivity analysis, calibration, identifiability,
  uncertainty propagation, model discrepancy, surrogate and reduced-order models. Flagged as a
  later read — worth most after several models have actually been built.
- **Calvetti & Somersalo, *Bayesian Scientific Computing*** (book) — *(unvetted)* inverse problems
  combined with scientific computing and Bayesian inference: identifiability, ill-posedness,
  regularisation, priors, non-uniqueness under noisy observation.

## Suggested minimal list

From the source guide, if the goal is to avoid accumulating books: DeGroot & Schervish (main
machinery), Cox (meaning of inference), van Kampen (mechanistic stochastic modelling), Meerschaert
(general modelling practice), Mahajan (scaling and approximation), and Smith (uncertainty
quantification, later).
