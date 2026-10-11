# One shared height in the two derivative ratios

This is the original shared-coefficient entry used by the later height theorems. The coefficients in both ratios belong to one original equation. The obsolete middle-mode continuation is replaced by [the origin-interior proof](middle-height-by-convexity.md). The arguments below supply the seven required contacts and their actual-height signs; they do not independently establish a complete height theorem.

Read [the appendix terminology](../../appendix.md#terminology) before this lemma.

## 1. Original coefficients and the two quotients

The original comparable row is

$$
f=1-E_-M_- -E_+M_+ -E'_+M'_+,
\quad E_-,E_+,E'_+>0,
$$

$$
\operatorname{supp}M_-\prec0\prec\operatorname{supp}M_+
\prec\operatorname{supp}M'_+,
$$

where each M is a beta function $x^a(1-x)^b$ and $\prec$ means strict comparison in both exponent coordinates. Multiplication by $-1/M_-$ gives

$$
G=c_1-u+c_3v+c_4w,
\quad(c_1,c_3,c_4)=(E_-,E_+,E'_+),
\tag{1}
$$

$$
u=1/M_-,\quad v=M_+/M_-,\quad w=M'_+/M_-,
\quad0\prec\operatorname{supp}u\prec\operatorname{supp}v
\prec\operatorname{supp}w.
\tag{2}
$$

All three beta functions vanish at both endpoints. No coefficient has been absorbed differently at different nodes.

Put

$$
q=w/v,\qquad F=(u-c_1)/v.
$$

Then the same row has two representations

$$
G/v=c_3+c_4q-F,
\qquad
G/w=c_4+c_3/q-F/q.
\tag{3}
$$

Define

$$
L_4=\frac{dF}{dq},\qquad
L_3=\frac{d(F/q)}{d(1/q)}=F-qL_4.
\tag{4}
$$

Away from the single mode of q, zeros of $(G/v)'$ are exactly hits $L_4=c_4$, and zeros of $(G/w)'$ are exactly hits $L_3=c_3$. The derivative relation is

$$
\boxed{(L_3)_x=-q(L_4)_x.}
\tag{5}
$$

The notation L3,L4 labels the original coefficients c3,c4. Both functions in (4) depend on the same c1 and the same support triple.

## 2. Raw cubic cores and a global seven-node theorem

For this section the negative term u may have any mode order. Generically the modes of v,w differ; reflect x if necessary so $\rho_w<\rho_v$. Write

$$
v=x^a(1-x)^b,\quad q=x^{a_q}(1-x)^{b_q},
\quad\Delta=ab_q-ba_q>0.
$$

Set

$$
\omega=x(1-x),\quad L_v=a-(a+b)x,
\quad L_q=a_q-(a_q+b_q)x.
$$

There are unique real h,n such that $u=v^h q^n$; put $m=h-1$, $H=1-h$, and $L_u=hL_v+nL_q$. The raw polynomial cores are

$$
\begin{aligned}
C_0&=L_v(L_v+L_q)L_q-\Delta\omega,\\
D_0&=(L_u-L_v)(L_u-L_v-L_q)L_q+m\Delta\omega,\\
K_0&=c_1C_0-uD_0.
\end{aligned}
\tag{6}
$$

C0 and D0 have degree at most three. K0 is a beta function times a cubic subtracted from a cubic. Direct differentiation, without using a fitted p-coordinate model, gives

$$
\boxed{
(L_4)_x=-\frac{K_0}{v q\omega L_q^2},
\qquad
(L_3)_x=\frac{K_0}{v\omega L_q^2}.}
\tag{7}
$$

At x=0 and x=1 the signs of C0 are respectively positive and negative:

$$
C_0(0)=a(a+a_q)a_q>0,
\quad C_0(1)=-b(b+b_q)b_q<0.
$$

Because u vanishes at both endpoints, K0 has the same endpoint signs and cannot be an identity.

The imported distinct-root theorem of El Hilany–Tavenas bounds K0 by eight roots. It is Theorem 1.2, printed page 3 of [arXiv:2409.01651v1](https://arxiv.org/pdf/2409.01651v1); the complete unchanged paper and attribution are included in the predecessor. We use the nonidentity, degree-three/degree-three case only. With generic simple roots, endpoint parity improves eight to seven.

**Theorem 1 (global shared-height saturation).** Suppose (1)–(2) have ten simple roots and the auxiliary data are generic. Then K0 has exactly seven simple roots $z_1<\cdots<z_7$. Both L4 and L3 have exactly nine hits of their respective common positive levels c4 and c3. At these seven nodes,

$$
\max\{0,L_4(z_1),L_4(z_3),L_4(z_5),L_4(z_7)\}
<c_4<\min\{L_4(z_2),L_4(z_4),L_4(z_6)\},
\tag{8}
$$

$$
\max\{0,L_3(z_2),L_3(z_4),L_3(z_6)\}
<c_3<\min\{L_3(z_1),L_3(z_3),L_3(z_5),L_3(z_7)\}.
\tag{9}
$$

**Proof.** Rolle applied separately to the two expressions (3) gives at least nine hits of each derivative ratio. Both ratios have one common generic simple pole, at the mode of q. Their stationary points away from that pole are precisely the zeros of K0, by (7). Nine hits on one side of the pole would require at least eight stationary points and is impossible. On the two sides together, nine hits require at least seven stationary points. The preceding bound therefore forces exactly seven.

Seven stationary points and one pole give exactly nine monotonicity intervals for each ratio. Every interval must contain one hit of its common level. Hence every local maximum exceeds its target level and every local minimum lies below it. By (7), K0 starts positive and alternates sign at its seven roots: odd-index nodes are L4 minima and L3 maxima, while even-index nodes are L4 maxima and L3 minima. Positivity of the actual coefficients gives (8)–(9). ∎

In particular, every L4 maximum must be positive, and every L3 maximum must be positive. These are consequences of two common levels; they are not independent coefficient choices at the critical nodes. The theorem is a necessary condition for ten roots, not a claim that (8)–(9) alone suffice to construct ten roots.

With $s=\log q$, put

$$
p=L_v/L_q,\qquad
\Pi=dp/ds=\frac{\Delta\omega}{L_q^3}
=\lambda\prod_{i=1}^3(p-r_i),
$$

$$
0<r_1<r_2<r_3,
\quad(r_1,r_2,r_3)=
\left(\frac b{b_q},\frac{a+b}{a_q+b_q},\frac a{a_q}\right).
\tag{10}
$$

The left original branch has $r_3<p<\infty$, $q_x>0$, $\Pi>0$. The right original branch has $-\infty<p<r_1$, $q_x<0$, $\Pi<0$. In each branch p increases with x. The two infinities represent the same q-mode seam.

Retain exactly the predecessor's polynomials

$$
\begin{aligned}
k&=mp+n,& C&=p(p+1)-\Pi,\\
E&=mhp^2+2mnp+n(n-1),&D&=E-mC,\\
A&=nC+pE,&B&=(h-n)C-(p+1)E,\\
J&=\Pi(EC'-E'C)-(p+k)CD.
\end{aligned}
\tag{11}
$$

Here primes mean p derivatives. One has $C_0=L_q^3C$, $D_0=L_q^3D$. At every generic critical node of Theorem 1,

$$
\boxed{
c_1=V:=uD/C>0,
\quad L_4=(u/w)A/C,
\quad L_3=(u/v)B/C.}
\tag{12}
$$

Thus **C>0 at one of these nodes automatically entails D>0**. This supplies the height condition missing from the preceding derivative-maxima argument, because it uses the original c1 before eliminating the other two coefficients.

Two further exact identities are

$$
V_p=-\frac{uJ}{\Pi C^2},
\qquad
(L_4)_x=\frac{Cq_x}{vq^2}(V-c_1)
\tag{13}
$$

where the denominators are nonzero. Since $(L_3)_x=-q(L_4)_x$, a crossing of V through c1 determines which ratio has a maximum:

| Branch and C sign | Downward V crossing | Upward V crossing |
|---|---|---|
| Left branch, C>0 | L4 maximum | L3 maximum |
| Left branch, C<0 | L3 maximum | L4 maximum |
| Right branch, C>0 | L3 maximum | L4 maximum |
| Right branch, C<0 | L4 maximum | L3 maximum |

This table is checked independently by finite sign arithmetic.

