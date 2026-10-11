# Native Q=1 LOW curvature six for real negative metric roots

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Let P>1, p=P-1, B=r(1+r), H=Pp r(r-xi), xi=2/p, and j=1-pr.
Let R=k product_i(r+A_i), k>0, A_i>0, counting repeated factors separately.
Equivalently R has four positive coefficients and three real negative roots.
For any finite actual entropy C, let u_C be the physical graph

J=[P log(1-Pu)+log(r-u)-log u-P log(1+r-Pu)]/P=C,
0<u<min(1/P,r).

Put Y=R-B and D_C=B+H u_C-R. If Y(xi)>0, then D_C has at most **six
positive zeros counted with analytic multiplicity**. The same bound holds
for either wall sign if some A_i<=1, and at the unit wall Y(xi)=0 for
every positive-coefficient cubic. This note does not itself prove the
remaining HIGH case when every A_i>1.

## Actual Q=1 graph and whole-sector comparison

The native Q=1 unit-wall note proves directly that the graph is
unique and analytic, M=B+Hu_C>0, and

u_C'=j u_C(1-Pu_C)/M,
u_C(r)~r/(1+exp(PC)) at zero,
u_C(r)~exp(-PC) r^(1-P) at infinity.

Its exact native elasticity formula, valid for every P,Q>0, gives

eta_C'=-A D {u_C(H+Pr)^2+Pr^2 S}/M^3<0,
A=1-Pu_C, D=r-u_C, S=1+r-Pu_C.

On r>xi, j<0, so eta_C<0 and u_C'<0. Every quantity in this
argument is evaluated at the same finite C.

For u_0=Y/H, B+H u_0=R>0 on each whole sector. The affine denominator
is positive between u_C and u_0, even if u_0 is not physical. The exact
ODE secant therefore supplies a positive analytic integrating factor mu
with

(mu(u_C-u_0))'=-mu W/(H^2 R),
W=R(HY'-H'Y)-Yj(H-PY), degree W<=6.

One weighted Rolle contribution to the root count per whole sector is valid. Analytic zero orders
are preserved away from xi. Since D_C tends to negative values at both
positive-axis ends, its finite total root multiplicity is even. The forcing
constant is w0=3P R0^2>0. If w6<=0, opposite forcing endpoint signs or
degree loss give at most five positive forcing weights. Two sector payments
give seven curvature weights, lowered by even parity to six. The positive
w0 also excludes identically zero forcing. Thus assume w6>0 below.

## A closed negative-metric-root inequality at Q=1

At any metric root -A,

W(-A)=B(-A)j(-A)[H(-A)+PB(-A)],
H+PB=(Pr-1)Pr.

For 0<A<1 this value is strictly negative; for A=1 it is zero. Since
w0,w6>0, W is a genuine degree-six polynomial positive at zero and at
negative infinity. A strict negative value gives at least two negative
roots. At A=1 the negative-axis root multiplicity is positive and even,
so is at least two. Hence at most four positive forcing weights remain.
Two whole-sector Rolle payments give curvature six. This inequality permits
multiple metric and forcing roots, and is valid for both nonunit wall signs.
The native Q=1 unit cancellation handles Y(xi)=0 directly.

## Contacted LOW when all metric distances exceed one

If there is no central contact, all contacts are on (xi,infinity). The
whole-sector comparison bounds them by seven; their endpoint phases are
both negative for D_C, so their total is even and is at most six.

Suppose there is a central contact. As Y(0)>0, Y(xi)>0, and Y<0 at
that contact, the cubic has two distinct simple roots 0<a<b<xi and its
third root is -l<0:

Y=k(r+l)(r-a)(r-b).

All central contacts lie in (a,b). Assume every A_i>1, since otherwise
the preceding inequality already applies. Because R(-1)>0 and

Y(-1)=k(l-1)(1+a)(1+b),

we have l>1. At each metric root the exact identity is

k(l-A_i)(A_i+a)(A_i+b)=A_i(1-A_i).

Its right side is negative, so A_i>l for every i, including repeated
factors. Constant coefficients give product_i A_i=lab>l^3, hence

T=ab>l^2.                                                    (1)

## A short exact middle-coefficient proof at h=0

Put d=b-a, L=a+l, M=b+l, S=a+b, T=ab, G=S+2T, and X=xi.
For the compact degree-six source-band forcing coefficients,

C3/(kdPp)=LinN3/X^2+kD3,
LinN3=d F(X),
D3=2d^3[(l^2-T)X-l(2T+lS)].

Here the h=0 compact operator gives

F(X)=f3 X^3+f2 X^2-f1 X,
f3=4S(T-l),
f2=4(lS^2+2ST+2lT)+2T(lS-2T),
f1=6T(2T+lS)>0.

Positive R'(a)=1+2a-kdL gives kd^2L<d(1+2a)<G. Since (1)
makes D3<0, it suffices to prove positivity at the larger scale ceiling
k=G/(d^2L). The required numerator, divided by d, is

Z(X)=L F(X)+2G X^2[(l^2-T)X-l(2T+lS)].

Write Z=K3X^3+K2X^2+K1X. Its leading coefficient has the exact positive
decomposition

K3=(T-l^2)(4LS-2G)+4LS(l-1)l,
4LS-2G=2[2a^2+(2l-1)(a+b)]>0.

The identity Z''(b)=2I2+4bK3 proves Z''(b)>0. Hence Z'(b)>0 as well.
Since K3>0, Z'' increases on X>=b; Z consequently increases strictly
from its positive value at b. It follows that Z(xi)>0 for xi>b.
At the scale ceiling the normalized C3 is d Z/(X^2 L)>0; the actual
strictly smaller scale with D3<0 makes it larger. Therefore

C3>0.                                                       (2)

This proof does not invoke F23, F24, the full C3 slope-support theorem,
or any entropy approximation.

## The closed h=0 C45 certificate and count

By (1), b>l>1. Thus only the C45 blended-bound domain l<b is
needed. Its raw polynomial identities specialize exactly at h=0,
equivalently q=0 in h=xi*q/[(1+2xi)(1+q)]. This is substitution into
verified polynomial identities; it takes no limit of root counts.

C4-2C5>0, hence C5>=0 implies C4>0.                           (3)

## Direct Q=1 exterior-two contribution to the root count

The retained one-positive-wall exterior proof is valid at h=0 by its exact
inequalities. For r>xi, write the positive source elasticity eta_0=p_0-q_0,

p_0=r/(r-a)+r/(r+l)-1>0,
q_0=r(xi-b)/[(r-xi)(r-b)]>0.

Its numerator N=r^2+la is positive. The retained log-derivative comparison
has the positive first difference

N'(r+l)-N=r^2+l(2r-a)>0,

and its two bracket differences are strictly positive. Hence eta_0'>0
where eta_0<=0. Since actual eta_C<0 and eta_C'<0, every source entropy
critical point is a nondegenerate strict maximum.

There is at most one physical exterior component: the unchanged positive
cubic ratio R/[r(Pr-1)] has exactly one minimum after the shift r=t+1/P,
by its coefficient sign variation. The ratio is >1 at xi and tends to
infinity, so its strict sublevel is empty or one interval. On that interval
entropy tends to negative infinity at both ends and has one nondegenerate
maximum. Every fixed finite entropy therefore has at most two exterior
contact weights. This includes a double entropy contact at the maximum.

The positive wall itself is not a contact because D_C(xi)=-Y(xi)<0.
Thus four central plus two exterior weights prove curvature six. All counts
apply to arbitrary finite zero selections, exclude infinite zero sets, and
retain analytic multiplicities at one fixed source and entropy.
