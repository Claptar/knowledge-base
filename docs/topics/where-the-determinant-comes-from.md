# The determinant — can I come up with the operation itself?

**Status:** open
**Opened:** 2026-10-23  **Last touched:** 2026-10-26

Practice: [practice/where-the-determinant-comes-from.md](../practice/where-the-determinant-comes-from.md)
· Continues as: [the size of a map](size-of-a-map.md) and [shears](shear.md) · Material outside
this repository, written by Claude during the sessions: *Determinants from the question up* and
*Four roads to the determinant* (four PDFs and a page). Material, not evidence.

## The question that opened it

The thread came out of my tensor-analysis work: in 3D I had $\det A = \varepsilon_{ijk}A_{1i}A_{2j}A_{3k}$
from a volume function $T$ — linear in each argument (M), zero when two arguments are equal (A).
Asked to go on to $n$ dimensions, I corrected the record first:

> "Well, it's not really that I found this. It's more like I took eijk a1ia2ja3k and showed that it
> is a determinant. Not like it was a proper derivation of determinant"

> "Ideally I would want to come up with the operation itself and not just check it's definition."

Asked what one number could tell me about a square matrix $A$, my answer was the stake: "Whether
there are any dependent rows?" So the determinant became a **dependence detector**, and Step 1 was
to build one in $n$ dimensions from (M) and (A) alone.

Where the thread was heading, and has not reached: a closed form for
$\det\big(\operatorname{diag}(p) - pp^\top\big)$, the singular covariance behind Pearson's χ² — the
statistics chapter 9–10 question in the [Live table](../questions.md#live). The page where I
derived the $n$-dimensional $T$ is in the notebook headed «Статистика 9-10».

Then, once the properties had piled up — (M), (A), (R2), (R3), (N), "polynomial in the entries",
"linear in each row" — the question changed from *how* to *why*:

> "I feel like we want to build something, but those properties/features are just jumping at me
> without any reason for that?"

> "I'm well familiar with determinant itself as I studies linear algebra, differential equations,
> quantum mechanics and so on, but I want to see more fundamental reason for what is going on here
> and what could actually be done differentely and what are the consicuensies of that"

The rest of that message — the goal, the most basic function, why anything more — is the way I
want motivation built, and lives in [profile.md](../profile.md#the-four-goals).

## Attached to

- **My 3D Levi-Civita work** ([tensor-analysis notes](../profile.md#anchors-worth-building-on)): the
  $27 \to 1$ count, the $e_1+e_2$ trick that makes a swap flip the sign, and the "$p=q$" page where
  the six terms cancel in pairs. Step 1 is those three moves in $n$ dimensions. The converse is the
  same expansion with the rows as the basis instead of the $e$'s.
- **The determinant as a tool** — linear algebra, ODEs, quantum mechanics. Known well as a thing to
  compute; not, until now, as the answer to a question.
- **Volume in a bare vector space.** My question mid-converse: "here in linear spaces we do not
  really have a notion of volume? (or do we?!)". The answer given — a nonzero alternating $n$-form
  *is* volume, up to a unit — is **Not yet derived.** It became [the size of a map](size-of-a-map.md).

## Where else this shows up

From the sessions; the outbound question was not asked separately.

- **The χ² chapter** — the destination above: a determinant that is a polynomial in $p$, whose
  factors would say exactly which $p$ make the covariance singular.
- **Solving equations.** Cramer's rule falls out of (M) and (A) — put $b$ in place of row $i$ and
  every other term repeats a row. Given, in answer to "why these features". Road 2 of the four
  roads reads $\det$ as the denominator of the inverse.
- **Eigenvalues** as the roots of $\det(A - \lambda I)$. Given.
- **Complexity.** The same sum over orderings without the sign is the permanent: multilinear, but
  it does not detect dependence and is #P-hard to compute (Valiant 1979), while $\det$ takes about
  $n^3$ steps. "The sign is exactly what buys both detection and fast computation." Given.
- **Change of variables for densities**, a linear map rescaling probability by $1/|\det A|$ —
  mentioned at the end of the four roads, and then raised by me as the reason to ask about the
  [size of a map](size-of-a-map.md).

## How I could have come up with this

- **The question.** "Whether there are any dependent rows?" — mine, and the inbound half: a single
  number that says whether a system has a unique solution.
- **(A)**, from my margin note on page 89: "this is clearly to target collinear vectors". Equal
  rows are the simplest dependence.
- **(M)** — not yet. My margin note next to it: "But this is less clear for me… I can accept it,
  but not defend out loud". The pending problem in *Still loose* is where it would become mine.
- **The ladder of wishes** — detector, then the simplest detector (an indicator, which is a label
  rather than a test), then "one polynomial in the entries" from the $2 \times 2$ elimination, then
  what that wish forces — was given, on my request. My verdict on it: "here you guessed polynomial
  from n=2 and show that all properties we want are actually either present either have a
  reasonable necessity". **Not yet derived.** The four roads were given when I asked "I wonder if
  there is any other approach?".

## Still loose

- **The pending problem, set twice and not yet tried.** All I know of a function $D$ of the rows:
  scaling one row by $c$ multiplies $D$ by $c$ (R2), adding a multiple of one row to another leaves
  $D$ unchanged (R3), and $D(I) = 1$ (N). Show $D = \det$: a swap flips the sign (build it from
  three row additions and one scaling by $-1$), dependent rows give $0$, and elimination to $I$
  fixes the rest. It is wanted because it would make (M) a consequence — the margin note above.
  My objection before trying it was fair and is still open in part: "But these R2 and R3 are still
  motivated by geometrical (euclidean) notion of volume".
- **Why a polynomial at all.** Road 1's answer — a polynomial that never vanishes on independent
  rows, over the complex numbers, cannot change under a row addition — was given, not derived. I
  was still asking in November; see [the size of a map](size-of-a-map.md#still-loose).
- **The converse** — independent rows give a nonzero value for any nonzero $T$ — was given on
  request. **Not yet derived.** Cold-check: in the row basis, what can each term of the expansion
  be?
- **Step 3**, the χ² determinant. Not started.
- **Traps**, each in [practice](../practice/where-the-determinant-comes-from.md):
  - *Uniqueness taken for existence* — "What is there to prove, if it could be done with both o1
    and o2 then betta_123..n = (-1) ^ o1 * beta = (-1) ^ o2 * beta which would mean that beta = 0".
    The implication was right; it describes the case where no nonzero $T$ exists. Deriving what
    something must look like does not show that it exists. The same trap came back with the
    [shear's inverse](shear.md#still-loose).
  - *A fact about $T$ taken for a fact about orderings* — "in my note above I've shown that any
    swap of two entries changes it by -1, have I not?"
  - *The shortest route* — "I should have obviously taked about the shortest permutation here".
    Right in kind: the sign needs a quantity read off the ordering itself. But proving that the
    shortest length changes parity at each swap is the original problem again.
  - *An argument that never uses its hypothesis* — the existence pairing as I first wrote it would
    have shown $D = 0$ for every input, including $D(e_1,\dots,e_n) = 1$.

## Derived / proved myself

The transcript is dated only at its start, 2026-10-23; Steps 1–2 ran over that and the next days.

- 2026-10-23 — dependent rows give $T(\text{rows}) = 0$, from (M) and (A) alone, no formula: "if we
  have an entry that is linear combination of all other ones we could use the liniarity and split
  it into n-1 entries with duplicated entries so that the final result is 0". **Derived unaided.**
- 2026-10-23 — an ordering reachable by both an even and an odd number of swaps would force
  $\beta_{12\dots n} = 0$: "that ordering would be both +$\beta_{12\dots n}$ and
  -$\beta_{12\dots n}$". **Derived unaided.**
- 2026-10-23 — page 89: $T$ in $n$ dimensions from (M) and (A) — expand in a basis, only the $n!$
  non-repeating terms survive, a swap flips the sign — so
  $T(v_1,\dots,v_n) = \sum \varepsilon_{i_1\dots i_n} v_{1i_1}\cdots v_{ni_n}\,\beta_{12\dots n}$.
  The uniqueness half. **Derived unaided.** The swap line had both sides written identically, and
  the repeated terms' signs flipped when moved across; both fixed after the check, neither changed
  the result.
- 2026-10-23 — the sign of an ordering is well defined: a swap of neighbours changes the inversion
  count by $\pm 1$, a swap of positions $p, q$ by $1 + 2k$. **Derived unaided** from the inversion
  count on; the count itself, and the idea of a quantity that changes parity at every swap, were
  supplied. I asked where my mistake was; there was none.
- 2026-10-23 — the existence half: pairing each ordering with the one that swaps positions $p$ and
  $q$, opposite signs. **Derived unaided** as far as the pairing and the signs; that the two
  products are equal *because* the two rows are equal was supplied.
- 2026-10-23 — Step 2: adding a multiple of one row to another leaves $\det$ unchanged, from (M)
  and (A); an upper triangular $\det$ is the product of the diagonal, by forcing $\sigma_n = n$
  first and working back; $\det A = -5$ for a $3 \times 3$ by elimination, checked against the six
  terms. **Derived unaided**, all three, first attempt.
