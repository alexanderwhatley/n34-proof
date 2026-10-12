# Only the physical derivative-core signs are needed

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Retain the strict positive comparable source with

```math
u=v^h q^{-m},\quad 0<h<1,\quad m>0,\quad q=w/v,
\quad \Delta=\det(v,q)>0.
```

Its modes obey $`x_q<x_w<x_v<x_u`$. Put
$`\rho=x(1-x)`$, $`L_f=a_f-(a_f+b_f)x`$, and define the
actual derivative cores

```math
P_v=(L_v-L_u)L_vL_u+\rho(L_v'L_u-L_vL_u'),
```

```math
P_w=(L_w-L_u)L_wL_u+\rho(L_w'L_u-L_wL_u').
```

Let $`W_{\rm raw}`$ be the actual raw degree-six numerator in
$`W(u',v',w')=uvwW_{\rm raw}/\rho^6`$, using the original column
order u,v,w. Assume

**(1)**

```math
W_{\rm raw}>0\quad\text{on }[x_v,x_u].
```

The original ten-root saturation provides the stronger condition that
all six simple raw roots lie before $`x_v`$, with positive eventual
sign after $`x_v`$. Specifically,

```math
W_{\rm raw}(0)=a_ua_va_w(a_v-a_u)(a_w-a_u)(a_w-a_v)>0.
```

Six simple roots before $`x_v`$ exhaust the degree and give an even
number of sign reversals; hence $`W_{\rm raw}>0`$ after $`x_v`$.
Condition (1) is all that is used here.

**Lemma.** There is exactly one simple P_v zero $`\alpha`$ in
$`(0,x_v)`$, and

**(2)**

```math
P_v>0\text{ on }(0,\alpha),\qquad
P_v<0\text{ on }(\alpha,1).
```

No claim about the number of real P_v roots outside $`(0,1)`$ is
required. Equivalently the projective Qv core has one sign transition
on the glued physical rays, with the sign reversed on the right ray.

## Proof before the v mode

The derivative ratio $`S_v=v'/u'`$ is positive on $`(0,x_v)`$,
vanishes at both ends, and is strictly log concave there. Indeed

```math
(\log S_v)''
=-\frac{a_v-a_u}{x^2}-\frac{b_v-b_u}{(1-x)^2}
-\frac1{(x_v-x)^2}+\frac1{(x_u-x)^2}<0.
```

Its logarithmic derivative goes from positive infinity to negative
infinity, so it has one nondegenerate maximum $`\alpha`$.
Direct differentiation is

```math
S_v'=\frac vu\frac{P_v}{\rho L_u^2},
```

giving the first part of (2).

## No additional core zero between v and u

On $`(x_v,x_u)`$, $`S_v<0`$, and

```math
\frac{S_w}{S_v}=\frac{w'}{v'}
=q\frac{a_w+b_w}{a_v+b_v}\frac{x-x_w}{x-x_v}>0
```

is strictly decreasing. Both q and the displayed positive linear
ratio strictly decrease there. At a P_v zero, $`S_v'=0`$, hence
$`S_w'=S_v(S_w/S_v)'>0`$, and therefore P_w>0.

The exact raw source identity is

```math
L_u W_{\rm raw}
=\rho(P_vP_w'-P_wP_v')+L_qP_vP_w.
```

At a P_v zero, condition (1) and $`\rho,L_u,P_w>0`$ force
$`P_v'<0`$. Multiple zeros would make $`W_{\rm raw}=0`$ and are
impossible. But

```math
P_v(x_v)=\rho L_v'L_u<0,\qquad
P_v(x_u)=-\rho L_vL_u'<0.
```

A continuous polynomial negative at both endpoints cannot have only
strict downward zeros in between. Thus no such zero exists.

## The remaining physical tail

Let $`f=v/u`$, $`s_f=a_f+b_f`$, $`s_v=a_v+b_v`$,
$`s_u=a_u+b_u`$, and $`d=a_ub_v-b_ua_v>0`$. Exact beta-jet
algebra gives

```math
P_v=s_fs_vs_u(x_f-x)(x_v-x)(x_u-x)-d\rho.
```

Since $`x_f<x_v<x_u`$, this is strictly negative on
$`(x_u,1)`$. This completes (2).

## Source and integration scope

In the actual projective chart,

```math
P_v=L_q^3 Q_v,\qquad Q_v=mC-pE=-A.
```

Thus (2) controls Qv everywhere the height argument uses it, without
requiring a nonreal pair for the cubic. In particular, whenever
Qv is positive at a physical point before v, that point is after alpha
on the right branch and before alpha on the left branch. This is enough
for the central, interlacing and signed crossing routing.

The proof reuses the original physical exclusion in s130, section 3,
but omits its beyond-x=1 exclusion, global discriminant theorem and
associated positive lower-scale barriers. It retains the original
actual-row raw saturation supplying (1); this premise is not derived
from arbitrary seven common-height nodes or coefficient signs alone.
