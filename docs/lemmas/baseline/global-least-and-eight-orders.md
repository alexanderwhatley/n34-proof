# Global least supports and an eight-order reduction

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

#### Retained inputs and scope.

The preliminary four-atom ceiling ten, its monotone-anchor saturation, the signed cofactor endpoint formulas, and the component/contact count are those proved in the manuscript. We retain the old global-least theorem only at its original scope 

$$
1+\alpha m_u-\beta m_v-\gamma m_w,\qquad
u,v,w\ge0,\quad v\le w,
\qquad Z\le8.                                      \tag{GL-c}
$$

 Its lower-fork and comparable-negative operator dependencies remain. We also retain the analytic disjoint-curvature lemma. The new comparable-atom theorem (Cross) replaces the separate F1 localization and the other cross cell’s two-inequality/regular-flag complement; its proof uses the existing endpoint operator and interior-root interpolation. No F2, F3, F4, or full chamber theorem is used in the following result.

#### Extended global-least theorem.

Let $\alpha,\beta,\gamma>0$ and 

$$
F=1+\alpha m_u-\beta m_v-\gamma m_w\not\equiv0,
\qquad u,v,w\ge0.
$$

 Then $Z(F)\le8$, with *no comparability assumption on $v,w$*. Equivalently, a two-positive, two-negative four-beta sum with a globally least active support has at most eight distinct roots.

#### Proof.

First use strict positive coordinates, distinct coordinate orders, simple original roots, and the same generic cofactor hypotheses used in the manuscript’s saturation argument. Comparable negative supports are covered by (GL$_c$), after interchanging them if necessary. Otherwise arrange $v_1<w_1$ and $w_2<v_2$. The positive support $u$ has just nine position cells: 

$$
\begin{array}{c|ccc}
 &u_2<w_2&w_2<u_2<v_2&v_2<u_2\\\hline
u_1<v_1&\text{corner}&\text{Cross}&\text{corner}\\
v_1<u_1<w_1&\text{Cross (reflected)}&\text{Disjoint}&\text{Cross}\\
w_1<u_1&\text{corner}&\text{Cross (reflected)}&\text{corner}
\end{array}
$$

 The Cross entries have the positive support comparable to one negative support, both lying northwest of the other, either directly or after physical reflection and relabeling the negative pair. The new theorem gives eight throughout those four cells. The center is exactly the already proved disjoint-curvature domain.

All four corners have one common proof. Label $0$ the constant, $1$ the positive support $u$, $2$ the negative support $v$, and $3$ the negative support $w$. Here $u_1$ lies outside $[v_1,w_1]$ and $u_2$ lies outside $[w_2,v_2]$. The signed cofactor endpoint formulas give 

$$
\begin{aligned}
 e_0(0)&=(v_1-u_1)(w_1-u_1)(w_1-v_1)>0,\\
 e_0(1)&=-(v_2-u_2)(w_2-u_2)(w_2-v_2)>0,\\
 e_1(0)&=-v_1w_1(w_1-v_1)<0,\\
 e_1(1)&=v_2w_2(w_2-v_2)<0.
\end{aligned}
$$

 The same formulas give 

$$
K(0)=u_1v_1w_1 e_0(0)>0,\qquad
 K(1)=-u_2v_2w_2 e_0(1)<0.
$$

 Use the monotone negative-pair anchor $2,3$, with complementary pair $0,1$. Each complementary cofactor has even endpoint parity and at most two physical roots; the coefficient-weighted pair product is negative at both ends. Thus the useful set has at most two components. The sextic $K$, with opposite endpoint signs, has at most five physical roots. The corresponding residual therefore has at most $2+5=7$ roots, whereas ten-root saturation would require eight. Ten original roots are impossible. The positive original endpoint signs and the preliminary ceiling ten now give at most eight simple roots in these cells too.

Every strict generic cell is proved. Apply the manuscript’s total distinct-root transfer with sign vector $(+,+,-,-)$ and exponent set $u,v,w\in(0,\infty)^2$, initially allowing the constant coefficient to vary independently over the positive numbers and then renormalizing it to one. This includes finite coordinate ties, vanishing exponent coordinates, repeated supports, and multiple original roots, excluding identities. Division by a globally least beta monomial and, if needed, global coefficient-sign reversal give the equivalent formulation.

#### Only eight coordinate-order configurations need checking.

We now reduce the remaining two-two chamber without enumerating 576 labeled permutations or any cubic root-count allocation.

Work in the strict generic case and suppose there are ten roots. Endpoint parity and the preliminary ceiling imply equal endpoint signs; reverse all coefficient signs to make them positive. If the same atom dominates both endpoints, its support is globally least and the theorem just proved gives eight. Therefore the endpoint dominants are distinct positive atoms. Label them $0$ (first-coordinate minimum) and $1$ (second-coordinate minimum). They are incomparable.

Monotone-anchor saturation forces the second atom at *each* endpoint to be negative. Label the first-coordinate second atom $2$ and the other negative atom $3$. Consequently 

$$
\text{first order}\in\{0213,0231\},\qquad
\text{second order}\in\{1203,1230,1302,1320\}.
$$

 This is the complete eight-entry table: 

$$
\begin{array}{c|cccc}
 &1203&1230&1302&1320\\\hline
0213&\mathrm{F2}&\mathrm{E}&\mathrm{F3}&\mathrm{F4}\\
0231&\mathrm{E}&\mathrm{E}&\mathrm{F4\ (reflected)}&\mathrm{E}
\end{array}
$$

 Here E denotes a direct contradiction of the residual endpoint sign condition (12) of the manuscript. For $0213/1230$, the incomparable anchor $1,2$ has complementary second-endpoint dominant $3$, whose negative coefficient and position beyond both anchor ranks give a negative residual sign. For each of $0231/1203$, $0231/1230$ and $0231/1320$, use anchor $0,2$: its complementary first-endpoint dominant is $3$, again with negative coefficient and rank beyond both anchor ranks. These four residual signs contradict the required positive endpoint sign.

Finally $0231/1302$ becomes $0213/1320$ under physical reflection followed by $0\leftrightarrow1$, $2\leftrightarrow3$. Only the three canonical F2, F3, F4 families remain. Their retained bounds exclude ten simple roots in the equal-endpoint cases. Together with the opposite-endpoint bound nine, this proves the strict two-two chamber bound nine; the same distinct-root transfer includes its finite boundary cases.

#### What this revision removes.

The 576-pattern classifier, the sixteen degree/parity root-count allocations, the separate F1 assembly row, and the 16-pattern cross family’s affine-inequality and regular-Wronskian complement are unnecessary. The proof still retains (GL$_c$), including its original lower-fork dependencies, disjoint curvature, the endpoint operator, interior-root interpolation, and the F2/F3/F4 theorems. This is a proof reduction, not a claim that every original technical lemma has disappeared.
