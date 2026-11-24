# Shears — what does adding one column to another leave unchanged?

**Status:** open
**Opened:** 2026-11-03  **Last touched:** 2026-11-14

Practice: [practice/shear.md](../practice/shear.md) · Comes from:
[the size of a map](size-of-a-map.md) · Material outside this repository: a three-page recap of my
own recap page, and a ten-minute explainer video, both made by Claude. Material, not evidence.

Notation: a hat marks a map, no hat its matrix. $H$ is a hyperplane, $\varphi$ a linear function
with $\ker\varphi = H$, and a map fixing $H$ pointwise is written $\hat G x = x + \varphi(x)\,w$.

## The question that opened it

Dictating my way through Road 3, at the column operations I had always used as a given:

> «А вот сейчас я думаю, а что, блин, ничего не менялось? Что это значит, что у нас ничего не
> меняется?»

*What does it mean that nothing changes?* And what drew me in: «Мне очень нравится, как оператор
сдвига задается через линейную функцию» — I like how the shear is built from a linear function.

In English, opening both sessions: "I realized that I'm not 100% confident with translation
operator. Help me to get more familiar with it and get more intuition and understanding through
the socratic approach", and "I want a route that would motivate and build the operator and then
the one that would go further to build the intuition".

The stake: [the size of a map](size-of-a-map.md) needs a shear to have size 1, and that is what
"nothing changes" means — the map changes, its size does not.

A naming point that matters for searching: «сдвиг» covers both. A translation $x \mapsto x + b$ is
not linear; $x \mapsto x + \varphi(x)\,w$ with $\varphi(w) = 0$ is a **shear**, or transvection.

## Attached to

- **Column operations as composition**: adding a multiple of one column to another replaces
  $\hat A$ by $\hat A \circ \hat T$ — from the Road 3 note. Problem 1 started there.
- **[Direct sums and complements](../notes/linear-algebra/direct-sums-and-complements.md)**:
  $V = H \oplus \langle u \rangle$ was my own first move for the general form.
- **[Quotient spaces](../notes/linear-algebra/quotient-spaces.md)**: $\varphi(x)$ as the height of
  $x$ above $H$, a coordinate on the line $V/H$. Supplied, as the basis-free reading of my item-4
  sentence.
- **The determinant thread**: the inverse I derived assumed it existed — the same trap as the sign
  of an ordering in [where the determinant comes from](where-the-determinant-comes-from.md#still-loose).

## Where else this shows up

- **The 4.1 trick, explained.** Shears along one hyperplane compose by adding their slides, so
  squaring one doubles its slide — the conjugation in [the size of a map](size-of-a-map.md) is
  "$w + w = 2w$". Given.
- **Projection without an inner product needs a direction.** The non-invertible member is a
  projection onto $H$ *along* a line, and "the component in $H$" depends on which line. The reflex
  that a projection is orthogonal comes from my [PCA anchor](../profile.md#anchors-worth-building-on).
- **What eigenvectors cannot see.** A shear has no eigenvector outside $H$ — the case Road 3 §10
  asks about.
- Named in the video, not worked: the shear as a stack of translations and Cavalieri's principle,
  homogeneous coordinates, a shear as $e^N$ with $\operatorname{tr} N = 0$, and three shears
  composing to a quarter-turn.

## How I could have come up with this

- **The general form**, from my recap: "It is also quite clear how this operator actually works.
  Let's say we have x = h + αu, then T̂h = h (leave it as is) and T̂u = u + w (move it in w
  direction). So it's only natural that T̂u and w would be the center of our attention."
- **What the one number measures**: "It says that u component of x is strestched in s times after
  the application of G". Right in content; the version that does not depend on $u$ — every height
  above $H$ multiplied by $s$ — was supplied.
- **Why $\varphi(w) = 0$ picks out the shears** — not yet mine. My first reading: "I could make it
  Te3 = ce3 + e3 instead and would get cx3 as phi and w as e3. I see nothing criminal in this move.
  And it feels like it is still shear in a way".

## Still loose

- **Problem 2(d), not started.** Fix the slide $w$ and vary the function: $x + \psi(x)\,w$ over all
  $\psi$ with $\psi(w) = 0$. What do these do under composition, and what plays the role that $H$
  played?
- **Problem 2(a) and (c)**: that the shears along one $H$, with $\varphi$ fixed, compose by adding
  slides, are injective in $w$, and form a group isomorphic to $(H, +)$ — given as the correction
  to my attempt. **Not yet derived.** Cold-check: with $\varphi$ fixed once, compose two of them
  and say where $\varphi(w') = 0$ is used.
- **The stretch factor**: that the invariant line's factor is $1 + \varphi(w)$ was supplied, after I
  had found the line. **Not yet derived.**
- **Uniqueness of the pair $(\varphi, w)$**: "It's easy let's move forward" — skipped; the answer
  was stated for the record. **Not yet derived.**
- **The Cowork Question 2**: replace $e_i$ by $e_i + e_j$ and keep the rest — does the $j$-th
  coordinate of a fixed vector change? Which basis vectors does a single coordinate really depend
  on? Open since 2026-11-03.
- **Are any two shears conjugate**, and what would that say about $D$ on shears without using a
  stretch? Set in the Road 3 conversation on 2026-11-03; the shear sessions followed another plan.
- **The whole picture first.** "Okay, I realised that I need to first get the whole idea of what is
  going on before I approach the problems myself." The video was the answer to that. Whether it
  gave the map the problems lacked is for the next session to find out.
- **Traps**, each in [practice](../practice/shear.md):
  - *Fixed vectors for an invariant line* — "Okay, so the question is about vectors that stay on the
    line not those that are fixed".
  - *A candidate taken for an inverse* — "But I basically present the inverse, don't I? Isn't it the
    same as proving that it exists?"
  - *"The component in $H$"* without a chosen complement — "but u does not have a component in H.
    How do I shouw that hu is zero".
  - *Cancelling a map* that need not be injective — both of my first two pages for 1(a).

## Derived / proved myself

- 2026-11-03 (Cowork) — the vectors a column operation fixes, and how the rest move, from my board:
  "Obviously those that have a zero x_j projection". **Derived unaided.**
- 2026-11-03 to 14 — Problem 1(a): the map behind "add $c$ times column 1 to column 3" sends $e_3$ to
  $ce_1 + e_3$ and fixes $e_1, e_2$; it fixes the plane $x_3 = 0$; everything else moves along $e_1$;
  $\varphi(x) = cx_3$, $w = e_1$. **Derived unaided** except one step: my own doubt — "I'm not sure
  there is no other T that would work for it" — was right, and the fix (the operation must work for
  every $\hat A$, so take $\hat A = \hat I$) was supplied.
- 2026-11-03 to 14 — Problem 1(b): every map fixing a hyperplane pointwise is
  $x + \varphi(x)\,w$, from $V = H \oplus \langle u \rangle$:
  $\hat G x = x + \alpha\,[t_1 v + (t_2 - 1)u]$. **Derived unaided.** The simplification
  $w = \hat G u - u$ was supplied.
- 2026-11-03 to 14 — item 1: a line outside $H$ that $\hat G$ maps to itself must be the line of
  $w$, from $x = \frac{\alpha}{s-1}\,w$. **Derived unaided** once the difference between a line
  mapped to itself and a line of fixed vectors had been pointed out.
- 2026-11-03 to 14 — item 2: for $\varphi(w) = 0$, $w \neq 0$, no line outside $H$ is mapped to
  itself, and $\hat G^{-1} y = y - \varphi(y)\,w$, found and then checked as $\hat K\hat G = \hat I$.
  **Derived unaided**; that a one-sided check suffices in finite dimensions was supplied.
- 2026-11-03 to 14 — item 3: $\hat G$ fails to be invertible when $\varphi(w) = -1$, and its image
  lies in $H$; in my recap, "makes sense it is not invertible as dim(Im T̂) = dim H = n − 1".
  **Derived unaided** from $\hat G w = 0$; that this is the *only* such case, and the name
  (projection onto $H$ along $w$), were supplied.
- 2026-11-03 to 14 — item 4: $t_2 = \varphi(\hat G u) = 1 + \varphi(w)$; it does not depend on the
  choice of $u$, through $\varphi = \lambda\varphi'$; and $\varphi(\hat G x) = s\,\varphi(x)$.
  **Derived unaided**, one line skipped.
- 2026-11-03 to 14 — Problem 2(b): powers and the inverse of a shear along a fixed $\varphi$.
  **Derived unaided**, with the cross term that $\varphi(w) = 0$ removes skipped.
