# Paired beta branch quotient theorem

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

This is a coordinate-free form of the proved positive-kernel theorem. It supplies a common height comparison for an entire family of first-order deflations. It is not a proof of the remaining seven-node contact exclusion.

Let

```math
q=x^A(1-x)^B,\qquad A,B\gt0,
```

and let two beta monomials

```math
\beta_j=x^{a_j}(1-x)^{b_j}\qquad(j=1,2)
```

satisfy

```math
0\lt a_1\lt a_2,\qquad 0\lt b_1\lt b_2,
\qquad
0\lt a_1B-b_1A\lt a_2B-b_2A.
```

For each $`0\lt q_0\lt q_{\max}`$, let $`x_L\lt x_R`$ be the two original points where $`q=q_0`$, and set

```math
\mathcal B_j(q_0)=\frac1{\beta_j(x_L)}-\frac1{\beta_j(x_R)}\gt0,
\qquad s=\log q_0.
```

For every $`\tau\ge0`$, the first-order quotient

```math
\mathcal R_\tau(q_0)
=\frac{\tau\mathcal B_1-(\mathcal B_1)_s}
       {\tau\mathcal B_2-(\mathcal B_2)_s}
```

is positive and strictly increasing. Its quantitative derivative margin is

```math
\frac{d\log\mathcal R_\tau}{d\log q_0}
\gt\frac{b_2-b_1}{B}\gt0.
```

The limits are

```math
\lim_{q_0\downarrow0}\mathcal R_\tau=0,
```

```math
\lim_{q_0\uparrow q_{\max}}\mathcal R_\tau
=\frac{a_1B-b_1A}{a_2B-b_2A}
  \frac{\beta_2(A/(A+B))}{\beta_1(A/(A+B))}.
```

The undeformed quotient $`\mathcal B_1/\mathcal B_2`$ has the same limits and the same strict logarithmic derivative margin. Moreover $`\mathcal R_\tau`$ strictly increases with $`\tau`$ toward this undeformed quotient. Consequently one common positive level has at most one intersection with each quotient, and these intersections are ordered as the deflation parameter varies.

## Proof from one kernel

Put

```math
\alpha_j=b_j/B,\qquad \kappa_j=(a_jB-b_jA)/B.
```

Then $`0\lt\alpha_1\lt\alpha_2`$, $`0\lt\kappa_1\lt\kappa_2`$, and at the equal-height points

```math
\log\beta_j=\alpha_js+\kappa_j\log x.
```

With $`t=\log x`$, the exact jump representation is

```math
\mathcal B_j=e^{-\alpha_js}\kappa_jJ_{\kappa_j},
```

where $`J_\kappa=\int_{t_L}^{t_R}e^{-\kappa t}\,dt`$. Therefore

```math
\mathcal R_\tau
=\frac{\kappa_1}{\kappa_2}
 e^{(\alpha_2-\alpha_1)s}
 \frac{P_{\kappa_1,\tau+\alpha_1}}
      {P_{\kappa_2,\tau+\alpha_2}}.
```

Both parameters are smaller in the numerator. The mixed-kernel theorem in [ordered physical branch contact heights](ordered-physical-branch-contact-heights.md) proves that the kernel ratio strictly increases. This gives the derivative margin and positivity. Its endpoint proof gives the two stated limits. The undeformed ratio uses the same argument with the interval hazard increasing in $`\kappa`$.

Finally the first-order quotient is a positive weighted mean of the undeformed quotient and its $`\tau=0`$ version, exactly as in the general first-order corollary; its derivative in $`\tau`$ is strictly positive.

For the original comparable row, take $`\beta_1=v/u`$ and $`\beta_2=v`$. Then $`\kappa_1/\kappa_2=1-h`$, and this one theorem gives the three original functions $`\mathcal I,\mathcal J,\mathcal K`$, together with every nonnegative first-order deflation. The theorem requires the displayed determinant order; it makes no claim for arbitrary ordered beta supports without that additional condition.
