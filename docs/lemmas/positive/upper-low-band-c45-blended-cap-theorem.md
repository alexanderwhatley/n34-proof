# Upper low-band C4/C5 inequality by a blended scale ceiling

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Statement and normalization

Let P>1,0<Q<1,p=P-1 and

H=Pp(r+h)(r-xi), B=r(1+r), j=Q-pr,
Y=k(r+l)(r-a)(r-b), R=B+Y,

where k>0,0<a<b<xi,l>1, and every coefficient of R is strictly positive. Define

W=B(Y'H-YH')-jYH+Y(Y'H+3PYj).

Assume its leading coefficient w6 is strictly positive. Let C_i be the ascending coefficients of

(1+v)^6 W((a+bv)/(1+v)).

**If l<b, then C4-2C5>0.** In conjunction with the C5 support inequality (C5<0 when b<=l and l>=1), this proves

C5>=0 => C4>0

throughout the upper tail l>1. This is a coefficient inequality; it does not alone assert the complete upper-tail three-variation theorem. A separate exclusion of C2>0,C3<0,C4>0 remains necessary when C1 can be negative.

Write d=b-a,L=a+l,M=b+l,gamma=Pp,

x=(a+h)(xi-a), y=(b+h)(xi-b),
Gamma=(xi+h)^2, Phi=xi-h(1+2xi), Pnum=Gamma+2Phi.

The wall-root identities are

p=2Phi/Gamma, Q=p(xi-h)/2, P=Pnum/Gamma.

In particular Phi>0. For Kbar=-x-(x+y+d^2)v-yv^2,
f=v(L+Mv), g=(a+bv)(1+a+(1+b)v), set

O=(1+v)(f'Kbar-fKbar')-fKbar,
Jnum=(xi-h-2a)+(xi-h-2b)v,
LinN=-Gamma*g*O+d*Phi*f*Kbar*Jnum,
Quad2=d^2*f*(2f'Kbar-3fKbar').

Direct polynomial expansion gives

C_i/(k*d*gamma)=LinN_i/Gamma+(k/2)Quad2_i.

Put LE=LinN4-2LinN5 and QE2=Quad2_4-2Quad2_5. Thus

(C4-2C5)/(k*d*gamma)=E_L+k E_Q,
E_L=LE/Gamma, E_Q=QE2/2.

The displayed formula is the compact polynomial operator used in the coefficient identities.

## Positive linear term

The complete domain l>1,0<a<b<xi admits the chart

xi=a+d+c,
h=xi*q/[(1+2xi)(1+q)], l=1+t,
a,d,c,t,q>0.

## Three affine scale ceilings and their blend

Set S=a+b,T=ab and

den1=lS-T,
den2=S-l,
den3=(l-S+3Q/p)/P.

Positive R1,R2 and w6>0 respectively give

k*den1<1, k*den2<1, k*den3<1.

No positivity assumption on an individual denominator is needed. Put D3=2(l-S)+3(xi-h), so den3=D3/(2P). For i=1,2 define the integer polynomial

N_i=2Pnum*LE*den_i+3Gamma*LE*D3+4Pnum*Gamma*QE2.

The exact identity is

N_i/(8P Gamma^2)=E_L*(den_i+3den3)/4+E_Q.  (1)

We will prove N_i>0 with i chosen to maximize the two source denominators. If blend=(den_i+3den3)/4, then k*blend<1. When E_Q>=0, E_L+kE_Q>0 follows directly. When E_Q<0, positivity in (1) forces blend>0. Hence k<1/blend and

E_L+kE_Q>(E_L*blend+E_Q)/blend>0.

It remains to certify the polynomial positivity in (1).

For b=1+z,xi=b+c,h=xi*q/Hd, with Hd=(1+2xi)(1+q), define

Uunit=b^3(1+u)^3 Hd^6 N1(a=u/[b(1+u)],l=1).

The original N1 at l=1 and d=b-a has degree three in a. This clearing is exact. Uunit has5089 nonzero monomials in z,u,c,q. Let Nb be its u^3 coefficient; equivalently

Nb=b^3 Hd^6 N1(a=1/b,l=1).

The following explicit identities are certified:

Hsquare=64(b^7-1)(b-3c)^2(b+c)^10(1+q)^6,
Jquad=64 z^15 c(13z^2-27zc+51c^2),

Uunit=(1+u)^3 Hsquare+u^3 Jquad+Punit,
Nb=Hsquare+Jquad+Pboundary.

Punit has4722 nonzero strictly positive integer coefficients. Pboundary has1173. Complete coefficient lists are in UNIT_POSITIVE_RESIDUAL.json.gz and BOUNDARY_POSITIVE_RESIDUAL.json.gz.

Hsquare>=0 because b>1. Moreover

52(13z^2-27zc+51c^2)=(26z-27c)^2+1923c^2>0

for c>0. Therefore Jquad>0 when z,c>0. Consequently Nb>0 and Uunit>0 for the positive unit chart, including its weak u=0 boundary. These identities replace every negative monomial of the unit numerator by one square and one positive definite quadratic. They do not assert that the unit wall needs this inequality for the curvature proof; the direct unit deflation remains available.

## Complete bound-chart lift

Because l<b and l>1, b>1. The comparison of source denominators is

den1-den2=(S+1)(l-l0), l0=(S+T)/(S+1).

If T<1, then l0<1 and source1 dominates. If T>1, then 1<l0<b. The equality l=l0 is assigned to source1. T=1 is included in the weak source1 chart below.

Use the common variables z,u,t,c,q, with b=1+z,xi=b+c,h=xi*q/Hd. The global clearing exponents are MA=11,MH=6,ML=2. Write DA=b(1+u),d=ND/DA,a=NA/DA,l=NL/DL.

### Chart A: T<1

NA=u, ND=b^2(1+u)-u,
NL=1+bt, DL=1+t.

Here T=u/(1+u)<1 and l=(1+bt)/(1+t) ranges over1<l<b. For the cleared polynomial

UA=DA^11 Hd^6 DL^2 N1,

there is the exact identity

UA=DA^8 Uunit+PA.

PA has50050 nonzero strictly positive coefficients, all with positive t exponent. Thus UA>0.

### Chart B: T>=1 and source1

NA=1+b^2u, ND=b^2-1,
Sn=NA+b*DA, Tn=b*NA,
Fn=Sn+Tn, Fd=Sn+DA,
NL=Fn+b*t*Fd, DL=Fd(1+t).

Then T=(1+b^2u)/(1+u), l0=Fn/Fd and l=(l0+bt)/(1+t). For u>0,t>=0 this covers T>1,l0<=l<b; for u=0,t>0 it covers T=1,1<l<b. Every denominator is strictly positive. The cleared polynomial obeys

UB=DA^11 Hd^6 DL^2 N1
  =b^8(b^2+b+1)^2 Nb+PB.

PB has98406 nonzero strictly positive coefficients, each having positive u or t exponent. Thus UB>0, including the source tie t=0.

### Chart C: T>1 and source2

Use the same NA,ND,Sn,Tn,Fn,Fd as in chart B, but

NL=Fd+t*Fn, DL=Fd(1+t).

Then l=(1+l0t)/(1+t) ranges over1<l<l0 for u,t>0. The cleared polynomial obeys

UC=DA^11 Hd^6 DL^2 N2
  =b^8(b^2+b+1)^2(1+t)^2 Nb+PC.

PC has91350 nonzero strictly positive coefficients, all with positive u exponent. Thus UC>0. Its u=0 face collapses to l=1 and is only a certificate boundary, not an additional upper-tail assumption.

All clearing factors are strictly positive. The three charts cover every 0<a<b<xi,1<l<b and choose the larger source denominator. Their exact lifts prove the positivity required in (1), which proves the stated coefficient inequality.

Run

This closes the upper-low C5/C4 ordering inequality. It does not yet supply the independent middle inequality needed to exclude C2>0,C3<0,C4>0 when C1<0. Hence the complete upper-low central-forcing-three theorem is not claimed by this certificate alone.
