# Upper-low C3 quadratic-slope support theorem

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Statement

Let P>1,0<Q<1,p=P-1,

H=Pp(r+h)(r-xi), B0=r(1+r), j=Q-pr,
Y=k(r+l)(r-a)(r-b), R=B0+Y,

where k>0,l>1,0<a<b<xi and every coefficient of R is strictly positive. Let C_i be the ascending coefficients of the degree-six central-band forcing

(1+v)^6 W((a+bv)/(1+v)),
W=B0(Y'H-YH')-jYH+Y(Y'H+3PYj).

Normalize as in the compact band operator. For d=b-a,L=a+l,M=b+l,gamma=Pp, define

x=(a+h)(xi-a), y=(b+h)(xi-b), Gamma=(xi+h)^2,
A3=LinN3/Gamma, D3=2d^2(L^2 y-M^2 x).

Then C3/(kd gamma)=A3+kD3.

**If D3<=0, then C3>0. Consequently C3<=0 forces D3>0.** No endpoint-forcing phase condition such as w6>0 is needed. The coefficient positivity of R is used through the elementary condition R'(a)>0.

This is a slope-support theorem. It does not alone prove the complete upper-low three-variation ceiling or the remaining four-sign exclusion.

## Source ceiling and the cubic to study

Because R has positive coefficients and a>0,

R'(a)=1+2a-kLd>0.

Hence

kd^2L<d(1+2a)<G, G=a+b+2ab,

where G-d(1+2a)=2a(1+a)>0. Thus k<G/(d^2L).

When D3<0 the normalized middle coefficient is strictly larger than its value at this ceiling; when D3=0 its value is independent of k. It therefore suffices to prove

Zraw=L LinN3+2 Gamma G(L^2 y-M^2 x)>0.  (1)

Introduce shifted variables

A=a+h, B=b+h, S=A+B, T=AB,
s=l-h, X=xi+h, e=1-2h, tH=2h(1-h).

The actual wall-root relations imply

0<h<1/2, e>0,
Phi=(1-2h)X-2h(1-h)>0,
X>Xnative=tH/e, X>B.

Also s>1-h,S>2h,0<T<S^2/4. Exact compact-operator expansion gives LinN3=d F(X), where

F=f3 X^3+f2 X^2-f1 X+f0,
f3=4S(T-es)+tH(2s-S),
f2=4e(sS^2+2ST+2sT)+2sST-4T^2+tH(S^2+sS+2T),
f1=6eT(2T+sS)+3tH(3ST+sS^2+2sT)>0,
f0=6tH T(2T+sS)>0.

Furthermore

L^2 y-M^2 x=d[(s^2-T)X-s(2T+sS)].  (2)

Consequently Zraw=d P(X), with the cubic

P(X)=L F(X)+2G X^2[(s^2-T)X-s(2T+sS)],
P=K3 X^3+K2 X^2+K1 X+K0,
K3=L f3+2G(s^2-T),
K2=L f2-2G s(2T+sS),
K1=-L f1<0, K0=L f0>0.

## The native-clipped support interval

Let Xlo=max(B,Xnative). If T<s^2, the condition D3<=0 is exactly

X<=X0=s(2T+sS)/(s^2-T).

The relevant interval is therefore [Xlo,X0], with the actual point satisfying X>Xlo. If X0<=Xlo there is no actual point to consider. If T>=s^2, the bracket in (2) is strictly negative for every X>0, and the support interval is [Xlo,infinity).

The integrated proof treats both finite and unbounded intervals, the native clipping, the zero slope upper boundary, and the junction B=Xnative.

## Positivity at the endpoints

- At X=B, equivalently xi=b, for 0<h<=b/(1+2b):406 positive coefficients. The weak equality is certified by the strictly positive leading q^3 block of its wall chart.
- At X=Xnative>B, equivalently Phi=0 with 0<a<b<xi:950 positive coefficients. Its xi derivative is also strictly positive, certified by727 positive coefficients. Since d is fixed, this gives P'(Xnative)>0.

At a finite upper endpoint X0, D3=0. The auxiliary boundary lemma proves A3>0. Thus the source-slope term vanishes, and

P(X0)=L LinN3/d>0.

That lemma uses an exact quadratic Bernstein certificate in T on [0,min(s^2,S^2/4)]. Five positive coefficient lifts contain118,125,123,336,335 monomials. The exact identity and all chart coverage are in the auxiliary proof.

## No interior minimum after the lower endpoint

I1=P'(B)-(d/4)P''(B)>0,
I2=B K3+K2>0.

Their positive charts contain430 and327 monomials. Their q^3 leading blocks contain111 and83 positive monomials, so both strict inequalities extend to h=b/(1+2b). This includes B=Xnative.

If K3>=0, then P''(B)=2I2+4BK3>0 and P'(B)>0. Since P'' is nondecreasing, P increases for all X>=B. If K3<0 and P'(B)<0, I1>0 gives P''(B)<0. Now P'' decreases, so P' stays negative and P decreases throughout. If K3<0 and P'(B)>=0, the derivative is a concave quadratic with strictly negative constant K1. Its nonnegative region is one interval, so after B it can only remain nonnegative and then become negative. P increases and then decreases, allowing no interior minimum below the endpoints.

For a finite support interval, the positive endpoint values therefore imply P(X)>0 throughout [Xlo,X0].

## The unbounded case

Let t=l-1>0. The exact leading-coefficient decomposition is

K3=(T-s^2)(4LS-2G)
   +L[S(tH+4t(1+t))+2s*tH],
4LS-2G=2[2a^2+(2l-1)(a+b)+4h(a+l)]>0.

This proves (1) whenever D3<=0. Restoring the strict source ceiling proves C3>0, as asserted.

## Mathematical inputs

The [auxiliary polynomial lemmas](c3-slope-support-auxiliary-lemmas.md) give the zero-slope and cubic-shape statements, and the [native endpoint lemma](c3-native-lower-endpoint-and-derivative-lemmas.md) gives the endpoint signs. The conclusion here is the sign of the third forcing coefficient under the displayed assumptions. The [one-wall master theorem](one-wall-positive-master.md) combines that sign with its other coefficient inequalities and the exterior count.
