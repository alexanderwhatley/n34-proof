# A factored, analytical Bernstein proof of left radial log-concavity

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

The immutable radial-log-concavity theorem already proves (log(uC/r))''<0 and (uC/r)'>0 on 0<r<(Q-1)/P, in particular the entire left fixed-wall interval. Its expanded Bernstein coefficients admit the following compact factorization. This does not change the theorem or its scope.

Retain s=Q-1-Pr>0, Q=s+1+Pr, v=uC/r, w=Qv in (0,1), A=1+r+Hv>0. The exact curvature numerator N obeys

Q²N=b0(1-w)²+2b1 w(1-w)+b2 w²,

where

b0=(r+1)Q²[Pr(r+1)+s(2r+1)],

2b1=Q{Pr(r+1)[r(s+2)+2(s+1)]
       +s(s+1)(2r+s+1)(2r+s+2)},

b2=(s+1)(r+s+1){Pr(r+1)+s(s+1)(2r+2s+1)}.

Every bracket and factor is strictly positive for P,r,s>0. Consequently N>0 is visible directly from these three expressions, without expanding any multivariate coefficient table. Together with

(log v)''=-(1-Qv)N/(r²A³)

this proves the strict sign analytically.
