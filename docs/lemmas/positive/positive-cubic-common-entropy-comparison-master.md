# A positive-cubic common-entropy comparison master

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Fix P,Q>1 and K=P+Q-1. For any finite C, let u_C(r), r>0, be the unique physical graph

J(r,u)=[P log(1-Pu)-log u+Q log(r-Qu)-K log(1+r-Ku)]/K=C,

0<u<min(1/P,r/Q).

Put B=r(1+r), H=P(P-1)r²-2PQr+Q(Q-1), with roots 0<eta<xi. Let R=R0+R1 r+R2 r²+R3 r³ have all four coefficients strictly positive, and put Y=R-B.

**Theorem.** A=B+H u_C-R has at most SIX positive zeros counting analytic multiplicity. If Y(eta)<=0 and Y(xi)<=0, the ceiling is FOUR. These bounds hold for one fixed finite C, without genericity, simple-contact, physical source-bound, geometric metric, real-root factorization, coordinate order, degree order or residue-margin assumptions.

## Common analytic interface

The graph exists globally because J_u<0 and the two endpoint limits at each fixed r are opposite infinities. Its ODE is u_C'=j u_C(1-Pu_C)/(B+H u_C), j=Q-(P-1)r, with positive denominator. The native elasticity identity proves strict concavity of log u_C(e^x). Its endpoint asymptotics are positive multiples of r^Q and r^(1-P), respectively. Every fact here depends only on P,Q,C.

The source u0=Y/H has B+H u0=R>0 wherever defined. On any whole nonunit wall interval, D=u_C-u0 satisfies the analytic comparison

D'=aD-W/(H²R),

W=R(HY'-H'Y)-Y(H-PY)j,

a=j[B(1-P(u_C+u0))-PH u_C u0]/[(B+H u_C)R].

The secant coefficient is analytic at every contact and every nonphysical source value. Weighted integrating-factor Rolle therefore gives Z_I(D)<=Z_I(W)+1. The degree-seven coefficients cancel, so deg W<=6. No geometric support enters this interface.

## Exhaustive proof in four wall patterns

1. **Both walls strictly high, Y<0.** The six-vertex source-coefficient comparison and convex source-scale interpolation use only R_i>0. Each exterior has one simple contact and the central interval has at most two weights: Z(A)<=4. The direct unit transversality closes this conclusion to Y<=0 at both walls, preserving the full multiplicity of mandatory and matching residual wall factors.

2. **Opposite strict signs.** The mixed exterior argument uses only the signs of the source residues and the actual entropy graph. The low exterior has at most two weights, the high exterior one. The positive-cubic mixed addendum replaces negative-root factorization by two coefficient inequalities and a four-term positive decomposition of C2+C4. The central forcing has at most three variations, and opposite endpoint phases lower its four-weight Rolle contribution to the root count to three. Total: 2+3+1=6. Reflection covers the other orientation.

3. **Both walls strictly low, Y>0.** The full low proof explicitly permits arbitrary positive-coefficient cubics. Its source-order identities use the positive leading coefficient and opposite wall residues. If a central contact exists, Y is negative there, positive at both walls, and has positive constant and leading coefficients. Hence Y automatically has two simple roots inside the central interval and one negative root; the resulting exterior elasticity proof requires no negative-root factorization of R. The generalized Descartes power-tangent argument forbids contacts in all three wall intervals. Central four and exterior two give six. With no central contact, opposite forcing wall signs consume one central forcing root; two exterior Rolle payments give seven, lowered to six by equal negative endpoint phases.

## Geometric corollary and limits

For positive strong-fork supports s2=P s1+Q s3, with distinct-mode outer supports oriented by gamma=a3 b1-a1 b3>0, the geometric cubic

R=(d1+rd3)(a1+ra3)(b1+rb3)/gamma²
