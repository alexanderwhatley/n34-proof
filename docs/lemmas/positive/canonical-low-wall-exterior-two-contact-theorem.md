# Each canonical low-wall exterior loop has one entropy maximum

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Statement

Let P,Q>1, let eta<xi be the roots of
H=P(P-1)r²-2PQr+Q(Q-1), and let R be a cubic with all four
coefficients strictly positive. Put Y=R-r(1+r) and theta0=Y/H.
Assume Y(eta)>0,Y(xi)>0 and that Y has two simple central roots

eta<c1<c2<xi.

Assume the physical source has a nonempty exterior bound-to-bound component
on each side. This is precisely the canonical three-loop geometry,
with one central middle-zero-to-middle-zero component.

On each exterior component, the source entropy J0(r)=J(r,theta0(r))
has exactly one stationary point. It is a nondegenerate strict maximum.
Consequently, each finite common entropy has at most TWO exterior
contacts, counting multiplicity. The maximum level has one double
contact; lower finite levels have two simple contacts.

The theorem permits arbitrary positive-coefficient cubics, unequal
P,Q and comparable positive geometric outer supports. It requires
the canonical central root band, rather than merely two low walls.
No unrestricted low-low original-contact ceiling is asserted here.

## Interlaced source roots and elasticity

Since Y has positive constant and leading coefficients and two
positive roots c1,c2, its third root is -l<0. On 0<r<eta one may write

theta0(r)=d(r+l)(c1-r)(c2-r)/[(eta-r)(xi-r)], d>0.

It is strictly positive throughout that exterior wall interval.
Define eta0=r theta0'/theta0. Logarithmic differentiation gives

eta0=r/(r+l)+p-q,
p=r(c1-eta)/[(eta-r)(c1-r)]>0,
q=r(xi-c2)/[(c2-r)(xi-r)]>0.

The essential elementary implication is

eta0>1 implies eta0'>0.                                      (1)

Indeed r/(r+l)<1, so eta0>1 forces p>q. Furthermore

p'/p=1/r+1/(eta-r)+1/(c1-r)
     >1/r+1/(c2-r)+1/(xi-r)=q'/q>0.

Thus p'>q', and

eta0'=l/(r+l)²+p'-q'>0.

No sign statement is claimed when eta0<=1. The strict comparison
uses only the interlacing eta<c1<c2<xi and positivity of l.

## Every stationary point is a strict maximum

The native common-entropy graph thetaC is unique and physical
at every r>0. Its exact projective elasticity etaC=r thetaC'/thetaC
is strictly decreasing:

etaC'=-(1-P thetaC)(r-Q thetaC)
 [thetaC(H+(P+Q-1)r)²+(P+Q-1)r²(1+r-(P+Q-1)thetaC)]
 /[r(1+r)+H thetaC]³ <0.                                    (2)

The actual reflected coordinate phiC=thetaC/r has its unique maximum
at alpha=(Q-1)/P, with eta<alpha. Hence etaC>1 throughout 0<r<eta.
Equivalently this follows from the exact derivative identity

phiC'=thetaC(r-Q thetaC)(Q-1-Pr)
 /[r²(r(1+r)+H thetaC)]>0 there.

Let r0 be any stationary point of the physical left source entropy.
Set C=J0(r0). At r0, the actual and source values coincide. Since
Ju<0 and

J0'=Ju(theta0'-thetaC'),

their first derivatives also coincide. Therefore

eta0(r0)=etaC(r0)>1,
J0''(r0)=Ju(r0,theta0(r0))*theta0(r0)/r0
          *(eta0'(r0)-etaC'(r0))<0,

by (1) and (2). In particular every stationary point is nondegenerate
and is a strict maximum.

On the canonical left component, both endpoints are positive-alpha
probability bounds, so J0 tends to minus infinity at both. An interior
maximum exists. There cannot be two maxima: a continuous function
with strict local maxima at two points has an interior minimum
between them, contradicting the just-proved stationary-point sign.
Thus exactly one maximum exists. The entropy is strictly increasing
before it and strictly decreasing after it. Every lower finite level
has exactly two simple contacts, and its maximum level one contact
of multiplicity exactly two.

## Reflection and what remains

Under r=1/s, swap P,Q and reverse the positive source cubic:
Rtilde(s)=s³R(1/s), Htilde=s²H(1/s), Ytilde=s³Y(1/s),
thetatilde0=s theta0.

The canonical root interlacing is preserved, with reflected central
roots 1/c2<1/c1 between walls 1/xi<1/eta and negative root -1/l.
The original right exterior becomes the reflected left exterior.
Entropy values, analytic contact orders and maximum nondegeneracy
are preserved. This proves the same two-contact ceiling on the right.

Together with the directional localization,
if both exterior loops are occupied at one common entropy, all
central contacts lie in

(alpha,beta)=((Q-1)/P,Q/(P-1)).

The present theorem pays for each outer loop independently. A
separate central contact or common-height argument is still required
to reduce the canonical total to six normal-curvature weights.
In particular, a bound of two on useful forcing weights in this
inner interval would give at most three central contacts by weighted
Rolle; the central positive endpoint phases then improve the bound
to two. That proposed inner forcing theorem is not proved here.
