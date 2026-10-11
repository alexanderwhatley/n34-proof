# Positive height in the reciprocal coordinates

Use the parameters and coefficients in
[Further simplifications](../further-simplifications.md). The purpose of
this lemma is to rule out $h\le0$ without dividing the possible event
orders into separate cases. The proof combines elementary inequalities
with two exact positive coefficient expansions.

## Statement

In addition to the strict parameter inequalities, assume

$$
A:=p+q>4,\qquad \lambda>A(M+yr).
\tag{1}
$$

If

$$
E_1,E_2,E_3>0,\qquad
8E_2^2-15E_1E_3\ge0,\qquad
9E_3^2-16E_2E_4\ge0,
\tag{2}
$$

then $h>0$. There is no assumption about the ordering of the events,
the nonreal roots of their cubics, or the sign of $E_4$.

The coefficient conditions in (2) are necessary when all six zeros of
$R$ are real and greater than $M$. This lemma does not assert height
positivity for every choice of the parameters without (1) and (2).

Assume $h\le0$ for a contradiction. In the proof below set

$$
v=-h\ge0,\qquad r=p+t,\qquad y=q+e,\qquad a=A-4>0.
$$

Here $e,t>0$, and the definition of $h$ gives
$2p-2q+t-e-3+v=0$. This relation is understood in every source
identity below.

## 1. The sign of $M$

We first show $M<0$. Suppose instead that $M\ge0$. Condition (1)
gives

$$
T>(A-2)M+q\{py+r(2y-p)\}.
$$

If $p\le2y$, the right side is strictly positive. If $p>2y$, the
assumption $h\le0$ gives

$$
r\le q+y+3-p<2y+3-p<3,\qquad p<r<3,
\qquad y>q>4-p.
$$

Since $2y-p<0$,

$$
\begin{aligned}
py+r(2y-p)&>y(p+6)-3p\\
&>(4-p)(p+6)-3p=(3-p)(p+8)>0.
\end{aligned}
$$

Thus $T>0$ in either case. But

$$
E_2=hT-Y-5ME_1-15M^2<0,
$$

contradicting (2). Write $M=-n$, so $0<n<pq$.

## 2. Two bounds for the first two coefficients

Put $N=pq$ and define the upper bound

$$
F(n)=15n^2+\{v(A-2)-5Z\}n-v(Ayr-D)-Y.
$$

The exact identity

$$
F(n)-E_2=v\{\lambda-A(yr-n)\}\ge0
\tag{3}
$$

shows that $F(n)>0$. Two positive expressions will establish

$$
n>11N/15,\qquad A_\sharp:=15nE_1-14E_2>0.
\tag{4}
$$

For completeness, the required polynomial identities are given here.
Let $c=11N/15$. Then

$$
-F(0)=qG_0,\qquad -F(c)=qG_c,
$$

where

$$
\begin{aligned}
G_0={}&2tv(q+e)+p\bigg[
\frac7{11}v^2
 +a\left(\frac{27}{44}+\frac3{11}v+\frac3{44}t+\frac9{22}q\right)
 +\frac4{11}t^2\\
&+e\left(\frac{15}{22}+\frac{41}{22}v+\frac3{22}t
 +\frac12e+\frac{53}{44}q\right)
 +\frac54qv
 +p\left(\frac{45}{44}+\frac{29}{44}t+\frac2{11}q\right)
\bigg],\\[2pt]
G_c={}&2tv(q+e)+p\bigg[
a\left(\frac{11}{30}+\frac1{60}t+\frac2{15}q\right)
 +v\left(\frac{11}{15}+\frac{11}{30}q+\frac1{10}p\right)+t^2\\
&+e\left(\frac{91}{15}+\frac23t+3e+\frac{127}{30}q+\frac12p\right)
 +t\left(\frac{53}{12}q+\frac3{20}p\right)
\bigg].
\end{aligned}
$$

Both are strictly positive: use $p,q>0$, the term
$(45/44)p^2$ in $G_0$, and the term $(11/30)pa$ in $G_c$.
If $0<n\le c$, the quadratic interpolation identity

$$
cF(n)=(c-n)F(0)+nF(c)-15cn(c-n)<0
$$

contradicts $F(n)>0$. This proves the first bound in (4).

For the second, put

$$
J_*(n)=15n(6n-Z)-14F(n).
$$

Its leading coefficient is $-120$. Its endpoint values are

$$
J_*(0)=14qG_0>0,\qquad J_*(N)=qK_*\ge0,
$$

where

$$
\begin{aligned}
K_*={}&p\big[
(A-4)(A+4)+15v+14t^2\\
&\qquad+e(84+13t+42e+57q+12p)+t(68q+p)
\big]+28tvy.
\end{aligned}
$$

All its terms are nonnegative. Hence, for $0<n<N$,

$$
NJ_*(n)=(N-n)J_*(0)+nJ_*(N)+120Nn(N-n)>0.
$$

Finally (3) gives

$$
A_\sharp-J_*(n)=14v\{\lambda-A(yr-n)\}\ge0.
$$

This proves the second bound in (4). Both bounds also apply when the
scale inequality is weak, $\lambda\ge A(yr-n)$.

## 3. Varying only the scale parameter

Put

$$
\delta=N-n,\quad \lambda_0=A(yr-n),\quad
\ell=\lambda-\lambda_0>0.
$$

By (4), $0<\delta<4N/15$. Define the values at the least permitted
scale:

$$
F=E_2(\lambda_0),\quad
E_{30}=E_3(\lambda_0),\quad
L_0=2E_4(\lambda_0)-nE_{30}.
$$

The symbol $F$ now denotes this endpoint value, not the quadratic
$F(n)$ as a variable function. These are the same quantity after
fixing $n$. Exact expansion gives

$$
\begin{aligned}
E_2&=F-v\ell,\\
E_3&=E_{30}+D_3\ell+2\ell^2,\\
L:=2E_4-nE_3&=L_0+\sigma\ell,
\end{aligned}
\tag{5}
$$

where

$$
D_3=(p+7q)(er+qt)+\delta(4A-9+3v)>0,
$$

$$
\sigma=3\{-3Dn+2Yh+4Y+(h+5)n^2\}.
$$

In particular $F=E_2+v\ell>0$. A positive coefficient identity
proves $L_0>0$. Its full list of 342 terms is in
[height-floor.json](../../calculation-data/further/height-floor.json).
It states

$$
L_0=\sum_i c_i p^{\alpha_i}q^{\beta_i}
 e^{\gamma_i}t^{\tau_i}\delta^{\kappa_i}g_i,
\qquad c_i>0.
\tag{6}
$$

The possible factors $g_i$ are

$$
1,\ a,\ v,\ c_0:=4N/15-\delta,\ F,
\quad a^iv^j\ (2\le i+j\le3),
\quad ac_0,vc_0,aF,vF.
$$

They are all nonnegative. One term in (6) is a strictly positive
rational multiple of $pqt^6$, so the strict inequality follows from
$p,q,t>0$. The exact rational values, not rounded values, are part of
the identity in the data file.

Let $N_2=8E_2^2-15E_1E_3$. Throughout the interval where $E_2>0$,

$$
N_2'=-16vE_2-15E_1(4\ell+D_3)<0.
\tag{7}
$$

Thus $N_2$ decreases strictly with the scale parameter. We will show
that $N_2\ge0$ forces $L>0$.

## 4. A smaller parameter range for the remaining sign

This section gives the explicit formulas needed for the second
coefficient identity. They reduce its unbounded source coordinates to
one unbounded parameter and four bounded parameters.

Put

$$
\Delta=p-q,\qquad U=er+qt,\qquad u=U/N,
\qquad k=\delta/N,\qquad \nu=1-k.
$$

Since $e,t>0$, $u>0$. Direct expansion gives

$$
yr=N+U,\quad Y=N(N+U),\quad D=(3-v)N+\Delta U,
$$

$$
uA>|(u+4)\Delta+2v-6|.
\tag{8}
$$

For the last inequality, let $\omega=e-t=2\Delta+v-3$.
The identities

$$
U-p\omega=t(A+e)>0,\qquad
U+q\omega=e(A+t)>0
$$

give $-U/q<\omega<U/p$. Rewriting these two inequalities gives
(8).

Here are normalized formulas for the endpoint quantities. They also
define the polynomial whose sign will finish the proof:

$$
\begin{aligned}
Z&=(A^2+\Delta^2)/2-3\Delta+2+v(\Delta-1)+Nu,\\
t_0&=(A-\Delta)u+(A-2)k+v-1,\\
d_0&=3-v+\Delta u,\\
w_0&=A(u+k)+\nu,\\
f_2&=-vt_0-N(1+u)-5\nu Z+15N\nu^2,\\
c_3&=-(1+v)\nu w_0-2t_0^2-d_0t_0
 -(1+u)(v^2-v-2+2Z),\\
f_3&=-c_3-4v\nu t_0-4N\nu(1+u)-10\nu^2Z+20N\nu^3,\\
c_4&=-(5t_0+2d_0)\nu w_0
 +(1+u)(2-v)(2d_0+3t_0)-N(1+u)^2,\\
e_4&=c_4-3\nu c_3-6v\nu^2t_0-6N\nu^2(1+u)
 -10\nu^3Z+15N\nu^4,\\
f_L&=2e_4-\nu f_3,\\
\bar\sigma&=3\{-3d_0\nu+(4-2v)(1+u)+(5-v)\nu^2\},\\
\bar d&=(4A-3\Delta)u+k(4A-9+3v),\\
\bar r&=4\nu f_2-7f_3,\\
\overline{Q_R}&=-14f_L^2
 +\bar\sigma f_L(4\nu v+7\bar d)+\bar\sigma^2\bar r.
\end{aligned}
\tag{9}
$$

Here $N=(A^2-\Delta^2)/4$. Substitution in the definitions of the
coefficients gives

$$
F=Nf_2,\quad E_{30}=N^2f_3,\quad L_0=N^3f_L,
\quad \sigma=N^2\bar\sigma,\quad D_3=N\bar d.
\tag{10}
$$

We need the useful bound $u<3/4$. Because $f_2>0$, it suffices
to show that its value at $u=3/4$ is negative. Indeed

$$
f_2(u)=f_2(3/4)-H(u-3/4),
\quad H=N(6-5k)+(A-\Delta)v>0.
$$

Define five scalar polynomials in $k$:

$$
\begin{aligned}
a_*&=-15k^2+65k/4+1/2,\\
b_*&=15k^2-145k/4+39/2,\qquad d_*=17-20k,\\
P_q&=16b_*-d_*^2,\\
P_1&=b_*(28k-12)+30d_*(1-k),\\
P_0&=b_*\{16a_*+40(1-k)\}-900(1-k)^2.
\end{aligned}
$$

The exact identity is

$$
\begin{aligned}
4b_*\{-4f_2(3/4)-a_*(A^2-16)-(4k+3)(A-4)v\}
={}&\{2b_*\Delta+d_*v-60(1-k)\}^2\\
&+P_qv^2+4P_1v+4P_0.
\end{aligned}
\tag{11}
$$

All five polynomials are strictly positive for $0\le k\le4/15$.
To see this explicitly, put $\eta=15k/4$. Their Bernstein
coefficient lists are:

| Polynomial | Coefficients, in increasing basis index |
| --- | --- |
| $a_*$ | $1/2,\ 8/3,\ 113/30$ |
| $b_*$ | $39/2,\ 44/3,\ 109/10$ |
| $P_q$ | $23,\ 109/3,\ 1723/45$ |
| $P_1$ | $276,\ 3968/15,\ 6452/27,\ 15544/75$ |
| $P_0$ | $36,\ 326,\ 62624/135,\ 7598/15,\ 12316/25$ |

A list of length $d+1$ represents $\sum_i c_iB_i^d(\eta)$,
where $B_i^d(x)={d\choose i}x^i(1-x)^{d-i}$. These basis functions
are nonnegative and sum to one. Equation (11) therefore has a strictly
positive right side. Since $A\ge4$, it implies $f_2(3/4)<0$,
and hence

$$
0<u<3/4.
\tag{12}
$$

## 5. The exact sign identity

Define

$$
w=\frac{uA+(u+4)\Delta+2v-6}{2uA}\in(0,1),
$$

so

$$
\Delta=\frac{uA(2w-1)-2v+6}{u+4}.
$$

Put $V_{\max}=3+A(2+uw)$ and $\rho=v/V_{\max}$. The exact
formula

$$
p=\frac{(1-\rho)V_{\max}}{u+4}>0
$$

shows that $0\le\rho<1$. The variables for the coefficient identity
are thus

$$
a=A-4\ge0,\quad \theta=4u/3\in(0,1),
\quad \eta=15k/4\in(0,1),\quad w\in[0,1],\quad \rho\in[0,1).
$$

The complete table
[full-height-bernstein.json](../../calculation-data/further/full-height-bernstein.json)
states the exact polynomial identity

$$
-(u+4)^4\overline{Q_R}
=\sum c_{j,i,l,m,n}a^j
B_i^{11}(\theta)B_l^8(\eta)B_m^4(w)B_n^4(\rho).
\tag{13}
$$

For each $j=0,1,2,3,4$, its array has 2,625 positive coefficients
and 75 zero coefficients. Thus the 13,500 entries comprise 13,125
positive entries and 375 zeros, with no negative entries. The zero
entries occur only at the index pairs $(i,l)=(0,0),(0,1),(1,0)$.
These counts describe the full table, not a selection of its terms.

To see strict positivity on the actual domain, two $j=0$ entries
have value $1134592/35$, at indices $(i,l,m,n)=(0,2,0,0)$ and
$(0,2,4,0)$. Their contribution is

$$
\frac{1134592}{35}B_0^{11}(\theta)B_2^8(\eta)
\{B_0^4(w)+B_4^4(w)\}B_0^4(\rho)>0.
$$

The first and last factors are positive because $\theta,\rho<1$,
the second because $0<\eta<1$, and the brace because it equals
$(1-w)^4+w^4>0$. All other terms in (13) are nonnegative. Thus

$$
\overline{Q_R}<0.
\tag{14}
$$

The calculation program
[derive_reciprocal_height.py](../../calculations/derive_reciprocal_height.py)
constructs (9) and the exact coefficients in (13). Identity (13) is
the computer-algebra part of this proof. The use of a nonnegative basis
explains why its coefficient signs prove the result for a continuous
range of parameters rather than merely for finitely many samples.

## 6. Finishing the contradiction

We return to $L=L_0+\sigma\ell$. If $\sigma\ge0$, then $L>0$
immediately. Suppose $\sigma<0$, and let

$$
\ell_L=-L_0/\sigma>0,\qquad J=\sigma F+vL_0.
$$

This is the scale where $L$ vanishes. Since

$$
E_2(\ell_L)=J/\sigma,
$$

if $J\ge0$, this scale is at or beyond the endpoint where $E_2$
ceases to be positive. Thus the actual scale with $E_2>0$ has
$\ell<\ell_L$, and $L>0$.

It remains to treat $J<0$. In this case $\ell_L$ lies inside the
interval where $E_2>0$. Define

$$
Q=\sigma^2N_2(\ell_L),\qquad
Q_R=\sigma^2\{4nE_2(\ell_L)-7E_3(\ell_L)\}.
$$

Substitution in (5) and (9) gives
$Q_R=N^6\overline{Q_R}<0$. The exact identity

$$
15E_1Q_R=7Q+4J\{15nE_1\sigma-14J\}
\tag{15}
$$

compares the needed Newton expression with this negative quantity.
The sharp bound (4), applied at $\lambda_0+\ell_L$, gives

$$
15nE_1-14J/\sigma>0.
$$

Therefore the brace in (15) equals $\sigma$ times a positive
quantity and is negative. Since $J<0$, the correction term in (15)
is strictly positive. Its left side is negative, so $Q<0$.

By (7), $N_2$ is strictly decreasing throughout this interval.
Consequently every point with $N_2\ge0$ occurs before
$\ell_L$, again giving $L>0$. We have proved $L>0$ in all
cases of the affine slope.

Now put

$$
B_{28}=28E_4-9nE_3=14L+5nE_3>0.
$$

The exact coefficient identity

$$
-36E_2E_3A_\sharp
=63E_3N_2+105E_1N_3+60E_1E_2B_{28}
$$

has a negative left side and a strictly positive right side, by (2)
and (4). This is the final contradiction. Thus $h>0$.

This proves the stated height lemma with its precise premises. It does
not prove that the remaining two event orders are impossible or supply
a larger universal height threshold.
