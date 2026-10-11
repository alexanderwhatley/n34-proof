# A height theorem for coordinatewise ordered supports

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Statement

Let

u=x^(a_u)(1-x)^(b_u), v=x^(a_v)(1-x)^(b_v), w=x^(a_w)(1-x)^(b_w),

with the strict comparable support chain

0<a_u<a_v<a_w, 0<b_u<b_v<b_w.

Fix c3,c4>0 and put S=u-c3*v-c4*w. Suppose S has nine ordered generic critical points x1<...<x9, alternating maxima (odd indices) and minima (even indices). Then

MH: min{S(x1),S(x3),S(x5),S(x7),S(x9)}
    <= max{0,S(x2),S(x4),S(x6),S(x8)}.

More generally, the same inequality holds for any such ordered alternating nine critical points whenever their values and the endpoint limits would otherwise yield the ten disjoint common-level brackets below. No scale, mode order, cubic discriminant, nonphysical-root inventory or separately chosen contact level is imposed on the statement.

The uniform original-row consequence is

$$
G=c_1-u+c_3v+c_4w
$$

has at most eight distinct roots in $(0,1)$ for every $c_1,c_3,c_4>0$ under the stated strict coordinatewise support chain.

## 1. One positive common level is the obstruction

All three beta monomials tend to zero at both endpoints, and S/u tends to one there. Hence S tends to zero and is positive sufficiently near each endpoint. If MH failed, choose the ONE positive number c1 strictly between its right and left sides. Then S-c1 has alternating signs at

0, x1, x2, ..., x9, 1.

Continuity gives ten distinct roots of G=c1-S on the ten disjoint intervals. Thus it suffices to exclude a ten-root original row while retaining its one coefficient triple. The regional arguments below do exactly that.

Conversely, a generic ten-root row with the standing nine-critical-point ceiling yields nine alternating extrema with all five maxima strictly above c1 and all four minima strictly below c1, violating MH. This converse explains the height interpretation; the forward implication alone suffices to prove the displayed inequality.

## 2. Coincident v/w modes and the fully collinear special case

Put q=w/v and Delta=det(s_v,s_q). If Delta=0, only the v and w support vectors are forced to lie on one positive ray; u need not lie on it. This boundary is covered by the original-function regularization and support perturbation in Section 4: perturb v or w sufficiently slightly to make Delta nonzero while retaining the ten compact simple-root brackets and the strict support chain.

There is also a stronger elementary bound in the special case when ALL THREE support vectors are on one positive ray. Then write u=T^alpha, v=T^beta, w=T^gamma for a positive beta monomial T, where 0<alpha<beta<gamma. In z=log T, the equation G=0 becomes

c1*exp(-alpha*z)+c3*exp((beta-alpha)*z)+c4*exp((gamma-alpha)*z)-1=0.

Its left side is strictly convex in z and has at most two roots. The unimodal T takes each positive value at at most two original x points. Hence G has at most four roots in this fully collinear special case, including tangencies. This optional direct bound is not used to cover Delta=0 with u off the common ray.

For Delta nonzero, reflection x -> 1-x reverses its sign and preserves the strict support chain and all root counts. Work with Delta>0. Write v=x^a(1-x)^b, q=x^A(1-x)^B, with a,b,A,B>0 and aB-bA>0. There are unique real h,n with u=v^h*q^n.

## 3. Exact mode-region coverage

Define r_left=a/A and r_right=b/B, so 0<r_right<r_left. The strict u/v support inequalities are exactly

0<h*r+n<r at r=r_right,r_left.

If n>0, these imply h<1. If h<=0, positivity implies n>0 and consequently n>h. If n<0, positivity implies h>0. Therefore away from the boundary hypersurfaces n=0 and n=h, every source belongs to exactly one of the four regions below. The boundary h-n=1 is included in the larger-gap module.

| Region | Exact chart | Uniform original-row proof |
|---|---|---|
| Earlier u | n>h | The earlier-mode height theorem; it includes $h<0$ and $0<h<n$. |
| Middle u | 0<n<h<1 | The origin-interior curvature theorem. |
| Larger rightmost gap | n<0, h-n>=1 | The large-gap theorem, with its analytical coefficient proof when $h\ge1$. |
| Smaller rightmost gap | 0<h<1, h-1<n<0 | The smaller-rightmost-gap height theorem. |

The proof uses this finite coverage to apply four complete regional theorems. It does not reintroduce the original scale/discriminant/auxiliary ratio dispatch within either newly completed middle or smaller-gap region.

### Earlier u

The module [left of w regional master height theorem](earlier-mode-height.md) proves G has fewer than ten distinct roots whenever theta_u<theta_w, equivalent to n>h in this source chart. It localizes every saturated curvature node after theta_w, propagates the one actual positive c3 inequality by a concave contact function, and charges a compulsory unused J root. Its pole-free and three possible E/pole placements then contradict the global seven-node ceiling. This is a complete analytic regional proof and uses no new positivity table.

### Middle u

For the entire region $0<n<h<1$, the [origin-interior curvature proof](middle-height-by-convexity.md) gives at most eight roots of the original equation. Its convex level curve has a positive-normal curvature equation of degree at most six. Weighted Rolle and the closed-curve endpoint count give eight, including multiplicities at strict affinely independent supports. The distinct-root boundary argument covers finite support equalities. This direct proof replaces the earlier local birth and scale-orientation calculations throughout this middle region.

### Larger rightmost gap

For 0<h<1 and n<=h-1, [s137](later-mode-large-gap.md) gives a direct derivative-ratio proof. At most two original roots occur after theta_(v/u), which lies no later than theta_w. Ten roots would force all six raw Wronskian roots before that mode. The displayed Wronskian evaluation there is strictly negative, whereas its Vandermonde endpoint value is positive; degree-six saturation gives the opposite endpoint parity and a contradiction. The equality n=h-1 is included directly.

For h>=1,n<0, the localization in [s136](later-mode-large-height-localization.md), Sections 1--3, forces six positive roots of shifted J. Replace its Section 4 tables by [hge1 analytic coefficient obstruction](later-mode-large-gap-coefficients.md): the constant and fifth coefficients are both strictly negative by a displayed grouped identity. Six positive roots require those coefficients to have opposite signs. At h=1, J drops to degree at most five. The original-function boundary argument completes that submodule.

### Smaller rightmost gap

The new module [rightmost small gap master height theorem](later-mode-small-gap-height.md) proves the entire region at every scale and height. It derives actual derivative saturation, uses only the auxiliary ratio's physical signs, and forces a two-physical-C cell. Its actual last positive maximum gives the integral common-height witness c1<V(y). Two possible placements of the negative E root remain:

* Interlacing placement: the initial component has no admissible node, the main component has at most three, the central positive component at most one, and the tail at most one. Total at most five.
* Earlier E root: the signed metric height comparison and physical auxiliary ratio signs give at most two main, two central, and one tail node. If the left pole's E sign is reversed, the compulsory zero-to-infinity main component has a forbidden positive-coefficient crossing instead.

Both contradict the seven-node collection. The proof removes global Qv/Pv root inventory and discriminants, all nonphysical root exclusions, the scale barriers, and the three final signed leading-sign branches. It retains the local central orientation certificate, the analytic left positive-contact lemma, the signed metric separator, and the original common-height extraction. Those are explicit dependencies.

## 4. One original-function transfer handles the remaining faces

Suppose a strict source row has ten distinct roots, possibly multiple. The analytic function is nonidentically zero because G tends to c1>0 at both endpoints. Around its ten isolated zeros, choose disjoint compact neighborhoods. Odd-order zeros retain at least one simple crossing after a sufficiently small constant shift. Each even-order zero splits into two simple crossings in one of the two shift directions. Choose the direction that splits the more numerous type of even zero; odd_count+2*max(even_type_counts) is at least ten. A sufficiently small regular shift of c1, still positive, therefore gives at least ten simple compact sign brackets.

Small perturbations of the original supports and coefficients preserve all those brackets and the strict support inequalities. They first make Delta nonzero if necessary, so the h,n chart is defined after reflection. The standing generic-root reduction also avoids proper auxiliary algebraic coincidences and the mode faces n=0,n=h,h=0 while preserving the original coefficients as one common triple for every resulting row. If desired h-n=1 may remain in its directly covered module; no separate contact-level perturbation is used. The perturbed noncollinear row lies in one of the four complete regions and contradicts that region's theorem.

Thus every strict comparable row has fewer than ten distinct roots. To obtain the stated bound of eight, suppose a row had nine selected distinct roots. The [original-root regularization](../baseline/limiting-cases.md) changes the single positive coefficient $c_1$ slightly and retains at least nine simple crossings. A small generic support perturbation preserves their compact sign-changing brackets and the strict support chain. The preliminary derivative bound gives a finite simple-root count, and the two positive endpoint signs make that count even. Hence the perturbed row would have at least ten roots, contrary to the four proved regions. Therefore every such row has at most eight distinct roots. Section 1 proves the height inequality MH. Reflection, internal coincident-mode faces and auxiliary double faces are all covered as stated. Weak support chains or a support on the coordinate axes are outside this theorem's stated strict scope; the other original sign chambers continue to supply their own proof.

## Scope

This theorem organizes the strict coordinatewise ordered positive supports into four regions. It gives one height inequality through those four proved arguments. The middle region has the direct convex-level proof above; the smaller rightmost-gap region retains its central orientation identity and signed-height comparison. The unrestricted [nonnegative-support corollary](nonnegative-height.md) is a separate assembly covering unordered supports as well.
