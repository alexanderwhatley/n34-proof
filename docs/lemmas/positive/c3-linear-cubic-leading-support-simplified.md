# Short proof of the linear-cubic leading support inequality

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

In the native upper-low domain, let A=a+h,B=b+h,S=A+B,T=AB,s=l-h,X=xi+h,e=1-2h,J=2h(1-h),d=b-a, as in the C3 support theorem. Write

LinN3=dF(X),
F=f3 X^3+f2 X^2-f1 X+f0,
f3=4S(T-es)+J(2s-S),
f2=4e(sS^2+2ST+2sT)+2T(sS-2T)+J(S^2+sS+2T),
f1=6eT(2T+sS)+3J(3ST+sS^2+2sT),
f0=6JT(2T+sS).

**D3>0 and LinN3<=0 force f3<0**, where D3=2d^3[(s^2-T)X-s(2T+sS)] is the quadratic scale slope.

Indeed, D3>0 gives u=s^2-T>0 and X>X0=s(2T+sS)/u. Set v=S^2-4T>0. Since s>sqrt(T) and S>=2sqrt(T), we have sS>2T and hence f2>0.

u[f1X0-2f0]
 =3(2T+sS){2eTs(2T+sS)
     +J[3sST+s^2v+2s^2T+4T^2]}

has a strictly positive right side. The second elementary identity is

F'(X0)-2F(X0)/X0=f3X0^2+f1-2f0/X0.

If f3>=0, these two identities give F'(X0)>0. Since F''(X)=6f3X+2f2>0 for X>0, F increases strictly after X0. Thus F(X)>0 for X>X0, contradicting LinN3=dF(X)<=0. Therefore f3<0.

Under the derivative bound k<(1+2a)/[(b-a)(a+l)], the coefficient-only C3 support theorem gives C3<=0=>D3>0. The normalized coefficient is

C3/[kdP(P-1)]=LinN3/(xi+h)^2+kD3.

Consequently C3<=0 and kD3>0 imply LinN3<0; the preceding result gives **C3<=0=>f3<0**. This includes the original positive-source setting, whose positive coefficients imply the derivative bound.

dependencies:
