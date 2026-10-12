# Fork master height theorem: independent assembly

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Scope

For A,B,a,b,p,q,c3,c4>0 put

```math
u=t^A(1-t)^B,\quad
v=t^{A+a}(1-t)^{B+b+q},\quad
w=t^{A+a+p}(1-t)^{B+b},\quad S=u-c_3v-c_4w.
```

The target is, for every nine ordered interior points t1<...<t9,

**(MH-F)**

```math
\min(S(t_1),S(t_3),S(t_5),S(t_7),S(t_9))
\le\max(0,S(t_2),S(t_4),S(t_6),S(t_8)).
```

Equivalently, every positive common level c1 has at most eight distinct
interior contacts with S. No whole N(3,4) theorem or complete INC theorem
is invoked in the proof below.

## Original source and two Rolle steps

Divide G=c1-S by -u. Its zeros are those of

```math
f=1-E_0h_0-E_1h_1-E_2h_2,
\quad h_0=t^{-A}(1-t)^{-B},\quad
h_1=t^a(1-t)^{b+q},\quad h_2=t^{a+p}(1-t)^b,
```

where (E0,E1,E2)=(c1,c3,c4)>0. Let D=t(1-t)d/dt, rho_t=t(1-t),

```math
\ell_0=-A+(A+B)t,
\quad\ell_1=a-(a+b+q)t,
\quad\ell_2=a+p-(a+b+p)t,
\quad L=\ell_2-\ell_1=p(1-t)+qt\gt0.
```

Let Pi=ell_i^2+D ell_i and

```math
R=\ell_1P_2-\ell_2P_1,\qquad
H=\det\begin{pmatrix}1&1&1\\\ell_0&\ell_1&\ell_2\\P_0&P_1&P_2\end{pmatrix},
\qquad K=H-R.
```

All original zeros lie in the one interval I={1-E0 h0>0}: h0 has
one strict minimum, and at an f-zero 1-E0 h0=E1 h1+E2 h2>0.
Set

```math
U=\frac{D[(1-E_0h_0)/h_1]}{D(h_2/h_1)}
=\frac{E_0h_0(\ell_1-\ell_0)-\ell_1}{h_2L}.
```

Direct differentiation gives

**(1)**

```math
\frac{D(f/h_1)}{D(h_2/h_1)}=U-E_2,
\qquad DU=\frac{R-E_0h_0H}{h_2L^2}.
```

Ten distinct original zeros would therefore force eight distinct
contacts in I of

**(2)**

```math
\Phi=w_0R/H=E_0\gt0,\qquad w_0=1/h_0=t^A(1-t)^B,
\qquad RK\gt0.
```

For strict simple/disjoint cores, division is legitimate: R and H
cannot vanish together. At a contact E0 h0=R/H is in (0,1), and H=R+K
turns that condition into RK>0.

## Linked cubics and the single-band geometry

The determinant identity simplifies to

```math
R=L\ell_1\ell_2+[qa+pb+pq]\rho_t,
```

```math
H=L(\ell_1-\ell_0)(\ell_2-\ell_0)
 +[q(A+a)+p(B+b)+pq]\rho_t,
```

**(3)**

```math
K=L\ell_0(\ell_0-\ell_1-\ell_2)+[qA+pB]\rho_t.
```

Thus R,H,K have degree at most three and strictly positive values at
both physical endpoints. For example

```math
R(0)=pa(a+p),\quad R(1)=qb(b+q),
```

```math
H(0)=p(A+a)(A+a+p),\quad H(1)=q(B+b)(B+b+q),
```

```math
K(0)=pA(A+2a+p),\quad K(1)=qB(B+2b+q).
```

On a strict core stratum each has zero or two physical roots. Hence
each negative locus is either empty or one interval. The useful locus
{RK>0} has at most three connected components.

## A five-critical budget with no external root-counting input

Use the increasing physical coordinate

```math
s=qt/L,\quad \alpha=a/p,\quad\beta=(b+q)/q,\quad
g=A/p,\quad h=B/q,\quad C=\alpha+\beta,\quad D_0=g+h,
```

```math
r=C/D_0\gt0,\quad x=-g+D_0s,\quad
\varrho=2(\alpha-rg)+1,\quad
T=D_0s(1-s)[(1-s)/p+s/q]\gt0.
```

The physical interval is (-g,h). Divide R,H,K by their common positive
factor L^3 and reuse their names. Put

```math
e=\frac{\varrho^2-1}{4r(r+1)},\quad Z=x^2-e,
\quad P=T-\varrho x+(2r+1)x^2.
```

Then

**(4)**

```math
R=r[P-(r+1)Z],\quad H=(r+1)[P-rZ],\quad K=P,
\quad (\log w_0)'=-x/T.
```

Prime now means d/dx. The derivative numerator is

**(5)**

```math
Q=x[P-(r+1)Z][P-rZ]+T(2xP-ZP'),
\qquad
\Phi'=-\frac{w_0r(r+1)Q}{TH^2}.
```

The degree-seven leading terms cancel exactly, so degree Q<=6. At
x=-g and x=h, T=0 while both bracketed factors in (5) are positive.
Thus Q(-g)<0<Q(h). Its total physical real-root multiplicity is odd
and at most six, hence at most five. In particular Phi has at most
five distinct physical critical points away from its poles.

The un-divided numerator in the original t-coordinate is generally
degree seven. The claim above is explicitly for the centered Q; no
degree-six assertion is made about that un-divided numerator.

## Separated negative bands: one critical point is unusable

If R or K has no negative band, there are at most two useful components,
and componentwise Rolle immediately gives at most 5+2=7 contacts.

If both negative bands exist and are disjoint, let J=(r1,r2) be the
negative R band. K>0 throughout J, and H=K>0 at its two endpoints.
On a strict stratum H therefore has zero or two roots in J.

If it has none, Phi<0 inside J and tends to zero at both ends, so it
has an interior minimum. If it has two, then between those two poles
R,H<0, so Phi>0 and tends to positive infinity at both ends; again
there is an interior minimum. In either event the minimum is a
physical critical point in RK<0, outside the useful locus. Hence at
most four of the five available critical points are useful. The at
most three useful components then contain at most 4+3=7 contacts.

This argument explains why three separated useful components do not
need a separate height comparison. It uses neither an old event atlas
nor an assumed saturation allocation.

## Overlapping negative bands: one concave-factor kernel

If the negative R,K bands overlap, H is negative on their intersection
and positive at the physical endpoints, hence it has two physical
roots. From H=R+K, its physical roots interlace with the R roots in
one of the four overlapping orders of
[quadratic ratio common level theorem](quadratic-ratio-level-count.md). Explicitly, the R,K band
arrangements RKRK, KRKR, KRRK, RKKR give R,H orders

```math
RHRH,\quad HRHR,\quad HRRH,\quad RHHR,
```

respectively. These are four descriptions of one quadratic-ratio
geometry, not separate gap-orientation proofs.

For p=q the cores are quadratic, and Phi is a positive constant times
w0 times the physical quadratic ratio; the common factor is already
strictly log-concave. For p!=q each cubic has one exterior root. Writing
xi_e for the R root and eta_e for the H root gives

```math
\Phi=v_0(t)q_{*}(t),\qquad
v_0(t)=C_0t^A(1-t)^B\frac{t-\xi_e}{t-\eta_e}\gt0,
```

with q_{*} the physical quadratic ratio and C0>0. The separate new
actual-source exterior-factor lemma proves (log v0)''<0 on (0,1)
for these overlapping bands; its full proof is
[overlap external factor concavity theorem](overlap-factor-concavity.md).
The quadratic-ratio
common-level theorem bounds all positive contacts, hence all useful
contacts, by six. It applies to both p-q signs and both mode sides.

Combined with the separated-band argument, eight useful contacts are
impossible. Equation (2) therefore excludes ten original zeros.

## Original rows, arbitrary levels, and finite boundaries

To exclude nine or more distinct zeros of an arbitrary nonidentity
original row, select finitely many such zeros with disjoint compact
neighborhoods. A small regular common height shift f=epsilon retains
at least the selected count: odd zeros contribute one root; one of the
two shift signs preserves twice the even minima, the other twice the
even maxima. The larger of these counts is at least the original count.
Renormalize using (f-epsilon)/(1-epsilon), scaling all E_i together.
The row still has negative endpoint limits and simple roots, so its
simple-root count is even. Nine retained roots therefore mean at least
ten. Compact sign brackets persist under a small generic original
support perturbation, contradicting the strict no-ten result.

Thus c1-S has at most eight distinct interior roots for every c1>0.
If (MH-F) failed at nine ordered samples, choose c1 strictly between
the two sides. Since S tends to zero at both endpoints, the ten
consecutive intervals formed by the nine samples and the two endpoints
would each give an original root. This contradicts the no-ten result.

Weak support limits of (MH-F) transfer directly at the nine fixed
interior samples. This does not take an endpoint limit in the exponents.
Combining the strict fork theorem with the comparable master
theorem covers every strict positive componentwise least support u,
with no relative ordering of v,w. At fixed interior samples, approximation
then gives the same height inequality whenever u,v,w have nonnegative
supports and s_u is componentwise no larger than s_v,s_w.

The at-most-eight distinct-root conclusion holds for every nonidentity
row in that weak closure: a positive common level regularization of
c1-S retains nine hypothetical zeros, and simple crossings give nine
alternating sample values with five above the positive level and four
below, contrary to the finite-sample height inequality. This step
does not need any endpoint sign at a zero exponent.

The weak least-support identity classification is explicit in
[weak least support identity classification](least-support-identities.md). Besides all three supports
being zero and c1+c3+c4=1, the only identity is u=1,v=t,w=1-t up to
exchange, with c3=c4=1-c1 in (0,1). The comparable-only all-zero
identity exception therefore cannot be reused for this larger boundary.
