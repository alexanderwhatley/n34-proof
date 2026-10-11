# A two-negative-root certificate for the closed low-band region h <= l <= 1

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

This note proves an analytical regional completion of the one-positive-wall low-band target. It does not assert a universal one-wall master outside the stated region.

Let P>1, 0<Q<1, B=r(1+r), j=Q-(P-1)r, and

H=P(P-1)r^2-2PQr+Q(Q-1)=P(P-1)(r+h)(r-xi),

where h>0 and xi>0. The negative root lies in (-1,0), because H(-1)=(P+Q)(P+Q-1)>0 and H(0)<0; in particular h<1. Let R be a cubic with all four coefficients strictly positive and Y=R-B. Assume the strict low wall has a central source band

Y=k(r+l)(r-a)(r-b),  k,l>0, 0<a<b<xi.

Suppose additionally **h <= l <= 1**. Then for every finite actual entropy level, the curvature numerator

D_C=B+H u_C-R

has at most **six positive zero weights**, including analytic multiplicities. In a geometric positive-support chart admitting the two weighted normal Rolle reductions, the original source equation therefore has at most **eight** positive zero weights.

## The residual endpoint-positive case

The closed endpoint inequality already proves the curvature-six bound if W(0)<=0 or the degree-six coefficient w6<=0, where

W=R(Y'H-YH')-Yj(H-PY),

w0=Q R0[3P R0-(1-Q)R1+1-Q^2],
w6=-P R3[(P-1)R2+3Q R3-(P^2-1)].

Consequently it suffices to consider w0>0 and w6>0. The polynomial W then has degree exactly six and positive signs at both negative infinity and zero.

For h<l<1, evaluate at the negative root -l of Y. Since R(-l)=B(-l),

W(-l)=B(-l)Y'(-l)H(-l)
      =l(l-1) k(l+a)(l+b) P(P-1)(h-l)(-l-xi)<0.

Thus W has at least one negative root in each of (-infinity,-l) and (-l,0), for a total negative root weight at least two.

At the closed endpoint l=h, both Y and H vanish at -h, so W(-h)=0. At l=1, both Y and R vanish at -1, so W(-1)=0. In either case W has at least one negative root. The total negative root weight is even, because its endpoint signs at negative infinity and zero agree and W does not vanish at either endpoint. It is therefore again at least two. This parity argument includes all multiple negative roots and uses no perturbation.

At the positive wall,

W(xi)=Y(xi)[-R(xi)H'(xi)+P Y(xi)j(xi)]<0.

Indeed the low wall has Y(xi)>0, R(xi)>0, H'(xi)>0, and j(xi)<0; the latter follows also from H'=-2Pj. Since w6>0, W has at least one root in (xi,infinity).

These disjoint root budgets consume at least three of the degree-six polynomial's root weights outside (a,b). Consequently **W has at most three root weights in the central source band (a,b)**. This conclusion concerns the residual endpoint-positive case only; the endpoint inequality handles the other cases without requiring this local forcing bound.

## From forcing to contacts

On the whole central wall interval the formal source u0=Y/H satisfies B+Hu0=R>0. The actual source u_C satisfies the native first-order ODE

u_C'=j u_C(1-Pu_C)/(B+Hu_C).

The positive denominator permits the analytic secant comparison, with positive integrating factor mu:

(mu(u_C-u0))'=-mu W/(H^2 R).

Since u0 is positive centrally only on (a,b), every actual central contact lies in that source band. Weighted Rolle gives at most three forcing weights plus one contribution to the root count, hence at most **four central contact weights**. No contact can occur at a or b because u0=0 and u_C>0 there; nor at xi because Y(xi)>0.

The low-band exterior theorem gives at most **two exterior contact weights** on (xi,infinity), for arbitrary l/h. Adding the disjoint central and exterior multisets proves the curvature-six bound. Multiplication by H changes no contact order away from the wall.

## Inputs and limits

The source-band factorization is automatic whenever a strict low wall has any actual central contact: Y(0)>0, Y(xi)>0 and Y<0 at that contact force two simple central positive roots; the remaining cubic root is negative. If there is no central contact, the whole exterior ODE comparison alone gives at most six contact weights by degree-six forcing, one Rolle contribution to the root count and even endpoint phase.

Thus under h<=l<=1 the regional result is unconditional at every actual finite level once that source band exists. It neither assumes a sign for the negative-wall residue nor relies on generic roots, simple contacts, computer algebra, or a multiplicity perturbation.
