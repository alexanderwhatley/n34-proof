# Strict central-contact orientation in the rightmost-u region

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## 1. Statement, notation and source dependencies

Retain the actual original row

```math
G=c_1-u+c_3v+c_4w,\qquad c_1,c_3,c_4\gt0,
\qquad 0\prec\operatorname{supp}u\prec\operatorname{supp}v
\prec\operatorname{supp}w,
```

with beta functions on $`0\lt x\lt1`$, $`q=w/v`$, and

```math
u=v^h q^{-m},\qquad H=1-h,\qquad
0\lt h\lt1,\quad 0\lt m\lt H.
```

In the reflected projective chart, write

```math
p=L_v/L_q,\quad \Pi=\lambda\prod_{i=1}^3(p-r_i),\qquad
\lambda\gt0,\quad m/h\lt r_1\lt r_2\lt r_3.
```

The right original branch is $`p\lt r_1`$, with $`\Pi\lt0`$, and p increases
with x. Use the unchanged polynomials

**(1)**

```math
\begin{aligned}
T&=hp-m,& C&=p(p+1)-\Pi,\\
E&=-Hhp^2+2Hmp+m(m+1),&D&=HC+E,\\
A&=-mC+pE,&B&=(h+m)C-(p+1)E,\\
J&=\Pi(EC'-E'C)-TCD,&V&=uD/C.
\end{aligned}
```

Primes in this note mean p derivatives. The exact identities are

**(2)**

```math
u'/u=T/\Pi,\qquad V'=-uJ/(\Pi C^2),\qquad A+B+D=C.
```

The local theorem below uses only (1)-(2) and the strict support inequalities.
It does not assume a root count for C or for $`P_v`$, nor the hypothetical
seven nodes. The counting corollaries in Sections 5-6 additionally use the
predecessors' common-height extraction and one-real-root reduction for
$`P_v`$.

**Theorem 1 (strict central orientation).** Suppose

**(3)**

```math
-1\lt p\lt0,\qquad C\lt0,\qquad D/C\gt0,\qquad A/C\gt0.
```

At every stationary point $`J=0`$ satisfying (3),

**(4)**

```math
\boxed{J'\lt0,\qquad V''\lt0.}
```

In particular there is no local minimum or multiple stationary point under
these strict inequalities. The remaining coefficient is automatically positive:
$`B/C\gt0`$. These inequalities describe a positive original triple contact; they
are not asserted at arbitrary Wronskian roots or at arbitrary curvature nodes.

## 2. The support-moment inequality

Put $`z=-p`$, and introduce the following **local** quantities:

```math
R=-C\gt0,\quad t=E/R,\quad \chi=D/C=H-t,\quad
\mathcal P=-\Pi=z(1-z)-R\gt0,\quad a_{*}=hz+m\gt0.
```

The symbol $`\mathcal P`$ here is not the actual derivative-ratio sum
$`P=c_3S_v+c_4S_w`$ used in the predecessor. From (3),

**(5)**

```math
0\lt t\lt H,\qquad zt\gt m,
\qquad A/C=zt-m,\qquad B/C=h+m+(1-z)t\gt0.
```

Let

```math
\sigma=\sum_{i=1}^3\frac1{r_i+z},\qquad
\sigma_2=\sum_{i=1}^3\frac1{(r_i+z)^2},\qquad
\beta=\mathcal P\sigma.
```

The actual shared support condition $`r_i\gt m/h`$ gives both strict bounds

**(6)**

```math
\boxed{\sigma\lt\frac{3h}{a_{*}},\qquad
\sigma_2\lt\frac{h\sigma}{a_{*}}.}
```

No independently variable cubic coefficients have replaced the support roots.
In particular

**(7)**

```math
g:=3h\mathcal P/a_{*}-\beta\gt0.
```

At a stationary point, (1) gives

**(8)**

```math
\boxed{\beta=1-2z+\frac{2Ha_{*}}{t}
-\frac{a_{*}\chi R}{t\mathcal P}.}
```

Differentiate J before imposing stationarity. Use
$`\mathcal P'=-\beta`$, $`\sigma'=\sigma_2`$,
$`C'=1-2z-\beta`$, $`E'=2Ha_{*}`$, $`E''=-2Hh`$.
At J=0 the resulting exact identity is

**(9)**

```math
\frac{J'}R=\mathcal U+
\mathcal P^2t\left(\sigma_2-\frac{h\sigma}{a_{*}}\right),
```

where, with $`k=1-2z`$,

**(10)**

```math
\begin{aligned}
\mathcal U={}&-2\mathcal P t-2Ha_{*}^2-a_{*}(\chi+H)k
+a_{*}(\chi+3H)\beta\\
&+t\beta k-2t\beta^2+
\frac{h\mathcal P t}{a_{*}}(2\beta-k).
\end{aligned}
```

For a chain-rule identity valid away from the stationary locus, set
$`S=a_{*}\chi R-\mathcal P\{t(k-\beta)+2Ha_{*}\}=J/R`$.
Without setting S=0, the right-hand side of (9) has the additional term
$`-hS/a_{*}`$. This identity follows from the derivative formulas before imposing the stationary equation, so it does not differentiate a formula restricted to that locus.

## 3. A positive multiplier and a polynomial certificate

Set

```math
v_{*}=t/H\in(0,1),\qquad \mu=m/(zt)\in(0,1),\qquad
K=h/v_{*}+H\mu(2-v_{*}\mu).
```

To keep the certificate formulas short, use **v** for this local scalar
$`v_{*}`$ only in this section. It is not the original beta function v.
Then direct algebra gives

```math
R=z(\mu-zK),\quad \mathcal P=z\{1-\mu+z(K-1)\},\quad
a_{*}=z(h+Hv\mu),
```

**(11)**

```math
K-\mu=(1-v\mu)(h/v+H\mu)\gt0.
```

Thus $`q_{*}=zK/\mu\in(0,1)`$ and $`z=\mu q_{*}/K\lt1`$.
Conversely this unit-cube parametrization gives R>0 and $`\mathcal P\gt0`$:

```math
\mathcal P/z=(1-q_{*})(1-\mu)+q_{*}(1-\mu/K)\gt0.
```

Choose the strictly positive multiplier

**(12)**

```math
\boxed{\eta=\frac{tR(1+\mu)}{2z}\gt0.}
```

The certificate proves the stronger inequality

**(13)**

```math
\boxed{\mathcal U+\eta g\lt0}
```

throughout this open unit cube when beta is replaced by the stationary
expression (8). It does not assume g>0 to prove (13); g>0 is consumed
only afterward.

Here is the complete polynomial to be checked. Define

```math
\begin{aligned}
a&=h+Hv\mu,& k&=1-2z,\\
K_n&=h+H\mu v(2-v\mu),\\
Q_n&=v(1-\mu)+z(K_n-v),&R_n&=\mu v-zK_n,\\
N&=\{v(1-2z)+2az\}Q_n-az(1-v)R_n,\\
G_n&=3hQ_n^2-aN.
\end{aligned}
```

Then $`\mathcal P=zQ_n/v`$, $`R=zR_n/v`$,
$`\beta=N/(vQ_n)`$, $`g=G_n/(vaQ_n)`$, and

**(14)**

```math
\begin{aligned}
U_n={}&-2zavQ_n^3-2z^2a^3vQ_n^2
-za^2v(2-v)kQ_n^2\\
&+za^2(4-v)NQ_n+avNkQ_n-2aN^2
+2hNQ_n^2-hvQ_n^3k,\\
\mathcal F&=-2U_n-R_n(1+\mu)G_nQ_n.
\end{aligned}
```

All denominators in the identity

**(15)**

```math
\mathcal U+\eta g=-\frac{H\mathcal F}{2avQ_n^2}
```

are positive. The degree of $`\mathcal F`$ in z is four. Substitute
$`z=\mu vq_{*}/K_n`$ and multiply by $`K_n^4\gt0`$. The resulting polynomial
$`\widetilde{\mathcal F}(h,v,\mu,q_{*})`$ has 1,133 nonzero monomial
coefficients and coordinate degrees $`(5,13,13,4)`$.

Finally substitute each unit-cube coordinate $`x_i=y_i/(1+y_i)`$ and
multiply by $`\prod_i(1+y_i)^{d_i}`$, where
$`d=(5,13,13,4)`$. The transformed polynomial has exactly:

| Coefficient sign | Count |
| --- | ---: |
| Strictly positive | 2,331 |
| Zero | 3,549 |
| Negative | 0 |

Every $`y_i\gt0`$, so at least one positive monomial and no negative
monomials prove strict positivity everywhere in the open cube. This proves
$`\mathcal F\gt0`$ and hence (13). These are exact integer coefficients,
not numerical Bernstein estimates. The full nonzero table is
[the full positive-coefficient table](../../../calculation-data/height/CENTRAL_POSITIVE_COEFFICIENTS.tsv).

## 4. Finish the orientation proof

By (6), the correction term in (9) is strictly negative. By (7), (12)-(13),

```math
\frac{J'}R\lt\mathcal U\lt-\eta g\lt0.
```

Since R>0, J'<0. At J=0, (2) gives
$`V''=-uJ'/(\Pi C^2)\lt0`$, because $`\Pi\lt0`$.
This proves Theorem 1, including exclusion of a nontransverse stationary
point under its strict inequalities. No genericity hypothesis on J is needed.

## 5. Central nodes when the E root precedes the C interval

Now import the generic surviving configuration from the predecessors:
C has two simple physical roots $`-1\lt\gamma_1\lt\gamma_2\lt0`$, its third
root is $`\gamma_3\gt r_3`$, and the cubic

**(16)**

```math
Q_v=P_v/L_q^3=mC-pE=-A
```

has exactly one simple real root. E has roots
$`\epsilon_-\in(-1,0)`$, $`\epsilon_+\gt0`$, and the last positive
maximum exclusion already requires $`\epsilon_-\lt\gamma_2`$.

Assume first $`\epsilon_-\lt\gamma_1`$. Then E>0 throughout
$`(\gamma_1,\gamma_2)`$, and Qv is positive at both endpoints. A cubic
with just one simple real root cannot have a root between two values of
the same strict sign. Thus Qv>0 throughout the interval; A/C>0 there.

At either endpoint D=E>0. Also $`D(r_3)\gt0`$, while D tends to minus
infinity as p tends to plus infinity. The cubic D therefore spends at
least one root on $`(r_3,\infty)`$, leaving at most two roots in the
central interval. Consequently its negative set inside that interval is
either empty or one interval bounded by two roots. This is exactly the
central set where V>0. At its endpoints V tends to zero, since C is
nonzero there. Under the generic auxiliary assumptions the endpoints are
simple; a multiple D root cannot create an additional positive component.

Every stationary point on this positive component satisfies Theorem 1.
There is at most one: two strict derivative crossings from positive to
negative would require an intervening stationary point of another type.
Finiteness follows directly from the degree-six numerator J. Hence any
regular fixed positive level has at most two hits in the central interval.
If there are two, their directions are upward then downward.

**Corollary 2A.** If $`\epsilon_-\lt\gamma_1`$, the central interval has
at most two hits of the one original level $`V=c_1\gt0`$. In a hypothetical
ten-root row they are an L3 maximum followed by an L4 maximum, using the
unchanged right-branch, C<0 crossing table.

## 6. Central nodes when the E root is inside the C interval

Assume $`\gamma_1\lt\epsilon_-\lt\gamma_2`$. The signs of Qv at
$`\epsilon_-`$ and $`\gamma_2`$ are respectively negative and positive.
Its unique real root, denoted $`\alpha_p`$ in the p coordinate, lies
between them. Qv is negative below this root and positive above it. In
particular Qv($`\gamma_3`$)>0, so E($`\gamma_3`$)<0 and
$`\epsilon_+\lt\gamma_3`$.

The signs of D force exactly three simple real roots:

**(17)**

```math
\delta_1\lt\gamma_1\lt\epsilon_-\lt\delta_2\lt\gamma_2\lt r_3\lt\delta_3\lt\gamma_3.
```

Here D is positive for sufficiently negative p, negative at gamma1 and
epsilon-, positive at gamma2 and r3, and negative at gamma3. The degree
leaves no extra root. The exact identity

```math
Q_v(-m/H)=-m\Pi(-m/H)\gt0
```

gives $`\alpha_p\lt-m/H`$. At Qv=0 one has
$`D/C=H+m/p`$, so D($`\alpha_p`$)<0 and in fact

**(18)**

```math
\epsilon_-\lt\alpha_p\lt\delta_2.
```

The only positive central component is $`(\gamma_1,\delta_2)`$.
V tends to plus infinity at gamma1 from the right and to zero at delta2.
At $`\alpha_p`$, the exact identity

**(19)**

```math
J=\Pi E Q_v'/m\lt0
```

holds: E>0 there, and Qv has a simple crossing from negative to positive.
Thus $`V'(\alpha_p)\lt0`$. On $`(\alpha_p,\delta_2)`$, all the inequalities
of Theorem 1 hold. Since V' starts negative, a first subsequent stationary
point would contradict its being a strict maximum. Hence V is strictly
decreasing throughout that interval.

For the actual row, the common-height extraction requires every downward
central crossing of V=c1 to be a **positive** L4 maximum, with value
$`(u/w)A/C`$. Before $`\alpha_p`$, that value is negative. If a central
level hit occurred there, the first hit after gamma1 would be downward,
because V starts at plus infinity. It would violate the actual positive
coefficient condition. Thus there is no hit before $`\alpha_p`$. A hit
at $`\alpha_p`$ would also be downward by (19) and would have L4=0, so
is forbidden as well.

All allowable central hits are therefore on the strictly decreasing final
interval. There is at most one, and its original height must satisfy

**(20)**

```math
\boxed{c_1\lt V(\alpha_p)
=u(\alpha_p)\left(H+\frac{m}{\alpha_p}\right).}
```

If (20) holds, this final interval has exactly one hit by its endpoint
values. No independent height has been assigned at different nodes.

**Corollary 2B.** If $`\gamma_1\lt\epsilon_-\lt\gamma_2`$, a hypothetical
ten-root row has at most one central common-height node, necessarily a
downward crossing and an L4 maximum, and must obey (20). This is a
conditional consequence of the actual shared coefficient requirements;
it is not an unrestricted one-hit theorem for arbitrary levels of V.

## 7. A five-node concentration in the second ordering

Corollary 2B also narrows the remaining routing problem. In that ordering,
write $`x(\gamma_3)`$ for the left-branch physical C root and
$`x(\delta_1)`$ for the right-branch physical D root from (17).
The four positive components of V, listed in original x order, are

1. $`(0,x(\delta_3))`$, corresponding to $`r_3\lt p\lt\delta_3`$.
2. $`(x(\gamma_3),x(\delta_1))`$, which contains the q-mode seam.
3. $`(x(\gamma_1),x(\delta_2))`$, the central positive component.
4. $`(x(\gamma_2),1)`$, the final positive tail.

The omitted gaps have CD<0. On the first component, C>0 and A<0,
while V tends to zero at both ends. Any nonempty regular positive level
set has a downward crossing, which would be a negative L4 maximum on
the left branch. Hence this component has no node of a bad row.

On the last component, C>0 and A<0 as well, because Qv>0 after its
unique root. Here V starts at plus infinity and ends at zero. An upward
crossing would be a negative L4 maximum on the right branch. Consequently
there is exactly one node there, a downward crossing and an L3 maximum.
The central component likewise has exactly one node: its endpoint values
ensure existence, while Section 6 proves the one-node bound and the
necessary inequality (20).

Thus the remaining five of the seven common-height nodes must all lie
in the second component:

**(21)**

```math
\boxed{x(\gamma_3)\lt x\lt x(\delta_1).}
```

V is positive and continuous throughout this interval, including at the
q-mode; its endpoint values are plus infinity and zero. The five crossings
are therefore downward, upward, downward, upward, downward. They still
use the same original c1 and the alternating original c3/c4 conditions.

This is a reduction to a five-node problem, not its exclusion. The seam
must remain in that problem: in original coordinates

```math
V_x=\frac{uL_qW_{\rm raw}}{\omega C_0^2},\qquad
V(x_q)=Hu(x_q).
```

In particular $`V_x(x_q)=0`$ automatically. This stationary point must
not be charged as a Wronskian root unless $`W_{\rm raw}(x_q)=0`$ is
proved separately. The generic avoidance of a *level node* at the seam
does not remove this stationary point.

## 8. Scope, boundaries and the remaining argument

The central contribution is now bounded by two in the first strict
ordering and one in the second. This does not bound the sum of central
and exterior nodes by six. The full seven-node exclusion is still open.

The local theorem includes multiple-J candidates under (3), because it
proves J'<0. It does not require C to be simple away from the tested point.
D=0 is a zero-height boundary, so it cannot be a positive c1 node. A=0
is handled directly by (19) in Corollary 2B. B=0 is impossible under (3).

The common-root face $`\epsilon_-=\gamma_1`$ remains in the final
boundary/continuation inventory; no global closure is asserted there.
The face $`\epsilon_-=\gamma_2`$, the nonoverlap alternative and the
physical double-C face are already excluded by the predecessor's
positive-maximum/C-E scale theorem. Weak support equalities remain outside
this strict comparable scope. A future final assembly must use one common
original-row perturbation preserving root brackets, not different
perturbations for different auxiliary nodes.
