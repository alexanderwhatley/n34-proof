# Canonical low-wall height separation persists under source dilation

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

This is an analytical monotonicity theorem for the displayed scaling family. The uniform low-wall height inequality is proved in [the power-tangent theorem](low-wall-power-tangent-global-height-theorem.md) and [the complete two-wall theorem](two-wall-positive-master.md). The monotonicity below is an auxiliary statement about that height
separation at the first unit scale.

## Statement

Fix P,Q>1 and a cubic S(r)=c0+c1 r+c2 r²+c3 r³ with all ci>0. Put

H=P(P-1)r²-2PQ r+Q(Q-1), B=r(1+r), Rk=kS, Yk=kS-B,
uk=Yk/H,

and let eta<xi be the positive roots of H. Suppose there is one k0>0
with both Yk0(eta),Yk0(xi)>0 and exactly the three canonical physical
source components: one central middle-zero-to-middle-zero interval
and two exterior positive-alpha-bound-to-positive-alpha-bound intervals.

Write Jk(r)=J(r,uk(r)) for the common-entropy function. Let
mC(k) be its global minimum on the central component, and ML(k),MR(k)
its global maxima on the left and right components.

There is one open interval I=(kstart,kend) of canonical scales containing
k0. For k1<k2 in I,

mC(k2)>mC(k1), ML(k2)<ML(k1), MR(k2)<MR(k1).

In particular the two global gaps mC-ML and mC-MR, and the weaker gap

G(k)=mC(k)-min(ML(k),MR(k)),

are strictly increasing. If G(k1)>=0 then G(k2)>0 for every later scale
k2 in I. No continuation of any particular critical point is required.
Critical pairs may be born or die, and the global extremizer may change.

The geometry and monotonicity statement needs only a positive-coefficient
cubic. The original-contact corollary below additionally uses the antichain strong-fork forcing budget.

## The entire canonical scale interval

Set f=S/B. Its derivative has, after clearing its positive denominator,
the numerator

c3 r4+2c3 r3+(c2-c1)r²-2c0 r-c0.

The descending coefficient sequence has exactly one sign change.
Descartes' rule and the opposite endpoint signs show that f has one
simple critical point, its global minimum. Since a canonical central
component exists at k0 while both walls have Yk0>0, this minimum lies
strictly between eta and xi.

Define

kstart=max(B(eta)/S(eta),B(xi)/S(xi)),
kC=1/min(f),

TL=B+Hr/Q=r(Q-Pr)(Q-(P-1)r)/Q,
TR=B+H/P=(Pr-Q)(Pr-Q+1)/P,

kL=max( TL(r)/S(r) : 0<r<eta ),
kR=max( TR(r)/S(r) : xi<r<infinity ),
kend=min(kC,kL,kR).

The two exterior maxima defining kL,kR are attained in their open
intervals. Indeed TL/S tends to zero at zero, TR/S tends to zero at
infinity, and their wall values are strictly below k0 while each
exterior component supplies a value greater than k0. Thus kstart<k0<kend.

For every k in I, the equation kS=B has exactly two positive roots
vL(k),vR(k), both strictly between eta and xi. Its negative region is
DC(k)=(vL(k),vR(k)). The exterior bound regions are

DL(k)={0<r<eta : kS<TL},
DR(k)={xi<r : kS<TR}.

Each is a nonempty open interval. To see the left assertion, put
alpha=Q/P and beta=Q/(P-1). On 0<r<alpha,

S/TL=S/(Qr) * (1-r/alpha)^(-1)*(1-r/beta)^(-1).

Its Laurent series has a positive 1/r coefficient and positive
coefficients at every nonnegative power. Its second derivative is
strictly positive. Since kS/TL tends to infinity at zero, is greater
than one at eta, and is less than one somewhere before eta, its
sublevel set is exactly one interval strictly before eta. The right
assertion follows by r=1/s, P,Q exchanged, and S reversed.

These intervals are precisely physical source components, not just
necessary bound domains. On each exterior, Yk>0 since the unique valley
of f is central. The indicated bound is the smaller probability bound.
Centrally, Yk<0 implies uk>0. The left sublevel interval just proved
ends before eta; strict convexity then gives kS/TL>1 throughout
eta<r<Q/P. Because H<0, this is exactly uk<r/Q there. Reflection gives
uk<1/P on Q/P<r<xi. At r=Q/P the two bounds agree and TL=TR=0, so Rk>0
gives the same strict bound inequality. Thus all of DC is physical.

## Pointwise entropy monotonicity and nested domains

Write D=P+Q-1 and T=1+r-Du. The exact entropy derivative is

Ju=-(B+Hu)/[D u(1-Pu)(r-Qu)T]<0.

As the source is dilated,

partial uk/partial k=S/H,
partial Jk/partial k=Ju*S/H.

It follows that Jk increases strictly at every central point where it
remains physical, and decreases strictly at every exterior point.
Moreover,

DC(k2) is contained in DC(k1),
DL(k2) is contained in DL(k1),
DR(k2) is contained in DR(k1)

whenever k1<k2 in I: all three domain definitions are strict sublevel
inequalities with the same positive source S.

At either endpoint of DC, uk tends to zero, with the two other
probabilities strictly positive, so Jk tends to plus infinity.
At either endpoint of either exterior interval, a positive-alpha
outer probability tends to zero while the middle and other outer
probabilities remain strictly positive, so Jk tends to minus infinity.
All endpoints are finite, away from the walls, and away from zero or
infinity. Hence the displayed global minima and maxima are attained
at interior points and are finite.

Choose a minimizer r2 for mC(k2). Domain nesting and pointwise strict
monotonicity give

mC(k2)=Jk2(r2)>Jk1(r2)>=mC(k1).

Choose a maximizer on either exterior at k2. The same reasoning gives

Mi(k2)=Jk2(r2)<Jk1(r2)<=Mi(k1), i=L,R.

This proves the theorem without labeling, selecting or continuing a
critical branch. In particular changes in the number of stationary
points do not affect the result.

## Relation to the complete contact bound

This scaling theorem describes how the central minimum and exterior maxima change. The [power-tangent theorem](low-wall-power-tangent-global-height-theorem.md) proves the required ordering directly, and the [complete two-wall theorem](two-wall-positive-master.md) gives the eight-root conclusion without a reference-scale assumption. The scaling argument therefore has the narrower role of a mathematical comparison tool; it does not leave an open case in the complete proof.
