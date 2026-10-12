# A master-height theorem for the entire smaller rightmost gap

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Theorem and exact standing inputs

Let

```math
G=c_1-u+c_3v+c_4w,\qquad c_1,c_3,c_4>0,
\qquad0\prec s_u\prec s_v\prec s_w,
```

where all functions are beta monomials. Write q=w/v, reflect so
$`\Delta=\det(v,q)>0`$, and suppose

```math
u=v^h q^{-m},\qquad H=1-h,\qquad0<h<1,\quad0<m<H.
\tag{1}
```

Then G has fewer than ten distinct roots in $`(0,1)`$, for every
source scale and every one fixed positive coefficient triple.

Equivalently, for $`S=u-c_3v-c_4w`$, if the source has nine generic
critical points $`x_1<\cdots<x_9`$, with alternating maxima and minima,

```math
\min\{S(x_1),S(x_3),S(x_5),S(x_7),S(x_9)\}
\le\max\{0,S(x_2),S(x_4),S(x_6),S(x_8)\}.
\tag{MH-R}
```

This proves the master-height inequality on the whole source region (1).
The proof constructs one forced physical two-pole cell and uses two
possible placements of one quadratic root, rather than the original
scale/discriminant/real-root dispatch.

Only the following standing mathematical inputs are retained:

1. The supplied degree-three beta-times-cubic root bound (El Hilany--Tavenas),
   the complete original seven-node L3/L4 common-height extraction with
   the required maxima positivity bridge (s051), and original-function
   regularization preserving compact root brackets. In particular the
   extracted maxima refer to the one actual c3 and c4; no independently
   perturbed height collection is assumed.
2. The local central-contact orientation theorem: at $`-1<p<0`$,
   $`C<0,D/C>0,A/C>0`$, every V-stationary point is a strict maximum.
   This is s132 Theorem 1; its local exact certificate remains an input.
3. The earlier proof left positive-contact theorem: at $`p>r_3,C<0`$ and
   $`A/C,B/C>0`$, one has $`V_p<0`$, for every m>0. The exact proof is
   in [all negative n left negative c contact monotonicity](left-contact-monotonicity.md) in the
   joint directory. It extends the local inequality of s056 Lemma 1
   without a gap-size restriction.
4. The all-exterior signed metric height theorem from the earlier proof:
   in the signed DCCDDC cell, every finite right-exterior stationary
   height is above every positive central height.

The right positive-residue exterior orientation used below is stated
and proved from its exact identity here. The original
global Qv-one theorem, discriminant reduction, nonphysical real-root
exclusion, and all upper/lower scale barriers are not standing inputs.

## 1. The original source forces derivative saturation

The modes satisfy

```math
x_q<x_{w/u}<x_w<x_{v/u}<x_v<x_u.
```

Indeed v/u has support Hs_v+ms_q and w/u adds s_q, while (1) and the
strict source determine the displayed angular order.

Put $`\tau=x_{v/u}`$. On $`(\tau,x_u)`$, all three positive
terms in

```math
G/u=c_1/u+c_3(v/u)+c_4(w/u)-1
```

strictly decrease. On $`(x_u,1)`$, the positive ratios v'/u' and
w'/u' strictly decrease from infinity to zero: each is a decreasing
positive beta ratio times the decreasing positive linear factor
$`(x-x_f)/(x-x_u)`$. Therefore the actual G' has one zero after x_u,
a strict minimum of G. These facts give at most two original roots
after $`\tau`$. If a root occurs between $`\tau`$ and x_u, the
function is negative at x_u and only one tail root remains; otherwise
the tail contributes at most two.

Assume ten generic original roots. At least eight lie before $`\tau`$.
Define

```math
S_v=v'/u',\quad S_w=w'/u',\quad P=c_3S_v+c_4S_w.
```

On $`(0,x_v)`$, u'>0 and G'=u'(P-1). Rolle gives at least seven
hits of the same actual level P=1. Its endpoint values are

```math
P(0^+)=0<1,\qquad P(x_v)=c_4w'(x_v)/u'(x_v)<0<1.
```

Simple-hit parity makes their count even, so there are at least eight.

With $`\rho=x(1-x)`$, $`L_f=a_f-(a_f+b_f)x`$, define the exact
cores

```math
P_f=(L_f-L_u)L_fL_u+\rho(L_f'L_u-L_fL_u'),\qquad f=v,w.
```

The numerator of P' is

```math
c_3vP_v+c_4wP_w,
\qquad P'=\frac{c_3vP_v+c_4wP_w}{u\rho L_u^2}.
```

Dividing by v gives a cubic plus q times a cubic. The standing root
bound gives at most eight distinct numerator zeros. Its strict eventual
signs are positive near zero and negative near one; simple-root parity
therefore gives at most seven. At x_u the numerator is negative and
nonzero. Hence the bound saturates: P has exactly seven stationary
nodes, all before x_v, interlacing exactly eight P=1 hits
$`\xi_1<\cdots<\xi_8`$. Odd stationary nodes are maxima above one.
G' has one additional tail zero, so these are the first eight of its
nine critical points; in particular

```math
G(\xi_7)<0.
\tag{2}
```

The positive S_v is strictly log concave on $`(0,x_v)`$, tends to
zero at both ends, and has one strict maximum $`\alpha`$. Away from
that point set

```math
F=S_w'/S_v'=qP_w/P_v.
```

All seven P-stationary nodes meet the same negative level
$`F=-c_3/c_4`$. F starts at zero with positive derivative near zero.
If j nodes precede alpha, an extra first turning point and ordinary
Rolle give j zeros of F' there; the remaining nodes give 6-j afterward.
All seven cannot precede alpha, since that would give seven zeros.
The exact identity is

```math
F'=\frac{qL_u}{\rho P_v^2}W_{\rm raw},\qquad
W(u',v',w')=\frac{uvw}{\rho^6}W_{\rm raw},\quad
\deg W_{\rm raw}\le6.
```

Also

```math
W_{\rm raw}(0)=a_ua_va_w(a_v-a_u)(a_w-a_u)(a_w-a_v)>0.
```

Thus exactly six simple raw W roots occur before x_v and exhaust its
degree. In particular Wraw is positive everywhere after x_v, and the
last P maximum $`y`$ is after alpha.

## 2. Physical auxiliary ratio signs replace the global cubic inventory

The source derivative core P_v is positive before alpha and negative
on $`(\alpha,x_v)`$, by strict log concavity of S_v. The lemma in
[physical derivative core auxiliary ratio lemma](derivative-polynomial-signs.md) now gives

```math
P_v>0\text{ before }\alpha,\qquad P_v<0\text{ after }\alpha
\quad\text{throughout }(0,1).
\tag{3}
```

For completeness, its only extra argument is physical. On $`(x_v,x_u)`$,
S_v<0 and w'/v' is positive and strictly decreasing. At a P_v zero,
P_w>0, while

```math
L_uW_{\rm raw}=\rho(P_vP_w'-P_wP_v')+L_qP_vP_w
```

forces P_v'<0. Its values at both endpoints of this interval are negative,
so no zero exists. After x_u,

```math
P_v=s_{v/u}s_vs_u(x_{v/u}-x)(x_v-x)(x_u-x)
-(a_ub_v-b_ua_v)\rho<0.
```

No roots outside the original interval enter this argument.

## 3. The last actual maximum forces one physical two-C cell

The last maximum y also lies after x_w. If alpha>=x_w this is immediate.
Otherwise P_v(x_w)<0. Let $`\kappa=h+m\in(0,1)`$, and at x_w
write L=L_v>0 and s_f=a_f+b_f. The exact mode identities are

```math
W_{\rm raw}(x_w)=-s_w\rho\kappa L^2\mathcal B,
```

```math
\mathcal B=-\frac{1+\kappa}{\kappa L}P_v
+(1-\kappa)(L\rho'+s_v\rho)
+\rho\left\{(s_v-s_u)+\frac{1-\kappa}{\kappa}s_u\right\}.
```

Here $`L\rho'+s_v\rho=a_v(1-x)^2+b_vx^2>0`$, and all remaining
terms are positive. Hence P_v(x_w)<0 implies Wraw(x_w)<0. If all
seven P-stationary nodes preceded x_w, the localized Rolle count from
section 1 would place all six W roots there and force Wraw(x_w)>0.
Equality y=x_w is impossible because both S_v' and S_w' are negative
there. Therefore

```math
y>\max\{\alpha,x_w\},\qquad y<x_v.
\tag{4}
```

Introduce the exact projective chart

```math
p=L_v/L_q,\quad\Pi=\Lambda\prod_i(p-r_i),\quad
m/h<r_1<r_2<r_3,\quad\Lambda>0,
```

and linked cores

```math
C=p(p+1)-\Pi,\quad E=-Hhp^2+2Hmp+m(m+1),\quad D=HC+E,
```

```math
A=-mC+pE,\quad B=(h+m)C-(p+1)E,\quad V=uD/C.
```

The two physical rays are p>r3 and p<r1, glued at x_q. Exact derivative
and core identities are

```math
P_v=L_q^3Q_v,\qquad Q_v=mC-pE=-A,
```

```math
\left(\frac{w'}{v'}\right)'=\frac{qL_q^3C}{\rho L_v^2}.
```

At a stationary P point,

```math
P=-\frac{c_4S_v^2}{S_v'}(w'/v')'.
```

At y, S_v'<0 and P(y)>1. Equations (4) give -1<p(y)<0 and Lq<0,
so C(y)<0. Also P_v(y)<0, hence Qv(y)>0; since mC<0 and p<0,
Qv=mC-pE>0 forces E(y)>0.

Because C(-1),C(0),C(r3)>0 and C(y)<0, its cubic degree gives exactly
the three simple roots

```math
-1<\gamma_1<\gamma_2<0<r_3<\gamma_3.
\tag{5}
```

The quadratic E has exactly one root $`\epsilon_-\in(-1,0)`$
and one positive root. Since E(y)>0, $`\epsilon_-<\gamma_2`$.
Only two generic placements remain: epsilon_- is before gamma1, or
inside (gamma1,gamma2). This is a forced source reduction, not a
scale/cubic-phase dispatch.

## 4. Both node extractions retain the actual original height

The standing global source identities for

```math
R=(u-c_1)/v,\quad L_4=R_q,\quad L_3=R-qR_q
```

show that ten generic original roots force exactly seven simple
common-height nodes V=c1. At every such node the appropriate L3 or L4
maximum must exceed the one actual positive c3 or c4. The resulting
crossing inequalities are exactly the table in
[uniform signed five node budget](signed-five-contact-count.md). In particular a required maximum
cannot have a nonpositive normalized coefficient A/C or B/C.

The actual last maximum supplies the stronger height witness. Put
$`S_+=c_3v+c_4w>0`$, $`M_P=P(y)>1`$. Since P<M_P and u'>0
between xi7 and y,

```math
S_+(y)-S_+(\xi_7)<M_P\{u(y)-u(\xi_7)\}.
```

At y, solving the two derivative-contact equations gives
$`V(y)=u(y)-S_+(y)/M_P`$. With (2),

```math
\boxed{c_1<u(\xi_7)-S_+(\xi_7)
<u(\xi_7)-S_+(\xi_7)/M_P<V(y).}
\tag{6}
```

This witness is a positive central value. The point y is not asserted to
be stationary for V. All coefficients and the height remain those of
the original row throughout.

## 5. The interlacing placement: at most five nodes

Suppose $`\gamma_1<\epsilon_-<\gamma_2`$. Qv=mC<0 at epsilon_-
and Qv=-pE>0 at gamma2. By the physical signs (3), alpha is on the
right branch between these points. Thus Qv>0 on the entire left ray,
so E(gamma3)<0. The source signs and cubic degree give

```math
\delta_1<\gamma_1<\epsilon_-<\alpha_p<\delta_2<\gamma_2
<r_3<\delta_3<\gamma_3,
\tag{7}
```

where the deltas are the D roots. For the refined alpha/delta2 order,
Qv(-m/H)=-mPi>0 puts alpha_p<-m/H; at Qv=0,
D/C=H+m/p>0, so D(alpha_p)<0.

The initial positive component before delta3 has C>0,A<0 and zero
endpoint values; its required downward crossing is forbidden. The final
tail after gamma2 has C>0,A<0 by (3), so upward crossings are forbidden
and it contributes one downward node.

The central positive component is (gamma1,delta2), from infinity to zero.
Before alpha_p its downward crossing would have A/C<0 and is forbidden.
At alpha_p,

```math
J=\Pi E Q_v'/m<0,\qquad V_p<0,
```

where $`J=\Pi(EC'-E'C)-(hp-m)CD`$. After alpha_p the local central
orientation permits only strict maxima. Starting with V_p<0, there can
be no subsequent stationary point; otherwise the first one would be a
minimum. Thus the central component contributes exactly one allowable
downward node, under the original level inequalities.

The main positive component runs from x(gamma3), through x_q, to
x(delta1), from infinity to zero. Its normalized coefficients A/C and
D/C are positive throughout by (3) and (7). All E/C residues d_i are
positive. Consequently

```math
(B/C)_p=\sum_i\frac{d_i(\gamma_i+1)}{(p-\gamma_i)^2}>0.
```

It is continuous and strictly increasing across the seam in original
x order. Every downward main crossing supplies B/C>0; this positivity
propagates over all later points of the component.

The left part begins at infinity. If it had two level crossings, its
first two would be downward and upward. On the interval between them,
A/C is positive throughout, and the first downward crossing makes B/C
positive throughout. The new left-contact theorem gives V_p<0 on that
interval, contradicting the required down/up minimum. Thus the left
main contributes at most one node.

Here is the positive-residue orientation identity. Put
$`\mathcal P=-\Pi`$, $`t=-E/C`$, $`\chi=D/C=H-t`$,
$`a_3=B/C,a_4=A/C`$, and

```math
\mathcal R=(\log|t|)_{pp}-((\log|t|)_p)^2.
```

On the right exterior all reciprocals (gamma_i-p)^-1 are positive,
and

```math
tt''-2(t')^2
=2\sum_{i<j}d_id_j s_is_j(s_i-s_j)^2>0,
\quad s_i=(\gamma_i-p)^{-1}.
```

Hence $`\mathcal R>0`$. At a stationary point the exact source
cancellation is

```math
\frac{V_{pp}}u=-\frac{\chi C a_3a_4}{\mathcal P^3t}-t\mathcal R.
\tag{8}
```

This identity has a short direct derivation. Since u_p/u=T/Pi with
T=hp-m, stationarity says $`t'=\chi T/\Pi`$. Differentiate
$`V=u(H-t)`$, and use $`E=-tC`$ and $`E'=-2HT`$, to obtain

```math
\frac{V_{pp}}u
=\chi\left\{(T/\Pi)'-(T/\Pi)^2(2H/t-1)\right\}-t\mathcal R.
```

The two polynomial identities

```math
h\Pi-T(2p+1)+T^2=E-hC=-(t+h)C,
\qquad
\Pi t(t+h)+\chi T^2=-a_3a_4
```

reduce the braces to $`Ca_3a_4/(\Pi^3t)`$, proving (8). Thus no
computer algebra certificate is needed for this exterior orientation.
It makes every right-main positive-contact stationary point a strict
maximum. The right part ends at zero, below c1. If the seam height is
above c1, its crossings start downward, and two crossings would already
force a down/up minimum. If the seam height is below c1, simple-crossing
parity makes the count even, and more than two crossings would start
up, down, up, down. In that event the second, downward crossing supplies
B/C>0 up to the third crossing, again forcing a minimum where (8)
permits only maxima. A/C and D/C are positive throughout. Thus the
right main contributes at most two nodes. A node at the seam is removed
by the original-function generic transfer, not counted twice.

The main component consequently has at most 1+2=3 nodes, without any
left-residue orientation or seam-minimum theorem. Therefore the total is

```math
0+3+1+1=5<7.
```

## 6. The other placement: the signed height comparison

Suppose $`\epsilon_-<\gamma_1<\gamma_2`$. Now E>0 throughout
the central interval; Qv>0 at its endpoints and (3) puts the entire
central interval after alpha. Thus A/C>0 there. The local central
orientation gives a single strict central maximum; the witness (6)
gives exactly two central nodes. The tail again has A/C<0 and gives
exactly one node.

If E(gamma3)<0, D has two central roots and its third root between
r3 and gamma3. The E/C residues have signs d1<0<d2,d3. The initial
positive component has A/C<0 and zero endpoints, so contributes no
nodes. On the left main component, B/C is strictly increasing, because

```math
\sum_i d_i(\gamma_i+1)
=\frac H\Lambda\{h(\textstyle\sum_i r_i+1+1/\Lambda)-2m\}>0,
```

and the negative residue has the farthest denominator for p>gamma3.

If two left-main nodes existed, the first would be downward and would
supply B/C>0. The second would be upward and would supply A/C>0,
equivalently P_v>0 on this left branch. By (3) it lies before alpha;
therefore A/C stays positive between the first two nodes. D/C is positive
throughout the main. The new left positive-contact theorem makes V_p
strictly negative there, whereas a down/up pair forces a minimum. Thus
the left main contributes at most one node.

On the right main, the signed metric theorem makes every
finite stationary height larger than V(y)>c1. Since the component ends
at infinity, two or more level hits would force a minimum below c1.
Thus the right main contributes at most one node, independent of the
seam height M and with no positive-contact assumption at that minimum.
The total is

```math
0+2+2+1=5<7.
```

If E(gamma3)>0, the third D root instead lies after gamma3. At gamma3,
Qv=-gamma3E<0, so (3) places alpha strictly before x(gamma3). On the
positive component from x(delta3), through the seam, to x(gamma1),
A/C is negative on both physical branches. This component goes from
zero to infinity. Every regular positive level must have an upward
crossing, which would require A/C>0. This is impossible.

These are the only two E placements and the only sign alternative
needed inside the second placement. None is a scale or discriminant
classification; all follow from the one actual saturated row.

## 7. Boundary transfer and proof savings

A hypothetical row with ten distinct roots is first regularized using
one common original coefficient, then sufficiently small common support
and coefficient perturbations retaining ten compact sign brackets.
All strict source inequalities (1) remain open. Avoid finitely many
proper algebraic coincidences: auxiliary multiple roots, C/E common
roots, simultaneous P_v=P_w=0 at the auxiliary ratio maximum, the auxiliary ratio
maximum at the seam, and a level node at the seam.
The generic contradiction applies. This is original-function boundary
transfer; no common-height nodes are independently perturbed.

The whole smaller-gap source region (1) is therefore excluded at every
scale, giving (MH-R). The new proof removes from this region:

- the global one-real-root/nonreal-pair theorem for P_v/Qv;
- the outside-x=1 real-root exclusion and its scale inequalities;
- the lower/upper scale barriers Lambda_uv, Lambda_V, Lambda_CE and
  Lambda_E as routing inputs;
- the three final leading-sign dispatches in SIGNED;
- the separate no-physical-C/off-branch-C discrimination, since an actual
  bad row forces the physical two-pole cell directly.

It retains three local geometric kernels, including the central exact
certificate, plus the global root/generic-transfer input. These are
explicit mathematical dependencies, not omitted case proofs. The
result is one new regional master-height proof; it does not claim that
all original comparable mode cases or the entire source-wide master
have disappeared.
