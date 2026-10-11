# Eight original weights for every positive strong fork with two low walls

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

B=r(1+r), H=P(P-1)r^2-2PQ r+Q(Q-1),
R=(d1+r d3)(a1+r a3)(b1+r b3)/gamma^2, Y=R-B,

and write eta<xi for the roots of H. If both wall ratios are at most one,
then every actual positive coefficient tuple and level has at most **EIGHT
original intersections counted with analytic multiplicity**. There is no
ordering or degree inequality. In the strict case Y(eta),Y(xi)>0, normal-curvature
weight is at most SIX. Unit-wall cases use the general positive-outer unit-wall theorem.

The proof below actually permits any strictly positive-coefficient cubic R
for its source geometry and curvature bounds. The geometric source is needed
to interpret those curvature contacts and apply the original normal-Rolle
transfer. No antichain forcing-five theorem, physical seam-component
classification, nongeneric edge contribution to the root count, or perturbation is used.

## Two actual entropy facts and two source orders

At one common finite entropy the actual graph uC(r) is analytic on all r>0,
0<uC<min(1/P,r/Q), and has positive ODE denominator B+H uC. It obeys

uC'=uC(1-PuC)[Q-(P-1)r]/(B+H uC).

Its native elasticity etaC=r uC'/uC is strictly decreasing: the square identity is

etaC'=-(1-PuC)(r-QuC)
 [uC(H+(P+Q-1)r)^2+(P+Q-1)r^2(1+r-(P+Q-1)uC)]
 /(B+H uC)^3<0.

Thus log(uC(e^x)) is strictly concave. The native graph uC has its unique
maximum at beta=Q/(P-1); the reflected graph uC/r has its unique maximum at
alpha=(Q-1)/P, with eta<alpha<beta<xi. Consequently etaC(alpha)=1 and
etaC(beta)=0.

For strict low walls the source seam u0=Y/H has the residue representation

u0=ell0+m r-V/(r-eta)+U/(r-xi), m,U,V>0.

For every central c and right exterior g,

(u0(g)-u0(c))/(g-c)
 =m+V/[(g-eta)(c-eta)]+U/[(g-xi)(xi-c)]>0.

Reflection gives the corresponding native reflected order:
every left exterior value u0(g)/g exceeds every central u0(c)/c.
Neither source order needs a physical source probability or an antichain.

## A common actual level cannot occupy all three wall intervals

Suppose, for contradiction, that this one actual curve has a source contact
on each exterior and a central contact at c. The two source orders localize
this actual contact strictly to alpha<c<beta. If c>=beta, the occupied right
exterior point g has

u0(g)>u0(c)=uC(c)>uC(g)=u0(g),

a contradiction. If c<=alpha, the same contradiction follows after division
by r using the occupied left exterior point and the maximum of uC/r.
Thus e=etaC(c) satisfies 0<e<1.

Define the tangent power a r^e with a=uC(c)/c^e=u0(c)/c^e>0. Strict geometric
log concavity gives

uC(r)<a r^e for every r!=c.

Therefore u0-a r^e is strictly negative at both occupied exterior contact
points. On each exterior it is positive near both formal ends: u0(0)>0
while a r^e tends to zero; u0 tends to plus infinity at both exterior walls;
and at infinity u0 is asymptotic to m r whereas e<1. The intermediate value
theorem supplies two distinct roots on each exterior, four roots in all.
The actual central contact c supplies one further root. No source tangency,
source-height extremum, or physical source component is used.

Multiplying by H preserves all five weights away from the walls. But the
resulting generalized polynomial is

G(r)=R(r)-r(1+r)-a H(r)r^e.

Its ordered exponents and coefficient signs are

0: +, e: -, 1: arbitrary, 1+e: +,
2: arbitrary, 2+e: -, 3: +.

There are at most FOUR sign variations after zero coefficients are omitted,
so generalized Descartes gives at most four positive zero weights. This
contradicts the five weights just obtained. The common level must leave at
least one of the three wall intervals empty.

For completeness, the generalized Descartes rule here follows by weighted
Rolle induction. Divide a real-power sum by its smallest power and
differentiate. If its first two nonzero coefficients have opposite signs,
ordinary weighted Rolle costs one root, exactly the extra sign variation.
If they have the same sign, the function and derivative initially have that
same sign near zero; reaching the first zero requires an extra derivative
zero before it, so Rolle costs none. Induction bounds positive zero weight
by the coefficient sign variations. Real powers are analytic on r>0, and
the positive leading source term prevents G from being identically zero.

## Curvature budget when a central contact exists

If the central interval is occupied, the no-three-interval theorem empties
at least one exterior. Thus curvature weight is at most four centrally plus
two on the other exterior, namely SIX.

## Curvature budget when no central contact exists

The nonzero forcing polynomial

W=R(HY'-H'Y)-Y(H-PY)[Q-(P-1)r]

has degree at most six, by the universal projective coefficient identity.
At a wall its exact value is

W(w)=-H'(w)Y(w)[3R(w)-B(w)]/2.

Strict low walls have R(w)>B(w)>0, so W(eta)>0 and W(xi)<0. Hence at least
one central W root consumes one of its six possible root weights, and the
two exterior intervals together have at most five W root weights.

The formal-ODE source comparison is valid on each whole exterior interval,
including nonphysical source values, because B+H u0=R>0. Its positive
integrating factor gives exterior contact weight at most five plus one
Rolle contribution to the root count per exterior, namely seven. On each exterior the actual-source
difference is negative near both ends: source values are positive finite at
zero, diverge at the adjacent wall, and grow linearly at infinity. Its total
root weight is even. Thus the two exterior contact weights sum to an even
number at most seven, hence at most SIX. This argument covers every possible
source edge and negative source band without a separate component classification.

## Original intersections and weak low walls

In either case there are at most six normal-curvature weights; no wall
contacts occur under strict low signs. The two weighted
normal-boundary Rolle stages give at most eight original weights for every
actual positive coefficient tuple and level.

If a low wall is unit, the general positive-outer
unit-wall theorem gives original eight directly (six when both walls are
unit). It includes comparable supports and arbitrary multiplicities. Thus
the printed at-most-one wall-ratio scope follows without a limiting-root
argument.
