# Uniform compatibility of the three positive PS components

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Statement

Use the actual cubics

```math
\begin{aligned}
A(t)&=(u+pt)(a-bt)[a+u-(b-p)t]-(ap+bu)t(1+t),\\
B(t)&=(q+zt)(a-bt)[(b+z)t-(a-q)]+(az+bq)t(1+t),
\end{aligned}
```

where all six support magnitudes are positive, $`q<a`$, $`p<b`$, and
$`p>u`$. Set $`\alpha=u+q\in(0,1)`$, $`\beta=p+z\ge2`$, and
$`c=a/b`$. Suppose the normalized roots satisfy

```math
A/A_3=(t+x)(t-Q)(t-R),\quad
B/B_3=(t+y)(t-P)(t-S),\quad
0<P<Q<c<S<R,\quad x,y>0,
```

and suppose $`P>2/(\beta-1)`$. For the positive profile

```math
F(t)=C\frac{(t+x)(t-Q)(t-R)}
 {t^\alpha(1+t)^{\beta-\alpha}(t+y)(t-P)(t-S)},\qquad C>0,
\tag{1}
```

every positive regular level has at most **five** distinct intersections
on the three positive components $`(0,P)`$, $`(Q,S)`$, and $`(R,\infty)`$.

Here a regular level has nonzero derivative at every intersection.
Critical points themselves need not be simple. This is a component
compatibility theorem, without a seven-contact allocation table or a
prior global root bound. Promotion to arbitrary levels is a separate step.

## 1. The critical-point budget and the actual central point

The logarithmic derivative is

```math
G=\frac1{t+x}-\frac1{t+y}+\frac1{t-Q}+\frac1{t-R}
 -\frac1{t-P}-\frac1{t-S}-\frac\alpha t
 -\frac{\beta-\alpha}{1+t}.
\tag{2}
```

Its denominator
$`D=t(1+t)(t+x)(t+y)(t-P)(t-Q)(t-S)(t-R)`$
has degree eight. Its cleared numerator $`N=DG`$ has degree seven,
leading coefficient $`-\beta`$, and constant coefficient
$`-\alpha xyPQRS<0`$. Consequently $`N`$ has at least one negative
real root and at most six positive roots counted with multiplicity.
Every critical point in one of the three open components contributes
its full multiplicity to this budget.

The actual source identities, with $`U=u+pc`$, $`V=q+zc`$, and
$`w=c(1+c)`$, are

```math
\begin{array}{ll}
A(c)=-bUw,&A'(c)=-bU(U+1+2c),\\
B(c)=bVw,&B'(c)=bV(1+2c-V).
\end{array}
```

Since $`U+V=\alpha+\beta c`$, these imply $`G(c)=0`$.
On the central component $`G`$ tends to positive infinity at both
ends. The sum of its central root multiplicities is therefore even:
the number of odd-multiplicity roots is even. Since $`c`$ is a central
root, this sum is at least two. On the terminal component $`F`$ is
positive, tends to zero at both ends, and attains an interior maximum,
so there is at least one terminal critical point. Thus the left
critical multiplicity is at most three.

## 2. The two literal beta=2 extensions

The linked prefix and height lemmas state $`\beta>2`$. The following arguments include the boundary $`\beta=2`$ directly.

**Central prefix.** The
[central critical-point prefix](central-critical-prefix.md) transforms $`(Q,S)`$
by $`r=(t-Q)/(S-t)`$. Its cumulative squared-Cauchy density has three
sign blocks if $`y\le x`$, and otherwise five complete ordered blocks
$`+,-,+,-,+`$. The first two complete blocks transform precisely to
$`(dt/dr)K(t)`$, where

```math
K(t)=\frac{Q-P}{(t-Q)(t-P)}-\frac{\alpha x}{t(t+x)}.
\tag{3}
```

The near negative block has magnitude $`\alpha`$; the intervening
positive block has magnitude $`1-\alpha`$. In the far negative block,
the possible magnitudes are $`\alpha,\beta`$ if $`x<y<1`$,
$`\beta-1,\beta`$ if $`y>1`$, and $`\beta`$ if $`y=1`$.
All remain strictly positive at $`\beta=2`$. The rate supports,
complete-column grouping, convergence, strict Cauchy minors, and the
[matrix prefix theorem](positive-matrix-prefix.md) are unchanged. Hence, literally for
$`\beta\ge2`$, four distinct central zeros imply

```math
K(t)<0\quad\text{at every central zero, including }c.
\tag{4}
```

The source identity
$`A(-1)=-(p-u)(a+b)[a+b-(p-u)]<0`$
gives $`x<1`$, the other required scalar premise. The
[mode-prefix inequality](all-coefficient-mode-prefix.md), already stated for
$`\beta\ge2`$, gives $`K(c)>0`$. Thus **there cannot be four distinct
central critical points**.

**Terminal maximum and height.** The
[last-pair height comparison](last-pair-height-comparison.md) removes the last physical pair:

```math
Z_T=F\frac{t-S}{t-R},\qquad
E_T=t(\log Z_T)'.
```

For $`t>Q`$, with $`\delta=\beta-\alpha`$, its exact derivative is

```math
E_T'=\frac{x}{(t+x)^2}-\frac{y}{(t+y)^2}
 -\frac{(Q-P)(t^2-PQ)}{(t-Q)^2(t-P)^2}
 -\frac{\delta}{(1+t)^2}.
\tag{5}
```

For $`\beta>2`$ the scalar estimate in the linked proof proves this negative.
At $`\beta=2`$, the source collar gives $`t>Q>P>2`$, and $`x<1`$
gives directly

```math
\frac{x}{(t+x)^2}<\frac1{(1+t)^2}
 <\frac{2-\alpha}{(1+t)^2}.
```

The other two summands in (5) are negative, so the conclusion is the
same. Hence $`E_T`$ decreases strictly from positive infinity to
$`-\beta`$, with a unique zero $`h_T`$.

For $`t>R`$, the full scaled derivative is $`tG=E_T+tQ_2`$, where
$`Q_2=(R-S)/[(t-R)(t-S)]`$. Its added term has derivative

```math
(tQ_2)'=\frac{(R-S)(RS-t^2)}{(t-R)^2(t-S)^2}<0.
```

It follows that the terminal profile has a unique simple maximum $`T`$.
At any central critical point $`v`$, and at $`T`$,
$`E_T=-tQ_2<0`$; both points lie beyond $`h_T`$.
The positive reduced profile $`Z_T`$ therefore decreases strictly
from $`v`$ to $`T`$. The removed factor is greater than one at $`v`$
and less than one at $`T`$, giving

```math
\boxed{F(v)>F(T)\quad\text{for every central critical point }v.}
\tag{6}
```

Thus the last-pair conclusion is literal for every $`\beta\ge2`$,
with arbitrary $`y>0`$ and no coefficient-word premise.

## 3. The first-pair height comparison

The [first-pair height comparison](first-pair-height-comparison.md) has the full
root-factor scope $`\alpha,\beta,x,y>0`$, $`P<Q<S<R`$: if
$`k_1<k_2<k_3<P`$ are three left critical points, then

```math
\boxed{F(k_3)>F(v)\quad\text{for every central critical point }v.}
\tag{7}
```

This theorem has no exponent band, coefficient word, unused-root order,
source prefix, or simple-critical premise. Its proof exhausts a
deflated quintic only under the contradictory bad height comparison;
there is no imported sextic allocation census.

## 4. Compatibility of the regular-level counts

Fix a positive regular level $`\rho`$, and let $`L,M,T_0`$ denote its
numbers of intersections on the left, central, and terminal components.
The endpoint values of $`F`$ are respectively
$`(\infty,\infty)`$, $`(0,\infty)`$, and $`(0,0)`$. Thus $`L`$
and $`T_0`$ are even and $`M`$ is odd and positive. Rolle's theorem
and Section 1 give $`L\le4`$. Section 2 gives $`M\le3`$ and
$`T_0\le2`$. In particular

```math
L\in\{0,2,4\},\qquad M\in\{1,3\},\qquad T_0\in\{0,2\}.
```

If $`L=4`$, its three intervening critical points exhaust the available
left budget. They are the minimum, maximum, and later minimum, and
$`F(k_3)<\rho`$. By (7) this later minimum is strictly above every
central critical height.

If $`M=3`$, regular crossing directions and Rolle's theorem supply a
central critical height above $`\rho`$ and another below $`\rho`$.
The upper one and (7) forbid $`L=4`$. The lower one and (6) forbid
$`T_0=2`$, since two terminal intersections require
$`\rho<F(T)`$. Consequently $`M=3`$ forces $`L\le2`$ and
$`T_0=0`$, giving at most five intersections.

If $`M=1`$, simultaneous $`L=4`$ and $`T_0=2`$ would give

```math
F(k_3)<\rho<F(T)<F(c),
```

contradicting (7) at the actual central point $`c`$. Hence
$`L+T_0\le4`$, again giving at most five intersections.

These two alternatives prove the theorem. They use the mandatory
actual source point, the two uniform height separators, and the
universal mode-prefix inequality. Degenerate critical points and the
literal $`\beta=2`$ boundary have been included explicitly. No claim
about perturbing arbitrary levels is made here.
