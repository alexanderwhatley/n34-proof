# Unit-wall closure of the high-high strong-fork six-contact master

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Statement

Retain the strictly positive outer supports with distinct modes, positive orientation $`\gamma\gt0`$, and $`s_2=P s_1+Q s_3`$, $`P,Q\gt1`$, from the strict high-high master. Define $`H,R,B,Y`$ and its walls $`0\lt\eta\lt\xi`$ exactly as there. The strict inequalities can be closed:

```math
\boxed{Y(\eta)\le0,\qquad Y(\xi)\le0.}
```

Equivalently, both origin-wall ratios are at least one. For every positive coefficient tuple and positive level, the original beta-level difference has at most **six zeros counting multiplicity**. The sharpness example already belongs to the strict region.

No genericity, source-edge regularity, or simplicity assumption is added. This is a direct multiplicity argument at the unit walls. It does not infer the weighted result by perturbing multiple real roots. Mixed and low-low wall regions remain outside this statement.

## The wall factors and endpoint transversality

Let $`u_C`$ be the actual common-entropy graph. Normal-curvature contacts are zeros of

```math
A(r)=B(r)+H(r)u_C(r)-R(r).
```

The gauge relating $`A`$ to the actual normal-curvature difference is analytic and nonvanishing, including at the walls: both $`B+Hu_C`$ and $`x(1-x)`$ are strictly positive. Thus analytic root weights are preserved.

If $`Y(\eta)=0`$, the source seam $`u_0=Y/H`$ has a removable singularity at $`\eta`$, with

```math
u_0(\eta)=\frac{Y'(\eta)}{H'(\eta)},\qquad
u_0'(\eta)=
\frac{Y''(\eta)H'(\eta)-Y'(\eta)H''(\eta)}
{2H'(\eta)^2}.
```

Put $`D=u_C-u_0`$, analytic through the unit wall. Then

```math
A=H D.
```

The independently source-bound endpoint-transversality corollary of the unit-left-wall comparison proves

```math
u_0'(\eta)-F(\eta,u_0(\eta))\lt0
```

for every genuine positive source cubic with $`Y(\eta)=0`$ and $`Y(\xi)\le0`$. The companion proof extends the six-vertex comparison to $`r=\eta`$, after cancelling the common vanishing factors; all five strict vertex gaps remain strictly negative, whereas the sole equality vertex $`R=B`$ is excluded by the genuine positive cubic.

Consequently, if $`D(\eta)=0`$, then $`D'(\eta)\gt0`$. Thus the residual wall root is simple, and the full curvature wall weight is exactly two. If $`D(\eta)\ne0`$, the mandatory factor $`H`$ gives curvature weight exactly one. Reflection gives $`D'(\xi)\lt0`$ at any matching right unit wall. The full unit-wall weights are therefore always one or two, never higher.

## One unit wall and one strictly high wall

Assume $`Y(\eta)=0`$ and $`Y(\xi)\lt0`$; the reflected case is identical. The unit comparison gives $`u_0'-F(r,u_0)\lt0`$ throughout $`0\lt r\lt\eta`$, including formal nonphysical source values. At every actual residual root $`D(r)=0`$, the source value is physical and

```math
D'(r)=F(r,u_0)-u_0'\gt0.
```

Hence all residual roots on the left are simple upward crossings. Since $`D(0+)=-u_0(0)\lt0`$, there is at most one such root; it exists exactly when $`D(\eta)\gt0`$. If $`D(\eta)=0`$, the endpoint-transversality sign gives $`D\lt0`$ just before the wall, so there is no left interior root.

The right exterior still has exactly one simple curvature contact. Indeed the remaining source residue is negative:

```math
u_0(r)=\ell(r)-\frac{B_+}{r-\xi},\qquad B_+\gt0.
```

Therefore $`u_0''\lt0`$ for $`r\gt\xi`$, opposite the actual graph's strict convexity, and the usual exterior endpoint phases give one.

Centrally, $`u_0''\gt0`$ for $`\eta\lt r\lt\xi`$, while $`u_C''\lt0`$. Thus $`D`$ is strictly concave, and $`D\to-\infty`$ at $`\xi-`$. The three possible left-wall phases have the following exact budgets:

| Residual phase at $`\eta`$ | Left interior | Unit wall | Central interior | Right exterior | Total curvature weight |
|---|---:|---:|---:|---:|---:|
| $`D(\eta)\gt0`$ | 1 | 1 | 1 | 1 | 4 |
| $`D(\eta)=0`$, $`D'(\eta)\gt0`$ | 0 | 2 | 1 | 1 | 4 |
| $`D(\eta)\lt0`$ | 0 | 1 | At most 2 | 1 | At most 4 |

For the middle row, strict transversality makes $`D\gt0`$ immediately inside the central interval, so strict concavity and the negative right endpoint give one simple interior crossing. This accounts for both weights of a coincident unit-wall contact rather than losing one through division by $`H`$.

## Both unit walls

If $`Y(\eta)=Y(\xi)=0`$, then $`Y=H u_0`$ with $`u_0=m r+n`$, where

```math
m=R_3/[P(P-1)]\gt0,\qquad n=R_0/[Q(Q-1)]\gt0.
```

Each wall is an automatic curvature root. The residual difference $`D=u_C-u_0`$ is strictly convex on the two exterior intervals and strictly concave centrally. It tends to negative values at both extreme normal directions.

As above, a left exterior residual root exists exactly when $`D(\eta)\gt0`$, and a right exterior one exactly when $`D(\xi)\gt0`$; each is simple. A zero wall value is a simple residual root, with the inward signs $`D'(\eta)\gt0`$ and $`D'(\xi)\lt0`$.

To count the remaining residual roots, treat each positive wall value as positive on the central side, and each zero wall value as positive immediately inside by transversality. If both central-side values are positive, strict concavity gives no central interior root. If exactly one is positive and the other wall value is negative, it gives one simple central root. If both wall values are negative, it gives at most two central weights. Replacing a positive wall value by zero trades its one exterior root for one residual wall root. Thus in every sign combination the full residual root weight, including matching wall roots, is at most two.

The two simple factors of $`H`$ contribute two additional mandatory weights. Therefore $`Z(A)\le2+2=4`$, including all unit-wall coincidences.

## Original level roots and exact examples

The two weighted normal-boundary Rolle steps transfer the curvature ceiling four to the original ceiling six. The strict high-high theorem covers the remaining case where neither wall is unit, so all weak inequalities in the statement are covered.

A rational one-unit, other-high source is

```math
P=2,\ Q=8,\quad
s_1=(352/5,1056/5),\quad s_3=(176/25,176/25).
```

Its middle support is $`(4928/25,11968/25)`$ and

```math
R(r)=\frac{(r+10)(r+20)(r+30)}{1408},\qquad
H=2(r-2)(r-14).
```

Here $`R(2)=6`$, $`R(14)=561/22\lt210`$. The removable source middle coordinate at the unit wall is $`u_0(2)=237/1408`$, strictly inside the probability bound $`1/4`$. The exact strict forcing-gap sign at that point permits a finite common entropy constant matching the wall and realizes the local order-two curvature mechanism.

A rational two-unit source is

```math
P=Q=2,\quad
s_1=(97/441,776/441),\quad s_3=(776/441,97/441).
```

Its source metric is

```math
R=(8+73r+73r^2+8r^3)/97,\qquad
Y=H\,[4(1+r)/97].
```

Thus both unit walls and the affine residual seam are exact. These examples check the new boundary scopes; no original-root sharpness claim is attached to them.
