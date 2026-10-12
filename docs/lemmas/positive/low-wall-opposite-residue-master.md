# A low-wall master from opposite residues

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Research theorem, 4 October 2026. The printed scope is strictly positive outer **antichain** supports. No statement for comparable outer supports is inferred from the forcing budget used below.

## 1. Exact scope

Let $`s_1=(a_1,b_1)`$, $`s_3=(a_3,b_3)`$ satisfy
$`0\lt a_1\lt a_3`$, $`0\lt b_3\lt b_1`$, and put

```math
s_2=P s_1+Q s_3,\qquad P,Q\gt1.
```

Suppose that both origin-quadratic wall curvature ratios are at most one. Then the following sources have, uniformly in all $`E_1,E_2,E_3,L\gt0`$, at most **eight original zeros in $`(0,1)`$, counting multiplicity**:

1. Every source with $`P=Q`$, with arbitrary unequal outer total degrees. There is no affine-contrast sign or size condition.
2. A source with $`P\ne Q`$ whose total degrees $`d_i=a_i+b_i`$ obey
   $`(Q-P)(d_3-d_1)\le0`$.
3. More generally, the explicit quantitative opposite-residue inequality in Section 4 below.

Source seam-edge tangencies are included. Multiple forcing, curvature and original zeros retain their full weights. The theorem does not assert the unrestricted unequal-weight low-wall chamber or either remaining upper-fork wall sector.

## 2. Normalized radial seam

Write

```math
N=P+Q,\quad K=N-1,\quad \mu=Q/N,\quad
\delta=\sqrt{PQ/(N^2K)},\quad A=NK,
```

and $`\gamma=a_3b_1-a_1b_3\gt0`$. Use the normal-ratio binary mean
$`t=r/(1+r)`$, $`y=t-\mu`$, and normalized actual middle probability
$`u=\pi/(1+K\pi)`$, where $`\pi=p_2`$. The two quadratic walls are
$`y=\pm\delta`$, and the physical direction interval is
$`-\mu\lt y\lt1-\mu`$.

The general unequal-weight seam identity is

**(1)**

```math
u_0(y)=\frac{n(y)}{A(y^2-\delta^2)}
=a+by+\frac{D+Ey}{A(y^2-\delta^2)},
```

where

```math
n(y)=\frac{[d_1+(d_3-d_1)t][a_1+(a_3-a_1)t]
[b_1+(b_3-b_1)t]}{\gamma^2}-t(1-t)
=n_0+n_1y+n_2y^2+n_3y^3,
```

```math
a=n_2/A,\quad b=n_3/A,\quad
D=n_0+(PQ/N)a,\quad E=n_1+(PQ/N)b.
```

Both wall ratios strictly below one are equivalent to
$`D\gt|E|\delta`$. In this strict case define positive residues

```math
U=\frac{D+E\delta}{2A\delta}\gt0,\qquad
V=\frac{D-E\delta}{2A\delta}\gt0.
```

Then the remainder in (1) has the especially useful form

**(2)**

```math
R(y)=\frac{U}{y-\delta}-\frac{V}{y+\delta}.
```

For every central $`c\in(-\delta,\delta)`$ and right-outer
$`g\gt\delta`$,

**(3)**

```math
\frac{R(g)-R(c)}{g-c}
=\frac{U}{(g-\delta)(\delta-c)}
 +\frac{V}{(g+\delta)(\delta+c)}\gt0.
```

The reflected formula gives the same strict remainder order between any left-outer point and any central point. No positivity of $`D+Eg`$ at an outer point or at the end of the physical interval is needed. The two signed pole contributions in (2) each supply a strictly positive difference.

## 3. The slope-free equal-weight theorem and the degree-sign theorem

The uniform wall-middle-probability-order lemma states that, on one fixed finite entropy curve, every central $`u`$ is larger than every point on the right outer tail if $`Q\gt P`$, and larger than every point on the left outer tail if $`P\gt Q`$. For $`P=Q`$, this strict comparison holds with either outer tail. It is uniform in the common entropy constant.

When $`P=Q`$, choose the right tail if $`b\ge0`$, and the left tail if $`b\le0`$; either choice is valid when $`b=0`$. The affine quotient in (1) is no smaller at this chosen outer point than at any central point. Together with the strict remainder difference (3), the source seam therefore imposes

**(4)**

```math
u_0(g)\gt u_0(c).
```

The actual common entropy curve imposes the opposite order. It cannot meet both the central seam component and the chosen outer seam component. This proves the required empty-component inequality with **no condition on the degree difference, remainder slope or contrast size**.

For unequal $`P,Q`$, put $`\varepsilon=\mathop{\mathrm{sgn}}\nolimits (Q-P)`$, and choose the smaller-wall-probability tail $`\varepsilon y\gt\delta`$. After reflecting if necessary, the affine quotient has slope $`\varepsilon b`$. Hence (4) follows whenever $`\varepsilon b\ge0`$. The source metric gives

```math
\gamma^2NKb=(d_3-d_1)(a_3-a_1)(b_3-b_1),
```

so this is exactly the degree-sign inequality in Section 1. This removes the old regional theorem's additional end-remainder inequality, even when that remainder is negative at the chosen physical endpoint.

## 4. A stronger quantitative inequality allowing the wrong degree sign

For unequal weights let

```math
e=\begin{cases}1-\mu,&Q\gt P,\\ \mu,&P\gt Q,\end{cases}
\qquad \widehat E=\varepsilon E,\qquad \widehat b=\varepsilon b.
```

The physical chosen-tail coordinate $`g=\varepsilon y`$ lies in
$`(\delta,e)`$. Define

**(5)**

```math
\eta=\frac{1}{4A\delta^2}
\left(
\sqrt{\frac{D+\widehat E\delta}{e-\delta}}
+\sqrt{\frac{D-\widehat E\delta}{e+\delta}}
\right)^2\gt0.
```

The quantitative sufficient inequality is

**(6)**

```math
\boxed{\widehat b+\eta\ge0.}
```

To prove it, each summand in (3) decreases strictly with $`g`$, so its sum is strictly larger for an interior $`g\lt e`$ than its value at $`e`$. At that endpoint put
$`x=\delta-c`$, $`z=\delta+c`$, $`x+z=2\delta`$. The exact Cauchy identity

```math
\frac{\alpha}{x}+\frac{\beta}{z}
-\frac{(\sqrt\alpha+\sqrt\beta)^2}{x+z}
=\frac{(\sqrt\alpha\,z-\sqrt\beta\,x)^2}{(x+z)xz}\ge0
```

with $`\alpha=U/(e-\delta)`$, $`\beta=V/(e+\delta)`$ gives the lower bound $`\eta`$ in (5). Thus

```math
\frac{u_0(g)-u_0(c)}{g-c}\gt\widehat b+\eta\ge0.
```

This again contradicts the actual common-entropy probability order. Equality in (6) is safe because the physical endpoint is excluded. Formula (5) is the exact infimum of the remainder's chord slope on the whole central/chosen-tail rectangle; it is attained only at the excluded outer endpoint and the unique Cauchy equality central point. The inequality is sufficient, and is not asserted to be necessary for the root bound or exhaustive for canonical source geometry.

## 5. Weighted root budget and unit walls

In the strict-low antichain strong fork, the radial-cubic reduction and the double-edge forcing contribution to the root count give at most three seam components, global physical forcing weight at most five, and

```math
N_{\rm cur}\le5+k-2e_0-M.
```

The actual curvature difference is positive at both extreme normal endpoints, so $`N_{\rm cur}`$ is even. Noncanonical endpoint geometry already gives $`N_{\rm cur}\le6`$. The only remaining geometry has three components with endpoint signs $`(--,++,--)`$; its unique plus-plus component is central, and the two minus-minus components lie in the two outer tails. The comparison proved above makes at least one central/chosen-outer component empty, so $`e_0\ge1`$, and $`N_{\rm cur}\le5+3-2=6`$. The two weighted normal-boundary Rolle steps give at most eight original weights.

If one or both wall ratios equal one, the compensated unit-wall theorem directly gives the same original weighted-eight bound. Consequently the equal-weight and degree-sign theorems in Section 1 include both ratios at most one. The quantitative inequality (5) is printed only for strict-low walls; it involves strictly positive residues. Unit-wall cases have no need for that formula.
