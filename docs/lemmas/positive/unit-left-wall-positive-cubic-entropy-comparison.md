# A universal unit-left-wall entropy comparison for positive source cubics

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Statement

Let P,Q>1, H=P(P-1)r²-2PQr+Q(Q-1), and let eta<xi be its two positive roots. Let R(r)=c0+c1 r+c2 r²+c3 r³ be a nonzero polynomial with nonnegative coefficients. Suppose

R(eta)=eta(eta+1), R(xi)<=xi(xi+1).

Set B=r(r+1), u0=(R-B)/H and

F(r,u)=u(1-Pu)[Q-(P-1)r]/[B+Hu].

Then for every 0<r<eta,

**u0'(r)-F(r,u0(r))<=0, with equality only when R=B.**

In particular, for every genuine positive source cubic (c0,c3>0) the inequality is strict. It holds even where u0 does not satisfy the probability bound: the only required differential-equation denominator is B+Hu0=R>0. The statement is a source comparison, not by itself an unrestricted master contact bound.

## Convexity reduces the statement to six vertices

Put z=xi/eta>1 and t=xi(1+xi)/[eta(1+eta)]. Then z<t<z². Normalize w_i=c_i eta^i/[eta(1+eta)]. The source assumptions are exactly

w_i>=0, sum w_i=1, sum w_i z^i<=t.

This three-dimensional clipped simplex has precisely six vertices: the pure constant and pure linear vertices, and four edge intersections indexed (i,j) with i in {0,1}, j in {2,3}. At an edge intersection

w_j=(t-z^i)/(z^j-z^i), w_i=1-w_j.

Those four sources saturate both wall equalities. Since H divides R-B, their seam curves u0 are affine. Their exact descriptions are

- (0,2): u0=1/(2PQ);
- (1,2): u0=0, R=B;
- (1,3): u0=r/(2PQ);
- (0,3): u0=l0+l1 r, with Z=3PQ+P+Q-1, l0=(2P+Q-1)/(PZ), l1=(P+2Q-1)/(QZ).

Fix r in (0,eta). Write j=Q-(P-1)r>0. The ODE nonlinearity has exact second derivative

F_uu=-2j B(PB+H)/(B+Hu)^3<0 on u>-B/H,

because PB+H=(Pr-Q)(Pr-Q+1)>0 when r<eta<(Q-1)/P. Both u0 and u0' are affine functions of the source weights w_i. Thus Phi=u0'-F(r,u0) is a convex function on this entire compact source polytope. All denominators remain strictly positive: R(r)>0 at every nonzero nonnegative-coefficient source.

It is enough to show Phi<=0 at the six vertices. The (1,2) vertex gives equality. At (0,2), u0'=0 while F>0, so Phi<0. At (1,3), 0<Qu0/r=1/(2P)<1, and the exact radial ODE identity

F(r,u)/r-u/r²=(u/r)(1-Qu/r)(Q-1-Pr)/[r(1+r+Hu/r)]

is positive. Hence F>u/r=u0' and Phi<0. The remaining three vertex signs have the coefficient-positive certificates below. Since every source is a convex combination of vertices, Phi<=0. If R!=B, any such representation uses at least one of the other five vertices, giving a strict negative convex upper bound.

## Exact coefficient-positive certificates for the remaining three vertices

Use the rational wall parameterization

S=eta+xi, W=2 eta xi+S, Delta=xi-eta,
P=S(S+2)/Delta², Q=S W/Delta².

Every pair 0<eta<xi gives P,Q>1 and these roots of H; conversely the formulas follow from the sum and product of the roots. Set a=eta-r>0, b=xi-eta>0, so eta=r+a, xi=r+a+b. Put PN=S(S+2), QN=S W, D=b². For any source define Y=R-B and the exact forcing numerator

T=R(Y'H-YH')-Y(H-PY)j,

so Phi=T/(H²R). For the pure constant source R=eta(1+eta), and pure linear source R=(1+eta)r, exact polynomial identities give

b⁶ Tconstant=-a² PN W Cconstant(r,a,b),
b⁶ Tlinear=-a² r PN W Clinear(r,a,b).

The constant and linear vertex signs, and the other vertex signs, have direct analytical proofs in [the vertex simplification](unit-left-wall-analytical-vertex-simplification.md). Those proofs supply the same strict forcing inequalities without a coefficient table.

For the affine (0,3) vertex, clearing Phi's denominator P Q Z² gives N03(P,Q,r). After the same wall substitution,

b¹⁰ N03=-4 S(S+2)² W² C03(r,a,b),

where the same coefficient table defines C03 with **78 strictly positive integer coefficients**. All cleared denominators and prefactors are positive, proving the third strict negative sign.

## Limits and source dependencies

This comparison uses the fixed-wall entropy ODE but imposes no common entropy-level restriction: it applies directly to every formal seam in the specified unit-wall source polytope. The high-high extension requires a separate scale/normalization argument. No mixed-wall, low-wall, or general asymmetric conclusion is included here.
