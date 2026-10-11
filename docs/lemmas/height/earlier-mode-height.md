# A regional master height theorem for every u mode before the w mode

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Theorem

Let

$$
G=c_1-u+c_3v+c_4w,\qquad c_1,c_3,c_4>0,
\qquad0\prec s_u\prec s_v\prec s_w,
$$

be the actual beta family. Reflect so that, for $q=w/v$,
$\theta_q<\theta_w<\theta_v$. If $\theta_u<\theta_w$, then
$G$ has fewer than ten distinct interior roots.

In the exactly realizable source chart this is the single condition
$n>h$, subject to the usual endpoint inequalities
$0<hr_i+n<r_i$, $i=1,3$. It includes both former strict mode
regions $h<0$ and $0<h<n$, without a bound condition. The proof
does not require the old 51-monomial prefix positivity certificate or
the old mode-dependent left-branch node deletions.

It suffices to prove the generic simple-root version. The standing
original-root compact-bracket perturbation supplies the distinct-root
statement and the nongeneric auxiliary faces within this open region.
Coincident $v,q$ modes can likewise be reached by original-function
perturbation while preserving $\theta_u<\theta_w$.

The coincidence $h=0$, i.e. $\theta_u=\theta_q$, is covered
directly by the proof: E is linear and the final pole comparison simply
has one E root. The boundary $n=h$, i.e.
$\theta_u=\theta_w$, is also excluded by the same standing
original-function transfer. A small perturbation moving the u mode
strictly earlier preserves the strict support chain and, after shared
coefficient regularization, the disjoint hypothetical original-root
brackets. The regional theorem then applies. This is a transfer of
original roots, not a claim about arbitrary auxiliary multiplicities.

## 1. Uniform localization: all seven envelope nodes lie after the w mode

Suppose a generic actual row has ten roots. Before $\theta_u$,
both derivative ratios

$$
v'/u'=(v/u)(\lambda_v/\lambda_u),\qquad
w'/u'=(w/u)(\lambda_w/\lambda_u)
$$

are strictly increasing positive functions. For example, $v/u$ is
a positive-exponent beta monomial whose mode is later than
$\theta_v>\theta_u$, and $\lambda_v/\lambda_u$ increases
strictly because $\theta_v>\theta_u$. The same reasoning applies
to $w$. Their positive weighted sum increases from zero to infinity.
Hence $G'=u'(c_3v'/u'+c_4w'/u'-1)$ has one zero there, a strict
minimum. Between $\theta_u$ and $\theta_w$, one has
$u'<0$, $v'>0$, $w'>0$, so $G'>0$. Thus $G$ has at
most two roots before $\theta_w$, leaving at least eight after it.

Define $R=(u-c_1)/v$, $L_4=dR/dq$, $L_3=R-qL_4$. On the
pole-free interval $(\theta_w,1)$, Rolle applied to

$$
G/w=c_4+c_3/q-R/q
$$

gives at least seven hits of $L_3=c_3$. The exact endpoint values are

$$
L_3(\theta_w)=\frac{u(\theta_w)}{v(\theta_w)}(h-n)<0,
\qquad L_3(x)\longrightarrow-\infty\quad(x\to1^-).
$$

For a generic regular positive level $c_3$, the number of its hits
on this interval is even, so there are at least eight. Rolle then gives
at least seven zeros of $\Gamma=c_1C_0-uD_0$, all after
$\theta_w$, since
$(L_3)_x=\Gamma/(v\rho\lambda_q^2)$.

The standing global ceiling is seven. Therefore **all seven** envelope
nodes lie after $\theta_w$, and there are none elsewhere. In the
physical right chart their coordinates obey
$-1<p_i<r_1$. This argument is independent of the sign of $h$.

There are exactly eight hits of the same $L_3=c_3$ level: nine hits
would force eight stationary nodes. The seven simple stationary nodes
divide the interval into eight monotonicity pieces, each containing a
hit. Since L3 starts below c3 and its derivative is initially positive,
the odd nodes 1,3,5,7 are its maxima above the one original c3. At every
node $C_0\ne0$ generically and $\mathcal V=uD_0/C_0=c_1$.
These conclusions are derived here; no second coefficient window is
imported or used.

## 2. One common coefficient inequality at every node

Retain

$$
\begin{gathered}
H=1-h>0,\quad T=hp+n,\quad k=n-Hp=T-p,\quad
P=-\Pi>0,\quad\sigma=\sum_i1/(r_i-p),\\
C=p(p+1)+P,\quad E=-Hhp^2-2Hnp+n(n-1),\quad D=HC+E,\\
B=(h-n)C-(p+1)E,\quad
J=\Pi(EC'-E'C)-TCD.
\end{gathered}
$$

The source cone and $n>h$ imply $n>0,H>0$. The affine
$T$ is positive at both endpoints of $(-1,r_1)$:
$T(-1)=n-h>0$, $T(r_1)>0$. Thus $T>0$ throughout.

Let $a=\max(-h,0)$. The source gives the uniform bound
$\sigma>3a/T$: for $a=0$ it is immediate; for $a=-h>0$,
$p_u=-n/h>r_3$ and each reciprocal is greater than
$1/(p_u-p)=a/T$. In particular
$h+T\sigma>h+3a\ge0$.

Set $t=c_1/u>0$. Throughout the tail,

$$
\frac{t'}t=\frac TP>0,\qquad
(\log t)''=\frac{h+T\sigma}{P}>0,
$$

so $t'>0,t''>0$. Set
$B_t=(p+1)(1-t)-T$. Then

$$
B_t''=-2t'-(p+1)t''<0.
$$

The odd-node maxima derived in §1 give $B_t>0$ at nodes 1,3,5,7.
Concavity propagates this strict positivity throughout the
whole node hull, including all even nodes. At every node

$$
\boxed{B/C=B_t>0,\qquad E/C=(h-n-B_t)/(p+1)<0.}
$$

Also $B_t<(p+1)-T=1-k$. The first node's positivity gives
$k<1$ there. Since $k'=-H<0$, all nodes satisfy

$$
p>p_1:=(n-1)/H.
$$

## 3. One compulsory J root outside the node tail

On the original left ray $p>r_3$, the cubic C has one simple root
$\gamma_3>r_3$. Indeed $\Pi/[p(p+1)]$ increases strictly from
zero to infinity, since its logarithmic derivative is greater than
$3/p-1/p-1/(p+1)>0$. Let $c\in(0,\theta_q)$ be that root in
the original coordinate.

The linked gap core $D_0=\mathcal C(v/u,q)$ satisfies
$D_0(0)>0$. If $D_0(c)>0$, the height
$\mathcal V=uD_0/C_0$ starts at zero and tends to positive infinity
as $x\to c^-$. It crosses $c_1>0$ before the w mode,
contradicting §1. Generic common-root avoidance excludes
$D_0(c)=0$, so $D_0(c)<0$.

Its first zero $d\in(0,c)$ bounds a positive height interval
$(0,d)$ with zero endpoint limits. An interior positive maximum
gives a J root on $p>r_3$. This root is disjoint from all J roots
forced between the tail nodes. Also
$E(\gamma_3)=D(\gamma_3)<0$, a useful root-order consequence.

## 4. Pole-free and unused-component degree budgets

The right physical C roots, if present, are exactly two roots
$-1<\gamma_1<\gamma_2<0$. For $p\le-1$ or $p\ge0$,
$C=p(p+1)+P>0$; and

$$
C''=2+2\Lambda(r_1+r_2+r_3)-6\Lambda p>0\quad(p<0),
$$

so the negative part has at most two roots. Auxiliary collisions are
excluded generically.

If there are no physical C roots, all seven nodes lie on one continuous
height component, forcing six tail J roots; §3 supplies a seventh,
contradicting $\deg J\le6$. The same holds when $n\ge1$,
because $p_1\ge0$ puts all nodes beyond both possible C roots.

Assume now $0<n<1$ and two C roots. Since $E'=-2HT<0$ on
$(-1,r_1)$, and

$$
E(p_1)=(1-n)(n-h)/H>0,\qquad E(0)=n(n-1)<0,
$$

E has one tail root $\epsilon\in(p_1,0)$. The inequality $E/C<0$
restricts nodes to at most two C components.

If $\epsilon<\gamma_1$, those are the two C-positive exterior
components. One occupied component forces six J roots and contradicts
§3. Two occupied components force at least five J roots between nodes.
On the unused central C-negative component, E and D are negative;
$\mathcal V$ tends to positive infinity at both ends, giving an
additional interior-minimum J root. Together with §3 there are at least
seven, again impossible.

## 5. A uniform barrier when epsilon follows both C roots

Suppose $\epsilon>\gamma_2$, and write $\epsilon=-z$.
Convexity gives $C(\epsilon)>0,C'(\epsilon)>0$, hence

$$
P>z(1-z),\qquad P\sigma<1-2z,\qquad0<z<1/2.
$$

At E=0,

$$
T(1-2z)-T^2=-hz(1-z)\le az(1-z).
$$

Using $\sigma>3a/T$,
$3\{T(1-2z)-T^2\}<T(1-2z)$, so

$$
T>2(1-2z)/3,\qquad k(\epsilon)>(2-z)/3>1/2.
$$

If $D(d)=0$ for $p_1<d<\epsilon$, integration of
$E'=-2HT$ gives
$C(d)=-(\epsilon-d)\{T(d)+T(\epsilon)\}$. Since
$C'<2p+1$,

$$
C(\epsilon)<(\epsilon-d)
\{1-k(d)-k(\epsilon)\}<0,
$$

contradicting $C(\epsilon)>0$. As $D(p_1)=HP(p_1)>0$, D stays
positive up to $\epsilon$. Thus the C-negative component has no
positive-height nodes; all seven lie after $\epsilon$ in the one
C-positive component. Six J roots there plus §3 are impossible.

## 6. The overlapping case: at most one central node and two tail nodes

It remains that $\gamma_1<\epsilon<\gamma_2$. D has roots
$\delta_1\in(\gamma_1,\epsilon)$,
$\delta_2\in(\gamma_2,r_1)$, and the left-ray root from §3.
These exhaust the cubic degree. Thus central positive-height nodes lie
in $(\delta_1,\epsilon)$, and right positive-height nodes lie in
$(\delta_2,r_1)$.

At a central node, $E>0,C<0,D<0,B<0$. Put
$K=k(1-k)$, $N=(p+1)T(1-k)$, $\alpha=n-h>0$. These
inequalities give

$$
0<L=N/\alpha<P<R=K/H,
$$

and the source core satisfies

$$
J=J_0(P)+E\sigma P^2>
Q(P):=J_0(P)+3aEP^2/T,
$$

$$
J_0(P)=-EP(2p+1)-T\{p(p+1)+P\}(3HP-K).
$$

The quadratic Q is strictly concave: its leading coefficient is
$-3(HT^2-aE)/T<0$. For a=0 this is immediate; for a=-h>0,
$HT^2-aE=n(n+a)>0$. Its endpoint values are

$$
\begin{aligned}
Q(L)&=-\frac{LC(L)}{p+1}\left(N'+\frac{3aN}{T}\right)>0,
&C(L)&=-\frac{(p+1)E}{\alpha}<0,\\
Q(R)&=RE\left(2k-1+\frac{3aR}{T}\right)>0.
\end{aligned}
$$

For the lower value,
$N'+3aN/T=T(1-k)+(p+1)(h+3a)(1-k)+(p+1)TH>0$.
For the upper value, k>=1/2 is immediate (the possible zero margin
would contradict E>0). If k<1/2, the identity
$E=-hK+H(2k-1)T-HT^2>0$ forces h<0 and gives
$aR/T>1-2k+T$. Thus Q and J are positive throughout (L,R).

Every central common node is consequently upward, since
$\mathcal V_p=uJ/(PC^2)>0$. Two upward crossings of one regular
level would require a downward crossing, which is another common node
and obeys the same inequalities. Hence there is at most one central node.

On the right positive component, put $\tau=-E/C>0$,
$d=D/C=H-\tau>0$. At any stationary point of
$\mathcal V=ud$, direct differentiation gives

$$
(\log\mathcal V)''
=-\frac{h+T\sigma}{P}
-\frac{\tau}{d}(\log\tau)''
-\frac{HT^2}{P^2\tau}.
$$

The first and third terms are negative. The second is negative by a
uniform pole-distance comparison. Factor E by its real roots: one is
$\epsilon$. If h>0 its other root is before -1, since
$E(-1)=(n-h)(n-h+1)>0$; if h<0 its other root is after
$\gamma_3$, by $E(\gamma_3)<0$ and its positive leading
coefficient; if h=0 it has only the one root. For
$p\in(\delta_2,r_1)$, the C pole $\gamma_2$ is closer than
$\epsilon$. The other E root is similarly dominated by
$\gamma_1$ or $\gamma_3$, respectively. Therefore

$$
(\log\tau)''=
\sum_{i=1}^3\frac1{(p-\gamma_i)^2}
-\sum_{E(\epsilon_j)=0}\frac1{(p-\epsilon_j)^2}>0.
$$

Every stationary point on this component is a strict maximum. There
can be at most one, hence at most two hits of the regular common level
c1. Together with the one central node this allows at most three,
contradicting the seven-node saturation.

The alternatives are exhaustive. This proves the generic theorem and,
by the stated standing boundary transfer, the original distinct-root
theorem.
