---
title: "8. Vector Spaces"
---

> **Imported note.** Written by me with an AI assistant in [Claptar/math-notes](https://github.com/Claptar/math-notes), imported 2026-09-13. It is *material* — my own exposition — not a record of a worked session. Nothing here is evidence that it has been derived from scratch; a [topic file](../../questions.md) is earned separately.

# 8. Vector Spaces

## Definition

Let $K$ be a field.

A **vector space** over $K$ is a set $V$ with:

1. vector addition

$$
+:V\times V\to V,
$$
making $(V,+)$ an abelian group;

2. scalar multiplication

$$
K\times V\to V,
\qquad
(\lambda,v)\mapsto \lambda v,
$$
satisfying compatibility axioms.

The most important scalar axioms are:

$$
\lambda(u+v)=\lambda u+\lambda v,
$$
$$
(\lambda+\mu)v=\lambda v+\mu v,
$$
$$
(\lambda\mu)v=\lambda(\mu v),
$$
$$
1v=v.
$$
## Central intuition

A vector space is a world of objects that can be:

- added together;
- scaled by elements of a field;
- combined into linear combinations.

The most important expression in a vector space is

$$
\lambda_1v_1+\cdots+\lambda_nv_n.
$$
So:

> A vector space is a space of linear combinations.

## Why two worlds appear

In a vector space, there are two kinds of objects:

1. **vectors** $v\in V$;
2. **scalars** $\lambda\in K$.

Vectors are the things being combined.

Scalars are coefficients controlling the combination.

A useful slogan:

> Vectors are the objects; scalars are the controls.

## Why vector addition is abelian

Vector addition represents combining independent contributions.

Examples:

- adding displacements;
- adding forces;
- adding functions;
- adding signals;
- adding columns of numbers.

The order of contributions usually does not matter:

$$
u+v=v+u.
$$
That is why $(V,+)$ is an abelian group.

## What scalar multiplication adds

An abelian group lets us add and subtract.

A vector space lets us also say:

- take half of a vector;
- multiply a vector by $3$;
- take $2u-5v$;
- express a vector in coordinates;
- solve linear equations with coefficients.

The field provides a rich arithmetic of coefficients.

## Why the distributive axioms appear

There are two additions:

1. vector addition $u+v$;
2. scalar addition $\lambda+\mu$.

Scalar multiplication must respect both.

### Scaling a vector sum

$$
\lambda(u+v)=\lambda u+\lambda v.
$$
Meaning:

> Scaling a sum of vectors equals the sum of the scaled parts.

### Splitting a scalar

$$
(\lambda+\mu)v=\lambda v+\mu v.
$$
Meaning:

> Applying a sum of coefficients to a vector equals adding the separately scaled copies.

These two laws are the vector-space version of distributivity.

## Why the associativity of scalar multiplication matters

$$
(\lambda\mu)v=\lambda(\mu v).
$$
Meaning:

> Scaling first by $\mu$, then by $\lambda$, is the same as scaling once by $\lambda\mu$.

This ensures scalar multiplication really behaves like scaling.

## Why $1v=v$

The scalar $1$ is the neutral scale.

Multiplying by $1$ should not change a vector.

## Natural examples

### Coordinate spaces

$$
K^n
$$
with componentwise addition and scalar multiplication is the standard example.

### Functions

Functions $X\to K$ form a vector space under pointwise operations.

### Polynomials

The set $K[x]$ of polynomials is a vector space over $K$.

A polynomial is a linear combination of monomials:

$$
a_0+a_1x+a_2x^2+\cdots+a_nx^n.
$$
### Matrices

All $m\times n$ matrices over $K$ form a vector space.

### Solutions to homogeneous linear equations

The solution set of a homogeneous linear system is a vector space.

## What vector spaces make possible

Vector spaces are the natural setting for:

- linear combinations;
- span;
- linear independence;
- basis;
- dimension;
- coordinates;
- linear maps;
- matrices;
- eigenvalues and eigenvectors;
- systems of linear equations.

## Vector spaces versus modules

If scalars come from a general ring rather than a field, the analogous structure is called a **module**.

Every vector space is a module over a field, but modules over general rings can behave much less cleanly.

The field assumption gives division by nonzero scalars, which makes basis and dimension theory much nicer.

## Place in the build-up

A vector space combines:

- an abelian group of vectors;
- a field of scalars;
- a compatible action of scalars on vectors.

It is not a ring, because vectors do not necessarily multiply with each other.

The next step is to add such an internal multiplication. That leads to algebras over fields.


{% include chapter-nav.html %}
