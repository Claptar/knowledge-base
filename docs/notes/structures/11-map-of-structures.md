---
title: "11. One-Page Map of the Structures"
---

> **Imported note.** Written by me with an AI assistant in [Claptar/math-notes](https://github.com/Claptar/math-notes), imported 2026-09-13. It is *material* — my own exposition — not a record of a worked session. Nothing here is evidence that it has been derived from scratch; a [topic file](../../questions.md) is earned separately.

# 11. One-Page Map of the Structures

## The main algebraic ladder

| Structure | Operations | Main axiom added | Central intuition |
|---|---|---|---|
| Binary operation | one operation | closure | combine two elements |
| Semigroup | one operation | associativity | combine non-empty finite sequences |
| Monoid | one operation | identity | allow the empty composition |
| Group | one operation | inverses | reversible actions |
| Abelian group | one operation | commutativity | order-independent contributions |
| Ring | two operations | distributivity | addition plus compatible multiplication |
| Field | two operations | multiplicative inverses and commutativity | arithmetic of scalars |
| Vector space | addition plus scalar action | compatibility with a field | linear combinations |
| Algebra over a field | vector space plus internal product | bilinearity | linear space with multiplication |
| Sigma-algebra | set operations on subsets | countable closure | language of measurable events |

## The meaning of the major axioms

### Associativity

$$
(ab)c=a(bc)
$$
Means: parentheses do not matter.

It turns a binary operation into finite composition.

### Identity

$$
ea=ae=a
$$
Means: doing nothing is part of the structure.

It allows empty products and zero-step processes.

### Inverse

$$
aa^{-1}=a^{-1}a=e
$$
Means: every action can be undone.

It gives cancellation and equation-solving.

### Commutativity

$$
ab=ba
$$
Means: order does not matter.

It turns sequences of operations into unordered contributions.

### Distributivity

$$
a(b+c)=ab+ac
$$
Means: multiplication respects additive decomposition.

It allows computation by parts, expansion, and factoring.

### Scalar compatibility

$$
\lambda(u+v)=\lambda u+\lambda v
$$
Means: scaling respects vector addition.

It makes linear combinations coherent.

### Bilinearity

$$
(\alpha x+\beta y)z=\alpha xz+\beta yz
$$
Means: internal multiplication in an algebra respects linear combinations in each input.

## Conceptual progression

### From operation to composition

A binary operation combines two elements.

Associativity lets it combine any finite sequence.

### From composition to action

An identity element gives a neutral action.

Inverses make actions reversible.

### From actions to symmetry

Groups model reversible transformations.

Symmetry groups preserve structure.

### From one operation to two

Rings introduce addition and multiplication.

Distributivity makes them one coherent system rather than two unrelated operations.

### From rings to fields

Fields are rings where nonzero multiplication behaves like reversible scalar scaling.

### From fields to vector spaces

A vector space is an additive world acted on by a field of scalars.

The central objects are linear combinations.

### From vector spaces to algebras

An algebra over a field is a vector space where vectors also multiply, and multiplication is compatible with linearity.

### Sigma-algebras

Sigma-algebras are different: they are not vector-space algebras.

They are collections of subsets closed under logical/countable operations, used to define measure and probability.

## Memory slogans

- **Semigroup:** one or more composable steps.
- **Monoid:** zero or more composable steps.
- **Group:** reversible composable steps.
- **Abelian group:** reversible contributions whose order does not matter.
- **Ring:** sums plus products, tied by distributivity.
- **Field:** scalars with addition, multiplication, and division by nonzero elements.
- **Vector space:** objects that admit linear combinations.
- **Algebra over a field:** a vector space with compatible internal multiplication.
- **Sigma-algebra:** a stable language of measurable events.

{% include chapter-nav.html %}
