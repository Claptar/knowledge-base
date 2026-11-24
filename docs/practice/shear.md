# Shears — practice

Attempts from the sessions in [topics/shear.md](../topics/shear.md): a short Cowork session on
2026-11-03, then a claude.ai session dated 2026-11-03 to 2026-11-14 as a whole. Handwritten and
tablet pages are known from the transcripts' transcriptions of them.

## 2026-11-03 — which vectors does a column operation fix? (Cowork)

**Problem:** $\hat T e_j = e_j + c\,e_i$ with $i \neq j$, every other basis vector fixed. Which
vectors does $\hat T$ leave where they are, and what does it do to the rest?
**Worked unaided up to:** both halves, on the board: "Obviously those that have a zero x_j
projection", with the fixed-point condition $x_j\,c\,e_i = 0$ boxed and $\hat T x$ written out.
**Derived unaided.**
**Where I asked for a hint:** none. Before any problem I asked for the route first: "Let's take a
step back and first come up with a route to shear operator and then only play with that".
**Attempt:** the board, which also restated my three consequences of multiplicativity.
**Outcome:** solved.
**What it revealed:** "projection" for a coordinate. Without an inner product a coordinate is not
read off $e_j$ alone — Question 2, still open. A slip: the matrix drawn was $I + cE_{21}$, written
$E + cE_{12}$ — the row/column habit in [profile.md](../profile.md#notation-and-conventions).
**Revisit:** Question 2: what does a single coordinate depend on?

## 2026-11-03 to 14 — Problem 1(a): from a column operation to a map

**Problem:** "add $c$ times column 1 to column 3" replaces $\hat A$ by $\hat A \circ \hat T$. Find
$\hat T$, the vectors it fixes, how the others move, and $\varphi, w$ with $\hat T x = x +
\varphi(x)\,w$. What condition on $\varphi, w$ says the two columns differ, and what is "column 3
into column 3"?
**Worked unaided up to:** $\hat T$ from the images of the basis; "T fixes vectors with x3=0";
"They move in e1 direction"; "phi(x) here is clearly c * x3 and w is e1".
**Where I asked for a hint:** none. My own doubt found the gap: "I struggle to defend the last
equation as I'm not sure there is no other T that would work for it". Supplied: $\hat T$ has to
work for every $\hat A$, so take $\hat A = \hat I$; and that "different columns" is $\varphi(w) = 0$.
**Attempt:** two notebook pages. The first compared coefficients of $\hat A e_1, \hat A e_2,
\hat A e_3$; the second cancelled $\hat A$ from $\hat A(\hat T e_k) = \dots$. For the condition:
"It's not clear to me to be honest. I could make it Te3 = ce3 + e3 instead and would get cx3 as phi
and w as e3. I see nothing criminal in this move. And it feels like it is still shear in a way";
then "Not sure to be honest".
**Outcome:** solved except the condition, which was given.
**What it revealed:** cancelling a map needs it injective — both pages did it, and with
$\hat A = 0$ every $\hat T$ works. Partly the problem statement, which did not say $\hat T$ must work
for all $\hat A$. The column-3-into-column-3 map fixes the same plane but stretches $e_3$ by
$1 + c$: right family, wrong member — the intuition is exactly right at the level of "fixes a
hyperplane pointwise", which is 1(b). And "Wat?" at the one-line claim "the two columns are
different exactly when $\varphi(w) = 0$" — a compressed sentence, a session failure.
**Revisit:** —

## 2026-11-03 to 14 — Problem 1(b): every map that fixes a hyperplane

**Problem:** a map $\hat G$ fixes every vector of a hyperplane $H$. Show $\hat G x = x +
\varphi(x)\,w$ with $\ker \varphi = H$, and decide whether the pair is unique.
**Worked unaided up to:** the construction — "Let's say that a hyperplane is such that V = H ⊕ ⟨u⟩",
$\hat G u = t_1 v + t_2 u$, so $\hat G x = x + \alpha[t_1 v + (t_2 - 1)u]$ with $\varphi(x) = \alpha$.
**Derived unaided.**
**Where I asked for a hint:** none. Added afterwards: why such a $u$ exists, why $\varphi$ is linear
with kernel $H$, and that the bracket is just $\hat G u - u$. Uniqueness: "It's easy let's move
forward" — skipped, the answer stated for the record.
**Outcome:** solved.
**What it revealed:** the capability — I chose a complement and a coordinate without being told to.
**Revisit:** uniqueness of $(\varphi, w)$, if it ever matters.

## 2026-11-03 to 14 — Problem 1(c), item 1: the case $\varphi(w) \neq 0$

**Problem:** find a line $L \not\subset H$ that $\hat G$ maps to itself, and its factor $s$.
**Worked unaided up to:** after two false starts, the key step: from $x + \alpha w = s x$,
$x = \frac{\alpha}{s-1}\,w$, so the only candidate line is the line of $w$.
**Where I asked for a hint:** none asked. The difference between "maps $L$ to itself" and "fixes
$L$" was explained after the first attempt; after my circular substitution, the move "$\alpha$ is
not free: $\alpha = \varphi(x)$" was supplied, unasked, giving $s = 1 + \varphi(w)$.
**Attempt:** first set $\hat G x = x$ and got $\hat G u = \frac1c u$ — "But this is a whole plane,
isn't it?"; then $\hat G u = u$. Then "Okay, so the question is about vectors that stay on the line
not those that are fixed". After the key step, substituted back into $\hat G w = s w$ and expanded
$\hat G(\hat G u - u)$, with a sign slip.
**Outcome:** solved with the last move supplied.
**What it revealed:** a line mapped to itself read as a line of fixed points; fixed vectors are the
case $s = 1$. My "a whole plane" was right about the set — but it was the level set $\varphi = c$,
an affine plane that misses $0$. And a symbol defined as $\varphi(x)$ treated as a free number;
check: *have I used what each symbol is?*
**Revisit:** —

## 2026-11-03 to 14 — Problem 1(c), item 2: the case $\varphi(w) = 0$

**Problem:** show $\hat G$ is invertible with an inverse of the same form, and that no line outside
$H$ is mapped to itself.
**Worked unaided up to:** both. No invariant line: $\hat G x = x + \alpha h$ with $\alpha, h \neq 0$
forces $x \in H$. The inverse: $\hat G^{-1} y = h + \alpha(u - w)$, that is $y - \varphi(y)\,w$.
**Derived unaided.**
**Where I asked for a hint:** none. Then I questioned the correction: "But I basically present the
inverse, don't I? Isn't it the same as proving that it exists? I can try to check it with G^-1 G x"
— and did the check. That a one-sided check is enough in finite dimensions was supplied.
**Outcome:** solved.
**What it revealed:** the trap from the determinant sessions, the other way round: a derivation
that applies $\hat G^{-1}$ assumes it exists, so it produces a candidate, and the candidate becomes
a proof once checked. This time the fix was my own proposal. Where $\varphi(w) = 0$ enters: the last
term of the check, because $w \in H$ is fixed.
**Revisit:** —

## 2026-11-03 to 14 — Problem 1(c), item 3: the non-invertible member

**Problem:** for which $\varphi(w)$ is $\hat G$ not invertible, and what is it then?
**Worked unaided up to:** $\varphi(w) = -1$ from $\hat G w = 0$, and the image inside $H$; in the
recap, "makes sense it is not invertible as dim(Im T̂) = dim H = n − 1". **Derived unaided** that
far.
**Where I asked for a hint:** none. Supplied: why $\varphi(w) = -1$ is the *only* such case (the
kernel can only be the line of $w$), and the name, projection onto $H$ along $w$. Then I asked:
"You are saying that G is projection in such case, but u does not have a component in H. How do I
shouw that hu is zero".
**Outcome:** solved, with the "only" direction supplied.
**What it revealed:** "the component in $H$" held as if it were defined by $H$ alone. It depends on
the complement: in $H \oplus \langle u \rangle$, $u$ has none; in $H \oplus \langle w \rangle$, which
the projection uses, it has $h_u$. The intuition is right in the splitting I had chosen. Without an
inner product, "the projection onto $H$" needs a direction.
**Revisit:** —

## 2026-11-03 to 14 — Problem 1(c), item 4: what $s$ measures

**Problem:** with $\hat G u = t_1 v + t_2 u$, express $\varphi(w)$ through $t_2$; show $t_2$ does
not depend on the choice of $u$; find $\varphi(\hat G x)$ in terms of $\varphi(x)$ and say what $s$
measures.
**Worked unaided up to:** all three computations, and the sentence: "It says that u component of x
is strestched in s times after the application of G". **Derived unaided**, one line skipped.
**Where I asked for a hint:** "Can you formulate it better? I don't remember what was the t1 and t2"
— the problem pointed back at symbols from much earlier; restated in full. The basis-free reading of
my sentence was supplied.
**Outcome:** solved.
**What it revealed:** the capability. The sentence was right; what it lacked was independence from
$u$: one height means nothing, a ratio of heights does — the same move as Road 3's ratio along a
line.
**Revisit:** —

## 2026-11-03 to 14 — Problem 2: shears along one hyperplane

**Problem:** fix $H$ and one $\varphi$; for $w \in H$ let $\hat T_w x = x + \varphi(x)\,w$.
(a) Compose two. (b) Powers and the inverse. (c) Is $w \mapsto \hat T_w$ injective, and what
structure do these maps form? (d) Fix $w$ and vary the function instead.
**Worked unaided up to:** (b): $\hat T_w^m x = x + m\,\varphi(x)\,w$ and the inverse
$x - \varphi(x)\,w$. **Derived unaided**, with the cross term skipped.
**Where I asked for a hint:** none. (a) and (c) were corrected and the answers given.
**Attempt:** (a) $x + \varphi(x)\,w + \varphi'(x)\,w'$; (c) "not injective, as the choice of φ(x)
also matters", and "{T̂_w : w ∈ H} should be isomorphic to V/H × all possible choices to select φ(x)
such that ker φ = H".
**Outcome:** (b) solved; (a), (c) given; (d) not started.
**What it revealed:** the freedom in $(\varphi, w)$ from 1(b) carried into a problem where fixing
$\varphi$ had removed it — what is fixed and what varies. The skipped cross term is where
$\varphi(w') = 0$ does its work. $V/H$ is one-dimensional and every shear acts on it trivially; the
group lives in $H$.
Then: "Okay, I realised that I need to first get the whole idea of what is going on before I
approach the problems myself."
**Revisit:** (a) and (c) cold, then (d).
