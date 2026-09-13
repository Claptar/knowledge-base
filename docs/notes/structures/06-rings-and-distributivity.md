---
title: "6. Rings and Distributivity"
---

> **Imported note.** Written by me with an AI assistant in [Claptar/math-notes](https://github.com/Claptar/math-notes), imported 2026-09-13. It is *material* — my own exposition — not a record of a worked session. Nothing here is evidence that it has been derived from scratch; a [topic file](../../questions.md) is earned separately.

# 6. Rings and Distributivity

## Definition

A **ring** is a set $R$ with two binary operations, usually called addition and multiplication, such that:

1. $(R,+)$ is an abelian group;
2. multiplication is associative;
3. multiplication distributes over addition:

$$
a(b+c)=ab+ac,
$$
and

$$
(a+b)c=ac+bc.
$$
Some authors require a multiplicative identity $1$; some do not. These notes focus on the conceptual role of the two operations and distributivity.

## Central intuition

A ring is a structure where objects can be both **added** and **multiplied**, and multiplication respects addition.

Addition represents combining contributions.

Multiplication represents interaction, composition, scaling, or product formation.

Distributivity is the bridge between them.

## Why two operations?

One operation gives one kind of composition.

Two operations allow two different modes:

| Operation | Typical meaning |
|---|---|
| Addition | accumulation, superposition, sum of contributions |
| Multiplication | interaction, scaling, composition, product |

Many mathematical worlds naturally have both:

- integers;
- polynomials;
- functions;
- matrices;
- operators.

## The intuition of distributivity

The key law is

$$
a(b+c)=ab+ac.
$$
It says:

> If something is decomposed as a sum of parts, then multiplying it by $a$ can be done part by part.

Equivalently:

> Multiplication is compatible with decomposition into additive contributions.

This is the central meaning of distributivity.

## Distributivity as “working by parts”

If $b+c$ is a whole made of two contributions, then $a(b+c)$ means letting $a$ interact with the whole.

Distributivity says this is the same as:

1. let $a$ interact with $b$;
2. let $a$ interact with $c$;
3. add the results.

So distributivity is the principle:

> The whole can be computed from its parts.

## Geometric example: area

A rectangle of height $a$ and width $b+c$ has area

$$
a(b+c).
$$
If we cut it into two rectangles of widths $b$ and $c$, the areas are

$$
ab
\quad\text{and}\quad
ac.
$$
The total area is

$$
ab+ac.
$$
So

$$
a(b+c)=ab+ac.
$$
Here distributivity says: area of the whole is the sum of the areas of the parts.

## Linear interpretation

For fixed $a$, the map

$$
x\mapsto ax
$$
preserves addition:

$$
a(x+y)=ax+ay.
$$
So multiplication by $a$ is a homomorphism of the additive group.

In other words:

> Multiplication acts linearly on the additive world.

This is why rings connect so strongly with linear algebra.

## What breaks without distributivity

If addition and multiplication are not connected by distributivity, then they are almost two unrelated operations on the same set.

We lose:

- expansion of brackets;
- factoring;
- polynomial algebra;
- ideals;
- quotient rings;
- modules;
- the usual manipulation of algebraic expressions.

Without distributivity, expressions like

$$
a(b+c)
\quad\text{and}\quad
ab+ac
$$
need not have any relationship.

## Natural examples of rings

### Integers

$$
\mathbb Z
$$
with ordinary addition and multiplication is the prototypical ring.

### Polynomials

$$
K[x]
$$
is a ring. Addition combines coefficients, multiplication combines powers and coefficients.

### Matrices

$$
M_n(K)
$$
is a ring under matrix addition and multiplication.

Multiplication is generally non-commutative, but it is associative and distributive over addition.

### Functions

Functions $X\to K$ form a ring under pointwise operations:

$$
(f+g)(x)=f(x)+g(x),
$$
$$
(fg)(x)=f(x)g(x).
$$
## Alternatives to distributivity

Distributivity is not the only possible compatibility law between two operations.

Other structures use different laws.

### No compatibility

One can simply put two operations on a set without requiring a relation. This is possible but usually too weak to support a rich theory.

### One-sided distributivity

Some structures require only one distributive law, such as

$$
a(b+c)=ab+ac,
$$
but not necessarily

$$
(a+b)c=ac+bc.
$$
These lead to structures such as near-rings.

### Absorption laws

Lattices use operations $\vee$ and $\wedge$ with absorption laws:

$$
a\vee(a\wedge b)=a,
$$
$$
a\wedge(a\vee b)=a.
$$
This models union/intersection-like behavior rather than addition/multiplication-like behavior.

### Mutual distributivity

Boolean algebras have two operations that distribute over each other, reflecting logical AND/OR or intersection/union.

## Place in the build-up

Rings are where algebra becomes the study of expressions involving both addition and multiplication:

$$
a^2+ab+b^2,
\quad
(a+b)(c+d),
\quad
x^3-2x+5.
$$
They are the natural setting for arithmetic, polynomials, matrices, and many algebraic constructions.

The next step is to ask when multiplication is as well-behaved as possible. That leads to fields.


{% include chapter-nav.html %}
