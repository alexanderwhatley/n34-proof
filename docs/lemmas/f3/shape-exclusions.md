# Excluding large parameter regions for one event order

Use the definitions in [the reciprocal-coordinate section of the appendix](../../appendix.md#reciprocal-coordinate-height-and-regional-bounds).
This lemma applies to the order

$$
\beta<\gamma<s<\delta<\alpha.
$$

Only the polynomial $P_p$ and one necessary inequality for $R$ are
needed. The result is stronger than a statement requiring all the
properties of this event order.

## Statement

Put

$$
V=sT-W-(h+2)Y,\qquad
N_1=5Z^2-12hT+12Y.
$$

Assume that $P_p$ has one real root and two nonreal conjugate roots,
that $V>0$, and that $N_1\ge0$. None of the following regions is
possible:

| Region | Inequalities |
| --- | --- |
| 1 | $p\ge5S/2$, $r\ge p$ |
| 2 | $p\ge2S$, $r\ge2p$ |
| 3 | $p\ge S$, $r\ge3p$ |
| 4 | $p\le S$, $pr\ge3S^2$ |

In particular, regions 3 and 4 imply the single exclusion

$$
r\ge3p,\qquad pr\ge3S^2.
\tag{1}
$$

The condition $N_1\ge0$ is necessary if $R$ has six real roots.
Indeed, for their mean $\mu=-Z/6$,

$$
N_1=6\sum_{j=1}^6(\xi_j-\mu)^2\ge0.
$$

The argument uses no extra lower bound on $\lambda$. The exclusions
remain valid at equality in the displayed region inequalities.

## One common root argument

Define three quantities depending only on the shape parameters:

$$
\begin{aligned}
L&=p(r-S),\\
T_b&=qry-pq^2+\frac p4(r-y-2q-1)^2,\\
G&=p\{3q+2(r-S)\}^2-9qry,\\
K&=12hT_b-5Z^2-12Y.
\end{aligned}
$$

We first prove the following general implication:

$$
h>0,\quad L>0,\quad G\ge0,\quad K\ge0
\quad\Longrightarrow\quad
\text{the stated root conditions are impossible.}
\tag{2}
$$

Let $\beta$ be the real root of $P_p$, and write its nonreal roots
as $a+ib,a-ib$, with $b\ne0$. The endpoint identities are

$$
P_p(M)=(M-pr)(M+pq)(M+py)<0,
\qquad P_p(s)=pV>0.
$$

A monic cubic with one real root has the sign of $v-\beta$ on the
real line, since its other quadratic factor is strictly positive.
Thus $M<\beta<s$. Comparing coefficients gives

$$
L=2a+\beta,\qquad pT-Y=a^2+b^2+2a\beta.
$$

Substitution gives the exact identity

$$
4p(T-T_b)=4b^2+(\beta+pq)(2L-3\beta+3pq).
\tag{3}
$$

Because $L>0$, both $s$ and $pq+2L/3$ are positive. The identity

$$
pG=9\{(pq+2L/3)^2-Y\}
$$

shows that $G\ge0$ implies $s\le pq+2L/3$. The two factors in
the second term of (3) are strictly positive: $\beta>-pq$ and
$\beta<s\le pq+2L/3$. Hence $T>T_b$. Now

$$
N_1=5Z^2+12Y-12hT
 <5Z^2+12Y-12hT_b=-K\le0,
$$

contrary to $N_1\ge0$. This proves (2).

## Regions 1–3: ordinary positive coefficients

For each region take its constants $(c,k)$ from

$$
(5/2,1),\qquad (2,2),\qquad (1,3).
$$

Use nonnegative difference variables

$$
e=y-q>0,\qquad a_0=p-c(2q+e+1)\ge0,
\qquad t_0=r-kp\ge0.
$$

Then

$$
p=c(2q+e+1)+a_0,\qquad r=kp+t_0,\qquad y=q+e.
$$

The exact expansions of $G,K,h$ in $q,e,a_0,t_0$ have only
positive rational coefficients. Their constant terms are:

| Region | Constant term of $G$ | Constant term of $K$ | Constant term of $h$ |
| --- | ---: | ---: | ---: |
| 1 | (45/2) | (135/16) | (2) |
| 2 | (72) | (117) | (3) |
| 3 | (16) | (12) | (1) |

The full identities are recorded in
[three-cone-0231.json](../../../calculation-data/reciprocal/three-cone-0231.json).
There are 323 coefficients in these nine polynomials. Each term is its
listed rational coefficient times the monomial described by its
exponents. Because every variable is nonnegative and each constant is
positive, the identities prove $G,K,h>0$.

Also $r>S$ in all three regions, so $L>0$. Applying (2) proves
their exclusion. The calculation program
[derive_regional_0231.py](../../../calculations/derive_regional_0231.py)
constructs these exact expansions from the displayed formulas.

## Region 4: coefficients in a nonnegative basis

Put

$$
Q=q+y>0,\quad z=p/(Q+1)\in(0,1],\quad
u=2q/Q\in(0,1),\quad t=r-3(Q+1)/z\ge0.
$$

Thus

$$
p=z(Q+1),\qquad r=3(Q+1)/z+t,
\qquad q=uQ/2,\qquad y=Q-q.
$$

The quantities $zG,z^2K,zh$ are polynomials. Expand them in powers of
the nonnegative variables $Q,t$. For the bounded variables $u,z$,
use the Bernstein basis

$$
B_i^d(x)={d\choose i}x^i(1-x)^{d-i}.
$$

Its values are nonnegative on $[0,1]$, and
$\sum_iB_i^d(x)=1$. Consequently an expansion with nonnegative
coefficients proves a nonnegative value throughout that square.

The complete exact expansions are in
[curved-0231.json](../../../calculation-data/reciprocal/curved-0231.json),
and the same calculation program constructs them.

| Polynomial | Bernstein degrees in $(u,z)$ | Groups of powers of $Q,t$ | Coefficients | Least coefficient in the $Q^0t^0$ group |
| --- | --- | ---: | ---: | ---: |
| $zG$ | ((2,2)) | 9 | 81 | 16 |
| $z^2K$ | ((4,4)) | 14 | 350 | 12 |
| $zh$ | ((0,2)) | 3 | 9 | 1 |

All 440 coefficients are nonnegative. Since the basis sums to one,
the strictly positive constant groups give

$$
zG\ge16,\qquad z^2K\ge12,\qquad zh\ge1.
$$

As $z>0$, this proves $G,K,h>0$. Also
$r\ge3S/z\ge3S$, so $L>0$. Implication (2) proves region 4.

Finally, to prove (1), if $p\le S$ use region 4; if $p\ge S$
use region 3. This covers the whole region in (1).

The exact coefficient tables establish the polynomial identities; no
numerical sampling is a premise. They prove the listed regions only,
not that the entire event order is impossible.
