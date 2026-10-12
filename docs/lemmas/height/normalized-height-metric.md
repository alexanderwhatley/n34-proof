# Metric monotonicity of the enhanced height criterion

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Fix a positive stationary contact chart and use the dimensionless variables

```math
\eta=U(y-x)/\rho,\quad r=R/U,\quad q=Q/U,\quad
 a=\rho S_r/U^2,\quad b=\rho S_q/U^2,\quad c=\rho S_u/U^2,
 \quad\kappa=x/U,\quad\ell=(1-x)/U.
```

The source determines $`w=\ell-\kappa`$. Thus hold $`r,q,a,b,c,w`$ fixed while varying $`\kappa`$, with $`\ell=\kappa+w`$. The corresponding original source changes, but the normalized stationary source jet remains fixed. Strict positive supports require

```math
\kappa>0,\quad\ell>0,\quad a>r\kappa,\quad b>q\ell,
 \quad c>\kappa.
```

The source cubics, normalized by $`U^3`$, are

```math
\begin{aligned}
 D_\eta&=(r-a\eta)(q-r+(a+b)\eta)(q+b\eta)
 -(rb+qa)(1+w\eta-\kappa\ell\eta^2),\\
 C_\eta&=D_\eta\big|_{r\mapsto r+1,\ a\mapsto a+c}.
 \end{aligned}
```

Put $`\Delta_r=rb+qa>0`$,
$`\Delta_v=(r+1)b+q(a+c)>0`$, and $`H=\Delta_r/\Delta_v`$.
At the contact point $`D_0=tC_0`$, with $`t>0`$. At a comparison point define

```math
z=D_\eta/(tC_\eta),\qquad
 F=\frac{\ell(\ell+c)/(1+\eta\ell)+\kappa(c-\kappa)}{\kappa+\ell}.
```

The normalized enhanced margin is exactly

**(1)**

```math
\mathcal P=(1-z)(3-z)-2\eta+\eta^2F.
```

Its nonnegative sign is equivalent to $`P_2\ge0`$ when the denominators are positive.

**Theorem.** Suppose $`\eta>0`$, $`C_\eta,D_\eta>0`$,
$`0<z<1`$, $`D_\eta/C_\eta<H`$, and $`\eta c<1`$.
Then $`\mathcal P`$ strictly decreases as $`\kappa`$ increases with the other normalized chart parameters fixed.

**Proof.** Both cubics depend on the metric only through
$`\kappa\ell`$, with coefficients $`\Delta_v\eta^2`$ and
$`\Delta_r\eta^2`$. Therefore

**(2)**

```math
\frac{\partial z}{\partial\kappa}
 =\frac{\eta^2(\kappa+\ell)
      (\Delta_r C_\eta-\Delta_vD_\eta)}{tC_\eta^2}>0.
```

Also

```math
\frac{\partial F}{\partial\kappa}
 =\frac{\eta\ell N}{(\kappa+\ell)^2(1+\eta\ell)^2},
```

```math
N=c\eta\ell(\ell-\kappa)-2c\kappa
       -2\eta\kappa\ell^2-\ell(3\kappa+\ell).
```

If $`\ell<\kappa`$, every summand in $`N`$ is negative.
If $`\ell\ge\kappa`$, use $`c\eta<1`$ to obtain

```math
N\le-2\kappa(c+\eta\ell^2+2\ell)<0.
```

Hence $`F_\kappa<0`$. Differentiating (1) gives

```math
\mathcal P_\kappa=-(4-2z)z_\kappa+\eta^2F_\kappa<0.
```

This proves the theorem.

In the signed comparable source, $`D/C<H`$ at every positive central point: projectively, $`C<0`$, $`E>0`$, and $`D=HC+E`$, so $`D/C=H+E/C<H`$. The cubic component separator gives $`z<1`$. The condition $`\eta c<1`$ is precisely $`\lambda_u(y)>0`$, proved from the source central gates. Thus all hypotheses hold inside the actual cell.

This suggests checking only the maximal permitted metric. However, the actual cubic root order may cease before a support exponent reaches zero. A proof must include that root-cell boundary; it cannot replace the permitted metric range by the larger support-only interval. Core support and contact gates alone already admit exact shifted-D counterexamples in a different root order.
