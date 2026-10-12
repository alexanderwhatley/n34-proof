# At most two contacts before the four roots in order $`1320`$

Use the actual F3 family and determinant convention of [the real exterior-pair lemma](f3-real-exterior-pairs.md). Suppose each cofactor has one simple physical root, their physical roots are distinct in order $`1320`$, and both other root pairs of $`E_1`$ and $`E_3`$ are genuinely nonreal. Then the contacts before all four physical roots have total multiplicity at most two.

The proof has three parts. An explicit positive phase identifies its stationary points with the actual determinant roots and removes the part before the beta mode. A local change of variables proves a curvature inequality for a single analytic function. Finally, that inequality bounds its zeros, including repeated zeros. No bound on $`b+d`$, $`(a-1)d-e(2-b)`$, or $`a-e`$ is required.

The coordinate $`t=x/(1-x)`$ is positive on the original interval. All locally introduced variables below are algebraic functions of the original parameters at a fixed point. They are held constant during local differentiation; the proof never differentiates a normalization that varies with the chosen point.

## Source and contact representation

Use strict canonical supports

```math
1,\quad x^a(1-x)^{-b},\quad x^e(1-x)^d,\quad x^c(1-x)^{-f},
```

with

```math
0\lt e\lt a\lt c,\quad 0\lt f\lt b,\quad d\gt0,\quad
0\lt e+d\lt a-b\lt c-f.
```

Write `t=x/(1−x)` for original odds. Assume all four signed cofactors have one
simple physical root, their roots are distinct with word `1320`, and both
variable pairs are nonreal. Denote the roots by

```math
0\lt t_1\lt p=t_3\lt t_2\lt t_0.
```

The jointly useful left interval is $`J=(0,t_1)`$. Here
$`E_0\lt0`$, $`E_2\gt0`$, and $`E_3\gt0`$. Deflate the actual E3 cofactor as

```math
E_3(t)=\gamma(p-t)Q(t),\qquad \gamma\gt0,
```

where the actual quadratic $`Q`$ is strictly positive on the whole real line.
The constant normalization of Q does not matter.

Use the positive inverse E3 phase

```math
\Psi(t)=\frac{m_3(t)E_2(t)}{m_2(t)E_3(t)}\gt0.
```

If the two fixed exterior E2 roots are $`-u,-v\lt-1`$, its logarithmic derivative
is

```math
(\log\Psi)'=P_{\rm ker}-Q'/Q=N/Q,
```

where

```math
P_{\rm ker}=\frac{d+f}{t}
 +\frac{c-f-e-d}{t(1+t)}
 +\frac1{t+u}+\frac1{t+v}
 +\frac{t_2-p}{(p-t)(t_2-t)}\gt0.
```

The actual determinant-linked source identity is

```math
(L_3-L_2)E_2E_3
+t(1+t)(E_3E_2'-E_2E_3')=-L_1K,
\qquad L_1=a+bt\gt0.
```

Consequently

```math
\boxed{N(t)=-\frac{Q(t)(a+bt)}{t(1+t)E_2(t)E_3(t)}K(t).}
```

The factor multiplying K is finite, analytic, and strictly negative throughout
J. Thus N and K have exactly the same zeros **with the same multiplicities**.
This binding uses the actual source cofactors rather than arbitrary cubics.

## There are no premode contacts

The [fixed exterior-interlacing lemma](f3-fixed-exterior-interlacing.md) gives

```math
R(t)=-E_0(t)/E_2(t)\gt0,\qquad R'(t)\gt0
```

on J. Its three partial-fraction residues are negative, so the derivative
is a sum of positive squared-reciprocal terms.

The beta atom $`m_2(t)=t^e/(1+t)^{e+d}`$ is nondecreasing for
$`0\lt t\le m=e/d`$. Hence $`(m_2R)'\gt0`$ on that part of J, including m.
The actual source identity

```math
L_2E_0E_2+t(1+t)(E_0'E_2-E_0E_2')=(L_3-L_1)K
```

shows that these derivatives vanish exactly at K contacts: the score difference
$`L_3-L_1`$ is strictly positive on J and all denominator factors are nonzero.
For completeness, the needed score difference has a direct source proof.
At $`\tau=(c-a)/(b-f)\gt0`$, the scores L1 and L3 coincide, and

```math
E_2(\tau)=-L_1(\tau)\tau[(c-f)-(a-b)]\lt0.
```

Since E2 starts positive and has exactly one simple physical root t2,
we have $`\tau\gt t_2\gt t_1`$. Therefore
$`L_3-L_1=(c-a)-(b-f)t\gt0`$ on J, including the mode when it lies there.
This excludes any exception in the premode phase factor.

Therefore there are **no contacts on or before the mode**. The earliest E1
root is postmode, so the only possible contacts lie on the connected interval
$`J_+=(m,t_1)`$.

## Actual source coverage

At a chosen postmode point let $`x=t_{*}/(1+t_{*})`$, set local coordinate
$`s=t/t_{*}-1`$, and take h=1 in the homogeneous kernel model. The original
source map is

```math
\begin{aligned}
a&=L(1-z)/(1-x),& b&=Lz/x,\\
e&=(W-P)/(1-x),& d&=W/x,\\
c&=(L+G)(1-v)/(1-x),& f&=(L+G)v/x.
\end{aligned}
```

It is a map of the actual fixed original source, not a choice of arbitrary
cubic coefficients. The complete polynomial identities are

```math
\begin{aligned}
(1-x)^3E_3(t_{*}(1+s))&=L A(s),\\
-(1-x)^3E_1(t_{*}(1+s))&=(L+G)B(s),\\
(1-x)^3E_2(t_{*}(1+s))&=L(L+G)D(s),
\end{aligned}
```

where A, B, D are the factored source cubics used by the local proof. In
particular A is normalized by L, not by P. All displayed scales are positive
constants during the local differentiation.

Put $`U=L+P`$, $`r=z-v`$, $`\delta=G-r`$,
$`q=Lr-Gv`$, $`H=A(0)-P\delta`$, and $`O=Ux-Lz-W`$.
Here is the complete coverage argument for every gate used by the proof:

- Postmode gives $`P=dx-e(1-x)\gt0`$, and $`W=dx\gt P`$ because e>0.
- On J, E1<0, E2>0, E3>0. These normalizations give H>0, delta>0,
  and a0=A(0)>0.
- The score difference G is positive on J. At
  $`\tau=(c-a)/(b-f)`$, scores 1 and 3 agree and
  $`E_2(\tau)=-L_1(\tau)\tau[(c-f)-(a-b)]\lt0`$. Since E2 has just one
  physical root and starts positive, $`\tau\gt t_2\gt t_1`$. Therefore the score
  difference is positive throughout J.
- Canonical b>f gives $`q=x(b-f)\gt0`$. With G>0 this gives r>0; since
  $`G=r+\delta\gt r`$, it also gives $`L\gt v`$.
- Canonical sum order gives
  $`O=x(1-x)(a-b-e-d)\gt0`$. The exact identity
  $`O=U(x-P-z)-a_0`$ then gives $`x\gt P+z`$.
- Thus $`1\gt x\gt P+z\gt z\gt v\gt0`$, $`W\gt Ph`$, and $`L\gt v`$, as required by the
  homogeneous local model with h=1.
- The beta derivative margins are
  $`D_T=x(1-x)(c-f-e-d)\gt0`$ and $`D_b=x(d+f)\gt0`$. Their source jets are
  exactly beta(0)=S, beta'(0)=−S−DT,
  beta''(0)/2=S+(1+x)DT, where S=U+G.

## Necessary signs at bad curvature

The inverse E3 phase has logarithmic derivative N/Q, with the actual positive
deflated E3 quadratic Q and actual pole kernel

```math
P_{\rm ker}(t)=\frac{d+f}{t}
 +\frac{c-f-e-d}{t(1+t)}
 +\frac1{t+u}+\frac1{t+v_e}
 +\frac{t_2-t_3}{(t_3-t)(t_2-t)}\gt0.
```

Here −u and −ve are the two fixed exterior E2 roots, below −1 by the fixed exterior-interlacing lemma. The quadratic Q is positive on
the whole real line because the E3 remaining pair is nonreal.

The pole-kernel inequality gives
$`P_{\rm ker}P_{\rm ker}''\gt\tfrac32(P_{\rm ker}')^2`$. Here is its proof. Each positive summand $`f`$ is a positive constant times a simple reciprocal or the product of two reciprocals of positive affine distances. For a simple reciprocal, $`ff''=2(f')^2`$. For a two-factor reciprocal, if its logarithmic derivative is $`q_1+q_2`$, then $`f''/f=(q_1+q_2)^2+q_1^2+q_2^2\gt\tfrac32(q_1+q_2)^2`$, because the two pole distances differ. Sum these inequalities and apply weighted Cauchy,

```math
\left(\sum f'\right)^2\le\left(\sum f\right)\left(\sum\frac{(f')^2}{f}\right).
```

The strict inequality persists for the actual kernel. It uses no residual parameter
bound. At N'=0, if Q'<0, put
$`R_q=2\gamma Q/(Q')^2\gt1/2`$ and
$`y_q=Q'P_{\rm ker}/(2\gamma)\lt0`$. The resulting lower bound is

```math
\frac{N''}{2\gamma P_{\rm ker}}
 \gt\frac{(2R_q-1)y_q^2-2y_q+3}{2R_qy_q^2}\gt0.
```

For Q'=0 the positive kernel second derivative gives N''>0 directly.
Therefore a hypothetical N'=0, N''<=0 point has Q'>0 and
$`P_{\rm ker}'\lt0`$.

For each exterior simple reciprocal, its contribution to N''/2 is a positive
multiple of Q evaluated at that exterior pole. The future pole-difference
term has Q,Q',Q'',g,g',g'' positive, hence a strictly positive contribution.
Thus N''<=0 forces the source beta contribution Bcurv<0. Its exact identity is

```math
B_{\rm curv}=S Q_H-D_T\xi BS,
\qquad Q_H=h^2Q(-1/h)\gt0,
\quad BS=a_1+a_0\xi-a_0(h+x).
```

Since S,DT,xi>0, this gives BS>0 strictly. These are precisely the preliminary signs used in the local algebraic argument below.

## Local algebraic inequality

Assume strict canonical supports, all four cofactors with one simple physical
root each, distinct physical roots of word 1320, and both additional E1/E3
root pairs nonreal. At a postmode jointly-left point, let

```math
z=v+r,\quad G=r+\delta,\quad U=L+P,\quad S=U+G,\quad X=h+x,\quad Y=hx.
```

The source parameters L,P,r,δ,v,W,h,x are positive. The source gates used below are

```math
h\gt x\gt P+z,\quad L\gt v,\quad W\gt Ph,\quad
H_s=a_0-P\delta\gt0,\quad q=Lr-Gv\gt0,
\quad O=Ux-Lz-W\gt0.
```

The global source still has both nonreal variable pairs. The coverage argument above gives $`h=1`$; the algebraic proof below permits the homogeneous parameter $`h\gt x`$. This larger domain does not remove a hypothesis from the global theorem.

Reconstruct the E3 source cubic as

```math
A(t)=(W-Pz)(1+ht)(1+xt)
 -(1+zt)(P+Wt)[U+(Lz+W)t]
 =a_0+a_1t+a_2t^2-\gamma t^3,
```

where

```math
\begin{aligned}
a_0&=W-P(U+z),\\
a_1&=W(X-L-2P)-Pz(2L+P+X),\\
a_2&=W(Y-2zU-W)-Pz(Lz+Y),\\
\gamma&=zW(Lz+W)\gt0.
\end{aligned}
```

The E2 source cubic is

```math
D(t)=(1+zt)(1+vt)(G-qt)-r(1+ht)(1+xt)
 =\delta+d_1t+d_2t^2+d_3t^3,
```

with

```math
d_1=G(z+2v)-r(L+X),\qquad
d_2=Gv(2z+v)-r[L(z+v)+Y].
```

Put

```math
D_b=W+(L+G)v,\quad
J_0=\delta S+d_1,\quad
J_1=-\delta^2(SX-D_b)+2d_2\delta-d_1^2.
```

Let $`\ell\gt0`$ be the physical E3 root and $`\xi=1/\ell`$. Then

```math
I_{\rm root}=a_0\xi^3+a_1\xi^2+a_2\xi-\gamma=0.
```

For the positive deflated E3 quadratic $`Q`$ and the source kernel $`P_{\rm ker}`$,
write $`N=Q P_{\rm ker}-Q'`$. At the chosen physical point, its sign is the sign
of $`N_{\rm num}=a_0J_0-\delta a_1`$; the sign of $`N'`$ is the sign of

```math
I_{\rm crit}=\xi(a_1+a_0\xi)\delta(J_0+\delta\xi)
 +\xi a_0(J_1+\delta^2\xi^2)-2\gamma\delta^2.
```

**Claim.** Every stationary point of $`N`$ with $`N\ge0`$ has $`N''\gt0`$.

The pole-kernel reduction just given shows that a hypothetical stationary
point with $`N''\le0`$ must satisfy

```math
B_0\lt0,\qquad BS=a_1+a_0\xi-a_0X\gt0,
```

where

```math
B_0=\gamma S-(a_1+a_0\xi)\xi(SX-D_b)
       +a_0\xi[S(X^2-Y)-XD_b].
```

We prove that these two necessary signs, together with $`N_{\rm num}\ge0`$,
actually imply $`I_{\rm crit}\gt0`$, contradicting stationarity.

## Two root-free gates

Set

```math
\alpha=a_0/P,\quad w=W/P,\quad
\kappa=w-X+P+2v,\quad
K_0=a_2+a_0(X^2-Y)-a_1X.
```

Thus $`0\lt\delta\lt\alpha`$. The exact identity

```math
B_0+S I_{\rm root}
 =\xi\{S K_0+BS(S\xi+D_b)\}
```

shows that the bad signs force $`K_0\lt0`$. Crucially, $`K_0`$ depends only on the
E3 source core $`(L,P,r,v,W,h,x)`$, and **does not depend on $`\delta`$**.

Let $`C=r(L+X-z-2v)\gt0`$. Another identity is

```math
N_{\rm num}/P=(\delta-\alpha)(\alpha\delta+C)
                  +\delta(w-v)\kappa.
```

The first summand is strictly negative and $`w\gt h\gt v`$. Hence
$`N_{\rm num}\ge0`$ forces $`\kappa\gt0`$, including the case $`N_{\rm num}=0`$.

The root-free sign $`K_0\lt0`$ also forces

```math
J=\kappa+r-v\lt0.
```

Here is a short proof retaining the source order. We have

```math
X=U+P+2z+\alpha-J,\quad
O=U(x-P-z)-P\alpha,
```

and

```math
D_{\rm lin}=U(h-x)+2O
 =\alpha(U-2P)+U(U-P-J)\gt0.
```

With $`Y_{\rm lo}=(P+z)(X-P-z)`$,

```math
Y-Y_{\rm lo}=(x-P-z)(h-P-z)\gt0,
```

and

```math
K_0/P=K_{\rm lo}+U(Y-Y_{\rm lo}),\qquad
K_{\rm lo}=\alpha[P^2+(U-P)J]+UJ(U-J).
```

Thus $`K_{\rm lo}\lt0`$. If $`0\le J\le U`$, its displayed expression is positive.
If $`J\gt U`$, the positive $`D_{\rm lin}`$ forces $`U\gt2P`$, but

```math
(U-2P)K_{\rm lo}
 =[P^2+(U-P)J]D_{\rm lin}+UP(J^2-PU+P^2)\gt0.
```

This is again impossible. Put $`j=-J=v-r-\kappa\gt0`$. In particular,
$`0\lt\kappa\lt v\lt U`$.

## Reduce stationarity to a source cubic

Define

```math
R=a_1\delta J_0+a_0J_1-2a_2\delta^2,\qquad
EP=a_0(J_0^2+J_1)-2a_2\delta^2.
```

The exact identities

```math
\begin{aligned}
I_{\rm crit}&=\xi R+\xi^2\delta N_{\rm num}
                           +2\delta^2I_{\rm root},\\
R&=EP-J_0N_{\rm num}
\end{aligned}
```

show that it suffices to prove $`R\gt0`$.

Freeze the E3 core and allow $`\delta`$ to vary algebraically. In the source
chart

```math
w=\alpha+U+r+v,\qquad
X=U+P+r+3v+\alpha-\kappa,
```

we have

```math
\frac{N_{\rm num}}P
 =\kappa C_n-(\alpha-\delta)E_n,
\quad C_n=\alpha r+\delta(\alpha+U),
\quad E_n=\alpha\delta+r(2U+\alpha).
```

This is a quadratic in $`\delta`$ with positive leading coefficient $`\alpha`$
and negative constant $`-\alpha r(2U+\alpha-\kappa)`$. Therefore it has exactly
one positive root $`\delta_N`$. Its value at $`\alpha`$ is positive, so

```math
0\lt\delta_N\lt\alpha,\qquad N_{\rm num}\ge0\Longrightarrow\delta\ge\delta_N.
```

Meanwhile $`R/P`$ is a cubic in $`\delta`$. Its constant is
$`-\alpha r^2(2U+\alpha-\kappa)^2\lt0`$. Its leading coefficient is

```math
a_3=\alpha(v-P)-U(\kappa+2r).
```

To see that $`a_3\lt0`$ at the actual source core, set

```math
Q_h=U\kappa-(\alpha-\delta)(v-P),\qquad
T_n=UE_n-(v-P)C_n.
```

Then

```math
C_nQ_h=U(N_{\rm num}/P)+(\alpha-\delta)T_n,
```

and

```math
T_n=\alpha(r+\delta)(U-v+P)
       +U[2rU-\delta(v-P)]\gt0,
```

because

```math
2rU-\delta(v-P)=q+r(U+P+v)+\delta P\gt0.
```

Consequently $`Q_h\gt0`$, and the identity

```math
-a_3=r(U+P+v)+Q_h+q+\delta P
```

gives $`a_3\lt0`$. This sign concerns a coefficient of the cubic; it
therefore remains valid throughout the ensuing algebraic endpoint argument.

## Positivity at the two endpoints

Set

```math
C_{*}=a_0r+\delta(a_0+PU)=PC_n,
\quad
Z=\frac{PUR+2\delta C_{*}K_0}{P^2},
\quad
F_0=\frac{PU\,EP+2\delta C_{*}K_0}{\delta P^2}.
```

At $`N_{\rm num}=0`$, $`R=EP`$, so $`Z=\delta F_0`$. Because $`K_0\lt0`$ remains
fixed and $`C_{*}\gt0`$, positivity of $`Z`$ implies positivity of $`R`$.

At the lower endpoint, write $`d=\delta_N`$, $`H=\alpha-d\gt0`$. The equality
$`N_{\rm num}=0`$ gives $`\kappa=HE_n/C_n`$; since $`j\gt0`$,
$`v=\kappa+r+j`$. Direct source expansion gives

```math
F_0=\frac{\alpha}{C_n}\,[Q_0+HQ_1+H^2Q_2+H^3Q_3],
```

where every factor and coefficient below is positive:

```math
\begin{aligned}
Q_0={}&2d(U+d+r)^2[dP(P+j)+Ur(P+2j+r)],\\
Q_1={}&(U+d+r)[4Pd(d+r)(P+j)+PU(3d^2+2dr+2r^2)\\
&\quad+U^2(d^2+6dr+4r^2)+2U(d+r)^3
             +2Uj(d+r)(d+2r)],\\
Q_2={}&(d+r)[2P(P+j)(d+r)+3PUd+2U^2(2d+3r)\\
&\quad+2U(d+r)(2d+2r+j)],\\
Q_3={}&2U(d+r)^2.
\end{aligned}
```

Thus $`F_0\gt0`$, $`Z(\delta_N)\gt0`$, and $`R(\delta_N)\gt0`$.

At the upper endpoint, retaining the same core and writing
$`v=\kappa+r+j`$, direct expansion gives

```math
Z(\alpha)=\alpha(U+\alpha+r)\,T,
```

where

```math
\begin{aligned}
T={}&U\kappa r(2U-\kappa)
 +2P\alpha[\alpha(P+j)+U(\kappa+r)]\\
 &+U\alpha[\kappa(U+2\alpha+\kappa+6r)
                      +j(3\kappa+4r)+2r^2]\gt0.
\end{aligned}
```

Here $`\kappa\lt v\lt U`$, so the first term is positive as well. Hence
$`R(\alpha)\gt0`$.

These endpoint expansions require only positive core parameters, $`j\gt0`$,
and the relevant endpoint relation. They do **not** assume that the moving
$`\delta`$ remains a physical source point or retains $`q\gt0`$, the order word,
or the E1 nonreal pair. The actual source gates were used to identify the core
and its negative cubic leading coefficient. The only transported bad sign is
$`K_0\lt0`$, which is explicitly independent of $`\delta`$.

## Finish the local lemma

A cubic with negative constant and negative leading coefficient has at most
two positive zeros counted with multiplicity: the number of coefficient sign
changes is either zero or two. Since this cubic is positive at both
$`\delta_N`$ and $`\alpha`$, it is positive on the whole interval between them.
Indeed, a nonpositive point inside would require a zero before $`\delta_N`$,
a zero after $`\alpha`$, and two additional zeros counted with multiplicity
inside. Thus

```math
R\gt0\quad\text{for }\delta_N\le\delta\le\alpha.
```

The actual source point has $`\delta_N\le\delta\lt\alpha`$, and therefore

```math
I_{\rm crit}=\xi R+\xi^2\delta N_{\rm num}\gt0.
```

This contradicts $`N'=0`$. Accordingly, a stationary point with $`N\ge0`$
cannot have $`N''\le0`$, proving the claim.

## The point-chart theorem applies to one global phase

At a fixed physical point $`t_{*}\in J_+`$, the local coordinate is
$`t=t_{*}(1+s)`$. Hold all source parameters constant while differentiating s.
If the local deflated quadratic is $`Q_{\rm loc}=c_QQ(t_{*}(1+s))`$,
then $`c_Q\gt0`$ and

```math
N_{\rm loc}(s)=c_Qt_{*}N(t_{*}(1+s)).
```

Its derivative of order j has the positive scale factor
$`c_Qt_{*}^{j+1}`$, for j=0,1,2. Thus the signs of N and N'', and the equation
N'=0, are exactly preserved. There is no derivative of a point-dependent
normalization: the chosen point and its normalization stay fixed during the
local differentiation.

The source chart also gives

```math
N_{\rm loc}(0)=\frac{\xi}{\delta}N_{\rm num},\qquad
\delta^2N_{\rm loc}'(0)=I_{\rm crit},
```

with $`\delta,\xi\gt0`$. Therefore the local inequality just proved is precisely

**(*)**

```math
N'(t)=0,\quad N(t)\ge0\quad\Longrightarrow\quad N''(t)\gt0
```

for the single global phase throughout $`J_+`$.

## A calculus lemma including multiplicities

Let a real analytic function n on an interval satisfy (*) and have isolated
zeros. Then it has at most two zeros counted with multiplicity.

A zero of multiplicity at least three has n=n'=n''=0 and violates (*).
A double zero must have n''>0, so it is a strict local minimum at zero and n is
positive immediately on both sides. If a double zero and a second distinct
zero existed, n would be positive somewhere between the two zeros. Its
positive maximum on that closed interval would occur in the interior and
satisfy n'=0,n>0,n''<=0, violating (*).

Finally, if three distinct zeros existed, use the interval between the outer
two. If n is positive somewhere inside, an interior positive maximum gives
the same contradiction. Otherwise n<=0 throughout that interval, and the
middle zero is a local maximum at zero; it satisfies n'=0,n=0,n''<=0 and again
violates (*). Negative-valued critical maxima do not create a missing case:
either a positive arch or this zero-valued middle maximum is forced by three
zeros.

Applying the lemma to N on J+ bounds its total zero multiplicity by two. The
premode exclusion and nonvanishing source factor give

```math
\boxed{\#\{\text{joint-left K contacts}\}\le2
\quad\text{counting multiplicity}.}
```

This is the left bound used with the separate right argument in the full F3 proof.
