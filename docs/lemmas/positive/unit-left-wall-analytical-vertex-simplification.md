# An analytical simplification of the three hard unit-wall vertices

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

This is an alternative proof of the three nontrivial vertex signs in [unit left wall positive cubic entropy comparison](unit-left-wall-positive-cubic-entropy-comparison.md). It replaces the raw 128-positive-term certificate with elementary calculus and a single **15-term** positive endpoint polynomial. It does not enlarge the scope of that unit-wall proposition.

Retain eta=e, xi=x, 0<r<e<x, S=e+x, W=2ex+S, and Delta=x-e. The original forcing numerator is T=R(Y'H-YH')-Y(H-PY)j, and Phi=T/(H²R). Define the polynomial factors C0,C1 by

Delta⁶ Tconstant=(r-e)² S(S+2)W C0(r),
Delta⁶ Tlinear=r(r-e)² S(S+2)W C1(r).

All prefactors are strictly positive on the left interval. Thus it remains to prove C0,C1<0.

## Pure linear vertex

Direct exact differentiation gives

C1''=-4S(S+2)<0,
C1'(e)=(x-e)(3e²+8ex+6e+x²+6x)>0,
C1(e)=-e(x-e)²(S+2)<0.

Because C1' decreases, it is positive on the entire interval r<e. Hence C1(r)<C1(e)<0. No multivariate positivity certificate is needed for this vertex.

## Pure constant vertex

The corresponding exact identities are

C0'''=-12S(S+2)<0,
C0'(e)=4(x-e)(3e³+3e²x+6e²+3ex+2e+x)>0,
C0(e)=-(x-e)²(2e³+2e²x+4e²+2ex+e+x)<0,

C0(0)=-(e+1)[3e³(x-e)+e²(7x-3e)+7e²x²+ex³+3ex²+x³]<0.

The derivative C0' is strictly concave and positive at its right endpoint. Its positive set in [0,e] is therefore an interval containing e. Consequently C0 either increases throughout, or first decreases and then increases; it has no interior maximum. Both endpoint values are negative, so C0<0 throughout.

## Affine (0,3) vertex

Use the precise denominator from the clarification: Phi=N03/(P Q Z² R03), where Z=3PQ+P+Q-1 and R03=B+H(l0+l1r)>0. The original numerator is the quadratic

N03=A2 r²+A1 r+A0,

A2=P(P+2Q-1)[(P-1)²(3Q-2)+(P-1)(4Q-1)+2Q]>0,
A1=PQ(P-Q)Z,
A0=-Q(2P+Q-1)[(Q-1)²(3P-2)+(Q-1)(4P-1)+2P]<0.

Thus N03 is strictly convex and negative at zero. Under the exact wall parameterization P=S(S+2)/Delta², Q=SW/Delta², its other endpoint is

N03(e)=-4S(S+2)²W² E(e,x)/Delta⁹<0,

where

E=e⁶+e⁵(4x+2)+e⁴(15x²+16x+2)
  +e³(14x³+36x²+14x)+e²(2x⁴+16x³+15x²)
  +e(2x⁴+4x³)+x⁴.

This seven-group display consists of 15 positive monomials; E>0 for e,x>0 is immediate. Convexity bounds N03(r) above by the negative straight chord between its two endpoint values, proving the required strict negative forcing gap.
