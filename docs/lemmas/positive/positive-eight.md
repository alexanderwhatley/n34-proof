# A unified all-positive theorem after the native Q=1 completion

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Theorem

For three affinely independent supports s_i=(a_i,b_i) with a_i,b_i>0,
positive coefficients E_i and a positive common level L,

L-sum_i E_i x^(a_i)(1-x)^(b_i)

has at most **eight zeros counted with analytic multiplicity** on (0,1).
No coordinate permutation, mode order, generic event routing, separate
integer boundary case, source coefficient regularity, or analytic-contact
simplicity is needed. The sources are genuinely positive, so the level
difference is automatically nonidentity.

Once this strict theorem is , its direct common-level transfer
also proves **eight distinct roots** for all nonnegative supports
a_i,b_i>=0, E_i,L>0, provided the level difference is nonidentity. This
closed theorem allows affinely collinear supports, repeated supports,
coincident modes and zero coordinates. It does not count arbitrary old
boundary multiplicities.

## The source classification gives an exhaustive theorem dispatch

Let alpha be the origin barycentrics, sum alpha_i=1 and sum alpha_i s_i=0.
Positive supports imply alpha has both a positive and a negative entry.
The origin-wall classification gives two disjoint alternatives.

If alpha has only one positive entry, label it alpha_1=1+u+v, with
alpha_2=-u, alpha_3=-v, u,v>=0. Origin balance gives the exact identity

V0=-lambda_1^2-u(lambda_2-lambda_1)^2-v(lambda_3-lambda_1)^2.

This is zero-free on the actual open positive-normal interval. An equality
would make all supports have the same mode, contradicting affine
independence, or would be the endpoint mode of two active supports when
one barycentric is zero. Thus the zero-free normal theorem gives
weighted eight. This includes the mode coincidences that cannot enter the
strict mode-ordered entropy chart.

If alpha has two positive entries, label them alpha_1=A, alpha_3=B and
alpha_2=-k, where k=A+B-1>0. Then

s_2=P s_1+Q s_3, P=A/k>0,Q=B/k>0,K=P+Q-1>0.

The two outer supports are linearly independent and have distinct modes.
Their positive combination s_2 has a strictly intermediate mode. Their
whole normal interval is carried analytically to r>0, preserving all root
orders, and

V0=-lambda_3^2 H/K,
H=P(P-1)r^2-2PQr+Q(Q-1).

The gauge identifies normal curvature with B+Hu_C-R, up to
nonvanishing analytic factors, where the genuine source metric is

R=[(d_1+r d_3)(a_1+r a_3)(b_1+r b_3)]/gamma^2,
d_i=a_i+b_i, gamma=a_3 b_1-a_1 b_3>0.

It has four strictly positive coefficients and three real negative roots,
counting repeated factors. No coordinate-order claim is needed to obtain
this metric factorization.

| Exact source parameters | Curvature theorem / original result |
|---|---|
| P<=1,Q<=1 | H has no positive root; zero-free normal theorem gives original weighted eight |
| P>1,0<Q<1, or its reflection | Complete sprint23 real-negative-root one-wall curvature six; two normal Rolle payments give original weighted eight |
| P>1,Q=1, or its reflection | New native Q=1 LOW + HIGH + direct unit theorem give one-wall curvature six; original weighted eight |
| P>1,Q>1 | Complete sprint22 arbitrary-positive-cubic two-wall curvature six; original weighted eight |

These four rows are exhaustive. In the first row all nonzero H coefficients
are negative; at P=Q=1, H=-2r has no positive zero. At a one-equals-one
boundary with the other below one there is still no positive wall. When
the other exceeds one, r=0 is excluded and there is exactly one positive
wall; this is precisely the new native Q=1 row. Reflection swaps P,Q and
reverses r while preserving contact multiplicity. No transition between
two entropy models by a multiplicity limit is used.

Two weighted normal Rolle steps apply globally to each actual
positive level branch. Each nonzero curvature ceiling six yields original
weighted eight. Homogeneous/no-contact cases are already included in the
corresponding source theorems.

## Direct closed-coordinate transfer, without an old global ceiling

Suppose a nonidentity nonnegative-support level difference has nine
distinct roots. Select nine disjoint compact neighborhoods. Let o be the
number of odd-order roots and e_+,e_- the counts of even minima and maxima.
A sufficiently small common level shift in one direction creates at least
o+2e_+ simple roots; the opposite shift creates at least o+2e_-.

Choose the better direction, giving at least
o+2 max(e_+,e_-)>=o+e_++e_-=9.

The shift can avoid the finitely many local critical values, and its level
remains positive. These selected simple roots have disjoint sign brackets
and persist under small support perturbations. Perturb all coordinates to
strict positivity and choose affinely independent supports; these generic
conditions are dense in the unrestricted positive support space. The
strict theorem would then forbid the nine surviving roots. Contradiction.

This common shift is the only change to the level. The same coefficient
vector is retained, and support perturbation is performed afterward. The
argument requires no EHT ceiling, no proof that ten old roots were simple,
and no separate poset or mode boundary inventory. It proves distinct eight,
not a preservation theorem for arbitrary analytic multiplicities.

## Effect on the actual six-row original all-positive partition

| Increasing second-coordinate order after sorting first coordinates | Earlier replacement | Unified consequence |
|---|---|---|
| 123 coordinate chain | Short extreme-coordinate/mode obstruction to ten-root saturation | Direct weighted eight for affine-independent positive sources |
| 132 lower fork | Weighted eight | Included in the same theorem |
| 213 upper fork | Weighted eight; closed-cone distinct eight | Included in the same theorem |
| 231 and 312 one-edge orientations | the earlier proof direct weighted eight; closed-cone distinct eight | Included in the same theorem |
| 321 antichain | Weighted eight for affine-independent strict supports; distinct closure | Included in the same theorem |

## A genuinely contacted Q=1 chain source

Use outer supports (2,3),(1,1), middle support (6/5)(2,3)+(1,1), and
scale every support by 30. In increasing first-coordinate order these
supports are (30,30),(60,90),(102,138); their second-coordinate order is
also 123, so they form a strict coordinate chain. The middle source mode
lies strictly between the two outer modes.

Its native parameters and genuine metric are

P=6/5,Q=1,xi=10,
R=(30+37r+15r^2+2r^3)/30,
Y=(r-2)(2r^2-11r-15)/30.

The metric distances are 2,5/2,3, all exceeding one. The positive Y roots
are a=2 and b=(11+sqrt(241))/4, and l=(sqrt(241)-11)/4>1. In particular
a<b<xi, the wall is LOW and ab>l^2. At r=3 the formal source is
u_0=25/126, strictly inside its physical bounds; choosing the finite entropy
C=J(3,25/126) creates an actual central contact. Both forcing endpoint
coefficients are positive. Thus the new Q=1 LOW theorem covers a genuine
contacted chain source that lies beyond the metric-root inequality; the seam
cannot simply be discarded as nonexistent.
