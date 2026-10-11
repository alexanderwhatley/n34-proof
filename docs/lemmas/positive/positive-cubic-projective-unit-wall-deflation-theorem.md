# Unit-wall deflation for every positive cubic source

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Statement

Fix P,Q>1 and let H=P(P-1)r²-2PQr+Q(Q-1) have roots eta<xi.
Let R be any cubic with all four coefficients strictly positive,
B=r(1+r), Y=R-B, and let uC be one actual fixed-entropy graph.

If Y vanishes at at least one of eta,xi, then

A(r)=B+H uC-R

has at most SIX positive zeros counting analytic multiplicity.
If Y vanishes at both walls, this improves to FOUR. The result does
not require a geometric metric, negative real roots of R, coordinate
antichain, source bounds, other-wall sign, or regularity of contact
orders. For a geometric positive strong fork, the two normal-Rolle
payments give original ceilings eight or six respectively.

## Analytic quotient and forced double factors

Let h be the product of the q unit-wall factors, q=1 or 2, and write

H=h Hbar, Y=h Ybar.

All H roots are simple. Thus u0=Ybar/Hbar is analytic through every
unit wall; if q=1 its only remaining possible pole is the other
nonunit wall. Its formal ODE denominator remains

B+H u0=R>0.

Put j=Q-(P-1)r and f(r,u)=j u(1-Pu)/(B+Hu). The source forcing is

W=R(HY'-H'Y)-Y(H-PY)j
 =h² [R(Hbar Ybar'-Hbar'Ybar)-Ybar(Hbar-PYbar)j].                (1)

Equivalently, W=H²R(u0'-f(r,u0)). The bracket is analytic through
every unit wall. Consequently W has a double polynomial factor
there, including when an actual curvature contact has higher order.
The universal forcing degree is at most six: both terms have degree at
most seven, and their degree-seven coefficients P(P-1)c3² cancel.
Write W=h²F; then

deg F<=6-2q.                                                   (2)

These statements hold simultaneously at both walls when q=2.

## Regular actual/source comparison

For D=uC-u0 the exact subtraction identity is

D'=L(r)D-W/(H²R),
L=j[B(1-P(uC+u0))-PH uC u0]/[(B+H uC)R].

The actual and formal-source denominators are positive. The coefficient
L is analytic through each unit wall, including at actual contacts.
Since W/(H²R)=F/(Hbar²R), a positive integrating factor makes D's
derivative a nonvanishing analytic multiplier of F on each connected
interval left after the nonunit walls are removed.

If q=1, there are two such intervals. Weighted Rolle bounds the total
D root weight by Z(F)+2<=6. There is no contact at the remaining
nonunit wall: there A=-Y is nonzero. Restoring the one mandatory
factor h in

A=H D=h Hbar D

therefore gives at most seven A weights, including the full additional
weight at a unit wall where D itself vanishes.

If q=2, Hbar is a positive constant and the comparison is regular on
all r>0. Weighted Rolle gives Z(D)<=Z(F)+1<=3. Restoring the two
mandatory factors gives at most five A weights.

Both counts are finite because the same bound applies to every finite
selection of zeros. There is no perturbation of multiple roots.

## Endpoint parity and zero forcing

The actual curve has uC asymptotic to a positive multiple of r^Q
at zero, and a positive multiple of r^(1-P) at infinity. Hence
B+H uC tends to zero at zero and grows at most quadratically at
infinity. The positive constant and cubic coefficients of R imply
A<0 near both endpoints.

Its finite total positive root weight is therefore even. The one-unit
bound seven improves to six; the two-unit bound five improves to four.

If F is identically zero, the integrating-factor comparison is
homogeneous and no polynomial root count is used. With one unit wall,
D is nowhere zero on each side of the remaining wall: identically
zero on either side would imply A identically zero there and, by
analyticity, throughout r>0, contradicting its negative endpoint
phase. With both unit walls, the same argument applies globally.
Thus D contributes no zeros in this case, and the mandatory q wall
weights satisfy the stated ceilings.

This abstract projective proof removes the normal-coordinate variance,
wall-residue and source-component interfaces from the unit contribution to the root count.
It uses only the entropy ODE, its endpoint asymptotics,
the generic degree-six forcing identity and weighted Rolle.
All positivity and multiplicity arguments are analytical.
