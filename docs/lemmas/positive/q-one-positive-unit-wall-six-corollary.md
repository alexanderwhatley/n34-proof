# The Q=1 one-positive-unit-wall boundary

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Separate optional corollary, 4 October 2026. This does not modify the Q<1 note or the 15-page readable proof.

**Theorem.** Let P>1, Q=1, and let R=R0+R1 r+R2 r²+R3 r³ have all four coefficients strictly positive. Put

```math
B=r(1+r),\quad H=P(P-1)r^2-2Pr,
\quad \xi=\frac2{P-1},\quad Y=R-B.
```

Let theta_C be the physical common-entropy curve determined by

```math
J(r,\theta)=\frac{P\log(1-P\theta)+\log(r-\theta)
-\log\theta-P\log(1+r-P\theta)}P=C,
\quad 0<\theta<\min(1/P,r).
```

If Y(xi)=0, the positive zeros of B+H theta_C-R have total analytic multiplicity at most six. No transverse-wall assumption is needed.

## Actual chart and endpoint behavior

The positive-metric and actual-curve identities from the all-positive-weights entropy lemma apply with K=P. In particular M=B+H theta>0 in the open chart, J_theta<0, and the entropy level gives a unique analytic theta_C on every r>0. The physical bound metrics specialize to

```math
M(r,1/P)=r(Pr-1)\quad(r\ge1/P),
\qquad M(r,r)=r(1-Pr)[1-(P-1)r]\quad(r\le1/P),
```

which are nonnegative; affine interpolation from M(r,0)=B>0 gives strict interior positivity.

With kappa=exp(PC), A=1-P theta_C and S=1+r-P theta_C, the level equation is exactly

```math
\kappa=(A/S)^P\frac{r-\theta_C}{\theta_C}.
```

As r tends to zero, theta_C<r implies A/S tends to one, and hence

```math
\theta_C(r)\sim\frac{r}{1+\kappa}.
```

At infinity theta_C tends to zero: any subsequence bounded away from zero would make the right side of the level equation tend to zero, since P>1, contradicting fixed positive kappa. Thus

```math
\theta_C(r)\sim\kappa^{-1}r^{1-P}.
```

The Q<1 left law r/Q is therefore not asserted at this boundary. The source/actual endpoint mismatches needed below follow without an elasticity limit argument.

## Global cancellation and the six contribution to the root count

Write

```math
h=r-\xi,\qquad L=P(P-1)r>0,\qquad H=hL,
\qquad Y=hZ,
```

where Z is quadratic. The canceled source theta_0=Z/L is analytic on the whole positive axis, and B+H theta_0=R>0 there. Put T=1-(P-1)r and

```math
W=R(Y'H-YH')-YT(H-PY).
```

The universal polynomial cancellation gives deg W<=6, and the exact unit factorization gives

```math
W=h^2\widehat W,\qquad
\widehat W=R(Z'L-ZL')-ZT(L-PZ),
\qquad \deg\widehat W\le4.
```

These identities are precisely the one-wall polynomial identities specialized to Q=1; they impose no Q<1 inequality. The formal ODE

```math
F(r,z)=\frac{zT(1-Pz)}{B+Hz}
```

has positive denominator R along theta_0 and positive denominator M along theta_C. Its affine denominator is positive between the two graphs. Thus its secant is analytic on the whole positive axis, including xi. The error identity is

```math
\theta_0'-F(r,\theta_0)=\frac{\widehat W}{L^2R}.
```

For D=theta_C-theta_0, multiplication by a positive integrating factor therefore makes D' proportional, with a nonvanishing factor, to -widehat W. Weighted Rolle gives at most deg widehat W+1<=5 zeros of D, counting analytic multiplicities.

The exceptional polynomial widehat W=0 is impossible. Indeed

```math
\theta_0(r)\sim-\frac{R_0}{2Pr}\quad(r\downarrow0),
\qquad
\theta_0(r)\sim\frac{R_3}{P(P-1)}r\quad(r\to\infty),
```

so D is positive near zero and negative near infinity, and has a zero. If the forcing vanished identically, the homogeneous difference ODE would make that zero force D identically zero, contradicting these endpoint mismatches.

Finally

```math
B+H\theta_C-R=hL D.
```

The factor L has no positive zero. The factor h restores exactly one positive unit-wall order, including when D already vanishes at xi. The total curvature zero weight is therefore at most 5+1=6.

This is an abstract curvature corollary. Original-profile weighted eight follows only for a genuine geometric source chart with the two normal Rolle reductions. No unrestricted nonunit theorem and no complete nongeneric ONE-EDGE source dispatch is asserted.
