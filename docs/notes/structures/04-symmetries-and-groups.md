---
title: "4. Symmetries and Groups"
---

> **Imported note.** Written by me with an AI assistant in [Claptar/math-notes](https://github.com/Claptar/math-notes), imported 2026-09-13. It is *material* — my own exposition — not a record of a worked session. Nothing here is evidence that it has been derived from scratch; a [topic file](../../questions.md) is earned separately.

# 4. Symmetries and Groups

## Central intuition

A **symmetry** of an object is a reversible transformation that may change how the object is presented, but preserves the structure we care about.

Informally:

> A symmetry changes the view, not the essence.

Groups are the natural language of symmetries because symmetries can be composed, have an identity transformation, and can be undone.

## What does it mean to preserve structure?

It depends on the object.

For a geometric figure, preserving structure may mean preserving distances and angles.

For a graph, it means preserving adjacency.

For an algebraic structure, it means preserving operations.

So the word “symmetry” always comes with the question:

> What features of the object count as essential?

## Example: symmetries of a square

A square has eight rigid symmetries:

- rotation by $0^\circ$;
- rotation by $90^\circ$;
- rotation by $180^\circ$;
- rotation by $270^\circ$;
- four reflections.

These transformations form a group because:

1. composing two symmetries gives another symmetry;
2. doing nothing is a symmetry;
3. every symmetry can be undone;
4. composition of transformations is associative.

This group is called the dihedral group of the square.

## Why symmetries must be reversible

If a transformation loses information, it is not a symmetry.

For example:

- rotating a square is reversible;
- reflecting a square is reversible;
- crushing a square into a line is not reversible;
- projecting a 3D object onto a plane usually loses information.

A symmetry is not just an action. It is an invertible action that preserves the relevant structure.

## Formal viewpoint: automorphisms

In abstract mathematics, a symmetry of a structure is often called an **automorphism**.

An automorphism is a structure-preserving bijection from an object to itself.

Examples:

- a symmetry of a set is a bijection;
- a symmetry of a graph is a vertex permutation preserving edges;
- a symmetry of a group is a bijective homomorphism $G\to G$;
- a symmetry of a vector space is an invertible linear map.

The set of all automorphisms of an object forms a group.

## Why symmetries matter

Symmetries reveal what is essential and what is arbitrary.

If an object has many symmetries, then many apparent differences are not structurally meaningful.

For example:

- all directions on a circle are equivalent under rotation;
- the vertices of a regular polygon are interchangeable by symmetry;
- coordinates in a vector space may change while the underlying vector remains the same.

A group of symmetries often acts like a fingerprint of the object.

## Group actions

A group can act on a set $X$. This means each group element is realized as a symmetry or transformation of $X$.

Formally, a group action assigns to each $g\in G$ a function $X\to X$, satisfying

$$
e\cdot x=x,
$$
and

$$
(gh)\cdot x=g\cdot(h\cdot x).
$$
This is how abstract groups become concrete transformations.

## Place in the build-up

The idea of symmetry explains why groups are central.

A group is not just an arbitrary algebraic object. It is exactly what appears when we collect all reversible transformations preserving a structure.

This is why groups occur in geometry, number theory, physics, combinatorics, and the theory of equations.


{% include chapter-nav.html %}
