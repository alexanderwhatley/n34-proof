# Candidate boundary routing for the signed source metric deformation

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Use the normalized fixed contact chart $`r,q,a,b,c,w,t`$. Let
$`\ell=\kappa+w`$ and increase $`\kappa`$, hence increase
$`P=\kappa\ell`$. The strict source supports remain positive while

```math
\kappa<\kappa_s:=\min(c,b/q-w).
```

Indeed $`b_u>0\iff\kappa<c`$, $`a_q>0\iff\ell<b/q`$,
and the gap support condition $`b_r>0\iff\kappa<a/r`$ is implied
by the rightmost-u mode inequality $`a>rc`$. The other support
exponents stay strictly positive. Both mode-order inequalities are
independent of the metric.

At the starting signed source, the normalized original-x order is

```math
-1/\ell<d_0<c_0<0<c_1<d_1<d_2<c_2<1/\kappa.
```

Here the symbols denote normalized displacements $`U(x_i-x)/\rho`$,
not the original projective p coordinates. Increasing $`P`$ adds
$`\Delta_vP\eta^2`$ and $`\Delta_rP\eta^2`$ to the source cubics.
Their values at zero and negative leading coefficients stay fixed.

## 1. The individual cubic roots cannot disappear

Each old positive dome contains a point where its cubic is positive.
That value strictly increases with the metric. The value at zero
remains negative, and the value at positive infinity remains negative.
Thus each cubic continues to have two distinct positive roots and one
negative root. Degree three makes these the complete root sets, all
simple. The negative root and larger positive root move right; the
smaller positive root moves left, by implicit differentiation of the
lifted cubic.

Before a support boundary, all these roots remain physical. In original
coordinates, both source cubics are positive at x=0 and negative at
x=1 because all support exponents are positive. A root cannot cross
an endpoint while these signs remain strict.

## 2. Only the lower E zero can exchange C,D root order

Let $`H=\Delta_r/\Delta_v`$. The polynomial
$`\mathcal E=D-HC`$ is independent of the metric, and the projective
ratio

```math
p(\eta)=-\frac{1+r-(a+c)\eta}{q+b\eta}
```

is independent of it as well. Its zeros are the fixed seam
$`\eta=-q/b`$, together with the original E quadratic roots
$`\epsilon_-<0<\epsilon_+`$, interpreted by the projective map.

The exterior-critical localization gives H−t>0 and places the starting p coordinate before $`\epsilon_-`$. The signed
ordering $`\epsilon_-<\gamma_1`$ places the corresponding
normalized zero $`e`$ in $`(0,c_1)`$. At that point $`C(e)<0`$.
Increasing the metric first makes $`C(e)=D(e)=0`$ at one finite
metric value $`\kappa_e`$, if the support boundary has not occurred
first. The lifted negative pole cancels there.

No other zero of $`\mathcal E`$ can produce an earlier common root:

- At the seam, the source C equals $`-\Delta_v\rho`$, strictly
  negative while the seam is physical and supports are positive.
- If the $`\epsilon_+`$ point lies on the left physical branch,
  $`\epsilon_+<\gamma_3`$ places it before the starting negative C
  root. C is positive there initially, and its metric lift is positive.
- If it lies on the right physical branch, $`\epsilon_+>m/h`$
  forces $`\lambda_u<0`$, so its normalized displacement exceeds
  $`1/c`$. The v mode is at $`(1+r)/(a+c)<1/c`$, by $`a>rc`$.
  Throughout the physical region after that v mode, the source C is
  strictly negative: $`\lambda_v\le0`$, $`\lambda_q<0`$, and
  $`\lambda_v+\lambda_q<0`$ make its cubic product nonpositive,
  while $`-\Delta_v\rho<0`$.
- If it is nonphysical initially, it stays so, because the normalized
  physical interval $`(-1/\ell,1/\kappa)`$ shrinks as the metric
  increases. A projective pole mapping to infinity also stays
  inaccessible.

Consequently the order can end only at

```math
\kappa_{*} = \min(\kappa_e,\kappa_s),
```

with either cancellation of the negative pole, $`b_u=0`$, or
$`a_q=0`$. Simultaneous endpoint events are limiting faces.

## 3. What remains to finish a height proof

The exact height ratio at the starting source is strictly less than its
value at every larger metric with the central inequalities retained. The
central comparison point persists: both positive cubic values increase,
and $`\lambda_u(y)>0`$ is metric independent.

A finished proof must verify height separation at all three endpoint
types. At the cancellation face, the comparison is a two-pole source
height theorem. At $`b_u=0`$, a factor in the u logarithmic derivative
cancels because $`r_1=m/h`$, leaving a quadratic metric numerator. At
$`a_q=0`$, the projective cubic metric becomes quadratic and deleting
the negative residue leaves only one positive pole. These reductions
are checked in the closed two-pole and a_q=0 boundary lemmas.
