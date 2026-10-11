# The full positive strong-fork master

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

The earlier regional inequalities can now be replaced by one theorem. Let $s_i=(a_i,b_i)$, $d_i=a_i+b_i$, and label two strictly positive, distinct-mode outer supports so $\gamma=a_3b_1-a_1b_3>0$.

Suppose $s_2=P s_1+Q s_3$, where $P,Q>1$. Then for every $E_1,E_2,E_3,L>0$, 

$$
Z_{(0,1)}\left(\sum_{i=1}^3E_i t^{a_i}(1-t)^{b_i}-L\right)\le8.
$$

 The count includes analytic multiplicity. The outer supports may be comparable and their degrees may be unequal. There is no genericity, seam-edge regularity, residue, slope, or origin-weight ordering inequality. When both origin-wall ratios are at least one, the bound is six and is sharp.

The original global proof of $N(3,4)=9$ is complete. This theorem replaces the positive strong-fork part of its casework; it is not a statement for arbitrary signed supports. The previously proved symmetric theorem also includes support families outside the strong-fork hypothesis.

## One chart, one curve, and two fixed walls

Put $K=P+Q-1$ and use $r=-\lambda_1/\lambda_3>0$ and $u=(1+r)p_2/(1+Kp_2)$. Then 

$$
(p_1,p_2,p_3)=\frac{(1-Pu,u,r-Qu)}{1+r-Ku},
\qquad 0<u<\min(1/P,r/Q).
$$

 The entropy (3) becomes 

$$
J(r,u)=\frac{P\log(1-Pu)-\log u+Q\log(r-Qu)
-K\log(1+r-Ku)}K.
$$

 At every finite $C$, it defines one analytic physical graph $u_C(r)$ on all $r>0$, because $J_u<0$ and its endpoint values at fixed $r$ are $+\infty$ and $-\infty$. Define 

$$
B=r(1+r),\qquad H=P(P-1)r^2-2PQr+Q(Q-1),\qquad j=Q-(P-1)r,
$$

 

$$
R=\frac{(d_1+rd_3)(a_1+ra_3)(b_1+rb_3)}{\gamma^2},\qquad Y=R-B.
$$

 The two positive simple roots of $H$ are $\eta<\xi$. Normal-curvature contacts, with their orders preserved, are the zeros of 

$$
A=B+H u_C-R.
\tag{21}
$$

 At a wall the source ratio satisfies $\sigma=B/R$. Thus high, low, and unit walls mean $Y<0$, $Y>0$, and $Y=0$, respectively. Away from a wall, (21) is equivalent to $u_C=u_0$, where $u_0=Y/H$.

The exact derivatives are 

$$
u_C'=f(r,u_C),\qquad f(r,u)=\frac{j u(1-Pu)}{B+Hu},
$$

 

$$
u_C''=\frac{u_C(1-Pu_C)(r-Qu_C)(1+r-Ku_C)}{(B+Hu_C)^3}H.
\tag{22}
$$

 All factors except $H$ in the second formula are strictly positive. There is also a stronger global shape statement. For $e_C=r u_C'/u_C$, 

$$
\boxed{\quad
e_C'=-\frac{(1-Pu_C)(r-Qu_C)
\{u_C(H+Kr)^2+Kr^2(1+r-Ku_C)\}}{(B+Hu_C)^3}<0.\quad}
\tag{23}
$$

 Consequently $\log u_C(e^x)$ is strictly concave on the entire real line.

## A comparison that does not require physical source bounds

The formal source denominator is always positive: $B+H u_0=R>0$. For $D=u_C-u_0$, direct subtraction gives 

$$
D'=aD-\frac{W}{H^2R},\qquad
W=R(HY'-H'Y)-Y(H-PY)j,
$$

 

$$
a=\frac{j[B(1-P(u_C+u_0))-PHu_Cu_0]}{(B+Hu_C)R}.
\tag{24}
$$

 This coefficient is analytic on each entire open wall interval, including at contacts and at nonphysical source values. A positive integrating factor therefore yields 

$$
Z_I(D)\le Z_I(W)+1.
\tag{25}
$$

 The weighted Rolle statement applies to arbitrary finite selections and also excludes infinitely many contacts. The forcing $W$ has degree at most six; its apparent degree-seven terms cancel.

## Seven coefficients for the central interval

Set $\Delta=\xi-\eta$, $v=(r-\eta)/(\xi-r)>0$, $L_0=B(\eta)$, $T_0=B(\xi)$, and 

$$
(1+v)^3R\left(\frac{\eta+\xi v}{1+v}\right)
=g_0+g_1v+g_2v^2+g_3v^3.
$$

 All $g_i$ are positive. The wall relation $(P-1)\Delta^2=2(2\eta\xi+\eta+\xi)$ gives the short identity 

$$
(1+v)^6W\left(\frac{\eta+\xi v}{1+v}\right)
=\frac{P(P-1)\Delta}{2}\sum_{i=0}^6 C_i v^i,
\tag{26}
$$

 where 

$$
\begin{aligned}
C_0&=(g_0-L_0)(3g_0-L_0),&
C_1&=4g_1(g_0-L_0),\\
C_2&=g_1^2+2g_2(g_0-2L_0)-(L_0^2+2L_0T_0+\Delta^2),\\
C_3&=4(g_0T_0-L_0g_3),\\
C_4&=T_0^2+2L_0T_0+\Delta^2+2g_1(2T_0-g_3)-g_2^2,\\
C_5&=4g_2(T_0-g_3),&
C_6&=(3g_3-T_0)(T_0-g_3).
\end{aligned}
$$

 These identities are universal, not sampled sign tests.

# Low walls: the power tangent eliminates height casework

Assume $Y(\eta)>0$ and $Y(\xi)>0$. The central coefficient signs in (26) are 

$$
(+,+,\,?,\,?,\,?,-,-).
$$

 There are at most three sign changes. Descartes and (25) give at most four weighted central contacts, on the whole central interval.

## Native source order localizes a simultaneous contact

Polynomial division gives 

$$
u_0=\ell_0+mr-\frac{V}{r-\eta}+\frac{U}{r-\xi},
\qquad m,U,V>0.
$$

 For every central $c$ and every right exterior $g>\xi$, 

$$
\frac{u_0(g)-u_0(c)}{g-c}
=m+\frac{V}{(g-\eta)(c-\eta)}
+\frac{U}{(g-\xi)(\xi-c)}>0.
\tag{27}
$$

 Reflection gives the corresponding order for $u_0/r$ on the left. Put 

$$
\alpha=\frac{Q-1}{P},\qquad \beta=\frac{Q}{P-1},
\qquad \eta<\alpha<\beta<\xi.
$$

 Equation (22) makes $u_C$ increase up to $\beta$ and decrease afterward. Its reflected equation makes $u_C/r$ increase up to $\alpha$ and decrease afterward. Thus, if one actual curve contacts both exteriors and centrally at $c$, (27) and its reflection force $\alpha<c<\beta$. At such a point, $0<e_C(c)<1$.

## The elementary sign-variation lemma

For distinct real exponents $\lambda_0<\cdots<\lambda_n$, a nonzero generalized polynomial $\sum a_i r^{\lambda_i}$ has at most as many positive zero weights as coefficient sign changes, after zero coefficients are omitted. Here is a self-contained proof.

Divide by the positive analytic unit $r^{\lambda_0}$ and differentiate. The derivative coefficients have the signs $(a_1,\ldots,a_n)$. Induct on the number of nonzero terms. If $a_0,a_1$ have opposite signs, ordinary weighted Rolle adds the allowed one weight. If they have the same sign, normalize them to be positive. Near zero the divided function and its derivative are positive. Before any first selected zero, the mean value theorem forces the derivative to become negative, supplying an extra derivative zero before that selected zero. Together with the internal and inherited multiplicity weights, this pays all the selected zero weights without the extra one. The one-term case is immediate. Applying the argument to arbitrary finite selections also rules out an infinite root set.

## One common level cannot occupy all three wall intervals

Suppose an actual $u_C$ had a contact in each interval. Choose any central contact $c$. By the localization above, $e=e_C(c)\in(0,1)$. Strict log concavity (23) gives its global power upper tangent 

$$
u_C(r)<a r^e\quad(r\ne c),\qquad a=u_C(c)/c^e>0.
\tag{28}
$$

 At each exterior contact, $u_0=u_C<a r^e$. The formal source-minus-power difference is positive at both ends of each exterior: on the left $u_0(0)=R(0)/[Q(Q-1)]>0$ and $u_0\to+\infty$ at $\eta-$; on the right $u_0\to+\infty$ at $\xi+$ and $u_0\sim R_3r/[P(P-1)]$, which dominates $a r^e$ at infinity. The two negative exterior points therefore force four distinct exterior zeros. The central contact supplies a fifth zero. No central critical point or source tangency is needed.

Multiplication by $H$ preserves their orders and gives 

$$
F(r)=R-r-r^2-aH r^e.
$$

 Its ordered exponent/coefficient-sign sequence is 

$$
\begin{array}{c|rrrrrrr}
\text{exponent}&0&e&1&e+1&2&e+2&3\\
\text{sign}&+&-&?&+&?&-&+
\end{array}
$$

 with exactly four variations, regardless of the two arbitrary signs. The sign-variation lemma forbids the five zeros just obtained. Hence *one actual level cannot occupy all three wall intervals*. This uses the whole formal tails; it assumes neither canonical bound geometry nor regular source edges.

## Paying for the two exterior intervals

If a central contact exists, then $Y$ has exactly two simple central roots $c_1<c_2$ and one negative root $-\ell$, since its constant and leading coefficients and its values at both walls are positive. On the left, 

$$
u_0=q\,\frac{(r+\ell)(c_1-r)(c_2-r)}{(\eta-r)(\xi-r)},\qquad q>0.
$$

 For its elasticity, 

$$
e_0=\frac{ru_0'}{u_0}=\frac r{r+\ell}+p-q_1,\quad
p=\frac{r(c_1-\eta)}{(\eta-r)(c_1-r)},\quad
q_1=\frac{r(\xi-c_2)}{(c_2-r)(\xi-r)}.
$$

 Both $p,q_1$ are positive, and 

$$
\frac{p'}p=\frac1r+\frac1{\eta-r}+\frac1{c_1-r}
>\frac1r+\frac1{c_2-r}+\frac1{\xi-r}=\frac{q_1'}{q_1}>0.
$$

 Thus $e_0>1$ implies $e_0'>0$. Consider $F=\log u_C-\log u_0$ on the whole left interval. At every stationary point in $\log r$, $e_0=e_C>1$, because $r<\eta<\alpha$. Equation (23) therefore makes that stationary point a nondegenerate strict maximum. Since $F\to-\infty$ at both ends, it has one maximum and at most two zero weights. Reflection gives the same exterior two-weight bound on the right.

With a central contact present, no-three-interval occupancy leaves at most one occupied exterior. Central four plus exterior two gives six curvature weights.

If there is no central contact, (24) gives instead 

$$
W(\eta)=\frac{P(P-1)\Delta}{2}Y(\eta)[3R(\eta)-B(\eta)]>0,
$$

 

$$
W(\xi)=-\frac{P(P-1)\Delta}{2}Y(\xi)[3R(\xi)-B(\xi)]<0.
$$

 At least one forcing weight is central, leaving at most five outside. The two whole-interval counts (25) give at most seven exterior curvature weights. But $A<0$ near both $0$ and infinity, and neither wall is a contact, so its finite total weight is even: at most six. In both cases (2) gives eight original weights. This proves the full strict-low theorem with no antichain or forcing-five hypothesis.

## The height theorem follows

For a canonical source with central entropy minimum $m_C$ and exterior maxima $M_L,M_R$, the same result gives 

$$
\boxed{m_C>\min(M_L,M_R).}
$$

 Otherwise the level $C=m_C$ would occur centrally and on both exterior components, contrary to the no-three-interval theorem. This closes the previously missing adaptive height statement. The earlier source-dilation monotonicity and terminal-collapse results remain valid, but are no longer needed as conditional substitutes.

# Mixed walls: one positive sum replaces the parameter inequalities

Assume $Y(\eta)>0>Y(\xi)$; reflection handles the other orientation. The mixed exterior theorem gives at most two left weights and exactly one simple right contact. On the right $u_0'>0$ while $u_C'<0$. On the left the source $u_0/r$ is a positive Stieltjes sum and hence strictly log convex, whereas the actual $u_C/r$ is strictly log concave. The latter has a compact three-coefficient analytical Bernstein proof in the accompanying sources.

In (26), $g_0>L_0$ and $g_3<T_0$, so $C_0,C_1,C_3,C_5>0$. The metric factors as $R=k\prod(r+A_i)$, $k,A_i>0$. Put 

$$
z_i=\frac{\eta+A_i}{\xi+A_i}\in(0,1),\quad
p=z_1z_2z_3,\quad e_1=\sum z_i,\quad e_2=\sum_{i<j}z_iz_j,
$$

 

$$
s=g_3/T_0\in(0,1),\quad m=L_0/T_0,\quad sp=g_0/T_0>m,
\quad E=\prod(1-z_i^2),\quad J=(e_1+p)^2+2e_2-e_2^2.
$$

 Since $e_1>e_2>0$, $J>0$. The exact identity 

$$
\boxed{\frac{C_2+C_4}{T_0^2}
=(1-s)+sE+s(1-s)J+(sp-m)(4se_1+sp+m)>0}
\tag{29}
$$

 prevents both uncertain internal coefficients from being negative. There are therefore at most three coefficient sign changes, including the possible last change at $C_6$. Equations (26) and (25) give at most four central weights. The difference $u_C-u_0$ is positive at $\eta+$ and negative at $\xi-$, so its weight is odd and at most three. Thus $2+3+1=6$ curvature weights give original eight.

If $C_2,C_4\ge0$, there is at most one forcing variation; the central contact is uniquely simple and the original bound improves to six. No attainment claim is needed for that sufficient region.

# High and unit walls: direct weighted closure

For strict high-high walls, the source has $u_0''>0$ centrally, opposite $u_C''<0$, so there are at most two central weights. The new high theorem proves exactly one simple contact in each exterior, without the previous residue-balance inequality. Its main reduction is as follows.

On the left, $f_{uu}<0$ throughout the formal positive-denominator domain, so $\Phi=u_0'-f(r,u_0)$ is convex in the cubic source coefficients. At a unit left wall and a weakly high right wall, normalizing the source gives a clipped simplex with six vertices: constant, linear, and the degree pairs $(0,2),(0,3),(1,2),(1,3)$. All have $\Phi<0$ except $R=B$, which has $\Phi=0$. The constant and linear signs follow from one-variable derivative identities. The only remaining endpoint polynomial is 

$$
\begin{split}
E(e,x)={}&e^6+e^5(4x+2)+e^4(15x^2+16x+2)
+e^3(14x^3+36x^2+14x)\\
&+e^2(2x^4+16x^3+15x^2)+e(2x^4+4x^3)+x^4>0.
\end{split}
$$

 Its 15 positive monomials replace the earlier 128-term expansion.

For a previously bad high exterior, write $R=\delta S$. The ratio $S/B$ has exactly one minimum by Descartes. At a fixed physical source point, interpolate between the scale where $u_0=0$ and the first unit scale. Both endpoint gaps $\Phi$ are strictly negative; convexity makes the actual gap negative. This proves strict exterior entropy monotonicity. Reflection covers the other exterior, so the curvature budget is $1+2+1=4$, giving original six.

Unit walls are counted directly. If one wall is unit and the other high, the residual $u_C-u_0$ is transverse at a matching unit wall: its sign trades an interior contact for the extra residual wall weight. The exact budget remains four. With two unit walls $u_0$ is affine; its residual has at most two weights and $H$ supplies two mandatory weights. Thus both ratios $\sigma\ge1$ give six, including all coincidences.

For one unit wall with the other low, use the normal ODE $d'=Ad+T/(V_0w^3)$, $\deg T\le6$. The unit residue of $A$ is one. Write $d=hv$, $T=h^2F$ for its unit factor. The deflated ODE is regular through that wall, its forcing multiplier nonzero, and $\deg F\le4$. Only the other wall splits the count: $Z(v)\le4+2=6$, hence $Z(d)\le7$. Positive normal endpoint phases make the weight even and at most six. Two unit walls give $\deg F\le2$, a global count $Z(v)\le3$, and $Z(d)\le5$, improving by parity to four. Homogeneous forcing cases follow from regular homogeneous uniqueness and endpoint divergence. No multiplicity is inferred by perturbation.
