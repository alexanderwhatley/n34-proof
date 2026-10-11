# Mixed strong-fork walls: an exact two-plus-one exterior contact reduction

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Let strictly positive linearly independent outer supports have ordered modes,
so gamma=a3 b1-a1 b3>0, and let s2=P s1+Q s3 with P,Q>1.
The outer supports may be coordinatewise antichain or comparable. Retain the
common-entropy graph uC(r) and source-cubic reduction

H=P(P-1)r^2-2PQr+Q(Q-1),
R=(d1+r d3)(a1+r a3)(b1+r b3)/gamma^2,
Y=R-r(r+1),
uC=Y/H at an original normal-curvature contact.

Write the two positive H roots as eta<xi. Assume the mixed-wall orientation

Y(eta)>0, Y(xi)<0,

meaning the left origin-wall ratio is below one and the right ratio is above
one. Then, uniformly over every actual positive coefficient tuple and level:

* The left exterior interval (0,eta) has at most TWO normal-curvature contact
  weights.
* The right exterior interval (xi,infinity) has exactly ONE normal-curvature
  contact, and it is simple.

No regularity of source seam endpoints or simplicity of original, curvature,
or forcing contacts is assumed. The reflected orientation exchanges the
outer labels and the two exterior intervals. The remaining central interval
is not counted by this theorem. The [complete mixed-wall theorem](mixed-wall-full-eight-master.md) proves at most three central weights. Together the counts are $2+3+1=6$ curvature weights and hence at most eight original roots. This document supplies only the two exterior counts.

## Residues of the source seam

Away from the walls write u0=Y/H. Polynomial division gives

u0=ell0+ell1 r-Bminus/(r-eta)-Bplus/(r-xi),

where

ell1=R3/[P(P-1)]>0,
Bminus=Y(eta)/[P(P-1)(xi-eta)]>0,
Bplus=-Y(xi)/[P(P-1)(xi-eta)]>0.

In particular u0'>0 on each wall interval, and u0'''
=6[Bminus/(r-eta)^4+Bplus/(r-xi)^4]>0. These identities by themselves
are not an intersection-count theorem.

## The left exterior count from strict radial log-concavity

For 0<r<eta set v0=u0/r. Partial fractions give the stronger positive
representation

v0=ell1+u0(0)/r+Bminus/[eta(eta-r)]+Bplus/[xi(xi-r)].

Here u0(0)=R(0)/[Q(Q-1)]>0. Thus every term is positive. The logarithm
of each nonconstant reciprocal-linear term is strictly convex, and the
constant is log-convex. A sum of positive log-convex functions is log-convex:
its log second derivative is the weighted mean of the summands' log second
derivatives plus the nonnegative variance of their log first derivatives.
The positive 1/r summand makes the sum strictly log-convex.

The universal radial-log-concavity lemma proves
that vC=uC/r has strictly concave logarithm on
0<r<(Q-1)/P. The whole interval (0,eta) lies within this range, since
H((Q-1)/P)=-(Q-1)(P+Q-1)/P<0. Consequently

F=log(vC)-log(v0)

has strictly negative second derivative throughout (0,eta). Weighted Rolle
therefore permits at most two root weights. Since v0,vC are positive,
F vanishes exactly at uC=u0 and the analytic root orders agree. No division
by a vanishing source probability is made.

At r down to zero, uC is asymptotic to a positive constant times r^Q,
whereas v0 is asymptotic to u0(0)/r; F tends to minus infinity.
As r approaches eta from the left, v0 tends to plus infinity and vC stays
finite and positive, so F again tends to minus infinity. Thus a finite
left contact set has even total weight, either zero or two. Finiteness
follows directly from strict concavity and the endpoint phases, including
for arbitrary finite root selections; no generic perturbation is used.

## The right exterior contact is unique and simple

For r>xi,

u0''=-2[Bminus/(r-eta)^3+Bplus/(r-xi)^3]<0.

The fixed-wall entropy identity gives uC''>0 there. Therefore
uC-u0 is strictly convex and has at most two root weights. As r approaches
xi from the right, u0 tends to minus infinity, so uC-u0 is positive.
As r tends to infinity, u0 is asymptotic to ell1 r and uC tends to zero,
so uC-u0 is negative. These opposite nonzero endpoint phases force an odd
contact weight; the two-weight ceiling leaves exactly one simple contact.
The argument excludes roots approaching either endpoint and requires no
seam-edge regularity.

## Exact algebra and a genuinely unqualified mixed fixture

R(r)=(r+1/10)(r+90)(r+100)/1000
