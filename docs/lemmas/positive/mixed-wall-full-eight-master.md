# A full original-eight master for mixed strong-fork walls

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Let strictly positive linearly independent outer supports have ordered modes,
gamma=a3 b1-a1 b3>0, and let s2=P s1+Q s3 with P,Q>1. Comparable outer
supports are allowed. Retain the actual common-entropy graph uC(r),
at one original coefficient tuple and one original level, and set

B(r)=r(1+r), H=P(P-1)r^2-2PQ r+Q(Q-1),
R=(d1+r d3)(a1+r a3)(b1+r b3)/gamma^2, Y=R-B,
j=Q-(P-1)r.

Write eta<xi for the two roots of H. If Y(eta)>0 and Y(xi)<0, then the
original weighted intersection ceiling is **EIGHT**, uniformly over all
actual positive coefficients and levels. Reflection gives the same ceiling
when Y(eta)<0 and Y(xi)>0. These are all strict mixed-wall configurations;
there is no ordering condition on P,Q, degree condition, residue-balance
condition, source-derivative inequality, or upper bound on the high wall ratio.
Unit-wall configurations are outside this strict statement.

The left exterior contributes at most two weighted normal-curvature contacts;
the central interval contributes at most three; the right exterior contributes
exactly one simple contact. The resulting curvature ceiling is six, and the
two weighted normal-Rolle stages give the original ceiling eight.
No seam-bound or seam-edge casework is needed for the central proof.

## An ODE comparison valid even outside the physical source seam

The actual entropy graph obeys

uC'=f(r,uC), f(r,u)=j u(1-Pu)/(B+Hu),
0<uC<min(1/P,r/Q), B+H uC>0.

Normal-curvature contacts are exactly uC=u0, where u0=Y/H, with analytic
orders preserved. The key source denominator identity is

B+H u0=R>0.

It holds throughout every open wall interval, even when u0 is outside its
probability bounds. Thus the formal entropy ODE is well defined at both uC
and u0. For D=uC-u0, direct subtraction gives

D'=a(r)D-W/(H^2 R),

a(r)=j[B(1-P(uC+u0))-P H uC u0]/[(B+H uC)R],
W=R(HY'-H'Y)-Y(H-PY)j.

The coefficient a is analytic throughout the open central interval, including
at contacts; the displayed formula makes its extension explicit. Equivalently,
the affine ODE denominator stays positive along the full secant segment
between uC and u0. Fix any central base point and put

I(r)=exp(-integral a(r) dr)>0.

Then (I D)'=-I W/(H^2 R). Weighted Rolle therefore gives

central contact weight of D <= central root weight of W + 1.

This is a comparison of the one actual entropy curve with its one source
seam. It introduces no independent entropy levels and makes no physical
seam-component count. All denominators used for the integrating factor are
strictly positive or nonzero on the full central interval.

## Seven projective coefficients and one positive sum

Set Delta=xi-eta and use v=(r-eta)/(xi-r)>0. Define

G(v)=(1+v)^3 R((eta+xi v)/(1+v))=g0+g1 v+g2 v^2+g3 v^3.

All gi are strictly positive. Put L=eta(1+eta), T=xi(1+xi). The mixed
hypotheses give g0>L and 0<g3<T. The exact wall relation is

(P-1)Delta^2=2(2eta xi+eta+xi).

It simplifies the degree-six forcing transform to

(1+v)^6 W((eta+xi v)/(1+v))
 = [P(P-1)Delta/2] sum(Ci v^i, i=0,...,6),

where

C0=(g0-L)(3g0-L)>0,
C1=4g1(g0-L)>0,
C2=g1^2+2g2(g0-2L)-(L^2+2LT+Delta^2),
C3=4(g0 T-L g3)>0,
C4=(T^2+2LT+Delta^2)+2g1(2T-g3)-g2^2,
C5=4g2(T-g3)>0,
C6=(3g3-T)(T-g3).

Only C2,C4 and C6 have unrestricted signs. The decisive exact fact is
**C2+C4>0**. To see this, factor the source metric as

R(r)=k(r+A1)(r+A2)(r+A3), k,Ai>0.

Let zi=(eta+Ai)/(xi+Ai) in (0,1), p=z1 z2 z3, e1=z1+z2+z3,
e2=z1 z2+z1 z3+z2 z3, s=g3/T in (0,1), and m=L/T. Then
g0/T=sp>m, g1/T=s e2, g2/T=s e1. Define

J=(e1+p)^2+2e2-e2^2>0,
E=product(1-zi^2)>0.

Here e1>e2 because e2=sum(zi(zj+zk))/2<sum(zi); this makes J positive
directly. The universal identity is

(C2+C4)/T^2
 =(1-s)+s E+s(1-s)J+(sp-m)(4s e1+sp+m)>0.

Every displayed factor has the stated strict sign. In particular C2 and C4
cannot both be negative. Their large expanded coefficient expressions are
replaced by this short analytical identity.

## Descartes, parity, and the central ceiling

The integrating-factor comparison bounds central D contact weight by four.
Mixed source residues are both negative in the r chart, so u0 tends to minus
infinity as r approaches eta from the right and plus infinity as r approaches
xi from the left. The actual uC stays finite and positive at both walls.
Hence D has positive left phase and negative right phase. Its finite total
contact weight is odd, and the four-weight ceiling improves to THREE.

Finiteness needs no genericity assumption: the weighted Rolle ceiling applies
to every finite selection of contacts and excludes an infinite set. Nonzero
endpoint phases also exclude contacts near either wall. If C6 vanishes,
its zero coefficient is simply omitted; its associated wall forcing zero
is not an interior contact and causes no change to the argument.

## Exterior counts and the original bound

The mixed exterior theorem gives at most two left
weights and exactly one simple right contact. For a shorter right argument,
u0'>0 throughout the r chart, whereas uC'<0 for r>xi because xi>Q/(P-1).
Thus uC-u0 strictly decreases there, from positive to negative, and its unique
root is simple. The left proof uses strict log-concavity of uC/r
and strict log-convexity of the source's positive Stieltjes sum. Its positivity
can be proved using three compact factored Bernstein expressions.

There are no wall contacts under the strict mixed hypotheses. Therefore
2+3+1 gives at most six normal-curvature weights, and the two weighted normal-Rolle stages give at most eight original intersection
weights, for antichain and comparable positive outer supports alike.
