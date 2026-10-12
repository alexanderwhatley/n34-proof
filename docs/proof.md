# A simplified proof that $`N(3,4)=9`$

A trinomial has at most three nonzero terms; a quadrinomial has at most four. We prove that two such polynomial equations in two variables have at most nine isolated solutions with both coordinates positive, and we give an explicit example attaining nine.

This document gives the full argument assembling the upper and lower bounds. The longer proofs of specialized lemmas and the exact polynomial calculations used in them are in [the appendix](appendix.md) and its accompanying source proofs. Those lemmas are mathematical dependencies, not consequences of a case label. The appendix also includes the [reciprocal-coordinate height and regional bounds](appendix.md#reciprocal-coordinate-height-and-regional-bounds), with their precise assumptions and their place in the F3 argument.

## How to read the proof

The reduction to one variable comes first. It turns the two equations into a sum of four positive functions of the form $`x^a(1-x)^b`$, with coefficients of either sign. A shared derivative argument gives a preliminary bound of ten zeros. We then exclude ten zeros in each of the two possible sign cases. Finally, ten alternating sample signs produce an example with nine zeros.

Only distinct zeros are counted in the main theorem. Where a supporting lemma counts **multiplicity**, a zero of order $`r`$ is counted $`r`$ times. We state that stronger convention explicitly when it is used. Bounds for distinct roots pass to parameter limits by Lemma 1; a bound with multiplicity is never silently passed to a boundary case.

Some source proofs use short labels. The following explanations fix their meaning here.

| Term | Meaning in this proof |
|---|---|
| Generic parameters | Parameters outside the explicitly excluded equality sets. These sets have empty interior, so any parameters in the same open case can be approximated by generic ones. |
| Support | The exponent pairs of the nonzero terms. For a single term, its support is its exponent vector. |
| Comparable vectors | Both coordinates of one vector are no larger than the corresponding coordinates of the other. Incomparable vectors have their two coordinates ordered in opposite directions. |
| Anchor | A chosen pair of terms removed by the two division-and-differentiation operations defined below. |
| Residual | The function left after those operations and the removal of factors that never vanish. |
| Core | A polynomial factor remaining after specified nonvanishing factors are removed. |
| Source | The original parameters and polynomials derived from the same four functions; their coefficients cannot be chosen independently. |
| Chart | A change of variables, together with its inverse and domain conditions. |
| Cofactor | A determinant obtained by deleting one column from the derivative matrix; its exact formula is (5). |
| Physical root | A root in the interval corresponding to $`0<x<1`$ after a change of variable. Other real roots are called exterior roots. |
| Pole or event | A denominator root, or a specified numerator/denominator root where the interval is divided. Root orders such as $`0231`$ record the labels in increasing order. |
| Height and level | Height means the value of a real function; a level is one fixed value with which all the relevant intervals are compared. |
| Contact | In the determinant argument, a stationary point of a logarithmic ratio. In later level-curve arguments, an intersection with the specified level. The defining equation is given in each use. |
| Saturation | Equality throughout an explicitly stated sequence of root-count inequalities. It is always derived from the hypothetical ten original roots. |
| Gate or cut | An explicit inequality limiting the parameter domain or the point being considered. |
| Coefficient head | A coefficient of the transformed polynomial, not a separate geometric object. |
| Root weight | Root multiplicity. All counts called weights in the source are counts with multiplicity. |
| Mode | The point where a positive beta monomial attains its maximum. |
| Nonreal pair | Two complex-conjugate roots of a real cubic, neither on the real line. |
| Log concavity | The second derivative of the logarithm is nonpositive. This bounds the number and relative heights of intersections. |
| Positive polynomial certificate | An exact expression of a polynomial as a sum of products known to be nonnegative on the stated domain, with positive rational coefficients. It proves a uniform sign, rather than just checking numerical samples. |

The labels in square brackets identify named proofs in the appendix. The external polynomial estimate [EHT] is listed in [the references](references.md).

## Statement and reduction to four beta monomials

Write $`N(3,4)`$ for the largest number of **isolated solutions in $`\mathbb R_{>0}^2`$** of a system

```math
P_{\rm tri}(X,Y)=P_{\rm quad}(X,Y)=0,
```

where $`P_{\rm tri},P_{\rm quad}`$ are nonzero real polynomials with at most three and four nonzero monomial terms, respectively. Solutions are counted without multiplicity. One can instead use Laurent polynomials without changing the number, since multiplication by a monomial does not change positive zeros.

**Theorem 1.** With this convention,

```math
N(3,4)=9.
```

The same maximum holds if only nondegenerate positive solutions are counted.

Here a solution is *isolated* if some neighborhood of it contains no other solution, and *nondegenerate* if the Jacobian determinant $`\det\bigl(\partial(P_{\rm tri},P_{\rm quad})/\partial(X,Y)\bigr)`$ is nonzero there. The *support* of a polynomial is the set of exponent pairs of its nonzero monomial terms. For an individual beta monomial we use the more precise term *exponent vector*.

The univariate statement needed for the upper bound is stronger than the polynomial formulation. For $`s=(s_1,s_2)\in\mathbb R^2`$, put

```math
m_s(x)=x^{s_1}(1-x)^{s_2},\qquad 0<x<1.
```

We call $`m_s`$ a **beta monomial**: this means exactly a function of the displayed form, with arbitrary real exponents. Its exponent vector is $`s`$. These functions are positive and real analytic on $`(0,1)`$. A *nonidentity* function means one that is not identically zero. For such an analytic function $`F`$ and a subset $`J\subseteq(0,1)`$, write

```math
\mathop{Z}(F;J)=\#\{x\in J:F(x)=0\},\qquad \mathop{Z}(F)=\mathop{Z}(F;(0,1)),
```

allowing the value $`+\infty`$ until a finite bound is proved. A zero $`\xi`$ is *simple* if $`F'(\xi)\ne0`$.

In a sum whose terms are labeled by $`i`$, write $`s_i=(a_i,b_i)`$ and $`m_i=m_{s_i}`$. Repeated exponent vectors and zero coefficients are allowed when expressly stated. For vectors $`u,v\in\mathbb R^2`$, write $`u\preceq v`$ when $`u_1\le v_1`$ and $`u_2\le v_2`$, and $`u\prec v`$ when both inequalities are strict. Thus weak and strict coordinatewise order are distinguished explicitly. They are *strictly coordinatewise incomparable* when $`(u_1-v_1)(u_2-v_2)<0`$. *Strict coordinate orders* mean that the first coordinates are pairwise distinct and the second coordinates are pairwise distinct.

**Theorem 2 (four-term theorem).** If

```math
F(x)=\sum_{i=0}^3 c_i m_{s_i}(x)\not\equiv0,
\qquad c_i\in\mathbb R,\quad s_i\in\mathbb R^2,
```

then $`\mathop{Z}(F)\le9`$.

Theorems 3 and 4 below treat the two possible splits between positive and negative coefficients and together prove Theorem 2. First we give the precise transfer back to the polynomial problem.

A **sign case** fixes the number of positive and negative coefficients: $`(2,2)`$ means two of each, and $`(3,1)`$ means three of one sign and one of the other. Some subcases also specify orders of the exponent coordinates. A boundary of a subcase is an equality between quantities otherwise required to be strictly ordered. Specialized lemmas are used only with their stated assumptions; their detailed proofs are in [the appendix and its accompanying source proofs](appendix.md). Labels such as F2 and F3 identify these lemmas and their parameter domains.

### A trinomial with two-dimensional support

Suppose the two differences between the three support vectors of $`P_{\rm tri}`$ are linearly independent. If $`P_{\rm tri}`$ has a positive zero, its coefficients cannot all have the same sign. After changing the overall sign, dividing by its uniquely signed term, and absorbing positive constants, its equation becomes

```math
U+V=1,
```

where

```math
U=A X^{u_1}Y^{u_2},\qquad V=B X^{v_1}Y^{v_2},
\qquad A,B>0,
```

and the two exponent vectors are linearly independent. Taking logarithms shows that $`(X,Y)\mapsto(U,V)`$ is a real analytic diffeomorphism of the positive quadrant onto itself. Each monomial in $`P_{\rm quad}`$ becomes a positive constant times $`U^aV^b`$, with $`a,b`$ real. On $`U+V=1`$ set $`x=U`$. The restriction of $`P_{\rm quad}`$ is a sum of at most four beta monomials.

If this restriction is an identity, the entire positive trinomial curve lies in $`P_{\rm quad}=0`$, so it contributes no isolated intersection. Otherwise its distinct zeros correspond bijectively to the positive intersections of the original system. Theorem 2 gives at most nine.

### Collinear support and fewer terms

If the trinomial support is collinear, a logarithmic linear coordinate change and a positive monomial division turn its equation into a univariate sum of at most three real exponentials. Such a nonidentity sum has at most two real zeros. Indeed, divide by one exponential, differentiate, and apply Rolle inductively; a sum with $`k`$ distinct exponential terms has at most $`k-1`$ zeros.

Each zero fixes one logarithmic coordinate. The restriction of $`P_{\rm quad}`$ to that line is a sum of at most four exponentials in the other coordinate, and has at most three zeros unless it is an identity. An identity gives a common curve, not isolated intersections. Hence this case contributes at most $`2\cdot3=6`$ isolated positive intersections. A binomial or monomial is easier. This deals with the degenerate trinomial supports directly.

## Tools shared by the cases

### Notation and the differentiation rule

The following conventions are used throughout this document.

| Symbol | Meaning |
|---|---|
| $`P_{\rm tri},P_{\rm quad}`$ | The original polynomials in two variables. |
| $`F`$, or $`f`$ in the three-versus-one case | The resulting function of one variable. |
| $`s_i=(a_i,b_i)`$, $`m_i=m_{s_i}`$ | An exponent pair and the function $`x^{a_i}(1-x)^{b_i}`$. |
| $`\mathop{Z}(F;J)`$, $`\mathop{Z}(F)`$ | Numbers of distinct zeros in $`J`$ and in $`(0,1)`$. |
| $`u\preceq v`$, $`u\prec v`$ | Both coordinates are no larger, or both are strictly smaller. |
| $`e_i`$, $`K`$ | The normalized determinants defined in (5). |

Each major subcase defines its own local variables. A letter newly defined there does not retain an earlier local meaning. In particular, $`p`$ sometimes denotes an exponent vector and sometimes a polynomial; the relevant definition is printed before use. The variable in which differentiation is taken is also stated. This keeps the source formulas intact without requiring the reader to track conventions from separate research notes.

For $`x\in(0,1)`$ and an exponent vector $`s=(s_1,s_2)`$, set

```math
\rho(x)=x(1-x),\qquad D=\rho(x)\frac{d}{dx},\qquad
\lambda_s(x)=D\log m_s(x)=s_1-(s_1+s_2)x.
```

Thus $`Dm_s=m_s\lambda_s`$. For labeled terms, $`\lambda_i`$ abbreviates $`\lambda_{s_i}`$. If a beta monomial is denoted by a letter $`u=m_s`$, we also write $`\lambda_u=D\log u=\lambda_s`$. For $`C^{k-1}`$ functions $`f_1,\ldots,f_k`$ on $`(0,1)`$, let

```math
W_D(f_1,\ldots,f_k)=\det(D^{i-1}f_j)_{i,j=1}^k.
```

This determinant is the Wronskian for the differentiation operator $`D`$. Using $`D`$ rather than ordinary differentiation does not change zeros of first derivatives in the open interval. Division by a positive function also preserves zeros. In particular, for a positive beta monomial $`m`$, the operation $`F\mapsto D(F/m)`$ removes a constant multiple of $`m`$ from the sum and loses at most one zero by Rolle’s theorem. We will use this division-and-differentiation operation repeatedly.

### Removing repeated roots by a small parameter change

**Lemma 1 (one-coefficient regularization and transfer).** Let $`k\ge1`$, let $`c=(c_1,\ldots,c_k)\in\mathbb R^k`$ and $`s=(s_1,\ldots,s_k)\in(\mathbb R^2)^k`$, and put

```math
F_{c,s}(x)=\sum_{i=1}^k c_i m_{s_i}(x),\qquad x\in(0,1).
```

**(a)** Suppose $`F_{c,s}\not\equiv0`$, fix an index $`j`$ with $`c_j\ne0`$, and let $`\xi_1,\ldots,\xi_n`$ be any $`n\ge1`$ distinct zeros of $`F_{c,s}`$. Let $`J_1,\ldots,J_n`$ be pairwise disjoint open intervals containing these zeros, with closures contained in $`(0,1)`$. For every $`\varepsilon>0`$ there exists $`t\in\mathbb R`$ such that

```math
0<|t|<\min\{\varepsilon,|c_j|/2\}
```

and

```math
F_t(x):=F_{c,s}(x)-t m_{s_j}(x)
```

has at least $`n`$ distinct simple zeros in $`\bigcup_{\nu=1}^n J_\nu`$. Moreover, every zero of $`F_t`$ in $`(0,1)`$ is simple. This changes only $`c_j`$, replacing it by $`c_j-t`$; in particular, its sign is preserved.

**(b)** Fix a sign vector $`\sigma\in\{-1,1\}^k`$, a nonempty exponent set $`S\subseteq(\mathbb R^2)^k`$, and an integer $`N_0\ge0`$. Define

```math
\mathcal P_{\sigma,S}
=\{(c,s)\in\mathbb R^k\times S:\sigma_i c_i>0\text{ for every }i\}.
```

Let $`\mathcal G`$ be dense in $`\mathcal P_{\sigma,S}`$ in the relative Euclidean topology. Assume that for every $`(c,s)\in\mathcal G`$, the function $`F_{c,s}`$ is not identically zero, all its zeros in $`(0,1)`$ are simple, and $`\mathop{Z}(F_{c,s})\le N_0`$. Then

```math
\mathop{Z}(F_{c,s})\le N_0
```

for every $`(c,s)`$ satisfying $`\sigma_i c_i\ge0`$ for all $`i`$, $`s\in\overline S`$, and $`F_{c,s}\not\equiv0`$. The closure $`\overline S`$ is taken in the finite-dimensional Euclidean exponent space.

**Proof.** For (a), set $`h=F_{c,s}/m_{s_j}`$. Positivity of the denominator preserves the zeros and their orders. Since $`h`$ has a zero and is not identically zero, it is nonconstant. At each $`\xi_\nu`$ there are an integer $`r_\nu\ge1`$ and a nonzero real number $`A_\nu`$ such that

```math
h(x)=A_\nu(x-\xi_\nu)^{r_\nu}
+O\bigl((x-\xi_\nu)^{r_\nu+1}\bigr).
```

Shrink a neighborhood of each $`\xi_\nu`$ inside $`J_\nu`$ so that $`h`$ is strictly monotone on each side of $`\xi_\nu`$. If $`r_\nu`$ is odd, each sufficiently small positive or negative level $`t`$ is attained once near $`\xi_\nu`$. If $`r_\nu`$ is even, a sufficiently small level with the sign of $`A_\nu`$ is attained twice, once on each side; a level of the opposite sign is not attained there.

Let $`o`$ count the selected odd-order zeros. Among the selected even-order zeros, let $`e_+`$ count those with $`A_\nu>0`$ and $`e_-`$ those with $`A_\nu<0`$. Thus the two signs of a sufficiently small $`t`$ give at least $`o+2e_+`$ and $`o+2e_-`$ nearby roots, respectively. One of these numbers is at least

```math
o+2\max(e_+,e_-)\ge o+e_++e_-=n.
```

Choose that sign. The zeros of the nonzero analytic function $`h'`$ form a discrete, hence countable, subset of $`(0,1)`$. Their images under $`h`$ are countable as well. We can therefore choose $`t`$ of the required sign, arbitrarily close to zero and obeying the stated bound, outside this set of critical values. At every zero of $`F_t=m_{s_j}(h-t)`$,

```math
F_t'=m_{s_j}h'\ne0.
```

This proves both simplicity and the asserted nearby root count. The inequality $`|t|<|c_j|/2`$ gives $`c_j(c_j-t)>0`$.

For (b), suppose a function in the claimed closure has $`n=N_0+1`$ distinct zeros. Since it is not identically zero, at least one coefficient $`c_j`$ is nonzero. Apply (a). The perturbed parameter still belongs to

```math
\overline{\mathcal P_{\sigma,S}}
=\{(c,s):\sigma_i c_i\ge0\text{ for every }i,\ s\in\overline S\},
```

because its exponents are unchanged and its nonzero coefficient retains its sign. Around $`n`$ of the resulting simple zeros choose pairwise disjoint closed intervals whose endpoint values have opposite signs. Evaluation of $`F_{c,s}`$ at each fixed interior endpoint is continuous in all coefficients and exponents. Those finitely many strict sign inequalities consequently hold throughout a parameter neighborhood of the perturbed function. This neighborhood meets $`\mathcal G`$ by density. Its member has at least one zero in each interval, contradicting the bound $`N_0`$ on $`\mathcal G`$. $`\square`$

**Scope of the transfer.** Part (a) preserves at least $`n`$ zeros in the union of the chosen intervals; it need not preserve a zero in every individual interval. Part (b) assumes that the coefficients can vary independently within their prescribed signs: $`S`$ restricts only the exponents. For example, a normalized constant coefficient equal to one is handled by first allowing a positive constant coefficient and then dividing by it again. Additional constraints on coefficients require their own justification.

A *regular value* of a differentiable function is a value whose preimages all have nonzero derivative. At fixed exponents, regular level shifts as in the proof give functions with only simple zeros arbitrarily close to any coefficient vector in the open sign orthant. If $`F_{c,s}/m_{s_j}`$ is constant, a small shift instead makes the function nonvanishing. Thus a dense set of exponent configurations gives a dense joint set with simple zeros. In the applications below, genericity requires strict coordinate orders and, where a technical input specifies them, avoidance of its exceptional parameter sets with empty interior. Density of that joint set is the hypothesis of (b), not a consequence of the word *generic*.

Only finitely many interior intervals are used. Applying (b) after all neighboring strict cases have been proved includes finite exponent ties, repeated exponent vectors, and zero coefficients. Internal first-collision arguments in an auxiliary family retain their separate boundary proofs; they are not applications of this final transfer.

### The external two-polynomial estimate

We use the following theorem of El Hilany and Tavenas [EHT](references.md):

```math
P+x^\alpha(1-x)^\beta Q\not\equiv0
\quad\Longrightarrow\quad
\mathop{Z}\bigl(P+x^\alpha(1-x)^\beta Q\bigr)
\le\deg P+\deg Q+2.                                      \tag{1}
```

Here $`P,Q`$ are nonzero real polynomials and $`\alpha,\beta`$ are real. Zero-polynomial cases are treated directly. A common polynomial factor may first be removed and its distinct roots added back. We use only the distinct-root consequence, with the identity excluded.

### A derivative reduction and the preliminary bound ten

Fix exponent vectors $`p=(p_1,p_2)`$ and $`q=(q_1,q_2)`$ in $`\mathbb R^2`$. In this subsection,

```math
\lambda_p(x)=p_1-(p_1+p_2)x,\qquad
\lambda_q(x)=q_1-(q_1+q_2)x,
```

so that $`Dm_p=m_p\lambda_p`$, $`Dm_q=m_q\lambda_q`$, and

```math
D\lambda_p=-(p_1+p_2)x(1-x),\qquad
D\lambda_q=-(q_1+q_2)x(1-x).
```

Define the following function of $`x`$:

```math
H(p,q;x)=\lambda_pD\lambda_q-\lambda_qD\lambda_p
+\lambda_p\lambda_q(\lambda_q-\lambda_p).
\tag{2}
```

The argument $`x`$ is suppressed only in the factors on the right side of (2). Substitution gives the explicit polynomial

```math
\begin{split}
H(p,q;x)={}&(p_2q_1-p_1q_2)x(1-x)\\
&+[p_1-(p_1+p_2)x]\,[q_1-(q_1+q_2)x]\\
&\qquad\cdot[(q_1-p_1)-((q_1+q_2)-(p_1+p_2))x].
\end{split}
```

Thus $`H(p,q;\cdot)\in\mathbb R[x]`$ has **degree at most three in $`x`$**. Its degree can be smaller, and it can be identically zero. Its endpoint values are

```math
H(p,q;0)=p_1q_1(q_1-p_1),\qquad
H(p,q;1)=-p_2q_2(q_2-p_2).                              \tag{3}
```

To derive the Wronskian identity used below, the product rule gives

```math
D^2m_s=m_s(\lambda_s^2+D\lambda_s).
```

Consequently,

```math
\begin{split}
W_D(Dm_p,Dm_q)
&=(Dm_p)(D^2m_q)-(Dm_q)(D^2m_p)\\
&=m_pm_q H(p,q;x)
=W_D(1,m_p,m_q).
\end{split}                                                   \tag{3a}
```

**Lemma 2.** Let $`F=\sum_{i=0}^3 c_i m_{s_i}\not\equiv0`$, where $`c_i\in\mathbb R`$ and $`s_i\in\mathbb R^2`$. If $`c_ic_j\ne0`$ and the corresponding exponent vectors satisfy

```math
(s_{i,1}-s_{j,1})(s_{i,2}-s_{j,2})<0,
```

then $`\mathop{Z}(F)\le10`$.

**Proof.** Divide by one of these beta monomials and write

```math
F_0=c_0+c_1m_p+c_2m_q+c_3m_r,
\qquad p_1>0>p_2.
```

Here $`p,q,r\in\mathbb R^2`$ are exponent differences after division and relabeling, and $`F_0`$ is $`F`$ divided by a positive beta monomial; hence $`\mathop{Z}(F_0)=\mathop{Z}(F)`$. Since $`\lambda_p(x)=p_1(1-x)-p_2x>0`$, we have $`Dm_p>0`$ throughout $`(0,1)`$. Using (3a) in the quotient rule gives

```math
D\left(\frac{DF_0}{Dm_p}\right)
=\frac{m_p}{(Dm_p)^2}
\{c_2m_qH(p,q;x)+c_3m_rH(p,r;x)\}.                \tag{4}
```

After division by $`m_q>0`$, the expression in braces becomes

```math
c_2H(p,q;x)+c_3x^{r_1-q_1}(1-x)^{r_2-q_2}H(p,r;x).
```

If both polynomial terms are nonzero and the expression is not identically zero, (1) gives at most $`3+3+2=8`$ distinct zeros. If precisely one polynomial term is zero, the remaining term has at most three. Two applications of Rolle’s theorem, with division by the nonvanishing function $`Dm_p`$ between them, therefore give $`\mathop{Z}(F)\le8+2=10`$. If the expression is identically zero, (4) makes $`DF_0/Dm_p`$ constant on $`(0,1)`$. Integration gives $`F_0=A+Bm_p`$, whose nonidentity root count is at most one because $`m_p`$ is strictly increasing. $`\square`$

For a function with four nonzero coefficients, strict coordinate orders, and no incomparable exponent pair, those vectors form a coordinatewise chain. After division by the least beta monomial, every other exponent vector has both coordinates positive. Choose one, $`p`$, as derivative divisor. Then $`Dm_p`$ has exactly one simple interior zero $`z`$. If $`DF_0(z)\ne0`$, a finite collection of $`N`$ zeros of $`DF_0`$ lies in the two intervals separated by $`z`$; Rolle applied to the quotient on those intervals supplies at least $`N-2`$ zeros of its derivative. If $`DF_0(z)=0`$, the quotient extends analytically across $`z`$, and at most one of those $`N`$ zeros is lost on division, again giving at least $`N-2`$ derivative zeros. The same polynomial estimate therefore gives $`\mathop{Z}(DF_0)\le10`$ and $`\mathop{Z}(F_0)\le11`$. An identically zero residual instead gives $`F_0=A+Bm_p`$, with at most two zeros. Both eventual endpoint signs of $`F_0`$ equal the sign of its nonzero constant coefficient. If all zeros are simple, their number is even, so the bound eleven improves to ten.

Apply Lemma 1(b) with $`k=4`$, $`S=(\mathbb R^2)^4`$, and a fixed coefficient-sign vector. Strict coordinate orders are dense, and the regular shifts in Lemma 1 give the required dense set with simple zeros. The incomparable and chain arguments together bound that entire set by ten. Lemma 1 transfers this bound to all nonidentity functions in its closure.

Thus ten is a general preliminary ceiling. If a function with strict coordinate orders and simple zeros has opposite endpoint signs, different beta monomials of opposite coefficient signs dominate the two endpoints. Their exponent vectors are incomparable. Lemma 2 and odd parity already give nine. The difficult part of the upper bound is therefore the exclusion of **ten simple roots with equal endpoint signs**.

### Determinants and a common horizontal level

An *anchor* is a chosen pair $`m_i,m_j`$ used for the two successive operations

```math
F\longmapsto D(F/m_i)
\longmapsto D\left(\frac{D(F/m_i)}{D(m_j/m_i)}\right).
```

The order $`i,j`$ specifies the first divisor. The anchor is *monotone* when $`D(m_j/m_i)`$ has no zero on $`(0,1)`$, as for a strictly incomparable exponent pair; an *oriented* monotone anchor is ordered so this derivative is positive. A *same-sign* anchor has $`c_ic_j>0`$; a *positive-pair* or *negative-pair* anchor has both coefficients positive or both negative, respectively. Its *complementary pair* consists of the two labels not in the anchor. These coefficient signs are separate from the signs of exponent coordinates. The phrase *derivative anchor* refers to this division-and-differentiation construction. The remaining two-term expression after removal of nonvanishing factors is the *residual*. A polynomial *core* is the polynomial factor left in a derivative or determinant after its specified nonvanishing factors have been removed. A *physical* root lies in the interval corresponding to $`0<x<1`$ under the current coordinate; an *exterior* root lies outside it. No exterior root is counted as a root of the original problem.

For four labeled exponent vectors $`s_i=(a_i,b_i)`$, $`i=0,1,2,3`$, recall the abbreviations $`m_i=m_{s_i}`$ and $`\lambda_i=\lambda_{s_i}`$. Define

```math
e_i=(-1)^i
\frac{W_D(m_0,\ldots,\widehat m_i,\ldots,m_3)}{\prod_{j\ne i}m_j},
\qquad
K=\frac{W_D(m_0,m_1,m_2,m_3)}{m_0m_1m_2m_3}.             \tag{5}
```

The hat means omission of that column. Thus $`e_i`$ is a signed, normalized three-column minor, and $`K`$ is the normalized four-column determinant. These are polynomials in $`x`$, with $`\deg_x e_i\le3`$ and $`\deg_x K\le6`$; identically zero cases are handled separately. Indeed, define

```math
B_{s,0}=1,\qquad B_{s,r+1}=\lambda_s B_{s,r}+DB_{s,r}.
```

Then $`D^r m_s=m_s B_{s,r}`$ and $`\deg_x B_{s,r}\le r`$ by induction. Factoring the beta monomial from each determinant column gives the degree bounds $`0+1+2=3`$ and $`0+1+2+3=6`$. If $`j,k,l`$ are the increasing complement of $`i`$, put

```math
\Delta_i=\det\begin{pmatrix}1&1&1\\a_j&a_k&a_l\\b_j&b_k&b_l\end{pmatrix}.
```

The unsigned polynomial $`T_i=(-1)^ie_i`$ satisfies

```math
T_i=\prod_{r<s,\ r,s\ne i}(\lambda_s-\lambda_r)-\rho\Delta_i.
\tag{6}
```

In particular,

```math
T_i(0)=\prod_{r<s,\ r,s\ne i}(a_s-a_r),\quad
T_i(1)=-\prod_{r<s,\ r,s\ne i}(b_s-b_r),                  \tag{7}
```



```math
K(0)=\prod_{r<s}(a_s-a_r),\qquad
K(1)=\prod_{r<s}(b_s-b_r).                               \tag{8}
```

The products in (7)–(8) are Vandermonde products, namely products of all pairwise differences in the stated order. The products for three and four columns have three and six factors, respectively. At $`x=1`$, each difference becomes $`\lambda_s(1)-\lambda_r(1)=-(b_s-b_r)`$. The odd factor count in (7) gives a minus sign, while the even factor count in (8) gives a plus sign. Below, *cubic* and *sextic* describe the relevant degree bounds unless a nonzero leading coefficient is specified.

For complementary ordered pairs $`i<j`$, $`k<l`$, let $`\varepsilon(i,j,k,l)`$ be the sign of that permutation of $`(0,1,2,3)`$. Jacobi’s complementary-minor identity for these Wronskians gives, wherever $`e_ke_l\ne0`$,

```math
D\log\left|\frac{m_ke_l}{m_le_k}\right|
=\frac{\varepsilon(i,j,k,l)(\lambda_j-\lambda_i)K}{e_ke_l}.       \tag{9}
```

In polynomial form, the identity being used is

```math
(\lambda_k-\lambda_l)e_ke_l+e_kDe_l-e_lDe_k
=\varepsilon(i,j,k,l)(\lambda_j-\lambda_i)K.
```

It can also be checked by expanding the minors in (5): their normalized rows are $`1`$, $`\lambda_i`$, $`\lambda_i^2+D\lambda_i`$, and $`\lambda_i^3+3\lambda_iD\lambda_i+D^2\lambda_i`$. The quotient and product rules turn this polynomial identity into (9). On the domain $`D(m_j/m_i)\ne0`$, the residual of the anchor $`i,j`$ vanishes precisely when

```math
c_km_ke_l=c_lm_le_k.                  \tag{10}
```

To check the placement of the monomial factors, put $`r=m_j/m_i`$ and suppose $`Dr\ne0`$. The quotient rule and the common-factor identity for a Wronskian give

```math
\begin{aligned}
R_{ij}:=D\left(\frac{D(F/m_i)}{Dr}\right)
&=\frac{c_kW_D(m_i,m_j,m_k)+c_lW_D(m_i,m_j,m_l)}
{m_i^3(Dr)^2}\\
&=\frac{\varepsilon(i,j,k,l)m_j}{m_i^2(Dr)^2}
\bigl(c_lm_le_k-c_km_ke_l\bigr).
\end{aligned}                                                   \tag{10a}
```

Indeed, multiplying each of three Wronskian columns by $`m_i`$ multiplies the determinant by $`m_i^3`$; derivatives of that common factor are eliminated by row operations. The ordering in (5) then gives $`W_D(m_i,m_j,m_k)=-\varepsilon(i,j,k,l)m_im_jm_ke_l`$ and $`W_D(m_i,m_j,m_l)=\varepsilon(i,j,k,l)m_im_jm_le_k`$. The prefactor in (10a) is nonzero, proving (10). Assume here that $`c_kc_l\ne0`$ and the relevant cofactors have no common physical zero, as required in the strict source cases. A residual root then has $`e_ke_l\ne0`$. Its *useful set*, the region where the signs permit (10), is

```math
U_{kl}=\{x\in(0,1):c_kc_l e_k(x)e_l(x)>0\}.
```

A useful component is a connected interval of this open set. Define the *phase*

```math
\phi_{kl}(x)=\log\left|\frac{m_ke_l}{m_le_k}\right|.
```

On every useful component, (10) is the equation $`\phi_{kl}=\log|c_l/c_k|`$, at the **same original coefficient level**. A stationary phase point is a zero of $`D\phi_{kl}`$; some sources call it a *contact*. This differs from a level intersection, a solution of $`\phi_{kl}=\log|c_l/c_k|`$. For a monotone complementary anchor, (9) identifies stationary phase points with zeros of $`K`$. For the following finite count, assume also $`K\not\equiv0`$. Strict coordinate orders guarantee this by (8). On an interval with $`r`$ such points, Rolle permits at most $`r+1`$ intersections with any fixed level. Summing over the useful components gives

```math
\#(\text{residual roots})\le
\#(\text{useful components})+\mathop{Z}(K;U_{kl}).        \tag{11}
```

All applications below retain these coefficient constraints. A degree bound on an arbitrary sextic, or a count at separately chosen levels on different components, would not prove the required result.

When several anchors are used, a point is *jointly useful* if it belongs to every useful set required by those anchors. A *gate* in the source notes means an explicitly stated inequality restricting those points or their parameters. Common cofactor roots, vanishing cofactors, and other excluded equalities require the source proof’s lower-degree argument or the justified final transfer of Lemma 1; (11) alone does not handle them.

The cofactor simplicity and disjointness assumptions used in the strict cases exclude proper algebraic sets. This can be checked without a rank-by-rank enumeration. After a common exponent translation, take

```math
(s_0,s_1,s_2,s_3)=((0,0),(1,2),(2,5),(3,9)).
```

The signed cofactors, divided respectively by $`2,6,6,2`$, are

```math
\begin{array}{ll}
P_0=-90x^3+61x^2-14x+1,&P_1=70x^3-52x^2+13x-1,\\
P_2=-54x^3+44x^2-12x+1,&P_3=42x^3-37x^2+11x-1.
\end{array}
```

The discriminant vanishes precisely when a polynomial has a repeated complex root; the resultant of two polynomials vanishes precisely when they share a complex root. Here the discriminants are $`-1668,-1156,-716,-507`$. Their pairwise resultants in the order $`01,02,03,12,13,23`$ are $`60,-378,972,36,-210,18`$. All are nonzero. Each corresponding discriminant or resultant is therefore a nonzero polynomial in the support coordinates; its zero set has empty interior in every strict coordinate-order case. A finite union of these sets still has empty interior. Regular coefficient shifts from Lemma 1 supply simple original roots on the resulting dense support set. Family-specific exceptional sets beyond these cofactor conditions retain their cited source proofs.

**Lemma 2A (simultaneous anchor saturation).** Fix a nonidentity four-term beta sum with nonzero coefficients and strict coordinate orders. Suppose the signed cofactors have simple, pairwise disjoint physical roots. Let $`\mathcal A`$ be a collection of monotone anchors. For each anchor, write $`kl`$ for its complementary pair, $`U_{kl}=\{c_kc_l e_ke_l>0\}`$, and let $`b_{kl}`$ be its number of components. Let $`T=\mathop{Z}(K)`$ and suppose a proved degree or parity bound gives $`T\le d`$.

If $`F`$ has $`n`$ distinct roots, then every anchor in $`\mathcal A`$ satisfies

```math
\mathop{Z}(K;(0,1)\setminus U_{kl})
\le T-n+2+b_{kl}\le d-n+2+b_{kl}. \tag{11a}
```

In particular, an anchor with $`n-2-b_{kl}=d`$ forces exactly $`d`$ physical contacts, all in its useful set. Form a graph on the four labels whose edges are the complementary pairs of all such anchors. Every one of those contacts has a constant sign of $`c_i e_i`$ within each connected component of this graph. If the graph is connected, all four signs agree.

**Proof.** For $`n\le2`$, (11a) is immediate from its right side. For $`n\ge3`$, both divisions in a monotone anchor are by nonvanishing functions. Rolle therefore supplies at least $`n-2`$ distinct residual roots. If a residual were identically zero, integrating its defining equation would express $`F`$ as a linear combination of the two anchor beta monomials; their monotone ratio would give at most one original root. Thus this exception cannot occur when the displayed lower bound is positive. Every residual root belongs to $`U_{kl}`$, and (11) gives

```math
n-2\le b_{kl}+\mathop{Z}(K;U_{kl}).
```

Subtract from the total physical contact count $`T`$ to obtain (11a). When its last upper bound is zero and $`n-2-b_{kl}=d`$, the same inequality forces $`T=d`$ and inclusion of the whole contact set in $`U_{kl}`$. For every graph edge this inclusion says that the two nonzero values $`c_ke_k`$ and $`c_le_l`$ have equal signs. Equality propagates along paths. $`\square`$

This lemma uses the actual residuals and their original coefficient levels. No generic simplicity of residual roots is needed. The graph argument is the common equality mechanism behind the simultaneous equality arguments for connected sets of term pairs; the useful-component counts and any sharper contact bound remain family-specific inputs.

**Definition (saturation of a root-count bound).** Suppose a proved counting chain for a proposed configuration is

```math
N\le a_0\le a_1\le\cdots\le a_r\le N.
```

We say that this chain is **saturated** precisely when

```math
\boxed{a_0=a_1=\cdots=a_r=N.}
```

Here each $`a_j`$ is a root count plus the losses already allowed by the preceding operations. Thus saturation is equality throughout a specified chain of bounds. For example, if $`F`$ has ten simple zeros and $`i,j`$ is a monotone anchor, write $`F_1=D(F/m_i)`$ and let $`R_{ij}`$ be (10a). The degree estimate in the proof of Lemma 2 yields

```math
10=\mathop{Z}(F)\le\mathop{Z}(F_1)+1\le\mathop{Z}(R_{ij})+2\le10,
\qquad \mathop{Z}(F_1)=9,\quad\mathop{Z}(R_{ij})=8.
```

The phrase *equality in the ten-root counting bounds* below refers to these forced equalities, or to the corresponding explicitly stated chain in a technical input. Equality in one chain does not automatically give equality in an unrelated estimate. In particular, a component or contact bound such as (11) is saturated only when its proved upper bound equals the count required by the preceding chain. An extra zero or a strict improvement then contradicts the assumed ten roots.

### A differential operator and an interpolation lemma

For $`0<\theta<1`$, $`k\le1`$, define

```math
\mathcal L_{\theta,k}f=\rho f''+k(\theta-x)f'+kf.
\tag{15}
```

It annihilates $`\theta-x`$ and has a positive kernel solution on $`(0,1)`$. To see this, let $`h_0=x^{1-\theta}(1-x)^\theta`$. Then

```math
\frac{\mathcal L_{\theta,k}h_0}{h_0}
=-\frac{(1-k)\theta(1-\theta)}\rho\le0.
```

Writing a solution of $`\mathcal L_{\theta,k}h=0`$ as $`h=h_0z`$ gives $`z''+pz'-Vz=0`$, where

```math
p=2h_0'/h_0+k(\theta-x)/\rho,\qquad
V=(1-k)\theta(1-\theta)/\rho^2\ge0.
```

For an interior base point $`x_0`$, put $`\mu(x)=\exp(\int_{x_0}^x p(t)\,dt)>0`$. Initial data $`z(x_0)=1,z'(x_0)=0`$ produce a positive solution on both sides: while $`z>0`$, the identity $`(\mu z')'=\mu Vz\ge0`$ makes $`z`$ nondecreasing to the right and nonincreasing as $`x`$ increases on the left, so it cannot reach zero on either side. The two solutions $`h>0`$ and $`\theta-x`$ are independent, and Abel’s Wronskian identity makes $`\tau=(\theta-x)/h`$ a coordinate with nonzero derivative. More precisely, for $`f=h\,v(\tau)`$ one has $`\mathcal L_{\theta,k}f=\rho h(\tau')^2v''(\tau)`$. It therefore loses at most two distinct zeros by Rolle. This is the only property of this differential operator needed here. The source uses the term *disconjugate* for this property.

The following interpolation lemma is [F1-INT]. It will be used for both comparable orientations in Lemma 3A.

**Lemma 3.** Let $`P,Q`$ be real polynomials of degree at most three, with $`P\ne0`$ and $`P(r)=0`$ for some $`r\in(0,1)`$. If $`0<a,b<1`$ and $`\kappa\ne0`$, the equation

```math
Q(x)=\kappa x^a(1-x)^bP(x)
```

has at most seven distinct solutions in $`(0,1)`$.

**Proof.** Suppose eight distinct solutions $`x_i`$ exist. Set $`\omega(z)=\prod_{i=1}^8(z-x_i)`$ and $`P_r(z)=P(z)/(z-r)`$. Since $`\deg(QP_r)\le5`$, comparison of the coefficient of $`z^7`$ in its Lagrange interpolation at the eight nodes gives

```math
\sum_{i=1}^8\frac{Q(x_i)P_r(x_i)}{\omega'(x_i)}=0.
```

Substitute the assumed equality and divide by $`\kappa`$. Choose principal branches of $`m(z)=z^a(1-z)^b`$ on the plane cut along $`(-\infty,0]\cup[1,\infty)`$. The jumps are $`2i\sin(\pi a)(-t)^a(1-t)^b`$ on the left and $`-2i\sin(\pi b)t^a(t-1)^b`$ on the right. Contour deformation applied to $`mPP_r/\omega`$ gives

```math
\begin{split}
\sum_i\frac{m(x_i)P(x_i)P_r(x_i)}{\omega'(x_i)}
={}&-\frac{\sin\pi a}{\pi}\int_{-\infty}^0
\frac{(-t)^a(1-t)^b(r-t)P_r(t)^2}{\omega(t)}\,dt\\
&-\frac{\sin\pi b}{\pi}\int_1^\infty
\frac{t^a(t-1)^b(t-r)P_r(t)^2}{\omega(t)}\,dt<0.
\end{split}
```

Both integrals converge: the integrand at infinity is $`O(|t|^{a+b-3})`$, and $`a+b<2`$. The endpoint small-circle terms vanish because $`a,b>0`$. Both integrals are strictly positive before their displayed minus signs, since $`\omega>0`$ on the exterior cuts and $`P_r\ne0`$. This contradicts interpolation. $`\square`$

## Two positive and two negative coefficients

**Theorem 3 (sign-case theorem).** Let $`s_0,s_1,s_2,s_3\in\mathbb R^2`$, let $`c_0,c_1>0`$ and $`c_2,c_3<0`$, and suppose $`F=\sum_{i=0}^3c_i m_{s_i}\not\equiv0`$. Then $`\mathop{Z}(F)\le9`$.

We give the assembly, an eight-entry order reduction, and representative analytic mechanisms. The remaining specialized lemmas are the explicitly identified inputs [C22] in [the appendix](appendix.md).

Parity is first used for the generic functions specified by those inputs: a finite set of simple zeros has even cardinality when the eventual endpoint signs agree, and odd cardinality when they differ. Where an auxiliary residual is counted this way, its simplicity is an additional source hypothesis; it does not follow from simplicity of $`F`$. The cited arguments justify these generic choices, and Lemma 1 transfers their bounds to arbitrary distinct original roots.

### Endpoint dominants and three remaining families

Work first at strict generic supports with simple original roots. The preliminary ceiling of ten and endpoint parity reduce the problem to excluding ten roots with equal endpoint signs. Reverse all coefficients if necessary so that their common sign is positive. If the same beta monomial dominates both endpoints, it is globally least, and the extended global-least theorem proved below gives eight.

Otherwise label the two distinct positive endpoint dominants $`0`$ at zero and $`1`$ at one. Their supports are incomparable. Monotone-anchor saturation forces the second beta monomial in each endpoint order to be negative: after division by the minimal beta monomial, a positive second coefficient would give an extra first-derivative root outside the original interlacing hull. Label the first-coordinate second beta monomial $`2`$ and the other negative beta monomial $`3`$. Thus

```math
\text{first order}\in\{0213,0231\},\qquad
\text{second order}\in\{1203,1230,1302,1320\}.
```

For an oriented monotone anchor $`i,j`$, saturation gives exactly nine first-derivative roots and eight residual roots. Its eventual residual sign must be positive at both endpoints. If $`k`$ and $`l`$ are the first- and second-coordinate minima outside the anchor, and $`A_i,B_i`$ are coordinate ranks, endpoint dominance therefore requires

```math
\mathop{sgn}(c_k)\mathop{sgn}[(A_k-A_i)(A_k-A_j)]=+1,
\quad
\mathop{sgn}(c_l)\mathop{sgn}[(B_l-B_i)(B_l-B_j)]=+1. \tag{12}
```

These necessary signs apply to mixed-sign anchors as well as same-sign anchors. They give the complete eight-entry hand table:

```math
\begin{array}{c|cccc}
&1203&1230&1302&1320\\\hline
0213&\mathrm{F2}&\mathrm{E}&\mathrm{F3}&\mathrm{F4}\\
0231&\mathrm{E}&\mathrm{E}&\mathrm{F4\ reflected}&\mathrm{E}
\end{array}
```

For $`0213/1230`$, anchor $`1,2`$ has negative label $`3`$ as the dominant complementary beta monomial at the second endpoint, beyond both anchor labels; its residual sign violates (12). For $`0231/1203,0231/1230,0231/1320`$, anchor $`0,2`$ gives the same violation at the first endpoint. Finally physical reflection and swaps $`0\leftrightarrow1`$, $`2\leftrightarrow3`$ send $`0231/1302`$ to $`0213/1320`$.

Only F2, F3 and F4 remain. Their first-coordinate order is $`a_0<a_2<a_1<a_3`$, and their respective second-coordinate orders are $`1203,1302,1320`$. For example, $`1203`$ means $`b_1<b_2<b_0<b_3`$. This eight-entry reduction is the argument [EIGHT-ORDER].

### One comparable-term theorem

**Lemma 3A (one comparable-term bound).** Let $`A,B,C>0`$ and

```math
F=1+A m_u-Bm_v-Cm_w.
```

Suppose all coordinates of $`u,v,w`$ are positive, $`u`$ and $`v`$ are comparable, and both lie northwest of $`w`$:

```math
u_1<w_1,\quad v_1<w_1,\qquad
u_2>w_2,\quad v_2>w_2,
```

with either $`u_1<v_1,\ u_2<v_2`$ or $`u_1>v_1,\ u_2>v_2`$. Then $`F`$ has at most eight distinct roots in $`(0,1)`$.

The parameters in this subsection are local support coordinates. The shared endpoint operator is (15).

For $`f_s=\lambda_{s-w}m_s`$, define its cubic core by

```math
\rho\mathcal Lf_s=m_s C_s,\qquad \deg C_s\leq3.
```

If $`T_1=1-k\theta`$ and $`T_2=1-k(1-\theta)`$, direct differentiation gives

```math
C_s(0)=(s_1-w_1)s_1(s_1-T_1),\qquad
C_s(1)=-(s_2-w_2)s_2(s_2-T_2).                     \tag{A}
```

##### A single selector.

Let $`r=\max(u,v)`$ and $`\ell=\min(u,v)`$ coordinatewise. Put

```math
\theta=\frac{w_1}{w_1+w_2},\qquad
k_{*} =\min\left\{\frac{1-r_1}{\theta},
\frac{1-r_2}{1-\theta}\right\}.
\tag{B}
```

First consider $`k_{*}\leq1`$ and choose $`k=k_{*}`$. Then $`T_i\geq r_i`$ for both coordinates, with equality in at least one coordinate. Consequently the higher core $`C_r`$ has a factor $`x`$ or $`1-x`$. The lower core has the strictly positive endpoints

```math
C_\ell(0)>0,\qquad C_\ell(1)>0,                   \tag{C}
```

since $`\ell_1<w_1`$, $`\ell_2>w_2`$ and $`\ell_i<r_i\leq T_i`$.

The first beta annihilation gives the exact identity

```math
G=(D-\lambda_w)F=-\lambda_w+A f_u-B f_v.
```

Since $`\mathcal L\lambda_w=0`$, its operator residual is

```math
R=\rho\mathcal LG=A m_u C_u-Bm_v C_v,
\qquad Z(F)\leq Z(R)+3.                          \tag{D}
```

Absorb the endpoint factor of the higher core into its beta exponent. The residual becomes a beta-weighted quadratic plus a beta-weighted cubic, and so has at most seven distinct roots. Crucially, the lower beta monomial dominates at *both* endpoints, even after an exponent of the higher beta monomial has been increased by one. By (C), $`R`$ therefore has the same sign at both endpoints: positive if $`\ell=u`$, negative if $`\ell=v`$. For generic parameters and coefficients its roots are simple, hence there are at most six. Equation (D) gives at most nine original roots. Their positive original endpoint signs reduce this to eight. If $`R`$ vanishes identically, $`G`$ lies in the disconjugate kernel and has at most one root unless it vanishes identically; integrating the first annihilator then gives at most two original roots. That exception therefore also satisfies the theorem.

##### The complementary region uses the same interpolation lemma.

If $`k_{*}>1`$, (B) gives

```math
r_1<1-\theta,\qquad r_2<\theta.
```

In particular $`0<u_1,u_2<1`$. No information about the modes of $`u`$ or $`v`$, or about a nonvanishing third Wronskian, is needed.

Set

```math
H(p,q)=\lambda_pD\lambda_q-\lambda_qD\lambda_p
+\lambda_p\lambda_q(\lambda_q-\lambda_p),
```



```math
P=H(w-v,u-v),\qquad Q=-H(w-v,-v),\qquad
L=\lambda_{w-v}>0.
```

The negative-pair reduction, whose divisors do not vanish, is

```math
D\left(\frac{D(F/m_v)}{D(m_w/m_v)}\right)
=\frac{m_{-w}}{L^2}\,[A m_uP-Q].                 \tag{E}
```

Writing $`u=(a,b),v=(c,d),w=(e,f)`$, the cubic endpoints are

```math
P(0)=-(e-c)(e-a)(a-c),\qquad
P(1)=(d-f)(b-f)(b-d).
```

They have opposite signs because $`(a-c)(b-d)>0`$. Thus $`P`$ is nonzero and has an interior root.

The interior-root interpolation lemma (Lemma 3) therefore applies: if $`P,Q`$ have degree at most three, $`P`$ has an interior root, and $`0<a,b<1`$, then $`Q=A x^a(1-x)^bP`$ has at most seven distinct solutions. Two Rolle steps in (E) give nine original roots, and positive endpoint parity gives eight in the generic case. The lemma is the same for both comparable orientations; its proof uses no source-specific cofactor order.

##### Distinct roots and seams.

The generic endpoint argument transfers to arbitrary distinct original roots as follows. For a finite set of distinct roots, a small change of the positive constant coefficient can be chosen to produce at least as many nearby simple crossings: odd-order roots each preserve one crossing, while one of the two shift signs splits at least half of the even-order roots into two. Avoiding the countably many critical values makes all crossings simple. Next perturb the supports and the other coefficients, preserving these closed interior intervals whose endpoint values have opposite signs, to generic parameters in the proved strict domain. The signs of the coefficients and endpoint limits remain fixed. Thus a function with more than eight distinct roots would give a generic function with more than eight simple roots, a contradiction. This also covers $`k_{*}=1`$, equal selector branches, and nonidentity finite support limits of the stated domain.

The exceptional parameter sets in both cancellation branches have empty interior. The source proof [COMP-ATOM] gives exact examples in which the lower cubic and the reduced higher quadratic have neither repeated roots nor common roots. Their discriminants and resultants therefore define nonzero polynomials in the parameters. Outside their zero sets, a regular choice of the coefficient ratio gives simple residual roots.

[COMP-ATOM] in the appendix gives the full source calculation and the two examples just mentioned.

### Global least supports

##### The two previously proved inputs.

We use the preliminary bound ten, the equality implications of the derivative reductions, the signed cofactor endpoint formulas and the component count proved above. We also need the following previously proved global-least result [GL], for $`\alpha,\beta,\gamma>0`$:

```math
1+\alpha m_u-\beta m_v-\gamma m_w,\qquad
u,v,w\ge0,\quad v\le w,
\qquad Z\le8.                                      \tag{GL-c}
```

Its detailed proof, including the two comparable-negative subcases, remains a needed input [GL]. We also use the analytic curvature lemma [DISJOINT] in the middle cell below. Lemma 3A handles the four entries labeled Cross. None of these inputs uses F2, F3, F4 or the full two-versus-two theorem, so this step is not circular.

**Lemma 3B (extended global-least theorem).** Let $`\alpha,\beta,\gamma>0`$ and

```math
F=1+\alpha m_u-\beta m_v-\gamma m_w\not\equiv0,
\qquad u,v,w\ge0.
```

Then $`Z(F)\le8`$, with no comparability assumption on $`v,w`$. Equivalently, a two-positive, two-negative four-beta sum with a globally least active support has at most eight distinct roots.

##### Proof.

First use strict positive coordinates, distinct coordinate orders, simple original roots, and the same generic cofactor hypotheses used in the equality argument in this document. Comparable negative supports are covered by (GL_c), after interchanging them if necessary. Otherwise arrange $`v_1<w_1`$ and $`w_2<v_2`$. The positive support $`u`$ has just nine position cells:

```math
\begin{array}{c|ccc}
&u_2<w_2&w_2<u_2<v_2&v_2<u_2\\\hline
u_1<v_1&\text{corner}&\text{Cross}&\text{corner}\\
v_1<u_1<w_1&\text{Cross (reflected)}&\text{Disjoint}&\text{Cross}\\
w_1<u_1&\text{corner}&\text{Cross (reflected)}&\text{corner}
\end{array}
```

The Cross entries have the positive support comparable to one negative support, both lying northwest of the other, either directly or after physical reflection and relabeling the negative pair. The new theorem gives eight throughout those four cells. The center is exactly the already proved disjoint-curvature domain.

All four corners have one common proof. Label $`0`$ the constant, $`1`$ the positive support $`u`$, $`2`$ the negative support $`v`$, and $`3`$ the negative support $`w`$. Here $`u_1`$ lies outside $`[v_1,w_1]`$ and $`u_2`$ lies outside $`[w_2,v_2]`$. The signed cofactor endpoint formulas give

```math
\begin{aligned}
e_0(0)&=(v_1-u_1)(w_1-u_1)(w_1-v_1)>0,\\
e_0(1)&=-(v_2-u_2)(w_2-u_2)(w_2-v_2)>0,\\
e_1(0)&=-v_1w_1(w_1-v_1)<0,\\
e_1(1)&=v_2w_2(w_2-v_2)<0.
\end{aligned}
```

The same formulas give

```math
K(0)=u_1v_1w_1 e_0(0)>0,\qquad
K(1)=-u_2v_2w_2 e_0(1)<0.
```

Use the monotone negative-pair anchor $`2,3`$, with complementary pair $`0,1`$. Each complementary cofactor has even endpoint parity and at most two physical roots; the coefficient-weighted pair product is negative at both ends. Thus the useful set has at most two components. The sextic $`K`$, with opposite endpoint signs, has at most five physical roots. The corresponding residual therefore has at most $`2+5=7`$ roots, whereas equality in the ten-root counting bounds would require eight. Ten original roots are impossible. The positive original endpoint signs and the preliminary ceiling ten now give at most eight simple roots in these cells too.

Every strict generic cell is proved. Apply Lemma 1’s transfer for distinct roots with sign vector $`(+,+,-,-)`$ and exponent set $`u,v,w\in(0,\infty)^2`$, initially allowing the constant coefficient to vary independently over the positive numbers and then renormalizing it to one. This includes finite coordinate ties, vanishing exponent coordinates, repeated supports, and multiple original roots, excluding identities. Division by a globally least beta monomial and, if needed, global coefficient-sign reversal give the equivalent formulation.

[GL-ALL] gives the standalone proof. Its comparable-negative branch uses the full proof of [GL]; its center retains [DISJOINT]. Lemma 3A supplies the four cross cells.

### The F2 and F4 exponent orders

The F2 normal form is

```math
F=A_0+A_1x^a(1-x)^{-b}-B_0x^e(1-x)^{-f}-B_1x^c(1-x)^d,
\quad0<e<a<c,\quad0<f<b,\quad d>0.                       \tag{16}
```

All four magnitudes are positive. The following height argument excludes ten roots for this entire domain. Here is its coordinate dictionary, so that its polynomial and interval claims have definite meanings. Set $`\Delta=af-be`$ and $`J_0=a(d+f)+b(c-e)>0`$. The common height argument below covers $`\Delta\le0`$. For the remaining $`\Delta>0`$ coordinate dictionary, define

```math
\alpha=(bc+ad)/J_0,\qquad \beta=\Delta/J_0,\qquad
\mu=(cf+de)/J_0.
```

These parameters satisfy $`\alpha+\beta=1`$ and $`0<\beta<\mu<\alpha<1`$. Put $`m_1=x^a(1-x)^{-b}`$, $`m_2=x^e(1-x)^{-f}`$, $`m_3=x^c(1-x)^d`$, and

```math
t=\frac{x}{1-x},\quad z=\log m_1,\quad
y=\frac{e-c+(d+f)t}{a+bt},\quad
l=\frac{e-c}{a},\quad r=\frac{d+f}{b}.
```

This fractional linear change sends $`(0,1)`$ to $`(l,r)`$ monotonically. Its speed with respect to $`z`$ is the polynomial

```math
q(y)=\frac{dy}{dz}
=\frac{(ay+c-e)(d+f-by)(c-e+d+f+(a-b)y)}{J_0^2}>0.
```

Define $`h=\mu-\alpha y`$, $`k=\mu+\beta y`$, and

```math
p=q+\frac{h(1-h)}\alpha,\qquad
g=q-\frac{k(1-k)}\beta,\qquad
s^2=\frac{\mu(1-\mu)}{\alpha\beta}.
```

Thus $`p,g`$ are polynomials in $`y`$ of degree at most three, and $`p-g=s^2-y^2`$. In this paragraph $`p,g,q`$ denote functions of $`y`$; they are unrelated to the exponent vectors used to define $`H(p,q;x)`$. The actual residual is, up to a nonvanishing factor,

```math
B_1m_3\alpha p-B_0m_2\beta g.
```

On $`pg>0`$ its zeros are exactly

```math
\Phi=\log|g/p|+\eta=\log\frac{\alpha B_1}{\beta B_0},
\qquad \eta=\log(m_2/m_3),\qquad \eta'=y/q.
```

Here and in the next equation primes mean ordinary differentiation with respect to $`y`$:

```math
\Phi'=-\frac{\mathcal C}{qpg},\qquad
\mathcal C=q(p'g-pg')-ypg,
\quad\deg_y\mathcal C\le6.                             \tag{17}
```

The coefficient level is fixed on every component. The four overlapping *band orders* ABBA, BAAB, ABAB, BABA list in increasing $`y`$ order the two physical zeros of $`p`$ (letter A) and the two physical zeros of $`g`$ (letter B). For example, ABAB means $`p_1<g_1<p_2<g_2`$. Overlap is proved below. These names record root order; all arguments use the actual source cubics: the displayed shared-support formulas are retained.

The proof uses one common-height theorem and one comparison involving the exterior roots of the original polynomials [F2-HEIGHT]. Only the two monotone anchors $`01,02`$ are needed. Ten generic original roots require eight residual roots for each. Their numerator and pole cores have degree at most three and equal endpoint signs, hence at most two physical roots each. The normalized four-column determinant has at most five roots in the interval. Eight positive-level intersections therefore force two roots of both cores, three positive components, and all five critical points useful for that same inverse phase.

If its two intervals between the two roots were disjoint, the inverse phase would be negative between its numerator roots, smooth there, and zero at both ends. An attained negative minimum gives a nonuseful critical point, a contradiction. Thus the two bands overlap, leaving just RHHR, HRRH, RHRH or HRHR. No full eight-event cofactor word is required, and the fourth cofactor and third anchor are unused.

##### One height comparison for a ratio with two denominator roots.

Let $`w>0`$ have concave logarithm on an interval containing the four distinct events $`r_1<r_2`$, $`h_1<h_2`$, and put

```math
Q_{*}(x)=\frac{(x-r_1)(x-r_2)}{(x-h_1)(x-h_2)},\qquad
\Psi(x)=w(x)Q_{*}(x).
```

For any of the four overlapping band orders just listed, if there are at most five positive-domain critical points, every fixed positive level has at most seven intersections. Indeed, write $`Q_{*}=1+a_1/(x-h_1)+a_2/(x-h_2)`$. The single identity

```math
Q_{*}(y)-Q_{*}(x)-Q_{*}'(x)(y-x)
=(y-x)^2\sum_{j=1}^2\frac{a_j}{(y-h_j)(x-h_j)^2}                 \tag{F2-H}
```

shows that, at a positive critical point $`x`$ of $`\Psi`$, a negative right-hand side implies $`\Psi(y)<\Psi(x)`$. To see this, apply $`\log t\le t-1`$ to $`Q_{*}(y)/Q_{*}(x)`$, and use the tangent bound for $`\log w`$; the linear terms cancel at $`x`$.

In RHRH both residues are positive: choose the left positive component. In HRHR both are negative: choose the right positive component. In HRRH their signs are $`(-,+)`$: choose the central numerator band. In each case (F2-H) is negative for every point of that component and every critical point on either other positive component. The chosen component has strictly concave $`\log Q_{*}`$, by pairing each numerator root with a farther pole, so it has at most two level intersections. If a level meets it, every critical height on either other component is greater than that level. Each such component has an infinite pole endpoint, hence at most one intersection. The total is then at most four. If the level misses the chosen component, componentwise Rolle gives at most $`5+2=7`$.

For RHHR, $`r_1<h_1<h_2<r_2`$, and $`a_1>0>a_2`$. The central positive component has an attained global minimum $`x`$, since its height tends to infinity at both poles. Set

```math
A_1=\frac{a_1}{(x-h_1)^2},\qquad
A_2=\frac{-a_2}{(x-h_2)^2},\qquad Q_{*}'(x)=A_2-A_1.
```

If $`A_1\ge A_2`$, the sum in (F2-H) is negative throughout the left positive component; if $`A_2\ge A_1`$, it is negative throughout the right one. That entire selected component lies strictly below the central minimum. Thus no level occupies all three components, again giving $`5+2=7`$.

##### Bind the theorem to the original F2 levels.

Here $`D=x(1-x)\partial_x`$, $`\lambda_i=D\log m_i`$, $`P_i=\lambda_i^2+D\lambda_i`$, and

```math
E_i=(-1)^i\det(1,\lambda,P)_{\widehat i},\qquad
\mathcal K=\det(\lambda_i,P_i,
\lambda_i^3+3\lambda_iD\lambda_i+D^2\lambda_i)_{i=1,2,3}.
```

These are the actual signed cofactors of $`1,m_1,m_2,m_3`$; $`\lambda_0=P_0=0`$. Anchors $`01`$ and $`02`$ are globally monotone. Their positive inverse residual heights are exactly

```math
\Psi_2=\frac{m_3E_2}{m_2E_3}=\frac{B_0}{B_1},\qquad
\Psi_1=-\frac{m_3E_1}{m_1E_3}=\frac{A_1}{B_1}.
```

After clearing positive monomial and denominator factors, their derivative cores are $`-\lambda_1\mathcal K`$ and $`-\lambda_2\mathcal K`$. Both score factors are positive physically. Moreover

```math
\deg\mathcal K\le6,\quad
\mathcal K(0)=-ace(a-e)(c-a)(c-e)<0,\quad
\mathcal K(1)=bdf(b-f)(b+d)(d+f)>0.
```

There are therefore at most five physical critical points, counting multiplicity. Every level above is one fixed ratio of the original coefficients on all components.

For $`\Delta\le0`$, $`\lambda_1>\lambda_2>0`$ and the source identity

```math
E_3=-[\lambda_1\lambda_2(\lambda_2-\lambda_1)+x(1-x)\Delta]>0.
```

The positive set of the cubic $`E_2`$, positive at both ends, has at most two components. The same $`5+2=7`$ bound excludes eight residual roots directly. This covers the whole region $`\Delta\le0`$. For $`\Delta>0`$ and $`a=b`$, $`\lambda_1=a`$ is constant, and $`E_2,E_3`$ are quadratic. Saturation forces two physical roots each; their inverse height has the strictly log-concave prefactor $`Cx^{c-e}(1-x)^{d+f}`$, with no exterior factor. The overlap and common-height arguments apply directly.

Reflect and divide by $`m_1`$, if needed, to arrange $`a>b`$; the transformed support is $`(b,a,b+d,c-a,b-f,a-e)`$, still of the form (16). Put

```math
\xi=-\frac{c-e+d+f}{a-b}<l.
```

The centered cubics have negative leading coefficient, are negative at both physical endpoints, and hence have unused roots $`p_0,g_0<l`$. Since $`h(\xi)>h(l)=c/a>1`$, $`p(\xi)<0`$, giving $`p_0<\xi`$. The inverse map

```math
x=\frac{ay+c-e}{(a-b)y+c-e+d+f}
```

is increasing on each side of its pole $`\xi`$. Thus the unused root of $`E_2=-\lambda_1^3\alpha p`$ is an original right exterior root $`\eta_2>1`$.

In the ordered sector $`p_0<g_0`$, there are two source possibilities. If $`g_0<\xi`$, the original $`E_3`$ exterior root is $`\gamma>\eta_2`$. Use anchor $`01`$, whose positive prefactor after division by the physical-root factors is

```math
w_2=C_2x^{c-e}(1-x)^{d+f}\frac{x-\eta_2}{x-\gamma},\qquad C_2>0.
```

Its logarithm is strictly concave: both beta powers contribute negatively, and $`1<\eta_2<\gamma`$ makes the numerator exterior contribution more negative than the pole contribution. If $`\xi<g_0<l`$, then $`\gamma<0`$. The original $`E_1`$ exterior root $`\eta_1`$ is also negative. At $`\gamma`$, the source identity

```math
E_3=-[\lambda_1\lambda_2(\lambda_2-\lambda_1)+x(1-x)\Delta]
```

forces $`\lambda_2(\gamma)<0`$. Since $`E_2(\gamma)>0`$, the cofactor null identity gives $`E_1(\gamma)=-\lambda_2(\gamma)E_2(\gamma)/\lambda_1(\gamma)>0`$. Its sign interval therefore implies $`\gamma<\eta_1<0`$. Use anchor $`02`$, with

```math
w_1=C_1x^{c-a}(1-x)^{d+b}\frac{x-\eta_1}{x-\gamma},\qquad C_1>0.
```

The closer numerator exterior root again gives strict log concavity. The common two-pole theorem applies to every ordered-sector event word, excluding the required eight residual roots.

##### One deflated height for the reversed sector.

If $`g_0<p_0`$, source coupling forces $`-s<g_0<p_0<\xi<l`$, and among the four words only ABBA or ABAB remains. In either order, deflate $`g_2,p_2`$ from the phase and put

```math
H=\eta+\log\left|\frac{g/(y-g_2)}{p/(y-p_2)}\right|.
```

Put $`\kappa=ab(a-b)/J_0^2>0`$, so $`q=\kappa(y-\xi)(y-l)(r-y)`$. Write $`\delta=p_2-g_2`$, and $`E=1+\kappa\delta`$. The root-sum identity gives $`g_1-p_1=(p_0-g_0)+E/\kappa`$, hence

```math
H'>
\frac{E}{\kappa(y-g_1)(y-p_1)}+\frac yq
\quad(g_1<y<r).
```

If $`\delta>0`$, then $`E>1`$; for $`y<0`$ positivity follows termwise from

```math
qE/\kappa
=E(y-\xi)(y-l)(r-y)
>(-y)(y-g_1)(y-p_1).
```

For $`\delta<0`$, the source coupling instead gives $`G=g_2>p_2>s>0`$. Set $`u=-p_0`$, $`v=-p_1`$. Evaluation at $`G`$ gives the compact identity

```math
E=\frac{s^2+uv+G(u+v)}{(G+u)(G+v)}>0.
```

For $`y=-w\in(g_1,0)`$, $`u>v>w>0`$, and

```math
E(G+w)-w
=\frac{G(s^2+uv)+G^2(u+v-w)+ws^2}{(G+u)(G+v)}>0.
```

Since $`r>G`$, this proves $`E(r-y)>-y`$, supplying the same comparison of three factors. For $`y\ge0`$, positivity is immediate. Thus $`H'>0`$ throughout $`(g_1,r)`$ in both orders.

In ABBA, the deflated singular logarithm adds a positive cross-ratio when passing from the middle to the right component. Every right height exceeds every middle height, so a common level occupies at most two components. In ABAB, restore the adjacent factor:

```math
\Phi'=H'+\frac{g_2-p_2}{(y-g_2)(y-p_2)}>0
```

on both the middle and right components. On the left component $`L=(\log|g/p|)'`$ is strictly increasing, as is $`q/(-y)`$. Where $`L\le0`$ there is no stationary phase point; where $`L>0`$, the product $`(q/(-y))L`$ increases from zero to infinity. There is exactly one left stationary point and at most four residual roots in total. This removes the separate negative/nonnegative/switch interval comparisons from the old reversed ABAB proof.

This exhausts the generic F2 saturation domain. Two applications of Rolle's theorem, with divisors that do not vanish, give at most nine original roots; the positive endpoint signs give eight for simple roots. Lemma 1(b), with the exponent domain in (16), the displayed coefficient signs and $`N_0=8`$, supplies the full distinct-root bound and finite closure, including the $`e=f`$ cofactor degree seam. The proof uses the two displayed derivative reductions, the five-critical-point bound and the left-interval calculation. No additional ordering of all the cofactor roots is needed.

For F4, the normal form is

```math
F=A_0+A_1x^a(1-x)^{-b}-B_0x^e(1-x)^{-f}-B_1x^c(1-x)^{-d},
\qquad0<e<a<c,\quad0<f<d<b. \tag{18}
```

All four magnitudes are positive. Here the endpoint signs of the signed cofactors are $`(-,-,+,+)`$ at zero and $`(+,-,-,+)`$ at one. Thus $`e_1,e_3`$ have at most two physical roots and $`e_0,e_2`$ at most three. The sextic has opposite endpoint signs and at most five physical contacts. Use just anchors $`02,03,12`$, whose complementary pairs are $`13,12,03`$. Each useful set has at most three components. Ten original roots would force eight residual roots for each anchor, so Lemma 2A with $`d=5`$ forces equality: the cofactor counts are $`(3,2,3,2)`$ and all five contacts are useful for each of the three complementary pairs. Their graph $`2`$–$`1`$–$`3`$–$`0`$ is connected, proving joint usefulness. No cofactor-count allocation is required for this implication.

For F4, the root-placement lemma [F4-TWO] needs only two of the four cofactor cubics. Its change of variable is

```math
J=e(b-d)+f(c-a),\quad
y=\frac{a-c+(b-d)t}{e+ft},\quad t=\frac{x}{1-x},
\qquad \mu=\frac{bc-ad}{J},\quad\eta=\frac{cf-de}{J}.
```

At saturation $`\mu>1`$, $`\eta>1`$. Put $`m=\mu-1`$, $`s^2=\mu m/[\eta(\eta-1)]`$, and use the source flow $`q=dy/d\log m_2>0`$. The retained parameter inequalities proved in the source include $`f>e`$ and

```math
q=\kappa(y-l)(r-y)(\xi-y),\qquad
\kappa>0,\quad l<0<r<\xi<m/\eta.
```

These inequalities follow from the hypothetical ten roots as well as from the source identities. The exponent ordering alone does not imply them. The two cubics needed for the ordering argument are

```math
g=q-\frac{[\mu-(\eta-1)y][\mu-1-(\eta-1)y]}{\eta-1},
\qquad
\mathscr D=mq+y[\mu-1-\eta y][\mu-1-(\eta-1)y].
```

They are nonzero multiples of the original $`e_3,e_0`$, respectively. Write their negative physical roots as $`g_1<g_2<0`$ and $`d_1<d_2<d_3<0`$. The other two cofactor cubics enter only through the source identities proving, for $`y<0`$,

```math
\begin{array}{ll}
-s<y<0:&\text{joint usefulness}\iff\mathscr D<0\ \text{or}\ g>0,\\
y<-s:&\text{joint usefulness}\iff g<0\ \text{or}\ \mathscr D>0.
\end{array}
```

Coefficient comparison with the positive physical flow gives $`\sigma_2<\zeta^2<s^2`$, where $`\sigma_2`$ is the sum of pairwise products of $`-d_i`$ and $`\zeta^2=m^2/[\eta(\eta-1)]`$. In particular $`d_2,d_3>-s`$. This short inequality also supplies the strict positivity of the remaining coefficients of $`q`$; the last interval is handled analytically below.

There are only three cases. If $`g_1<g_2<-s`$, source evaluation at the two $`g`$ roots forces a $`K`$ root in their intervening interval outside the common allowed set, contradicting the equality requirement that all five critical points lie on the common allowed intervals. If $`g_1<-s<g_2`$, the switch identities force $`g_1<d_1<-s<g_2<d_2<d_3`$, and the joint intervals have contact bounds $`(0,0,1)`$. If $`-s<g_1<g_2`$, then $`d_1>-s`$ and $`d_1<g_1`$; the joint intervals are $`(l,d_1),(g_1,g_2),(d_2,d_3)`$, where $`l`$ is the physical left endpoint. The last two may occur in either order. The interval proofs below give one contact in each, totaling three. Both totals are below the required five.

The central interval $`(g_1,g_2)`$ has a direct analytic one-contact proof [F4-CENTRAL], replacing its coefficient certificate. The source root bounds give $`-s<g_1<g_2<0<g_3<s`$, and $`g=\kappa(y-g_1)(y-g_2)(y-g_3)`$, $`\kappa>0`$. Put $`\Delta=s^2-y^2`$, $`f_{*}=g+\Delta`$, $`n=\eta-1>0`$, $`b_{*}=2\mu-1>0`$. The source flow is exactly

```math
q=g+ny^2-b_{*}y+(n+1)s^2,
```

and the contact polynomial is

```math
\mathcal C=q(f_{*}'g-f_{*}g')-yf_{*}g,
\qquad K/\lambda_2^6=-\eta(\eta-1)\mathcal C.
```

On this interval $`g,\Delta,f_{*},q>0`$. Write

```math
\rho=g/\Delta,\quad L=\log\rho,\quad p=-y\in(0,s),\quad
M=\frac{p(1+\rho)}q,\quad H=L'-M.
```

Then $`\mathcal C=-q\Delta gH`$. Pairing the two $`\Delta`$ poles against the nearest $`g`$ poles gives

```math
a_{*}=\frac1{y-g_1}-\frac1{y+s}>0,\quad
b_\circ=\frac1{g_3-y}-\frac1{s-y}>0,\quad
c_{*}=\frac1{g_2-y}>\frac1p,
```



```math
L'=a_{*}-b_\circ-c_{*},\qquad
L''=-a_{*}^2-\frac{2a_{*}}{y+s}
-b_\circ^2-\frac{2b_\circ}{s-y}-c_{*}^2.
```

At a zero of $`H`$, $`a_{*}=M+b_\circ+c_{*}>M+1/p`$, so

```math
L''<-\left(M+\frac1p\right)^2
-\frac{2(M+1/p)}{s-p}-\frac1{p^2}.
\tag{F4-C1}
```

At the same point $`\rho'=\rho M`$. Set $`Z=np^2+b_{*}p+(n+1)s^2`$, so $`q=\Delta\rho+Z`$. Direct differentiation, with $`p'=-1`$, gives

```math
M'=-\frac{(1+\rho)[\rho(s^2+p^2)+n\Delta+s^2]}{q^2}
+\frac{p^2\rho(1+\rho)(Z-\Delta)}{q^3}.
```

The last term is positive because $`Z-\Delta=(n+1)p^2+b_{*}p+ns^2>0`$. Consequently

```math
\begin{split}
M'+\left(M+\frac1p\right)^2
+\frac{2(M+1/p)}{s-p}+\frac1{p^2}
>{}&\frac{2s}{p^2(s-p)}\\
&+\frac{1+\rho}{q^2}
\left[\frac{2sq}{s-p}-\rho s^2-(n+1)\Delta\right]>0.
\end{split}
\tag{F4-C2}
```

The bracket is positive by the exact decomposition

```math
\rho s(s+2p)
+(n+1)\left[\frac{2s^3}{s-p}-\Delta\right]
+\frac{2s(np^2+b_{*}p)}{s-p},
```

since $`2s^3/(s-p)>2s^2>\Delta`$. Equations (F4-C1)–(F4-C2) give $`H'<0`$ at every zero. At the two $`g`$ endpoints, $`L'\to+\infty,-\infty`$, respectively, while $`\rho\to0`$ and $`M`$ stays finite. Hence $`H`$ has exactly one zero, a strict downward crossing. The contact is therefore unique and simple. This proof uses no other cofactor-root placement or coefficient ratio.

The last dual-root interval $`(d_2,d_3)`$ also has an analytic one-contact proof [F4-LASTD]. Write $`d_i=-r_i`$, so $`r_1>r_2>r_3>0`$; the source bounds already proved give $`r_2<s`$. Its cubic coefficient is $`m\kappa+\eta(\eta-1)>0`$. Put $`p=-y\in(r_3,r_2)`$, $`n=\eta-1`$, and

```math
u=-\mathscr D=\kappa_D(r_1-p)(r_2-p)(p-r_3)>0,
\qquad\Delta=s^2-p^2>0,
\qquad\rho=\frac{s^2u}{mp\Delta}.
```

For $`C=\mu q+y[\mu-\eta y][\mu-(\eta-1)y]`$, the source identities give

```math
\frac{C}{\mathscr D}=\frac\mu m\frac{1+\rho}{\rho},\qquad
q(C'_y\mathscr D-C\mathscr D'_y)-C\mathscr D=-yK_{\rm can},
\quad K_{\rm can}=K/\lambda_2^6.
```

Therefore, with $`L=\log\rho`$, $`M=(1+\rho)/q`$,

```math
K_{\rm can}=\frac{C\mathscr Dq}{p(1+\rho)}H,
\qquad H=L'_p-M.
```

The prefactor is positive on this interval.

Pair the nearest numerator poles against 0 and $`s`$:

```math
a_{*} =\frac1{p-r_3}-\frac1p>0,\quad
b_{*} =\frac1{r_2-p}-\frac1{s-p}>0,\quad
c_{*} =\frac1{r_1-p}>0,\quad e_{*} =\frac1{s+p}>0.
```

Exactly

```math
L'=a_{*}-b_{*}-c_{*}-e_{*},\qquad
L''=-a_{*}^2-\frac{2a_{*}}p-b_{*}^2-\frac{2b_{*}}{s-p}-c_{*}^2+e_{*}^2.
```

At a zero of $`H`$, $`a_{*}=M+b_{*}+c_{*}+e_{*}>M+e_{*}`$, hence

```math
L''<-(M+e_{*})^2-\frac{2(M+e_{*})}p+e_{*}^2
<-M^2-\frac{2M}p.
\tag{F4-L1}
```

This pays the unfavorable $`-s`$ pole even when $`r_1>s`$.

The source equation $`\mathscr D=mq-p(m+\eta p)(m+np)=-u`$ gives

```math
q=p\left[m+(2\eta-1)p+\frac{(m+1)p^2}{s^2}
-\frac{\rho\Delta}{s^2}\right].
```

At the same contact $`\rho'=\rho M`$. Differentiating $`M`$ with this actual flow yields the positive identity

```math
M'+M^2+\frac{2M}p
=\frac{(1+\rho)(m+1+\rho)\Delta}{s^2q^2}
+\frac{\rho(1+\rho)^2p\Delta}{s^2q^3}>0.
\tag{F4-L2}
```

Equations (F4-L1)–(F4-L2) give $`H'<0`$ at every zero. At the two endpoints $`L'\to+\infty,-\infty`$, respectively, while $`\rho\to0`$ and $`M`$ stays finite. Thus there is exactly one contact, and it is simple. No positive-slack coefficient table or separate placement of the first $`\mathscr D`$ root is used.

For the next argument, write $`D=\mathscr D`$. Primes in the reciprocal lemma denote $`z`$ derivatives.

##### Initial intervals: a reciprocal cubic ratio [F4-INITIAL].

Let $`r_i,t_i>0`$, $`s>0`$, $`\alpha>s^{-2}`$, and

```math
P(z)=\prod_{i=1}^3(1-r_i z),\qquad
N(z)=\alpha P(z)+z^2-s^{-2}
=(\alpha-s^{-2})\prod_{i=1}^3(1-t_i z).
```

On any positive interval $`z>0`$ where all six factors are positive, set $`\Lambda=(\log(N/P))'`$. Then $`\Lambda'>0`$ wherever $`\Lambda\ge0`$.

*Proof.* Put $`A=-P'/P=\sum_i r_i/(1-r_i z)>0`$ and $`V=z^2-s^{-2}`$. Then $`N>0`$, $`N'<0`$, $`A'<A^2`$, and

```math
\Lambda=\frac BN,\qquad B=2z+VA.
```

If $`V\ge0`$, then $`B'=2+2zA+VA'>0`$. If $`V<0`$ and $`B\ge0`$, use

```math
B'=2+BA+V(A'-A^2)>2.
```

Hence $`\Lambda'=B'/N-BN'/N^2>0`$ wherever $`\Lambda\ge0`$. ◻

For the actual F4 source, write $`m=\mu-1`$, $`n=\eta-1`$, $`s^2=\mu m/(\eta n)`$, and $`D/m=\alpha\prod_i(y+r_i)`$, where $`\alpha=\kappa+\eta n/m`$. Thus $`\alpha s^2=\kappa s^2+\mu>1`$, as required by the reciprocal lemma. The inequalities for the change of variable give $`y<r<\xi<m/\eta`$, hence $`\mu-\eta y>1`$ and $`\mu-ny>1`$ on the physical interval. In particular $`C,D>0`$ for $`y\ge0`$. Saturation supplies three physical roots of both $`C`$ and $`D`$, all negative. Thus $`r_i>0`$ and, writing the $`C`$ roots as $`-t_i`$, also $`t_i>0`$. The exact source identity gives, for $`p=-y`$ and $`z=1/p`$,

```math
\frac CD=\frac\mu{m\alpha}\frac{N(z)}{P(z)}.
```

The source coefficient comparison gives

```math
q(-p)=-\kappa p^3+(\alpha\sigma_1+2\eta-1)p^2
+(m-\alpha\sigma_2)p+\alpha\sigma_3,
```

with $`m-\alpha\sigma_2>0`$: indeed, $`\kappa(L-r-\xi)=\alpha\sigma_1+2\eta-1>0`$, where $`L=-l`$, and $`m-\alpha\sigma_2=\kappa[L(r+\xi)-r\xi]>0`$. Consequently $`q(-p)/p^2`$ is strictly decreasing.

On either initial joint interval, $`D<0`$ and $`g<0`$. The source identities, with $`k=\mu-ny`$ and $`\Delta=s^2-y^2`$, are

```math
C=\mu g+\eta k\Delta,\qquad
mC=\mu D+\eta n y\Delta.
```

The first gives $`C<0`$ for $`y\le-s`$; the second gives $`C<0`$ for $`-s<y<0`$. Thus $`C,D<0`$ throughout each initial interval, so every one of their physical roots is to the right of that interval. All factors in $`P,N`$ are positive there. Put

```math
G(p)=\frac{q(-p)}{p^2}\Lambda(1/p).
```

The reciprocal lemma and the decreasing positive factor coming from the change of variable show $`G'<0`$ wherever $`G\ge0`$. The dual source contact identity is

```math
K_{\rm can}=-\frac{CD}{y}(G-1).
```

If both physical $`g`$ roots exceed $`-s`$, the initial component is $`(l,d_1)`$. Here $`C(d_1)<0`$, so $`G\to+\infty`$ as $`p\downarrow r_1=-d_1`$. At $`p=L`$, $`G\to0`$ because $`q(l)=0`$ while $`C(l),D(l)<0`$. Thus $`G=1`$ has exactly one simple crossing, and the initial component contains exactly one simple contact.

If the $`g`$ roots straddle $`-s`$, the initial component is $`(l,g_1)`$. At $`g_1<-s`$, one has $`\Delta<0`$, $`g'(g_1)>0`$ and

```math
\mathcal C(g_1)=-q(g_1)\Delta(g_1)g'(g_1)>0,
\qquad K_{\rm can}(g_1)<0.
```

Hence $`G(-g_1)<1`$. Since $`G'<0`$ wherever $`G\ge0`$, no larger $`p`$ can give $`G=1`$. This initial component contains no contact.

In the following middle-interval argument, all displayed primes denote $`y`$ derivatives. The straddling middle interval $`(d_1,g_2)`$ is contact-free by a short pole comparison. Write $`d_i=-r_i`$. The source inequality $`\sigma_2<s^2`$ and $`r_1>s`$ give $`r_2+r_3<s`$. On $`(d_1,-s)`$, put $`T=\eta(\eta-1)y(s^2-y^2)>0`$; then $`mC=\mu\mathscr D+T`$, and for $`z=-y\in(s,r_1)`$,

```math
\left(\log\frac{T}{\mathscr D}\right)'
=-\frac1{r_1-z}-\left[
\frac1{z-s}+\frac1z+\frac1{z+s}
-\frac1{z-r_2}-\frac1{z-r_3}\right]<0.
```

Indeed, for positive $`u,v`$ with $`u+v<z`$, subtracting $`2/z`$ shows

```math
\frac1{z-u}+\frac1{z-v}<\frac1z+\frac1{z-u-v}.
```

The bracket is therefore greater than $`1/(z+s)`$. Thus $`(\log(C/\mathscr D))'<0`$, and the dual contact identity gives $`K<0`$ on $`(d_1,-s)`$. On $`(-s,g_2)`$, the three source roots of $`g`$ give

```math
\left(\log\frac{s^2-y^2}{g}\right)'
=\left(\frac1{y+s}-\frac1{y-g_1}\right)
+\left(\frac1{y-s}-\frac1{y-g_3}\right)
-\frac1{y-g_2}>0.
```

Hence $`(f_{*}/g)'>0`$, so $`\mathcal C=q(f_{*}'g-f_{*}g')-yf_{*}g>0`$ and $`K<0`$. At $`-s`$, $`f_{*}=g>0`$ and $`f_{*}'g-f_{*}g'=2sg>0`$. This proves the middle contact bound zero, without the expanded degree-four numerator of the former argument.

[F4-TWO] in the appendix supplies the parameter inequalities and the three possible root placements used above. The displayed central, last-$`D`$, initial and straddling-middle arguments prove all their required critical-point counts analytically. The original endpoint signs give at most eight simple roots, and Lemma 1 extends this to distinct roots and finite parameter limits.

### The F3 exponent order

Normalize F3 as

```math
F=A_0+A_1x^a(1-x)^{-b}-B_0x^e(1-x)^d-B_1x^c(1-x)^{-f},
\qquad0<e<a<c,\quad0<f<b,\quad d>0. \tag{19}
```

All four coefficient magnitudes are positive. The sums $`(S_0,S_1,S_2,S_3)=(0,a-b,e+d,c-f)`$ have six strict orders. The orders $`0123,1032`$ use [F3-SUM]; $`0132,1023`$ use [F3-ORDER-I]. The other two orders, $`0213,1302`$, are related by physical reflection. It is therefore enough to treat

```math
0<e+d<a-b<c-f. \tag{20}
```

Apply the original-root reductions before splitting into cases according to the order of the cofactor roots. Put $`A=a-e`$, $`B=b+d`$; condition (20) gives $`0<B<A`$. Each of the following conditions gives at most eight distinct zeros of the original function (19), uniformly in its four positive coefficient magnitudes:

```math
A\le4,\qquad B\ge1,\qquad bc-af\ge a-2b.             \tag{F3-CUT}
```

The proofs use an anchor reduction with nonvanishing divisors, a signed interpolation argument and source pair-location or disconjugacy arguments, as printed in [the appendix](appendix.md). These are cuts on the *original* equation; they assert no arbitrary scalar height bound or unqualified sextic contact cap. The remaining saturation argument may therefore assume

```math
A>4,\qquad 0<B<1,\qquad bc-af<a-2b.     \tag{F3-LIVE}
```

The fixed cofactors $`e_0,e_2`$ have exactly one simple physical root. Each variable cofactor $`e_1,e_3`$ has one or three physical roots at strict generic supports. If either has three, the uniform three-root theorem [F3-THREE] gives at most eight original roots. Its proof avoids assigning roots to many individual interval cases; it uses a sum of residues on the outer interval and a common-level count using a degree-five polynomial, as described in [the appendix](appendix.md). This input has no additional bound on the exponent gaps. It remains to treat exactly one simple physical root $`r_i`$ for each cofactor, with these four roots distinct.

**Required joint-contact theorem [F3-JOINT].** For the actual determinant-linked cofactors of (19)–(20), when every cofactor has exactly one simple root in $`(0,1)`$ and (F3-LIVE) holds, the source sextic $`K`$ cannot have six distinct roots in

```math
J=(0,\min_i r_i)\cup(\max_i r_i,1).                       \tag{21}
```

This concerns common useful outer intervals of the actual source. The reductions (F3-CUT) already cover the complementary parameter region.

Here is how this critical-point bound excludes ten original roots. All four anchors $`01,03,12,23`$ are monotone. The signed cofactor endpoint signs are $`(-,-,+,+)`$ at zero and $`(+,+,-,-)`$ at one. Consequently every complementary useful set has exactly two components. Under ten roots, Lemma 2A with $`d=6`$ forces the same six physical contacts into every one of these useful sets. Their complementary edges $`23,12,03,01`$ form a connected cycle, so all four values $`c_i e_i`$ have the same sign at each contact. Because each cofactor changes sign just once, this common-sign condition is precisely membership in $`J`$, contradicting [F3-JOINT].

For clarity, the joint-contact theorem retains the following proof dependencies. A real extra root pair of $`e_1`$ or $`e_3`$ consumes two nonphysical degrees of $`K`$, including double pairs and shared exterior roots. Otherwise both variable pairs are nonreal, and the source null identities permit only the physical cofactor orders $`0231`$ and $`1320`$. These words list cofactor roots, not the exponent sums $`S_i`$.

The [reciprocal-coordinate lemmas](appendix.md#reciprocal-coordinate-height-and-regional-bounds) supply positive height, a sum-of-roots bound on exterior contacts, and shape exclusions under their stated assumptions. They apply only in their specified regions. The two cofactor-order arguments below give the required joint-contact bound throughout the remaining F3 source, including every configuration outside those regions.

In root order $`0231`$, the analytic left bound is exactly one simple contact. If five right contacts existed, all six degrees would be physical and real, counting multiplicity. The original-root cut $`B=b+d<1`$ already gives $`b<1`$ and $`d<1`$. The degree-six polynomial obtained by shifting to the last cofactor root has endpoint coefficients $`q_0>0,q_6<0`$, so five right roots require exactly five Descartes variations, deleting zero coefficients.

Newton’s inequalities give necessary bounds between coefficients of a polynomial whose roots are all real and of the specified sign. They also apply to repeated roots. There are only two coefficient cases. If $`q_2\ge0`$, these inequalities give the strict height inequality with factor $`5/2`$ stated in the appendix. Two uniform identities for the coefficients of the source polynomial force $`q_3>0,q_4>0`$, including $`q_2=0`$. These coefficient signs allow at most three variations, contradicting five right roots. If $`q_2<0`$, five variations force $`q_3>0,q_4<0,q_5>0`$. A third identity for the polynomial coefficients, using no height, forces $`q_4>0`$ and gives the contradiction directly. Thus the right-root multiplicity is at most three; with the retained one-simple-left input the total multiplicity of the critical points on the common allowed intervals is at most four. This proves the local bound on the common allowed intervals. Its hypotheses include the source formulas, the nonreal companion pairs, the left-interval bound and (F3-LIVE).

For the cofactor root order $`1320`$, retain the strict conditions (19)–(20), both variable extra pairs genuinely nonreal, and the original-root reductions (F3-LIVE). The analytic joint-left bound is two, counting multiplicity. Put

```math
G_T=(a-1)d-e(2-b).
```

Only two contact sectors remain:

| Sector    | Source input                                                                                    |
|:----------|:------------------------------------------------------------------------------------------------|
| $`G_T\ge0`$ | Two uniform exclusions involving adjacent coefficients give right cap two; the separate analytic left cap is two. |
| $`G_T\le0`$ | First-two-Newton source cap four; its theorem needs only $`A\ge2`$.                               |

The face $`G_T=0`$ is covered by both proofs. The $`B\ge1`$ sector has already been handled at the original-equation level.

##### Two exclusions involving adjacent coefficients when $`G_T\ge0`$.

At the actual $`E_2`$ root $`x_2`$, use the positive odds coordinate $`t=x/(1-x)`$ and the right coordinate $`w=t/t_2-1`$, $`t_2=x_2/(1-x_2)`$. After positive source normalization, write the actual right-tail sextic as $`\sum_{i=0}^6 c_iw^i`$. Its endpoint coefficients satisfy $`c_0,c_1,c_6<0`$. For the source (19)–(20) with exactly one simple root of each cofactor, in the order $`1320`$,

```math
A\ge4,\quad B<1,\quad G_T\ge0
\quad\Longrightarrow\quad
\text{not }(c_2\ge0\text{ and }c_3\le0).   \tag{AH1}
```

An exact identity writes the relevant degree-six polynomial as a sum of nonnegative products and proves (AH1). Its variable substitution and the signs of all its factors are given in the appendix. With the additional original-cut complement $`bc-af<a-2b`$,

```math
\text{not }(c_3\ge0\text{ and }c_4\le0).   \tag{AH2}
```

A degree-eight identity of the same kind proves (AH2). Neither local coefficient theorem needs a nonreal extra pair. The identities use two cofactor evaluations whose positive signs follow from the root order. The appendix defines their local variables $`F_1,F_3,L,G`$, proves $`F_1(1/2)/(L+G)>0`$ and $`F_3(1)/L>0`$, and gives the exact expansions and the sign of every factor.

Here is a table-free sign proof of their joint consequence. If $`c_3<0`$, (AH1) forces $`c_2<0`$, so a positive block starts only at $`c_4`$ or $`c_5`$. If $`c_3=0`$, the two exclusions force $`c_2<0`$ and $`c_4>0`$; after deleting the zero there is again at most one positive block. If $`c_3>0`$, (AH2) forces $`c_4>0`$; a positive $`c_2`$ extends the same block, and $`c_5`$ can extend or end it. The sequence $`(-,-,c_2,c_3,c_4,c_5,-)`$ therefore has at most two variations. Descartes’ rule of signs bounds positive roots, with multiplicity, by the number of coefficient sign changes after zero coefficients are deleted. It gives multiplicity of roots in the right interval at most two, including repeated roots. Together with the separate left cap, this proves the required joint cap four.

**First-two-Newton source theorem [F3-NEWTON].** For the strict F3 source (19)–(20), with cofactor root order $`1320`$ and both additional root pairs genuinely nonreal,

```math
A\ge2,\qquad G_T\le0
```

imply that the total positive-root multiplicity of the source sextic in odds coordinate is at most four. More precisely, with

```math
t=\frac{x}{1-x},\qquad
\widehat K(t)=(1+t)^6K\!\left(\frac{t}{1+t}\right),
```

the multiplicity of positive roots of $`\widehat K`$ is at most four, equivalently the multiplicity of the roots of $`K`$ in the original interval is at most four. No $`B`$ bound or contact premise is required. The reduction (F3-CUT) for $`A\le4`$ means that this theorem covers every remaining $`G_T\le0`$ source in the present proof. Its broader statement, including $`A=2`$, is unchanged.

Suppose instead that $`\widehat K`$ had six positive roots counting multiplicity. Use the rational change of variables in the [appendix](appendix.md). The letters $`\Delta,Z,M,h,\lambda,\lambda_G,T_G,Q_{GN},D_{3G}`$ in the rest of this paragraph refer to that change of variables. They are different from the local variables of F2 and F4. The normalized coefficients satisfy

```math
H=c_1<0,\quad c_2>0,\quad c_3<0,
\qquad N_1=5H^2-12c_2\ge0,
\quad N_2=8c_2^2-15Hc_3\ge0.
```

The source change of variables, under these precise hypotheses, gives $`\Delta>0`$. If $`Z\le0`$, the compact integer first-Newton identity gives $`N_1<0`$. For $`Z>0`$, put $`m=-M>0`$. If $`0<\Delta\le3`$, a direct evaluation of the one-positive-root first cofactor gives the strict crossing gate $`T_G>0`$. With $`G_T\le0`$, the 297-product positive-generator identity then gives $`c_2\le c_2(\lambda_G)<0`$, contradicting the second coefficient. Thus a hypothetical six-root source must have $`h=\Delta-3>0`$.

In this positive-$`h`$ cone, $`N_1\ge0`$ and $`G_T\le0`$ supply the necessary nonnegative generator $`Q_{GN}`$. Two exact positive-generator identities, with 29 and 283 products, give

```math
D_{3G}>0,\qquad c_3(\lambda_G)-\frac5{54}H^3<0.
```

The first makes $`c_3`$ strictly decreasing for $`\lambda\ge\lambda_G`$, while $`G_T\le0`$ gives precisely that lower bound on the actual scale. Hence $`c_3(\lambda)<5H^3/54`$. The two necessary Newton inequalities give the opposite conclusion through

```math
15H\left(c_3-\frac5{54}H^3\right)
=-N_2-\frac23N_1\left(c_2+\frac5{12}H^2\right).
```

Since $`H<0`$, $`c_2>0`$, $`N_1,N_2\ge0`$, the bracketed gap $`c_3-5H^3/54`$ must be nonnegative. This contradiction excludes six positive odds roots. The negative signs of $`k_0,k_6`$ make positive-root multiplicity even, so the cap is four, including repeated roots. The equality faces $`A=2`$ and $`G_T=0`$ are included by strict products which avoid the weak generators.

The constant positive beta monomial dominates near zero, and the positive beta monomial with exponent $`-b`$ dominates near one because $`b>f`$. Simple original roots therefore have even cardinality. The preliminary ceiling of ten, the contradiction above, the three-root input and the other sum orders give the bound eight at generic strict F3 supports. Lemma 1(b), with the coefficients free within their signs, transfers this to distinct roots and all finite boundary parameters of the domain in (19).

### Conclusion of the two-versus-two sign case

Opposite endpoint signs use the preliminary ceiling and odd parity. Equal signs use the extended global-least theorem or the eight-entry table, followed by F2, F3 or F4. This is exhaustive at strict generic supports. Lemma 1(b), with coefficients free within the prescribed signs, extends the bound nine to distinct original roots, zero coefficients and finite support ties. This proves Theorem 3 from the explicitly retained analytic and exact certificate inputs.

## Three coefficients of one sign and one of the other

After sign reversal and division by the unique term of the other sign, the normal form is

```math
f(x)=1-\sum_{i=1}^3 E_i x^{a_i}(1-x)^{b_i},
\qquad E_i>0,\quad a_i,b_i\in\mathbb R.                         \tag{25}
```

**Theorem 4 (sign-case theorem).** For all $`E_i>0`$ and $`a_i,b_i\in\mathbb R`$, the function $`f`$ in (25) satisfies $`\mathop{Z}(f)\le9`$ whenever $`f\not\equiv0`$.

We use the endpoint and parameter-perturbation lemmas [C31] and [SUPPORT] from the appendix. The following four exponent-sign classes state where each specialized theorem is needed.

### Endpoint reduction and support classes

For the use of Lemma 1, first allow the constant coefficient in (25) to vary over the positive numbers. Equivalently, a constant shift with $`|t|<1/2`$ is returned to the displayed normalization by

```math
\frac{f-t}{1-t}
=1-\sum_{i=1}^3\frac{E_i}{1-t}m_{(a_i,b_i)}.
```

All three coefficients remain positive. Lemma 1(a) therefore turns any proposed counterexample into a function with at least as many simple zeros. Its finite sign brackets permit the original exponent perturbations specified by [C31]; they do not permit independent variation of auxiliary contact heights. A derivative anchor in (25) gives at most eleven roots by the the cubic-polynomial derivative argument with one zero in the divisor. Equal endpoint signs make a hypothetical count of at least ten exactly ten. With opposite endpoint signs the exponent vectors of the two endpoint-dominant terms are strictly coordinatewise incomparable, giving a nonvanishing derivative anchor; the bound improves to ten, and odd parity gives nine.

At an endpoint, a *dominant* term eventually exceeds the other terms in magnitude; a strict coordinate order selects it by the smallest corresponding exponent. A *common-dominant* case has the same negative beta monomial, with support $`(-,-)`$, dominant at both ends. Under ten original simple roots and equal endpoint signs, the source transition lemmas [SUPPORT] give the following four-row partition. Support signs refer to exponents, not coefficients.

| Support class                                                              | Source exclusion                                                                   |
|:---------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
| Three $`(+,+)`$ supports                                                     | Positive-support eight-root theorem [AP-MASTER].                                 |
| Different negative endpoint dominants, with mixed-sign extremes            | Split exponents $`(-,+),(+,+),(+,-)`$; nested, mixed and double-reversed source theorems. |
| Different endpoint dominants, both $`(-,-)`$, with remaining support $`(+,+)`$ | Signed-curvature exclusion [EASY].                                               |
| One common $`(-,-)`$ endpoint dominant                                       | Nonnegative-support height theorem [HEIGHT-MASTER].                              |

This partition follows from the hypothetical ten *original* roots and the endpoint and denominator-root counts. It is a classification under that hypothesis, rather than a classification of arbitrary exponent triples. When the same term dominates at both endpoints, division by that actual term places all the remaining cases under one height theorem.

### One theorem when all exponents are positive

**Positive-support theorem [AP-MASTER].** Let $`L,E_1,E_2,E_3>0`$ and $`a_i,b_i>0`$. If the three supports $`s_i=(a_i,b_i)`$ are affinely independent, then

```math
L-\sum_{i=1}^3E_i x^{a_i}(1-x)^{b_i}
```

has at most eight zeros on $`(0,1)`$, counted with analytic multiplicity. For arbitrary nonnegative coordinates, including collinear or repeated supports, the same bound holds for *distinct* roots of a function that is not identically zero. Thus no ordering of the three first or second coordinates is needed. No case split according to the six possible coordinate orders is required.

##### Proof and the remaining source modules.

Put

```math
G(z)=\log\sum_iE_i e^{s_i\cdot z},\qquad q(z)=e^{z_1}+e^{z_2}.
```

The original roots are the intersections of $`G=\log L`$ and $`q=1`$. Here $`z=(z_1,z_2)=(\log x,\log(1-x))`$. The three exponent points are *affinely independent* when they do not lie on one line. The Hessian, the matrix of second derivatives of $`G`$, is positive definite in that case. Indeed, with

```math
p_i=\frac{E_i e^{s_i\cdot z}}{\sum_j E_j e^{s_j\cdot z}},\qquad \bar s=\sum_i p_i s_i,
```

it is the matrix $`\sum_i p_i(s_i-\bar s)(s_i-\bar s)^T`$, which has a strictly positive value on every nonzero vector. Thus the level curves are strictly convex. Their positive-normal portions are the portions whose outward normal has both coordinates positive. Each actual positive-normal branch is parametrized by its normal $`(x,1-x)`$. The normal-flow calculation in [the appendix](appendix.md) reduces its curvature contacts to a sextic forcing polynomial. Two weighted Rolle steps convert a bound on the zeros of the curvature expression of six into the asserted bound of eight on the original level.

For completeness, the remaining division into cases can be stated without an AP permutation table. Let $`\alpha_i`$ be the **barycentric coordinates of the origin**: the unique real numbers satisfying $`\sum\alpha_i=1`$ and $`\sum\alpha_i s_i=0`$, and set $`\lambda_i=a_i-(a_i+b_i)x`$. With only one positive barycentric, write $`\alpha=(1+u+v,-u,-v)`$ after relabeling, $`u,v\ge0`$. The identity

```math
V_0=\sum_i\alpha_i\lambda_i^2
=-\lambda_1^2-u(\lambda_2-\lambda_1)^2
-v(\lambda_3-\lambda_1)^2
```

makes $`V_0`$ nonvanishing on the interval on the actual level curve where the normal has both coordinates positive. The normal comparison gives at most nine original roots counted with multiplicity; positive endpoint signs make that number even, hence at most eight.

With two positive barycentrics, write

```math
s_2=P s_1+Q s_3,\qquad P,Q>0,
\qquad K_{*}=P+Q-1>0.
```

The projective normal coordinate $`r=-\lambda_1/\lambda_3`$ runs over $`(0,\infty)`$ and

```math
V_0=-\frac{\lambda_3^2}{K_{*}}\,
\bigl(P(P-1)r^2-2PQr+Q(Q-1)\bigr).
```

Its positive change-of-variable factor is the genuinely factored cubic

```math
R(r)=\frac{(d_1+r d_3)(a_1+r a_3)(b_1+r b_3)}
{(a_3b_1-a_1b_3)^2},\qquad d_i=a_i+b_i.
```

All its coefficients are positive and all three roots are negative, counting repeated factors. The exact source curvature lemmas have the following exhaustive scopes:

| Parameters                    | Actual-level curvature argument                                                     |
|:------------------------------|:------------------------------------------------------------------------------------|
| $`P,Q\le1`$                     | The quadratic has no positive zero; use the nonvanishing normal calculation.                                 |
| $`P>1`$, $`0<Q<1`$, or reflection | The quadratic has one positive zero. The factored cubic $`R`$ gives a curvature-root count of at most six, including multiplicity.       |
| $`P>1`$, $`Q=1`$, or reflection   | Treat $`Q=1`$ directly, including its zero at the endpoint. The three interval arguments give a curvature-root count of at most six.  |
| $`P,Q>1`$                       | The quadratic has two positive zeros. Compare the same actual function values across both; the total curvature-root count is at most six. |

The proof mechanisms and precise source locations are given in [the appendix](appendix.md); the case $`Q=1`$ is proved directly, rather than by transferring multiplicities from a neighboring parameter cell. The four cases exhaust the source parameters and require no additional hypothesis on the order of the exponent coordinates or auxiliary roots.

For the closed statement, regularize one common positive level and then perturb the original supports. Around nine hypothetical distinct roots, the better of the two level-shift directions creates at least nine simple roots: if $`o`$ roots have odd order and $`e_+,e_-`$ are the two even types, the retained number is $`o+2\max(e_+,e_-)\ge o+e_++e_-=9`$. Their closed interior intervals whose endpoint values have opposite signs persist under a perturbation to strictly positive affinely independent supports, contradicting the strict theorem. This proves the bound eight for distinct roots on the boundary; it does not preserve every old multiple-root weight.

### Split exponents: curvature, common level and common height

For supports $`(-,+),(+,+),(+,-)`$, label the beta monomials $`h_1,h_2,h_3`$ in that order and put

```math
C_s=b_1-b_2,\qquad \Delta_s=a_3-a_2.
```

The four strict sign combinations now use three source theorems. $`C_s,\Delta_s>0`$ is the nested theorem below; the two mixed combinations are reflections of one source; and $`C_s,\Delta_s<0`$ is the double-reversed theorem for the displayed equation. The change of variables and the boundary transfer use the original coefficients throughout each argument.

##### The entire nested source [PS-NESTED].

For

```math
s_1=(-U,b_1),\quad s_2=(a_2,b_2),\quad s_3=(a_3,-F),
\qquad U,F,a_2,b_2>0,\quad a_3>a_2,\quad b_1>b_2,
```

every positive level has at most eight roots counted with multiplicity if the supports are noncollinear, and at most eight distinct roots on the collinear seam. Finite limits of its parameters also satisfy the bound eight for distinct roots, unless the function becomes identically zero. Here is the source proof. The numerators of the three barycentric coordinates of the origin are

```math
N_1=-(a_2F+a_3b_2),\quad N_2=a_3b_1-UF,
\quad N_3=-(Ub_2+a_2b_1).
```

If $`N_2<0`$, all barycentric coordinates of the origin are positive. The argument on the closed strictly convex level curve in [the appendix](appendix.md) gives at most eight roots counted with multiplicity. If $`N_2\ge0`$, the vector $`(b_1,U)`$ separates the convex hull of the three exponent points from the open negative quadrant. Also $`\lambda_1<\lambda_2<\lambda_3`$, with $`\lambda_1<0<\lambda_3`$ on the entire physical interval. When the determinant of the matrix with rows $`(1,a_i,b_i)`$ is positive, the origin identity writes $`\lambda_2=\theta\lambda_1+\eta\lambda_3`$, $`\theta,\eta>0`$, $`\theta+\eta<1`$, giving

```math
V_0=-\alpha_2\bigl[(1-\theta-\eta)
(\theta\lambda_1^2+\eta\lambda_3^2)
+\theta\eta(\lambda_1-\lambda_3)^2\bigr]<0.
```

For a negative determinant, $`\alpha_1,\alpha_3>0`$, $`\alpha_2=-k\le0`$, and, according to the sign of $`\lambda_2`$,

```math
\begin{aligned}
V_0&=\alpha_1(-\lambda_1)(\lambda_3-\lambda_1)
+k\lambda_2(\lambda_3-\lambda_2),&&\lambda_2\ge0,\\
V_0&=\alpha_3\lambda_3(\lambda_3-\lambda_1)
+k(-\lambda_2)(\lambda_2-\lambda_1),&&\lambda_2\le0.
\end{aligned}
```

Both are strictly positive. Thus the normal theorem for this separated convex hull gives at most nine roots counted with multiplicity; the negative endpoint signs improve this to eight, since the total multiplicity must be even. The affine-collinear and weak statements follow from a common-level regularization followed by perturbation preserving these opposite endpoint signs to the strict noncollinear source. This is a distinct-root transfer only.

##### One dictionary for both mixed source theorems.

Reflect if necessary so that

```math
a_1<0<a_2<a_3,\qquad b_3<0<b_1<b_2.
```

Write $`w=x(1-x)`$, $`D=w\,d/dx`$, $`\lambda_i=a_i-(a_i+b_i)x`$, $`J=\lambda_2-\lambda_1`$ and $`L=\lambda_3-\lambda_2>0`$. Define the actual cubics

```math
\begin{aligned}
P_1&=(D\lambda_2)J-\lambda_2(\lambda_1J+DJ),\\
P=P_3&=\lambda_2(\lambda_3L+DL)-(D\lambda_2)L,\\
G_{*}&=(\lambda_3-\lambda_1)JL+(DL)J-(DJ)L.
\end{aligned}
```

Their source-linked critical polynomial $`K_6`$ satisfies

```math
LP_1+JP=\lambda_2G_{*},\qquad
(DP-\lambda_1P)G_{*}-P DG_{*}=-L K_6,
\qquad\deg K_6\le6.                                      \tag{PS1}
```

$`P_1`$ has two simple physical roots straddling the mode $`c=a_2/(a_2+b_2)`$, and $`P>0`$ on $`(0,c]`$. These are literal source identities, not properties of arbitrary cubics.

##### A common-level theorem [PS-LEVEL].

If $`P`$ has exactly one odd-order physical root, or $`P,G_{*}`$ have a common physical root, then for every $`\kappa>0`$

```math
Z_{\mathrm{mult}}(P-\kappa h_1G_{*})\le6.                 \tag{PS2}
```

This covers multiple $`G_{*}`$ poles and the direct common-root cells. It does not assert (PS2) on an arbitrary three-root $`P`$ source. The proof counts derivative weights on the positive components of $`P/(h_1G_{*})`$, together with the compulsory weights in the negative gaps and at divisor events. If the contact weight were $`N\ge8`$, the count would force at least $`N-2\ge6`$ physical weights of $`K_6`$. At a shared event the common factor contributes two critical weights; it is retained before division. Exhaustion of all six weights invokes the actual-source exterior-witness lemma: both companion cubics have two real negative roots and one physical root. Their coefficient sign bounds (with zero coefficients allowed) and the positive fractional-power basis lemma then give the bound six, a contradiction. The [appendix](appendix.md) records these source imports and their precise hypotheses. The original derivative reduction and its interval-location lemma would require eight such intersections with the same level under ten original roots, so (PS2) excludes it.

##### A table-free common-height theorem [PS-HEIGHT].

Suppose instead that $`P`$ has three simple physical roots and $`P_1,P`$ are without common roots. For the two actual profiles

```math
F_{*}=-\frac{h_1P_1}{h_3P},\qquad W_{*} =\frac{h_1G_{*}}{P},
```

every positive level of $`F_{*}`$ has at most seven intersections counted with multiplicity. If it has seven simple level intersections $`r_1<\cdots<r_7`$, no real number $`\tau`$ can satisfy

```math
W_{*}(r_i)<\tau\ (i\text{ odd}),\qquad
W_{*}(r_i)>\tau\ (i\text{ even}).                         \tag{PS3}
```

No physical-root count of $`G_{*}`$, phase tag, cofactor interlacing or origin-wall restriction is imposed.

The source exterior-witness lemma and endpoint parity give at most four physical weights of $`K_6`$ when $`P`$ has three physical roots. Moreover

```math
DF_{*}=-\frac{h_1\lambda_2K_6}{h_3P^2},\qquad
DW_{*} =\frac{h_1 L K_6}{P^2}.                            \tag{PS4}
```

Thus $`\lambda_2K_6`$ has at most five weights, including its compulsory mode weight at $`c`$. The five $`P_1/P`$ events create three positive $`F_{*}`$ components and two negative gaps. Exactly one negative gap has two $`P`$ poles. On it $`1/F_{*}`$ is negative and vanishes at both endpoints, so it supplies one disjoint critical weight. Contacts of total weight $`N`$ on $`\ell\le3`$ occupied positive components therefore satisfy $`N-\ell+1\le5`$, hence $`N\le7`$.

Seven simple level intersections exhaust that budget. The mode $`c`$ must lie strictly between one consecutive pair of contacts in the first positive component and be its unique simple critical point. From (PS4),

```math
DW_{*}=-\frac{h_3L}{\lambda_2}\,DF_{*}.
```

At an odd-indexed preceding contact, $`F_{*}`$ has its unique maximum between that pair while $`W_{*}`$ strictly decreases across the entire gap. At an even-indexed contact the signs reverse. Each contradicts (PS3). This proves the two-profile theorem without the former allocation table.

To apply it to the original function, retain the original projective equality entry with its actual coefficients $`\rho=E_3/E_1>0`$, $`\kappa=E_1>0`$ and

```math
B_{*}=h_1J-\rho h_3L,\qquad X_{*}=\lambda_2/B_{*}.
```

The mixed denominator count is elementary. $`J`$ has one physical zero $`\ell`$ and is positive before it. On $`(0,\ell)`$, $`J/L`$ is strictly decreasing, as is $`h_1/h_3`$ because $`\lambda_1<0<\lambda_3`$. Their positive product decreases from infinity to zero, so $`B_{*}=h_3L[(h_1/h_3)(J/L)-\rho]`$ has exactly one simple physical zero. After $`\ell`$ it is strictly negative. This replaces the general linear/linear polynomial–beta count in the mixed source only; a coincidence with $`c`$ still belongs to the original interval-location lemma or original-function boundary transfer. Ten simple original roots force seven transverse $`F_{*}=\rho`$ contacts and the interval-location inequalities forced by equality in the nine-root derivative count. At these contacts (PS1) gives the undivided identity $`\lambda_2G_{*}=P B_{*}/h_1`$, hence $`W_{*}=1/X_{*}`$. The window requires $`X_{*}>\kappa`$ at useful odd nodes and $`0<X_{*}<\kappa`$ at even nodes. Its possible non-useful odd node has $`X_{*}<0`$, so also $`W_{*}<0<1/\kappa`$. All seven nodes therefore obey (PS3) with the *same* $`\tau=1/\kappa`$, a contradiction. This replaces the five-event height allocation tables; the original interval-location inequalities remain a specialized input with their stated hypotheses, rather than a freely chosen auxiliary height.

##### The double-reversed theorem [PS-DR].

In the remaining quadrant a positive projective coordinate gives

```math
H_\rho(t)=A_{*}(t)+\rho t^\alpha(1+t)^{\beta-\alpha}B_{*}(t),\qquad\rho>0,
```

where $`u,p,a,b,q,z>0`$, $`q<a`$, $`p<b`$, $`\alpha=u+q`$, $`\beta=p+z`$, and

```math
\begin{aligned}
A_{*}&=(u+pt)(a-bt)[a+u-(b-p)t]-(ap+bu)t(1+t),\\
B_{*}&=(q+zt)(a-bt)[(b+z)t-(a-q)]+(az+bq)t(1+t).
\end{aligned}
```

For every such source and every $`\rho>0`$, $`H_\rho`$ has at most five *distinct* positive roots. This includes equal and integral gaps, coefficient zeros and positive-event collisions. The strict hypotheses $`u,p,a,b,q,z>0`$, $`p<b`$ and $`q<a`$ are required for this particular auxiliary theorem.

Reflection interchanges $`\alpha,\beta`$ and reciprocates $`\rho`$, so assume $`\beta\ge\alpha`$. The theorem for a minimum exponent difference of at least one covers $`\alpha\ge1`$; the coefficient sign theorem for $`\beta<2`$ covers $`\alpha<1`$, $`\beta<2`$. In the remaining range put $`n=\lfloor\beta\rfloor\ge2`$, $`\zeta=\beta-n\in[0,1)`$. The alternating fractional-power basis $`1,t^\alpha(1+t)^{\zeta-\alpha},t,t^{1+\alpha}(1+t)^{\zeta-\alpha},\ldots`$ gives at most seven sign changes in the corresponding ordered coefficients. Six roots would force the first four coefficients of $`B_{*}`$, after multiplication by the degree-$`n`$ polynomial factor, to be nonpositive. Polynomial division by the linear factor belonging to the later $`B_{*}`$ root then forces the earlier root $`P>2/(\beta-1)`$ and the strict source event order $`P<Q<a/b<S<R`$. The actual profile $`-A_{*}/[t^\alpha(1+t)^{\beta-\alpha}B_{*}]`$ has three positive components. The source proofs give bounds of four intersections on the left outer component, three on the central component and two on the right outer component. Three central intersections exclude any tail intersection and exclude four left intersections; one central intersection excludes the simultaneous occurrence of four left and two tail intersections by one strict common-height chain. Thus every regular level has at most five contacts. Aggregate common-level regularization extends this to the *distinct* roots of the displayed equation; it does not promote the statement to a multiplicity theorem. When $`\zeta=0`$, the needed positivity follows directly from an integral representation with a positive measure. The appendix gives that representation, so no transfer of strict determinant signs through a limit is needed. The [appendix](appendix.md) identifies these three proof modules. The original ten-root entry needs seven contacts of this same displayed equation, contradicting five.

These arguments cover all strict generic split-exponent sources. A common constant shift, followed by a perturbation of the original supports with their exponent signs fixed, handles equalities between the logarithmic derivative scores, event collisions and finite coefficient/support faces at the original distinct-root scope. Only the bound for distinct roots of the original function is transferred to a boundary parameter.

### A height theorem when one term dominates at both endpoints

**Nonnegative-support height theorem [HEIGHT-MASTER].** Let $`u,v,w`$ be beta monomials whose support coordinates are nonnegative, and let $`c_3,c_4>0`$. Put $`S=u-c_3v-c_4w`$. For every nine ordered interior samples $`x_1<\cdots<x_9`$,

```math
\min_{i\in\{1,3,5,7,9\}}S(x_i)
\le\max\{0,S(x_2),S(x_4),S(x_6),S(x_8)\}.             \tag{MH}
```

Consequently $`c_1-S`$, with $`c_1>0`$, has at most eight distinct roots unless it is identically zero. No relative ordering of the three supports, mode restriction or bound on the coefficients is imposed. The weak identity exceptions are the case where all three beta monomials are constant and $`u=1`$, $`\{v,w\}=\{x,1-x\}`$, $`c_3=c_4=1-c_1\in(0,1)`$.

##### Proof from original-function saturation.

First take strictly positive supports. Failure of (MH) supplies one positive number $`\ell`$ between its right and left sides. Since $`S`$ tends to zero at both endpoints, the nine samples and the two endpoints give ten disjoint sign intervals for $`\ell-S`$. Divide this function by the nonzero beta monomial $`-u`$:

```math
\frac{\ell-S}{-u}=1-\frac\ell u-c_3\frac vu-c_4\frac wu.
\tag{MH1}
```

Its beta monomial $`1/u`$ has both exponents negative and is coordinatewise below the other two relative supports. The source transition lemmas [SUPPORT] are necessary conditions for these *ten original* roots. After reflection, they leave just three patterns for the other two relative supports: $`(+,+),(+,+)`$; $`(+,+),(+,-)`$; or $`(+,-),(+,-)`$. They are not a classification of arbitrary supports without saturation.

In the first pattern $`u`$ is a componentwise least support. The least-support proof has the proof for incomparable exponent vectors and the comparable modules described below. In the second pattern the full mixed theorem applies to

```math
C_0-E_0x^{-A}(1-x)^{-B}-E_1x^a(1-x)^b
-E_2x^c(1-x)^{-\nu},
```

with all magnitudes positive and $`B>\nu`$. It excludes ten roots at all scales, with no restriction on the shape of the positive regions, exponent differences or maxima. Its division into cases and final endpoint count are printed in [the appendix](appendix.md). In the third pattern write $`h_0=x^{-A}(1-x)^{-B}`$, $`h_j=x^{c_j}(1-x)^{-\nu_j}`$, $`B>\nu_j>0`$. Both $`h_j'`$ are positive. Before the minimum of $`h_0`$, each ratio $`h_j'/(-h_0')`$ is strictly increasing by its positive two-score identity; afterward the original derivative is negative. There is at most one critical point, hence at most two original roots. Each pattern contradicts the function with ten roots.

For weak nonnegative supports, add $`\varepsilon(1,1)`$ to every support. The values at the nine fixed interior samples converge, so their finite minimum and maximum pass continuously to the limit. This proves (MH) without taking an endpoint limit in the exponents. The distinct-root consequence uses the same aggregate level regularization and closed interior intervals whose endpoint values have opposite signs as above; identities are excluded explicitly.

##### The least-support proof for incomparable vectors.

The strict source can be written

```math
u=x^A(1-x)^B,\quad
v=x^{A+a}(1-x)^{B+b+q},\quad
w=x^{A+a+p}(1-x)^{B+b},\qquad A,B,a,b,p,q>0.
```

Two Rolle steps force eight contacts, at the same positive level, of a beta factor times a linked cubic ratio $`R/H`$ on the useful set $`R(H-R)>0`$. In the centered physical coordinate its critical numerator has degree at most six and opposite endpoint signs, hence at most five physical weights. If the negative $`R`$ and $`H-R`$ bands are separated, a compulsory critical point is outside the useful set; at most four useful criticals on at most three components give seven contacts. If the bands overlap, the actual exterior-root factor is strictly log-concave. Factoring it leaves a physical quadratic ratio, and the two-pole common-level comparison gives at most six contacts. Thus eight useful contacts are impossible. This argument applies to both orientations of the exponent differences.

### Comparable exponent vectors: four parameter ranges

In the strict comparable chain $`0\prec s_u\prec s_v\prec s_w`$, put $`q=w/v`$, reflect so that $`\det(s_v,s_q)>0`$, and write $`u=v^h q^n`$. If $`v=x^a(1-x)^b`$, $`q=x^A(1-x)^B`$, then $`0<b/B<a/A`$ and the actual support inequalities are

```math
0<hr+n<r\quad\text{at }r=b/B,a/A.
```

They give the exhaustive open regions

| Parameter region   | Argument excluding ten original roots                                                                                         |
|:-------------------|:-----------------------------------------------------------------------------------------------------------------|
| $`n>h`$              | Locate roots relative to the earlier maximum, propagate the resulting coefficient inequality and force a curvature root outside the allowed intervals.   |
| $`0<n<h<1`$          | The origin lies inside the exponent triangle; use the closed strictly convex level curve argument.                                                                     |
| $`n<0`$, $`h-n\ge1`$   | Use ratios of derivatives and the distance between their maxima; for $`h\ge1`$, the constant and fifth shifted coefficients have the same negative sign. |
| $`0<h<1`$, $`h-1<n<0`$ | Compare with the last positive maximum; the remaining sign and middle-interval arguments are given in the appendix.                   |

The equality $`h-n=1`$ is included directly in the larger-gap module. Other mode and determinant faces are handled by an original-function common-level regularization and support perturbation within the strict chain. The [appendix](appendix.md) states the retained modules and their source proof locations.

The whole middle region now has a short proof at the fixed actual coefficients. The identity

```math
s_u=(h-n)s_v+n s_w
```

means that, after division by $`-u`$ in (MH1), the barycentric coordinates of the origin of $`-s_u,s_v-s_u,s_w-s_u`$ are

```math
(1-h,h-n,n).
```

They are strictly positive precisely when $`0<n<h<1`$. The theorem for a closed strictly convex level curve therefore gives at most eight original roots counted with multiplicity for every noncollinear source in this entire region. This uses the actual coefficients directly and requires no further division according to the roots of an auxiliary polynomial. If all supports lie on a single ray with both coordinates positive, use a positive beta monomial $`T`$ and write $`u=T^\alpha,v=T^\beta,w=T^\gamma`$, $`0<\alpha<\beta<\gamma`$. After division by $`u`$, the sum of exponentials

```math
c_1e^{-\alpha z}+c_3e^{(\beta-\alpha)z}
+c_4e^{(\gamma-\alpha)z}-1,
\qquad z=\log T,
```

has strictly positive second derivative, hence at most two real roots counted with multiplicity. The beta coordinate has one nondegenerate maximum and at most doubles those weights, giving four. A coincident $`v,w`$ mode with $`u`$ off that ray is covered by the original-function perturbation, not by this special ray argument. Limits in which modes coincide receive the bound eight for distinct roots only.

To return to the function with one common endpoint-dominant term, write its supports as $`s_0=(-A,-B)`$ and $`s_j`$ for the other beta monomials. Dominance gives $`s_j-s_0`$ strictly positive coordinatewise. Dividing the original $`f`$ by its dominant nonzero beta monomial gives

```math
\frac{f}{E_0m_{s_0}}=
\frac1{E_0}m_{-s_0}-1
-\frac{E_1}{E_0}m_{s_1-s_0}
-\frac{E_2}{E_0}m_{s_2-s_0}.
```

Equivalently, division by $`-m_{s_0}`$ gives exactly $`E_0-m_{-s_0}+E_1m_{s_1-s_0}+E_2m_{s_2-s_0}`$. This is a positive common constant minus one nonnegative-support beta monomial plus two positive multiples of such beta monomials. The height theorem excludes ten original roots throughout these common-dominant cases while preserving the actual coefficients. Its statement at finite parameter limits concerns distinct roots.

### Conclusion of the three-versus-one sign case

The strict support partition is exhaustive under equality in the ten-root counting bounds. The all-positive, split-exponent, elementary, mixed, incomparable and comparable lemmas exclude every case. Apply Lemma 1(b) with sign vector $`(+,-,-,-)`$, $`N_0=9`$, and $`S=\{(0,s_1,s_2,s_3):s_i\in\mathbb R^2\}`$, where $`0`$ denotes the zero exponent vector and the constant coefficient is allowed to be positive. The dense set and its proper exceptional subsets are specified by [C31] and the boundary assembly [WEAK]. Dividing by the constant coefficient then recovers (25). This proves Theorem 4, including its finite boundary parameters, from the stated source inputs.

## Assembly of the upper bound

We can now finish Theorem 2. With four nonzero coefficients, a sum with coefficients of both signs has, up to overall sign reversal, split $`(3,1)`$ or $`(2,2)`$. Theorems 4 and 3 give nine, respectively. A sum with coefficients all of the same sign has no zeros.

For fewer nonzero terms, include zero coefficients to represent the function with four labeled terms. Choose a sign for each zero coefficient, retaining the signs of all nonzero coefficients. Apply Lemma 1(b) with this sign vector, $`S=(\mathbb R^2)^4`$, and $`N_0=9`$. Every function in the open sign family is covered by the preceding cases. The given nonidentity function belongs to its closure, so it too has at most nine distinct zeros.

The monomial normalization and degenerate-support reduction now give the polynomial upper bound $`N(3,4)\le9`$, including degenerate trinomial support and excluding common curve components from the isolated count.

## An exact nine-root example

Take

```math
F(x)=1-\sum_{i=1}^3 E_i x^{a_i}(1-x)^{b_i}
```

with the following values interpreted as **exact terminating decimals**, not rounded descriptions of unknown parameters:

| $`i`$ | $`E_i`$ | $`a_i`$ | $`b_i`$ |
|---:|---:|---:|---:|
| 1 | $`1.0087711983885019`$ | $`0.0020954782173229`$ | $`1.2835032616093814`$ |
| 2 | $`1.3358363059764513`$ | $`1.0252846058508502`$ | $`0.9082951710178624`$ |
| 3 | $`0.9900599367225573`$ | $`2.0673123701130679`$ | $`-0.0016847698173825`$ |

Set $`x(u)=1/(1+e^{-u})`$. At the following exact decimal $`u`$ values, interval evaluation gives the displayed enclosures. The wider decimal intervals below are outward enclosures of the 100-digit interval outputs.

|       $`u`$ | Enclosure for $`F(x(u))`$       |
|----------:|:------------------------------|
|   $`-0.25`$ | $`[2.4514,2.4515]\,10^{-13}`$   |
| $`-0.2135`$ | $`[-9.2068,-9.2067]\,10^{-15}`$ |
|   $`-0.16`$ | $`[2.9622,2.9623]\,10^{-14}`$   |
|   $`-0.09`$ | $`[-1.4319,-1.4318]\,10^{-14}`$ |
|       $`0`$ | $`[4.1145,4.1146]\,10^{-14}`$   |
|    $`0.09`$ | $`[-1.4356,-1.4355]\,10^{-14}`$ |
|    $`0.15`$ | $`[2.0212,2.0213]\,10^{-14}`$   |
|    $`0.22`$ | $`[-1.2899,-1.2898]\,10^{-13}`$ |
|       $`1`$ | $`[1.6603,1.6604]\,10^{-7}`$    |
|       $`5`$ | $`[-3.6729,-3.6728]\,10^{-4}`$  |

The ten values alternate in sign: $`+,-,+,-,+,-,+,-,+,-`$. Since $`x(u)`$ is strictly increasing, the intermediate value theorem gives a zero in each of the nine intervening disjoint intervals. The example is not an identity. It has at least nine distinct roots, and the upper bound makes the count exactly nine. The proof calculation for these interval enclosures is described in the appendix; it uses the exact decimals printed above.

### An explicit system with integer exponents

Let

```math
D_0=10^{16},\qquad L=16847698173825,
\qquad A_i=D_0a_i,\quad B_i=D_0b_i.
```

The integers are

```math
(A_1,A_2,A_3)=(20954782173229,10252846058508502,20673123701130679),
```



```math
(B_1,B_2,B_3)=(12835032616093814,9082951710178624,-16847698173825).
```

Consider

```math
\boxed{\begin{aligned}
X^{D_0}+Y^{D_0}-1&=0,\\
Y^L-E_1X^{A_1}Y^{B_1+L}
-E_2X^{A_2}Y^{B_2+L}
-E_3X^{A_3}Y^{B_3+L}&=0.
\end{aligned}}                                         \tag{30}
```

All exponents are nonnegative integers, and $`B_3+L=0`$. The two equations have three and four distinct monomial terms. Their coefficients are rational; clearing coefficient denominators makes them integral if desired. Along the first curve put $`x=X^{D_0}`$, $`1-x=Y^{D_0}`$. The second equation is exactly $`Y^LF(x)=0`$. Thus the nine certified univariate roots give nine positive isolated intersections of (30).

No simplicity claim about the unperturbed witness is needed. Label the ten displayed sample values $`u_0<\cdots<u_9`$. Choose a regular value $`t`$ of $`F`$, as in the proof of Lemma 1(a), with

```math
0<|t|<\min\left\{\frac12,
\frac12\min_{0\le\ell\le9}|F(x(u_\ell))|\right\}.
```

Replace the coefficient of $`Y^L`$ in (30) by $`1-t`$. The new restriction is $`F-t`$, with the same ten endpoint signs and therefore at least nine distinct roots. All these roots are simple because $`t`$ is a regular value. The upper bound shows that there are exactly nine. The first curve is smooth in the positive quadrant, and a simple restriction zero makes the intersection nondegenerate. The same term counts are retained. Hence the nondegenerate maximum is also nine.
