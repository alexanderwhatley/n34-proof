# A power tangent proves the full canonical low-wall height barrier

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Statement and source scope

Fix P,Q>1. Let H=P(P-1)r²-2PQr+Q(Q-1) have roots eta<xi,
and let R=c0+c1 r+c2 r²+c3 r³ have all four coefficients positive.
Put Y=R-r(1+r), theta0=Y/H. Assume strict-low walls
Y(eta)>0,Y(xi)>0 and canonical physical source geometry: one central
middle-zero-to-middle-zero component and two exterior bound-to-bound
components.

Let mC be the global minimum of the source entropy on the central
component and ML,MR its global maxima on the two exterior components.
Then

mC>min(ML,MR).                         (1)

The conclusion is strict, including equality possibilities in a
proposed comparison and arbitrary multiplicities of stationary points.
There is no degree, residue-balance, contrast, source-slope, P/Q-order,
wall-ratio-size, critical-location, or critical-branch-persistence inequality.
Negative real roots of R and coordinate antichain order are not used.

At every common finite entropy, at least one canonical component is
empty. The antichain forcing budget therefore gives at most
six normal-curvature weights and eight original weights. Extension
of this contact corollary to comparable supports requires its own
exterior/central or degree-six contribution to the root count; (1) itself already holds for
all positive cubic source geometry stated here.

## A self-contained generalized Descartes lemma

Let lambda0<...<lambdan be real numbers and all ai be nonzero. The
function f(r)=sum(ai r^lambdai), r>0, has at most V(a0,...,an)
zeros counting analytic multiplicity, where V is the number of
coefficient sign changes. Zero coefficients are omitted.

Here is an induction proof retaining multiplicity. Divide by the
positive analytic unit r^lambda0. The resulting function
g=a0+sum(ai r^(lambdai-lambda0),i>=1) has the same zero weights.
Its derivative has the coefficient signs (a1,...,an), so induction
bounds its root weight by V(a1,...,an). Weighted Rolle gives at
least N-1 derivative weights from any finite selection of N weights
of g.

If a0 and a1 have opposite signs, V(a0,...,an)=1+V(a1,...,an),
and this is sufficient. If their signs agree and g has a first
selected positive zero x1, multiply g by -1 if needed so a0,a1>0.
Near zero, g>0 and g'>0. Choose a sufficiently small epsilon<x1.
The initial increase followed by g(x1)=0 supplies, by the mean value
theorem, a point with negative derivative before x1. Continuity of
g' supplies an additional derivative zero before x1. It is distinct
from the N-1 internal and inherited-multiplicity Rolle weights.
Thus g' has at least N weights and V(a0,...,an)=V(a1,...,an) pays
them. The same argument works for any finite selection of roots;
the finite bound excludes infinitely many roots. The one-term
base case has no roots. This proves the lemma for arbitrary real
exponents without citing an external theorem.

## The actual curve has a global power upper tangent

The native entropy chart is

J=[P log(1-P theta)-log theta+Q log(r-Q theta)
   -(P+Q-1)log(1+r-(P+Q-1)theta)]/(P+Q-1),

0<theta<min(1/P,r/Q), with Jtheta<0. At every finite C there is one
actual graph thetaC(r), r>0. The square
identity proves strict geometric log concavity:

etaC=r thetaC'/thetaC, etaC'<0 on all r>0.                       (2)

Thus at every c>0, with v=etaC(c) and
a=thetaC(c)/c^v, strict concavity in log r gives

thetaC(r)<a r^v for every r!=c.                                (3)

Let alpha=(Q-1)/P, beta=Q/(P-1). The actual thetaC has its unique
maximum at beta, and thetaC/r its unique maximum at alpha. Hence

0<etaC(c)<1 whenever alpha<c<beta.                              (4)

The unconditional native source chord comparison
gives directional height barriers: every physical central source
height at c>=beta exceeds every physical right-outer height; every
physical central source height at c<=alpha exceeds every physical
left-outer height. These include the two threshold equalities.

## A central stationary height cannot lie below both outer maxima

The central entropy tends to plus infinity at both middle-zero
endpoints, so its finite global minimum is attained at an interior
point c. Set C=J(c,theta0(c))=mC.

If c<=alpha or c>=beta, the directional height barrier just stated
already gives C>ML or C>MR respectively, proving (1).

Now suppose alpha<c<beta. At c, the source and actual values match.
Since Jsource'(c)=0 and Jtheta<0, implicit differentiation also gives
theta0'(c)=thetaC'(c). The power tangent in (3), with v in (0,1),
therefore satisfies

theta0(c)=a c^v, theta0'(c)=a v c^(v-1).                        (5)

Assume for contradiction that C<=ML and C<=MR. Choose one maximizer
gL,gR on each physical exterior component. Since entropy decreases
strictly with theta,

theta0(gi)<=thetaC(gi)<a gi^v, i=L,R.                           (6)

The second inequality is strict even if C equals an outer maximum.
These are two strict negative points of theta0-a r^v.

Use the entire formal exterior wall sectors for the endpoint signs.
On the left, theta0(0)=c0/[Q(Q-1)]>0 while a r^v tends to zero,
and theta0 tends to plus infinity as r increases to eta. On the
right, theta0 tends to plus infinity as r decreases to xi, and
theta0 is asymptotic to [c3/(P(P-1))]r, which dominates a r^v
as r tends to infinity since v<1. Therefore each negative point
in (6) forces two distinct exterior zeros of theta0-a r^v.
Equation (5) supplies a central zero of multiplicity at least two.

Away from the walls, multiplying by H preserves zero orders. All
these zeros are zeros of the analytic generalized polynomial

Fv(r)=R-r-r²-a H r^v.

Its ordered exponents and coefficient signs are

| Exponent | Coefficient | Sign |
|---|---|---|
| 0 | c0 | + |
| v | -a Q(Q-1) | - |
| 1 | c1-1 | arbitrary |
| v+1 | 2aPQ | + |
| 2 | c2-1 | arbitrary |
| v+2 | -a P(P-1) | - |
| 3 | c3 | + |

They are strictly ordered because 0<v<1. After zero coefficients
are deleted, this sequence has exactly four sign changes, regardless
of the two arbitrary signs. The generalized Descartes lemma permits
at most four positive root weights. The four exterior zeros and the
central zero of weight at least two supply at least six, a contradiction.
This proves (1).

The same argument applies to every physical central stationary
source point: its height exceeds at least one of the two outer
maxima. Only the global-minimum consequence is needed here.

## Common entropy and the remaining contact payments

Every occupied central entropy level C satisfies C>=mC. By (1),
one outer maximum is strictly below mC and therefore below C.
That outer component is empty at this same C. This is a uniform
common-level result, rather than a comparison of independently
chosen entropy curves.

For antichain strong forks, the canonical
forcing budget Ncur<=5+3-2 gives six normal-curvature weights.
Two weighted normal-boundary Rolle payments give original eight,
including nonregular source edges and multiple original contacts.
