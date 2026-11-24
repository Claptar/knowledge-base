# The size of a map — practice

Attempts from the sessions in [topics/size-of-a-map.md](../topics/size-of-a-map.md). The
handwritten pages of 2026-11-01 and the dictation of 2026-11-03 are in Russian; quotes are verbatim.

## 2026-11-01 — what multiplicativity gives for free

**Problem:** my own, set before anything was posed: a size $D$ of maps $V \to V$, on a space with
no norm, that respects composition, $D(\hat A\hat B) = D(\hat A)\,D(\hat B)$ — what follows?
**Worked unaided up to:** three consequences — the size of the identity, $D(\hat I) = D(\hat I)^2$;
the size of the inverse, $D(\hat A) = 1/D(\hat A^{-1})$; and conjugation,
$D(\hat P^{-1}\hat A\hat P) = D(\hat A)$. **Derived unaided.**
**Where I asked for a hint:** none. Corrections afterwards: $D(\hat I) = D(\hat I)^2$ allows $0$ as
well as $1$, and $0$ has to be ruled out; the useful output of the second is that $D(\hat A) \neq 0$
for every invertible $\hat A$; with hats, the third is about a *different* map, not a change of
basis.
**Attempt:** the handwritten notes, which headed ③ "Change of the basis".
**Outcome:** solved; the zero case closed in my own words on 2026-11-03.
**What it revealed:** the capability — the question, its three sub-questions and the demand were
mine before any problem was set. And ③ read with matrix habits: once $D$ lives on maps, nothing
depends on a basis to begin with, and what the line shows is that conjugate maps have equal size.
I noticed afterwards that it had lost its motivation: «Здесь это все стало, конечно, менее
мотивировано».
**Revisit:** —

## 2026-11-03 — why does a column addition "change nothing"?

**Problem:** mine, from the dictation: elementary column operations were the moves that left the
size alone — what does that actually mean?
**Worked unaided up to:** the question itself, which I had not asked before: «Как-то я раньше
воспринимал это больше как данность», and «Но, как бы, если честно, вообще нетривиально, что у нас
размер не будет меняться».
**Where I asked for a hint:** none; the correction was given with the next problem.
**Attempt:** «Может, это значит, что они, как бы, у нас эти преобразования обратимые, что они, как
бы, задают изоморфизм».
**Outcome:** open — became the [shear](../topics/shear.md) question.
**What it revealed:** a false analogy: invertible, so the size is unchanged. A stretch by 2 is an
isomorphism too, and its size is 2. Where the intuition is exactly right: invertible means the size
is not zero — my own consequence of multiplicativity above. "Nothing changes" means
$D(\hat A \circ \hat T) = D(\hat A)$, that is $D(\hat T) = 1$; the map itself changes.
**Revisit:** with the shear problems.
