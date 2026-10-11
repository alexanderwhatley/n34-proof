Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Statement and scope

Let $s_1=(a_1,b_1)$ and $s_3=(a_3,b_3)$ have strictly positive coordinates and distinct modes. Relabel so $\gamma=a_3b_1-a_1b_3>0$, and let $s_2=P s_1+Q s_3$, where $P,Q>1$. The outer supports need not be a coordinate antichain, have equal degrees, or have reflection symmetry. Put $d_i=a_i+b_i$ and

$$
H(r)=P(P-1)r^2-2PQ r+Q(Q-1),\quad
R(r)=\frac{(d_1+r d_3)(a_1+r a_3)(b_1+r b_3)}{\gamma^2},
\quad B(r)=r(1+r),\quad Y=R-B.
$$

Write $0<\eta<\xi$ for the two roots of $H$. Assume only

$$
\boxed{Y(\eta)<0,\qquad Y(\xi)<0.} \tag{1}
$$

Then every positive-coefficient mixture on these supports has at most **six contacts with every positive level, counting multiplicity**:

$$
Z_{(0,1)}\left(\sum_{i=1}^3 E_i x^{a_i}(1-x)^{b_i}-L\right)\le6,
\qquad E_1,E_2,E_3,L>0. \tag{2}
$$

The bound is sharp. There is no residue-balance inequality, seam-edge regularity hypothesis, or simplicity hypothesis on forcing, curvature, or original contacts.

Condition (1) is exactly that both origin-wall ratios $\sigma=V_1/[x(1-x)]$ exceed one. This closes the entire strict high-high strong-fork region, including ratios between one and three and comparable positive outer supports. It does not claim mixed or low-low wall closure, unit walls, negative supports, or the whole $(3,1)$ chamber.

The new input is monotonicity of the entropy on each exterior source seam. Its algebra needs only the four strictly positive coefficients of $R$; the three negative roots of the geometric source cubic are not used.

## fixed-entropy reduction

For each actual original coefficient tuple and level there is one common entropy constant

$$
C=\sum_i\alpha_i\log E_i-\log L,\qquad
\alpha=(P,-1,Q)/(P+Q-1).
$$

The fixed-wall chart supplies one analytic graph $u_C(r)$, $r>0$, with

$$
0<u_C<\min(1/P,r/Q),\qquad
(p_1,p_2,p_3)=\frac{(1-Pu_C,u_C,r-Qu_C)}
{1+r-(P+Q-1)u_C}.
$$

Its source-independent differential equation is

$$
u_C'=F(r,u_C),\qquad
F(r,u)=\frac{u(1-Pu)[Q-(P-1)r]}{B(r)+H(r)u}. \tag{3}
$$

Its second derivative has the strict sign of $H$. Thus $u_C$ is convex on the exterior wall intervals and concave centrally.

The original normal-curvature contact equation is

$$
B+Hu_C=R. \tag{4}
$$

Since (1) excludes contacts at either wall, this is equivalent, with the same analytic contact orders, to $u_C=u_0$, where $u_0=Y/H$, on each wall interval.

The entropy function is

$$
(P+Q-1)J(r,u)=P\log(1-Pu)-\log u+Q\log(r-Qu)
-(P+Q-1)\log(1+r-(P+Q-1)u). \tag{5}
$$

The entropy chart gives $J_u<0$ in the probability domain and $J_r+J_uF=0$. Hence, on a physical source seam,

$$
\frac{d}{dr}J(r,u_0(r))
=J_u(r,u_0)\,[u_0'-F(r,u_0)]. \tag{6}
$$

We prove that the bracket is strictly negative on the left exterior arc and strictly positive on the right one.

## Scalar concavity beyond the probability bounds

Fix $0<r<\eta$. Put $a=P(P-1)$ and $j=Q-(P-1)r>0$. Direct differentiation gives

$$
F_{uu}(r,u)=-\frac{2jB(PB+H)}{(B+Hu)^3}<0
\quad\text{for }u>-B/H. \tag{7}
$$

Indeed $PB+H=(Pr-Q)(Pr-Q+1)>0$, because
$\eta<(Q-1)/P$; the latter follows from $H((Q-1)/P)<0$.
Thus $F$ is strictly concave on the entire formal interval where its denominator is positive, even where the source probability bounds fail.

For fixed $r$, both $u_0=(R-B)/H$ and $u_0'$ depend affinely on the source coefficients. Consequently

$$
\Phi(R)=u_0'-F(r,u_0) \tag{8}
$$

is convex on any convex set of nonnegative-coefficient sources with $R(r)>0$. This extension to formal nonphysical values is essential: intermediate source seams in the scale argument need not obey the bounds.

## Exact unit-left-wall comparison

The companion theorem "[unit left wall positive cubic entropy comparison](unit-left-wall-positive-cubic-entropy-comparison.md)" proves:

$$
R(\eta)=B(\eta),\quad R(\xi)\le B(\xi),\quad
R=\sum_{i=0}^3c_i r^i,\ c_i\ge0
\quad\Longrightarrow\quad \Phi(R)\le0 \text{ on }(0,\eta), \tag{9}
$$

with equality only for $R=B$.

Its geometric reduction is short. Let $z=\xi/\eta>1$, $t=B(\xi)/B(\eta)$, so $z<t<z^2$, and $w_i=c_i\eta^i/B(\eta)$. The source constraints form the clipped simplex

$$
w_i\ge0,\quad\sum_iw_i=1,\quad\sum_iw_i z^i\le t.
$$

Its six vertices are the pure constant and pure linear source, and the four wall-saturating edge mixtures with degrees $(0,2),(0,3),(1,2),(1,3)$. Their seams are:

| Vertex | Source seam $u_0$ | Sign of $\Phi$ |
|---|---|---|
| Constant | $(1+\eta+r)/[a(\xi-r)]$ | Strictly negative |
| Linear | $r/[a(\xi-r)]$ | Strictly negative |
| $(0,2)$ | $1/(2PQ)$ | Strictly negative |
| $(0,3)$ | $\ell_0+\ell_1r$, both coefficients positive | Strictly negative |
| $(1,2)$ | $0$, corresponding to $R=B$ | Zero |
| $(1,3)$ | $r/(2PQ)$ | Strictly negative |

The constant, linear and $(0,3)$ signs have coefficientwise positive-polynomial certificates, using the rational wall parameterization

$$
P=\frac{S(S+2)}{(\xi-\eta)^2},\quad
Q=\frac{S(2\eta\xi+S)}{(\xi-\eta)^2},\quad S=\eta+\xi,
$$

and $\eta=r+a_0,\xi=r+a_0+b_0$, $r,a_0,b_0>0$.
The three positive polynomials have 33, 17 and 78 positive integer coefficients.The other two strict signs follow from (3), and $R=B$ gives equality. Convexity (8) proves (9), strictly for every source other than $B$.

## Scale interpolation closes the previously bad left exterior

Write the actual source as $\delta S(r)$, where $S$ is a fixed cubic with strictly positive coefficients and $\delta>0$. Define $f=S/B$. If $S=c_0+c_1r+c_2r^2+c_3r^3$, the numerator of $f'$, up to a positive denominator, is

$$
N_f=c_3r^4+2c_3r^3+(c_2-c_1)r^2-2c_0r-c_0. \tag{10}
$$

Its descending coefficients have exactly one sign change. Descartes' rule, the negative constant and the positive leading coefficient prove that $f$ has exactly one simple critical point, a strict global minimum. It decreases before that point and increases afterward.

Let $q=Y(\eta)/Y(\xi)>0$. The residue comparison already makes the left exterior good whenever $q\ge(\eta/\xi)^3$: $u_0$ is strictly concave while $u_C$ is strictly convex. We only need

$$
q<(\eta/\xi)^3. \tag{11}
$$

As a function of scale,

$$
q(\delta)=\frac{B(\eta)-\delta S(\eta)}
{B(\xi)-\delta S(\xi)},\qquad
\operatorname{sgn}q'=\operatorname{sgn}[f(\xi)-f(\eta)].
$$

At zero scale,

$$
q(0)=B(\eta)/B(\xi)>(\eta/\xi)^2>(\eta/\xi)^3.
$$

Thus (11) forces $f(\eta)>f(\xi)$. The first unit scale is

$$
\delta_*=\frac{B(\eta)}{S(\eta)},\qquad
\delta_*S(\xi)<B(\xi). \tag{12}
$$

Fix a physical seam point $0<r<\eta$, $u_0(r)>0$, and put
$\delta_0=B(r)/S(r)$. Positivity and strict high-wall assumptions give

$$
0<\delta_0<\delta<\delta_* . \tag{13}
$$

Hence $f(r)>f(\eta)$. Since $r<\eta$ and $f$ has one minimum, (10) forces $f'(r)<0$. At scale $\delta_0$, $u_0=0$ and $F=0$, so

$$
\Phi(\delta_0S)
=\frac{\delta_0S'(r)-B'(r)}{H(r)}
=\frac{B(r)}{H(r)}\,\frac{f'(r)}{f(r)}<0. \tag{14}
$$

At scale $\delta_*$, (9) applies. This source has strictly positive coefficients and cannot equal $B$, whence $\Phi(\delta_*S)<0$.

Finally, $\Phi(\delta S)$ is convex in $\delta$ by (7)-(8) on the whole interval $[\delta_0,\delta_*]$: every intermediate denominator is the positive polynomial $\delta S(r)$. A convex function lies below its endpoint chord. Thus

$$
\boxed{u_0'-F(r,u_0)<0} \tag{15}
$$

at every physical point of the bad left arc. The argument does not require that arc to avoid the source's bad-curvature segment.

## Reflection closes the right exterior

Swap the outer supports, put $r=1/s$, and set

$$
\widetilde u=su,\quad \widetilde P=Q,\quad\widetilde Q=P,\quad
\widetilde R(s)=s^3R(1/s).
$$

The reversed source again has four positive coefficients, and

$$
\widetilde H(s)=s^2H(1/s),\qquad
\widetilde Y(s)=s^3Y(1/s).
$$

Multiplying (4) by $s^3$ gives exactly the reflected equation in $s,\widetilde u$. The walls are $1/\xi<1/\eta$. A bad right ratio $q>1$ becomes

$$
\widetilde q=(\eta/\xi)^3/q<(\eta/\xi)^3.
$$

The left proof therefore covers the bad right arc. Entropy and analytic contact orders are preserved; its derivative orientation reverses.

The exterior admissible-arc theorem gives one open physical source arc on each exterior wall interval. The left arc runs from $u_0=r/Q$ to $u_0=0$; the right arc runs from $u_0=0$ to $u_0=1/P$.

On a bad left arc, (6) and (15) make $J(r,u_0)$ strictly increasing. It tends from $-\infty$ at the positive-alpha bound endpoint to $+\infty$ at the negative-alpha middle-zero endpoint. Every common entropy level therefore has exactly one contact, and it is simple. Reflection gives one simple right contact on a bad right arc. On a good exterior, the opposite-curvature and endpoint-phase argument gives the same conclusion. At most one exterior can be bad, so both exterior budgets are now one.

Centrally, the high-high residue signs give $u_0''>0$, while $u_C''<0$. Their difference is strictly concave and has at most two contact weights. No contact occurs at a wall by (1). Total normal-curvature weight is therefore at most $1+2+1=4$. The two weighted normal-boundary Rolle steps add two, proving (2), including arbitrary multiplicities without perturbing multiple real roots.

The exact mixture

$$
x(1-x)^8+x^8(1-x)
+\frac{4^{18}}{25}[x(1-x)]^{18}-\frac1{40}
$$

has six distinct simple zeros. Its supports are $(1,8),(18,18),(8,1)$, with $P=Q=2$, and both wall ratios are $441/97>1$. It proves sharpness.

Strict high-high is the exact scope. Unit walls need separate accounting for automatic curvature contacts; mixed and low-low sources remain outside this note.
