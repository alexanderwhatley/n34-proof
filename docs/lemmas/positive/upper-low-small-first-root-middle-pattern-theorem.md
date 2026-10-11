# Small first source root excludes the remaining upper-low middle pattern

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Let P>1,0<Q<1,k>0,l>1,0<a<b<xi be in the native upper-low band. Assume the derivative bound k<(1+2a)/[(b-a)(a+l)].

**If a<1/7 or a<2h, the coefficient pattern C2>0,C3<=0,C4>0 is impossible.**

This is a coefficient-only theorem; positive coefficients of R imply the derivative bound but are not otherwise required here. It includes the C3=0 and D2=0 boundaries. It is sufficient for the genuine geometric upper-low residue because its C1<=0 localization gives a<1/7. The counting and original-geometry transfers are separate composition steps.

## Notation and the exact recurrence

Use d=b-a,L=a+l,M=b+l,Gamma=(xi+h)^2. Let Ni=LinNi be the compact-band linear coefficient numerators, and set

x=(a+h)(xi-a),y=(b+h)(xi-b),q=x+y+d^2,
R2=L^2q-6LMx,R3=L^2y-M^2x,R4=6LMy-M^2q,
A_i=Ni/Gamma,D2=(d^2/2)R2,D3=2d^2R3,D4=(d^2/2)R4.

Thus C_i/[kdP(P-1)]=A_i+kD_i. Define

F=LinN3/d,
E=[3LM N3-2M^2N2-2L^2N4]/d,
F23=[4N2R3-N3R2]/d,
F24=[N2R4-N4R2]/d.

The compact quadratic operator gives

12LMR3-2M^2R2-2L^2R4=0,
2L^2F24=3LMF23+E R2.  (1)

## Reusing the exact first determinant certificate

The natural-cofactor integer certificate gives the polynomial identity

-H F23=PE*(-E)+P2*R2+sum Pg*Gg+Rpos,

where H is a positive integer constant times S=a+b+2h, every P has nonnegative monomial coefficients, and Rpos has 1,828 strictly positive coefficients. The remaining four inequalities Gg are -F,-f3,-F',-F'', using the shifted cubic F(X),X=xi+h. The identity has 184 positive integer weights and is an identity for all polynomial variables. Its reuse does not assume R2>=0.

Multiplying by 3LM and applying (1) gives

-2L^2H F24=AE*(-E)+sum (3LM Pg)*Gg+RE,  (2)
AE=3LM PE+H R2,
RE=3LM(Rpos+P2 R2).

The two new polynomials AE and RE contain some negative monomial coefficients in the original variables. The following exact bounded-variable lifts prove their positivity in the stated region.

## Two complete positive charts

The native wall roots always satisfy 0<h<1/2. Put d=b-a>0,c=xi-b>0,z=l-1>0.

For 0<a<1/7 use

a=u/[7(1+u)], h=v/[2(1+v)], u,v>0.

The inverse is u=7a/(1-7a),v=2h/(1-2h), so this chart covers the whole region. Multiplication by the positive clearing factors gives:

| Polynomial | Clearing factor | Strictly positive coefficients |
|---|---|---:|
| AE | [7(1+u)]^4 [2(1+v)]^3 | 351 |
| RE | [7(1+u)]^12 [2(1+v)]^8 | 23,948 |

For 0<a<2h use

a=2h*u/(1+u), h=v/[2(1+v)], u,v>0.

Its inverse is u=a/(2h-a),v=2h/(1-2h). The positive lifts are:

| Polynomial | Clearing factor | Strictly positive coefficients |
|---|---|---:|
| AE | (1+u)^4 [2(1+v)]^5 | 495 |
| RE | (1+u)^12 [2(1+v)]^13 | 32,877 |

## The actual residual inequality and the scale contradiction

If D2>=0, the F23 threshold theorem already excludes the pattern. If D2<0, recurrence (1) gives D4>0 because R3>0. The scale cancels in

D4*(A2+kD2)-D2*(A4+kD4)
 =A2D4-A4D2=[d^3/(2Gamma)]F24<0.

But C2>0,C4>0,D4>0,D2<0 make its left side strictly positive, a contradiction. This proves the theorem.

The exact positive expansions in the two displayed charts are [first-chart AE](../../../calculation-data/positive/f24_certificate/a_lt_one_seventh-AE.json.gz), [first-chart RE](../../../calculation-data/positive/f24_certificate/a_lt_one_seventh-RE.json.gz), [second-chart AE](../../../calculation-data/positive/f24_certificate/a_lt_two_h-AE.json.gz), and [second-chart RE](../../../calculation-data/positive/f24_certificate/a_lt_two_h-RE.json.gz). Their chart substitutions and strictly positive clearing factors are the ones printed above.
