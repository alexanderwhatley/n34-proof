# A uniform raw five-root theorem for every strict double-reversed source

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## 1. Statement and distinction from original no-ten scope

Let

```math
u,p,a,b,q,z>0,\qquad q<a,\qquad p<b,
\qquad \alpha=u+q,\qquad\beta=p+z.
```

Use the actual support cubics

```math
\begin{aligned}
A(t)&=(u+pt)(a-bt)[a+u-(b-p)t]-(ap+bu)t(1+t),\\
B(t)&=(q+zt)(a-bt)[(b+z)t-(a-q)]+(az+bq)t(1+t).
\end{aligned}
```

For every $`\rho>0`$,

```math
\boxed{H_\rho(t)=A(t)+\rho t^\alpha(1+t)^{\beta-\alpha}B(t)
\text{ has at most five distinct positive roots}.}
\tag{1}
```

There is no integrality, equality, coefficient-word, unused-root-order,
positive-event-collision or critical-value restriction. In particular,
both singly integral gap walls and beta=2 are included literally.
All six support magnitudes are strictly positive, with the displayed
strict double-reversed inequalities. Weak source signs or the degree-drop
faces p=b and q=a are not claimed. The conclusion counts distinct roots,
not root multiplicity.

This is a theorem about the raw actual-source equation, stronger than the
generic no-ten interface. It does not follow merely by passing a generic
root ceiling to a limit. Sections5--6 give the needed common-level argument
for multiple critical-level roots explicitly.

## 2. Reflection and the two unconditional gap modules

The actual source reflection is

```math
(u,p,a,b,q,z)\mapsto(z,q,b,a,p,u),\qquad
(\alpha,\beta,\rho)\mapsto(\beta,\alpha,1/\rho).
\tag{2}
```

Its cubics obey
$`A_{\rm new}(s)=-s^3B(1/s)`$ and
$`B_{\rm new}(s)=-s^3A(1/s)`$. Its equation differs from
H(1/s) only by a nonzero factor, so distinct positive root counts are
preserved. We may consequently assume beta>=alpha.

If alpha>=1, the [uniform min gap one dr five root theorem](double-reversed-large-gap.md) proves (1), including
integer and equal gaps.

If alpha<1 and beta<2, the [uniform low beta dr hurwitz five root theorem](double-reversed-small-exponent.md) proves (1), including
beta=1, coefficient zeros and positive-event coincidences.

It remains to prove the theorem for

```math
0<\alpha<1,\qquad\beta\ge2.
\tag{3}
```

## 3. The fractional shuffle includes every integral beta

Write n=floor(beta)>=2 and zeta=beta-n in [0,1). Put

```math
G=t^\alpha(1+t)^{\zeta-\alpha},\qquad
C=(1+t)^nB=\sum_{j=0}^{n+3}c_jt^j.
```

The strict fractional Stieltjes--Hurwitz flag is

```math
1,G,t,tG,t^2,t^2G,t^3,t^3G,t^4G,\ldots.
\tag{4}
```

For zeta>0 this is the retained complete-Bernstein flag in the [fractional-power basis proof](fractional-root-factor-argument.md).
For zeta=0, irrespective of n, the fractional factor is the same function
$`t^\alpha/(1+t)^\alpha`$ used at beta=1 in the low-beta theorem. It has
the exact infinite-support positive representation

```math
G(t)=\frac{\sin(\pi\alpha)}\pi
\int_0^1\frac{t}{t+s}s^{\alpha-1}(1-s)^{-\alpha}\,ds.
\tag{5}
```

The finite Gaussian-quadrature strictness proof therefore applies directly
to every finite selected flag, with as many nodes as its shifts/jets
require. The degree n of the polynomial multiplier does not change (5).
This explicitly extends the same shuffle to beta=n; it is not an argument
from nonnegative limits of strict minors.

Actual endpoint/mode signs give two positive roots of each cubic and two
zero-safe coefficient variations in A and B. Pascal convolution preserves
the two positive B roots and cannot increase coefficient variation. Thus
C has word -+- after zero deletion. In flag order the coefficient row is

```math
(A_0,\rho c_0,A_1,\rho c_1,A_2,\rho c_2,A_3,
\rho c_3,\rho c_4,\ldots,\rho c_{n+3}).
\tag{6}
```

The short insertion argument from the low-beta theorem applies for every
n: the merged row has at most seven variations. The only way it can exceed
five is

```math
c_0<0,\qquad c_1,c_2,c_3\le0,
\quad\text{followed by a positive block and final negative block}.
\tag{7}
```

Coefficient zeros are filled without increasing the individual two-word
variations and cannot decrease merged variation. In particular, the
zero-safe statement (7) is valid on every raw coefficient seam.

If H has six distinct positive roots, generalized Descartes for (4)
requires at least six coefficient variations. The row's positive first
and negative final entries make its variation odd, so (7) must hold.
We now work only on this forced source chart and derive a contradiction.

## 4. A coefficient prefix forces the strict physical chart

### 4.1 Synthetic division proves the collar for every integer n

Factor

```math
B=-\kappa(t-P)(t-S)(t+y),\qquad
0<P<S,\quad y,\kappa>0.
```

Let E=(1+t)^n(t+y)=sum(e_j t^j), so

```math
e_j=\binom n{j-1}+y\binom nj.
```

Divide C by t-S and write C=(t-S)Q. Its first coefficients satisfy

```math
q_0=-c_0/S>0,\qquad
q_j=(q_{j-1}-c_j)/S>0\quad(j=1,2,3)
```

by (7). But Q=kappa(P-t)E, so
$`q_3=\kappa(Pe_3-e_2)>0`$. Hence

```math
P>\frac{e_2}{e_3}
=\frac{n+y n(n-1)/2}
{n(n-1)/2+y n(n-1)(n-2)/6}
>\frac2{n-1}\ge\frac2{\beta-1}.
\tag{8}
```

The strict middle inequality follows from

```math
(n-1)e_2-2e_3=\frac{yn(n-1)(n+1)}6>0.
\tag{9}
```

This proof has no nonintegral-gap premise. It includes n=2, where
e2/e3=2+y. The same argument with P and S exchanged also bounds S,
but only the P collar in (8) is needed.

### 4.2 Actual support gives interlacing

Put c=a/b, U(t)=u+pt, V(t)=q+zt. The exact identity and score bound are

```math
\frac{A(t)}{U(t)}+\frac{B(t)}{V(t)}=(a-bt)N(t),
\qquad
N(t)=\alpha+\beta t-
\frac{(pq-uz)t(1+t)}{U(t)V(t)}
>\alpha-1+(\beta-1)t.
\tag{10}
```

The signs at 0,c,infinity give A roots Q<c<R and B roots P<c<S,
with one negative root each. Equation(8) makes N positive at P and R.
Thus A(P)>0 implies P<Q, and B(R)<0 implies S<R. Therefore

```math
A/A_3=(t+x)(t-Q)(t-R),\qquad
B/B_3=(t+y)(t-P)(t-S),
\quad0<P<Q<c<S<R.
\tag{11}
```

In particular there are no common positive A/B roots on the only chart
where six H roots could occur. Every positive root of H corresponds to a
contact of the analytic positive profile

```math
F(t)=-A(t)/[t^\alpha(1+t)^{\beta-\alpha}B(t)]=\rho
```

on one of (0,P), (Q,S), (R,infinity).

If p<=u, alpha<1 and beta>=2 imply p<1 and z>1>q.
The actual -1 evaluations give x>=1>y. The ordered-unused-root theorem then proves raw H<=5 directly. Consequently
we may assume p>u, which gives x<1. This uses only the displayed actual
evaluations and the new uniform theorem; the old degree-half-space
source chain is not a dependency.

## 5. Regular levels: one component compatibility theorem

For the remaining actual chart, beta>=2, p>u, alpha<1, strict3131,
P>2/(beta-1), use
[uniform ps component compatibility theorem](double-reversed-component-compatibility.md).
Its conclusion is that **every positive regular level of F has at most
five contacts**. Its primary geometric modules are exactly:

1. the scaled last-pair separator;
2. the first-pair extra-left separator;
3. the universal all-B mode inequality and strict-TP central-four prefix.

For clarity, the compatibility mechanism is short. The full logarithmic
critical numerator has degree seven, a negative root, and at most six
positive critical multiplicities. The source identity g(c)=0, with g
positive at both central ends, gives at least two central critical
multiplicities. Mandatory outer extrema give the component level bounds

```math
L\le4,\qquad M\le3,\qquad T\le2.
\tag{12}
```

For M, five central regular contacts would force four distinct central
critical points. The degree is then exhausted by those four, one left,
one terminal and one negative root, so c is among the four and all are
simple. The strict-TP prefix forces K(c)<0, while the universal actual
mode theorem gives K(c)>0.

If M=3, the central minimum is below the level, while every central
critical height exceeds the terminal maximum; hence T=0. The extra-left
separator forbids L=4 because its later left minimum would be below the
central maximum. Thus L<=2 and the total is at most five.

If M=1, the only possible total above five under (12) and outer parity
would be L=4,T=2. Choosing the mandatory central critical point c gives

```math
F(k_3)<\rho<F(T)<F(c)<F(k_3),
```

where the last inequality is the extra-left separator. This is impossible.
No allocation enumeration is needed.

The beta=2 extensions are literal in the component module. Its last-pair
domination uses t>Q>P>2 and delta=2-alpha>1. Its central-four density
weights alpha,1-alpha,beta,beta-1 remain strictly positive. Thus no
generic gap perturbation is being used at beta=2.

## 6. Multiple contacts: the aggregate common-level lemma

We use the following elementary analytic fact.

> Let F be real analytic and nonconstant on every component of a finite
> union of open intervals, and have only finitely many critical values
> there. If a positive level rho has k
> distinct contacts in those intervals, then arbitrarily close positive
> regular levels have at least k distinct simple contacts for one choice
> of the common shift direction.

**Proof.** Choose disjoint compact neighborhoods of the k contacts,
lying strictly inside their intervals. At a contact r write

```math
F(t)-\rho=\gamma_r(t-r)^{m_r}+O((t-r)^{m_r+1}),
\qquad\gamma_r\ne0.
```

At every odd-multiplicity contact, both sufficiently small common shift
directions preserve at least one root in its neighborhood. At an even
contact with gamma_r>0, a small upward shift gives two roots; at one with
gamma_r<0, a small downward shift gives two roots. Let o be the number
of odd contacts and e+,e- the respective even-contact counts. The two
directions therefore give at least

```math
o+2e_+,\qquad o+2e_-.
```

The larger count is at least o+e++e-=k. Take the shift arbitrarily small
in that direction, below rho/2 in absolute value, and avoid the finite
critical values. All contacts at the resulting level are then simple.
This proves the lemma. It does **not** claim that every old root bracket
is retained in the same direction.

On the strict chart (11), F is analytic and nonconstant on its three useful
components, as their endpoint limits also show.
Its logarithmic derivative has a nonzero degree-seven polynomial
numerator, so it has finitely many critical points and critical values.
Every selected H root has the same multiplicity as F-rho, since B is
nonzero there. If H had six distinct roots, the lemma would produce a
nearby positive regular level with at least six contacts of this same
actual F, contradicting Section5's ceiling five. This proves (1).

The level is shifted within the raw scalar family H_rho while the six
support magnitudes remain fixed. No independent alteration of critical
heights or cubics is used. A Hurwitz seven-root bound or EHT eight-root bound
is not needed after the common-level lemma: the regular-level ceiling
five yields the contradiction directly.

## 7. Proof dependencies and practical consequence

Primary inputs are the actual cubic/reflection dictionary; the minimum-gap-one and low-beta Hurwitz theorems; the retained strict
fractional Hurwitz/Gaussian proof; the direct synthetic-division collar
(8); the ordered-unused-root easy region; and the new regular-level
component compatibility theorem with its three geometric modules.

The generic actual seven-allocation atlas, original physical sextic table,
old fourth-annihilator band table, middle paired-cofactor estimate,
remote finite cutoffs, A2 branch and B1 sign split are not primary inputs.
Earlier notes remain preserved as optional or historical checks.

At original pure-split scope the theorem directly contradicts the required
seven contacts in the double-reversed quadrant. All double-reversed gap,
event and critical seams are now covered at the raw distinct-root level;
the original regularization remains relevant to the entry and other score
quadrants, rather than being used to patch raw DR seams. The other nested
and mixed PS quadrants, AP, the one-corner master theorem and the (2,2)
sign chamber are outside this new raw theorem.
