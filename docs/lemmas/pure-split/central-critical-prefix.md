# Four central critical points force a negative actual-mode prefix

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. All variables are local to this document.

## Statement

Let $0<\alpha <1$, $\beta >2$, $0<x<1$, $y>0$, and $0<P<Q<S<R$. Put $\delta =\beta -\alpha $ and

$$
G(t)=\frac1{t-Q}-\frac1{t-P}+\frac1{t-R}-\frac1{t-S}
     +\frac1{t+x}-\frac1{t+y}-\frac\alpha t-\frac\delta{1+t}
$$

on the central component $(Q,S)$. Define

$$
Q_1(t)=\frac1{t-Q}-\frac1{t-P},\qquad
K(t)=Q_1(t)-\frac\alpha t+\frac\alpha{t+x}
    =Q_1(t)-\frac{\alpha x}{t(t+x)}.
$$

If $G$ has at least four distinct central zeros, then $x<y$ and **$K(t)<0$ at every central zero of $G$**.

In particular, for actual strict double-reversed support with $p>u$, $0<\alpha <1$, $\beta >2$, and interlacing $P<Q<c<S<R$, four central critical points force

$$
\boxed{K(c)<0},\qquad c=a/b.
$$

No coefficient word, $P$ collar, simple-critical hypothesis, or sign of $B1$ is required. A separate actual-support inequality $K(c)\ge0$ would therefore rule out four central critical points. Such an inequality is not asserted here.

## 1. Move all sources to one side of a positive coordinate

Use the increasing central Möbius coordinate

$$
r=\frac{t-Q}{S-t}>0,\qquad
t=\frac{Q+Sr}{1+r},\qquad
\frac{dt}{dr}=\frac{S-Q}{(1+r)^2}>0.
$$

For a source $s\ne S$ outside the open central interval, set

$$
h_s=\frac{Q-s}{S-s}\ge0.
$$

Direct subtraction gives

$$
\frac{dt}{dr}\frac1{t-s}
 =\frac1{r+h_s}-\frac1{r+1}.
$$

The source at $S$ instead transforms to $-1/(r+1)$. The sum of the eight original reciprocal charges is $-\beta $. Consequently, with $g(r)=G(t(r))dt/dr$,

$$
g(r)=\frac1r-\frac1{r+h_P}-\frac\alpha{r+h_0}
 +\frac1{r+h_{-x}}-\frac1{r+h_{-y}}
 -\frac\delta{r+h_{-1}}+\frac\beta{r+1}
 +\frac1{r+h_R}.
$$

All finite transformed poles now lie on the nonpositive axis. In particular

$$
0<h_P<h_0<h_{-x}<h_{-1}<1<h_R
$$

because $x<1$. Among the negative physical sources, $h_s$ increases as $s$ decreases; hence $h_{-y}$ occurs before or after $h_{-x}$ according as $y<x$ or $y>x$. The physical sources on the right have been incorporated without any mixed-side kernel: $S$ supplied the total-charge correction at rate one, and $R$ has rate greater than one.

## 2. The complete ordered density blocks

The identity

$$
\frac1{r+h}=\int_h^\infty\frac{dv}{(r+v)^2}
$$

represents $g$ by its cumulative charge density $w(v)$. Its first source jumps, at rates $0,h_P,h_0$, give densities $1,0,-\alpha $. The final jumps at rates $1,h_R$ give densities $0,1$.

If $y\le x$, the $-1$ charge at $h_{-y}$ occurs no later than the $+1$ charge at $h_{-x}$. The density remains negative throughout $(h_0,1)$: when the two rates are distinct its successive negative values are $-\alpha $, $-\alpha -1$, $-\alpha $, $-\beta $; if they collide the two unit jumps cancel. Thus the zero-deleted density has three nonempty sign blocks $+,-,+$.

If $y>x$, define $e=min(h_{-y},h_{-1})$ and $f=max(h_{-y},h_{-1})$. The five complete sign blocks, in increasing rate order, are

| Block | Rate support | Sign and magnitude |
|---|---|---|
| 1: left physical pair | $(0,h_P)$ | $+1$ |
| 2: near negative baseline | $(h_0,h_{-x})$ | $-\alpha $ |
| 3: unused positive run | $(h_{-x},e)$ | $+(1-\alpha )$ |
| 4: far negative baseline | $(e,1)$ | piecewise strictly negative |
| 5: right physical pair | $(h_R,\infty)$ | $+1$ |

All five supports have positive measure and are strictly ordered, with zero-density intervals deleted. The far negative block is one complete block, even when its magnitude changes internally:

- If $x<y<1$, it has density $-\alpha $ on $(h_{-y},h_{-1})$, then $-\beta $ on $(h_{-1},1)$.
- If $y>1$, it has density $1-\beta $ on $(h_{-1},h_{-y})$, then $-\beta $ on $(h_{-y},1)$.
- If $y=1$, the two negative source jumps collide and the density is $-\beta $ on $(h_{-1},1)$.

The assumption $\beta >2$ makes all these far-block magnitudes strictly positive after reversing their sign. They can therefore be integrated as a single weighted column. Equivalently, the two adjacent same-sign pieces may first be integrated separately and then positively grouped; no nonconsecutive or overlapping grouping is used.

## 3. Strict total positivity and the first-two prefix

The kernel $(r+v)^(-2)$ is strictly totally positive for increasing positive $r$ and increasing nonnegative $v$: Borchardt's identity expresses each determinant as the positive Cauchy determinant times its positive permanent. Integrating columns over disjoint ordered positive-measure supports with positive weights preserves every strict square minor by determinant multilinearity and Fubini. For the unbounded fifth block, all integrals converge; strictness already follows on any bounded positive-measure subinterval.

If $y\le x$, three distinct zeros of $g$ would give a strictly totally positive $3\times3$ block matrix annihilating $(1,-1,1)$. Its determinant is positive, a contradiction. Thus four distinct central zeros necessarily give $x<y$ and the five-block case.

At any four distinct zeros $r_1<r_2<r_3<r_4$, integrate the magnitudes of the five complete blocks to obtain a strictly totally positive $4\times5$ matrix $M$. Then

$$
M(1,-1,1,-1,1)^T=0.
$$

The [matrix prefix theorem](positive-matrix-prefix.md) with cut two gives

$$
M_{i1}-M_{i2}<0,\qquad i=1,2,3,4.
$$

Here the first two *complete* blocks have exactly the transform

$$
\frac1r-\frac1{r+h_P}
 -\frac\alpha{r+h_0}+\frac\alpha{r+h_{-x}}
 =\frac{dt}{dr}\left[Q_1(t)-\frac\alpha t+\frac\alpha{t+x}\right]
 =\frac{dt}{dr}K(t).
$$

Since $dt/dr>0$, their negative prefix implies $K(ti)<0$. Any other central zero can be included with three of the already available zeros, so the inequality holds at every central zero. No assertion about cofactor ratios or confluent rows is involved.

## 4. Actual-support specialization and scope

For the actual source, $p>u$ gives $x<1$: the exact identity

$$
A(-1)=-(p-u)(a+b)[a+b-(p-u)]<0
$$

has positive final factor since $p<b$. In the normalized actual cubic, $A(-1)$ has the sign of $x-1$; hence $x<1$. The directly calculated common-support mode identity gives $G(c)=0$, with $Q<c<S$. The root-factor statement therefore applies to $c$ whenever the actual profile has four central critical points.

This theorem gives a strictly negative prefix at the actual central point. The [mode-prefix inequality](all-coefficient-mode-prefix.md) gives the contradictory positive sign under its additional source assumptions. Their combination excludes four distinct central critical points in that stated region.
