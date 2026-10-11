# Endpoint transversality of the unit-left-wall source comparison

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Under the unit-left-wall proposition's assumptions R(eta)=eta(1+eta), R(xi)<=xi(1+xi), R nonzero with nonnegative coefficients, its strict forcing comparison extends to **0<r<=eta**, interpreting u0=(R-B)/H by removable continuation at eta. Equality at the endpoint occurs only for R=B.

Indeed H has a simple zero at eta and Y=R-B vanishes there, so

u0(eta)=Y'(eta)/H'(eta),
u0'(eta)=[Y''(eta)H'(eta)-Y'(eta)H''(eta)]/[2H'(eta)²].

Both quantities are affine in the source coefficients. At the wall F(eta,u)=u(1-Pu)j(eta)/B(eta), a strictly concave quadratic for every real u. Therefore Phi=u0'-F is still convex in the source weights at the wall, and the same six-vertex reduction applies.

For the pure constant and pure linear vertices, the forcing numerator T has a factor (r-eta)². The denominator H² has precisely the same factor and a strictly positive remaining limit. The analytical simplification gives C0(eta)<0 and C1(eta)<0, so their endpoint forcing gaps remain strictly negative after cancellation. The affine (0,3) vertex has N03(eta)<0 and a positive denominator. The constant (0,2) vertex has u=1/(2PQ), F>0 at eta, and u'=0. The linear (1,3) vertex has u=r/(2PQ); its strict radial ODE inequality remains valid at eta because eta<(Q-1)/P. Finally R=B gives u0=0 and Phi=0. Convexity now proves the asserted endpoint comparison, strict for every R!=B.

Consequently, if the actual common-entropy graph satisfies uC(eta)=u0(eta) with positive probabilities, then

**(uC-u0)'(eta)>0.**

This is a transverse residual seam contact. The original curvature-contact expression B+H uC-R=H(uC-u0) then has order exactly two at that wall. If uC(eta)!=u0(eta), it has order exactly one. These conclusions control contact multiplicity directly; no perturbation persistence assertion is used.

The reflected statement at the right unit wall follows by swapping P,Q and replacing r by 1/r, u by u/r, and R by the reversed cubic r³R(1/r). The residual crossing there has the reversed orientation in the original increasing-r coordinate.

This corollary is local boundary control. A closed high-wall original-contact ceiling needs a separate global interval/sign budget, which is not asserted here.
