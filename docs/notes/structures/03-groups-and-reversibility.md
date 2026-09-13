---
title: "3. Groups and Reversibility"
---

> **Imported note.** Written by me with an AI assistant in [Claptar/math-notes](https://github.com/Claptar/math-notes), imported 2026-09-13. It is *material* — my own exposition — not a record of a worked session. Nothing here is evidence that it has been derived from scratch; a [topic file](../../questions.md) is earned separately.

# 3. Groups and Reversibility

## Definition

A **group** is a monoid $G$ such that every element has an inverse.

That is, for every $a\in G$, there exists $a^{-1}\in G$ with

$$
aa^{-1}=a^{-1}a=e.
$$
## Central intuition

A group is the algebra of **reversible actions**.

A monoid describes actions that can be composed and includes a “do nothing” action. A group adds the requirement that every action can be undone.

So:

| Structure | Intuition |
|---|---|
| Semigroup | compose non-empty processes |
| Monoid | compose processes including doing nothing |
| Group | compose reversible processes |

## What inverses buy us

### Undoing actions

If $a$ is an action, $a^{-1}$ is the action that cancels it.

This means elements of a group do not destroy information.

### Solving equations

In a group, the equation

$$
ax=b
$$
has the unique solution

$$
x=a^{-1}b.
$$
Similarly,

$$
ya=b
$$
has the unique solution

$$
y=ba^{-1}.
$$
This is one of the main algebraic powers of inverses: they allow division-like reasoning.

### Cancellation

If

$$
ax=ay,
$$
then multiplying on the left by $a^{-1}$ gives

$$
x=y.
$$
Groups always have cancellation.

### Negative powers

In a monoid we have

$$
a^0,a^1,a^2,\dots
$$
In a group we also have

$$
a^{-1},a^{-2},\dots
$$
So powers are indexed by all integers:

$$
a^n,
\qquad n\in\mathbb Z.
$$
## What breaks without inverses

Without inverses, actions may be irreversible.

We may lose:

- general solvability of equations;
- cancellation;
- negative powers;
- symmetry interpretation;
- the ability to recover earlier states.

For example, a non-injective function can collapse two inputs into one output. Once collapsed, the original information cannot be recovered.

## Natural examples of groups

### Integers under addition

$$
(\mathbb Z,+)
$$
is a group. The inverse of $n$ is $-n$.

This models reversible displacement along a line.

### Nonzero real numbers under multiplication

$$
(\mathbb R^\times,\cdot)
$$
is a group. The inverse of $a\neq 0$ is $1/a$.

This models reversible scaling.

### Permutations

All permutations of a set form a group under composition.

Every permutation is reversible.

### Invertible matrices

Invertible $n\times n$ matrices over a field form a group:

$$
GL_n(K).
$$
These are exactly the linear transformations that lose no information.

## Natural monoids that are not groups

### Natural numbers under addition

$$
(\mathbb N,+)
$$
is a monoid but not a group, because adding $5$ cannot be undone inside $\mathbb N$.

Passing from $\mathbb N$ to $\mathbb Z$ can be viewed as adding formal additive inverses.

### All functions $X\to X$

All functions form a monoid under composition, but not a group. Only bijections are invertible.

### All square matrices

All square matrices form a monoid under multiplication, but singular matrices are not invertible.

## Place in the build-up

The group is the point where algebra begins to model symmetry.

A group is not merely “a monoid with more axioms.” It is a shift from general actions to reversible actions.

This leads naturally to the next idea: symmetries of objects.


{% include chapter-nav.html %}
