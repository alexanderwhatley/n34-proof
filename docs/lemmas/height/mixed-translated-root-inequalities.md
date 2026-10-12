# Exact translated cubic for the mixed monotone-anchor pair

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Let $`a,b,c,\nu\gt0`$, $`c\gt a`$, and
$`h_1=t^a(1-t)^b`$, $`h_2=t^c(1-t)^{-\nu}`$. Put
$`\ell_1=a-(a+b)t`$, $`\ell_2=c-(c-\nu)t`$,
$`p=c-a\gt0`$, $`q=b+\nu\gt0`$, and

```math
R=\ell_1\ell_2[p+(q-p)t]+t(1-t)(bc+a\nu).
```

Every physical root of $`R`$ lies to the right of the $`h_1`$ mode
$`m=a/(a+b)`$: all three terms in the displayed formula are positive
for $`t\le m`$, including the positive second term at $`t=m`$.

For $`t\gt m`$, use the bijective coordinate

```math
z=\frac{t-m}{1-t}\gt0,\qquad t=\frac{m+z}{1+z},
\quad d_0=\frac{bc+a\nu}{a+b}\gt0.
```

Direct substitution gives the exact cubic normal form

**(1)**

```math
\boxed{\frac{(1+z)^3}{b}R(t)=
 d_0m+d_0(1+m-d_0)z+d_0(1-b-2\nu)z^2
 -\nu(b+\nu)z^3.}
```

Consequently a strict generic row has three physical $`R`$-roots only if

**(2)**

```math
\boxed{b+2\nu\lt1,\qquad bc+a\nu\gt2a+b.}
```

Indeed the constant coefficient in (1) is positive and its cubic
coefficient is negative. Three positive roots require three sign changes
by Descartes, forcing negative linear and positive quadratic coefficients.
If either strict inequality fails, the cubic has only one sign change after
zero coefficients are discarded. It has exactly one positive root,
since its physical endpoint signs are opposite.

The three-root inequalities imply several further source restrictions:

```math
\nu\lt\frac12,\quad b\lt1-2\nu\lt1,
\quad c\gt1+\frac{(2-\nu)a}{b}\gt1\gt\nu,
```

**(3)**

```math
p=c-a\gt1+a\left(\frac{2-\nu}{b}-1\right)\gt1,
\qquad q=b+\nu\lt1-\nu\lt1.
```

Thus every three-root mixed row automatically has $`p\gt q`$; a separate
opposite gap orientation is impossible. In the original coordinate its
$`R`$ cubic has negative leading coefficient and all three roots lie
inside $`(0,1)`$. If the actual $`H`$ cubic has two physical roots,
its third root lies to the right of 1, because $`H`$ has positive endpoint
values and negative cubic leading coefficient.

This is a pair-shape theorem. It does not prove a uniform common-auxiliary ratio
height bound in the remaining $`K`$-negative region, and it does not
replace the full old mixed NOLOBE/GENUINE proof.
