# A common-level theorem for the mixed three-event region

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## 1. Source and theorem

Let

```math
a_1=-U\lt0\lt a_2\lt a_3,\qquad b_3\lt0\lt b_1=v\lt b_2,\qquad U,v\gt0.
```

Write $`w=x(1-x)`$, $`\mathcal D=w\,d/dx`$, $`d_i=a_i+b_i`$,
$`\lambda_i=a_i-d_ix`$, $`h_i=x^{a_i}(1-x)^{b_i}`$,
$`J=L_{21}=\lambda_2-\lambda_1`$, and $`L=L_{32}=\lambda_3-\lambda_2`$.
The actual cubics are

```math
\begin{aligned}
P_1&=(\mathcal D\lambda_2)J-\lambda_2(\lambda_1J+\mathcal DJ),\\
P=P_3&=\lambda_2(\lambda_3L+\mathcal DL)-(\mathcal D\lambda_2)L,\\
G&=(\lambda_3-\lambda_1)JL+(\mathcal DL)J-(\mathcal DJ)L.
\end{aligned}
```

**Theorem.** Assume either that $`P_3`$ has exactly one odd-multiplicity physical root, or that $`P_3,G`$ share a physical root. For every $`\kappa\gt0`$,

```math
\boxed{Z_{(0,1),\mathrm{mult}}(P_3-\kappa h_1G)\le6.}
```

In the first clause, the odd root may be simple or triple; a simple root may also be accompanied by a distinct double root. Physical $`G`$ roots may have any allowed multiplicity. The common-event clause additionally covers collisions even when $`P_3`$ has three simple physical roots. No degree-cell, critical-allocation, exterior-reality, critical-simplicity, or regular-level assumption is needed.

The generic canonical words in the first clause are $`131`$ and $`113`$; exact reflection covers $`313`$ and $`133`$. Their event boundaries inside strict supports are included directly, with multiplicity. Sources with three odd physical $`P_3`$ roots and no physical $`P_3/G`$ common root remain outside this theorem. The bound concerns the common-level residual, rather than the original four-beta row or the auxiliary ratio $`R`$.

## 2. Actual identities and automatic event facts

The source has the exact polynomial identities

```math
LP_1+JP=\lambda_2G,
```

```math
w(P_1'P-P_1P')-(\lambda_3-\lambda_1)P_1P=\lambda_2K,
```

```math
Q=w(P'G-PG')-\lambda_1PG=-LK,\qquad \deg K\le6,
```

with

```math
K(0)=a_1a_2a_3(a_3-a_2)(a_3-a_1)(a_2-a_1)\lt0.
```

Thus $`K\not\equiv0`$. Also $`L\gt0`$ on the physical interval.
The endpoint signs are $`P_1(0),P_1(1)\gt0`$, and
$`P(0),G(0)\gt0\gt P(1),G(1)`$.

At $`c=a_2/d_2`$, $`P_1(c)\lt0`$. A polynomial of degree at most three with positive endpoints and this negative interior value has exactly two simple physical roots $`r_A\lt c\lt r_B`$. Its physical simplicity needs no genericity hypothesis.

The undivided identity

```math
P=\lambda_2\lambda_3L+w(a_3b_2-a_2b_3)
```

shows $`P\gt0`$ on $`(0,c]`$. Consequently every physical $`P`$ root is greater than $`c`$. Endpoint signs force either one or three odd physical roots. In the one-odd-root region, the odd root is simple or triple, with at most one further double root.

If $`P(q)=G(q)=0`$ physically, the Pluecker identity gives $`q=r_B`$. There is therefore at most one physical common root. Its two orders cannot both exceed one, since that would make $`P_1`$ multiple at $`q`$. After dividing both cubics by $`x-q`$, the residual polynomials have no common physical root.

For fixed $`\kappa\gt0`$, $`S=P-\kappa h_1G`$ is negative near both endpoints: the beta term dominates at zero, and $`h_1\to0`$ at one. Its physical zeros lie in a compact interval and are finite, since it is analytic and nonidentity. Their total multiplicity $`N`$ is even. A failed bound six therefore means $`N\ge8`$.

## 3. One divisor count when the events are distinct

Suppose $`P`$ has one odd physical root $`p`$, and $`P,G`$ have no common physical root. Every $`S`$ root is a positive contact of $`Y=P/(h_1G)`$, with the same multiplicity, and

```math
Y'=-\frac{LK}{w h_1G^2}.
```

At a physical pole $`g`$ of order $`r`$, write $`G=(x-g)^rH`$.
The leading term of $`Q`$ is

```math
-r\,w(g)P(g)H(g)(x-g)^{r-1}.
```

It is nonzero, so this pole supplies exactly $`r-1`$ physical $`K`$ weights.

Let $`o,e`$ count odd- and even-order physical poles, let $`e_+,e_-`$ classify even poles by the sign of $`Y`$ on their sides, and put $`d=\sum_g(\mathop{\mathrm{ord}}\nolimits _gG-1)`$. Let $`n_+,n_-`$ count the even numerator events by the sign of $`Y`$ on their sides. There is at most one such event, a double $`P`$ root, and write $`n=n_++n_-`$.

Ignoring an even numerator event, the odd $`P`$ event and the odd $`G`$ poles flip the positive endpoint sign. Even poles split a region without changing its sign. An even positive numerator event splits one additional positive component. Thus the number of positive components is

```math
q_+=(o+3)/2+e_++n_+.
```

Without the even numerator event there are $`(o-1)/2+e_-`$ negative components bounded by two $`G`$ poles. An even negative numerator event removes at most one of these components from the pole-to-pole Rolle count. Hence their usable count satisfies

```math
t\ge(o-1)/2+e_--n_-.
```

The bound is a lower estimate even when its right-hand side is negative. At each double numerator event, the leading term $`wP'G`$ in $`Q`$ gives exactly one $`K`$ weight. Remove this zero from the sign components when making the count, so its weight is disjoint from contact and negative-gap contributions.

Contacts totaling $`N_i`$ on one occupied positive component give at least $`N_i-1`$ derivative weights. Every usable negative pole-to-pole gap gives an extra critical root by applying Rolle to $`1/Y`$, which is zero at both ends. Together with pole weights and the $`n`$ even-numerator weights,

```math
\begin{aligned}
Z_{(0,1),\mathrm{mult}}(K)
&\ge N-q_++d+t+n\\
&\ge N-2+(d-e)+2e_-\\
&=N-2+2\sum_g\left\lfloor\frac{\mathop{\mathrm{ord}}\nolimits _gG-1}{2}\right\rfloor+2e_-\\
&\ge N-2.
\end{aligned}
```

This single count handles simple or triple odd numerator events, a collapsed double pair, and every cubic pole multiplicity. If $`N\ge8`$, the degree ceiling forces complete physical exhaustion of the six $`K`$ roots, counted with multiplicity.

## 4. Every common event has the same weighted entry

Suppose $`P(q)=G(q)=0`$. No assumption on the remaining $`P`$ events is needed. Section 2 gives the unique common root $`q=r_B`$, with minimum common order one. Write

```math
P=(x-q)A,\qquad G=(x-q)B,\qquad S=(x-q)T,
\quad T=A-\kappa h_1B.
```

The residuals $`A,B`$ are physically common-free quadratics. Exact cancellation in the Wronskian gives

```math
Q=(x-q)^2\widehat Q,\qquad K=(x-q)^2\widehat K,
\qquad\deg\widehat K\le4,
```

```math
\widehat Q=w(A'B-AB')-\lambda_1AB=-L\widehat K.
```

The function $`T`$ has finite physical root multiplicity $`M=N-1`$, including any contact at $`q`$. Every root is a positive level contact of $`V=A/(h_1B)`$. The quadratic $`B`$ has at most two distinct physical roots, so $`V`$ is analytic on at most three physical intervals. There

```math
V'=-\frac{L\widehat K}{w h_1B^2}.
```

Weighted Rolle therefore gives at least $`M-3`$ physical $`\widehat K`$ weights. Adding the two weights of the factored common event gives

```math
Z_{(0,1),\mathrm{mult}}(K)\ge2+(M-3)=N-2.
```

If $`N\ge8`$, sextic physical exhaustion follows again. This proof requires no numerator-sign classification, pole-topology table, or root perturbation. When $`\widehat K`$ also vanishes at $`q`$, its weight adds to the two factored weights in the usual divisor identity.

Both entries now have exactly the same terminal argument: the uniform geometry lemma supplies the real cofactor cubics, and the unchanged all-positive-exponent Hurwitz theorem contradicts $`N\ge8`$. This proves the main theorem.

This lemma assumes only strict actual mixed supports and six physical $`K`$ roots counted with multiplicity. It requires no initial event order or simplicity.

Set $`z=(1-x)/x`$, and let $`\bar P_1,\bar P,\bar G`$ be the degree-three reciprocal homogenizations. Put $`\bar K=(1+z)^6K(1/(1+z))`$. Since $`K(0)\lt0`$, complete physical exhaustion gives
$`\bar K(z)\lt0`$ for $`z\le0`$.

The cubic $`\bar P_1`$ has two positive roots bracketing $`b_2/a_2`$ and one negative root $`E`$. Write
$`\Delta=a_3-a_2\gt0`$, $`F=b_2-b_3\gt0`$, and
$`L_0=-F/\Delta\lt0`$. At the leftmost reciprocal $`\bar P_1`$ root, $`\bar P_1'(E)\gt0`$. The transformed critical identity reads

```math
-E(1+E)\bar P_1'(E)\bar P(E)
=(a_2E-b_2)\bar K(E)\gt0.
```

Both reciprocal linears $`(a_2-a_1)E-(b_2-b_1)`$ and $`a_2E-b_2`$ are negative. The Pluecker identity therefore gives

```math
\mathop{\mathrm{sgn}}\nolimits \bar P(E)=\mathop{\mathrm{sgn}}\nolimits \bar G(E)
=\mathop{\mathrm{sgn}}\nolimits (1+E).
```

Exact evaluation at the zero $`L_0`$ of the reciprocal $`L`$ gives

```math
\begin{aligned}
\Delta^2\bar P(L_0)&=-(\Delta-F)F(a_2F+b_2\Delta),\\
\Delta^2\bar G(L_0)&=-(\Delta-F)F((a_2-a_1)F+(b_2-b_1)\Delta).
\end{aligned}
```

Thus both signs there are $`-\mathop{\mathrm{sgn}}\nolimits (1+L_0)`$.
Neither point is $`-1`$, because

```math
\bar K(-1)=d_1d_2d_3(d_2-d_1)(d_3-d_1)(d_3-d_2)\lt0.
```

If neither fixed point were a shared positive witness, one would have
$`E\lt-1\lt L_0`$. The first inequality gives
$`\bar P_1(-1)=d_1d_2(d_2-d_1)\gt0`$, hence $`d_1\gt0`$.
The second gives $`d_3\gt d_2\gt d_1\gt0`$. Every factor in $`\bar K(-1)`$ would then be positive, a contradiction.

At a shared positive point $`z_{*}\lt0`$, both reciprocal cubics are positive. Both have negative constant term and positive cubic leading coefficient. Each consequently crosses zero in the three disjoint intervals
$`( -\infty,z_{*} )`$, $`(z_{*},0)`$, and $`(0,\infty)`$.
These exhaust its degree, so both have two simple negative roots and one simple positive root. There is no root at $`-1`$; equivalently both actual cubics have two finite real exterior roots and one simple physical root.

For a cubic with roots $`-s,-t,r`$, where $`s,t,r\gt0`$, its coefficient row is proportional to
$`(-rst,st-r(s+t),s+t-r,1)`$. A nonpositive quadratic coefficient forces the linear coefficient to be negative. A nonnegative linear coefficient forces the quadratic coefficient to be positive. Deleting zeros therefore leaves one transition from negative to positive. This is exactly the Hurwitz interface.

The root-factor theorem states that real cubics with these exterior roots and endpoint signs satisfy
$`Z_{\mathrm{mult}}(P-\kappa x^{-U}(1-x)^vG)\le6`$ for all $`U,v,\kappa\gt0`$. Its analytical proof uses the Stieltjes--Hurwitz flag, a single coefficient-insertion argument, and ordinary Descartes on integer walls. That module is retained unchanged in this proof package.

## 6. Exact reflection

Start with an opposite-cone source
$`a_1\lt0\lt a_3\lt a_2`$, $`b_3\lt0\lt b_2\lt b_1`$.
Reflect the coordinate and exchange the outer labels:
$`\widetilde a_i=b_{4-i}`$, $`\widetilde b_i=a_{4-i}`$.
Under coordinate composition,
$`\widetilde P_3=-P_1`$, $`\widetilde G=G`$, and
$`\widetilde h_1=h_3`$. The theorem gives the bound six for
$`-P_1-\kappa_1h_3G`$ under the reflected one-odd-event or common-event hypothesis.
Words $`131,113`$ correspond to $`313,133`$, respectively.
This actual-source reflection is distinct from the profile duality used inside the Hurwitz module.

## 7. The event closure is covered directly

Inside the strict support cone, the relative closure of the generic $`131`$ chart is characterized by exactly one odd physical $`P_3`$ event $`p\le r_B`$. It may contain a distinct double event, a triple event, multiple $`G`$ poles, common events, and polynomial degree drops. The main theorem now proves a bound six counted with multiplicity throughout this chart, and throughout the one-odd-event region on the $`113`$ side as well.

A separate closure proof reaches the distinct-root bound by one common-level regularization and compact sign-bracket persistence. Its explicit support-scaling construction verifies the closure characterization. It is an alternative boundary proof; it is no longer a required continuation step in the preferred common-level proof.

Strict support inequalities remain part of the source. Zero support exponents, score equalities, and zero original coefficients still use their direct lower-order arguments or the original-function transfer below.

## 8. The original boundary reduction

For a nonidentity original beta row $`F=\sum c_i m_i`$, divide by a positive monomial whose coefficient is nonzero. At any finite collection of distinct roots, a sufficiently small level shift retains one crossing at every odd contact and two at each even contact of the chosen sign. If the two even types number $`e_+,e_-`$ and the odd type numbers $`o`$, one of the two signs retains at least
$`o+2\max(e_+,e_-)\ge o+e_++e_-`$ roots in aggregate.
Avoiding the countable critical-value set makes the retained roots simple. Compact sign brackets then persist under small coefficient and exponent perturbations.

It follows that a distinct-root bound on a dense admissible sign/support parameter set extends to nonidentity finite rows in its nonnegative-coefficient and support closure. Coefficients must be free within their signs, and density must be justified relative to the permitted exponent set. A normalized positive constant can first be allowed to vary and then divided out again.

This is the original manuscript's Lemma 1, reused as one interface. Its proof is not newly needed to repair an unproved global boundary claim. The new direct weighted theorem removes physical event-simplicity and common-event exclusions before this transfer is applied. Its strict support scope remains explicit.

The auxiliary ratio-to-common-level bridge remains the retained strict, transverse theorem. A broader terminal bound does not by itself extend every division and alternating-sign step of that bridge to a boundary; the original-function transfer still justifies working in its generic chart.

The transfer does not imply continuity of a raw auxiliary multiplicity bound. It does not discard internally imposed first-loss constraints, identity rows, or missing strict support branches. Other support families and their original-root exclusions remain in the global proof.
