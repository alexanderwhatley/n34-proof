# A complete one-wall theorem for real-rooted positive metrics

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Completed composition, 4 October 2026, from F23/F24 and the retained comparison/counting results. The following proof combines those coefficient statements with the common-level root counts.

## Statement

Let $P>1$, $0<Q<1$, $B(r)=r(1+r)$, and

$$
H(r)=P(P-1)(r+h)(r-\xi),\qquad j(r)=Q-(P-1)r.
$$

Retain the actual finite-entropy graph $u_C$ and its positive-denominator comparison equation. Let $R$ be a cubic with four strictly positive coefficients and three real negative roots, counted with multiplicity. Equivalently,

$$
R(r)=k\prod_{i=1}^3(r+A_i),\qquad k>0,\quad A_i>0.
$$

**The curvature comparison $B+Hu_C-R$ has at most six positive zeros counted with analytic multiplicity.** Every finite actual entropy is covered. Coincident negative metric roots and multiple curvature contacts are permitted.

For a genuine geometric source, the two weighted normal Rolle reductions give at most eight original positive-level contacts counted with analytic multiplicity.

This theorem imposes real-rootedness on $R$. The unrestricted arbitrary positive-cubic one-wall statement remains separate. Nonunit $Q=1$ and general coordinate-boundary multiplicity claims are outside the statement.

## dispatch and the only possible obstruction

Write $Y=R-B$ and

$$
W=R(Y'H-YH')-Yj(H-PY),\qquad \deg W\le6.
$$

The following results are inputs, not new assumptions on the metric:

| Situation | curvature bound |
|---|---:|
| HIGH, $Y(\xi)<0$ | Six, for every positive cubic |
| UNIT, $Y(\xi)=0$ | Six, including multiple wall contacts |
| LOW with no actual central contact | Six, without a central source factorization |
| Contacted LOW with $l\le1$ | Six, by the complete LOW lower-root master |
| $w_0\le0$ or $w_6\le0$ | Six, including equality and degree loss |
| Some negative metric root has $t\le A_i\le1$, $t=(1-Q)/P$ | Six, with no requirement that this root be simple |

At a contacted strict LOW wall, degree-three root exhaustion gives

$$
Y=k(r+l)(r-a)(r-b),\qquad k,l>0,\quad0<a<b<\xi.
$$

All actual central contacts lie in $(a,b)$. On that whole interval the weighted comparison equation costs one Rolle contribution to the root count, even when the formal source exceeds physical probability bounds. The exterior theorem costs at most two weights.

Thus it remains to consider $l>1$, $w_0,w_6>0$, and no metric distance in $[t,1]$. For the projective forcing coefficients $C_i$, the C45 theorem and exact weak-sign enumeration prove curvature six unless

$$
C_1<0,\quad C_2>0,\quad C_3<0,\quad C_4>0. \tag{1}
$$

The enumeration includes all zero-coefficient boundaries: its only possible five-variation words are $(+,-,+,-,+,-,-)$, $(+,-,+,-,+,0,-)$, and $(+,-,+,-,+,+,-)$. They all require (1). Outside (1), Descartes gives at most three central forcing weights, so the total curvature bound is $3+1+2=6$.

## Exact allocation of the negative metric roots

Under (1), the C3 source-bound localization gives

$$
ab<l. \tag{2}
$$

At each metric root $-A_i$, $R(-A_i)=0$ and $Y=R-B$ give the exact identity

$$
k(l-A_i)(A_i+a)(A_i+b)=A_i(1-A_i). \tag{3}
$$

Because $l>1$, equation (3) implies $A_i\in(0,1)\cup(l,\infty)$. The values $A_i=1$ and $A_i\in[1,l]$ are impossible. The closed negative-metric-root inequality has already dispatched every $A_i\in[t,1]$; hence every remaining distance lies either below $t$ or above $l$.

Also $R(-l)=B(-l)=l(l-1)>0$. The product $k\prod_i(A_i-l)$ therefore has an even number of negative factors. Counting repeated roots with their multiplicities, either zero or two metric distances lie below $l$.

If all three lie above $l$, comparison of constant coefficients gives

$$
A_1A_2A_3=lab>l^3,\qquad ab>l^2>l,
$$

contradicting (2). There are therefore **exactly two distances below $t$ and one above $l$**. This conclusion allows the two small distances to coincide; no ordering or density argument is used.

## One-seventh localization without a simple-root hypothesis

Set $d=b-a$, $L=a+l$, $M=b+l$, and $j_a=Q-(P-1)a$. The first-coefficient identity is

$$
\frac{C_1}{kd[-H(a)]}=2a(1+a)(M+L)+Ld[R'(a)-j_a]. \tag{4}
$$

Thus $C_1\le0$ forces $R'(a)<j_a$. Since $R(a)=a(1+a)$, the two metric distances below $t$ give

$$
R'(a)=a(1+a)\sum_{i=1}^3\frac1{a+A_i}
 >\frac{2a(1+a)}{a+t}. \tag{5}
$$

The logarithmic derivative in (5) counts repeated factors separately, so it remains exact for coincident roots. Using $Pt=1-Q$, (4)--(5) imply

$$
G(P,Q,a):=P(P+1)a^2+[3P-1-(2P-1)Q]a-Q(1-Q)<0.
$$

The one-seventh decomposition is

$$
G=(Q-4/7)^2+(a-1/7)(2a+16/7-Q)
 +(P-1)[(P+2)a^2+(3-2Q)a].
$$

Every term is nonnegative when $a\ge1/7$, and the last is strictly positive. Hence the actual obstruction (1) necessarily has $a<1/7$. This directly proves the ordering relaxation of the original geometric one-seventh lemma; its former strict $A<D$ wording is not needed here.

## Closing both scale-slope branches

Positive coefficients of $R$ imply $R'(a)>0$. Differentiating $R=B+Y$ at $a$ gives

$$
R'(a)=1+2a-kdL>0,\qquad k<\frac{1+2a}{dL}. \tag{6}
$$

This is exactly the derivative-bound hypothesis of the coefficient-only F23 and F24 theorems. Native wall roots satisfy $0<h<1/2$, since $H(-h)=0$ gives $1-Q>2Ph>2h$.

If the quadratic source-scale slope $D_2\ge0$, F23 excludes $C_2>0,C_3\le0,C_4>0$, including $D_2=0$. If $D_2<0$, F24 excludes that same pattern throughout $a<1/7$ under (6). Its exact certificate is valid for all native $h<1/2$, all $b-a>0$, all $\xi-b>0$, and all $l-1>0$. No additional metric-factor or entropy-level hypothesis is required.

Thus (1) is impossible. The C45 counting composition gives at most three central forcing weights, four central curvature weights, and two exterior weights. This finishes the real-negative-root metric curvature-six theorem.

## The complete strict original ONE-EDGE corollary

For positive supports in the original row

$$
a_1<a_3<a_2,\qquad b_3<b_2<b_1,
$$

and every $E_i,L>0$, the original level $\sum_iE_ix^{a_i}(1-x)^{b_i}=L$ has at most eight contacts counted with analytic multiplicity. The reflected row has the same conclusion. No source-event regularity, simple forcing roots, binary event nesting, mode-routing table, generic density argument, or total-positivity root count is a premise of this new strict corollary.

The following support calculation gives the cases. If the middle mode is not between the outer modes, the zero-free origin-quadratic theorem applies, including mode equality. Otherwise write $s_2=p s_1+q s_3$, with $p>0,q>0,p+q>1$. The coordinate order forces $p<1$. If $q\le1$, there is no internal origin wall. If $q>1$, reflection and the outer-support swap give $P=q>1,0<Q=p<1$, exactly the chart above. Two internal walls and nonunit $Q=1$ are impossible in this strict row.

The genuine cubic always has three real negative metric roots:

$$
R=\delta(r+A)(r+D)(r+E),\quad
A=\frac{a_1}{a_3},\quad D=\frac{a_1+b_1}{a_3+b_3},\quad E=\frac{b_1}{b_3}.
$$

Here the reflected coordinates obey $a_1<a_2<a_3$, $b_3<b_1<b_2$, so $A<E$ and

$$
D-A=\frac{\gamma}{a_3(a_3+b_3)}>0,\qquad
E-D=\frac{\gamma}{b_3(a_3+b_3)}>0,
\quad\gamma=a_3b_1-a_1b_3>0.
$$

Metric coincidence is therefore impossible in the strict original row, although the broader master permits it. Nongeneric original entropy contacts do not alter these strict support inequalities. The curvature-six theorem and two weighted normal Rolle reductions give original weighted eight.

The closed nonnegative one-edge cone has distinct eight, with the nonidentity exception: assume $a_i,b_i\ge0$, $a_1\le a_3\le a_2$, $b_3\le b_2\le b_1$, $E_i,L>0$, and a nonidentity level difference. The following direct transfer uses the new strict theorem. Suppose nine old distinct roots exist. Among selected roots let $o$ be odd crossings and $e_+,e_-$ the even minima and maxima. A sufficiently small common level shift in the better direction creates at least $o+2\max(e_+,e_-)\ge o+e_++e_-$ simple roots in disjoint compact neighborhoods. Choose the shift away from their finitely many critical values and keep the level positive. Perturb first coordinates in the order $(1,3,2)$ by $(\varepsilon,2\varepsilon,3\varepsilon)$, and second coordinates in the order $(3,2,1)$ by the same ordered increments. All coordinates and gaps become strictly positive. Every selected simple root persists under sufficiently small support perturbation, contradicting the new strict weighted-eight theorem. This transfer preserves a selected old distinct count, not arbitrary original multiplicities. Coordinate equalities, zero coordinates, repeated supports and affine collinearity consequently gain no new general weighted-eight assertion.
