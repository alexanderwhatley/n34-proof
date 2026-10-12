# Native projective log curvature and directional barriers

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## 1. Actual entropy curves for every strong fork

Let $`P,Q\gt1`$, $`K=P+Q-1`$, and $`r\gt0`$. In the native projective chart use

```math
0\lt\theta\lt\min(1/P,r/Q),\qquad
A=1-P\theta,\quad B=r-Q\theta,\quad S=1+r-K\theta=A+B+\theta.
```

The probabilities are $`p_1=A/S`$, $`p_2=\theta/S`$, $`p_3=B/S`$. Define

```math
J(r,\theta)=\frac{P\log A+Q\log B-\log\theta-K\log S}{K},
```

```math
H(r)=P(P-1)r^2-2PQr+Q(Q-1),\qquad M=r(1+r)+\theta H(r).
```

Here $`M\gt0`$ throughout the open physical chart. It is affine in $`\theta`$, is positive at $`\theta=0`$, and at the active upper endpoint equals

```math
M(r,1/P)=\frac{(Pr-Q)(Pr-Q+1)}P\quad(r\ge Q/P),
```

```math
M(r,r/Q)=\frac rQ(Q-Pr)[Q-(P-1)r]\quad(r\le Q/P).
```

Both endpoint values are nonnegative. Affine interpolation is strictly positive before the endpoint, including $`r=Q/P`$. Direct differentiation gives

**(1)**

```math
J_\theta=-\frac{M}{K\theta ABS}\lt0,\qquad
J_r=\frac{Q-(P-1)r}{KBS}.
```

For each finite $`C`$, the equation $`J=C`$ defines one smooth physical curve $`\theta_C(r)`$ for all $`r\gt0`$. Indeed, at fixed $`r`$, $`J`$ decreases continuously from $`+\infty`$ to $`-\infty`$ as $`\theta`$ runs through its physical interval. Put $`T=Q-(P-1)r`$. Its exact derivatives are

**(2)**

```math
\theta_C'=\frac{\theta_C T(1-P\theta_C)}M,\qquad
\theta_C''=\frac{\theta_C(1-P\theta_C)(r-Q\theta_C)S H}{M^3}.
```

In particular, every actual native curve is strictly concave between the two roots $`\rho_-\lt\rho_+`$ of $`H`$, and strictly convex outside them.

The stronger global fact is **strict geometric log concavity**. For its projective elasticity

```math
\eta_C(r)=\frac{r\theta_C'(r)}{\theta_C(r)},
```

one has the square decomposition

**(3)**

```math
\boxed{\eta_C'(r)=
-\frac{(1-P\theta_C)(r-Q\theta_C)
\{\theta_C[H+Kr]^2+Kr^2S\}}{M^3}\lt0.}
```

Thus $`\log\theta_C(e^x)`$ has a strictly negative second derivative for all real $`x`$. This holds for arbitrary unequal $`P,Q`$, with no source metric or wall assumption. It is a rational differentiation identity followed by positivity of the displayed factors; no root isolation or numerical sampling is used.

## 2. Unconditional native source order in a strict-low wall sector

Take strictly positive outer supports $`s_i=(a_i,b_i)`$ with $`\gamma=a_3b_1-a_1b_3\ne0`$, and $`d_i=a_i+b_i`$. Write

```math
R(r)=\frac{(d_1+rd_3)(a_1+ra_3)(b_1+rb_3)}{\gamma^2},\qquad
Y(r)=R(r)-r(1+r),\qquad \theta_0(r)=\frac{Y(r)}{H(r)}.
```

Assume strict-low walls, equivalently $`Y(\rho_-)\gt0`$, $`Y(\rho_+)\gt0`$. Polynomial division gives

**(4)**

```math
\theta_0(r)=\ell_0+mr-\frac{V}{r-\rho_-}+\frac{U}{r-\rho_+},
```

where

```math
m=\frac{d_3a_3b_3}{\gamma^2P(P-1)}\gt0,\quad
U=\frac{Y(\rho_+)}{P(P-1)(\rho_+-\rho_-)}\gt0,\quad
V=\frac{Y(\rho_-)}{P(P-1)(\rho_+-\rho_-)}\gt0.
```

For every central $`c\in(\rho_-,\rho_+)`$ and every right outer $`g\gt\rho_+`$,

**(5)**

```math
\frac{\theta_0(g)-\theta_0(c)}{g-c}
=m+\frac{V}{(g-\rho_-)(c-\rho_-)}
  +\frac{U}{(g-\rho_+)(\rho_+-c)}\gt0.
```

Unlike normalized-middle-probability source order, this native order needs no affine-contrast or degree inequality. Reflection $`r\mapsto1/r`$, $`P\leftrightarrow Q`$, $`s_1\leftrightarrow s_3`$ gives the parallel statement for $`\phi_0(r)=\theta_0(r)/r`$: every left outer value exceeds every central value.

## 3. Directional height barriers and localization of simultaneous contacts

Put

```math
\alpha=\frac{Q-1}{P},\qquad \beta=\frac Q{P-1},\qquad
\rho_-\lt\alpha\lt\beta\lt\rho_+.
```

The inequalities follow from $`\alpha\lt\beta`$, positivity, and
$`H(\alpha)=-(Q-1)K/P\lt0`$, $`H(\beta)=-QK/(P-1)\lt0`$.
Equation (2) says that $`\theta_C`$ has its unique maximum at $`\beta`$. Its reflected version says that $`\phi_C=\theta_C/r`$ has its unique maximum at $`\alpha`$.

At every physically admissible central source point $`c\ge\beta`$, and every physically admissible right outer source point $`g\gt\rho_+`$,

**(6)**

```math
J(c,\theta_0(c))\gt J(g,\theta_0(g)).
```

To prove (6), set $`C=J(c,\theta_0(c))`$. The actual curve satisfies
$`\theta_C(g)\lt\theta_C(c)=\theta_0(c)\lt\theta_0(g)`$, by the actual maximum and (5). Since $`J_\theta\lt0`$, the outer source height is strictly below $`C`$. Reflection gives

**(7)**

```math
J(c,\theta_0(c))\gt J(g,\theta_0(g))
\quad(c\le\alpha,\ g\lt\rho_-).
```

Consequently, if one common finite entropy level meets both outer source components, every central contact at that level is confined to

**(8)**

```math
\boxed{\alpha\lt r\lt\beta.}
```

Statements (6)–(8) concern source height and actual entropy curves, not a claim that every central probability exceeds an outer probability. They therefore remain valid in the exact fixtures that disprove the latter claim. They also do not prove a bound on the number of central contacts inside (8).

## 4. A connected source elasticity positive band

Suppose the source has one central positive $`\theta_0`$ band whose endpoints are two simple roots $`c_1\lt c_2`$ of $`Y`$, with
$`\rho_-\lt c_1\lt c_2\lt\rho_+`$. Since $`Y`$ has positive constant and leading cubic coefficients, its third root is $`-l\lt0`$. For a positive constant $`q`$,

```math
\theta_0(r)=q\frac{(r+l)(r-c_1)(c_2-r)}{(r-\rho_-)(\rho_+-r)},
\qquad c_1\lt r\lt c_2.
```

For $`\eta_0=r\theta_0'/\theta_0`$, logarithmic differentiation gives

**(9)**

```math
\eta_0'=
\frac{l}{(r+l)^2}
-\left[\frac{c_1}{(r-c_1)^2}-\frac{\rho_-}{(r-\rho_-)^2}\right]
-\left[\frac{c_2}{(c_2-r)^2}-\frac{\rho_+}{(\rho_+-r)^2}\right].
```

The function $`(r+l)^2\eta_0'`$ is **strictly concave** on $`(c_1,c_2)`$. For a proof put

**(10)**

```math
f_s(r)=\frac{s(r+l)^2}{(r-s)^2},\qquad
f_s''(r)=\frac{2s(l+s)(3l+2r+s)}{(s-r)^4}.
```

Its parameter derivative is

**(11)**

```math
\partial_s f_s''(r)=
-\frac{2[3l^2r+9l^2s+2lr^2+14lrs+8ls^2+4r^2s+7rs^2+s^3]}{(s-r)^5}.
```

All numerator terms are positive. Therefore $`f_s''`$ increases strictly with $`s\lt r`$, and decreases strictly with $`s\gt r`$. Each of
$`f_{c_1}-f_{\rho_-}`$ and $`f_{c_2}-f_{\rho_+}`$ is strictly convex on the source band. Their sum is subtracted from $`l`$ in (9), proving strict concavity. Moreover, $`(r+l)^2\eta_0'\to-\infty`$ at both endpoints. Its positive set is empty or one open interval. There can be at most two zeros counted with multiplicity; at an interior tangent zero, strict negative second derivative gives multiplicity exactly two.

This connected-band statement and the actual log-concavity statement (3) do **not**, by themselves, bound the zeros of $`\eta_0-\eta_C`$. A central entropy maximum can occur while both elasticity derivatives are negative. No step from this lemma to unrestricted height ordering is asserted.
