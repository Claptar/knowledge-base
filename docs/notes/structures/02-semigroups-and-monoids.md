---
title: "2. Semigroups and Monoids"
---

> **Imported note.** Written by me with an AI assistant in [Claptar/math-notes](https://github.com/Claptar/math-notes), imported 2026-09-13. It is *material* — my own exposition — not a record of a worked session. Nothing here is evidence that it has been derived from scratch; a [topic file](../../questions.md) is earned separately.

# 2. Semigroups and Monoids

## Definitions

A **semigroup** is a set $S$ with an associative binary operation.

A **monoid** is a semigroup with an identity element $e$, meaning

$$
ea=ae=a
$$
for all $a\in S$.

## Central intuition

A semigroup is the algebra of **non-empty finite composition**.

A monoid is the algebra of **all finite composition**, including the empty composition.

The identity element represents the result of doing nothing.

So the difference is:

| Structure | Intuition |
|---|---|
| Semigroup | at least one step |
| Monoid | zero or more steps |

## What the identity element buys us

### Empty products

In a monoid, the empty product is defined to be the identity:

$$
\prod_{i=1}^{0} a_i=e.
$$
This is not just a convention. It is the algebraic version of “no factors were used.”

### Zero-th powers

In a monoid we can define

$$
a^0=e.
$$
Then the exponent law

$$
a^m a^n=a^{m+n}
$$
works even when $m$ or $n$ is zero.

### The empty action

If elements are actions, the identity is the action “do nothing.”

Examples:

- identity function;
- empty string;
- zero vector for addition;
- unit matrix;
- number $1$ for multiplication.

### A base point for inverses

To define an inverse, we need something to return to:

$$
aa^{-1}=a^{-1}a=e.
$$
So groups depend conceptually on monoids.

## What happens if we remove the identity

Going from monoid to semigroup removes the null action.

We lose:

- empty products;
- $a^0$;
- the general notion of inverse;
- the distinguished state of “nothing happened.”

But we may gain a more faithful model of processes that are necessarily non-empty.

## Natural semigroups where identity is not central

### Positive durations

$$
(0,\infty)
$$
under addition is a semigroup.

A positive duration plus a positive duration is a positive duration. The zero duration is a boundary case, not a genuine elapsed interval.

This naturally models processes that have actually taken positive time.

### Positive lengths, masses, or amounts

If objects are real nonzero pieces of material, lengths or masses may naturally be positive.

Combining two pieces adds their quantities, but the zero quantity may not be an object of the same kind.

### Non-empty event histories

Take finite non-empty logs of events:

```text
login, click, logout
```

Concatenation is associative. The empty history may be formally useful, but if we are studying actual observed episodes, we may choose to consider only non-empty histories.

### Positive-time evolution

In analysis, one often studies operators $T_t$ for $t>0$ satisfying

$$
T_tT_s=T_{t+s}.
$$
The interesting dynamics may live at positive times. The time $t=0$ can be a limiting or technical case rather than part of the main phenomenon.

## Adding an identity formally

Every semigroup $S$ can be enlarged to a monoid by adding a new element $1$:

$$
S^1=S\cup\{1\},
$$
with

$$
1s=s1=s.
$$
This shows that a monoid can often be seen as a semigroup completed by adding the empty step.

## Place in the build-up

The progression is:

$$
\text{semigroup} \to \text{monoid}.
$$
Conceptually:

- semigroup: composition of one or more steps;
- monoid: composition of zero or more steps.

The next step is to ask whether every step can be undone. That leads to groups.


{% include chapter-nav.html %}
