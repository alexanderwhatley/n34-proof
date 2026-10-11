# The negative middle linear part lies on a decreasing concave cubic tail

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Use the native upper-low shifted notation A=a+h,B=b+h,S=A+B,T=AB,s=l-h,X=xi+h,e=1-2h,J=2h(1-h),d=b-a, and LinN3=dF(X), where

F=f3X^3+f2X^2-f1X+f0,
f3=4S(T-es)+J(2s-S),
f2=4e(sS^2+2ST+2sT)+2T(sS-2T)+J(S^2+sS+2T),
f1=6eT(2T+sS)+3J(3ST+sS^2+2sT),
f0=6JT(2T+sS).

**If D3>0 and LinN3<=0, then F'(X)<0 and F''(X)<0**, where D3=2d^3[(s^2-T)X-s(2T+sS)]. Under the derivative bound k<(1+2a)/[(b-a)(a+l)], this applies whenever C3<=0 by the slope support theorem.

## The boundary inequalities

D3>0 gives u=s^2-T>0 and X>X0=s(2T+sS)/u. Set v=S^2-4T>0. The zero-slope certificate gives F(X0)>0, and the linear leading support inequality gives f3<0 when LinN3<=0 on D3>0. Also f2>0 because sS>2T.

The first elementary identity is

u[f1X0-3f0]
 =3(2T+sS){2eTs(2T+sS)+J[3sST+s^2v+6T^2]}>0.

The second, valid at every positive z, is

F(z)=(2z/3)F'(z)-(z^2/6)F''(z)+f0-(z/3)f1.

At z=X0, the simultaneous inequalities F'(X0)<=0 and F''(X0)>=0 would therefore give F(X0)<0. They are impossible. Thus either F'(X0)>0, or F''(X0)<0.

## No interior minimum and the negative tail

Because f3<0, F''(z)=6f3z+2f2 decreases strictly and F'(z) is a concave quadratic with negative constant term -f1.

If F'(X0)<=0, the preceding boundary argument forces F''(X0)<0. Both F'' and F' are then strictly negative for z>X0, so F decreases throughout this tail.

If F'(X0)>0, the positive region of the concave quadratic F' is one bounded interval. After X0, F' remains positive until its unique later zero, then becomes strictly negative. At that zero F''<0, and F'' stays negative afterwards. Hence F first increases from its positive boundary value, then decreases. In either case there is no interior minimum after X0.

Since the actual point has X>X0 and F(X)=LinN3/d<=0, it must belong to the final strictly decreasing segment. Both F'(X)<0 and F''(X)<0 follow. In polynomial form these necessary restrictions are

3f3X^2+2f2X-f1<0,
3f3X+f2<0.

For C3<=0, the derivative-bound support gives D3>0. Since C3/[kdP(P-1)]=LinN3/(xi+h)^2+kD3 and kD3>0, one has LinN3<0, and the same strict derivative restrictions hold.
