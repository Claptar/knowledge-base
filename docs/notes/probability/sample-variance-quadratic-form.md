---
title: "Sample Variance as a Quadratic Form"
---

> **Imported note.** Written by me with an AI assistant in [Claptar/math-notes](https://github.com/Claptar/math-notes), imported 2026-09-13. It is *material* — my own exposition — not a record of a worked session. Nothing here is evidence that it has been derived from scratch; a [topic file](../../questions.md) is earned separately.

> **Alternative treatment.** [`sample-variance-quadratic-form-geometry`](sample-variance-quadratic-form-geometry.md) covers the same material by a different route. Both are kept deliberately — comparing two expositions of one idea is worth more than picking a winner.

# Sample Variance as a Quadratic Form

## 1. The Main Point

There are two different spaces involved:

1. The space of scalar random variables, such as

   $$
   X_1, \dots, X_n \in L^2(\Omega).
   $$

2. The deterministic sample-value space

   $$
   \mathbb R^n.
   $$

The sample variance quadratic form is first defined on the deterministic space

$$
\mathbb R^n.
$$

Then we plug in the random vector

$$
X=(X_1,\dots,X_n):\Omega\to\mathbb R^n.
$$

So the structure is:

$$
\Omega \xrightarrow{X} \mathbb R^n \xrightarrow{q} \mathbb R.
$$

Therefore the sample variance is the random variable

$$
S^2 = q(X).
$$

The important correction is:

> The matrix of the sample-variance quadratic form is not written in the basis $X_1,\dots,X_n$.  
> It is written in the standard basis $e_1,\dots,e_n$ of $\mathbb R^n$.

The variables $X_1,\dots,X_n$ are not basis vectors. They are the random coordinates of the vector-valued random variable $X$.

---

## 2. The Deterministic Quadratic Form

Start with a deterministic sample vector

$$
x=(x_1,\dots,x_n)\in\mathbb R^n.
$$

Its sample mean is

$$
\bar x = \frac1n\sum_{i=1}^n x_i.
$$

The vector of deviations from the mean is

$$
x-\bar x\mathbf 1,
$$

where

$$
\mathbf 1=(1,\dots,1)^T.
$$

This operation is linear. It is given by the matrix

$$
P = I - \frac1n \mathbf 1\mathbf 1^T.
$$

So

$$
Px = x-\bar x\mathbf 1.
$$

The matrix entries are

$$
P_{ij}
=
\begin{cases}
1-\frac1n, & i=j,\\
-\frac1n, & i\neq j.
\end{cases}
$$

The unnormalised sum of squared deviations is

$$
q(x)=\sum_{i=1}^n (x_i-\bar x)^2.
$$

In matrix form,

$$
q(x)=x^T P x.
$$

The unbiased sample variance is

$$
S^2(x)=\frac1{n-1}x^T P x.
$$

If instead one uses the convention with denominator $n$, then

$$
S_n^2(x)=\frac1n x^T P x.
$$

So the matrix $P$ gives the raw squared-deviation quadratic form, and the sample variance just rescales it.

---

## 3. The Bilinear Form Associated With Sample Variance

The quadratic form

$$
q(x)=x^TPx
$$

has an associated symmetric bilinear form

$$
p(x,y)=x^T P y.
$$

This bilinear form is defined on

$$
\mathbb R^n\times\mathbb R^n.
$$

In the standard basis

$$
e_1,\dots,e_n,
$$

its matrix is

$$
P.
$$

That is,

$$
p(e_i,e_j)=P_{ij}.
$$

This is the correct analogue of saying that a bilinear form has a matrix in a particular basis.

But we should not write

$$
p(X_i,X_j)=P_{ij},
$$

because $X_i$ and $X_j$ are scalar random variables, not basis vectors of $\mathbb R^n$.

---

## 4. Geometry of the Matrix $P$

The space $\mathbb R^n$ decomposes as

$$
\mathbb R^n
=
\operatorname{span}\{\mathbf 1\}
\oplus
\mathbf 1^\perp.
$$

Here

$$
\operatorname{span}\{\mathbf 1\}
$$

is the one-dimensional space of constant vectors

$$
(c,c,\dots,c),
$$

and

$$
\mathbf 1^\perp
=
\left\{x\in\mathbb R^n:\sum_{i=1}^n x_i=0\right\}
$$

is the $(n-1)$-dimensional space of mean-zero fluctuation vectors.

The matrix $P$ is the orthogonal projection onto $\mathbf 1^\perp$.

Indeed,

$$
P\mathbf 1=0,
$$

and if

$$
x\in \mathbf 1^\perp,
$$

then

$$
Px=x.
$$

So $P$ kills the mean direction and preserves all fluctuation directions.

The sample variance measures the squared length of the fluctuation component of the sample vector.

---

## 5. Diagonalising $P$

Choose an orthonormal basis of $\mathbb R^n$ as follows.

First take

$$
u_1=\frac1{\sqrt n}(1,\dots,1).
$$

Then choose

$$
u_2,\dots,u_n
$$

to be any orthonormal basis of the mean-zero subspace

$$
\mathbf 1^\perp.
$$

Then

$$
Pu_1=0,
$$

and

$$
Pu_k=u_k,\qquad k=2,\dots,n.
$$

Therefore, in the basis

$$
u_1,u_2,\dots,u_n,
$$

the matrix of $P$ is

$$
\operatorname{diag}(0,1,\dots,1).
$$

If

$$
x=a_1u_1+a_2u_2+\cdots+a_nu_n,
$$

then

$$
x^TPx=a_2^2+\cdots+a_n^2.
$$

The first coordinate $a_1$ is the mean direction. It does not contribute to sample variance.

The other coordinates $a_2,\dots,a_n$ are the fluctuation directions. These are exactly what sample variance measures.

---

## 6. Plugging In A Random Vector

Now let

$$
X=(X_1,\dots,X_n):\Omega\to\mathbb R^n.
$$

For each outcome $\omega$, we get a deterministic sample vector

$$
X(\omega)=(X_1(\omega),\dots,X_n(\omega))\in\mathbb R^n.
$$

The sample variance is

$$
S^2(\omega)
=
\frac1{n-1}X(\omega)^TPX(\omega).
$$

Equivalently, as an identity of random variables,

$$
S^2=\frac1{n-1}X^TPX.
$$

The diagonalisation of $P$ remains valid after plugging in $X$, because it is a deterministic pointwise identity. For every $\omega$,

$$
X(\omega)^TPX(\omega)
=
Y_2(\omega)^2+\cdots+Y_n(\omega)^2,
$$

where $Y_1,\dots,Y_n$ are the coordinates of $X$ in the diagonalising basis.

---

## 7. Rotating The Coordinates Of The Random Vector

Let $U$ be the orthogonal matrix whose columns are

$$
u_1,u_2,\dots,u_n.
$$

Define

$$
Y=U^T X.
$$

Then

$$
Y_k=u_k^T X.
$$

Each $Y_k$ is a scalar random variable.

In the original standard basis, we write

$$
X(\omega)=X_1(\omega)e_1+\cdots+X_n(\omega)e_n.
$$

In the new diagonalising basis, we write

$$
X(\omega)=Y_1(\omega)u_1+\cdots+Y_n(\omega)u_n.
$$

Thus the $X_i$'s are the old random coordinates of the vector-valued random variable $X$, and the $Y_i$'s are the new random coordinates.

The basis vectors are not $X_1,\dots,X_n$. The basis vectors are either

$$
e_1,\dots,e_n,
$$

or

$$
u_1,\dots,u_n.
$$

This is why diagonalising in $\mathbb R^n$ produces a diagonal expression in terms of the new random variables $Y_i$.

---

## 8. Can We Define This Directly On Random Variables?

There are two meanings of this question.

### 8.1 On scalar random variables

Suppose we try to define a quadratic form on

$$
\operatorname{span}\{X_1,\dots,X_n\}\subseteq L^2(\Omega).
$$

An element of this span looks like

$$
Z=a_1X_1+\cdots+a_nX_n.
$$

This is one scalar random variable.

But sample variance is not naturally a function of one scalar random variable. It is a function of the whole vector

$$
(X_1,\dots,X_n).
$$

It needs the sample-coordinate structure. It needs to know which coordinate is the first observation, which is the second observation, and so on.

One could artificially define

$$
\widetilde p(Z,W)=a^TPb
$$

when

$$
Z=a^TX,\qquad W=b^TX.
$$

But this is not really the sample variance. It is just the coefficient-space bilinear form transported through the map

$$
a\mapsto a^TX.
$$

It may also fail to be well-defined if the random variables $X_1,\dots,X_n$ are linearly dependent.

For example, if

$$
X_1=X_2,
$$

then

$$
X_1-X_2=0.
$$

The scalar random variable is zero, but the coefficient vector

$$
(1,-1)
$$

is not zero. A coefficient-based quadratic form could assign a nonzero value to a representation of the zero random variable. Therefore it would not be a well-defined quadratic form on the scalar random-variable space itself.

So sample variance is not naturally a quadratic form on

$$
\operatorname{span}\{X_1,\dots,X_n\}\subseteq L^2(\Omega).
$$

### 8.2 On vector-valued random variables

There is, however, a natural way to define it on vector-valued random variables.

Let

$$
Z:\Omega\to\mathbb R^n
$$

be a vector-valued random variable.

Define

$$
Q(Z)(\omega)=Z(\omega)^TPZ(\omega).
$$

Then

$$
Q(Z)=Z^TPZ.
$$

This is a quadratic map

$$
Q:L^2(\Omega;\mathbb R^n)\to L^1(\Omega).
$$

It does not return a number. It returns a scalar random variable.

The associated bilinear map is

$$
B(Z,W)(\omega)=Z(\omega)^TPW(\omega).
$$

So

$$
B:L^2(\Omega;\mathbb R^n)\times L^2(\Omega;\mathbb R^n)\to L^1(\Omega).
$$

This is why the situation feels different from covariance.

---

## 9. Comparison With Covariance

Covariance is different.

For scalar random variables

$$
X_1,\dots,X_n\in L^2(\Omega),
$$

we define

$$
\operatorname{Cov}(X_i,X_j)\in\mathbb R.
$$

So covariance is a scalar-valued bilinear form:

$$
\operatorname{Cov}:L^2(\Omega)\times L^2(\Omega)\to\mathbb R.
$$

If

$$
Z=a^TX,
\qquad
W=b^TX,
$$

then

$$
\operatorname{Cov}(Z,W)=a^T\Sigma b,
$$

where

$$
\Sigma_{ij}=\operatorname{Cov}(X_i,X_j).
$$

So covariance acts on scalar random variables and returns a scalar.

Sample variance instead is

$$
X^TPX.
$$

This applies a deterministic quadratic form to the whole random vector $X$. It returns a random variable.

Therefore:

$$
\boxed{\text{Covariance is a bilinear form on scalar random variables with scalar output.}}
$$

$$
\boxed{\text{Sample variance is a quadratic form on sample vectors, evaluated at a random vector.}}
$$

---

## 10. Example: $n=2$

Let

$$
X=(X_1,X_2).
$$

Then

$$
P=
\begin{pmatrix}
1/2 & -1/2\\
-1/2 & 1/2
\end{pmatrix}.
$$

The eigenvectors are

$$
u_1=\frac1{\sqrt2}(1,1),
$$

and

$$
u_2=\frac1{\sqrt2}(1,-1).
$$

Define

$$
Y_1=u_1^TX=\frac{X_1+X_2}{\sqrt2},
$$

and

$$
Y_2=u_2^TX=\frac{X_1-X_2}{\sqrt2}.
$$

Then

$$
X^TPX=Y_2^2.
$$

Indeed,

$$
Y_2^2
=
\left(\frac{X_1-X_2}{\sqrt2}\right)^2
=
\frac12(X_1-X_2)^2.
$$

Also,

$$
\sum_{i=1}^2(X_i-\bar X)^2
=
\frac12(X_1-X_2)^2.
$$

So the direction

$$
(1,1)
$$

is the mean direction, and the direction

$$
(1,-1)
$$

is the variation direction.

Sample variance only sees the variation direction.

---

## 11. Gaussian Case

Suppose

$$
X_1,\dots,X_n
$$

are independent Gaussian random variables with

$$
X_i\sim N(\mu,\sigma^2).
$$

Then

$$
X\sim N(\mu\mathbf 1,\sigma^2 I).
$$

Let

$$
Y=U^TX,
$$

where $U$ diagonalises $P$.

Then

$$
X^TPX=Y_2^2+\cdots+Y_n^2.
$$

The first coordinate

$$
Y_1=\frac1{\sqrt n}(X_1+\cdots+X_n)
$$

is the mean-direction coordinate.

The remaining coordinates

$$
Y_2,\dots,Y_n
$$

are fluctuation coordinates.

If the $X_i$'s are i.i.d. Gaussian, then after the orthogonal rotation the $Y_i$'s are still jointly Gaussian, and their covariance matrix is still diagonal.

Therefore the fluctuation coordinates are independent Gaussian random variables, and

$$
\frac{(n-1)S^2}{\sigma^2}
=
\frac{Y_2^2+\cdots+Y_n^2}{\sigma^2}
\sim \chi^2_{n-1}.
$$

The number $n-1$ appears because the mean-zero fluctuation subspace

$$
\mathbf 1^\perp
$$

has dimension $n-1$.

---

## 12. Final Summary

The clean picture is:

1. The deterministic sample-value space is

   $$
   \mathbb R^n.
   $$

2. The sample-variance matrix is

   $$
   P=I-\frac1n\mathbf 1\mathbf 1^T.
   $$

3. This matrix is written in the standard basis

   $$
   e_1,\dots,e_n
   $$

   of $\mathbb R^n$.

4. The scalar random variables $X_1,\dots,X_n$ are coordinates of the vector-valued random variable

   $$
   X=(X_1,\dots,X_n).
   $$

5. Diagonalising $P$ means choosing a better basis of $\mathbb R^n$:

   $$
   \mathbb R^n
   =
   \operatorname{span}\{\mathbf 1\}
   \oplus
   \mathbf 1^\perp.
   $$

6. This induces new scalar random variables

   $$
   Y_k=u_k^TX.
   $$

7. In those coordinates,

   $$
   X^TPX=Y_2^2+\cdots+Y_n^2.
   $$

8. Sample variance is therefore the squared length of the projection of the random sample vector onto the mean-zero subspace:

   $$
   S^2=\frac1{n-1}\|PX\|^2.
   $$

The important distinction is:

$$
\boxed{\text{Covariance is geometry on scalar random variables.}}
$$

while

$$
\boxed{\text{Sample variance is geometry on sample-value vectors, evaluated at a random vector.}}
$$

---

## 13. See Also

- [Gaussian Vectors, Coordinate Random Variables, and Covariance Geometry](gaussian-vectors-covariance-geometry-alt.md) — develops the $L^2(\Omega)$ viewpoint where the covariance matrix is the Gram matrix of the centered coordinate random variables
- [Direct Sums, Complements, and Decompositions](../linear-algebra/direct-sums-and-complements.md) — the orthogonal decomposition $\mathbb{R}^n = \operatorname{span}\{\mathbf{1}\} \oplus \mathbf{1}^\perp$ used in Section 4
