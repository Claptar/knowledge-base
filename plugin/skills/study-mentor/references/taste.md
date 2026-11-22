# Taste

What "excellent" means to him, reconstructed from the works he named himself. Read this before
recommending material, and again when an explanation isn't landing.

> **Status: mostly reconstructed.** The works below are his; the verdicts on them are inferred
> from what he has said about how he studies. *What he has said outright* is confirmed, in his
> words. Correct the rest as he reacts to actual recommendations.

## What he has said outright

From the determinant and shear sessions, 2026-11, after they left him organising the material
himself:

> What is our goal? Do we want just a function that can identify linearly dependent rows/columns?
> If so what properties do we expect to see? What is the most basic function to perform such role?
> Why would we want anything more complicated? What properties/features do we expect then?
> … Later results are good to keep in mind, though, as we might not be satisfied with something
> simple and future cases/results is a good motivation to broaden what our function should do, but
> not from the start though, you can't just ask EVERYTHING

> I could not see the global picture and the reason for those problems and questions and had to
> stop once in a while and reorganise it myself

So an explanation is excellent for him when it **constructs** the object from a question — each
requirement forced by what the simpler answer could not do — and keeps the overall route and the
reason for each step in view. One that recognises a known answer and checks it fits is not, however
rigorous.

## The discriminator

He wants **maximal motivation at full depth** — not maximal rigour, and not the easiest route.

These come apart constantly, and getting it wrong is the most common failure:

- A more rigorous text is not automatically better. Rigour that arrives as
  definition → lemma → theorem → convenient proof is the style he calls artificial.
- A text pitched at newcomers — "accessible", "intuitive introduction", "in plain English" — usually
  wastes his time. That is a judgement about the audience, not about length or ease: a concise text
  that motivates fully is a good recommendation.
- Length follows from the motivation; it is not a target. Prefer the treatment that shows why each
  object had to exist, at whatever length that takes — but navigating a long explanation has a real
  cost, and a shorter one that does the same job wins.
- Motivation and the equation come side by side, as in Kostrikin. An exposition of mathematics in
  words alone fails however well motivated it is: the formula is what he works against.

The test to apply to a candidate source: **does it let the reader see how someone could have come
up with this?** A book that states the right things in the right order but leaves that invisible
is a bad recommendation for him even when it is the standard reference.

## What he has named

- **Kostrikin; Gelfand** — linear algebra, the Russian tradition. This is his baseline for what a
  good mathematical text feels like: structural, unhurried, motivated from inside the subject.
  When a topic has a Russian classic that beats the Anglophone standard — often true in probability
  and algebra — recommend it. He reads Russian fluently.
- **His own tensor-analysis lecture notes** (Russian, Markdown/LaTeX) — he writes the kind of
  exposition he wants to read. A useful calibration: if an explanation is something he could adapt
  and teach from, it is at the right level.
- **Murphy, *Probabilistic Machine Learning*** — his current route through probability and
  statistics on the ML side. Broad and current; a reference to work through rather than a source of
  motivation for any single idea.
- **ISL vs ESL** — he compared them and is working at ESL's level. Treat this as settled: never
  recommend the lighter of a pair on the assumption it is more approachable.
- **Rabiner; Durbin et al.** — HMMs. Rabiner's tutorial is the model of the genre he likes: a real
  problem, the algorithms that the problem forces, and the reasoning kept visible throughout.
- **Boyd & Vandenberghe / EE364A** — convex optimization. A course with problem sets attached,
  which is the shape he gets most out of.
- **Gorin & Pachter, and the Pachter lab biophysics curriculum** — his current target. Primary
  literature aimed at a biological question, not a textbook treatment.

## How to shape a recommendation

- **Primary sources and real lecture notes first.** Original papers, course notes with problem
  sets, lecture series by people who work in the area. These carry the author's own reasoning,
  which is the thing he is buying.
- **Two to four options, each with a verdict** — what it is good for *and* what is wrong with it.
  A named weakness is what makes the rest of the verdict credible. "Strong on the measure-theoretic
  setup, but the martingale chapter is the convenience-proof style you dislike" is useful;
  "a comprehensive introduction" is not.
- **Search fresh every time.** What is best for a topic changes, and a stale recommendation from
  recall is worse than none.
- **Record the verdict in `resources/`.** The judgement is the expensive part; it is why that
  file exists instead of a bookmark folder.

## Signals an explanation isn't landing

Reach for a different route — usually a more concrete problem, or a different anchor — when:

- he asks *why* a definition is stated that way, rather than asking about its consequences;
- he can follow each step but cannot say what made the first step the natural one;
- the exchange has turned into him confirming your statements rather than deriving anything;
- he stops to reorganise the material himself, asks what the goal is, or asks for the route — the
  map is missing, and repairing it comes before the next problem.
