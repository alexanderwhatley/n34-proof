# A complete positive two-wall master

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Let the outer supports $s_1=(a_1,b_1)$, $s_3=(a_3,b_3)$ have strictly positive coordinates and distinct modes. After relabeling, $\gamma=a_3b_1-a_1b_3>0$. Put

$$
s_2=P s_1+Q s_3,\qquad P,Q>1.
$$

For every $E_1,E_2,E_3,L>0$, the level difference

$$
\sum_{i=1}^3 E_i t^{a_i}(1-t)^{b_i}-L,\qquad 0<t<1,
$$

has at most **eight zeros counting analytic multiplicity**. The outer supports can be comparable or incomparable, have unequal degrees, or share one coordinate. All source edges and multiple contacts are included.

## Exhaustive composition

For $r=-\lambda_1/\lambda_3>0$, define

$$
B=r(1+r),\quad H=P(P-1)r^2-2PQr+Q(Q-1),\quad
R=\frac{(d_1+rd_3)(a_1+ra_3)(b_1+rb_3)}{\gamma^2},\quad Y=R-B.
$$

The roots of $H$ are $0<\eta<\xi$, and their source ratios are $\sigma=B/R>0$. At every one original coefficient tuple and level there is one actual common-entropy curve. Its normal-curvature contacts are zeros of $B+H u_C-R$, with their analytic orders preserved. Two normal-Rolle stages add at most two original weights.

Write the sign pair as $(\operatorname{sgn}Y(\eta),\operatorname{sgn}Y(\xi))$.

| Sign pair | theorem | Curvature ceiling | Original ceiling |
|---|---|---:|---:|
| $(-,-),(-,0),(0,-),(0,0)$ | Closed-high positive strong-fork master | 4 | 6 |
| $(+,-),(-,+)$ | Full strict-mixed positive master | 6 | 8 |
| $(+,+)$ | Full strict-low positive master | 6 | 8 |
| $(+,0),(0,+)$ | General positive unit-wall boundary theorem | 6 | 8 |

The strict-low proof is the main final simplification. Strict geometric log concavity gives a global power upper tangent through any actual central contact. Simultaneous contacts in both exteriors would force at least five positive roots of a seven-term generalized polynomial whose coefficients have exactly four sign changes. An elementary weighted Rolle induction proves the requisite generalized Descartes rule. This empties a wall interval without canonical seam or critical-point cases. Central four, exterior two, and a short no-central forcing/parity contribution to the root count then give curvature six.

The mixed proof uses a short positive decomposition of two projective forcing coefficients, Descartes, the actual entropy ODE and endpoint parity. The high proof uses a six-vertex convex comparison and source-scale interpolation; a 15-monomial endpoint polynomial replaces a 128-term sign expansion. Unit contacts are factored and counted directly. These are analytical arguments with short exact arithmetic checks.

## Complete positive two-internal-wall scope

The classification states that every strictly positive, affinely noncollinear source has two internal origin-quadratic walls on its actual positive-normal interval if and only if it has a relabeling of the strong-fork form above. Thus this theorem closes **all positive two-internal-wall sources**, not only the coordinate-antichain upper-fork row.

“Internal” refers to the normal interval between extreme support modes. Roots of the origin quadratic elsewhere in $(0,1)$ are not counted in that classification.

## Scope limits

The original global proof of $N(3,4)=9$ remains complete. This theorem does not assert the same eight-bound for arbitrary signed supports, replace every signed $(3,1)$ or $(2,2)$ chamber, or give a nongeneric weighted one-edge extension. The separate closed strong-fork boundary transfer proves a distinct-root result, not a weighted result at old degenerate sources.

regional inequalities, large redundant certificates, and exact guards remain immutable records. Their obsolete scope restrictions are superseded by this full theorem, not silently edited. Numerical scans are discovery only. The replaced regions overlap, so this theorem is not an additive count of deleted original cases.
