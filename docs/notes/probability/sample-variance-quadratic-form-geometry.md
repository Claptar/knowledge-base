---
title: "Sample Variance as a Quadratic Form and Its Geometry"
---

> **Imported note.** Written by me with an AI assistant in [Claptar/math-notes](https://github.com/Claptar/math-notes), imported 2026-09-13. It is *material* — my own exposition — not a record of a worked session. Nothing here is evidence that it has been derived from scratch; a [topic file](../../questions.md) is earned separately.

> **Alternative treatment.** [`sample-variance-quadratic-form`](sample-variance-quadratic-form.md) covers the same material by a different route. Both are kept deliberately — comparing two expositions of one idea is worth more than picking a winner.

# Sample Variance as a Quadratic Form and Its Geometry

## Main question

We understand that the sample variance can be written as a quadratic form on coordinate space. But to diagonalise this quadratic form, for example using spectral decomposition or Gram-Schmidt, we need a dot product on the space.

The natural question is:

> Why is it legitimate to use the ordinary Euclidean dot product  
> $$
> x_1y_1+\cdots+x_ny_n?
> $$
>
> And why does Euclidean orthogonality of the diagonalising directions later correspond to independence of the transformed Gaussian random variables?

The answer is that there are two geometries involved:

1. **Euclidean geometry on coordinate space** $\mathbb R^n$.
2. **Covariance geometry on random variables**, determined by the covariance matrix $\Sigma$.

These two geometries are not always the same. They become aligned in the special case where the original Gaussian variables are i.i.d. with common variance $\sigma^2$, because then

$$
\Sigma=\sigma^2 I.
$$

---

## 1. Sample variance is first a function on coordinate space

Before introducing randomness, take a deterministic vector

$$
x=(x_1,\dots,x_n)\in\mathbb R^n.
$$

Its average is

$$
\bar x=\frac1n\sum_{i=1}^n x_i.
$$

The vector of deviations from the mean is

$$
x-\bar x\mathbf 1,
$$

where

$$
\mathbf 1=(1,\dots,1)^T.
$$

The unnormalised sample variance is

$$
\sum_{i=1}^n (x_i-\bar x)^2.
$$

This is the squared Euclidean length of the deviation vector:

$$
\sum_{i=1}^n (x_i-\bar x)^2
=
\langle x-\bar x\mathbf 1,\,x-\bar x\mathbf 1\rangle_{\mathbb R^n}.
$$

So the ordinary dot product is not added artificially later. It is already built into the usual definition of sample variance.

---

## 2. The projection matrix

Define

$$
P=I-\frac1n\mathbf 1\mathbf 1^T.
$$

Then

$$
Px=x-\bar x\mathbf 1.
$$

The matrix entries are

$$
P_{ij}
=
\begin{cases}
1-\frac1n, & i=j,\\
-\frac1n, & i\ne j.
\end{cases}
$$

The unnormalised sample variance is therefore

$$
q(x)=x^TPx.
$$

For the usual unbiased sample variance,

$$
S^2(x)=\frac1{n-1}x^TPx.
$$

For the version with denominator $n$,

$$
S_n^2(x)=\frac1n x^TPx.
$$

The matrix $P$ is the Euclidean orthogonal projection onto the mean-zero subspace.

---

## 3. The geometric decomposition of coordinate space

Coordinate space decomposes as

$$
\mathbb R^n
=
\operatorname{span}\{\mathbf 1\}
\oplus
\mathbf 1^\perp,
$$

where

$$
\mathbf 1^\perp
=
\left\{x\in\mathbb R^n: \sum_{i=1}^n x_i=0\right\}.
$$

The direction

$$
\operatorname{span}\{\mathbf 1\}
$$

is the direction where all coordinates move together:

$$
(c,c,\dots,c).
$$

This direction contains no variation between coordinates. It only changes the common level of the sample.

The subspace

$$
\mathbf 1^\perp
$$

contains the genuine fluctuations around the mean.

The projection $P$ satisfies

$$
P\mathbf 1=0,
$$

and if $x\in\mathbf 1^\perp$, then

$$
Px=x.
$$

So $P$ kills the mean direction and keeps the fluctuation directions.

---

## 4. Why the Euclidean dot product is natural

The ordinary sample variance treats the coordinates symmetrically and measures deviation using a sum of squares:

$$
(x_1-\bar x)^2+\cdots+(x_n-\bar x)^2.
$$

That is exactly the Euclidean squared norm.

Thus the dot product

$$
\langle x,y\rangle=x_1y_1+\cdots+x_ny_n
$$

is part of the definition of ordinary sample variance.

If we used a different dot product, we would be defining a different statistic. For example, a weighted inner product would give a weighted variance-like quantity.

So it is both legal and natural to diagonalise $P$ using the standard Euclidean structure on $\mathbb R^n$, because $P$ was built from the Euclidean operation of subtracting the orthogonal projection onto the constant-vector direction.

---

## 5. Diagonalising the sample variance quadratic form

Let

$$
u_1=\frac1{\sqrt n}(1,\dots,1).
$$

Then choose any Euclidean orthonormal basis

$$
u_2,\dots,u_n
$$

of the mean-zero subspace $\mathbf 1^\perp$.

In this basis,

$$
Pu_1=0,
$$

and

$$
Pu_k=u_k,\qquad k=2,\dots,n.
$$

Therefore the diagonal form of $P$ is

$$
\operatorname{diag}(0,1,\dots,1).
$$

If

$$
x=a_1u_1+\cdots+a_nu_n,
$$

then

$$
x^TPx=a_2^2+\cdots+a_n^2.
$$

The first coordinate $a_1$ is the mean direction. It contributes nothing to sample variance. The remaining coordinates $a_2,\dots,a_n$ are fluctuation coordinates.

---

## 6. Now introduce the random vector

Let

$$
X=(X_1,\dots,X_n)^T
$$

be a random vector.

The sample variance is the deterministic quadratic form evaluated at the random vector:

$$
S^2=\frac1{n-1}X^TPX.
$$

Let $U$ be the orthogonal matrix whose columns are

$$
u_1,\dots,u_n.
$$

Define the transformed random vector

$$
Y=U^TX.
$$

Then

$$
Y_1=u_1^TX
=\frac1{\sqrt n}(X_1+\cdots+X_n)
=\sqrt n\,\bar X.
$$

The remaining variables

$$
Y_2,\dots,Y_n
$$

are fluctuation coordinates.

Because $U$ diagonalises $P$, we get

$$
X^TPX
=
Y_2^2+\cdots+Y_n^2.
$$

Therefore

$$
S^2=\frac1{n-1}(Y_2^2+\cdots+Y_n^2).
$$

Up to this point, this is just linear algebra plus substitution of a random vector. No independence has been used yet.

---

## 7. Covariance geometry of linear combinations

Now consider the covariance geometry.

For deterministic vectors $u,v\in\mathbb R^n$, the corresponding linear combinations are

$$
u^TX
$$

and

$$
v^TX.
$$

Their covariance is

$$
\operatorname{Cov}(u^TX,v^TX)
=
u^T\Sigma v,
$$

where

$$
\Sigma=\operatorname{Cov}(X)
$$

is the covariance matrix of the random vector $X$.

So covariance defines a second geometry on coefficient space:

$$
\langle u,v\rangle_\Sigma=u^T\Sigma v.
$$

This is not necessarily the same as the Euclidean dot product

$$
\langle u,v\rangle=u^Tv.
$$

---

## 8. Why Euclidean orthogonality gives independence in the i.i.d. Gaussian case

Suppose now that

$$
X_1,\dots,X_n
$$

are i.i.d. Gaussian random variables with common variance $\sigma^2$. Then

$$
\Sigma=\sigma^2 I.
$$

For the transformed variables

$$
Y_i=u_i^TX,
\qquad
Y_j=u_j^TX,
$$

their covariance is

$$
\operatorname{Cov}(Y_i,Y_j)
=
u_i^T\Sigma u_j.
$$

Since $\Sigma=\sigma^2 I$, this becomes

$$
\operatorname{Cov}(Y_i,Y_j)
=
\sigma^2 u_i^T u_j.
$$

Therefore, in the i.i.d. case,

$$
u_i\perp u_j
\quad\Longrightarrow\quad
\operatorname{Cov}(Y_i,Y_j)=0.
$$

And because the transformed variables are jointly Gaussian, zero covariance implies independence.

So for jointly Gaussian variables,

$$
\operatorname{Cov}(Y_i,Y_j)=0
\quad\Longrightarrow\quad
Y_i\text{ and }Y_j\text{ are independent}.
$$

This is the reason Euclidean orthogonality of the diagonalising directions turns into probabilistic independence of the transformed random variables.

---

## 9. The synchronization of the two geometries

In the i.i.d. Gaussian case, the covariance inner product is

$$
\langle u,v\rangle_\Sigma
=
u^T\Sigma v
=\sigma^2 u^Tv.
$$

So it is just a scalar multiple of the Euclidean dot product.

Therefore:

$$
\text{Euclidean orthogonality}
\quad\Longleftrightarrow\quad
\text{zero covariance}
\quad\Longleftrightarrow\quad
\text{independence, for Gaussian variables.}
$$

This is why the diagonalisation of the sample variance matrix feels perfectly compatible with covariance and independence.

The compatibility is real, but it depends on the covariance matrix being

$$
\Sigma=\sigma^2 I.
$$

That is, the original Gaussian vector must be isotropic, or spherical, up to scale.

---

## 10. What goes wrong in the non-i.i.d. case

If the covariance matrix is not a scalar multiple of the identity, then Euclidean orthogonality does not necessarily imply zero covariance.

For example, suppose

$$
X_1,X_2
$$

are independent Gaussian variables with

$$
\operatorname{Var}(X_1)=1,
\qquad
\operatorname{Var}(X_2)=4.
$$

Then

$$
\Sigma=
\begin{pmatrix}
1&0\\
0&4
\end{pmatrix}.
$$

Take the Euclidean orthogonal vectors

$$
u=(1,1),
\qquad
v=(1,-1).
$$

They satisfy

$$
u^Tv=0.
$$

But the corresponding random variables are

$$
u^TX=X_1+X_2,
$$

and

$$
v^TX=X_1-X_2.
$$

Their covariance is

$$
\operatorname{Cov}(X_1+X_2,\,X_1-X_2)
=
\operatorname{Var}(X_1)-\operatorname{Var}(X_2)
=1-4
=-3.
$$

So even though the coefficient vectors are Euclidean orthogonal, the random variables are not uncorrelated, and therefore not independent.

This shows that Euclidean orthogonality and covariance orthogonality are generally different notions.

---

## 11. The general rule

For a Gaussian random vector

$$
X\sim N(\mu,\Sigma),
$$

two linear combinations

$$
u^TX
$$

and

$$
v^TX
$$

are independent exactly when

$$
u^T\Sigma v=0.
$$

So the probabilistically relevant orthogonality is not usually

$$
u^Tv=0,
$$

but rather

$$
u^T\Sigma v=0.
$$

When

$$
\Sigma=\sigma^2 I,
$$

these two conditions are equivalent.

---

## 12. Consequence for sample mean and sample variance

In the i.i.d. Gaussian case, after choosing the Euclidean orthonormal basis

$$
u_1=\frac1{\sqrt n}\mathbf 1,
\qquad
u_2,\dots,u_n\in\mathbf 1^\perp,
$$

we get

$$
Y_1=\sqrt n\,\bar X,
$$

and

$$
S^2=\frac1{n-1}(Y_2^2+\cdots+Y_n^2).
$$

The variable $Y_1$ is independent of $Y_2,\dots,Y_n$, because its coefficient vector is Euclidean orthogonal to the coefficient vectors of the fluctuation directions, and Euclidean orthogonality agrees with covariance orthogonality when $\Sigma=\sigma^2I$.

Therefore the sample mean is independent of the sample variance in the i.i.d. Gaussian case.

This independence is not just a consequence of diagonalising the sample variance matrix. It also uses the fact that the covariance matrix of $X$ is proportional to the identity.

---

## Final summary

The sample variance quadratic form lives first on coordinate space:

$$
q(x)=x^TPx,
\qquad
P=I-\frac1n\mathbf 1\mathbf 1^T.
$$

The ordinary Euclidean dot product is natural because sample variance is defined as a sum of squared Euclidean deviations from the constant-vector subspace:

$$
\sum_{i=1}^n (x_i-\bar x)^2.
$$

Diagonalising $P$ uses Euclidean geometry and gives the decomposition

$$
\mathbb R^n
=
\operatorname{span}\{\mathbf 1\}
\oplus
\mathbf 1^\perp.
$$

When we plug in a Gaussian random vector $X$, the covariance geometry is governed by

$$
\operatorname{Cov}(u^TX,v^TX)=u^T\Sigma v.
$$

If $X_1,\dots,X_n$ are i.i.d. with variance $\sigma^2$, then

$$
\Sigma=\sigma^2I,
$$

so covariance geometry is just Euclidean geometry up to scale.

That is why Euclidean orthogonal diagonalising directions produce uncorrelated, and hence independent, transformed Gaussian variables.

The key point is:

$$
\boxed{
\text{The coordinate dot product and covariance geometry agree only in the isotropic i.i.d. case.}
}
$$
