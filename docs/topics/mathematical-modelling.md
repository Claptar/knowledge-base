# Mathematical modelling

**Status:** open — seeded, not yet studied
**Opened:** 2026-09-13  **Last touched:** 2026-09-13

> **Provenance.** This file was seeded on 2026-09-13 from an external reading guide, not from a
> session. It is borrowed structure, not my own trajectory — nothing below has been worked through,
> and no phrasing here is mine yet. The sections that matter (*How I could have come up with this*,
> *Derived / proved myself*) are deliberately empty. Sources are in
> [resources/index.md](../resources/index.md); the live questions this file is attached to are in
> [questions.md](../questions.md).

## The question that opened it

Not yet asked in my own terms. The guide's framing: applied mathematics is usually organised by
*technique* (ODEs, optimisation, statistics, numerics) when it would be more useful organised by
*modelling task* — what to model, which mechanism matters, how you tell when the model fails. The
open question is whether that reframing survives contact with a real problem, or whether it is the
kind of tidy meta-structure that dissolves once you are actually deriving something.

## Attached to

- **Chemical master equation / stochastic transcription work.** The mechanism → transition rates →
  master equation → Fokker–Planck ↔ Langevin chain is exactly the modelling loop specialised to
  jump processes. van Kampen is the text that treats it as modelling rather than as probability.
- **Daily pipeline QC and 10x chemistry inference.** Sampling artefacts, noise models and count
  data are model-form assumptions being made and violated continuously in real data — the
  validation/discrepancy vocabulary below is a formalisation of judgements already made informally.
- **Convex optimisation (Boyd/EE364A).** Already hold the theory; the missing half is formulation —
  how a real problem *becomes* $\min_x c^T x$ subject to $Ax \le b$ in the first place.
- **HMMs (Rabiner, Durbin).** Latent-variable inference is the inverse problem $y \rightarrow
  \theta$ in the classification below, with identifiability as the live concern.

## The modelling loop

The guide's central claim is that modelling is not $\text{equation} \rightarrow \text{solve
equation}$, but a cycle:

$$
\text{question} \rightarrow \text{scale + variables} \rightarrow \text{assumptions} \rightarrow
\text{model} \rightarrow \text{analysis/simulation} \rightarrow \text{calibration} \rightarrow
\text{validation} \rightarrow \text{sensitivity + uncertainty} \rightarrow \text{revision}
$$

with the hard decisions concentrated at the front (what to model, what to leave out, which
timescale and which mechanism matter) and the credibility questions at the back.

For mechanism-driven stochastic models specifically, the chain runs:

$$
\text{physical mechanism} \rightarrow \text{stochastic model} \rightarrow
\text{mathematical description}
$$

e.g. starting from a particle obeying $m\dot v = -\gamma v + \eta(t)$ and asking what $\eta(t)$
should represent, why zero mean, why short correlation time, why the white-noise idealisation, and
what density that implies — rather than starting from an abstract $B_t$.

## Verification vs validation

The distinction the guide insists is essential:

- **Verification — did I solve my model correctly?** For $\partial_t u = D\nabla^2 u$, whether the
  numerical method actually solves that equation: discretisation error, convergence, solver
  tolerance, implementation bugs, floating-point effects.
- **Validation — is this model an adequate description of reality for the intended purpose?** You
  can solve the PDE perfectly and still have the wrong model.

Compressed: verification is solving the model right; validation is choosing the right model.

## Four error sources worth separating

Parameter uncertainty, model-form error, measurement error, and numerical error are different in
kind and get confused routinely. The guide's example: solving an ODE to $10^{-12}$ precision is
pointless when a biological parameter is uncertain by 30%.

A model honest about this looks less like $y = f(x,\theta)$ and more like

$$
y = f(x,\theta) + \delta(x) + \epsilon
$$

with $\theta$ the uncertain parameters, $\delta(x)$ the model discrepancy, and $\epsilon$
measurement noise — rather than pretending all uncertainty lives in one parameter estimate.

## Forward and inverse problems

Forward: $\theta \rightarrow y$ — given parameters, predict observations.
Inverse: $y \rightarrow \theta$ — given observations, infer parameters or hidden structure.

Examples: MRI measurements → image; seismic waves → Earth structure; expression data → kinetic
parameters; observed trajectories → dynamical-system parameters. The governing concerns are
identifiability, ill-posedness, regularisation, prior information, and non-uniqueness.

## Dynamical systems, from a modelling stance

For $\dot x = f(x;\theta)$, the explicit solution $x(t)$ is usually the wrong target. The useful
questions: what equilibria exist, are they stable, are there oscillations or multiple attractors,
how do qualitative regimes change with parameters, is there a bifurcation, which timescales
dominate.

## Numerics, from a modelling stance

Not an algorithm list (Newton, Runge–Kutta, quadrature, finite differences, finite elements) but a
set of questions: what accuracy is actually needed, which error source dominates, is the solver
stable, is the problem stiff, is the discretisation resolving the relevant scale, could a numerical
artefact be mistaken for physical behaviour.

## The modelling notebook

The guide's per-project checklist, kept here as a working template rather than as something
understood:

1. **Question** — predict, explain, control, estimate or optimise *what*, exactly. A vague question
   produces a vague model.
2. **Scale** — which spatial, temporal, population-size, energy, concentration scales matter; which
   can be ignored.
3. **Variables** — state variables, observables, hidden variables, parameters, controls, inputs,
   outputs.
4. **Assumptions** — every important one written explicitly (homogeneous mixing, independence,
   constant rate, Gaussian noise, no spatial structure, Markov property, conservation, linear
   response), then: which conclusions depend strongly on each?
5. **Mechanism** — why the equations follow from the assumed mechanism. Not because the equation is
   familiar.
6. **Sanity checks** — dimensions, signs, conservation, limiting cases, symmetry, positivity,
   boundary conditions, monotonicity. Push $t \to 0$, $t \to \infty$, $\theta \to 0$, $\theta \to
   \infty$.
7. **Parameters** — for each: measurable, known from literature, estimated, fitted, varying between
   systems, identifiable from the available data?
8. **Identifiability** — can different parameter combinations produce nearly the same observations?
   If so, a good fit does not imply a determined model.
9. **Predictions** — written *before* looking at validation data. What observation would surprise
   this model? A model that explains everything predicts nothing.
10. **Validation** — against data not used for fitting; study residual structure, systematic
    deviations, failure regions, extrapolation, regime dependence.
11. **Sensitivity** — perturb parameters, initial conditions, boundary conditions, and assumptions;
    see which outputs move.
12. **Uncertainty** — propagate into the quantity of interest; do not report a point prediction
    when the uncertainty is large.
13. **Competing models** — is there a simpler mechanism explaining the same data? Compare
    mechanistically, not only statistically.
14. **Next experiment** — which measurement best discriminates between the competing models?
15. **Revision** — what failed, which assumptions were wrong, what the next model changes, and
    whether added complexity actually improved prediction.

## The organising claim

Rather than organising applied mathematics by technique, organise by task:

| Task | Tools |
| --- | --- |
| Formulating the model | dimensional analysis, conservation laws, probability, mechanistic reasoning, scaling |
| Understanding dynamics | ODEs, PDEs, dynamical systems, stochastic processes |
| Estimating unknowns | statistics, inverse problems, Bayesian inference, optimisation |
| Computing predictions | numerical analysis, simulation, Monte Carlo, finite differences/elements |
| Assessing credibility | diagnostics, sensitivity analysis, UQ, validation, cross-validation, experimental design |
| Choosing actions | optimisation, control, decision theory |

The fields connect because they are stages of one loop:

$$
\text{observe} \rightarrow \text{model} \rightarrow \text{infer} \rightarrow \text{predict}
\rightarrow \text{test} \rightarrow \text{revise} \rightarrow \text{act}
$$

## How I could have come up with this

_Empty. Nothing here has been derived or even studied yet — this is imported structure._

## Still loose

- Everything. No part of this has been tested against a problem I actually care about.
- The first real test should be a model I already half-hold: the chemical master equation for
  simple transcription. Run the notebook checklist against it and see which steps are load-bearing
  and which are bureaucracy.
- Open question: is the verification/validation split actually useful in the single-cell setting,
  where "reality" is itself a noisy, heavily-processed measurement rather than a clean experiment?
- Unclear whether Meerschaert is worth reading linearly or whether modelling craft only transfers
  by doing it on a problem with stakes.

## Derived / proved myself

_Nothing yet._
