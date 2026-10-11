# The entire comparable middle chamber by origin-interior curvature

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Statement

Let u,v,w be beta monomials whose support vectors satisfy the strict chain
0<s_u<s_v<s_w coordinatewise. Suppose

s_u = lambda*s_v + mu*s_w,
    lambda>0, mu>0, lambda+mu<1.

For every c1,c3,c4>0, the actual original row

G=c1-u+c3*v+c4*w

has at most eight interior root weights, including analytic multiplicity.
There is no scale, mode-root, auxiliary-discriminant, contact-level, or
generic-root hypothesis.

In the original comparable chart w=v*q, u=v^h*q^n, this is exactly the
entire middle region 0<n<h<1: lambda=h-n, mu=n. The scalar scale Lambda
and every physical cubic-root type are unrestricted.

## Five-line noncollinear reduction

Divide by the positive actual monomial -u:

-G/u = 1-c1*(1/u)-c3*(v/u)-c4*(w/u).

Its three support vectors are

t0=-s_u, t1=s_v-s_u, t2=s_w-s_u.

The displayed relation gives

(1-lambda-mu)*t0 + lambda*t1 + mu*t2 = 0.

All three coefficients are strictly positive and sum to one. If
det(s_v,s_w)!=0, the three t_i are affinely independent because
det(t1-t0,t2-t0)=det(s_v,s_w). Their triangle therefore contains the
origin strictly in its interior. Apply the signed compact-oval
theorem to this exact positive coefficient tuple (c1,c3,c4) at level one.
It gives eight root weights. Multiplication by the nonvanishing analytic
monomial -u preserves every original root order, proving the statement.

## Collinear ray, covered directly

If det(s_v,s_w)=0, positivity makes s_v and s_w lie on the same positive
ray. The displayed relation puts s_u on that ray as well. Write
u=T^a,v=T^b,w=T^c, where T is a positive beta monomial and 0<a<b<c.
For z=log T, division by T^a gives

F(z)=c1*exp(-a*z)-1+c3*exp((b-a)*z)+c4*exp((c-a)*z).

Its second derivative is strictly positive. Weighted Rolle therefore
gives at most two real root weights of F. The analytic map log T has one
nondegenerate maximum: each value below that maximum has at most two
preimages with nonzero derivative, and at the maximum composition doubles
root order. Thus G has at most four root weights. This includes multiple
contacts and does not use a collinear limiting theorem.

The noncollinear eight and collinear four bounds together prove the full
stated strict chamber without any generic support choice.

## Exact original mode dictionary

The published comparable chart defines q=w/v and u=v^h*q^n. As support
identities,

s_u = (h-n)*s_v + n*s_w,
    alpha_origin=(1-h,h-n,n).

The old middle mode is 0<n<h<1, with r1>n/(1-h) required by the source
chain. Its three origin barycentrics are strictly positive, regardless of
the cubic scale Lambda. Conversely the positive-barycentric conditions
are exactly 0<n<h<1. The source chain is retained; it is not inferred
from barycentric positivity.

If lambda or mu tends to zero while the strict coordinate chain remains,
the closed middle-cone source inherits an eight-DISTINCT-root bound by one
common-level regularization and compact sign brackets followed by moving
s_u slightly into the displayed open triangle. No new weighted assertion
on those origin-boundary faces follows from that transfer. In particular,
the full theorem above already includes the common-ray case, but this
boundary observation is not used to prove it.

## Scope and height consequence

The theorem proves the entire region $0<n<h<1$ directly from the convex level curve. The earlier-mode, larger-rightmost-gap, and smaller-rightmost-gap arguments remain separate: their origin barycentric coefficients do not all have the required positive signs. The smaller-gap central orientation identity is therefore still needed there.

The nine-sample height inequality follows directly. A strict violation chooses one positive common level between the four minima and five maxima. The zero endpoint limits give ten disjoint original sign-changing brackets, contrary to the eight-root bound proved above.
