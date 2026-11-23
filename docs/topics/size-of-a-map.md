# The size of a map — by how much does a map change sizes, and why is that the determinant?

**Status:** open
**Opened:** 2026-10-26  **Last touched:** 2026-11-03

Practice: [practice/size-of-a-map.md](../practice/size-of-a-map.md) · Comes from:
[where the determinant comes from](where-the-determinant-comes-from.md) (Road 3 of the four roads)
· Led to: [shears](shear.md) · Material outside this repository: the Road 3 note *The determinant
as the size of a map*, rebuilt by Claude from my handwritten pages.

Notation: a hat marks a map, no hat its matrix in a basis — $\hat A : V \to V$ and $A$.

## The question that opened it

At the end of the four-roads session, an observation of my own:

> "Thinking about it I realised that we have a (kind of) notion of the length of the vector even
> without giving the space a defined norm. We understand that c * v is a vector of the size c
> compared to vector v. This allows us to compare in size only collinear vectors, but still it also
> does not require a defined norm. Similarly for a map we could find directions in which vector
> direction does not change under the map (eigen vectors) their values could give us some hint about
> the size of the map itself"

> "So I see all of that but I struggle a bit to understand how all this connects to determinant
> profoundly"

On 2026-11-01, rewriting the Road 3 note by hand for maps rather than matrices, the question as I
wrote it:

> «А на сколько в «среднем» увеличивается размер векторов при таком отображении?»

*By how much, "on average", does such a map increase the size of vectors?* — with three questions
inside it: «Зачем задаваться этим вопросом?!», «Что значит «в среднем»?», «Как мерять «изменение
размера»?» (why ask it at all; what does "on average" mean; how do you measure a change of size).
On the second I had one firm point: «понятно, что эта мера среднего не должна зависеть от базиса,
т.к. это характеристика отображения» — it cannot depend on the basis, because it describes the map.

The first one I answered myself, dictating, on 2026-11-03. In one dimension a linear map is
multiplication by a coefficient, the factor by which a line or a neighbourhood stretches; for a
general map, «как раз производное — это тот самый коэффициент, который будет говорить о том, как у
нас окрестность сама, окрестность точки будет растягиваться или сжиматься»; for random variables,
«растягивание или сжимание этой самой окрестности будет говорить про то, как у нас меняется
плотность вероятности». In many dimensions the question is how a neighbourhood stretches «в целом.
Не в каком-то конкретном направлении, а вот, ну, вот в принципе, в целом», and for that «нам нужна
какое-то определение для объема, которое бы не зависело от выбора базиса».

## Attached to

- **Road 3 of the [four roads](where-the-determinant-comes-from.md)**: ask for a size that
  respects composition, $D(\hat A\hat B) = D(\hat A)\,D(\hat B)$ — "«уважение» композиций", in my notes.
- **The derivative and change of variables** — my own anchor in the dictation, not a supplied one:
  the Jacobian determinant as the local stretch of volume, and with it the density.
- **Eigenvectors**, my hint from the start: «Это может быть намёком на то, что собственные вектора
  и их значения могут быть связаны с тем, что нам нужно».
- **[Change of basis](../notes/linear-algebra/change-of-basis.md)**: for matrices, $P^{-1}AP$ is the
  same map in another basis; for maps, $\hat P^{-1}\hat A\hat P$ is a different map, $\hat A$
  carried along $\hat P$. Supplied as the correction to my ③.
- **Linear functionals**, met more closely only recently — «с линейными функциями в целом на
  линейных пространствах я относительно недавно познакомился прям поближе». This is what pulled me
  into [shears](shear.md).

## Where else this shows up

- **Probability densities** — my reason for asking, above. If $Y = \hat A X$, the density picks up
  $1/|\det \hat A|$; the formula was supplied, the reason was mine.
- **Tensor analysis.** A bilinear form — a metric $g$, a covariance $\Sigma$ — is not a map
  $V \to V$; under $Y = MX$ its determinant picks up $(\det M)^2$. So $\sqrt{|g|}$ is a density, and
  only ratios such as $\det\Sigma_1 / \det\Sigma_2$ are invariant. Given.
- **PCA.** Comparing stretch across *different* directions needs an inner product: that is the
  singular values, with $|\det A| = \sigma_1\cdots\sigma_n$. The determinant only compares volumes.
  Given; it ties to the [PCA anchor](../profile.md#anchors-worth-building-on).
- **Maps between two spaces** $V \to W$: a size only after choosing a unit of volume on each side;
  only "zero or not" is intrinsic. Given.

## How I could have come up with this

- **Why ask the question** — answered in my own words, above: a scale factor, a derivative, a
  density, a volume that does not depend on the basis.
- **Why ask for multiplicativity** — mine, tentatively: «это логичное свойство для того, чтобы
  просить от какой-то линейной, ну, вот линейных преобразований», because nothing here is
  nonlinear. What is lost without it is still open.
- **Why the answer is the determinant** — not yet. My verdict on the first version of Road 3:

  > "But it does not really feel like a road to determinant more like: hmm, we want this kind of
  > funciton and it seems that we know something with similar properties let's try it. Oh it seems
  > to be matching, good, just as we wanted it to"

  The answer given — $n$-volumes form a single line, every map acts on it by one factor, and ratios
  along a shared line compose where eigenvalues on each map's own lines do not — is **Not yet
  derived.** So is the forced-linearity version of Road 3 that replaced the guess.

## Still loose

- **Road 3 §10, for maps — set 2026-11-01, left unsolved on purpose.** Using maps only, and only
  the wish ($D$ a non-constant polynomial on maps, multiplicative): what does it force on a stretch
  — the identity on a hyperplane, times $s$ on a line outside it; on a map that is not invertible;
  on a map with an eigenbasis? Which maps does that miss — try a shear and the quarter-turn — and
  what would reaching them cost?
- **My two open questions** from the dictation, both in the [Live table](../questions.md#live):
  - «я вот не понимаю, что мы теряем, если мы выкидываем вот это свойство» — what is lost without
    multiplicativity?
  - «Но почему тоже полиномиальную функцию? Тоже … непонятно.» — why a polynomial? Road 1's
    complex-roots argument was given in October and has not become mine.
- **What a column addition changes** — opened here, worked in [shears](shear.md).
- **The volume line.** That alternating $n$-forms make a one-dimensional space is my Levi-Civita
  page; reading it as "the line every map keeps", with $\det \hat A$ the factor on it, was given
  on 2026-10-26 and again on 2026-11-01. **Not yet derived.**
- **Eigenvalues do not compose** — two shears with only the eigenvalue 1 whose product stretches
  by about $2.62$ and $0.38$. Given. Cold-check: multiply them and find the eigenvalues.
- **4.1 for maps** — a shear is conjugate to its square, so every shear is a commutator and has
  size 1 — given whole in reply to "I'm not sure how to move to 4.1 section and further".
  **Not yet derived.** The shear sessions rebuild its pieces.
- **Trap**: "invertible, so the size does not change" — in
  [practice](../practice/size-of-a-map.md).

## Derived / proved myself

- 2026-11-01 — from multiplicativity alone: $D(\hat I) \in \{0, 1\}$; $D(\hat A^{-1}) = 1/D(\hat A)$;
  $D(\hat P^{-1}\hat A\hat P) = D(\hat A)$. **Derived unaided.** That $D(\hat I) = 0$ has to be ruled
  out was pointed out; on 2026-11-03 I gave the reason in my own words — «умножая на любое, другое
  преобразование identity и получая то же самое преобразование, будем получать снова 0».
