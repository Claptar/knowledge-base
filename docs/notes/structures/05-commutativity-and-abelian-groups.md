---
title: "5. Commutativity and Abelian Groups"
---

> **Imported note.** Written by me with an AI assistant in [Claptar/math-notes](https://github.com/Claptar/math-notes), imported 2026-09-13. It is *material* — my own exposition — not a record of a worked session. Nothing here is evidence that it has been derived from scratch; a [topic file](../../questions.md) is earned separately.

# 5. Commutativity and Abelian Groups

## Definition

A binary operation is **commutative** if

$$
ab=ba
$$
for all elements $a,b$.

A group whose operation is commutative is called an **abelian group**.

## Central intuition

Commutativity says that order does not matter.

If associativity lets us ignore parentheses, commutativity lets us ignore the order of the factors or summands.

So:

- associativity turns expressions into sequences;
- commutativity turns sequences into unordered collections of contributions.

## What commutativity buys us

### Order independence

In a non-commutative group,

$$
abc,
\quad acb,
\quad bac
$$
may all be different.

In an abelian group, all rearrangements give the same result.

### The language of contributions

Commutative operations often model independent contributions:

- adding forces;
- adding balances;
- adding vectors;
- combining charges;
- accumulating quantities.

If order does not matter, elements behave less like actions in time and more like contributions to a total.

### Simpler structure

Abelian groups are much easier to analyze than arbitrary groups.

For example, finitely generated abelian groups admit a complete classification. General groups are far more complicated.

## What we lose without commutativity

Without commutativity, order matters.

This is not merely a nuisance. It models real phenomena:

- rotations in 3D do not generally commute;
- matrix multiplication is usually non-commutative;
- permutations do not usually commute;
- doing actions in different orders can produce different outcomes.

Non-commutativity is the algebraic language of order-sensitive processes.

## Natural examples of abelian groups

### Integers under addition

$$
(\mathbb Z,+)
$$
is the basic abelian group.

It models reversible one-dimensional displacement.

### Real vector spaces under addition

$$
(\mathbb R^n,+)
$$
is an abelian group.

Geometrically, moving by $u$ and then $v$ ends at the same point as moving by $v$ and then $u$.

### Numbers under addition

$$
(\mathbb Q,+),
\quad (\mathbb R,+),
\quad (\mathbb C,+)
$$
are abelian groups.

### Nonzero numbers under multiplication

$$
(\mathbb R^\times,\cdot),
\quad (\mathbb C^\times,\cdot)
$$
are abelian groups.

They model reversible scalar multiplication.

### Cyclic groups

Every cyclic group is abelian.

If every element has the form $g^n$, then

$$
g^m g^n=g^{m+n}=g^{n+m}=g^n g^m.
$$
Examples include $\mathbb Z$ and $\mathbb Z/n\mathbb Z$.

## Useful contrast: non-abelian groups

Groups of symmetries are often non-abelian.

For a square, rotating and then reflecting is generally different from reflecting and then rotating.

Thus:

- abelian groups model compatible reversible contributions;
- non-abelian groups model order-sensitive reversible actions.

## Place in the build-up

Commutativity is not as foundational as associativity.

Associativity is needed to make finite composition coherent. Commutativity is an additional simplification saying that the order of composition does not matter.

The next major step is to introduce two operations and ask how they interact. This leads to rings.


{% include chapter-nav.html %}
