# An all-scale mixed height theorem whenever the pair cofactor has three roots

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Source and conclusion

Let $`A,B,a,b,c,\nu>0`$, $`B>\nu`$, $`c>a`$. For arbitrary positive
coefficients consider

**(1)**

```math
f(t)=1-E_0t^{-A}(1-t)^{-B}-E_1t^a(1-t)^b-E_2t^c(1-t)^{-\nu}.
```

Use $`\mathscr D=t(1-t)d/dt`$, the source slopes
$`\ell_0=-A+(A+B)t`$, $`\ell_1=a-(a+b)t`$,
$`\ell_2=c-(c-\nu)t`$, and $`P_i=\ell_i^2+\mathscr D\ell_i`$. Put

```math
R=\ell_1P_2-\ell_2P_1,\qquad
H=\det\begin{pmatrix}1&1&1\\\ell_0&\ell_1&\ell_2\\P_0&P_1&P_2\end{pmatrix},
\quad K=H-R,
```

```math
p=c-a>0,\qquad q=b+\nu>0,\qquad L=p+(q-p)t>0.
```

**Theorem.** On every strict generic source for which $`R`$ has three
physical roots, every positive level of

```math
\Phi(t)=t^A(1-t)^B R(t)/H(t)
```

has at most six contacts on its entire positive locus. In particular it
has at most six useful contacts $`RK>0`$. Hence (1) has at most eight
distinct roots. The theorem is uniform in all positive coefficients and
all scales, and requires no sign assumption on $`K`$.

Finite original-row limits of this source region inherit the nonidentity
eight-distinct-root bound by compact common-level regularization and
support perturbation. The result is a sufficient mixed subregion, rather
than a claimed closure of all mixed rows.

## The pair normal form

The independently derived pair lemma gives

```math
m=\frac a{a+b}\in(0,1),\quad d=\frac{bc+a\nu}{a+b}>0,
\quad z=\frac{t-m}{1-t}>0,
```

```math
\frac{(1+z)^3}{b}R(t)=C(z)
=dm-dDz+d\kappa z^2-\nu qz^3,
```

**(2)**

```math
D=d-1-m>0,\qquad\kappa=1-q-\nu>0,
\quad q>\nu>0,\quad p>1>q.
```

All three physical roots are after $`m`$. Write their positive translated
coordinates as $`z_1<z_2<z_3`$. The exact Vieta identities are

**(3)**

```math
S_1=z_1+z_2+z_3=\frac{d\kappa}{\nu q},\quad
S_2=z_1z_2+z_1z_3+z_2z_3=\frac{dD}{\nu q},\quad
P=z_1z_2z_3=\frac{dm}{\nu q}.
```

## The smallest translated root lies below 1/nu

Suppose all $`z_i\ge1/\nu`$. Reciprocal Vieta gives
$`D/m=\sum_i1/z_i\le3\nu`$, hence
$`D<3\nu`$ and $`d=1+m+D<2+3\nu`$.
The product identity and $`m<1,q>\nu`$ give

```math
d>\frac q{\nu^2}>\frac1\nu.
```

Thus $`1/\nu<2+3\nu`$, which forces $`\nu>1/3`$.
On the other hand, the sum identity gives $`d\kappa\ge3q`$, so

```math
d\ge\frac{3q}{1-q-\nu}>\frac{3\nu}{1-2\nu}.
```

Here $`\nu<1/2`$ by (2). For $`\nu>1/3`$, the rightmost expression is
strictly greater than $`2+3\nu`$, contradicting the upper bound on $`d`$.
Therefore

**(4)**

```math
\boxed{\nu z_1<1.}
```

This elementary root-size bound is independent of $`A,B`$.

## The actual shifted cofactor is positive after the last R root

The source identity $`H=R`$ with the exponents shifted by $`A,B`$ remains
valid in the mixed chart. At the weak boundary $`A=0,B=\nu`$, it gives

```math
H_{\rm bdry}(t)=c(1-t)\{[a-(a+q)t]L+qt\}
=\frac{c(1-t)}{(1+z)^2}J(z),
```

**(5)**

```math
J(z)=q(1-q)z^2-q(D+m\nu)z+m(q-\nu d).
```

Direct subtraction gives the exact identity

**(6)**

```math
\boxed{dJ(z)-qC(z)=\nu(d+qz)(qz^2-dm).}
```

Put $`k=\nu q/d>0`$. At the largest $`C`$-root, Vieta gives the visible
positive factorization

**(7)**

```math
\boxed{J(z_3)=qz_3(\nu+kz_3)(z_3-\nu z_1z_2)>0.}
```

Indeed (4) and $`z_2<z_3`$ imply $`\nu z_1z_2<z_2<z_3`$.
A second positive factorization gives

**(8)**

```math
\boxed{\frac{J'(z_3)}q=2\nu z_3+
 k\{2z_3^2+z_1(z_3-z_2)+z_2z_3(1-\nu z_1)\}>0.}
```

Because $`J`$ is an upward quadratic, (7)--(8) show
$`J(z)>0`$ for every $`z\ge z_3`$. Thus the boundary cofactor is positive
throughout the final $`R`$-negative tail.

It remains to check that increasing $`A,B`$ cannot lower $`H`$ there.
For any such point put

```math
X=\ell_0=-A(1-t)+Bt,\quad Y=\nu t\in(0,1),
\quad Z=\ell_1+\ell_2+\frac{qt}L.
```

The literal original-core formula is

**(9)**

```math
\boxed{H/L=R/L+X^2-ZX+Bt.}
```

In the translated coordinate, $`Z-2Y`$ has the positive denominator
$`(1+z)(d+qz)`$ and numerator

**(10)**

```math
\boxed{d^2+qm-2\nu md+q(1+m-2m\nu)z+q(1-q)z^2>0.}
```

Every coefficient is positive by (2): $`d>1+m>2\nu m`$ and
$`\nu<1/2`$. Thus $`Z>2Y`$. Since $`R\le0`$ on $`z\ge z_3`$ and
$`H_{\rm bdry}>0`$, evaluating (9) at $`X=Y,B=\nu`$ gives
$`Z<1+Y`$.

For fixed $`X`$, the constraints $`A\ge0,B\ge\nu`$ give
$`B\ge\max(\nu,X/t)`$. If $`X\le Y`$, the lower expression in (9) is
$`R/L+X^2-ZX+Y`$, which strictly decreases up to $`Y`$, because
$`Z>2Y`$. If $`X\ge Y`$, it is
$`R/L+X^2-(Z-1)X`$, which strictly increases from $`Y`$, because
$`Z<1+Y`$. Both have their minimum at $`X=Y,B=\nu`$.
Consequently

**(11)**

```math
\boxed{H(t)\ge H_{\rm bdry}(t)>0\qquad(t\ge r_3),}
```

where $`r_3=(m+z_3)/(1+z_3)`$ is the last physical $`R`$-root.
In particular, if $`H`$ has two physical roots, both precede $`r_3`$.
This eliminates all four formally possible R/H root orders ending in an
H-root, using the shared source rather than an event-word table.

## Common-height count

The actual phase numerator is $`-L W`$, where

```math
W=\det\begin{pmatrix}\ell_0&\ell_1&\ell_2\\P_0&P_1&P_2\\Q_0&Q_1&Q_2\end{pmatrix},
\quad Q_i=\ell_iP_i+\mathscr DP_i.
```

It has degree at most six. If $`H`$ has no physical root, $`\Phi`$ has two
positive components and two separate negative excursions with zero endpoint
limits: one between $`r_1,r_2`$, one between $`r_3,1`$. Each consumes a
critical point outside the positive locus. Thus at most four useful critical
points remain, and any positive level has at most $`4+2=6`$ contacts.

If $`H`$ has two physical roots $`h_1<h_2<r_3`$, its negative cubic leading
coefficient, positive endpoint values, and two simple physical roots give
one exterior root $`\eta_e>1`$. On $`(0,r_3)`$, factor

**(12)**

```math
\Phi=C_0\,v(t)\frac{(t-r_1)(t-r_2)}{(t-h_1)(t-h_2)},
\quad C_0>0,\quad
v=t^A(1-t)^B\frac{r_3-t}{\eta_e-t}.
```

The factor $`v`$ tends to zero at both endpoints of $`(0,r_3)`$ and is
strictly log-concave, since

```math
(\log v)''=-A/t^2-B/(1-t)^2-1/(r_3-t)^2+1/(\eta_e-t)^2<0.
```

The negative tail $`(r_3,1)`$ has no pole by (11), and has zero limits at
both endpoints. It consumes one of the six critical points. Thus at most
five remain on $`(0,r_3)`$. If the two zero/pole pairs overlap, the [quadratic ratio common level theorem](quadratic-ratio-level-count.md) gives at most six positive
contacts there. If the pairs are disjoint, the bounded negative zero-zero
interval and the negative pole-pole interval each contain a critical point;
componentwise Rolle again gives at most $`(5-2)+3=6`$ positive contacts.
No $`K`$-root ordering enters either conclusion.

## Transfer to the original row

All original zeros of (1) lie in the one interval
$`I=\{1-E_0t^{-A}(1-t)^{-B}>0\}`$, because the other two terms are positive.
The original two-Rolle interface gives at least $`n-2`$ contacts of one
positive level $`\Phi=E_0`$, with $`0<R/H<1`$, from any $`n`$ original zeros
on a generic core source. The six-contact bound therefore gives $`n\le8`$.
This uses the actual coefficients throughout.

For a finite nonidentity original-row limit, choose compact neighborhoods
of a hypothetical nine distinct roots. A small common constant shift keeps
at least nine simple nearby roots, using the larger of the two even-extremum
counts. The equation remains in (1) after all three coefficients are scaled
by the same positive factor. Its sign brackets persist under approximation
from the strict three-R-root source region, contradicting the bound eight.
No divided auxiliary ratio continuity or endpoint limit is used.
