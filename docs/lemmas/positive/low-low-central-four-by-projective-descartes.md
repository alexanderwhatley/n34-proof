# Four central contact weights in every strict low-low strong fork

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Let P,Q>1, let eta<xi be the roots of
H=P(P-1)r^2-2PQ r+Q(Q-1), and let R be a cubic with strictly positive
coefficients. Put B=r(1+r), Y=R-B, u0=Y/H. Suppose

Y(eta)>0 and Y(xi)>0.

At any one finite actual common entropy, the central normal-curvature
contact weight is at most FOUR. Its finite total weight is even, hence is
zero, two or four. No physical source-component regularity, root simplicity,
antichain ordering, or metric negative-root factorization is required. This
lemma does not claim the unrestricted low-low original-eight theorem.

Use the universal projective forcing identity verified in the mixed-wall
module. The identity itself is polynomial and does not require mixed signs.
Write G(v)=(1+v)^3 R((eta+xi v)/(1+v)) with coefficients g0,...,g3, and
L=eta(1+eta), T=xi(1+xi), Delta=xi-eta. Its forcing coefficients are

C0=(g0-L)(3g0-L), C1=4g1(g0-L),
C2=g1^2+2g2(g0-2L)-(L^2+2LT+Delta^2),
C3=4(g0T-Lg3),
C4=T^2+2LT+Delta^2+2g1(2T-g3)-g2^2,
C5=4g2(T-g3), C6=(3g3-T)(T-g3).

Since g0>L and g3>T, the first two coefficients are strictly positive
and the last two strictly negative. Between the second and penultimate
coefficients there are only four possible sign transitions. Their starting
and ending signs are opposite, so their sign-variation count is odd and
cannot exceed three. Omitting zero middle coefficients cannot increase
that count. Thus the transformed forcing polynomial has at most three
positive root weights, by Descartes. Its positive projective substitution
preserves analytic orders, so central W root weight is at most three.

The universal formal-ODE comparison applies throughout the central interval:
the actual denominator B+H uC and source denominator B+H u0=R are positive,
and their secant coefficient is analytic even when u0 lies outside its
probability bounds. Its positive integrating factor gives

central contact weight <= central W root weight + 1 <=4.

As either wall is approached from inside the central interval, H<0 and
Y has positive nonzero wall limit, so u0 tends to minus infinity. The
actual uC remains finite; thus the contact difference is positive near
both walls. Its finite total zero weight is even. Finiteness follows from
the ceiling applied to every finite contact selection.

## A conditional canonical original-eight consequence

Assume in addition the canonical low-wall geometry: Y has two simple roots
strictly between eta and xi, and there is a physical exterior bound loop on
each side. The canonical exterior theorem gives
at most two weighted contacts on each exterior. If a common-level ordering
inequality makes at least one of the three source components empty, then the
normal-curvature total is at most six: if one exterior is empty, it is at
most four central plus two on the other exterior; if the central component
is empty, it is at most two plus two. Two normal-Rolle stages give original
weight at most eight (and at most six when the central component is empty).

This conditional consequence requires no global forcing-five budget or
double-edge contribution to the root count. It consequently permits comparable positive outer
supports whenever the exterior theorem and chosen common-level ordering
inequality have that scope. It does not extend an antichain-only source-order
inequality by implication, and it does not pay noncanonical geometry.
