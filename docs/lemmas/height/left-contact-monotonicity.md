# Negative-C left contact heights decrease throughout the whole negative-n source

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Retain $0<h<1$, $H=1-h$, $m>0$, $p>r_3>r_2>r_1>m/h$, and $\Pi=\Lambda\prod_i(p-r_i)>0$. Put

$$
T=hp-m,\quad C=p(p+1)-\Pi,\quad
E=-Hhp^2+2Hmp+m(m+1),\quad D=HC+E,
$$

$$
A=-mC+pE,\quad B=(h+m)C-(p+1)E,
\quad V=uD/C,\quad u_p/u=T/\Pi.
$$

**Theorem.** At every finite point where $C<0$, $A/C>0$, and $B/C>0$, one has $V_p<0$. In particular V has no stationary point on that contact domain, without any upper bound on m.

Write $R=-C>0$ and $e=E/C$. The coefficient signs imply

$$
\frac mp<e<\frac{h+m}{p+1},\qquad E=-eR<0.
\tag{1}
$$

The source inequalities yield

$$
\sigma=\sum_i\frac1{p-r_i}>\frac{3h}{T}.
\tag{2}
$$

Set

$$
J=\Pi(EC'-E'C)-TCD.
$$

Using $E'=-2HT$ and $C'=2p+1-\Pi\sigma$,

$$
\frac{J}{\Pi C e}
=2p+1-\Pi\sigma+\frac{2HT}{e}
+\frac{TR(H+e)}{\Pi e}
<g,
$$

where

$$
g=2p+1-\frac{3h\Pi}{T}+\frac{2HT}{e}
+\frac{TR(H+e)}{\Pi e}.
\tag{3}
$$

Parameterize the interval (1) by

$$
e=\frac mp+\frac{\theta T}{p(p+1)},\qquad 0<\theta<1.
$$

With $N=T\Pi e^2g$ and $R=-E/e$, define
$F=-p(p+1)N/T^2$. Exact expansion gives a quadratic Bernstein form

$$
F=b_0(1-\theta)^2+2b_1\theta(1-\theta)+b_2\theta^2,
$$

$$
b_0=m(p+1)(Hp+m)((2-h)p+m),
\qquad
b_2=p(h+m)(Hp+m+1)((2-h)p+m+2).
\tag{4}
$$

Both are strictly positive for every m>0. To prove positivity of b1, set $q_0=m/p>0$. One has

$$
\frac{2b_1}{p}
=2q_0(H+q_0)(H+q_0+1)p^3+K_2p^2
+3h(H+q_0)p-q_0,
$$

$$
K_2=hH(2-h)+q_0(6-3h-h^2)
+q_0^2(6-h)+q_0^3>0.
\tag{5}
$$

Since E<0,

$$
p(Hh-2Hq_0-q_0^2)>q_0.
$$

And $3h(H+q_0)>Hh>Hh-2Hq_0-q_0^2$, so the last two terms of (5) have positive sum. Hence b1>0. Thus F>0, N<0 and g<0.

By (3), $J/(\Pi C e)<0$. Since $\Pi>0$, $C<0$, and $e>0$, this means J>0. Finally

$$
V_p=-\frac{uJ}{\Pi C^2}<0.
$$

No step used m<H. The conclusion is strict and applies on any connected part of the displayed positive-contact domain.

## Connectedness of the source contact domain

The exact identities

$$
A=m\Pi-pT(Hp+m),\qquad
B=(p+1)T(Hp+m+1)-(h+m)\Pi
$$

show, by the increasing source ratios Z3,Z4, that A is negative and may cross once to positive; B is positive and may cross once to negative. Thus their same-sign set is one interval, possibly empty or unbounded. Also C has exactly one left-ray zero, since $\Pi/[p(p+1)]$ strictly increases from zero to infinity. At C=0, A and B have opposite signs unless E=0. Away from that nongeneric cancellation, the positive-contact interval therefore has a constant sign of C. The negative-C positive-contact interval, if present, is connected, and V strictly decreases on its entirety.

For later root counts, generic cancellation and tangent coefficient levels can be removed by the original-function boundary transfer. They must not be silently treated as strict points of the theorem.
