---
title: "Gaussian Vectors and Covariance Geometry — the source of the confusion"
---

> **Imported note.** Written by me with an AI assistant in [Claptar/math-notes](https://github.com/Claptar/math-notes), imported 2026-09-13. It is *material* — my own exposition — not a record of a worked session. Nothing here is evidence that it has been derived from scratch; a [topic file](../../questions.md) is earned separately.

> **Alternative treatment.** [`gaussian-vectors-covariance-geometry-alt`](gaussian-vectors-covariance-geometry-alt.md) covers the same material by a different route. Both are kept deliberately — comparing two expositions of one idea is worth more than picking a winner.

# Gaussian Vectors, Coordinate Random Variables, and Covariance Geometry

## 1. The Source of the Confusion

In statistics and machine learning we often write

$$
X =
\begin{pmatrix}
X_1 \\
\vdots \\
X_n
\end{pmatrix}
$$

and call $X$ a **Gaussian vector** or **random vector**.

At first this can feel strange. The entries $X_1,\dots,X_n$ are themselves random variables, and random variables can be added and scaled. So it is tempting to think of

$$
X_1,\dots,X_n
$$

as a family of vectors in some larger vector space, namely a space of random variables.

That intuition is correct, but it is only one of two relevant viewpoints.

The main point is:

> A Gaussian vector is a single random object taking values in a finite-dimensional vector space, but its coordinate functions are scalar random variables that themselves live in a vector space such as $L^2(\Omega)$.

Much confusion comes from using the same notation for both structures.

## 2. Random Vector as a Map

Let $(\Omega,\mathcal F,\mathbb P)$ be a probability space. A random vector is a measurable map

$$
X:\Omega \to V,
$$

where $V$ is a finite-dimensional real vector space.

If we choose a basis of $V$, we may identify $V$ with $\mathbb R^n$, and then write

$$
X(\omega)
=
\begin{pmatrix}
X_1(\omega) \\
\vdots \\
X_n(\omega)
\end{pmatrix}.
$$

So for each outcome $\omega\in\Omega$,

$$
X(\omega)\in V.
$$

This is the first meaning of "vector": the random object $X$ takes values in a vector space.

When people write

$$
X\in \mathbb R^n,
$$

they often mean informally that $X$ is an $\mathbb R^n$-valued random variable. More precisely,

$$
X:\Omega\to \mathbb R^n.
$$

## 3. Coordinate Random Variables

After choosing a basis $e_1,\dots,e_n$ of $V$, we get coordinate functions

$$
X_1,\dots,X_n.
$$

Each $X_i$ is a scalar random variable:

$$
X_i:\Omega\to\mathbb R.
$$

If these random variables have finite second moment, then

$$
X_i\in L^2(\Omega).
$$

Therefore the collection $X_1,\dots,X_n$ spans a finite-dimensional subspace of $L^2(\Omega)$:

$$
\operatorname{span}\{X_1,\dots,X_n\}\subseteq L^2(\Omega).
$$

This is the second vector-space viewpoint.

So we have two spaces:

$$
X:\Omega\to V
$$

and

$$
X_1,\dots,X_n\in L^2(\Omega).
$$

The first says that $X$ is a vector-valued random variable. The second says that the coordinates of $X$ are scalar random variables, which themselves form vectors in a function space.

## 4. The Two Copies of $\mathbb R^n$

There is another subtlety. When we write

$$
a^TX = a_1X_1+\cdots+a_nX_n,
$$

the vector $a$ is not another possible value of $X$. It is a list of coefficients.

More invariantly, if $X:\Omega\to V$, then $a$ represents a linear functional

$$
a\in V^*.
$$

The expression $a^TX$ really means

$$
a(X),
$$

which is a scalar random variable.

Thus there are two different roles:

- $X(\omega)\in V$: possible values of the random vector.
- $a\in V^*$: deterministic directions or linear functionals used to probe $X$.

After choosing an inner product and coordinates, we often identify

$$
V\cong \mathbb R^n
$$

and

$$
V^*\cong \mathbb R^n.
$$

This is convenient, but conceptually $X(\omega)$ and $a$ live in different spaces.

## 5. Covariance as a Bilinear Form

Assume first that $X$ is centered:

$$
\mathbb E[X]=0.
$$

In coordinates, the covariance matrix is

$$
\Sigma_{ij}
=
\mathbb E[X_iX_j].
$$

Equivalently,

$$
\Sigma
=
\mathbb E[XX^T].
$$

For two coefficient vectors $a,b\in V^*$, the scalar random variables $a(X)$ and $b(X)$ have covariance

$$
\operatorname{Cov}(a(X),b(X))
=
\mathbb E[a(X)b(X)].
$$

In coordinates,

$$
\operatorname{Cov}(a^TX,b^TX)
=
a^T\Sigma b.
$$

So covariance is naturally a bilinear form on the dual space:

$$
\operatorname{Cov}_X:V^*\times V^*\to\mathbb R.
$$

It takes two deterministic probes $a,b$ and returns the covariance between the scalar random variables they extract from $X$.

## 6. Covariance as a Gram Matrix

Now switch to the $L^2(\Omega)$ viewpoint.

The space $L^2(\Omega)$ has inner product

$$
\langle U,V\rangle_{L^2}
=
\mathbb E[UV].
$$

If $X$ is centered, then

$$
\Sigma_{ij}
=
\mathbb E[X_iX_j]
=
\langle X_i,X_j\rangle_{L^2}.
$$

Therefore the covariance matrix is the Gram matrix of the coordinate random variables $X_1,\dots,X_n$.

This is a key insight:

> The covariance matrix is both a matrix describing the geometry of the distribution of $X$ in $V$, and the Gram matrix of the coordinate random variables inside $L^2(\Omega)$.

These are not competing interpretations. They are two views of the same structure.

## 7. Linear Transformations of Gaussian Vectors

If

$$
Y=SX,
$$

where $S$ is an $m\times n$ matrix, then

$$
Y:\Omega\to\mathbb R^m
$$

is another random vector.

Pointwise,

$$
Y(\omega)=S X(\omega).
$$

Coordinate-wise,

$$
Y_i=\sum_{j=1}^n S_{ij}X_j.
$$

Thus a linear transformation of the random vector corresponds to forming new scalar random variables as linear combinations of the old ones.

The covariance transforms as

$$
\operatorname{Cov}(Y)
=
S\Sigma S^T.
$$

This is the same transformation rule as for Gram matrices.

## 8. Dependent Spanning Families and Quotients

Suppose $v_1,\dots,v_n$ span a finite-dimensional vector space $W$, but are linearly dependent.

Then the map

$$
\Phi:\mathbb R^n\to W
$$

defined by

$$
\Phi(a_1,\dots,a_n)
=
a_1v_1+\cdots+a_nv_n
$$

is surjective, but not injective.

Its kernel is

$$
\ker\Phi
=
\{a\in\mathbb R^n:a_1v_1+\cdots+a_nv_n=0\}.
$$

So $W$ is not isomorphic to $\mathbb R^n$. Instead,

$$
W\cong \mathbb R^n/\ker\Phi.
$$

This explains why a dependent spanning set does not give genuine coordinates. It gives redundant coordinates.

The same thing happens for random variables.

Define

$$
\Phi:\mathbb R^n\to L^2(\Omega)
$$

by

$$
\Phi(a)=a^TX.
$$

Then

$$
\operatorname{im}\Phi
=
\operatorname{span}\{X_1,\dots,X_n\}.
$$

If the $X_i$ are linearly dependent as random variables, then $\Phi$ has nontrivial kernel. The true generated space is

$$
\operatorname{span}\{X_1,\dots,X_n\}
\cong
\mathbb R^n/\ker\Phi.
$$

## 9. Degenerate Gaussian Vectors

For centered $X$,

$$
\|a^TX\|_{L^2}^2
=
\mathbb E[(a^TX)^2]
=
a^T\Sigma a.
$$

Therefore,

$$
a^T\Sigma a=0
$$

means

$$
a^TX=0
$$

in $L^2(\Omega)$, and hence almost surely.

So directions $a$ for which

$$
a^T\Sigma a=0
$$

are directions with zero random variation.

If $\Sigma$ is singular, then some nonzero deterministic direction $a$ satisfies

$$
a^TX=0
$$

almost surely, assuming centered $X$. More generally, for non-centered $X$,

$$
a^T(X-\mu)=0
$$

almost surely.

Thus a Gaussian vector with singular covariance does not really fill all of $\mathbb R^n$. It lives on a lower-dimensional affine subspace.

This is the probabilistic version of redundant coordinates.

## 10. Diagonalizing Covariance

Since $\Sigma$ is symmetric positive semidefinite, it can be diagonalized:

$$
\Sigma=Q\Lambda Q^T,
$$

where $Q$ is orthogonal and $\Lambda$ is diagonal with nonnegative entries.

Define

$$
Y=Q^T(X-\mu).
$$

Then

$$
\operatorname{Cov}(Y)=\Lambda.
$$

So the components of $Y$ are uncorrelated.

If $X$ is Gaussian, then uncorrelated components are independent. This is a special property of Gaussian vectors.

For non-Gaussian random vectors, diagonal covariance only gives uncorrelated components, not necessarily independent components.

## 11. PCA as Covariance Geometry

For a centered random vector $X$, the variance along direction $a$ is

$$
\operatorname{Var}(a^TX)=a^T\Sigma a.
$$

PCA asks:

> Which unit direction $a$ makes $a^TX$ have maximal variance?

That is,

$$
\max_{\|a\|=1} a^T\Sigma a.
$$

The solution is the top eigenvector of $\Sigma$.

The next principal components are found by maximizing variance subject to being orthogonal to earlier directions.

Thus PCA is not merely "diagonalizing a covariance matrix." It is finding directions in coefficient space whose corresponding scalar random variables have maximal variance.

In the $L^2$ picture, PCA finds especially important linear combinations of the coordinate random variables.

## 12. Whitening

Whitening transforms a random vector so that its covariance becomes the identity.

If

$$
\Sigma=Q\Lambda Q^T
$$

with positive eigenvalues, then one whitening transform is

$$
Y=\Lambda^{-1/2}Q^T(X-\mu).
$$

Then

$$
\operatorname{Cov}(Y)=I.
$$

Geometrically, this first rotates into the principal-component basis, then rescales each direction to have variance $1$.

If $\Sigma$ is singular, full whitening in $\mathbb R^n$ is impossible because some directions have zero variance. One must either discard the zero-variance directions or use a pseudoinverse.

This is another place where the quotient-space idea matters.

## 13. Gaussian Conditioning and Projection

Gaussian conditioning has a beautiful geometric interpretation.

Suppose

$$
\begin{pmatrix}
X \\
Y
\end{pmatrix}
$$

is jointly Gaussian.

Then the conditional expectation

$$
\mathbb E[X\mid Y]
$$

is a linear function of $Y$.

This is not true for arbitrary distributions. It is special to the Gaussian case.

In $L^2(\Omega)$ language, conditional expectation is an orthogonal projection. For Gaussian variables, projecting onto the information generated by $Y$ reduces to projecting onto the linear span of the components of $Y$.

This is why linear regression, least squares, and Gaussian conditioning fit together so tightly.

## 14. Gaussian Processes

A Gaussian process is an infinite-dimensional analogue of a Gaussian vector.

Instead of finitely many variables

$$
X_1,\dots,X_n,
$$

we have a family

$$
\{X_t:t\in T\}.
$$

The defining property is that every finite subcollection

$$
(X_{t_1},\dots,X_{t_n})
$$

is a Gaussian vector.

The covariance matrix becomes a covariance kernel:

$$
K(s,t)=\operatorname{Cov}(X_s,X_t).
$$

This kernel is a Gram matrix generalized to infinitely many indexed random variables:

$$
K(s,t)=\langle X_s,X_t\rangle_{L^2}.
$$

So the ideas from finite Gaussian vectors extend naturally to Gaussian processes, kernel methods, RKHS theory, and stochastic processes.

## 15. Main Applications

### PCA and Dimensionality Reduction

Covariance eigenvalues reveal how much random variation exists in each principal direction.

Small eigenvalues correspond to nearly redundant directions. Zero eigenvalues correspond to exactly redundant directions.

### Whitening and Preprocessing

Whitening removes second-order correlations and rescales directions to unit variance. It is common in signal processing, statistics, and machine learning.

### Factor Analysis and Probabilistic PCA

A high-dimensional Gaussian vector may be represented using fewer latent Gaussian variables:

$$
X = AZ+\varepsilon.
$$

Here $Z$ is lower-dimensional. This is explicitly about representing the observed random-variable span through a smaller latent Gaussian space.

### Kalman Filtering

Kalman filtering repeatedly updates Gaussian estimates using means and covariance matrices. The covariance matrix describes uncertainty geometry, and the update step is closely related to orthogonal projection in $L^2$.

### Gaussian Processes

Gaussian processes use covariance kernels to define joint distributions over infinite families of random variables. The finite-dimensional covariance matrix becomes an infinite-dimensional Gram structure.

## 16. Common Pitfalls

### Pitfall 1: Treating $X\in\mathbb R^n$ Literally

More precisely,

$$
X:\Omega\to\mathbb R^n.
$$

The random vector is a function whose values are vectors.

### Pitfall 2: Confusing Value Space and Coefficient Space

The value $X(\omega)$ belongs to $V$.

The direction $a$ in $a^TX$ belongs to $V^*$.

Coordinates often identify both with $\mathbb R^n$, but conceptually they are different.

### Pitfall 3: Thinking Normal Marginals Imply Joint Gaussianity

It is possible for each $X_i$ to be normally distributed while the vector

$$
(X_1,\dots,X_n)
$$

is not jointly Gaussian.

Joint Gaussianity is a stronger condition: every linear combination

$$
a_1X_1+\cdots+a_nX_n
$$

must be Gaussian.

### Pitfall 4: Forgetting Degenerate Cases

If $\Sigma$ is singular, then $X$ has zero variation in some directions. The Gaussian distribution lives on a lower-dimensional affine subspace.

In that case, the natural object is not all of $\mathbb R^n$, but a quotient or lower-dimensional support space.

## 17. What To Retain

A Gaussian vector has two linked interpretations.

First,

$$
X:\Omega\to V
$$

is a single random object taking values in a finite-dimensional vector space.

Second, after choosing coordinates,

$$
X_1,\dots,X_n
$$

are scalar random variables spanning a subspace of $L^2(\Omega)$.

The covariance matrix connects these two views:

$$
\Sigma_{ij}
=
\operatorname{Cov}(X_i,X_j)
=
\langle X_i-\mathbb E X_i,\;X_j-\mathbb E X_j\rangle_{L^2}.
$$

For deterministic directions $a,b$,

$$
a^T\Sigma b
=
\operatorname{Cov}(a^TX,b^TX).
$$

So covariance tells us the inner products between all scalar random variables obtained by linearly probing $X$.

The deepest summary is:

> A Gaussian vector is a random vector in ordinary finite-dimensional space, but its linear probes form a Gaussian subspace of $L^2(\Omega)$. Covariance is the bridge between these two geometries.

## 18. Suggested Reading Path

1. Berkeley Prob 140, **Random Vectors**  
   https://data140.org/fa18/textbook/chapters/Chapter_23/01_Random_Vectors

2. StatLect, **Multivariate Normal Distribution**  
   https://www.statlect.com/probability-distributions/multivariate-normal-distribution

3. Wisconsin Stat 609, **Multivariate Normal Distributions and Singular Covariance**  
   https://pages.stat.wisc.edu/~shao/stat609/stat609-15.pdf

4. Stanford CS233, **PCA Lecture Notes**  
   https://graphics.stanford.edu/courses/cs233-20-spring/ReferencedPapers/LectureNotes-PCA.pdf

5. QuantEcon, **Multivariate Normal Distribution**  
   https://stats.quantecon.org/multivariate_normal.html

6. Cornell CS4780, **Gaussian Processes**  
   https://www.cs.cornell.edu/courses/cs4780/2018sp/lectures/lecturenote15.html

