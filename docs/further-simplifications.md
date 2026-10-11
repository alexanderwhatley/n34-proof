# Further simplifications of the remaining polynomial arguments

The complete proof in this repository is Revision 5. The results below were
proved afterward. They shorten some of its remaining polynomial arguments,
but they do not replace every remaining configuration by one theorem. In
particular, the original arguments must still be used outside the stated
regions.

These results concern a change of variables used to study some of the
remaining cases. The [appendix](appendix.md) explains its connection to the
original geometric problem. This document gives the common definitions;
the linked documents give the proofs.

| Result | What it establishes | Proof |
| --- | --- | --- |
| Positive reciprocal height | Under the scale conditions and two specified inequalities, $h>0$. No ordering of the events is required. | [Height lemma](further-lemmas/reciprocal-height.md) |
| A bound using the sum of the roots | For one ordering of the events, the exterior contribution is at most four when $p>q+y+1$, $r\ge7p/4$, and $-Z/6\ge\sqrt{pqry}$. | [Sum-of-roots lemma](further-lemmas/exterior-root-bound.md) |
| Three simple shape exclusions | For the other ordering, three large-parameter regions are impossible under the necessary root conditions. | [Shape exclusion lemma](further-lemmas/shape-exclusions.md) |
| A curved shape exclusion | The same ordering is impossible if $r\ge3p$ and $pr\ge3(q+y+1)^2$. | [Shape exclusion lemma](further-lemmas/shape-exclusions.md) |

The sum-of-roots lemma has an analytical proof. The height and shape
lemmas use exact polynomial coefficient identities. Their proof data and
calculation programs are included; separate verification programs are not.

## Parameters and polynomials

Throughout these supplementary lemmas, the parameters satisfy

$$
y>q>0,\qquad r>p>0,\qquad -pq<M<\min(pr,qy).
$$

The additional real parameter is $\lambda$. Define

$$
\begin{aligned}
h&=p+r-q-y-3, &Y&=pqry,\\
D&=pr(q+y)-qy(p+r),
&Z&=(q+y+1)(p+r-1)-pr-qy,\\
T&=\lambda-2M-D, &W&=M(\lambda-M).
\end{aligned}
$$

Here $h$ is a quantity in this particular change of variables. It is
not the height in every other section of the proof. Put

$$
s=\sqrt Y,\qquad S=q+y+1,\qquad \mu=-Z/6.
$$

The four event polynomials are

$$
P_k(v)=(v^2-Y)(v+k^2)
 +k\{-(h+2)v^2+Tv-W\},
\qquad k\in\{p,r,-q,-y\}.
$$

An **event** in these documents means a real zero of one of these
polynomials with $v>M$. Thus the word describes an algebraic boundary
value, rather than a new geometric object. When each polynomial has
exactly one such zero, write it as

$$
\beta\ (P_p),\quad \gamma\ (P_r),\quad
\delta\ (P_{-q}),\quad \alpha\ (P_{-y}).
$$

The two remaining orders considered here are

$$
\beta<\gamma<s<\delta<\alpha
\quad\text{and}\quad
\alpha<\delta<s<\gamma<\beta.
$$

Some earlier calculations call these orders `0231` and `1320`,
respectively. These labels are only abbreviations for the displayed
inequalities. We use the inequalities in the proofs.

The degree-six contact polynomial is

$$
R(v)=v^6+C_1v^5+C_2v^4+C_3v^3+C_4v^2+C_5v+C_6,
$$

where

$$
\begin{aligned}
C_1={}&Z,\\
C_2={}&hT-Y,\\
C_3={}&(1-h)W-2T^2-DT-Y(h^2+h-2+2Z),\\
C_4={}&(5T+2D)W+Y(h+2)(3T+2D)-Y^2,\\
C_5={}&-3W^2-Y(3h+7)W-YT(T+D)+Y^2(Z-h-2),\\
C_6={}&Y(WT+Y^2).
\end{aligned}
$$

Calling a zero of $R$ a **contact** agrees with the geometric
interpretation in the appendix. In these documents a *physical* zero
simply means a real zero satisfying $v>M$. The identity

$$
R(M)=(M+qr)(pr-M)(M+pq)(M+yr)(qy-M)(M+py)>0
$$

follows from the parameter inequalities. If all six zeros are real,
their mean is $\mu$, by the coefficient of $v^5$.

To state the necessary coefficient inequalities, expand

$$
R(M+x)=x^6-E_1x^5+E_2x^4-E_3x^3+E_4x^2-E_5x+E_6.
$$

With $C_0=1$, this means

$$
E_j=(-1)^j\sum_{i=0}^j C_i
 {6-i\choose6-j}M^{j-i}.
$$

If all six contacts are physical, each $E_j$ is a positive elementary
symmetric sum of their distances from $M$. Newton's inequalities for
these six positive distances include

$$
N_2:=8E_2^2-15E_1E_3\ge0,\qquad
N_3:=9E_3^2-16E_2E_4\ge0.
$$

These are necessary inequalities. Assuming them alone does not assert
that $R$ has six physical roots.

## How to use these results

First apply the height lemma if its extra scale conditions hold. For the
order $\alpha<\delta<s<\gamma<\beta$, apply the sum-of-roots lemma
when its three shape inequalities hold. For the other order, eliminate
the regions in the shape exclusion lemma. Retain the original argument
for every remaining parameter configuration.

The later results do not prove that the two entire event orders are
impossible. They also do not justify deleting all the original appendix
cases. The complete proof does not depend on that unfinished stronger
claim.
