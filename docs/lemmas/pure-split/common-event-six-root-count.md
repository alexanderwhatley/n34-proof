# One divisor theorem for the short mixed words and every common-event face

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## 1. Literal statement

Let

$$
a_1=-U<0<a_2<a_3,\qquad b_3<0<b_1=v<b_2,\qquad U,v>0.
$$

Put $w=x(1-x)$, $\mathcal D=w\,d/dx$,
$h_i=x^{a_i}(1-x)^{b_i}$, $\lambda_i=a_i-(a_i+b_i)x$,
$L_{21}=\lambda_2-\lambda_1$, and $L=\lambda_3-\lambda_2$.
The **actual source polynomials**, of degree at most three, are

$$
\begin{aligned}
P_1&=(\mathcal D\lambda_2)L_{21}
      -\lambda_2(\lambda_1L_{21}+\mathcal DL_{21}),\\
P&=P_3=\lambda_2(\lambda_3L+\mathcal DL)
      -(\mathcal D\lambda_2)L,\\
G&=(\lambda_3-\lambda_1)L_{21}L
     +(\mathcal DL)L_{21}-(\mathcal DL_{21})L.
\end{aligned}                                                    \tag{1}
$$

* $P_3$ has exactly one odd-multiplicity root in $(0,1)$; or
* $P_3$ and $G$ have a common root in $(0,1)$.

Then, for every $\kappa>0$,

$$
\boxed{Z_{(0,1),\mathrm{mult}}(P_3-\kappa h_1G)\le6.}              \tag{2}
$$

No event order, physical $G$ simplicity, numerator simplicity, initial pole topology, source common-freeness, exterior reality, or degree-cell condition is a premise. The first shape includes a sole simple numerator root, a sole triple numerator root, and a simple numerator root together with a distinct double numerator root. The second shape includes common-event faces even when $P_3$ has three distinct simple physical roots. Integer exponent walls are included literally.

## 2. Automatic source interfaces and finite even contact weight

The actual identities are

$$
LP_1+L_{21}P=\lambda_2G,
\qquad Q:=w(P'G-PG')-\lambda_1PG=-LK,
\qquad \deg K\le6.                                               \tag{3}
$$

Here $K$ is a polynomial and

$$
K(0)=a_1a_2a_3(a_3-a_2)(a_3-a_1)(a_2-a_1)<0.                     \tag{4}
$$

In particular $K$ is nonzero. Throughout the physical interval,
$L>0$, $\lambda_1<0$, and $\lambda_3>0$. Endpoint values satisfy

$$
P_1(0),P_1(1)>0,\quad P(0),G(0)>0,\quad P(1),G(1)<0.
$$

At $c=a_2/(a_2+b_2)$, one has $P_1(c)<0<P(c)$.
The two sign changes force two odd physical roots of $P_1$, one on either side of $c$. Their multiplicities are both one: an order at least three at either, or any additional even root, exceeds the cubic degree, while a third odd root contradicts equal endpoint signs. Thus automatically

$$
r_A<c<r_B,\qquad P_1\text{ has precisely these two simple physical roots.}
$$

The additional exact identity

$$
P=\lambda_2\lambda_3L+w(a_3b_2-a_2b_3)                           \tag{5}
$$

shows $P>0$ on $(0,c]$. Indeed $\lambda_2\ge0$ there, and
$a_3b_2-a_2b_3>0$. Hence every physical $P$ root lies right of $c$.
If $P(q)=G(q)=0$, (3) gives $P_1(q)=0$, so necessarily $q=r_B$.
There is at most one distinct physical common root. Since

$$
\lambda_2G-L_{21}P=LP_1
$$

has a right side of exact order one at $r_B$, both polynomials cannot have order at least two there. Consequently every actual common event satisfies

$$
\min(\operatorname{ord}_{r_B}P,\operatorname{ord}_{r_B}G)=1.        \tag{6}
$$

Set $S=P-\kappa h_1G$. As $x\to0+$, $h_1\to+\infty$, while
$P(0),G(0)>0$, so $S<0$ in an endpoint collar. As $x\to1-$,
$h_1\to0$ and $P(1)<0$, giving the same sign. Thus $S$ is a nonzero real analytic function with no roots in either endpoint collar. Compact analytic root isolation gives finitely many physical roots of finite order. Their total multiplicity $N$ is even: every odd-order zero changes sign, and the two endpoint signs agree. A failure of (2) therefore means $N\ge8$.

## 3. No common event: numerator defects pay for their topology

Suppose $P,G$ are physically common-free and $P$ has exactly one odd physical root $p$. Any further physical numerator root is even; because $\deg P\le3$, it can only be one distinct double root. All $S$ roots are positive-level contacts of

$$
Y=\frac{P}{h_1G},\qquad
Y'=\frac{-LK}{w h_1G^2},                                         \tag{7}
$$

with their original multiplicities. Such contacts lie away from every numerator zero and pole.

Count odd- and even-order physical $G$ poles by $o,e$. Classify an even pole by the sign of $Y$ on its two sides, giving $e_+,e_-$, and put
$d=\sum_g(\operatorname{ord}_gG-1)$. Let $a_+,a_-$ count even numerator roots by the sign of $Y$ on either side. Each such root is double.

First ignore the even numerator events in the sign sweep. They do not change its signs. The positive signs at both physical endpoints, the sole odd numerator sign flip, and the $o$ odd pole flips give

$$
q_0=\frac{o+3}{2}+e_+,
\qquad t_0=\frac{o-1}{2}+e_-.                                    \tag{8}
$$

Here $q_0$ is the positive-component count before those numerator events are inserted. Every negative component is interior; precisely one has the odd numerator event as an endpoint, and the remaining $t_0$ components have two $G$-pole endpoints. Inserting an even numerator root in a positive component splits that component once. Inserting one in a negative component destroys at most one pole-to-pole component: it either splits such a component into two pieces with a numerator endpoint or lies in a component already lacking two pole endpoints. Thus the actual counts obey

$$
q=q_0+a_+,\qquad t\ge t_0-a_-.                                  \tag{9}
$$

Weighted Rolle on the positive components supplies at least $N-q$ ordinary $K$ weights. To see the multiplicity statement directly, contacts of orders $m_1,\ldots,m_j$ on one occupied component contribute $\sum_i(m_i-1)$ derivative weights at the contacts and at least $j-1$ further weights between successive contacts; their sum is $\sum_i m_i-1$. Summing over components gives the stated lower bound even when some components are empty.

At a $G$ pole $g$ of order $r$, write $G=(x-g)^rH$. Common-freeness and (3) give

$$
Q=-r w(g)P(g)H(g)(x-g)^{r-1}+O((x-g)^r).
$$

The leading coefficient is nonzero, so the exact pole contribution to $K$ is $r-1$, totaling $d$. At an even numerator zero $q$, write $P=(x-q)^2A$. Then

$$
Q=2w(q)A(q)G(q)(x-q)+O((x-q)^2),
$$

so it contributes one exact $K$ weight, totaling $a_++a_-$.
Each remaining negative pole-to-pole component contributes an additional interior $K$ weight: $1/Y=h_1G/P$ is continuous with zero values at its two pole endpoints, nonzero and negative inside, and its interior derivative is a nonvanishing factor times $K$. Ordinary Rolle applies. These contributions, the numerator defects, the pole defects, and the positive-component critical weights are disjoint.

Combining (8)–(9) gives the single divisor budget

$$
\begin{aligned}
\deg K
&\ge N-q+d+t+a_++a_-\\
&\ge N-q_0+d+t_0\\
&=N-2+(d-e)+2e_-\\
&=N-2+2\sum_g\left\lfloor
       \frac{\operatorname{ord}_gG-1}{2}\right\rfloor+2e_-
\ge N-2.                                                        \tag{10}
\end{aligned}
$$

A triple odd numerator root contributes two additional $K$ weights, which may simply be omitted from this lower bound. No numerator/pole ordering table or topology dispatch occurs in (10).

## 4. Any common event: cancel once and count analytic intervals

Suppose instead that $P,G$ have a common physical root $q$. Section 2 identifies it uniquely as $r_B$ and proves (6). Factor once:

$$
P=(x-q)A,\quad G=(x-q)B,\quad
S=(x-q)T,\quad T=A-\kappa h_1B.
$$

The quadratics $A,B$ are physically common-free. This includes $q$, since the smaller original root order is one, and every other point, since there is no other original common root. Also

$$
Q=(x-q)^2\widehat Q,\qquad
\widehat Q=w(A'B-AB')-\lambda_1AB.
$$

Because $L(q)>0$, polynomial divisibility in (3) gives

$$
K=(x-q)^2\widehat K,\quad \deg\widehat K\le4,
\quad \widehat Q=-L\widehat K.                                  \tag{11}
$$

The residual analytic function $T$ has positive sign near zero and negative sign near one. Its finite total physical root multiplicity is $M=N-1$, an odd number. At every $T$ root, $B\ne0$; otherwise physical common-freeness would force an impossible simultaneous $A$ zero. Consequently every residual root is a contact of

$$
V=A/(h_1B),\qquad V'=-L\widehat K/(w h_1B^2).
$$

A polynomial $B$ of degree at most two has at most two distinct physical roots, and hence $V$ has at most three analytic continuity intervals. Numerator zeros do not split these intervals: $V$ remains analytic through them, so weighted Rolle may run across a zero or sign change of $V$. Applying weighted Rolle to all residual contacts yields at least $M-3$ physical $\widehat K$ weights. The two forced $K$ weights at $q$ add to these, even if $T$ also has a root at $q$, since orders add in the polynomial factorization (11). Thus

$$
Z_{(0,1),\mathrm{mult}}(K)
\ge 2+(M-3)=N-2.                                                \tag{12}
$$

This common-event argument requires no hypothesis about the number or orders of physical $P$ roots. In particular it covers common events on the long three-numerator-root words as well as the short words.

## 5. One saturation contradiction finishes both entries

If (2) fails, the even root weight is $N\ge8$. Either (10) or (12), according to whether there is a common event, supplies at least $N-2\ge6$ physical $K$ weights. The nonzero degree-six polynomial therefore has **exactly six physical roots counted with multiplicity**, and $N=8$.

Apply the [actual reciprocal root geometry theorem](reciprocal-root-geometry.md). Its only premises are this physical sextic exhaustion and the strict actual source cone; it has no event-word, common-freeness, pole-simplicity, numerator-simplicity, or degree-cell premise. It proves that both $P$ and $G$ have one simple physical root and two real exterior roots, with their required endpoint signs. The proof uses a shared positive reciprocal witness and a cubic root budget, rather than the old A/B atlas.

The **all-positive-exponent Hurwitz six-root theorem** now gives
$Z_{\mathrm{mult}}(P-\kappa x^{-U}(1-x)^vG)\le6$, contradicting $N=8$.
It allows common roots, repeated exterior roots, and all positive $U,v$, including every integer wall. This proves (2). No generic root perturbation, root simplicity assumption, Cauchy critical count, height comparison, or new computer-algebra positivity certificate is used.

The two analytical dependencies are:

## 6. Original-proof scope

For simple physical source events and a sole physical $P_3$ root, its location right of $c$ leaves exactly the canonical orders `113` and `131`. The theorem eliminates routing between them and includes their merged common event, every multiple physical $G$ pole, a sole triple numerator event, and the double-numerator seams allowed by its one-odd-root hypothesis. The common-event branch additionally covers every strict actual physical $P_3/G$ collision face, even on the three-simple-numerator-root words.

For the opposite oriented source cone, reset labels and reflect the actual source into the canonical cone. Canonical $P_3$ is then the negative of the opposite source $P_1$, and canonical $h_1$ is the opposite $h_3$. The identical ceiling applies to the auxiliary ratio residual $-P_1-\kappa_1h_3G$ under the reflected one-odd-$P_1$-root or common-$P_1/G$-event condition. This includes words `133` and `313`; it is an actual source reflection, not an assertion that unchanged `131` data has identical bounds for both profiles.

Common-free sources with three simple physical $P_3$ roots remain outside this theorem. A covered collision face is not the full closure of its long event order. Weak support boundaries and other support families also remain outside its literal strict-support scope. No raw six-root bound for $R=h_1P_1+\rho h_3P_3$ is asserted.
