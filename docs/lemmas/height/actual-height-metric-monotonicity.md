# Exact height increases with the normalized source metric

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Keep the normalized stationary contact chart from [metric monotonicity for enhanced height](normalized-height-metric.md). Hold $`r,q,a,b,c,w=\ell-\kappa,t`$ fixed, and let $`\ell=\kappa+w`$. The comparison displacement is fixed as $`\eta=U(y-x)/\rho>0`$. At each metric value, the original coordinates and supports are

```math
U=(\kappa+\ell)^{-1},\quad x=U\kappa,
 \quad y=x+\eta U\kappa\ell,
```

```math
a_u=U(1+c/\ell),\qquad b_u=U(c/\kappa-1).
```

The source cubics satisfy $`D_0/C_0=t>0`$, independently of the metric. Let

```math
\mathcal H(\kappa)=\log\frac{u(y)D_\eta/C_\eta}{u(x)t}.
```

**Theorem.** Suppose $`\kappa,\ell>0`$, $`\eta c<1`$, $`0<\kappa<c`$, $`C_\eta,D_\eta>0`$, and $`D_\eta/C_\eta<H=\Delta_r/\Delta_v`$. Then $`\mathcal H`$ strictly increases as $`\kappa`$ increases with the normalized chart fixed, as long as these inequalities remain valid.

**Proof.** The exact beta growth satisfies

```math
\frac{\partial}{\partial\eta}\log\frac{u(y)}{u(x)}
 =\frac{1-c\eta}{(1+\ell\eta)(1-\kappa\eta)}.
```

Since $`\eta c<1`$ and $`\kappa<c`$, both denominator factors are positive. Integrating from zero gives

```math
\log\frac{u(y)}{u(x)}
 =\int_0^\eta\frac{1-cs}{1+ws-\kappa\ell s^2}\,ds.
```

For every $`0<s\le\eta`$, the numerator is positive and the denominator strictly decreases with $`\kappa`$, because

```math
\frac{\partial}{\partial\kappa}
 (1+ws-\kappa\ell s^2)=-(\kappa+\ell)s^2<0.
```

Thus the beta growth strictly increases. The rational factor also strictly increases:

```math
\frac{\partial}{\partial\kappa}\frac{D_\eta}{C_\eta}
 =\frac{\eta^2(\kappa+\ell)
      (\Delta_rC_\eta-\Delta_vD_\eta)}{C_\eta^2}>0.
```

The contact value $`t`$ is fixed. This proves strict increase of the full height ratio.

At a positive central point of the actual signed source, $`D/C<H`$ follows from $`D=HC+E`$ with projective $`C<0<E`$, and $`\eta c<1`$ is precisely the positive u slope at the comparison point. These are imported parameter inequalities, not conclusions of arbitrary cubic coefficient signs.

A prospective proof can therefore compare the actual height with a larger metric. The physical root cell can end at a C,D common-root face, and a support exponent can reach zero first. Both possibilities must be retained.
This exact-height monotonicity is stronger for that reduction than monotonicity of the sufficient polynomial $`P_2`$: it compares the actual beta-rational height directly.

The deformed source is concrete. Its support sums are S_u=c/(kappa ell), S_r=a/(kappa ell), and S_q=b/(kappa ell), with

```math
(a_u,b_u)=U(1+c/\ell,\ c/\kappa-1),
```

```math
(a_r,b_r)=U(r+a/\ell,\ a/\kappa-r),\qquad
 (a_q,b_q)=U(-q+b/\ell,\ b/\kappa+q).
```

It passes nineteen identities. No independently chosen cubics are substituted into the deformation.
