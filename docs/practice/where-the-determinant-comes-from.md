# The determinant — practice

Attempts from the sessions in
[topics/where-the-determinant-comes-from.md](../topics/where-the-determinant-comes-from.md). The
transcript (claude.ai, 2026-10-23 on) is dated only at its start, so entries carry that date.
Handwritten pages are known from the transcript's descriptions of them, not as images.

## 2026-10-23 — does $T$ notice dependent rows?

**Problem:** with no formula for $T$ in $n$ dimensions, only (M) and (A), does $T(\text{rows}) = 0$
when the rows are dependent?
**Worked unaided up to:** all of it. "in the definition we put it to be zero whenever there are
duplicated entries. And if we have an entry that is linear combination of all other ones we could
use the liniarity and split it into n-1 entries with duplicated entries so that the final result is
0". **Derived unaided.**
**Where I asked for a hint:** none.
**Attempt:** first, "Not sure, I haven't build T for n dimensional case yet" — then the argument
from the properties.
**Outcome:** solved.
**What it revealed:** the properties were enough without a formula; the first reflex was to wait
for one.
**Revisit:** —

## 2026-10-23 — the converse: independent rows and $T(\text{rows}) = 0$

**Problem:** if the rows are independent and $T(\text{rows}) = 0$, show that $T \equiv 0$.
**Worked unaided up to:** the right statement — "for rows to retain their independence all
bij..k should also be 0. And if it is not, then the rows should be dependent" — and nearly the
idea: "If I had the formula for n dimensional T in the basis row1, ..., rown … then we would see
that b123...n supposed to be 0."
**Where I asked for a hint:** the questions were vague ("I'm not sure, the question is rather
vague"); then "Okay, just give me what you have in mind this time". The proof was given, and again
in 3D after "This is a bit cryptic". **Not yet derived.**
**Attempt:** expanded $T$ in the $e$'s and tried to manufacture coefficients $\gamma$ with
$\sum_k a_{ik}\gamma_k = 0$: "Hmm, I thought I would be able to show that we have 0 combinations for
all rows or columns but something seems to be missing".
**Outcome:** stuck; given on request.
**What it revealed:** the row-basis idea was there, but held only through the formula. The
formula-free version is my own $27 \to 1$ count with the rows standing in for the $e$'s: each term
is $0$ or $\pm$ one value. The $\gamma$ route builds a relation among columns, not rows, and needs
one $\gamma$ that works for every $i$. Partly a session failure: the purpose of each question was
hidden.
**Revisit:** cold — in the row basis, what can each term of the expansion be?

## 2026-10-23 — could the sign be inconsistent?

**Problem:** if some ordering of $(1,\dots,n)$ could be reached by both an even and an odd number
of swaps, what would that force $\beta_{12\dots n}$ to be? Then: show no ordering can.
**Worked unaided up to:** the first part, at once. **Derived unaided.**
**Where I asked for a hint:** "Okay, I'm confused, use more words to word the problem please". The
inversion count was then supplied as the quantity to use, unasked.
**Attempt:** "What is there to prove, if it could be done with both o1 and o2 then betta_123..n =
(-1) ^ o1 * beta = (-1) ^ o2 * beta which would mean that beta = 0". Then "I should have obviously
taked about the shortest permutation here".
**Outcome:** the implication right; the existence question not seen.
**What it revealed:** uniqueness taken for existence. Everything so far had the form *if a nonzero
$T$ exists, it looks like this*, and my implication described the case where none does. The
session never said that the open part was existence — a session failure first. The shortest-route
instinct is right in kind: the sign needs a number read off the ordering, not off a route.
**Revisit:** —

## 2026-10-23 — page 89: $T$ in $n$ dimensions

**Problem:** Step 1 — the $n$-dimensional formula from (M) and (A).
**Worked unaided up to:** the whole uniqueness half: expand in a basis, keep the $n!$
non-repeating terms, a swap flips the sign, so $T = \sum \varepsilon \prod v \cdot \beta_{12\dots n}$.
**Derived unaided.**
**Where I asked for a hint:** none. Asked "This should resolve (a)???" — it did not.
**Attempt:** the page, with margin notes: next to (M), "But this is less clear for me… I can accept
it, but not defend out loud"; next to (A), "this is clearly to target collinear vectors".
**Outcome:** solved, two slips fixed: the swap line had both sides identical (so it read $T = -T$),
and the repeated terms' signs when moved across.
**What it revealed:** "in my note above I've shown that any swap of two entries changes it by -1,
have I not?" — a fact about $T$ (a swap flips its sign) taken for a fact about orderings (no odd
number of swaps returns $(1,\dots,n)$ to itself). The sign rule is consistent only if there are no
odd loops — the picture supplied was colouring a triangle's corners so neighbours differ.
**Revisit:** —

## 2026-10-23 — a swap changes the inversion count by an odd number

**Problem:** with $\operatorname{inv}(\sigma)$ the number of out-of-order pairs (supplied): a
neighbour swap changes it by $\pm 1$, any swap by an odd number.
**Worked unaided up to:** all of it — the neighbour case, and a swap of $p < q$ giving
$\operatorname{inv}(\sigma) + 1 + 2k$. **Derived unaided** from the definition of the count on.
**Where I asked for a hint:** "Help me locate my mistake please". There was no mistake.
**Attempt:** the handwritten proof, with $r$ and $k$ bookkeeping.
**Outcome:** solved. Tidying only: $q - p - r$ for $q - p - 1 - r$ in the words; the reason the
other pairs are unaffected left unsaid; the other case only implied.
**What it revealed:** the capability — a correct, complete proof that I read as wrong. The
shortcut was already on my page ($2(q-p) - 1$ neighbour swaps, each $\pm 1$) and I did the exact
count instead.
**Revisit:** —

## 2026-10-23 — existence: the formula vanishes on equal rows

**Problem:** show $\sum_\sigma \varepsilon_\sigma v_{1\sigma_1}\cdots v_{n\sigma_n} = 0$ when
$v_p = v_q$, $p \neq q$.
**Worked unaided up to:** the pairing and the signs: "For each ordering sigma there exists an
exactly one ordering sigma' that have sigmap and sigmaq swapped and as proved above those would
have different signs. So all of them would cancel each other". **Derived unaided** that far.
**Where I asked for a hint:** first "Why do we want to show this?" — the purpose was missing, and
the answer was a session repair (squaring $\sqrt{x+2} = x$ and plugging back). That the paired
products are equal because $v_p = v_q$ was supplied.
**Outcome:** solved with one line supplied.
**What it revealed:** an argument that never uses its hypothesis proves too much — this one would
have killed $D(e_1,\dots,e_n) = 1$. Check: *where does the hypothesis enter?* The same check is
what found the gaps in the [shear sessions](shear.md).
**Revisit:** —

## 2026-10-23 — Step 2: row operations, and a $3 \times 3$

**Problem:** (a) from (M) and (A), adding $c$ times row $j$ to row $i$ leaves $\det$ unchanged;
(b) an upper triangular $\det$ is the product of its diagonal; (c) reduce a given $3 \times 3$ to
triangular form, track each operation, read off $\det$, check against the six-term formula.
**Worked unaided up to:** all three. **Derived unaided.**
**Where I asked for a hint:** none.
**Attempt:** one handwritten page; (b) by the backward argument, $\sigma_n = n$ forced first.
**Outcome:** solved, first attempt; $\det A = -5$ both ways.
**What it revealed:** the capability. This was the first step posed as one problem with its goal
stated, after the retrospective; the whole step went through unaided.
**Revisit:** —

## 2026-10-23 — reading the $2 \times 2$ dependence test

**Problem:** not a problem — reading why "dependent exactly when $ad - bc = 0$" comes from the
definition of dependence alone.
**Where I asked for a hint:** "I do not understand"; then "'Nothing skipped' but you skipped your
define what is s and t".
**Outcome:** "Oh, I see, s(a,b) is not s of (a,b) but s * [a, b] where (a,b) is a row".
**What it revealed:** a session failure, not a gap: $s(a,b)$ written beside $T(u,v)$, where the
same shape means a function applied to arguments.
**Revisit:** —
