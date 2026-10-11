# One positive origin wall: actual geometry and a unit-wall six bound

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Analytical probe, 4 October 2026. This is separate from the two-internal-wall master. It proves the statements below for the indicated one-wall curvature model; it does not retire the whole original nongeneric ONE-EDGE row.

Let $P>1$, $0<Q<1$, $K=P+Q-1$, and

$$
H=P(P-1)r^2-2PQr+Q(Q-1),\quad B=r(1+r),\quad
T=Q-(P-1)r.
$$

The roots of $H$ are $-h\in(-1,0)$ and $\xi>0$. Let $R=R_0+R_1r+R_2r^2+R_3r^3$, with all four coefficients positive, and put $Y=R-B$. The actual curvature equation is

$$
d_C(r):=B(r)+H(r)\theta_C(r)-R(r)=0.                  \tag{1}
$$

Weights throughout are ordinary finite analytic orders of vanishing. Bounds are for positive $r$; the endpoints zero and infinity are excluded.

## Actual curves and the correct endpoint laws

Write

$$
A=1-P\theta,\quad D=r-Q\theta,\quad S=1+r-K\theta=A+D+\theta,
\quad M=B+H\theta,
$$

on $0<\theta<\min(1/P,r/Q)$, and define

$$
J(r,\theta)=\frac{P\log A+Q\log D-\log\theta-K\log S}{K}.
$$

The affine function $M$ is strictly positive in this open chart. Its active endpoint values are

$$
M(r,1/P)=\frac{(Pr-Q)(Pr-Q+1)}P\quad(r\ge Q/P),
\qquad
M(r,r/Q)=\frac rQ(Q-Pr)T\quad(r\le Q/P),
$$

and both are nonnegative. Since $J_\theta=-M/(K\theta ADS)<0$, every finite $C$ determines a unique smooth physical curve $\theta_C$ on all $r>0$. Its exact derivatives are

$$
\theta_C'=\frac{\theta_CTA}{M},\qquad
\theta_C''=\frac{\theta_C ADS H}{M^3},\qquad
\eta_C':=\left(\frac{r\theta_C'}{\theta_C}\right)'
=-\frac{AD\{\theta_C(H+Kr)^2+Kr^2S\}}{M^3}<0.          \tag{2}
$$

These rational identities do not require $Q>1$. In this chart $\beta=Q/(P-1)$ lies strictly between zero and $\xi$; the actual curve increases up to $\beta$ and decreases thereafter. In addition

$$
1-\eta_C=\frac{D(1-Q+Pr)}M>0.                       \tag{3}
$$

Let $\kappa=e^{KC}$, $\nu=(1-Q)/Q$, and $c_L=(\kappa/Q)^{1/Q}$. The endpoint laws are

$$
\theta_C(r)=\frac rQ[1-c_Lr^\nu+o(r^\nu)]\quad(r\downarrow0),
\qquad
\theta_C(r)\sim\kappa^{-1}r^{1-P}\quad(r\to\infty).    \tag{4}
$$

In particular the left leading term is $r/Q$. To derive it without assuming a power ansatz, put $w=1-Q\theta_C/r$. The exact level equation reads

$$
\kappa=Qr^{Q-1}\frac{A^Pw^Q}{(1-w)S^K}.
$$

It first forces $w\to0$, and then gives $w\sim c_Lr^\nu$. At infinity, the level equation first forces $\theta_C\to0$ and then gives the right law in (4). Equation (3), with $M\sim Qr$, yields

$$
\eta_C=1-\nu c_Lr^\nu+o(r^\nu),\qquad
\eta_C'\sim-\nu^2c_Lr^{\nu-1},\qquad
\lim_{r\to\infty}\eta_C=1-P.
$$

The derivative asymptotic follows directly from the exact square in (2), rather than by differentiating an unspecified little-oh term. Thus elasticity strictly decreases from $1$ to $1-P$.

## Source residues require a source condition

Away from $\xi$, let $\theta_0=Y/H$. Division gives

$$
\theta_0=\ell+mr-\frac{V}{r+h}+\frac{U}{r-\xi},\quad
m=\frac{R_3}{P(P-1)}>0,
$$

$$
U=\frac{Y(\xi)}{P(P-1)(\xi+h)},\qquad
V=\frac{Y(-h)}{P(P-1)(\xi+h)}.                       \tag{5}
$$

Positivity of all coefficients of $R$ does not imply $V>0$. For example, take $P=2,Q=1/2$ and

$$
R=\frac1{125}+\frac{111}{100}r+\frac1{20}r^2+r^3,
\quad Y=(r+1/20)(r-1/5)(r-4/5).
$$

Here $1/20<h=(\sqrt6-2)/4<1/8$, and therefore $Y(-h)<0$.

A useful sufficient source condition is $R=\lambda\prod_{i=1}^3(r+A_i)$, with $A_i\ge t=(1-Q)/P$. Since

$$
H(-t)=(1-Q)\left[Q+\frac{(P-1)(1-Q)}P\right]>0,
$$

one has $h<t$, whence $R(-h)>0$ and $Y(-h)>0$. This factor condition holds, for example, when the middle support dominates the third support coordinatewise and $s_2=Ps_1+Qs_3$, with both outer supports strictly positive.

## Exact forcing polynomial and a nonunit conditional six bound

For the formal actual ODE $F(r,z)=zT(1-Pz)/(B+Hz)$, set

$$
W=R(Y'H-YH')-YT(H-PY).
$$

Then

$$
\theta_0'-F(r,\theta_0)=\frac{W}{H^2R}.             \tag{6}
$$

Its degree is at most six, and its endpoint coefficients are

$$
w_0=QR_0[3PR_0-(1-Q)R_1+1-Q^2],
$$

$$
w_6=-PR_3[(P-1)R_2+3QR_3-(P^2-1)].                 \tag{7}
$$

If $Y(\xi)\ne0$ and $w_0w_6\le0$, then (1) has weighted root count at most six. Indeed, a nonzero polynomial of degree at most six with opposite nonzero endpoint signs has odd positive root weight, hence at most five; a zero constant or leading coefficient also reduces the available positive root weight to at most five.

For clarity, the ODE comparison is valid on each *whole* interval $(0,\xi)$ and $(\xi,\infty)$, without dividing it by probability-bound crossings. Along the source its ODE denominator is $R>0$, along the actual curve it is $M>0$, and by affine interpolation it stays positive between them. The secant of $F$ is analytic. Multiplication by its positive integrating factor turns the difference derivative into the right side of (6), times a positive factor. Weighted Rolle therefore bounds graph contacts on each interval by its forcing root weight plus one. The total is at most seven.

The total graph-contact weight is even: if $Y(\xi)>0$, each sector has identical endpoint signs; if $Y(\xi)<0$, each sector has opposite endpoint signs, giving two odd contributions. The source is negative at zero and positive and linearly growing at infinity, whereas the actual curve is positive and has the laws (4). Thus the even bound improves seven to six. If $W$ were identically zero, positive-denominator ODE uniqueness and these endpoint mismatches imply no graph contacts, and the same conclusion holds. In the nonunit case multiplying the graph difference by $H$ does not change any positive zero order.

The factor condition $A_i\ge(1-Q)/P$ makes $w_0>0$, since $R_1/R_0=\sum 1/A_i\le3P/(1-Q)$; it does not by itself supply the required sign of $w_6$.

## Unconditional unit-wall six bound

**Theorem.** If $Y(\xi)=0$, equation (1) has positive weighted root count at most six, for every positive-coefficient cubic $R$.

Write $H=(r-\xi)L$ and $Y=(r-\xi)Z$, where $L=P(P-1)(r+h)>0$ for all $r>0$, and $Z$ is quadratic. The canceled source $\theta_0=Z/L$ is analytic on the whole positive axis. The polynomial identity

$$
W=(r-\xi)^2\widehat W,
\qquad
\widehat W=R(Z'L-ZL')-ZT(L-PZ)                     \tag{8}
$$

implies $\deg\widehat W\le4$, because $\deg W\le6$. The canceled source satisfies $B+H\theta_0=R>0$, including at the wall. Consequently the same positive-denominator ODE comparison applies on all of $(0,\infty)$, with residual

$$
\theta_0'-F(r,\theta_0)=\frac{\widehat W}{L^2R}.
$$

It gives at most five weighted zeros of $\theta_C-\theta_0$. The curvature is exactly

$$
d_C=(r-\xi)L(\theta_C-\theta_0).
$$

It therefore has one additional unit-wall order, even when a graph contact coincides with that wall, for total weight at most six. There is no assumption that the wall contact is transverse. The case $\widehat W\equiv0$ is impossible: the analytic source/actual graph difference has opposite signs near zero and infinity, so it has a contact, and ODE uniqueness would force equality everywhere, contradicting its endpoint behavior.

The proof uses neither a simple-root perturbation nor a multiplicity boundary closure. In a genuine positive-support affine chart to which the two normal Rolle reductions apply, this curvature bound supplies the corresponding original weighted-eight bound. Identifying all nongeneric ONE-EDGE source words with this chart remains a separate scope question.

The unrestricted nonunit positive-cubic curvature-six assertion is left open here. Root-count discovery and the stronger one-wall inequality in the separate radial lane are not used as a theorem input in this note.
