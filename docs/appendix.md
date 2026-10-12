# Appendix: specialized proofs and exact calculations

The [main proof](proof.md) gives the reduction, the case coverage, and the final nine-root example. This appendix expands its specialized arguments and links to their complete mathematical proofs. A named label is a reference to a proved statement under its displayed assumptions. In particular, the auxiliary polynomials are linked to the original exponent parameters; an assertion about those linked polynomials is not automatically an assertion about arbitrary polynomials.

The [reciprocal-coordinate lemmas](#reciprocal-coordinate-height-and-regional-bounds) give height and root bounds under explicit parameter conditions. The F3 coefficient arguments cover the parameters outside those regions. The [calculation guide](calculations.md) explains the exact identities and their supporting coefficient data.

## Terminology

The [reading guide](reading-guide.md#terms-used-in-the-documents) defines the common terms. In the technical proofs, a **weight** means a zero's multiplicity, a **physical** point lies in the interval corresponding to the original variable, and a **source** formula retains the relations to the original exponents. An **event order** lists the designated cofactor roots from left to right. A **wall** is a root or parameter equality where the indicated formula changes sign; its location and type are specified locally.

A **Wronskian** is a determinant formed from functions and their consecutive derivatives. Its factorizations make repeated Rolle arguments possible. **Weighted Rolle** counts multiplicities: a zero of order $`m`$ leaves order $`m-1`$ under differentiation, and consecutive distinct zeros force an additional derivative zero between them. A **positive integrating factor** transforms a first-order equation $`d'=Ad+F`$ into $`(e^{-\int A}d)'=e^{-\int A}F`$.

The **origin barycentric coefficients** are the coefficients $`\alpha_i`$ with $`\sum\alpha_i=1`$ and $`\sum\alpha_i s_i=0`$; they express the origin relative to three exponent vectors. **Affine independence** means those three vectors do not lie on one line. The **convex hull** is their filled triangle. **Gibbs weights** are the positive numbers $`p_i=E_ie^{s_i\cdot z}/\sum_jE_je^{s_j\cdot z}`$, which sum to one. The term **entropy curve** refers to the level curve of the explicitly printed logarithmic function $`\mathcal J`$; its definition, rather than an information-theory interpretation, is used in the proof.

A **forcing polynomial** is the polynomial $`F`$ on the right of a displayed differential comparison. Its zeros bound the zeros of the compared functions by Rolle. A **residue** is the coefficient of $`(x-r)^{-1}`$ in a rational function at a pole $`r`$. A **Stieltjes representation** is a positive integral of reciprocal functions $`(z+s)^{-1}`$; the fractional-power proofs display the actual measure. A **Hurwitz matrix** is the particular shifted coefficient matrix defined in those proofs; **total nonnegativity** means every finite minor is nonnegative. **Cauchy--Binet** is the determinant formula for a product of rectangular matrices. A **jet** is the finite list of values of a function and its derivatives at a point. **Gaussian quadrature** replaces a positive measure by finitely many positive point weights that match a stated finite list of moments.

Technical filenames name their mathematical content. All symbols and section numbers inside a linked lemma are local to that lemma. A local coefficient table proves a sign only under that lemma's listed nonnegative-factor assumptions.

Other local terms have these meanings:

| Term | Meaning |
| --- | --- |
| Score | The affine logarithmic derivative $`D\log h=a-(a+b)x`$ of a beta monomial. |
| Mode | An interior maximum or minimum of a beta monomial, at its score's zero. |
| Log-convex / log-concave | The logarithm of a positive function is convex / concave in the variable specified by that proof. |
| Pole | A point where a rational function's denominator vanishes and its value becomes unbounded. |
| Interlacing | Roots from the specified two functions alternate in their stated order. |
| Deflation | Removing an explicitly known polynomial factor, with its roots counted separately when necessary. |
| Projective coordinate | The stated ratio or rational change of variables; only its printed domain is used. |
| Seam | A boundary or joining point of the stated coordinate intervals. |
| Normal direction | A vector perpendicular to a level curve; the normal-flow calculation parametrizes the curve by that direction. |
| Strong fork | The stated positive-support relation $`s_2=Ps_1+Qs_3`$, with $`P,Q>1`$. |
| Split supports | Two supports have opposite mixed exponent signs $`(-,+)`$ and $`(+,-)`$, while the third has $`(+,+)`$. |
| Saturation / exhaustion | A hypothetical root count uses the entire upper bound allowed by degree or Rolle's theorem. |
| Root budget / ceiling | An upper bound on the number of roots, with its counting convention stated. |
| Analytic unit | An analytic factor that never vanishes on the interval; dividing by it preserves zero orders. |
| Prefix | An initial segment of an ordered list, as in the coefficient arguments. |

## Where each main-proof input is proved

| Label | Content and complete proof |
| --- | --- |
| EHT | The two-polynomial estimate, stated with its exceptions in [references](references.md). |
| WEAK | [Original distinct-root regularization and finite parameter limits](lemmas/baseline/limiting-cases.md). |
| COMP-ATOM / F1-INT | [Comparable factor, derivative operator, and interpolation proof](lemmas/baseline/comparable-atom.md). |
| EIGHT-ORDER / GL-ALL | [Eight coordinate orders and the enlarged least-support argument](lemmas/baseline/global-least-and-eight-orders.md). |
| GL | [Least support with comparable negative factors](lemmas/baseline/least-support-and-comparable-pairs.md). |
| DISJOINT | [A compulsory contact outside the common useful intervals](lemmas/baseline/disjoint-contact-exclusion.md). |
| C22 | The preceding four entries and the F2, F3, F4 entries below give the two-positive, two-negative case coverage. |
| F2-HEIGHT | The F2 section of [the main proof](proof.md) gives the inverse-anchor comparison and common-height argument explicitly; it invokes the included generic transfer, rather than an arbitrary cubic contact bound. |
| F4-TWO / F4-CENTRAL / F4-LASTD / F4-INITIAL | The F4 section of [the main proof](proof.md) states the two-cubic root geometry and proves the three required interval bounds. |
| F3-SUM | [The two exterior exponent-sum orders](lemmas/baseline/two-exponent-sum-orders.md) and [the intermediate sum order](lemmas/baseline/intermediate-exponent-sum-order.md). |
| F3-ORDER-I | [The two cofactor orders](lemmas/baseline/f3-two-cofactor-orders.md), including its first order. |
| F3-THREE | [Uniform three-physical-root theorem](lemmas/f3/three-physical-root-count.md). |
| F3-JOINT | The F3 assembly in the main proof and the three detailed F3 coefficient arguments below, with [real extra pairs](lemmas/baseline/f3-real-exterior-pairs.md), [fixed-root interlacing](lemmas/baseline/f3-fixed-exterior-interlacing.md), [one left contact](lemmas/baseline/f3-first-order-left-contact.md), and [the qualified second-order left count](lemmas/baseline/f3-second-order-left-contacts.md). |
| F3-NEWTON | The first-two-Newton argument below and its exact [F3 calculation data](calculations.md). |
| C31 / SUPPORT | [Endpoint-dominant support classification and its local one-corner refinement](lemmas/baseline/endpoint-support-classification.md). |
| EASY | [Fully analytical signed-curvature exclusion](lemmas/geometry/signed-curvature-exclusion.md). |
| AP-MASTER | [All positive supports](lemmas/positive/positive-eight.md), using [the two-wall proof](lemmas/positive/two-wall-positive-master.md), [the one-wall proof](lemmas/positive/one-wall-positive-master.md), and the direct [low](lemmas/positive/unit-one-wall-low.md) and [high](lemmas/positive/unit-one-wall-high.md) unit-wall proofs. |
| PS-NESTED | [Normal-curvature proof for nested split supports](lemmas/geometry/normal-curvature.md). |
| PS-LEVEL | [Three designated events at one level](lemmas/pure-split/three-event-level-count.md), with the linked fractional-power and common-factor lemmas. |
| PS-HEIGHT | [Five-event shared-height proof](lemmas/pure-split/five-event-shared-height.md), its [assumptions](lemmas/pure-split/five-event-assumptions.md), and [original shared-coefficient entry](lemmas/pure-split/original-five-event-entry.md). |
| PS-DR | [Double-reversed five-root theorem](lemmas/pure-split/double-reversed-five-root-count.md), with its [large-gap](lemmas/pure-split/double-reversed-large-gap.md), [small-exponent](lemmas/pure-split/double-reversed-small-exponent.md), and [component-height](lemmas/pure-split/double-reversed-component-compatibility.md) modules. |
| HEIGHT-MASTER | [Unrestricted nonnegative-support height theorem](lemmas/height/nonnegative-height.md), [least-support](lemmas/height/least-support-height.md), [all-scale mixed](lemmas/height/mixed-height.md), and [comparable](lemmas/height/comparable-height.md) assemblies. |

## Exact arithmetic in the lower-bound example

The terminating decimals in the main proof are exact rational numbers. The included calculation evaluates their exponential terms at the ten listed rational points using the interval context of `mpmath`, with 100 decimal digits of working precision. Its interval exponential and logarithm operations retain enclosures of the resulting function values. The intervals have the ten alternating signs required by the intermediate value theorem. See the [calculation guide](calculations.md) for the included proof-calculation program and the exact example data.

## Actual-level normal flow and the signed eight-root theorem

This calculation supplies the common analytic core of [AP-MASTER], [PS-NESTED] and the new comparable middle proof. Let the three real supports be affinely independent, with positive coefficients and positive level $`L`$. Write $`G(z)=\log\sum_i E_i e^{s_i\cdot z}`$, $`q(z)=e^{z_1}+e^{z_2}`$ and $`\ell=\log L`$. Let $`\alpha`$ be the origin barycentrics and let $`\beta(x)`$ satisfy $`\sum\beta_i=0`$, $`\sum\beta_i s_i=(x,1-x)`$. On an actual positive-normal level branch,

```math
\nabla G=\tau(x,1-x),\quad\tau>0,
 \qquad p_i=E_i e^{s_i\cdot z-\ell}=\alpha_i+\tau\beta_i>0.
```

 Put $`d_i=a_i+b_i`$, $`\lambda_i=a_i-d_i x`$, $`w=x(1-x)`$ and

```math
\begin{aligned}
 V&=\sum p_i\lambda_i^2,& C&=\sum p_i\lambda_i d_i,&\rho&=\tau/V,\\
 V_0&=\sum\alpha_i\lambda_i^2,&V_1&=\sum\beta_i\lambda_i^2,\\
 C_0&=\sum\alpha_i\lambda_i d_i,&C_1&=\sum\beta_i\lambda_i d_i,\\
 \Lambda&=\sum\lambda_i,&\Pi&=\lambda_1\lambda_2\lambda_3.
\end{aligned}
```

 Here $`V>0`$, $`V_0`$ is quadratic and $`C_0=-V_0'/2`$. Differentiating the normal equation and its Gibbs weights gives

```math
z'=\rho(1-x,-x),\quad p_i'=\rho p_i\lambda_i,
 \quad\tau'=\rho C,
 \quad V'=\rho\sum p_i\lambda_i^3-2C.
```

 The mean score is zero. Its cubic polynomial therefore gives $`\sum p_i\lambda_i^3=\Lambda V+\Pi`$. Use $`V=V_0+\tau V_1`$, $`C=C_0+\tau C_1`$ and $`V(1-\rho V_1)=V_0`$ to obtain

**(A1)**

```math
V_0\rho'=3C_0\rho+\mathcal B\rho^2+\Pi V_1\rho^3,
 \quad\mathcal B=3C_1V_0-3C_0V_1-\Lambda V_0-\Pi.
```

 On a zero-free $`V_0`$ interval, $`d=\rho-1/w`$ obeys

**(A2)**

```math
d'=A(x)d+\frac{T(x)}{V_0w^3},\qquad
 T=3C_0w^2+\mathcal B w+\Pi V_1+V_0(1-2x)w.
```

 The coefficient $`A`$ is analytic, including at $`d=0`$. The degrees $`\deg V_0\le2`$, $`\deg V_1\le3`$, $`\deg C_0\le1`$, $`\deg C_1\le2`$ give $`\deg T\le6`$ directly. A positive integrating factor and weighted Rolle give at most seven weights of $`d`$ when $`T`$ is nonzero. The identities

**(A3)**

```math
H=\log\frac{x}{1-x}-z_1+z_2,
 \quad H'=-d,
 \quad \frac{d}{dx}q(z(x))=\rho e^{z_2}x(e^{-H}-1)
```

 give the normal contact budget. If $`T\equiv0`$, (A2) is homogeneous: $`d`$ is zero-free or identically zero. The latter gives constant $`H`$; each geometry below treats this alternative explicitly.

#### Origin strictly inside the source triangle.

If all $`\alpha_i>0`$, $`G`$ is coercive and strictly convex. Its minimum level is empty or a singleton; a contact of that singleton with $`q=1`$ has order exactly two by the positive Hessian. Every higher level is a compact strictly convex analytic oval. The positive-normal arc is $`0<x<1`$ and $`V_0>0`$. Its finite endpoints give $`H(0+)=-\infty`$, $`H(1-)=+\infty`$. Thus its at-most-eight $`H`$ weights are odd, hence at most seven. The homogeneous constant-$`H`$ case is incompatible with these endpoint limits. On the negative-normal arc $`q`$ has exactly one critical point: its unique minimum on the convex sublevel. The constrained tangent Hessian is $`\operatorname{Hess}q+c\operatorname{Hess}G>0`$, so its derivative weight is one. Mixed and axis normals give no $`q`$ critical point. Periodic weighted Rolle on the full oval now bounds every $`q=1`$ level by eight contact weights.

#### Separated hull and a zero-free actual normal quadratic.

If the source hull misses the open negative quadrant, a separating $`n\in[0,\infty)^2\setminus\{0\}`$ has $`n\cdot s_i\ge0`$, with at least one strict inequality. Consequently $`\partial_nG>0`$ and the whole level is one connected analytic graph. Its actual positive-normal domain is one open angular interval. For an interior normal, write it as $`\sum c_i s_i`$ with every $`c_i>0`$. On a sublevel all $`s_i\cdot z`$ have upper bounds; an escaping supporting-cap sequence would force all $`s_i\cdot d=0`$ in its limiting direction, contradicting that the supports span the plane. Hence the supporting cap is compact and has one actual normal point. These points give the analytic branch above. There are no negative-normal $`q`$ criticals. If $`V_0`$ is zero-free on this branch, (A2)–(A3) and ordinary weighted Rolle give nine contact weights on the whole connected graph. Equal eventual nonzero signs of the original row improve nine to eight. In the homogeneous case, constant $`H=0`$ would make $`q`$ constant on an open branch and hence on the graph; the constant is either different from one, giving no roots, or gives an excluded original identity.

Original orders agree with these contact orders. At a tangency, both regular curves are local analytic graphs over one logarithmic coordinate; their restricted defining functions are nonzero analytic units times the same graph difference. The beta coordinate is a local analytic diffeomorphism. This also explains why none of the weighted conclusions depends on a simplicity assumption.

## Positive coefficient arguments

The proofs below handle positive coefficient sums through a common level curve. Their coefficient identities and table conventions are described in [the calculation guide](calculations.md).

### Curvature for positive supports

The two-positive-barycentric chart in [AP-MASTER] has probabilities

```math
(p_1,p_2,p_3)=\frac{(1-Pu,u,r-Qu)}{1+r-K_{*}u},
 \quad0<u<\min(1/P,r/Q).
```

 For every fixed actual coefficient level its entropy constant defines one analytic graph $`u_C(r)`$:

```math
\mathcal J(r,u)=\frac{P\log(1-Pu)-\log u+Q\log(r-Qu)
               -K_{*}\log(1+r-K_{*}u)}{K_{*}}=C.
```

 Here $`\mathcal J_u<0`$ and the two physical $`u`$ endpoints have infinite opposite entropy limits. Put $`B=r(1+r)`$, $`H=P(P-1)r^2-2PQr+Q(Q-1)`$, $`j=Q-(P-1)r`$ and $`Y=R-B`$. Normal curvature has the same zero orders as $`B+Hu_C-R`$. The exact derivatives are

```math
u_C'=\frac{j u_C(1-Pu_C)}{B+Hu_C},\qquad
 u_C''=\frac{u_C(1-Pu_C)(r-Qu_C)(1+r-K_{*}u_C)}{(B+Hu_C)^3}H.
```

 The physical denominator is positive. Moreover the elasticity $`e_C=r u_C'/u_C`$ satisfies

**(A4)**

```math
e_C'=-\frac{(1-Pu_C)(r-Qu_C)
 \{u_C(H+K_{*}r)^2+K_{*}r^2(1+r-K_{*}u_C)\}}{(B+Hu_C)^3}<0.
```

 Away from a wall compare $`u_C`$ with $`u_0=Y/H`$. Their difference obeys

**(A5)**

```math
(u_C-u_0)'=a(r)(u_C-u_0)-\frac{W}{H^2R},
 \quad W=R(HY'-H'Y)-Y(H-PY)j,\qquad\deg W\le6.
```

 The coefficient $`a`$ is analytic throughout each wall interval, even where $`u_0`$ lies outside the physical probability caps. Thus a positive integrating factor bounds contact weight by the forcing weight plus one.

The complete two-wall module ($`P,Q>1`$) uses seven projective coefficients of (A5), plus (A4). Low–low walls give at most four central contacts; three simultaneous contact components would require five zeros of the formal power-tangent difference, whose generalized coefficient word has only four variations. Mixed walls use a strictly positive sum of the two uncertain forcing coefficients. High–high walls have a direct four-curvature budget. Unit walls are deflated directly. These give curvature six in every case; when both wall ratios are at least one, the stronger curvature four gives original weighted six. That sharpening is optional in the chamber assembly.

For the one-wall rows the hypothesis that $`R`$ has three real negative roots is retained. It comes from the displayed actual metric, not from mere positivity of its coefficients. The strict one-wall theorem for $`P>1>Q>0`$ uses the negative metric root to close the low-wall exterior budget, and the positive-cubic high-wall comparison on the other side. Its native $`Q=1`$ completion has low, high and direct-unit arguments; the excluded projective endpoint $`r=0`$ is never counted as a physical wall. Those modules each bound the actual curvature weight by six, including their actual contacts and unit faces. Reflection exchanges $`P,Q`$ and reverses $`r`$ without changing orders. No multiplicity limit between entropy models is used.

Thus the ONE-EDGE and upper-fork event traversals are historical alternatives. The original endpoint and finite-boundary conclusions follow from the actual-level theorem and the distinct-only transfer printed in the main proof.

## Height proof modules and their retained parameter inequalities

The broad height statement is the fixed-sample consequence of original ten-root exclusion, as (MH1) shows. Its local [SUPPORT] refinement and the elementary two-mixed-atom derivative ratio are retained analytic inputs. The complete height statement and its proof are given in the linked documents.

#### The incomparable least-support proof.

Its actual cubics satisfy $`H=R+K`$ and have positive physical endpoints. In the centered coordinate, with a positive physical cubic $`T`$, they have the common forms

```math
R=r[P-(r+1)Z],\quad H=(r+1)[P-rZ],\quad K=P,
 \quad Z=x^2-e,\quad P=T-\varrho x+(2r+1)x^2.
```

 For $`\Phi=w_0R/H`$, $`(\log w_0)'=-x/T`$, and

```math
\Phi'=-\frac{w_0r(r+1)Q}{TH^2},\qquad
 Q=x[P-(r+1)Z][P-rZ]+T(2xP-ZP').
```

 The degree-seven terms cancel; $`\deg Q\le6`$, and its two physical endpoint values have opposite signs. Hence at most five physical critical weights are available. The separated-band charge and the overlapping-band log-concavity/two-pole comparison in the main text contradict eight useful contacts. The centered numerator alone has this degree-six assertion; the undivided original-coordinate numerator can have degree seven. [fork master height assembly](lemmas/height/incomparable-least-support-height.md), with its linked exterior-factor concavity and quadratic-ratio proofs. The least-support assembly is [least support master height theorem](lemmas/height/least-support-height.md).

#### The mixed one-corner proof, at all scales.

For the strict mixed row in (MH1), use its actual slopes $`\ell_0=-A+(A+B)x`$, $`\ell_1=a-(a+b)x`$, $`\ell_2=c-(c-\nu)x`$, $`P_i=\ell_i^2+D\ell_i`$ and

```math
R=\ell_1P_2-\ell_2P_1,\quad V=\ell_2P_0-\ell_0P_2,
 \quad C=\ell_0P_1-\ell_1P_0,
 \quad W=\det[\ell_i;P_i;\ell_iP_i+DP_i].
```

 For $`c>a`$, $`R`$ has one or three physical roots. The complete source dispatcher is: $`c<a`$; three physical $`R`$ roots; one root with $`\mu=A/(A+B)>m=a/(a+b)`$; one root with $`\mu<m`$ and $`V(r)>0`$; or one root with $`V(r)<0`$. These five scopes have the same eight-distinct-root conclusion. The third-root geometry supplies the translated pair inequalities rather than imposing an extra gap inequality. The last, straddling scope uses the late $`C`$ root $`d`$ and the exact endpoint identities

```math
\frac{C''(d)}{C'(d)}<\frac4{d-m},\quad
 \frac{\ell_0(d)}{x(1-x)|_{x=d}}<\frac1{d-m},\quad
 \frac{W'(d)}{W(d)}=\frac{C''(d)}{C'(d)}
       +\frac{\rho'(d)-\ell_2(d)+\ell_0(d)}{\rho(d)}-\frac1{d-m},
```

 where $`\rho=x(1-x)`$. They give $`(d-r)W'(d)/W(d)<5`$. With $`W(r)\le0`$, $`W(d)<0`$ and degree six, the endpoint budget permits at most four $`W`$ roots on $`(r,d)`$, five selector contacts there, six contacts of the late original derivative and one on its initial component. Hence $`f'`$ has at most seven roots and $`f`$ at most eight. This is an endpoint budget, not a claim that $`W`$ is everywhere negative. Its four earlier modules remain at their scopes; the original complete NOLOBE/GENUINE inputs, lobe event atlases and coefficient tables are not imported into this dispatcher.

#### The three remaining comparable modules.

For $`n>h`$, saturated curvature nodes are all after the last relevant mode; a concave contact function propagates the one actual coefficient inequality and charges a compulsory unused root. For $`n<0`$, $`h-n\ge1`$, the derivative ratio gives at most two original roots after the gap mode and forces six Wronskian roots before it; its strictly negative mode value contradicts degree-six endpoint parity. The $`h\ge1`$ part instead has negative constant and fifth shifted coefficients, inconsistent with six positive roots; $`h=1`$ has degree at most five. For $`0<h<1`$, $`h-1<n<0`$, the actual last positive maximum fixes one height. The two physical signed placements allow at most five nodes: respectively $`0+3+1+1`$ or $`2+2+1`$. The reversed left-pole sign forces a forbidden positive-coefficient crossing. This last proof retains its central orientation certificate, metric separator and last-maximum integral bridge. The exact four-region dictionary and all retained module paths are in [global master height theorem](lemmas/height/comparable-height.md). Its middle module is replaced, throughout $`0<n<h<1`$, by [comparable middle by origin interior curvature](lemmas/height/middle-height-by-convexity.md). Thus the middle birth/orientation packets are not dependencies of this revision; the other three comparable modules remain scoped inputs.

## Pure-split source proofs and the retained original entry

[PS-LEVEL] is the literal theorem in [mixed three event common level theorem](lemmas/pure-split/three-event-level-count.md). It includes the common-event factor count and one-odd-$`P`$ dividend count, the exact exterior witness, and the retained root-factor fractional Hurwitz theorem. The witness requires actual linked cubics and full physical sextic exhaustion. It is not an arbitrary-cubic discriminant theorem.

[PS-DR] is the complete raw theorem in [uniform raw double reversed five root theorem](lemmas/pure-split/double-reversed-five-root-count.md). The min-gap-one, low-$`\beta`$ Hurwitz and regular-component modules are named there with their exact scopes. The integral seam uses the positive representation

```math
\frac{t^\alpha}{(1+t)^\alpha}
 =\frac{\sin(\pi\alpha)}\pi
   \int_0^1\frac{t}{t+s}s^{\alpha-1}(1-s)^{-\alpha}\,ds,
 \qquad0<\alpha<1.
```

 Finite Gaussian quadrature reproduces the selected finite jets and gives strict positive minors. Regular-level contacts have the component budget described in the main proof; a better-direction common-level shift retains at least every selected *number* of raw distinct contacts. It need not preserve every old even-contact neighborhood, and proves no raw multiplicity ceiling. The original double-reversed projective entry needing seven contacts and the source reflection are retained at their original-row scopes.

## F3 polynomial inequalities

These are inequalities in the polynomials linked to the original F3 exponents. The original-root cuts come first, followed by the cofactor and coefficient arguments.

### F3 original-root cuts

All three cuts in (F3-CUT) concern (19)–(20) with its four original coefficients. In particular $`A=a-e>B=b+d>0`$. The original function is positive near both endpoints, so a generic simple-root count is even.

#### One contour proof for $`A<4`$, $`B<2`$.

Let $`P,Q`$ be monic real cubics, with $`Q`$ having one root $`q\in(0,1)`$ and a genuine nonreal pair. For nonintegers $`0<\beta<\alpha<4`$, $`\beta<2`$, and a fixed $`\kappa>0`$, the equation

```math
Q(x)=\kappa x^\alpha(1-x)^{-\beta}P(x)
```

 has at most seven distinct solutions. No hypothesis on the other roots of $`P`$ is needed. Put $`z=1-x`$, $`N(z)=-P(1-z)`$ and $`M(z)=-Q(1-z)`$. Then $`M(z)=(z-r)C(z)`$ with $`r=1-q\in(0,1)`$ and a monic quadratic $`C>0`$ on the real line. At eight hypothetical solution nodes $`z_i`$, put $`\omega(z)=\prod_i(z-z_i)`$ and choose

```math
m=\lfloor\alpha\rfloor,\quad n=\lfloor\beta\rfloor,\quad
 \varepsilon=1-n,\qquad Z(z)=(1-z)^m(z-r)^\varepsilon.
```

 The degrees of $`NZ`$ and $`MZ`$ are $`d=4+m-n\le7`$. Lagrange interpolation gives

```math
L:=\sum_i\frac{z_i^\beta(1-z_i)^{-\alpha}M(z_i)Z(z_i)}
                         {\omega'(z_i)}
              =\kappa[z^7](NZ)\le0.
```

 Indeed the coefficient is zero when $`d<7`$; the sole degree-seven case is $`m=3,n=0`$, whose leading coefficient is $`-1`$. Residue deformation on the two exterior cuts gives

```math
\begin{aligned}
 L={}&\frac{\sin\pi\beta}{\pi}\int_{-\infty}^0
    \frac{|t|^\beta(1-t)^{-\alpha}M(t)Z(t)}{\omega(t)}\,dt\\
 &+\frac{\sin\pi\alpha}{\pi}\int_1^\infty
    \frac{t^\beta(t-1)^{-\alpha}M(t)Z(t)}{\omega(t)}\,dt.
\end{aligned}
```

 On both cuts $`\omega>0`$. On the left, both $`MZ`$ and $`\sin\pi\beta`$ have sign $`(-1)^n`$; on the right, both $`MZ`$ and $`\sin\pi\alpha`$ have sign $`(-1)^m`$. Thus both integrals are strictly positive. Convergence is explicit: the endpoint powers are $`\beta>0`$ at zero and $`m-\alpha\in(-1,0)`$ at one. The large-circle exponent, including its length, is $`\{\beta\}-\{\alpha\}-3<0`$. Common roots of $`P,Q`$ give zero residues. This contradicts $`L\le0`$. One floor-parity choice replaces the four former interpolation strips.

For the actual F3 $`03`$ anchor, let $`\lambda_3=c-(c-f)x>0`$, and use the original triple beta-jet core $`H`$. For a support $`r=(r_1,r_2)`$, write $`\lambda_r=r_1-(r_1+r_2)x`$ and $`D_x=x(1-x)\partial_x`$; explicitly

```math
H(r,s)=\lambda_rD_x\lambda_s-\lambda_sD_x\lambda_r
                 +\lambda_r\lambda_s(\lambda_s-\lambda_r).
```

 Its two pole-free operations give, up to a positive common factor,

```math
A_1x^A(1-x)^{-B}P_{\rm raw}-B_0Q_{\rm raw},\quad
 P_{\rm raw}=-H((a,-b),(c,-f)),\quad
 Q_{\rm raw}=-H((e,d),(c,-f)).
```

 Their leading coefficients are strictly positive:

```math
L_P=(a-b)(c-f)(c-f-a+b),\qquad
 L_Q=(e+d)(c-f)(c-f-e-d).
```

 Monic normalization therefore has the single original level $`\kappa=A_1L_P/(B_0L_Q)>0`$, with $`(\alpha,\beta)=(A,B)`$. Seven residual zeros and two Rolle losses give at most nine simple original zeros, hence eight by parity. The real extra-pair degree budget and the allocation-free THREE theorem below cover the other cofactor strata in the same original-root argument.

#### The elementary large-$`B`$ and $`B=1`$ seams.

For $`P(x)=\sum_{j=0}^3p_jx^j`$, $`P(0)<0<P(1)`$, define the index cubic

```math
\begin{aligned}
 I(z)={}&p_0(z+\beta-3)(z+\beta-2)(z+\beta-1)\\
 &+p_1z(z+\beta-3)(z+\beta-2)
   +p_2z(z-1)(z+\beta-3)+p_3z(z-1)(z-2).
\end{aligned}
```

 For noninteger $`\beta`$, the coefficient of $`x^n`$ in $`P(x)/(1-x)^\beta`$ is $`\Gamma(\beta+n-3)I(n)/(\Gamma(\beta)n!)`$. Here $`[z^3]I=P(1)>0`$ and $`I(0)=P(0)(\beta-1)(\beta-2)(\beta-3)`$. When $`2<\beta<3`$, $`I(0)>0`$ and $`I`$ has a negative real root, so its sampled coefficient sequence has at most two variations. The gamma quotient reverses only the initial sign. Four derivatives of $`x^\alpha P/(1-x)^\beta`$, for $`\alpha>\beta`$, consequently have at most three coefficient variations; the possible falling-factorial reversal when $`2<\alpha<3`$ only improves this count. When $`\beta>3`$, all multipliers are positive and a cubic has at most three variations. The power-series Descartes lemma and four Rolle steps give seven residual roots. At $`\beta=1`$, use directly the coefficient sequence $`p_0,p_0+p_1,p_0+p_1+p_2,P(1),P(1),\ldots`$ for every $`\alpha>0`$. The fourth-derivative falling factorials may change sign or vanish only at indices $`n=0,1,2`$. For $`n\ge3`$, $`\alpha+n>3`$ makes all factors positive, and $`P(1)>0`$ makes the entire tail positive. Three arbitrary initial coefficients followed by this positive tail have at most three sign variations. The power-series Descartes lemma and four Rolle steps therefore give seven scalar roots without an additional rectangle input. Integer $`\beta=2,3`$ follow by distinct-root regularization and perturbation. Thus $`B\ge2`$ and $`B=1`$ give eight original roots independently of $`A`$. Combining this with the contour and cofactor-stratum arguments proves the full original cut $`A\le4`$.

#### A zero-free operator for the remaining cuts.

Put $`\rho=x(1-x)`$, $`D_x=\rho\partial_x`$. For an anchor $`r=(C,-F)`$, let $`v=C-(C-F)x>0`$, $`\theta=C/(C-F)`$, and

```math
\mathcal L_{\theta,k}y=\rho y''+k(\theta-x)y'+ky,
 \qquad\mu=v^2x^{k\theta}(1-x)^{k(1-\theta)}>0.
```

 For arbitrary real $`k`$,

```math
\mathcal L_{\theta,k}y
           =\frac{\rho v}{\mu}[\mu(y/v)']'.
```

 Thus $`F\mapsto(D_x-v)F\mapsto\rho\mathcal L_{\theta,k}[(D_x-v)F]`$ loses at most three zeros, annihilates the anchor atom and constant, and leaves two atoms. For a surviving support $`s=(U,V)`$, put $`\lambda=U-(U+V)x`$, $`\ell=\lambda-v`$. Its degree-three core is

```math
\begin{aligned}
 C_s={}&(\lambda^2-\rho'\lambda+\rho\lambda')\ell
           +2\rho\lambda\ell'\\
 &+k(\theta-x)(\lambda\ell+\rho\ell')+k\rho\ell,
\end{aligned}
```

 with endpoints $`C_s(0)=U(U-C)[U-1+k\theta]`$ and $`C_s(1)=-V(V+F)[V-1+k(1-\theta)]`$, and leading coefficient $`-(U+V)(U+V-C+F)(U+V+1+k)`$. The retained polynomial–beta theorem gives at most seven distinct zeros to a nonidentity residual with cubic and quadratic cores. Common polynomial factors may be removed and their zeros added back; the bound does not increase. Negative signs at both residual endpoints give six simple roots at a regular ratio. Three Rolle losses and positive original endpoint signs then give eight original simple roots. The retained external input is El-Hilany–Tavenas, *Counting positive intersection points of a trinomial and a $`t`$-nomial curves via Grothendieck’s dessin d’enfant*, arXiv:2409.01651v1, Theorem 1.3, at its nonidentity/common-factor scope.

#### The $`B\ge1`$ cut when $`f\le1`$.

The previous cuts leave $`A>4`$, $`1<B<2`$. Use anchor $`(c,-f)`$ and $`k=(1+b)/(1-\theta)`$, $`\theta=c/(c-f)>1`$. The positive atom core has the factor $`C_1=(1-x)\widehat C_1`$, $`\deg\widehat C_1\le2`$, giving

```math
R=A_1x^a(1-x)^{1-b}\widehat C_1-B_0x^e(1-x)^dC_2.
```

 At zero $`C_2(0)=e(e-c)(e-T_1)>0`$, $`T_1=1+c(1+b)/f>e`$, so $`R<0`$. At one the first atom dominates, because $`B>1`$, and $`f\widehat C_1(1)=N_1`$, where

```math
N_1=af(1-b)(1-b+f)-cb[1-b+(b-f)(b+3)]+2bf(b-f).
```

 The sign $`N_1<0`$ follows from three short decompositions. For $`b\le1`$,

```math
\begin{aligned}
-N_1={}&(c-a)f(1-b)(1-b+f)+c(1-b)(b-f)(1+f)\\
       &+b(b-f)[c(b+3)-2f].
\end{aligned}
```

 For $`b>1`$, put $`\delta=b-f`$. If $`\delta\le1`$,

```math
-N_1=af(b-1)(1-\delta)+b\delta[c(b+2)-2f]+bc(1-f);
```

 if $`\delta\ge1`$,

```math
\begin{aligned}
-N_1={}&(c-a)f(b-1)(\delta-1)\\
 &+\delta\{c[b^2+b+2+(b-1)(1-f)]-2bf\}.
\end{aligned}
```

 Every term is nonnegative and at least one is strict, including $`b=1`$, $`f=1`$ and $`\delta=1`$. Both endpoint signs of $`R`$ are negative, so the operator count above proves eight original roots.

#### A displayed source-pair location when $`f>1`$.

Now $`A>4`$, $`1<f<b<B<2`$. Real-cofactor and THREE sources are already covered. For the genuine nonreal pair of $`Q_{\rm raw}=H((a,-b),(e,d))=-e_3`$, its physical center is $`h>1`$. Here is the positive proof replacing the historical 246-monomial expansion. Write $`\Gamma=a-e`$, and put

```math
\begin{gathered}
 M=(b+d)(b+1-d),\quad L=\Gamma(2b+d-1)-3b(b+d),\\
 C=2b^2-2b\Gamma+b-2d^2+d,\quad q_{*}=\Gamma-b-d>0.
\end{gathered}
```

 If $`Q_{\rm raw}(1+y)=\sum_{i=0}^3c_iy^i`$, then

```math
c_0=bd(b+d),\quad c_1=Me-dL,\quad
 c_3=(e+\Gamma-b)(e+d)q_{*}>0.
```

 The remaining translated coefficient is

```math
c_2=-(b+d)e^2+Ce
             +d[3b^2-4b\Gamma+3bd+\Gamma^2-2\Gamma d+\Gamma].
```

 The real root is $`q\in(0,1)`$. With $`r=1-q`$, $`h_0=h-1`$, deflation gives

```math
c_1/c_3=h_0^2+\eta^2-2rh_0,\qquad
 \frac{c_2c_1-c_3c_0}{c_3^2}
                    =-2h_0[(r-h_0)^2+\eta^2].
```

 If $`c_1\le0`$, the first identity forces $`h_0>0`$. Otherwise use the onto chart $`T=1+u+v`$, $`b=1+u/T`$, $`d=v/T`$, $`\Gamma=4+g`$, with $`u,v>0`$, $`g\ge0`$. The identity

```math
T^2[4(2b+d-1)-3b(b+d)]=2uv+4u+2v^2+3v+1
```

 gives $`L>0`$, while $`C=-2bg-b(7-2b)+d-2d^2<-3+1/8<0`$. Put $`e_{*}=dL/M`$ and $`e=e_{*}+j`$, $`j>0`$. Then

```math
-(c_2c_1-c_3c_0)=\mathscr A_0+\mathscr A_1j
                         +\mathscr A_2j^2+\mathscr A_3j^3,
```

 where $`\mathscr A_0=c_3(e_{*})c_0>0`$, $`\mathscr A_2=2(b+d)dL-MC+q_{*}c_0>0`$, and $`\mathscr A_3=(b+d)M>0`$. The remaining coefficient factors as

```math
\mathscr A_1=
 \frac{v(2u+v+1)(gT+2u+2v+3)[gT\mathcal R+\mathcal S]}
                            {T^5(3u+v+2)}>0,
```

 with two positive polynomials

```math
\begin{aligned}
\mathcal R={}&15u^2+26uv+13u+12v^2+10v+2,\\
\mathcal S={}&12u^3+40u^2v+32u^2+46uv^2+64uv+16u\\
             &+18v^3+35v^2+13v.
\end{aligned}
```

 The second deflation identity now forces $`h_0>0`$, including $`g=0`$. These displayed identities prove the physical pair-location sign without an external positive-coefficient table.

#### One actual level closes the $`f>1`$ sector.

The monotone $`12`$ anchor leaves $`-e_3=(B_1/A_0)x^c(1-x)^{-f}e_0`$, with two Rolle losses. The fixed cubic $`P_{\rm raw}=e_0`$ has a direct source root-location proof. Set $`R_0=c-a>0`$, $`q_0=b-f>0`$, $`\theta_0=A/(A-B)>1`$. Its values at $`0,1,\theta_0`$, and its leading coefficient are

```math
\begin{gathered}
 -AR_0(A+R_0)<0,\qquad Bq_0(B-q_0)>0,\\
 -AB(Aq_0+R_0B)/(A-B)^2<0,\\
                 (A-B)(R_0+q_0)(A-B+R_0+q_0)>0.
\end{gathered}
```

 Thus it has three simple roots $`0<p<1<u<\theta_0<v`$, with $`v>1+1/c`$. After positive monic normalization the source equation has one actual level $`Q=\kappa x^c(1-x)^{-f}P`$, with $`\kappa>0`$, $`P=(x-p)(x-u)(x-v)`$ and $`Q=(x-q)[(x-h)^2+\eta^2]`$, $`h>1`$. For the deflated phase

```math
\Psi=\log\frac{(x-h)^2+\eta^2}{(u-x)(v-x)}
                  -c\log x+f\log(1-x),
```

 the bounds $`1/(u-x)<1/(1-x)`$ and $`1/(v-x)<c/x`$ give

```math
\Psi'<\frac{2(x-h)}{(x-h)^2+\eta^2}-\frac{f-1}{1-x}<0.
```

 If $`p<q`$, every value of $`\phi=\Psi+\log|(x-q)/(x-p)|`$ on $`(0,p)`$ exceeds every value on $`(q,1)`$. Hence a single level occupies at most one useful component. Its cleared derivative has degree at most seven and negative endpoint signs, so at most six physical critical weights. Rolle and equal endpoint directions give at most six regular level intersections in the occupied component. If $`q<p`$, both useful phases decrease and give at most two solutions. If $`p=q`$, remove the common root and use $`\Psi'<0`$, again giving at most two including that root. The residual bound six and two original losses give eight. Together with the preceding cuts, this exhausts $`B\ge1`$.

#### The determinant cut.

Use anchor $`(a,-b)`$, $`\theta=a/(a-b)`$ and $`k=-(c-f)-1`$. The leading coefficient formula gives $`\deg C_3\le2`$, while $`\deg C_2\le3`$, and the residual is $`R=-B_0m_2C_2-B_1m_3C_3`$. At zero $`m_2`$ dominates and $`C_2(0)=e(e-a)(e-T_1)>0`$, $`T_1=1+a(c-f+1)/(a-b)>e`$. At one $`m_3`$ dominates, and

```math
C_3(1)=\frac{f(b-f)}{a-b}[bc-af-a+2b]>0.
```

 Thus the strict determinant inequality gives negative residual endpoint signs and the same cubic/quadratic, three-loss and parity count eight. At equality, increasing $`c`$ slightly makes the inequality strict while preserving oriented II and the original brackets.

#### Original distinct-root and support transfer.

Choose one noncritical shift of $`A_0`$ before a support perturbation. It preserves the prescribed coefficient signs and retains at least the selected number of original distinct roots in compact sign-changing brackets. At integer $`A=1,2,3,4`$, a sufficiently small decrease of $`a`$ enters a proved interpolation strip while leaving $`Q_{\rm raw}`$ unchanged and preserving all strict source ranks. Analogous proved-side support changes handle the other equality faces; the original brackets persist. For operator routes $`A_0`$ is annihilated, so a subsequent smaller surviving coefficient-ratio change regularizes the residual while preserving the original brackets. Generic support changes avoid common-factor and cofactor-discriminant walls within the proved union. This proves an original distinct-root bound. It asserts no persistence of even contact weights at a cofactor or exponent seam.

## The allocation-free F3 THREE theorem

#### The allocation-free THREE theorem.

Let $`P=(x-p)(x-u)(x-v)`$ with $`0<p<1<u<v`$ and let $`Q=\prod_{i=1}^3(x-q_i)`$ with $`0<q_1<q_2<q_3<1`$, all disjoint. For $`\alpha>\beta>0`$, $`\kappa>0`$,

```math
Z_{(0,1)}\bigl(Q-\kappa x^\alpha(1-x)^{-\beta}P\bigr)\le6
```

 for distinct roots. The actual $`E_1`$ or $`E_3`$ three-physical-root source reduces to this statement with respectively $`(\alpha,\beta)=(a-e,b+d)`$ or $`(c-e,d+f)`$, and one fixed original coefficient ratio after positive monic normalization. Two monotone anchors then give original bound eight.

Here is the common budget replacing the old allocation list. Put

```math
\phi=\log|Q/P|-\alpha\log x+\beta\log(1-x),\quad
 T=\rho(Q'P-QP')+[(\alpha-\beta)x-\alpha]PQ,
 \quad\rho=x(1-x).
```

 The phase derivative is $`T/(\rho PQ)`$; $`T`$ has degree seven and a compulsory root between $`u,v`$, so at most six physical weights. The cumulative-residue variation lemma bounds its useful interval critical counts. Its tail sequence is

```math
2-\alpha,\quad2-\beta,\quad1-\beta,\quad-\beta.
```

 Because $`\alpha>\beta`$, a nonnegative initial block followed by this tail has at most three sign changes, including zero entries by deletion. This one comparison replaces the eleven exponent sign cells. For $`q_1<p<q_2`$, direct pole pairing makes the first two useful intervals decreasing and the last has at most three criticals: the level bound is $`1+1+4=6`$.

In the two extreme placements, a compulsory critical in a non-useful $`Q/Q`$ gap leaves five useful weights. Eight transverse level intersections would exhaust them and occupy all three components. For $`p<q_1`$ the first two components each have two level intersections and the last four. For $`p>q_2`$ the first has one, and both remaining components must have an extremum and five criticals in total. These conclusions use the budget and endpoint signs, not a list of possible allocations.

Remove the adjacent $`P/Q`$ pair $`p,s`$ and put

```math
H_{*} =\log|\widetilde Q/\widetilde P|
                  -\alpha\log x+\beta\log(1-x),
 \quad\widetilde P=P/(x-p),\quad\widetilde Q=Q/(x-s).
```

 Its critical numerator $`N`$ is quintic and

```math
T=(x-p)(x-s)N+(s-p)\rho\widetilde P\widetilde Q.
```

 Extrema on the two sides of the adjacent gap lie on opposite sides of the same level. Removing the singular logarithm forces two roots of $`N`$ between them; the fixed signs force its other three, exhausting the quintic. Positive/negative residue pairing then bounds the remaining phase contacts. The left adjacent gap leaves at most one contact on the component that needed three. At the right gap, for either orientation, the two simultaneous bounds sum to at most three where five were needed. Poles with the same residue are one packet; their internal order does not generate six separate interleaving cases. This excludes eight. The residual has negative endpoint signs; aggregate level regularization excludes seven distinct roots as well.

## Two F3 exclusions using adjacent coefficients

Exact finite sums: [first adjacent identity](../calculation-data/f3/1320-first-adjacent.json) and [second adjacent identity](../calculation-data/f3/1320-second-adjacent.json).

Here is the actual-source construction used in (AH1)–(AH2). Retain the strict canonical oriented-II source (19)–(20), with four distinct simple physical cofactor roots in event order $`1320`$. At the $`E_2`$ physical root $`x`$, put $`h=1-x`$ and $`t_2=x/h`$. The complete source chart is

```math
\begin{aligned}
 a&=\frac{L(h+k)}h,&b&=\frac{L(x-k)}x,\\
 c&=\frac{(L+G)(h+k+G)}h,&f&=\frac{(L+G)(x-k-G)}x,\\
 e&=\frac Eh,&d&=\frac{P+E}x.
\end{aligned}
```

 To see its source binding, take $`L=ah+bx`$ and $`k=xh(a-b)/L`$. The $`E_2`$ root equation gives the positive score gap $`G=(ch+fx)-(ah+bx)`$ and $`k+G=xh(c-f)/(L+G)`$. Solving these score and exponent-sum relations gives the four displayed $`a,b,c,f`$ formulas. Set $`E=eh>0`$. The second atom’s mode precedes the unique physical $`E_3`$ root, so event order $`1320`$ implies $`P=dx-eh>0`$. The strict original source order and cofactor sign at $`E_2`$ give

```math
H_1=Lk-Ph-E>0,\qquad H_3=P(L+P-k-h)-E>0.
```

 Moreover $`r=x-k-G>0`$ follows from $`f>0`$, and $`x(b-f)=G(L-r)>0`$ gives $`z=L-r>0`$. Thus the single positive chart

```math
r,G,k,P,h,z,E>0,\qquad x=r+k+G,\quad L=r+z
```

 covers every source in the theorem, with no $`P/k`$ comparison.

For $`w=t/t_2-1`$, the literal normalized scores are

```math
\Lambda_1=L+L(x-k)w,\quad
 \Lambda_2=-P-(P+E)w,\quad
 \Lambda_3=L+G+(L+G)(x-k-G)w.
```

 With $`(T_1,T_2,T_3)=(Lk,Ph+E,(L+G)(k+G))`$, set

```math
R_{2,i}=\Lambda_i^2-T_i(1+w),\qquad
 R_{3,i}=\Lambda_i^3-3T_i(1+w)\Lambda_i
                 -T_i(1+w)(1-2x-xw).
```

 These rows are exact beta-jet identities, and

```math
\sum_{i=0}^6c_iw^i
 =\frac{\det(\Lambda,R_2,R_3)}{GL(L+G)}
 =\frac{h^6\widehat K(t_2(1+w))}{GL(L+G)}.
```

 All clearing factors are strictly positive. The odds coordinate $`w>0`$ is precisely the physical interval after $`E_2`$, and it preserves root multiplicity. The endpoint identities are

```math
\begin{aligned}
 c_0&=-(z+k+1-r)H_3,\\
 c_1/H_3&=(r-1)(3G+3r+1)-Gk-k^2-4k-P(k+1-r)\\
 &\quad-z^2-z(3G+P+2k+4r+2),\\
 c_6&=-z(E+P)(r+G)r\{E+P+L(r+G)\}\{E+P+(L+G)r\}.
\end{aligned}
```

 Since $`0<r<x<1`$, every displayed coefficient is strictly negative. The original cofactor witnesses

```math
F_1=-(\Lambda_2R_{2,3}-\Lambda_3R_{2,2}),\qquad
 F_3=\Lambda_1R_{2,2}-\Lambda_2R_{2,1}
```

 have values $`(L+G)H_3`$ and $`LH_3`$ at $`w=0`$. Their unique simple physical roots precede $`E_2`$, so they are strictly positive for all $`w>0`$. Only $`F_1(1/2)/(L+G)>0`$ and $`F_3(1)/L>0`$ are used by the two coefficient identities. These are two auxiliary values in addition to the stated parameter upper bounds, rather than six values at $`1/2,1,2`$. This argument uses no nonreal-pair hypothesis.

Put $`h_0=x+h`$, equal to one on the physical source. Give weight one to $`r,G,k,P,h,z`$ and weight two to $`E`$, and homogenize $`c_i`$ to weighted degree $`i+3`$, writing $`C_i`$. The source generators include

```math
\begin{gathered}
 B_{\rm lower bound}=xh_0-E-Ph_0-L(r+G)>0,\qquad L-r=z>0,\\
 \mathcal G_T=P[L(h+k)-hh_0]+E(L-h_0-x)\ge0,\\
                  \mathcal G_A=L(h+k)-E-4hh_0\ge0.
\end{gathered}
```

 At $`h_0=1`$, these weak inequalities are exactly $`xhG_T`$ and $`h(A-4)`$. Together with $`E,H_1,H_3`$ and the required strict cofactor witness, they are nonnegative at every actual source under consideration. Assuming $`C_2\ge0`$, $`-C_3\ge0`$, the degree-six identity expresses zero as 373 positive rational monomial-generator terms. Their plain source-monomial coefficients sum to one, so a strictly positive term survives without strictness of either weak inequality. This proves (AH1), including $`A=4`$, $`G_T=0`$ and $`P=k`$.

For (AH2), literal substitution gives

```math
bc-af=\frac{L(L+G)G}{xh},\qquad
 a-2b=\frac{L[(x+2h)k-xh]}{xh}.
```

 The original-cut complement is therefore exactly

```math
D=(x+2h)k-xh-(L+G)G>0.
```

 The extra low-degree primitives are

```math
T_{\rm ord}=2k-G,\quad N=L+P-k-h,\quad V=x-P,
 \quad U=k(x+4h)-3xh-E-P(h+k).
```

 They are strictly positive by the exact identities

```math
\begin{aligned}
 h_0T_{\rm ord}&=D+k(h_0-G)+rh+zG,\\
 PN&=H_3+E,\\
 h_0V&=B_{\rm lower bound}+E+L(r+G),\\
 h_0U&=(r+G)\mathcal G_A+(h+k)B_{\rm lower bound}.
\end{aligned}
```

 Here $`h_0-G=r+k+h>0`$; the last line retains strictness even at $`A=4`$. There is no stronger assumption $`k>G`$.

If $`C_3\ge0`$, $`-C_4\ge0`$, the new weighted-degree-eight identity is

```math
-rGkPhzE=\sum_{\nu=1}^{1302}q_\nu M_\nu\Gamma_\nu,
                       \qquad q_\nu>0.
```

 Each $`M_\nu`$ is a monomial in the positive chart variables. Each $`\Gamma_\nu`$ is one, a displayed source generator or the single finite witness $`F_3(1)/L`$, a nonnegative product of source generators, an alleged coefficient inequality, or its product with a source generator. Every term is nonnegative, but the left side is strictly negative. This proves (AH2) and survives $`A=4`$, $`G_T=0`$ and $`P=k`$. Homogenization is evaluated at the same source with $`h_0=1`$; it does not assert that arbitrary homogeneous points are beta supports. The witness occurs in 21 multiplier records; no other finite cofactor value occurs in this identity.

The exact adjacent-coefficient identities are the two linked finite sums at the start of this subsection.

The identities use the original beta derivative recurrence. The three-way coefficient argument in the main proof gives the Descartes bound after zero coefficients are omitted. The separate analytic left-contact bound remains an input.

## Two coefficient cases for F3 event order 0231

Exact finite sums: [third coefficient](../calculation-data/f3/0231-third-head.json), [fourth coefficient](../calculation-data/f3/0231-fourth-head.json), and [last fourth-coefficient case](../calculation-data/f3/0231-terminal-fourth-head.json).

This subsection retains the actual strict canonical oriented-II source (19)–(20), four distinct simple cofactor events in event order $`0231`$, and both variable extra pairs genuinely nonreal. Write the exponent gaps $`A_{\rm gap}=a-e`$, $`B_{\rm gap}=b+d`$ to distinguish them from the historical coefficient families A/B/C. At the original-proof use,

```math
A_{\rm gap}>4,\quad B_{\rm gap}<1,\quad
                    a-2b-(bc-af)>0.
```

 In particular $`d<1`$. All three coefficient theorems permit the weak seams $`A_{\rm gap}=4`$, $`B_{\rm gap}=1`$ and $`a-2b-(bc-af)=0`$, under the same strict actual source context.

#### Literal source and positive normalization.

Let $`T`$ be the last physical event, the $`E_1`$ root, and put $`x=T/(1+T)`$, $`y=1-x`$ and $`w=(t-T)/(1+T)=yt-x`$. Physical points before $`T`$ have $`-x<w<0`$; the right tail is $`w>0`$. Use the complete last-$`E_1`$ chart

```math
x=P+r+v,\qquad L=1-P-r+\ell,\qquad V=1-r+\ell=L+P,
```



```math
\begin{aligned}
 b&=\frac{Lr+V\eta}{x},&d&=\frac{P(1+\ell)}x,\\
 a&=\frac{xL(1-r)+V(y\eta-\lambda)}{xy},&e&=\frac{P\ell}y,\\
 c&=\frac{L(1-r)}y,&f&=\frac{Lr}x.
\end{aligned}
```

 Its positive variables satisfy $`\lambda<v`$, $`\lambda>y\eta`$. The inverse source bindings are $`P=dx-ey`$, $`L=cy+fx`$, $`\ell=ey/P`$, $`r=fx/L`$, $`\eta=x(b-f)/V`$, $`\lambda=y\eta+xy(c-a)/V`$ and $`v-\lambda=xy(a-b-e-d)/V`$. The $`E_1`$ root equation supplies $`L=1-P-r+\ell`$. Thus this is a chart of the linked beta source, not a choice of independent cofactor polynomials. Set

```math
\begin{aligned}
 Y&=\ell+r-v>0,\\
 G&=(\eta-\lambda)[x(V+v)+V(\eta-\lambda)]+x^2\lambda>0,\\
 C&=x(P+2r)\ell+r(P+r)(1+x)-v(P+v),\\
 \Delta_{E_1}&=4x^2Y(1+\ell)(P+r)r-C^2>0.
\end{aligned}
```

 $`Y`$ and $`\Delta_{E_1}`$ come from the genuinely nonreal deflated $`E_1`$ quadratic, and $`G`$ is the correctly signed source $`E_3`$ value at the last event. The actual $`d<1`$ inequality is $`r+v-P\ell>0`$. Divide the primitive beta-score/second/third-jet determinant by $`PLV^2>0`$ and write the resulting sextic as $`\sum_{i=0}^6q_iw^i`$. The literal endpoint identities are

```math
q_0=x^4YG>0,\qquad
 q_6=-r(1+\ell)(Lr+V\eta)\eta V(P+r+\eta)(P+r)<0.
```

 The normalization preserves every coefficient sign and root multiplicity.

#### Root exhaustion, Vieta and one strict height inequality.

Suppose five positive-$`w`$ roots exist, counting multiplicity. The left theorem gives one simple physical contact before all events. These six roots exhaust the sextic degree, so its only negative root is $`-u`$, with $`0<u<x`$, and

```math
K(w)/q_0=(1+w/u)\prod_{i=1}^{5}(1-s_iw),
                       \qquad s_i>0.
```

 The $`s_i`$ may repeat. Write $`e_j`$ for their elementary symmetric functions. Vieta gives

```math
q_1/q_0=1/u-e_1,\qquad q_2/q_0=e_2-e_1/u.
```

 If $`q_2\ge0`$, then $`e_2/e_1\ge1/u`$. Newton’s inequality gives $`e_2/e_1\le2e_1/5`$, and hence

```math
q_1/q_0=1/u-e_1\le-3/(2u)<-3/(2x).
```

 This supplies the strict height-five-halves inequality

```math
H_{5/2}=Y[x(L-5/2-v)+V(\eta-\lambda)]-2C>0.
```

 The exact source bridge is $`xq_1+(3/2)q_0+x^3GH_{5/2}=0`$. Strictness comes from the physical location $`u<x`$, including $`q_2=0`$; coefficient-zero faces and repeated right roots cause no loss.

#### Paired degree-eight coefficients at the common height.

At the same actual source, retain

```math
d<1,\quad A_{\rm gap}\ge4,\quad B_{\rm gap}\le1,\quad
 a-2b-(bc-af)\ge0,\quad q_2\ge0,\quad H_{5/2}>0.
```

 Then $`q_3>0`$ and $`q_4>0`$. Each coefficient has its own exact identity; neither assumes the sign of the other coefficient. No $`q_1`$ or $`q_5`$ sign premise is used.

For the identities, homogenize in seven positive variables $`P,r,\lambda,\mu,\ell,\eta,\rho`$, with $`v=\lambda+\mu`$, $`h=P+r+\lambda+\mu+\rho`$, $`x=h-\rho`$. The physical normalization is $`h=1`$, $`\rho=y`$. Each normalized coefficient $`q_j`$ has homogeneous degree eight. Let $`a_n=xL(1-r)+V(y\eta-\lambda)`$ and $`b_n=Lr+V\eta`$. At this normalization the cut inequalities are

```math
\begin{aligned}
 T_B&=x-b_n-P(1+\ell)=x(1-B_{\rm gap})\ge0,\\
 A_4&=a_n-xP\ell-4xy=xy(A_{\rm gap}-4)\ge0,\\
 \mathcal D&=a_n(x+Lr)-b_nx[2y+L(1-r)]\\
            &=x^2y[a-2b-(bc-af)]\ge0.
\end{aligned}
```

 All clearing factors are strictly positive. Write $`\delta_1`$ for the homogeneous $`r+v-P\ell`$ inequality and $`c_a`$ for the homogeneous $`\lambda-y\eta`$ inequality. The strict $`d<1`$ and $`c>a`$ source hypotheses make these positive.

The existing genuinely nonreal $`E_1`$ pair supplies the strict inequality $`\Delta_{E_1}>0`$. In this jet normalization its original cofactor numerator is exactly

```math
\mathcal E_1=wPLV\{x^2Y+Cw+A_qw^2\},\qquad
                    A_q=(1+\ell)(P+r)r>0.
```

 After removal of the simple anchor root, the remaining quadratic has negative discriminant, precisely $`\Delta_{E_1}=4x^2YA_q-C^2>0`$. The $`q_3`$ identity uses this inequality in two multiplier records, and the $`q_4`$ identity in three. These are five uses of an existing strict source hypothesis, rather than a new premise. The $`E_3`$ nonreal pair remains part of the left-contact/root-exhaustion context. No negative evaluation of $`E_3`$ is used by either identity.

The shared base inequalities are

```math
\mathcal G=\{T_B,Y,\delta_1,c_a,G,\Delta_{E_1},
                         A_4,\mathcal D,q_2,H_{5/2}\}.
```

 The eight product inequalities for the fourth coefficient are

```math
\begin{aligned}
\mathcal P_4=\{&YH_{5/2},GH_{5/2},c_aH_{5/2},\delta_1H_{5/2},\\
              &A_4Y,A_4c_a,Gc_a,A_4G\},
\end{aligned}
```

 and the nine for the third coefficient are $`\mathcal P_3=\mathcal P_4\cup\{A_4\delta_1\}`$. Every product follows from its already stated factor signs and introduces no additional source restriction. For $`j=3,4`$, the source identity is the homogeneous *degree-eight* equality

```math
0=-m_jq_j+\sum_{g\in\mathcal G}gM_{j,g}
                    +\sum_{p\in\mathcal P_j}pM_{j,p}+R_j,
                  \qquad m_j>0.
```

 Here $`m_j`$ is one positive integer constant, all multiplier coefficients are nonnegative integers, and every remainder coefficient is strictly positive. For $`q_3`$ there are 869 positive multiplier and 1,116 positive remainder records, totaling 1,985. For $`q_4`$ there are 721 and 1,275, totaling 1,996. On the positive chart the remainders are strictly positive, while every source or product summand is nonnegative. Thus both equalities force $`q_j>0`$.

This includes $`A_{\rm gap}=4`$, $`B_{\rm gap}=1`$, $`\mathcal D=0`$ and $`q_2=0`$: the remainders remain strict when those inequalities vanish. Actual source-coordinate positivity, distinct simple cofactor events and genuinely nonreal pairs remain strict; no cofactor collision or discriminant-zero extension is asserted.

#### The terminal fourth coefficient without a height premise.

At the same actual strict source, retain the three original-cut inequalities and $`d<1`$, but now assume only

```math
q_2\le0,\qquad q_3\ge0,\qquad q_5\ge0.
```

 Then $`q_4>0`$. No $`q_1`$ or $`q_4`$ sign and no height inequality is assumed. Use the same positive homogeneous chart, normalized $`q_j`$ and parameter inequalities above. Put

```math
\mathcal S=\{T_B,Y,\delta_1,c_a,G,\Delta_{E_1},A_4,\mathcal D\}.
```

 The exact homogeneous degree-ten identity is

```math
0=(-q_4)M_4+\sum_{g\in\mathcal S}gM_g
                   +(-q_2)M_2+q_3M_3+q_5M_5+R.
```

 All multipliers have nonnegative integer coefficients. The target $`M_4`$ is a quadratic polynomial with 26 positive monomial records, so $`M_4>0`$ everywhere on the positive chart. The nonzero remainder $`R`$ has only strictly positive coefficients. There are 686 positive multiplier records and 5,067 positive remainder records, totaling 5,753. Every term other than $`(-q_4)M_4`$ is nonnegative, and $`R>0`$. Therefore $`(-q_4)M_4<0`$, proving $`q_4>0`$ without coefficient division.

This identity uses the existing strict $`\Delta_{E_1}`$ inequality in 36 multiplier records. Together with the paired coefficients’ two and three uses, these are 41 uses of the same nonreal-$`E_1`$ source premise. There are no product inequalities, height generators or negative-$`E_3`$ evaluation generators in the terminal identity. The actual nonreal $`E_3`$ pair remains in the surrounding left-contact context. The proof includes $`q_2=0,q_3=0,q_5=0`$ and the three weak cut seams: strictness of $`M_4`$ and $`R`$ is unaffected when those inequalities vanish. It retains strict source coordinates, distinct simple events and genuinely nonreal pairs.

#### Two cases instead of the eleven-word table.

Five positive roots force exactly five Descartes variations: the endpoint signs are opposite, so the variation count is odd and at most five. Delete zero coefficients in this count. If $`q_2\ge0`$, the Newton argument gives $`H_{5/2}>0`$. The two source lemmas at this single height force $`q_3>0,q_4>0`$. After deleting any zero $`q_2`$, the segment $`q_0\to q_4`$ has at most two variations: only $`q_1`$ can separate its positive coefficients. The segment $`q_4\to q_6`$ has at most one variation. The total is therefore at most three. This contradicts five right roots, including the $`q_2=0`$ face.

If $`q_2<0`$, the first portion $`q_0\to q_2`$ has at most one variation, including $`q_1=0`$. The four remaining edges must all vary, so $`q_3>0,q_4<0,q_5>0`$. The terminal theorem, under the weaker nonnegative coefficient inequalities just stated, gives $`q_4>0`$, a contradiction. No height or $`b>1`$ conclusion enters this branch. Every coefficient-zero face is covered by this argument.

#### Local master conclusion and exact proof inventory.

With the retained one-simple-physical-left theorem, the source conditions and original-cut inequalities stated above imply right-root multiplicity at most three and joint useful multiplicity at most four. Indeed the left root leaves at most five right roots by degree six. Since $`q_0>0`$ and $`q_6<0`$, positive-root multiplicity is odd. The two branches exclude five, so it is at most three. This conclusion retains the fixed-root interlacing input for the left contact. It is not an unrestricted all-source F3 theorem.

The argument has two cases according to the sign of $`q_2`$, one common-height comparison, and three exact positive-sum identities. It proves the required bound under the source assumptions printed above.

## The first two Newton inequalities in F3

Exact finite sums: [nonpositive-height identity](../calculation-data/f3/1320-low-height.json), [derivative sign](../calculation-data/f3/1320-derivative-gap.json), and [cubic coefficient gap](../calculation-data/f3/1320-cubic-gap.json).

For [F3-NEWTON], the exact rational shape chart is

```math
y>q>0,\quad r>p>0,\quad -pq<M<\min(pr,qy),\quad\lambda>M+yr>0,
```



```math
a=y+p,\quad e=y-q,\quad c=y+r,\qquad
 b=\frac{a(M+qr)}\lambda,\quad
 d=\frac{e(pr-M)}\lambda,\quad f=\frac{c(M+pq)}\lambda.
```

 These chart letters are support spacings. They are distinct from similarly named beta differences in other local notation. Put

```math
\begin{gathered}
 A=p+q,\quad T=Ay+(A-1)p,\quad W=rT,\quad P=pqr,\quad Y=yP,\\
 D_{*}=P+y[pr-q(p+r)],\quad\Delta=p+r-q-y,\quad h=\Delta-3,\\
 Z=(y+1)(y+\Delta-1)-[pr-q(p+r)].
\end{gathered}
```

 Here the Newton coefficients $`k_i`$ are the coefficients of $`\widehat K(t)`$ in the odds coordinate defined in the main theorem; an overall source normalization does not change their ratios. Then $`B=b+d=A(M+yr)/\lambda`$ and $`G_T/e=(M+W)/\lambda-2`$ exactly. Literal source jets give $`c_i=\lambda^ik_i/k_0`$ and

**(A6)**

```math
\begin{aligned}
 H=c_1&=6M+Z,\\
 c_2&=h\lambda+15M^2+M(5Z-2h)-hD_{*}-Y,\\
 c_3&=20M^3+(10Z-7h-9)M^2-[(4h+6)D_{*}+4Y]M\\
 &\quad-D_{*}^2-Y(h^2+h-2+2Z)+3(\Delta M+D_{*})\lambda-2\lambda^2.
\end{aligned}
```

 The lower bound $`\lambda>M+yr`$ is exactly the strict sum inequality $`a-b>e+d`$ in this canonical chart. The qualified both-nonreal event order $`1320`$ bridge supplies $`pr>qy`$, $`D_\lambda=M^2+MD_{*}+Y(\Delta-1)>0`$ and

```math
\lambda<\lambda_+=2M+D_{*}+\frac{D_\lambda}{s-M},\qquad s=\sqrt Y.
```

 The necessary first coefficient $`H<0`$ also gives $`\Delta>0`$ by the general positive-$`\Delta`$ source inequality. These are physical-word and nonreal-pair necessities, not consequences of the bare shape chart.

#### A displayed integer proof when $`Z\le0`$.

Let $`d_{*}=p-q`$. The elementary shape identities for $`Z`$ exclude $`d_{*}\le0`$, $`0<d_{*}\le1`$ and $`1<d_{*}\le y+1`$, since each makes $`Z>0`$. Thus $`v=d_{*}-y-1>0`$. Put $`E=y-q>0`$, $`z=-Z\ge0`$, $`S=2q+E`$. The full substitution is

```math
y=q+E,\quad p=2q+E+1+v,\quad
 r=\frac{(y+1)(y+v)+pq+z}{v}.
```

 For $`\ell_{*}=A-2\ge0`$, the identities

```math
vh=v(v-1)+(2q+E)v+3q^2+3qE+E^2+2q+E+z
```

 and, for $`v\le1`$,

```math
3vh=E^2+E\ell_{*}+2E+\ell_{*}^2+4\ell_{*}
                         +2(1-v)^2+(1-v)+3z>0
```

 prove $`h>0`$; the first is strictly positive when $`v\ge1`$. Define

```math
E_{GT}=5Z^2+12Y+12hD_{*}-6hW-3hZ.
```

 The exact integer identity is

**(A7)**

```math
-v^2E_{GT}=R_{\mathrm{new}}
 +6v^3\left[\left(v+\frac32S\right)^2-1
                         +Sv^2+\frac{11}{4}S^2\right].
```

 Here $`v+3S/2=A-1+E/2>1`$. To display the whole remainder compactly, put

```math
\begin{aligned}
 F_0&=E^2+3Eq+E+3q^2+2q,\\
 B_0&=E(E+1)^2+q(11E^2+7E+2)+q^2(27E+7)+18q^3,\\
 C_0&=3E^2(E+1)^2+qE(E+1)(26E+5)\\
 &\quad+q^2(80E^2+57E+5)+2q^3(54E+19)+54q^4,\\
 D_0&=E(E+1)(4E+3)+q(32E^2+25E+6)+q^2(72E+25)+48q^3.
\end{aligned}
```

 All are strictly positive. The complete thirteen-group expansion is $`R_{\mathrm{new}}=\sum a_{ij}v^iz^j`$ with precisely

| $`i`$ | $`j`$ | $`a_{ij}`$                      |
|----:|----:|:------------------------------|
|   4 |   1 | $`6`$                           |
|   4 |   0 | $`6(3E^2+13Eq+13q^2)`$          |
|   3 |   1 | $`3(6E+12q+1)`$                 |
|   3 |   0 | $`12(E+2q)(E+3q)(2E+3q)`$       |
|   2 |   2 | $`1`$                           |
|   2 |   1 | $`3(8E^2+34Eq+7E+34q^2+14q+1)`$ |
|   2 |   0 | $`6C_0`$                        |
|   1 |   2 | $`3(2E+4q+1)`$                  |
|   1 |   1 | $`3D_0`$                        |
|   1 |   0 | $`6F_0B_0`$                     |
|   0 |   2 | $`18q(E+q)`$                    |
|   0 |   1 | $`36q(E+q)F_0`$                 |
|   0 |   0 | $`18q(E+q)F_0^2`$               |

Thus (A7) is strictly positive even at $`z=0`$ and $`A=2`$, proving $`E_{GT}<0`$. The literal coefficient identity

```math
N_1=E_{GT}-6h(2\lambda-M-W)+3h(6M+Z)
```

 and $`G_T\le0`$, $`H<0`$ give $`N_1<E_{GT}<0`$. This entire local certificate is printed here as positive coefficients and one square; no computer-algebra package is needed to check its expansion. Its thirteen-group source is the accompanying mathematical proof.

#### The positive-$`Z`$, low-$`\Delta`$ bridge.

Now $`Z>0`$ and $`H<0`$ give $`M=-m<0`$, $`Z/6<m<pq`$. Suppose $`0<\Delta\le3`$, so $`h\le0`$. The first cofactor is a nonzero negative multiple of

```math
F_1(u)=[1-(pr-M)u][1+(M+pq)u][1+(M+py)u]+pu(1+\lambda u).
```

 At $`u_{*}=1/(s-M)`$ it equals $`p(\lambda-\lambda_+)/(s-M)^2<0`$. Its nonreal extra pair leaves exactly one positive root, which is therefore below $`u_{*}`$. Since $`pr>qy`$ implies $`s>qy`$, $`\tau=1/(qy-M)>u_{*}`$, hence $`F_1(\tau)<0`$. Writing $`v_{*}=qy+m`$, direct evaluation yields

```math
v_{*}^3F_1(\tau)=p(\lambda+v_{*})v_{*}-(pr-qy)qy(y+p)A.
```

 Combine this strict upper bound on $`\lambda`$ with $`\lambda\ge\lambda_G=(M+W)/2`$ to obtain

**(A8)**

```math
T_G=2(pr-qy)qy(y+p)A
                 -p(qy+m)[-m+W+2qy+2m]>0.
```

 As $`h\le0`$, $`c_2(\lambda)\le c_2(\lambda_G)=C_{2G}`$, where

```math
C_{2G}=15m^2-m(5Z-3h/2)-hD_{*}-Y+hW/2.
```

 The exact table expresses $`-2C_{2G}`$ as 297 positive rational products of the fourteen generators

```math
p,q,r-p,y-q,m,A-2,\Delta,3-\Delta,
                         pq-m,6m-Z,Z,pr-qy,D_\lambda,T_G.
```

 Only $`A-2`$, $`3-\Delta`$ may vanish; 77 products avoid both and remain strictly positive. Thus $`c_2<0`$, contradicting the necessary second coefficient. A hypothetical six-positive-root source must therefore have $`h>0`$.

#### The two-Newton contradiction when $`h>0`$.

In this cone, $`N_1\ge0`$ and $`\lambda\ge\lambda_G`$ force

```math
Q_{GN}=5Z^2+12Y+12hD_{*}-18hm-6hW\ge0.
```

 The thirteen generators are

```math
p,q,r-p,y-q,m,A-2,h,pq-m,6m-Z,Z,pr-qy,Q_{GN},D_\lambda.
```

 Only $`A-2,Q_{GN}`$ may vanish. Two exact positive-generator identities give

```math
D_{3G}=4\lambda_G-3(\Delta M+D_{*})>0,\qquad
 -54\left(c_3(\lambda_G)-\frac5{54}H^3\right)>0.
```

 They have respectively 29 and 283 positive rational products, with 21 and 145 strict products avoiding both weak generators. The source formula (A6) has $`c_3''=-4`$ and $`c_3'(\lambda_G)=-D_{3G}<0`$, so $`c_3(\lambda)\le c_3(\lambda_G)<5H^3/54`$. The exact Newton identity printed in the main proof gives the opposite inequality. Here $`k_0=K(0)`$ and $`k_6=K(1)`$ are negative in the retained literal orientation. Their same sign makes the total positive odds-root weight even and at most four. All polynomial tables are rational positive-product equalities with zero reconstructed remainder; optimization was used only to discover them.

This extends the the earlier argument no-$`B`$ $`A\ge4`$ theorem to $`A\ge2`$. Its original-proof use after (F3-CUT) remains within the unchanged qualified $`A\ge2`$, $`G_T\le0`$ theorem. The stronger original-root cuts provide all removed domains; they imply no contact cap there.

## Reciprocal-coordinate height and regional bounds

The F3 arguments also use the following height and root bounds. Each theorem states its parameter region and its polynomial hypotheses. The order-specific F3 arguments above provide the case coverage outside these regions.

The variables in this section are local. The parameters $`p,q,r,y,M,\lambda`$ are those of the rational F3 source chart in the preceding section. The quantity $`D`$ below is written $`D_{*}`$ in that section; the local definitions of $`T,W`$ differ from its similarly named quantities. The coefficients $`E_j`$ below refer to the translated polynomial $`R`$ defined here.

### Parameters and polynomials

Throughout the reciprocal-coordinate lemmas, the parameters satisfy

```math
y>q>0,\qquad r>p>0,\qquad -pq<M<\min(pr,qy).
```

The scale parameter is $`\lambda`$. Define

```math
\begin{aligned}
h&=p+r-q-y-3, &Y&=pqry,\\
D&=pr(q+y)-qy(p+r),
&Z&=(q+y+1)(p+r-1)-pr-qy,\\
T&=\lambda-2M-D, &W&=M(\lambda-M).
\end{aligned}
```

Here $`h`$ is a quantity in this particular change of variables. It is
not the height in every other section of the proof. Put

```math
s=\sqrt Y,\qquad S=q+y+1,\qquad \mu=-Z/6.
```

The four event polynomials are

```math
P_k(v)=(v^2-Y)(v+k^2)
 +k\{-(h+2)v^2+Tv-W\},
\qquad k\in\{p,r,-q,-y\}.
```

An **event** in this section means a real zero of one of these
polynomials with $`v>M`$. Thus the word describes an algebraic boundary
value, rather than a new geometric object. When each polynomial has
exactly one such zero, write it as

```math
\beta\ (P_p),\quad \gamma\ (P_r),\quad
\delta\ (P_{-q}),\quad \alpha\ (P_{-y}).
```

The two remaining orders considered here are

```math
\beta<\gamma<s<\delta<\alpha
\quad\text{and}\quad
\alpha<\delta<s<\gamma<\beta.
```

The calculation filenames call these orders `0231` and `1320`,
respectively. These labels are only abbreviations for the displayed
inequalities. We use the inequalities in the proofs.

The degree-six contact polynomial is

```math
R(v)=v^6+C_1v^5+C_2v^4+C_3v^3+C_4v^2+C_5v+C_6,
```

where

```math
\begin{aligned}
C_1={}&Z,\\
C_2={}&hT-Y,\\
C_3={}&(1-h)W-2T^2-DT-Y(h^2+h-2+2Z),\\
C_4={}&(5T+2D)W+Y(h+2)(3T+2D)-Y^2,\\
C_5={}&-3W^2-Y(3h+7)W-YT(T+D)+Y^2(Z-h-2),\\
C_6={}&Y(WT+Y^2).
\end{aligned}
```

Calling a zero of $`R`$ a **contact** agrees with the geometric
interpretation in the appendix. In this section a *physical* zero
simply means a real zero satisfying $`v>M`$. The identity

```math
R(M)=(M+qr)(pr-M)(M+pq)(M+yr)(qy-M)(M+py)>0
```

follows from the parameter inequalities. If all six zeros are real,
their mean is $`\mu`$, by the coefficient of $`v^5`$.

To state the necessary coefficient inequalities, expand

```math
R(M+x)=x^6-E_1x^5+E_2x^4-E_3x^3+E_4x^2-E_5x+E_6.
```

With $`C_0=1`$, this means

```math
E_j=(-1)^j\sum_{i=0}^j C_i
 {6-i\choose6-j}M^{j-i}.
```

If all six contacts are physical, each $`E_j`$ is a positive elementary
symmetric sum of their distances from $`M`$. Newton's inequalities for
these six positive distances include

```math
N_2:=8E_2^2-15E_1E_3\ge0,\qquad
N_3:=9E_3^2-16E_2E_4\ge0.
```

These are necessary inequalities. Assuming them alone does not assert
that $`R`$ has six physical roots.

### Height and regional lemmas

The table summarizes the premises; the full statements in the linked proofs govern their use.

| Lemma | Premises and conclusion | Complete proof |
| --- | --- | --- |
| Positive reciprocal height | With $`p+q>4`$, $`\lambda>(p+q)(M+yr)`$, $`E_1,E_2,E_3>0`$ and $`N_2,N_3\ge0`$, one has $`h>0`$. No event order, nonreal-pair assumption or sign of $`E_4`$ is required. | [Reciprocal height](lemmas/f3/reciprocal-height.md) |
| Exterior count from the sum of the roots | Suppose $`p>S`$, $`r\ge7p/4`$, $`\mu\ge s`$, and $`P_p`$ has one real root $`\beta>M`$, two nonreal conjugate roots, and $`\beta>s`$. Then $`\beta>3\mu-2M`$. For $`\alpha<\delta<s<\gamma<\beta`$, if also $`R(\alpha),R(\beta)>0`$, the total contact multiplicity in $`(M,\alpha)\cup(\beta,\infty)`$ is at most four. | [Exterior root bound](lemmas/f3/exterior-root-bound.md) |
| Shape exclusions | Suppose $`P_p`$ has one real root and two nonreal conjugate roots, $`V:=sT-W-(h+2)Y>0`$, and $`N_1:=5Z^2-12hT+12Y\ge0`$. The regions $`(p\ge5S/2,\ r\ge p)`$, $`(p\ge2S,\ r\ge2p)`$, $`(p\ge S,\ r\ge3p)`$ and $`(p\le S,\ pr\ge3S^2)`$ are impossible. In particular, $`r\ge3p`$ and $`pr\ge3S^2`$ is impossible. These hypotheses apply to the order $`\beta<\gamma<s<\delta<\alpha`$ considered in the proof. | [Shape exclusions](lemmas/f3/shape-exclusions.md) |

The reciprocal-height lemma uses the first two translated Newton inequalities and the scale bounds to exclude $`h\le0`$. The exterior-root lemma uses an analytical barrier for the real cubic root, then contradicts the sum of six exterior contacts. The shape exclusions use one common root argument and exact positive coefficient expansions for the four listed regions. Their exact identities and coefficient data are described in [the calculation guide](calculations.md#tables-for-the-reciprocal-coordinate-lemmas).

Apply each lemma only after establishing its premises. A region-specific result does not exclude an entire event order. The preceding F3 coefficient arguments remain applicable for every parameter configuration outside the listed regions.
