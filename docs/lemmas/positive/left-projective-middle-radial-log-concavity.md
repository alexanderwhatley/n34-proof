# Exact left-tail radial log-concavity of the strong-fork entropy curve

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Let P,Q>1 and u=uC(r) be the common-entropy graph, with

H=P(P-1)r²-2PQr+Q(Q-1),
K=r(r+1)+Hu,
u'=u(1-Pu)(Q-(P-1)r)/K,
0<u<min(1/P,r/Q).

Then

**log(u(r)/r) is strictly concave and u(r)/r is strictly increasing on 0<r<(Q-1)/P.**

In particular both conclusions hold on the entire left fixed-wall interval 0<r<eta. This statement is independent of the source metric, common entropy level, and original coefficients. Its reflected version applies to the right tail after swapping P,Q and replacing r by 1/r and u by u/r.

## Proof with an explicit positive Bernstein certificate

Set v=u/r, s=Q-1-Pr>0, and A=1+r+Hv=K/r>0. The first-order equation reduces exactly to

v'=v(1-Qv)s/(rA),
(log v)'=(1-Qv)s/(rA)>0.

Here 0<Qv<1, Q=s+1+Pr, and H=s(s+1)-Pr(r+1). Differentiating at fixed P,Q (thus s'=-P) gives

(log v)''=-(1-Qv)N/(r² A³),

where

N=Pr A²+s A²+Qv s² A+rs A[1-2P(s+1+r)v]+Hv(1-Qv)s².

Although the displayed N has one term of indeterminate sign, it is a quadratic polynomial in v with an explicit strictly positive Bernstein representation. Put w=Qv in (0,1). Then

Q² N=b0(1-w)²+2b1 w(1-w)+b2 w²,

with

b0=(r+1)Q²(Pr²+Pr+2rs+s),

2b1=Q[Pr³s+2Pr³+3Pr²s+4Pr²+2Prs+2Pr+4r²s²+4r²s+4rs³+10rs²+6rs+s⁴+4s³+5s²+2s],

b2=(s+1)(r+s+1)(Pr²+Pr+2rs²+2rs+2s³+3s²+s).

Every coefficient in these expressions is positive and P,r,s>0. Consequently N>0 and the second derivative is strictly negative. The certificate does not need H>0; the probability conditions already ensure A>0.

Finally, H((Q-1)/P)=-(Q-1)(P+Q-1)/P<0, while H(0)>0. Thus eta<(Q-1)/P<xi, so the whole left exterior interval is included.
