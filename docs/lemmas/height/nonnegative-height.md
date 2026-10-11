# An unrestricted nonnegative-support height corollary

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Statement

Let u,v,w be beta monomials with arbitrary exponent vectors in
[0,infinity)^2. No order between any pair is assumed. For c3,c4>0,
set S=u-c3*v-c4*w. Then every nine ordered interior points obey

min(S(x1),S(x3),S(x5),S(x7),S(x9))
       <= max(0,S(x2),S(x4),S(x6),S(x8)).              (MH)

Consequently every nonidentity row c1-S, c1>0, has at most eight
distinct physical zeros.

The only positive-level identities are the weak
least-support identities:

1. u=v=w=1 and c1+c3+c4=1;
2. u=1, {v,w}={t,1-t}, and c3=c4=1-c1 in (0,1).

The names of v and w may be interchanged.

## Proof on strict positive supports

First assume both coordinates of each support vector are positive.
A violation of (MH) permits a common height ell>0 strictly above
all four even sample values and below all five odd sample values.
Since S tends to zero at both endpoints, the equation S=ell has
at least ten distinct sign-changing zeros: one before x1, eight
between successive samples, and one after x9.

Normalize this one common level by the actual positive atom u:

f=(ell-S)/(-u)=1-ell/u-c3*v/u-c4*w/u.

The three original negative-coefficient atoms have supports

d=-s_u,
    h1=s_v-s_u,
    h2=s_w-s_u.

The vector d is (-,-) and is strictly below h1 and h2 in both
coordinates, because s_v and s_w are strictly positive. It is
therefore the same dominant negative atom at both endpoints.
The normalization preserves all ten original zeros and all three
positive original coefficients.

The retained original one-corner SUPPORT refinement, with its
ten-simple-original-root premise, applies after an arbitrarily small
generic perturbation in the preserved compact sign brackets. A further
arbitrarily small common regular-height shift makes all original
roots simple, retaining every selected bracket and coefficient sign.
The
elementary derivative-anchor ceiling proved below, together with the
two negative endpoint signs and simple-root parity, makes such a
candidate have exactly ten simple roots. This is the preliminary
cubic/cubic counting ceiling used by SUPPORT, not the final original
nine-root theorem. Its
conclusion is precisely: after reflection, both other first
exponents are positive, and the only remaining sign patterns are

(++),(++);  (++),(+-);  (+-),(+-).                (1)

These are necessary conditions for a ten-root counterexample, not
a claim that (1) classifies every arbitrary pair of relative supports.
The standalone retained local calculation is
[the endpoint classification](../baseline/endpoint-support-classification.md), in its one-corner refinement.

The first pattern is excluded by the least-support master:
here u is componentwise below v and w. The second is the mixed
one-corner normal form. Its dominant atom has supports (-A,-B),
the ordinary atom (a,b), and the mixed atom (c,-nu), all magnitudes
positive, with B>nu. The complete mixed theorem gives
at most eight original roots for every c>0, independently of delta
and with no separate c<=nu signed-curvature inequality.

For completeness the last pattern has a short direct proof. Write
the dominant atom h0=t^(-A)(1-t)^(-B), with mode mu=A/(A+B),
and the two mixed atoms hj=t^cj(1-t)^(-nuj), j=1,2, where
cj,nuj>0 and B>nuj. Both hj' are positive. For t>=mu every
nonzero summand of f'=-E0*h0'-E1*h1'-E2*h2' is negative.
For t<mu, put rj=hj'/(-h0')>0. The pair identity

Vj=ellj*ell0*(ell0-ellj)+rho*(B*cj+A*nuj)>0

holds there because ell0<0 and ellj>0. Hence
(h0'/hj')'>0 and rj'=(h0'/hj')'/(h0'/hj')^2>0.
The equation f'=0 on (0,mu) is

E0=E1*r1+E2*r2.

Its right side is strictly increasing, so f' has at most one zero.
The row f has at most two zeros. This excludes the final pattern.

All three possibilities contradict the ten original roots. This
proves (MH) on strict positive supports, without the full N(3,4)
root bound and without the AP or PS theorems.

### Preliminary derivative-anchor ceiling, proved locally

The only external root-count statement needed here is the retained
El Hilany--Tavenas inequality

Z(t^alpha*(1-t)^beta*P-Q) <= deg(P)+deg(Q)+2,

for a nonidentity equation with real polynomial P,Q. Put
gi=D hi=elli hi and N=sum(Ei*gi)=-D f. The dominant (-,-)
atom has a single derivative zero mu. On both sides divide N by
g0. The derivative numerator is

g0*N'-g0'*N=sum_{j=1,2}(Ej*g0*gj'-Ej*g0'*gj),
    g0*gj'-g0'*gj=(h0*hj/rho)*C0j,
    C0j=ell0*ellj*(ellj-ell0)
                       +rho*(ell0*ellj'-ell0'*ellj),

with degree at most three. After removing one nonvanishing beta
factor, its zero equation is beta times a cubic plus a cubic. The
displayed inequality gives at most eight derivative zeros, including
common polynomial roots by removing and then restoring their factor.
If that derivative equation is an identity, N/g0 is constant and
the original function has at most two roots; it cannot be a ten-root
candidate.

For a generic candidate N(mu)!=0. The two quotient intervals cost
at most two in componentwise Rolle, so N has at most ten zeros and
f has at most eleven. Analyticity extends any removable quotient
case, or it can be avoided by generic perturbation in the ten
preserved original-root brackets. The two negative endpoint signs
make the generic simple original-root count even, so a hypothetical
count at least ten is exactly ten. This supplies the sole saturation
premise of the retained local SUPPORT refinement. No AP, PS,
no-lobe, genuine-lobe, or final global chamber theorem enters this
preliminary count.

## Nonnegative supports, roots and identities

For arbitrary nonnegative supports, replace each support by itself
plus epsilon*(1,1), leaving every coefficient and sample point fixed.
The values at the nine selected interior samples converge to their
original values. The strict-support (MH) inequality therefore passes
to the limit, proving the full displayed statement.

To obtain the distinct-root corollary, suppose a nonidentity row
c1-S has nine distinct zeros. The usual one-common-height analytic
regularization retains at least nine simple roots in disjoint compact
brackets, at a level still positive. Perturb all supports to positive
ones within those preserved brackets. If new incidental zeros are
multiple, choose the one common positive level regular again by an
arbitrarily small shift, still retaining every selected bracket.
The perturbed row is positive at both endpoints, so its finite set
of now-simple zeros has even
cardinality, at least ten. Ten crossings create a violation of (MH),
as in the first paragraph. This contradiction gives eight distinct
roots, including nonnegative support boundaries.

If c1-S is an identity, then u=c1+c3*v+c4*w is bounded below by
c1>0. A nonnegative beta monomial u with a positive exponent in
either coordinate vanishes at that endpoint. Thus s_u=(0,0), so
u=1 and s_u is automatically least. The least-support
identity classification then gives exactly the two families stated
above. No new identity classification is assumed on an unordered
support chart.
