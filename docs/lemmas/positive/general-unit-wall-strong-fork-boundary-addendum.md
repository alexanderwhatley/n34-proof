# Positive strong forks with a unit wall

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

This separate addendum clarifies the unit-wall boundary scope of the mixed quadratic-metric corollary. It does not change that corollary's strict-mixed statement or any earlier file.

Let the two outer supports $`s_1,s_3`$ have strictly positive coordinates and distinct modes, and let

```math
s_2=P s_1+Q s_3,\qquad P,Q\gt1.
```

The normal-curvature reduction and wall identities are the only imported results. Here is the complete additional argument.

Write $`I=(\theta_1,\theta_3)`$, ordering the distinct outer modes, $`w=x(1-x)`$, and

**(1)**

```math
d=\rho-1/w,\qquad
d'=A d+\frac{T}{V_0w^3},\qquad \deg T\le6.
```

The actual $`d`$ is analytic throughout $`I`$. The strong-fork origin quadratic has exactly two simple internal walls. At a wall $`c`$, put $`\sigma=V_1(c)/w(c)\gt0`$. The identities are

**(2)**

```math
d(c)=\frac{1-\sigma}{\sigma w(c)},\qquad
\mathop{\mathrm{res}}\nolimits _c A=\frac{\sigma(3-\sigma)}2.
```

At a unit wall, $`d(c)=0`$ and $`A=1/(x-c)+A_0`$, where $`A_0`$ is analytic. Write $`d=(x-c)v`$. Then

```math
d'-A d=(x-c)(v'-A_0v).
```

Since $`V_0`$ has a simple zero at $`c`$, equation (1) forces $`T`$ to have a double factor $`(x-c)^2`$. This is valid even when $`d`$ has higher multiplicity at $`c`$.

Let $`h`$ be the product of all unit-wall factors, let their number be $`r\in\{1,2\}`$, and put

```math
d=hv,\qquad T=h^2F,\qquad \deg F\le6-2r.
```

Then

**(3)**

```math
v'=\left(A-\frac{h'}h\right)v+
\frac{hF}{V_0w^3}.
```

The coefficient and multiplier of $`F`$ in (3) are analytic across each unit wall, and that multiplier is nonzero there. Thus those walls do not split the Rolle count.

If exactly one wall is unit, only the other wall $`c_{*}`$ remains as a possible pole. It is not a zero of $`d`$, by (2), so $`v(c_{*})\ne0`$. On each of the two intervals separated by $`c_{*}`$, a positive analytic integrating factor changes (3) into a derivative equal to a nonvanishing multiplier of $`F`$. Ordinary weighted Rolle gives

```math
Z_I(v)\le Z_I(F)+2\le6.
```

Here $`Z`$ denotes the sum of analytic root multiplicities, and zeros at the unit wall are included in $`Z_I(v)`$. Restoring its factored contact gives $`Z_I(d)\le7`$.

```math
Z_I(d)\le6.
```

The two further normal-boundary Rolle steps give at most eight original contacts, including their multiplicities.

If both walls are unit, (3) is regular on the whole connected interval $`I`$, and $`\deg F\le2`$. Global weighted Rolle yields $`Z_I(v)\le3`$, hence $`Z_I(d)\le5`$. The same positive endpoint phases sharpen this to four curvature weights and therefore six original contact weights.

If $`F\equiv0`$, no polynomial-root count is used. With one unit wall, $`v`$ solves a regular homogeneous equation on each interval separated by $`c_{*}`$. Its nonzero analytic value at $`c_{*}`$ excludes the identically zero solution on either interval, so it has no zeros. With both unit walls, the homogeneous equation is regular throughout $`I`$: $`v`$ is identically zero or nowhere zero. The first possibility would make $`d\equiv0`$, contradicting its positive infinite normal-endpoint limits. These cases satisfy the bounds as well.

This proves the unit contribution to the root count for the common-$`a`$ and common-$`b`$ quadratic-metric cases without the older odd-source-parity hypothesis. The result also covers all other strictly positive strong forks with a unit wall, independently of the metric degree. It does not settle strong forks whose two wall ratios are both nonunit.
