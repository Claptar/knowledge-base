---
title: "9. Algebras over Fields"
---

> **Imported note.** Written by me with an AI assistant in [Claptar/math-notes](https://github.com/Claptar/math-notes), imported 2026-09-13. It is *material* — my own exposition — not a record of a worked session. Nothing here is evidence that it has been derived from scratch; a [topic file](../../questions.md) is earned separately.

# 9. Algebras over Fields

## Definition

Let $K$ be a field.

An **algebra over $K$** is a vector space $A$ over $K$ equipped with an internal multiplication

$$
A\times A\to A,
\qquad
(x,y)\mapsto xy,
$$
that is bilinear.

Bilinear means:

$$
(\alpha x+\beta y)z=\alpha(xz)+\beta(yz),
$$
and

$$
z(\alpha x+\beta y)=\alpha(zx)+\beta(zy).
$$
Depending on context, one may additionally require the multiplication to be associative, commutative, or to have an identity element.

## Central intuition

An algebra over a field is a vector space whose elements can also multiply each other.

So:

| Structure | What you can do |
|---|---|
| Abelian group | add elements |
| Vector space | add elements and scale them |
| Algebra over $K$ | add, scale, and multiply elements internally |

The essential slogan is:

> An algebra is a linear space with multiplication compatible with linearity.

## Why bilinearity is the key

If multiplication were arbitrary, it would not interact well with vector-space structure.

Bilinearity says multiplication respects linear combinations in each variable.

For example:

$$
(x+y)z=xz+yz,
$$
$$
x(y+z)=xy+xz,
$$
$$
(\lambda x)y=\lambda(xy)=x(\lambda y).
$$
So multiplication can be computed by expanding across sums and pulling out scalars.

This is the vector-space analogue of distributivity in rings.

## Why algebras are natural

Many important vector spaces have a natural product.

For example:

- functions can be multiplied pointwise;
- polynomials can be multiplied;
- matrices can be multiplied;
- linear operators can be composed;
- differential forms can be multiplied by wedge product;
- Lie algebra elements can be combined by a bracket.

In all these cases, the product is compatible with linear combinations.

## Algebra as ring plus vector space

An algebra over $K$ can be seen as an object that is both:

1. a vector space over $K$;
2. a ring-like object under $+$ and multiplication;

with compatibility between scalar multiplication and internal multiplication.

This is why algebras sit at the intersection of ring theory and linear algebra.

## Natural examples

### The field itself

$K$ is an algebra over itself.

### Polynomial algebra

$$
K[x]
$$
is an algebra over $K$.

It is a vector space with basis

$$
1,x,x^2,x^3,\dots
$$
and it also has polynomial multiplication.

### Matrix algebra

$$
M_n(K)
$$
is an algebra over $K$.

It is usually non-commutative:

$$
AB\neq BA
$$
in general.

This is one of the most important examples because it shows that algebras can be linear and non-commutative at the same time.

### Endomorphism algebra

If $V$ is a vector space, then

$$
\operatorname{End}(V)
$$
is the algebra of linear maps $V\to V$, with multiplication given by composition.

### Function algebra

Functions $X\to K$ form an algebra under pointwise operations.

## Associative, commutative, and non-associative algebras

The word “algebra” does not always mean the multiplication is associative.

### Associative algebras

$$
(xy)z=x(yz).
$$
Examples: matrices, polynomials, functions.

### Commutative algebras

$$
xy=yx.
$$
Examples: polynomial rings, function algebras.

### Non-associative algebras

Examples include Lie algebras, where the product is a bracket

$$
[x,y]
$$
satisfying different laws such as antisymmetry and the Jacobi identity.

## What algebras make possible

Algebras let us build expressions involving both linear combinations and products:

$$
x^2+3xy-2y^2,
$$
$$
xy-yx,
$$
$$
x^3+ax+b.
$$
Thus algebras are natural environments for polynomial expressions in abstract objects.

## Place in the build-up

Algebras over fields combine two previous lines:

1. the vector-space line: addition plus scalar multiplication;
2. the ring line: addition plus internal multiplication.

So an algebra is:

> a vector space whose vectors also multiply, with multiplication compatible with linear combinations.


{% include chapter-nav.html %}
