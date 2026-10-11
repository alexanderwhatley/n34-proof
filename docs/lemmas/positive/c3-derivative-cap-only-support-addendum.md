# Coefficient-only C3 support under the derivative bound

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

This addendum weakens the source assumptions of the upper-low C3 quadratic-slope support theorem. Its proof and exact certificate inputs are unchanged.

## Statement

Let P>1,0<Q<1,p=P-1. Let h>0 and xi>0 be the roots in

H(r)=Pp(r+h)(r-xi),

with the native wall-root relations

p=2[ xi-h(1+2xi) ]/(xi+h)^2,
Q=p(xi-h)/2.

Assume k>0,l>1,0<a<b<xi, and only the strict derivative bound

k<(1+2a)/[(b-a)(a+l)].  (1)

The coefficients of R=r(1+r)+k(r+l)(r-a)(r-b) need not be positive. Define the forcing W and its degree-six central-band coefficients C_i exactly as in the theorem. Set

d=b-a,L=a+l,M=b+l,gamma=Pp,
x=(a+h)(xi-a),y=(b+h)(xi-b),Gamma=(xi+h)^2,
A3=LinN3/Gamma,D3=2d^2(L^2 y-M^2 x).

Then C3/(kd gamma)=A3+kD3, and

**D3<=0 implies C3>0. Equivalently, C3<=0 implies D3>0.**

Here D3 denotes the quadratic coefficient's scale slope. It is distinct from the endpoint-phase denominator used in the C45 theorem. No positivity assumption on R or its individual coefficients, and no forcing endpoint phase, enters this coefficient-only statement.

## Proof by the source-free certificate

Put G=a+b+2ab. Assumption (1) gives

kd^2L<d(1+2a)=G-2a(1+a)<G.

Thus k<G/(d^2L), exactly the source ceiling used by the theorem. That theorem's remaining proof establishes

Zraw=L LinN3+2 Gamma G(L^2 y-M^2 x)>0

Consequently

A3+[G/(d^2L)]D3=Zraw/(Gamma L)>0.

For D3<0 the strict ceiling makes A3+kD3 strictly larger than this positive value. For D3=0 it equals that value. The normalization kd gamma is strictly positive, so C3>0 follows in both cases.

The original positive-source theorem obtains (1) from R'(a)=1+2a-kdL>0. This addendum assumes that same inequality directly, so no new algebraic certificate or numerical argument is required.

## dependencies and scope

The addendum concerns the compact polynomial coefficients only. A curvature-contact or original-geometry transfer still requires the relevant positive-source hypotheses of that separate argument. In particular, this weakening does not itself exclude the remaining alternating coefficient pattern or close the full upper-low chamber.
