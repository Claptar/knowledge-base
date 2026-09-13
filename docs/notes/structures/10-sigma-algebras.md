---
title: "Sigma-Algebras"
---

> **Imported note.** Written by me with an AI assistant in [Claptar/math-notes](https://github.com/Claptar/math-notes), imported 2026-09-13. It is *material* — my own exposition — not a record of a worked session. Nothing here is evidence that it has been derived from scratch; a [topic file](../../questions.md) is earned separately.

# 10. Sigma-Algebras

## Warning about the word “algebra”

A **sigma-algebra** is not an algebra over a field in the sense of the previous chapter.

Here the word “algebra” refers to a family of sets closed under set operations.

So sigma-algebras belong primarily to measure theory and probability, not to the same line as groups, rings, fields, and vector-space algebras.

## Definition

Let $\Omega$ be a set.

A **sigma-algebra** $\mathcal F$ on $\Omega$ is a collection of subsets of $\Omega$ such that:

1. $\Omega\in\mathcal F$;
2. if $A\in\mathcal F$, then $A^c\in\mathcal F$;
3. if $A_1,A_2,A_3,\dots\in\mathcal F$, then

$$
\bigcup_{n=1}^{\infty}A_n\in\mathcal F.
$$
From this it follows that $\mathcal F$ is also closed under countable intersections and set differences.

## Central intuition

A sigma-algebra is a language of events.

If $\Omega$ is the set of possible outcomes, then $\mathcal F$ is the collection of events about which we are allowed to ask:

> Did this happen or not?

In probability, a probability measure is defined on a sigma-algebra:

$$
(\Omega,\mathcal F,\mathbb P).
$$
Here:

- $\Omega$ is the space of outcomes;
- $\mathcal F$ is the sigma-algebra of events;
- $\mathbb P$ assigns probabilities to those events.

## Why not just take all subsets?

If $\Omega$ is finite, taking all subsets is usually fine.

But for infinite spaces such as $\mathbb R$, taking all subsets can lead to pathological sets that cannot be assigned length, area, volume, or probability in a coherent way.

So measure theory chooses a sufficiently rich but controlled collection of measurable subsets.

That collection is a sigma-algebra.

## Why these axioms?

### Why include $\Omega$?

The certain event should be measurable.

In probability:

$$
\mathbb P(\Omega)=1.
$$
### Why close under complements?

If event $A$ is meaningful, then “not $A$” should also be meaningful.

### Why close under countable unions?

If $A_1,A_2,A_3,\dots$ are meaningful events, then the event

> at least one of them occurs

should also be meaningful.

This is the event

$$
\bigcup_{n=1}^{\infty}A_n.
$$
## Why countable operations?

The symbol $\sigma$ indicates countable closure.

Countable closure is essential because analysis and probability constantly use sequences and limits.

Events such as:

- “something happens eventually”;
- “something happens infinitely often”;
- “a sequence converges into a set”;
- “a random variable lies in some countable union of intervals”;

naturally involve countable unions and intersections.

## Sigma-algebras as information

A sigma-algebra can also represent the information available to an observer.

A small sigma-algebra means the observer can distinguish only coarse events.

A large sigma-algebra means the observer can distinguish more detailed events.

Example:

Let

$$
\Omega=\{1,2,3,4\}.
$$
The collection

$$
\mathcal F=\{\varnothing,\Omega,\{1,2\},\{3,4\}\}
$$
is a sigma-algebra.

It can distinguish whether the outcome lies in $\{1,2\}$ or $\{3,4\}$, but it cannot distinguish $1$ from $2$, or $3$ from $4$.

## Borel sigma-algebra

On $\mathbb R$, the most important sigma-algebra is the **Borel sigma-algebra**:

$$
\mathcal B(\mathbb R).
$$
It is the smallest sigma-algebra containing all open subsets of $\mathbb R$.

Intuitively, we start with open intervals and allow complements and countable unions.

This gives a huge class of measurable sets, including open sets, closed sets, intervals, countable sets, and many more.

## Sigma-algebras versus topologies

A topology is closed under:

- arbitrary unions;
- finite intersections.

A sigma-algebra is closed under:

- complements;
- countable unions;
- countable intersections.

Topologies are designed for continuity and local structure.

Sigma-algebras are designed for measurability and events.

## Place in the build-up

Sigma-algebras are not part of the same algebraic ladder as groups, rings, fields, vector spaces, and algebras over fields.

But they share a common structural idea:

> choose a class of objects and require it to be closed under the operations you need.

In groups and rings, the objects are elements.

In sigma-algebras, the objects are subsets/events.

The operations are logical set operations: not, or, and countable combinations.


{% include chapter-nav.html %}
