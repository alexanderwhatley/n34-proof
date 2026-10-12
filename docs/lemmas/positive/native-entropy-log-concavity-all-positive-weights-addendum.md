# Native entropy log concavity for all positive weights with positive K

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

This extends only the actual-curve part of the native projective log-curvature lemma. No source root budget, chamber master, or height-order conclusion is inferred.

Let $`P,Q>0`$, $`K=P+Q-1>0`$, and $`r>0`$. In the physical chart put

```math
0<u<\min(1/P,r/Q),\quad A=1-Pu>0,\quad B=r-Qu>0,\quad S=1+r-Ku=A+B+u>0.
```

Define

```math
J=\frac{P\log A+Q\log B-\log u-K\log S}{K},\quad
H=P(P-1)r^2-2PQr+Q(Q-1),\quad M=r(1+r)+Hu.
```

Then for every finite $`C`$, the equation $`J=C`$ defines one real analytic physical graph $`u_C(r)`$ on all $`r>0`$. Its elasticity $`\eta_C=ru_C'/u_C`$ strictly decreases:

```math
\boxed{\eta_C'=-\frac{(1-Pu_C)(r-Qu_C)\{u_C[H+Kr]^2+Kr^2S\}}{M^3}<0.}
```

Equivalently $`\log u_C(e^x)`$ is strictly concave for all real $`x`$. In particular this includes every one-positive-wall family $`P>1`$, $`0<Q<1`$, and its reflection.

## Physical positivity and global graph

The polynomial $`M`$ is affine in $`u`$, is positive at zero, and is nonnegative at the active physical bound. If $`r\ge Q/P`$, the active bound is $`1/P`$, and

```math
M(r,1/P)=\frac{(Pr-Q)(Pr-Q+1)}P\ge0.
```

If $`r\le Q/P`$, the active bound is $`r/Q`$, and

```math
M(r,r/Q)=\frac rQ(Q-Pr)[Q-(P-1)r]\ge0.
```

Here $`Q-Pr\ge0`$. For $`P\ge1`$, the remaining bracket is at least $`Q/P>0`$; for $`P\le1`$, it is at least $`Q>0`$. Thus affine interpolation gives $`M>0`$ strictly before the bound, also when the bound endpoint has value zero.

The same universal identities as in the proof give

```math
J_u=-\frac{M}{KuABS}<0,\qquad J_r=\frac{Q-(P-1)r}{KBS}.
```

At fixed $`r`$, $`J`$ tends from $`+\infty`$ to $`-\infty`$ as $`u`$ ranges from zero to its physical bound; at the coincident bound $`r=Q/P`$, both positive-weight logarithms tend to $`-\infty`$ while $`S`$ remains positive. Existence, uniqueness, and real analyticity of every level graph follow. Implicit differentiation yields

```math
u_C'=\frac{u_C(1-Pu_C)[Q-(P-1)r]}M.
```

Differentiating $`ru_C'/u_C`$ gives the displayed square decomposition. Every factor in its numerator is strictly positive except the squared factor, which is merely nonnegative; the additional term $`Kr^2S`$ is strictly positive. Consequently the decrease is strict. This proof uses only $`P,Q,K>0`$, not $`P-1,Q-1>0`$.
