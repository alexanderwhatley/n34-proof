# Classifying the possible endpoint-dominant factors

Consider

```math
f=1-\sum_{i=1}^3E_i h_i,\qquad h_i=x^{a_i}(1-x)^{b_i},\qquad E_i>0.
```

A support is its exponent pair $`(a_i,b_i)`$. The shorthand $`(+,-)`$ records the signs of its two exponents, not the sign of its coefficient. At the left endpoint, the support with least first exponent dominates; at the right, the least second exponent dominates. Strict coordinate orders make these choices unique. A common endpoint dominant means the same support wins at both ends.

Put $`\rho=x(1-x)`$, $`D=\rho\,d/dx`$, $`g_i=Dh_i`$, $`S=\sum E_i h_i`$, and $`N=DS=-Df`$. The two-polynomial beta-factor bound (EHT) gives at most eight roots for a beta-weighted cubic plus another beta-weighted cubic. The [limiting-cases lemma](limiting-cases.md) permits us to examine a generic original row with ten simple roots when trying to disprove the nine-distinct-root bound. Equal endpoint signs then force exactly ten; opposite endpoint signs already give at most nine.

For the derivative counts below, simplicity of $`N`$ can be arranged without losing the ten simple original roots. Vary one $`E_i`$ and avoid the critical values of $`N/g_i`$ away from its at-most-one pole, after a small support perturbation if necessary. A multiple zero is also excluded directly when nine zeros of a quotient already exhaust the eight-root bound for its derivative. These statements concern the original parameters and do not perturb auxiliary root locations independently.

## A coordinate-zero boundary

**Lemma 1 (zero exponent implies at most eight roots).**  If some
$`a_i=0`$, then $`Z(f)\leq8`$.  The same holds if some $`b_i=0`$.

**Proof.** Relabel the term as
$`h_1=(1-x)^{b_1}`$.  First suppose $`b_1\ne0`$, and put

```math
u=h_1'=-b_1(1-x)^{b_1-1};
```

this never vanishes in $`(0,1)`$.  For
$`h_j=x^{a_j}(1-x)^{b_j}`$, direct differentiation gives

**(4)**

```math
W(u,h_j')=-b_1x^{a_j-2}(1-x)^{b_1+b_j-3}K_j(x),
```

where

**(5)**

```math
\begin{split}
 K_j(x)={}&\bigl((a_j-1)(1-x)-(b_j-b_1)x\bigr)
             \bigl(a_j-(a_j+b_j)x\bigr)\\
          &-(a_j+b_j)x(1-x)
 \end{split}
```

has degree at most two.  Since the $`h_1`$-term drops out,

**(6)**

```math
u^2(f'/u)'=W(u,f')=-E_2W(u,h_2')-E_3W(u,h_3').
```

After factoring a nonvanishing beta monomial, (6) is an equation
$`x^\alpha(1-x)^\beta P-Q=0`$ with
$`\deg P,\deg Q\leq2`$.  By (EHT), it has at most six roots.
If $`f`$ has $`m`$ distinct roots, then $`f'/u`$ has at least $`m-1`$
distinct roots and its derivative at least $`m-2`$, so $`m-2\leq6`$.
The identically-zero case of (6) makes $`f'/u`$ constant and is much
smaller.

If $`a_1=b_1=0`$, absorb $`E_1h_1`$ into the constant.  Then $`f'`$ is
a sum of two functions $`E_jh_j'`$.  Its zero equation, after removing
a beta monomial, is
$`x^\alpha(1-x)^\beta L_1-cL_2=0`$ with linear $`L_i`$, hence has at
most four roots by (EHT), and $`Z(f)\leq5`$.  Reflection proves the
$`b_i=0`$ assertion.  $`\square`$

## 3. Transition lemma for a mixed-sign dominant term

**Lemma 2 (a ten-root split chamber must have a unique negative left
exponent).**  Assume that $`L`$ is the unique minimizer of the left
exponents and

**(9)**

```math
a_L<0<b_L,\qquad a_L<a_i\quad(i\ne L),
```

and assume the right endpoint is negative, i.e. some $`b_R<0`$.
If $`f`$ had ten roots, then necessarily

**(10)**

```math
a_i>0\qquad(i\ne L).
```

**Proof.** Since $`a_L<0<b_L`$,

**(11)**

```math
g_L=(a_L(1-x)-b_Lx)h_L<0
```

throughout $`(0,1)`$.  Thus
$`H=N/g_L`$ is defined on the entire interval and has exactly the
zeros of $`N`$.

We work with a generic proposed counterexample having ten simple original roots, as justified above.  Rolle gives $`Z(N)\geq9`$.  On the other hand,

**(12)**

```math
g_L^2\,\delta H=W(g_L,N)
   =\sum_{i\ne L}E_iW(g_L,g_i),
```

and, after removing a beta factor, (12) is a beta-monomial times a
cubic minus a cubic.  Therefore (EHT) gives $`Z(\delta H)\leq8`$,
and Rolle gives $`Z(H)\leq9`$.  Consequently

**(13)**

```math
Z(H)=9,\qquad Z(\delta H)=8,
```

with the eight derivative roots lying between successive roots of
$`H`$; there is no derivative root before the first or after the last.
Moreover, all nine zeros of $`H`$ are simple: a multiple zero would
itself also be a zero of $`\delta H`$, in addition to the eight
inter-zero Rolle roots, contradicting $`Z(\delta H)\leq8`$.

The endpoint germs are sign-controlled.  Unique left dominance gives

**(14)**

```math
H(x)\longrightarrow E_L>0\qquad(x\to0+).
```

At the right, a $`b_R<0`$ term makes $`N\to+\infty`$, while
$`g_L<0`$ and tends to zero because $`b_L>0`$, so

**(15)**

```math
H(x)\longrightarrow-\infty\qquad(x\to1-).
```

Nine simple zeros therefore start with a downward crossing.  If
$`\delta H>0`$ in a left endpoint germ, $`H`$ must first acquire a
critical point before that downward crossing.  Together with the eight
inter-zero critical points this would contradict (13).

Let $`k\ne L`$ have the smallest $`a_k`$ among the remaining terms.
For distinct endpoint exponents,

**(16)**

```math
H=E_L+E_k\frac{a_k}{a_L}x^{a_k-a_L}(1+o(1))
```

at the left (terms with larger $`a_i`$ are lower order).  If
$`a_k<0`$, then $`a_k/a_L>0`$ and $`a_k-a_L>0`$, so
$`\delta H>0`$ in a left germ, the forbidden situation above.  If
$`a_k=0`$, Lemma 1 already excludes ten roots.  Hence $`a_k>0`$, and
then every $`a_i`$, $`i\ne L`$, is positive.  $`\square`$

Reflection gives the exact right-hand analogue.

**Lemma 3.**  If $`R`$ is the unique right minimizer and
$`b_R<0<a_R`$, then a ten-root configuration forces
$`b_i>0`$ for every $`i\ne R`$.

For clarity, applying Lemmas 2 and 3 classifies every generic split
pattern as follows.

**1.** If the left dominant is of type $`(- ,+)`$, ten roots force the
right dominant to be $`(+,-)`$, force the third term to be
$`(+,+)`$, and force all three indicated signs to be strict.  Thus
the only residual mixed-extreme split pattern is

**(17)**

```math
(-,+),\quad (+,+),\quad (+,-),
```

with the first term uniquely left-dominant and the last uniquely
right-dominant (the **pure split** chamber).

**2.** If the left dominant is $`(-,-)`$ but the right dominant is
$`(+,-)`$, Lemma 3 is contradicted by the left term's negative
$`b`$.  Hence ten is impossible.  The reflected pattern
$`(-,+)`$ versus a right-dominant $`(-,-)`$ is likewise impossible.

**3.** The only split pattern not decided by these transition lemmas has
**both distinct extreme dominants of type $`(-,-)`$**.  The third
term can have any of the four strict sign types.  Endpoint
dominance merely imposes (1).

The one-corner chamber always has a single dominant $`(-,-)`$ term and
two arbitrary strict-sign terms.  It is not decided by Lemmas 2--3.
Thus, after the transition exclusion, the complete residual registry
is:

**(18)**

```math
\boxed{\text{pure split (17); split with two distinct `--' extremes;
 one-corner with one `--' dominant.}}
```

## One-corner refinement

**Lemma.** Let $`D`$ be the unique coordinatewise dominant
negative-negative term. A ten-root configuration requires

**(R1)**

```math
\min_{j\ne D}a_j>0\quad\text{or}\quad \min_{j\ne D}b_j>0.
```

Because a ten-simple-root chamber is open, perturb generically within
it so endpoint orders are strict, the zeros of $`N`$ are simple, and
$`N(\rho_D)\ne0`$, where $`\rho_D`$ is the unique zero of $`g_D`$.
Put $`H=N/g_D`$ on the two sides of its pole. The cubic--cubic
equation for $`\delta H`$ has at most eight roots. Extended Rolle
across one pole gives $`Z(N)\leq10`$; opposite endpoint signs,
generic simplicity, and Rolle from ten roots of $`f`$ give
$`Z(N)=9`$.

If zeros occur on both sides of the pole, there are seven inter-zero
critical points. Another negative left exponent makes
$`\delta H>0`$ at the left endpoint although the first zero is a
downward crossing, forcing a pre-zero critical point. Another
negative right exponent makes $`\delta H<0`$ at the right endpoint
although the last zero is an upward crossing, forcing a post-zero
critical point. This totals nine, contradicting the EHT bound eight.
If all nine zeros lie on one side of the pole, there are already eight
inter-zero critical points and the corresponding endpoint mismatch
gives the ninth. This proves (R1).

Up to reflection, the only one-corner sign patterns still needing
work have

**(R2)**

```math
D=(-,-),\qquad v_2,v_3\in\{(+,+),(+,-)\}.
```

## Two distinct negative-negative extremes

**Lemma.** In a split chamber whose left and right dominant terms
$`L,R`$ are both negative-negative, ten roots force the third term $`K`$ to
be plus-plus.

Writing $`\rho_i`$ for the mode of a negative-negative term, coordinate
dominance gives $`\rho_R<\rho_L`$. Apply the same pole count to
$`N/g_L`$. Because a second negative left exponent is present, all
nine zeros of $`N`$ cannot lie left of $`\rho_L`$; hence one lies to
its right. The reflected argument for $`N/g_R`$ supplies a zero left
of $`\rho_R`$. At the left zero both $`g_L,g_R<0`$, so $`N=0`$
forces $`g_K>0`$. At the right zero both $`g_L,g_R>0`$, so $`N=0`$
forces $`g_K<0`$. The affine factor
$`a_K(1-x)-b_Kx`$ therefore changes from positive to negative,
forcing $`a_K,b_K>0`$.

## An elementary convexity exclusion

For one beta monomial,

**(19)**

```math
h''=x^{a-2}(1-x)^{b-2}
 \bigl(a(a-1)(1-x)^2-2abx(1-x)+b(b-1)x^2\bigr).
```

The quadratic factor is nonnegative for every $`0<x<1`$ exactly in
the following exponent cone:

**(20)**

```math
\mathcal C=\{a\leq0,b\leq0\}\cup
             \{a\leq0,b\geq1\}\cup
             \{a\geq1,b\leq0\}.
```

Necessity follows from the two endpoint coefficients and from the
negative second derivative at the interior mode when $`a,b\geq1`$.
Sufficiency is immediate when $`ab\leq0`$; when $`a,b<0`$, the
quadratic has positive endpoint coefficients and negative
discriminant $`4ab(a+b-1)<0`$.

**Lemma 4 (convex-mixture chamber).**  If all three exponent pairs
belong to $`\mathcal C`$, then $`S`$ is convex, $`f=1-S`$ is concave,
and $`f\not\equiv0`$ has at most two roots.  This covers, in
particular, the chamber in which all six exponents are negative, and
many split/two-`--` chambers whose opposite-sign positive exponents
are at least one.

## The resulting exhaustive table

After reflecting $`x\mapsto1-x`$ when necessary, a generic ten-simple-root candidate must belong to one of the following classes. The transition arguments give necessary conditions under that ten-root premise; they do not classify arbitrary support triples without it.

| Endpoint behavior | Necessary support types | Further theorem used in the complete proof |
|---|---|---|
| Both positive | Three $`(+,+)`$ supports | Positive-support height theorem |
| Both negative, different dominants, a mixed-sign extreme | $`(-,+),(+,+),(+,-)`$ | Split-support theorem |
| Both negative, different dominants, both negative-negative | $`(-,-),(+,+),(-,-)`$ | Separate signed-curvature exclusion |
| Both negative, one common dominant | One $`(-,-)`$ dominant; both other first coordinates positive | Common-dominant height theorem after normalization |

The convexity lemma above immediately settles any case where all three supports belong to its displayed cone. The other rows need the indicated theorems. In particular, the classification itself does not prove the separate signed-curvature exclusion.
