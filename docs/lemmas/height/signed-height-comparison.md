# Signed source height separation by metric deformation

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Keep a strict positive comparable beta-support chain u<v<w, q=w/v,

$$
u=v^h q^{-m},\qquad H=1-h,\qquad 0<h<1,\quad0<m<H.
$$

Use the linked source cubics C,D and V=uD/C. Suppose their physical
original-x roots have the signed order

$$
d_0<c_0<c_1<d_1<d_2<c_2.
$$

Equivalently, in the projective source p=lambda_v/lambda_q, the poles
satisfy

$$
-1<\gamma_1<\gamma_2<0<r_3<\gamma_3,
 \qquad\epsilon_-<\gamma_1,\quad\epsilon_+<\gamma_3,
$$

and E/C has residues $d_1<0<d_2,d_3$. Here E=D−HC is the
original linked quadratic, not an independently chosen numerator.

**Theorem.** Every finite stationary point x of V on the right main
branch p<gamma1 is higher than every positive central value:

$$
\boxed{V(y)<V(x)\qquad(y\in(d_1,d_2)).}
$$

Neither a Qv root-count condition nor positivity of the two nonconstant
contact coefficients is required.

## 1. Every exterior critical precedes epsilon_minus

Write the projective ratio as

$$
Q=D/C=H-\frac A{p-\gamma_1}
        +\frac{d_2}{p-\gamma_2}+\frac{d_3}{p-\gamma_3},
 \qquad A>0,\quad d_2,d_3>0.
$$

At epsilon_minus, C>0, E=0, and E'>0, so
Q'=E'/C>0. For p<gamma1,

$$
Q'=\frac A{(\gamma_1-p)^2}
 \left[1-\sum_{j=2,3}\frac{d_j}{A}
       \left(\frac{\gamma_1-p}{\gamma_j-p}\right)^2\right].
$$

Each ratio in brackets strictly decreases as p increases. Hence the
bracket strictly increases, and Q'>0 on [epsilon_minus,gamma1).
Also u_p/u=(hp−m)/Pi>0 on the entire exterior branch. Thus V'>0 on
that interval, and every exterior critical has p*<epsilon_minus.

Consequently 0<t=Q(p*)<H<1. The u and v scores are positive there.
The gap score is positive as well, because

$$
E(-m/H)=m(H-m)/H>0
 \quad\Longrightarrow\quad\epsilon_-<-m/H,
$$

and lambda_(v/u)=(Hp+m)lambda_q>0 on the right branch at p*.

## 2. Fix the source chart and increase its metric

Put U=lambda_u(x)>0, R=lambda_(v/u)(x)>0,
Q=−lambda_q(x)>0 and rho=x(1−x). Define

$$
r=R/U,\quad q=Q/U,\quad
 a=\rho S_{v/u}/U^2,\quad b=\rho S_q/U^2,
 \quad c=\rho S_u/U^2,
$$

$$
\kappa=x/U,\quad\ell=(1-x)/U,\quad w=\ell-\kappa,
 \qquad\eta=U(y-x)/\rho.
$$

Hold r,q,a,b,c,w fixed and increase kappa, with ell=kappa+w.
This defines actual beta supports by the reconstruction in
[actual height metric monotonicity](actual-height-metric-monotonicity.md).

The source cubics' values and first eta derivatives at eta=0 are
independent of kappa. Thus t=D0/C0 and the stationary equation

$$
D_0C_0+D'_0C_0-D_0C'_0=0
$$

remain fixed. No probability weights or coefficient sign assumptions
are needed to preserve the stationary envelope contact.

At a positive central point, lambda_u(y)>0 and D/C<H. The exact
height ratio V(y)/V(x) therefore strictly increases with kappa, by
[actual height metric monotonicity](actual-height-metric-monotonicity.md).

## 3. The boundary height is controlled by fewer source poles

The routing theorem in [metric deformation root cell boundaries](metric-deformation-root-cell-boundaries.md)
uses H−t>0, now supplied by Section 1 without contact weights. It
shows that the first boundary is either cancellation of the negative
pole, b_u=0, or a_q=0. The old positive central point remains physical
and positive throughout.

At cancellation and at b_u=0, apply the closed two-pole
source height lemma. At a_q=0, apply the one-positive-pole
boundary theorem in
[zero q left exponent signed height separator](zero-q-left-exponent-signed-height-separator.md).
Both closed versions allow their simultaneous endpoint events.
The boundary central/exterior height ratio is at most one. Since it
strictly increases with the metric, the starting ratio is strictly
less than one, proving the theorem.

The original actual-row HEIGHT bridge and global node routing remain
part of the N(3,4) application. This theorem replaces the analytic
signed exterior-to-central comparison; it does not automatically remove
any other comparable source cell or increase the appendix-case
replacement count.
