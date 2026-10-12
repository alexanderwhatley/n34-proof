# Signed height separation at a zero left exponent of q

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Analytic boundary lemma, 2 October 2026. This proves a source-linked two-pole height separator at $`a_q=0`$. It retains the signed interlacing inequality; it is not an unconditional boundary theorem and does not itself justify deformation from a positive $`a_q`$.

## Actual source and the retained signed cell

Let

```math
q=(1-x)^B,\qquad v=x^{a_v}(1-x)^{b_v},\qquad
u=v^h q^n,
```

with $`B,a_v,b_v>0`$, $`0<h<1`$, $`n<0`$, strictly positive supports of $`v/u`$, and $`u_b=h b_v+nB\ge0`$. The simultaneous boundary $`u_b=0`$ is allowed; $`u_a=h a_v>0`$. Put

```math
H=1-h,\quad \mu=1/a_v,\quad
r_1=b_v/B,\quad r_2=(a_v+b_v)/B,
\quad p=\frac{\lambda_v}{\lambda_q}.
```

As $`x`$ increases from zero to one, $`p`$ strictly increases through $`(-\infty,r_1)`$. The exact source metric is

```math
\Pi=dp/d\log q=-\mu(p-r_1)(p-r_2)<0.
```

Define the source polynomials

```math
C=p(p+1)-\Pi,
```

```math
D=HC-Hh p^2-2Hnp+n(n-1),\qquad Q=D/C,
\quad V=uQ.
```

Retain the following closed signed cell: $`C`$ has two simple physical roots $`\gamma_1<\gamma_2`$, and $`D`$ has two simple roots satisfying

**(1)**

```math
\gamma_1\le\delta_1<\delta_2<\gamma_2.
```

Thus $`Q>0`$ on the exterior component $`(-\infty,\gamma_1)`$ and on the central component $`(\delta_1,\delta_2)`$. The physical C roots are negative: for $`0\le p<r_1`$, $`p(p+1)-\Pi>0`$, while (1) places both roots in the physical interval. The parameter inequalities in (1) gives the needed nonpositive-left, positive-right residue signs and the positive central dome. Equality $`\delta_1=\gamma_1`$ permits simultaneous cancellation of the left pole. This inequality must not be removed.

## The separator

For every finite positive exterior critical point $`p_{*}<\gamma_1`$ of $`V`$,

**(2)**

```math
\boxed{\quad V(p)<V(p_{*})\quad
\text{for every }\delta_1<p<\delta_2.\quad}
```

The same original beta weight $`u`$ is retained throughout the comparison.

## Proof by deleting the negative pole

The exact leading-coefficient quotient is

```math
L_0=\frac{H(H+\mu)}{1+\mu}>0.
```

Partial fractions give

```math
Q=L_0+\frac{d_1}{p-\gamma_1}+\frac{d_2}{p-\gamma_2},
\qquad d_1\le0<d_2.
```

Indeed $`D(\gamma_1)\ge0`$ and $`D(\gamma_2)>0`$ under (1), whereas
$`C'(\gamma_1)<0<C'(\gamma_2)`$. Delete the negative residue:

```math
\chi_0=L_0+\frac{d_2}{p-\gamma_2}.
```

Its unique zero $`\eta_0=\gamma_2-d_2/L_0`$ lies in $`\delta_2\le\eta_0<\gamma_2`$, and hence after every strictly positive central point. Indeed $`Q\le\chi_0`$ on the central component, so $`\chi_0>0`$ there. At $`\delta_2`$, $`Q=0`$ and the deleted term is nonpositive, so $`\chi_0(\delta_2)\ge0`$. The equality case is exactly $`d_1=0`$, in which $`\eta_0=\delta_2`$.

Set

```math
s=\eta_0-p>0,\quad b=\gamma_2-\eta_0>0,
\quad a=-n/h-\eta_0,
```

```math
R_i=r_i-\eta_0,\qquad K=h/\mu>0.
```

The nonnegative support of $`u`$ at the right endpoint gives
$`-n/h\le r_1<r_2`$. Since $`\gamma_2<0<-n/h`$,

```math
0<b<a\le R_1<R_2.
```

The exact deleted quotient and source weight derivative are

```math
\chi_0=L_0\frac{s}{s+b},\qquad
\frac{u_p}{u}=K\frac{s+a}{(s+R_1)(s+R_2)}>0.
```

Consequently

```math
\frac{(u\chi_0)_p}{u\chi_0}
=\frac{s+a}{(s+R_1)(s+R_2)}\{K-\mathcal R(s)\},
```

**(3)**

```math
\mathcal R(s)=\frac{b(s+R_1)(s+R_2)}{(s+a)s(s+b)}
=\frac bs
 \left(1+\frac{R_1-a}{s+a}\right)
 \left(1+\frac{R_2-b}{s+b}\right).
```

Each positive factor on the right is nonincreasing in $`s>0`$, and the factor $`b/s`$ strictly decreases. Thus $`\mathcal R`$ strictly decreases in $`s`$, and hence strictly increases in $`p`$.

On the exterior component write $`Q=\chi_0+A`$, where

```math
A=d_1/(p-\gamma_1)\ge0,\qquad A_p\ge0.
```

At an original exterior critical point $`p_{*}`$,

```math
(u\chi_0)_p=-(uA)_p\le0,
```

because $`u_p>0`$. Equation (3) gives $`\mathcal R(s_{*})\ge K`$. Its strict monotonicity gives $`\mathcal R>K`$ at every later point before $`\eta_0`$. Thus $`u\chi_0`$ strictly decreases from $`p_{*}`$ through every positive central point, without a pole. There $`Q\le\chi_0`$, whereas at $`p_{*}`$, $`Q\ge\chi_0`$. Therefore

```math
u(p)Q(p)\le u(p)\chi_0(p)
<u(p_{*})\chi_0(p_{*})\le u(p_{*})Q(p_{*}),
```

which proves (2).

## Use and limits

This removes the beta-weight obstacle to rational central/exterior height separation in this exact boundary metric. It can serve as an endpoint lemma in a deformation proof, provided that the deformation preserves the original signed cell, source weight and relevant critical heights. That preservation is a separate global obligation.
