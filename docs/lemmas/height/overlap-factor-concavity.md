# A common log-concave factor for every overlapping fork row

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Exact scope

Take the original fork source

$$
f(t)=1-E_0t^{-A}(1-t)^{-B}-E_1t^a(1-t)^{b+q}-E_2t^{a+p}(1-t)^b,
\qquad A,B,a,b,p,q,E_0,E_1,E_2>0.
$$

Let $\mathscr D=t(1-t)d/dt$, $\ell_0=-A+(A+B)t$,
$\ell_1=a-(a+b+q)t$, $\ell_2=a+p-(a+b+p)t$, and
$P_i=\ell_i^2+\mathscr D\ell_i$. Define

$$
R=\ell_1P_2-\ell_2P_1,\qquad
H=\det\begin{pmatrix}1&1&1\\\ell_0&\ell_1&\ell_2\\P_0&P_1&P_2\end{pmatrix},
\qquad K=H-R.
$$

Assume a strict generic row with $p\ne q$ and a point where
$R<0$ and $K<0$. All three cubics have positive physical endpoint
values. Thus each has two simple physical roots, and the remaining root of
$R$ and $H$ is exterior. Denote the exterior roots in the ORIGINAL
coordinate by $\xi_e$ and $\eta_e$.

Then the exterior $R$-root lies closer to $(0,1)$ than the exterior
$H$-root. Consequently

$$
v(t)=t^A(1-t)^B\frac{t-\xi_e}{t-\eta_e},\qquad 0<t<1,
$$

is positive and strictly log-concave. A positive constant multiplying $v$
does not change this conclusion.

The overlap condition is essential. Two physical roots of $R,H$ alone
do not imply the theorem; an exact counterexample with $K>0$ is retained
by the numeric lane.

## Two original-coordinate identities

Put $L=\ell_2-\ell_1=p+(q-p)t>0$. Direct expansion gives

$$
R=\ell_1\ell_2L+t(1-t)(aq+bp+pq),
\qquad H(A,B,a,b,p,q)=R(a+A,b+B,p,q).
\tag{1}
$$

For the second identity, subtract column 0 from columns 1 and 2 in the
three-by-three determinant, then subtract $2\ell_0$ times its second
row from its third. This leaves the pair cofactor for the shifted slopes
$\ell_1-\ell_0$ and $\ell_2-\ell_0$.

If $Q_i=\ell_iP_i+\mathscr DP_i$, the phase identity is

$$
t(1-t)(R'H-RH')-\ell_0RH
=-L\det\begin{pmatrix}\ell_0&\ell_1&\ell_2\\P_0&P_1&P_2\\Q_0&Q_1&Q_2\end{pmatrix}.
\tag{2}
$$

The determinant on the right has degree at most six. Thus the raw degree
seven phase numerator includes a positive linear factor which must be
removed when applying the critical-point degree bound. The identity is
verified from the source slopes, not from stored cofactor expansions.

## Centered physical pencil

Use the actual source coordinate

$$
s=\frac{qt}{p(1-t)+qt},\quad g=\frac Ap,\quad h=\frac Bq,
\quad\alpha=\frac ap>0,\quad\beta=\frac{b+q}q>1,
$$

$$
x=-g+(g+h)s,\quad r=\frac{\alpha+\beta}{g+h}>0,
\quad\rho=2(\alpha-rg)+1.
$$

Divide the original cubics by $L^3$, a positive factor physically. The
normalized cores are

$$
T=(g+h)s(1-s)\left(\frac{1-s}{p}+\frac{s}{q}\right),
\quad e=\frac{\rho^2-1}{4r(r+1)},\quad S=x^2-e,
$$

$$
P=T-\rho x+(2r+1)x^2,\quad
R=r[P-(r+1)S],\quad H=(r+1)[P-rS],\quad K=P.
\tag{3}
$$

For $p>q$,

$$
T=\kappa(x+g)(h-x)(x+\zeta),\qquad
\kappa=\frac{p-q}{pq(g+h)^2}>0,
\quad\zeta=\frac{qh+pg}{p-q}>g.
\tag{4}
$$

The normalized $R,H$ have negative cubic leading coefficient and two
simple physical roots. Their third roots therefore lie to the right of
$h$. At the exterior $R$-root $r_e$, (3) gives
$H(r_e)=(r+1)(r_e^2-e)$. It suffices to show $r_e^2>e$, because then
$H(r_e)>0$, and its unique exterior root lies strictly farther to the
right.

If $e\le0$, this is immediate. Suppose $e>0$ and put
$\delta=\sqrt e>0$. At a joint negative point, $K<0$ implies that
$\rho$ and $x$ have the same sign. If $x>0$, then $\rho>1$,
and $\beta=rh-(\rho-1)/2>1$ gives

$$
h>\frac{\rho+1}{2r}>\delta.
$$

Thus $r_e>h>\delta$. Only a negative joint point needs a new inequality.

## The negative joint point

Write $\rho=-u<-1$, $c=2r+1$, and

$$
a_0=\frac{u+1}{2r},\qquad b_0=\frac{u-1}{2r},
\quad a_0-b_0=\frac1r,
\quad\delta^2=\frac{ra_0b_0}{r+1}.
$$

The source condition $\alpha>0$ gives $g>a_0>\delta$. At a joint
negative point $x=-y$, (3) gives the strict upper bounds

$$
0<T(-y)<\min\{A_0(y),B_0(y)\},
$$

$$
A_0(y)=r(y-b_0)(a_0-y),\qquad
B_0(y)=y(u-cy).
\tag{5}
$$

In particular $b_0<y<a_0$ and $y<u/c$. Hence $b_0<u/c$,
which is equivalent to $u<c$. This proves $\delta<1$ and

$$
b_0<\delta<\min(a_0,u/c).
\tag{6}
$$

For example, $\delta^2-b_0^2=b_0(1-b_0)/(r+1)>0$, and
$u^2-c^2\delta^2=1-\delta^2>0$. The inequality
$a_0>\delta$ also follows directly from the displayed definition.

If $h\ge\delta$, again $r_e>h\ge\delta$. Suppose $h<\delta$.
From the actual factorization (4),

$$
\frac{-T(\delta)}{T(-y)}
=\frac{g+\delta}{g-y}\frac{\zeta+\delta}{\zeta-y}
 \frac{\delta-h}{h+y}
<\frac{\delta}{y}
 \left(\frac{a_0+\delta}{a_0-y}\right)^2.
\tag{7}
$$

All denominators are positive. The first two factors decrease as their
positive parameter increases; use $\zeta>g>a_0>y$. The last factor is
strictly less than $\delta/y$.

Define

$$
M(y)=\frac{\min(A_0(y),B_0(y))}{y}
 \left(\frac{a_0+\delta}{a_0-y}\right)^2.
$$

The exact identity
$A_0-B_0=(r+1)(y^2-\delta^2)$ shows that the first branch is used for
$y\le\delta$, the second for $y\ge\delta$. The first is strictly
increasing: apart from a positive constant its derivative is that of

$$
\frac{y-b_0}{y(a_0-y)},\quad
\frac d{dy}\frac{y-b_0}{y(a_0-y)}
=\frac{(y-b_0)^2+b_0(a_0-b_0)}{y^2(a_0-y)^2}>0.
$$

The second is strictly decreasing for $y\ge\delta$: apart from a
positive constant its derivative has the sign of
$y_0-y$, where $y_0=2u/c-a_0$, and

$$
y_0=\frac{2r-1}{c}b_0-\frac1{rc}
<\frac r{r+1}b_0<\delta.
$$

The first strict inequality uses
$r/(r+1)-(2r-1)/c=1/[c(r+1)]>0$. Therefore $M(y)\le M(\delta)$.

Finally,

$$
(u+c\delta)(a_0-\delta)^2-(u-c\delta)(a_0+\delta)^2
=2\delta\{c(a_0^2+\delta^2)-2ua_0\},
$$

$$
c(a_0^2+\delta^2)-2ua_0
=\frac{(u+1)(u+2r+1)}{4r^2(r+1)}>0.
\tag{8}
$$

Thus $M(\delta)<u+c\delta$. Combining (5), (7), and (8) gives
$-T(\delta)<\delta(u+c\delta)$, so

$$
R(\delta)/r=P(\delta)=T(\delta)+\delta(u+c\delta)>0.
$$

Since the unique exterior $R$-root follows $h$, this proves
$r_e>\delta$. Hence $R$'s exterior root precedes $H$'s.

## Return to the original coordinate

For $p>q$, the inverse map

$$
t(x)=\frac{p(x+g)}{qh+pg+(p-q)x}
$$

is increasing for $x>h$ and sends that interval into $t>1$.
Thus $1<\xi_e<\eta_e$. It follows that

$$
(\log v)''=-\frac A{t^2}-\frac B{(1-t)^2}
-\frac1{(t-\xi_e)^2}+\frac1{(t-\eta_e)^2}<0.
$$

Reflection $t\mapsto1-t$, combined with exchange of the two positive
support functions, exchanges $p,q$, swaps $A,B$ and $a,b$, and
preserves $R,H,K$ up to the stated positive normalizations. It therefore
covers $p<q$, with $\eta_e<\xi_e<0$. The same logarithmic-curvature
inequality follows. No rootword or side/gap orientation remains in this
external-factor theorem.
