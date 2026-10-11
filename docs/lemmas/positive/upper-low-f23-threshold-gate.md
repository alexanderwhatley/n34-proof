# The nonnegative C2-slope branch cannot alternate through C3

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Let P>1,0<Q<1,k>0,l>1,0<a<b<xi be in the native compact upper-low band. Assume only the derivative bound k<(1+2a)/[(b-a)(a+l)]. Let C_i be the projective forcing coefficients and write

C_i/[kdP(P-1)]=A_i+kD_i,
A_i=LinNi/Gamma, Gamma=(xi+h)^2,
d=b-a,L=a+l,M=b+l,
x=(a+h)(xi-a),y=(b+h)(xi-b),q=x+y+d^2,
R2=L^2q-6LMx,R3=L^2y-M^2x,R4=6LMy-M^2q,
D2=(d^2/2)R2,D3=2d^2R3,D4=(d^2/2)R4.

**The pattern C2>0,C3<=0,C4>0 is impossible when D2>=0.** No positivity of the coefficients of R or forcing endpoint phase enters this coefficient-only theorem beyond the explicitly assumed derivative bound.

## The exact determinant certificate

Set

Eraw=[3LM LinN3-2M^2 LinN2-2L^2 LinN4]/d,
F=LinN3/d,
F23raw=[4 LinN2 R3-LinN3 R2]/d.

Use the shifted cubic F=f3X^3+f2X^2-f1X+f0 with X=xi+h. The finite integer certificate proves

-H*F23raw
 =P_E*(-Eraw)+P_F*(-F)+P_2*R2
    +P_3*(-f3)+P_d*(-F')+P_dd*(-F'')+Rpos,

where H and every P have nonnegative monomial coefficients, H is strictly positive, and Rpos has 1,829 strictly positive monomial coefficients. There are 189 positive integer weights. The variables are a,d,c=xi-b,h,z=l-1, all strictly positive. H has exactly three positive monomials a,d,h. Therefore, whenever Eraw<0,F<0,R2>=0,f3<0,F'<0,F''<0, this exact identity gives F23raw<0.

## Why the actual alternating pattern is excluded

The exact quadratic identity

12LM R3-2M^2R2-2L^2R4=0

shows that the normalized middle combination

3LM*C3-2M^2*C2-2L^2*C4

is independent of k after division by the positive normalization kdP(P-1). Consequently C2>0,C3<=0,C4>0 implies Eraw<0.

As D3>0 and A3<0, define the positive zero scale k3=-A3/D3. The condition C3<=0 gives k<=k3. If D2>=0, the second coefficient is nondecreasing with k, so

A2+kD2<=A2+k3D2=(A2D3-A3D2)/D3.

But

A2D3-A3D2=[d^3/(2Gamma)]*F23raw<0.

Hence C2<0, contradicting C2>0. This includes both C3=0 and D2=0 boundaries.
