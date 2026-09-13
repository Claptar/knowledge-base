---
title: "Change of Basis"
---

> **Imported note.** Written by me with an AI assistant in [Claptar/math-notes](https://github.com/Claptar/math-notes), imported 2026-09-13. It is *material* — my own exposition — not a record of a worked session. Nothing here is evidence that it has been derived from scratch; a [topic file](../../questions.md) is earned separately.

# Change of Basis: Bases, Coordinates, and Isomorphisms

## 1. The main distinction

Let $V$ be an $n$-dimensional vector space over a field $K$.

A vector $x \in V$ is an actual element of the vector space. A coordinate column is a list of scalars that describes this vector **after a basis has been chosen**.

So the slogan is:

$$\text{vector} = \text{basis} \times \text{coordinate column}.$$

If $e = (e_1, \dots, e_n)$ is a basis of $V$, then every vector $x \in V$ can be written uniquely as

$$x = x_1 e_1 + \cdots + x_n e_n.$$

In matrix notation we write this as $x = eX$, where

$$X = \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}.$$

Here $e$ is not a usual numerical matrix. It is a **row of basis vectors**:

$$e = (e_1, \dots, e_n).$$

So the expression $eX$ means

$$(e_1, \dots, e_n) \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} = x_1 e_1 + \cdots + x_n e_n.$$

![Vector equals basis times coordinate column](figures/diag1_vector_equals_basis_times_coords.svg)

The vector $x$ lives in $V$. The coordinate column $X$ lives in $K^n$. A basis gives us a way to pass between these two worlds.

---

## 2. A basis as an isomorphism

Choosing a basis $e = (e_1, \dots, e_n)$ gives an isomorphism

$$\varphi_e : K^n \to V, \qquad \varphi_e(X) = eX.$$

In other words,

$$\begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} \mapsto x_1 e_1 + \cdots + x_n e_n.$$

This map is an isomorphism because every vector in $V$ has coordinates in the basis $e$, those coordinates are unique, and the map respects addition and scalar multiplication.

So a basis is not merely a list of vectors. It is a coordinate system — equivalently, an isomorphism from the arithmetic space $K^n$ to the abstract vector space $V$. Different bases give different isomorphisms $K^n \to V$. This is the core idea behind change of basis.

---

## 3. Two bases and the change-of-basis matrix

Now let $e = (e_1, \dots, e_n)$ be the old basis and $$e' = (e'_1, \dots, e'_n)$$ be the new basis. Every vector of the new basis can be expressed through the old basis. So for each $j = 1, \dots, n$, we have

$$e'_j = c_{1j} e_1 + c_{2j} e_2 + \cdots + c_{nj} e_n = \sum_{i=1}^n c_{ij} e_i.$$

Notice the indices carefully:

- $j$ tells us which new basis vector we are describing;
- $i$ tells us which old basis vector appears in the expansion;
- $c_{ij}$ is the coefficient of $e_i$ in the expansion of $$e'_j$$.

So the coordinates of $$e'_j$$ in the old basis are

$$[e'_j]_e = \begin{pmatrix} c_{1j} \\ c_{2j} \\ \vdots \\ c_{nj} \end{pmatrix}.$$

That is, the $j$-th column of the change-of-basis matrix is the old-coordinate column of the $j$-th new basis vector.

Define

$$C = \begin{pmatrix} c_{11} & c_{12} & \cdots & c_{1n} \\ c_{21} & c_{22} & \cdots & c_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ c_{n1} & c_{n2} & \cdots & c_{nn} \end{pmatrix}.$$

Then the columns of $C$ are $$[e'_1]_e, [e'_2]_e, \dots, [e'_n]_e$$.

![Definition of C: each new basis vector becomes one column](figures/diag2_definition_of_C.svg)

This matrix $C$ is called the **change-of-basis matrix** from the old basis $e$ to the new basis $e'$.

---

## 4. Coordinates of the same vector in two bases

Let $x \in V$. Suppose its coordinate column in the old basis is $X$ and in the new basis is $X'$. Then

$$x = eX = e' X'.$$

But $e' = eC$, so

$$x = e' X' = (eC) X' = e(C X').$$

On the other hand, $x = eX$. Therefore $eX = e(CX')$. Since coordinates in the old basis $e$ are unique, we must have

$$X = C X'.$$

This is the coordinate transformation formula. Solving for $X'$:

$$X' = C^{-1} X.$$

So

$$\boxed{X = CX' \quad \text{and} \quad X' = C^{-1} X.}$$

The matrix $C$ sends new coordinates to old coordinates. The inverse matrix $C^{-1}$ sends old coordinates to new coordinates.

---

## 5. Why the basis and coordinates transform in opposite directions

We have two formulas: $e' = eC$ and $X' = C^{-1} X$. So the basis changes by $C$ while the coordinate column changes by $C^{-1}$.

![Basis changes by C; coordinates change by C inverse](figures/diag4_opposite_directions.svg)

This is not a contradiction. It is exactly what must happen. The actual vector $x$ stays fixed: $x = eX = e' X'$. But if the basis vectors change, the coordinates must compensate so that the final vector remains the same. The basis and the coordinates move in opposite ways because their product represents one fixed vector.

Symbolically: if $e' = eC$, then to keep the same vector $x$, we need $X' = C^{-1} X$. Indeed,

$$e' X' = (eC)(C^{-1} X) = eX = x.$$

So the vector is unchanged. Only its coordinate description changes.

---

## 6. Sanity check: choosing a new basis vector

This is the simplest check of the formula. Take the coordinate column

$$X' = \begin{pmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}.$$

Then the vector represented by this column in the new basis is

$$x = e' X' = e'_1.$$

Now apply $X = C X'$. We get

$$X = C \begin{pmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix} = \begin{pmatrix} c_{11} \\ c_{21} \\ \vdots \\ c_{n1} \end{pmatrix},$$

which is exactly the first column of $C$. And by definition, the first column of $C$ is the coordinate column of $$e'_1$$ in the old basis. So the formula works perfectly.

More generally, if $X'$ is the $j$-th standard column, then $x = $ $$e'_j$$ and $X = CX'$ is the $j$-th column of $C$ — exactly the expansion $$e'_j = \sum_i c_{ij} e_i$$. So matrix multiplication by $C$ is the linear extension of the rule "the $j$-th new coordinate basis vector $\mapsto$ the $j$-th column of $C$."

---

## 7. What happens when $V = K^n$?

Now suppose the vector space itself is the arithmetic space $V = K^n$. At first, it may seem that vectors and coordinates are the same thing. This is only partly true.

In $K^n$, vectors are already written as columns or rows of scalars. But this representation is actually tied to the standard basis. Let the standard basis be $e = (e_1, \dots, e_n)$ where $e_i$ has a $1$ in position $i$ and $0$ elsewhere. Then for a vector

$$x = \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} \in K^n,$$

we have $x = x_1 e_1 + \cdots + x_n e_n$. So in the standard basis, the vector and its coordinate column look identical:

$$[x]_e = \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}.$$

But if we choose a different basis $e'$, the coordinate column changes. The vector $x$ is still the same element of $K^n$, but its coordinates in the basis $e'$ are generally different.

So even in $K^n$, one should distinguish between the vector $x$ itself, its coordinates in the standard basis, and its coordinates in some other basis. The standard basis makes this distinction invisible; a nonstandard basis makes it visible again.

---

## 8. Example in $K^2$

Let $V = K^2$, and let the old basis be the standard basis. Choose a new basis

$$e' = \left( \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \end{pmatrix} \right).$$

The new basis vectors written in the old (standard) basis are

$$e'_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \qquad e'_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}.$$

Therefore

$$C = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix},$$

and indeed $e' = eC$.

Now take

$$x = \begin{pmatrix} 3 \\ 1 \end{pmatrix}.$$

Since $e$ is the standard basis, the old coordinate column is $X = (3, 1)^T$. To find the new coordinate column $X'$, we solve $X = CX'$:

$$\begin{pmatrix} 3 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} x'_1 \\ x'_2 \end{pmatrix}.$$

This gives $$x'_1 + x'_2 = 3$$ and $$x'_1 - x'_2 = 1$$, so $$x'_1 = 2$$, $$x'_2 = 1$$. Therefore $X' = (2, 1)^T$. Verification:

$$2 \begin{pmatrix} 1 \\ 1 \end{pmatrix} + 1 \begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 3 \\ 1 \end{pmatrix} = x. \quad \checkmark$$

The same vector has two coordinate descriptions:

$$[x]_e = \begin{pmatrix} 3 \\ 1 \end{pmatrix}, \qquad [x]_{e'} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}.$$

![Same vector v in two bases of R^2](figures/diag5_R2_example.svg)

The vector did not change. Only the coordinate system changed.

---

## 9. Change of basis as a change of isomorphism

Each basis gives an isomorphism from coordinate space to the vector space. For the old basis $e$ we have $\varphi_e : K^n \to V$ with $\varphi_e(X) = eX$. For the new basis $e'$ we have $\varphi_{e'} : K^n \to V$ with $\varphi_{e'}(X') = e' X'$.

Since $e' = eC$,

$$\varphi_{e'}(X') = e' X' = (eC) X' = e(CX') = \varphi_e(CX').$$

Therefore

$$\boxed{\varphi_{e'} = \varphi_e \circ C.}$$

![Two isomorphisms linked by C](figures/diag6_isomorphism_triangle.svg)

This is the conceptual meaning of the change-of-basis matrix. The matrix $C$ does not change the vector inside $V$. It translates new coordinate columns into old coordinate columns. Then the old basis isomorphism $\varphi_e$ turns those old coordinate columns into actual vectors.

So the picture is:

$$K^n \xrightarrow{\;C\;} K^n \xrightarrow{\;\varphi_e\;} V,$$

and this composition equals $\varphi_{e'}$.

---

## 10. Final summary

Let $e$ be the old basis and $e'$ be the new basis. The change-of-basis matrix $C = (c_{ij})$ is defined by

$$e'_j = \sum_{i=1}^n c_{ij} e_i, \qquad \text{equivalently} \qquad e' = eC.$$

If $x = eX = e' X'$, then $X = CX'$, and so $X' = C^{-1} X$. The matrix $C$ converts new coordinates into old coordinates; the inverse matrix $C^{-1}$ converts old coordinates into new coordinates.

The basis changes by $C$:

$$e' = eC.$$

The coordinate column changes by $C^{-1}$:

$$X' = C^{-1} X.$$

This happens because the actual vector must remain fixed: $x = eX = e' X'$.

A basis is an isomorphism $K^n \to V$. Changing basis means changing this isomorphism. The vector does not move; only its coordinate name changes.

{% include chapter-nav.html %}
