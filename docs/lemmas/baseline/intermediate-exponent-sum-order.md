# The exponent-sum order $0<S_1<S_3<S_2$

Let

$$
F=A_0+A_1m_1-B_0m_2-B_1m_3,
 \quad m_1=x^a(1-x)^{-b},\quad m_2=x^e(1-x)^d,
 \quad m_3=x^c(1-x)^{-f},
$$

where all four coefficient magnitudes are positive and

$$
0<e<a<c,\qquad 0<f<b,\qquad d>0,\qquad 0<x<1.
\tag{F3}
$$

Set

$$
S_0=0,\quad S_1=a-b,\quad S_2=e+d,\quad S_3=c-f.
$$

Every original root statement counts distinct roots and excludes an identity.

The complete sector is

$$
\boxed{0<S_1<S_3<S_2.}                                  \tag{I}
$$

The following preceding reductions are used. They are mathematical prerequisites of the sector assembly; the exterior barrier proved here does not establish them by itself:

1. The four mixed rectangles: if both entries of any of (a,b), (c,f), (a-e,b+d), (c-e,d+f) are at most two, the original bound is eight, with the stated integer and support-limit qualifications.
2. The cofactor count/exterior reduction in order I. If P=e0/LC(e0), Q=e1/LC(e1), then LC(e0)>0 and LC(e1)<0. Q has one root q_minus<0, one physical root q, and one root q_plus>1. If P(q_plus)>0, the original bound is eight. In particular, this covers the three-physical-root e0 case.
3. If P(q_plus)<0 remains, P has one physical root p and two right-exterior roots

$$
1<p_-<q_+<p_+.
\tag{1.1}
$$

4. All order-I rows with b>=1 are already proved by a deflated phase inequality.

## 2. Source reconstruction and a four-gap polynomial

Let rho=x(1-x), D_x=rho d/dx, lambda_r=r1-(r1+r2)x, and

$$
H(r,s)=\lambda_rD_x\lambda_s-\lambda_sD_x\lambda_r
       +\lambda_r\lambda_s(\lambda_s-\lambda_r).
$$

For supports (0,(a,-b),(e,d),(c,-f)), the signed cofactors are

$$
e_0=H((e-a,d+b),(c-a,b-f)),\quad
 e_1=-H((e,d),(c,-f)),
$$

$$
e_2=H((a,-b),(c,-f)),\quad e_3=-H((a,-b),(e,d)).
$$

They have degree at most three and endpoint signs (-,-,+,+) at zero and (+,+,-,-) at one. Their leading coefficients follow by expanding the displayed cubic formulas.

Introduce strictly positive support gaps

$$
h=a-e,\qquad k=c-a,\qquad v=b-f,\qquad D=d+f.
\tag{2.1}
$$

Here D is a scalar gap, distinct from the operator D_x. Then

$$
e_0=H((-h,D+v),(k,v)).
$$

In order I,

$$
\boxed{D>h+k,}
\tag{2.2}
$$

because S2-S3=D-h-k>0.

Set x=1+z. Define

$$
\mathcal A=D+v+(D+v-h)z,\quad
 \mathcal B=v+(k+v)z,\quad
 \mathcal C=D+(D-h-k)z,
$$

$$
\Delta=Dk+v(h+k)>0.
$$

Direct original differentiation gives

$$
\boxed{e_0(1+z)=\mathcal A\mathcal B\mathcal C-\Delta z(1+z).}
\tag{2.3}
$$

This formula uses the original six exponents through their four actual differences. It is not an arbitrary choice of an auxiliary cubic.

## 3. The exterior-root barrier

### Lemma 3.1

If D>h+k and D>1, then

$$
\boxed{e_0(x)>0\quad\text{for every }1\le x\le D.}
\tag{3.1}
$$

In particular, every right-exterior root of e0 lies strictly beyond D.

**Proof.** For z>=0, (2.2) gives

$$
\mathcal A>D,\qquad \mathcal C\ge D,\qquad
 \Delta<D(k+v).
$$

Thus

$$
\begin{aligned}
 e_0(1+z)
 &>D^2\{v+(k+v)z\}-D(k+v)z(1+z)\\
 &=D^2v+D(k+v)z(D-1-z).
\end{aligned}
\tag{3.2}
$$

For 0<=z<=D-1 this is at least D^2v>0. Strictness at z=0 follows from A>D and B=v>0. This proves the lemma, including x=D.

The strict remainder can also be written as

$$
\begin{aligned}
&e_0(1+z)-\{D^2v+D(k+v)z(D-1-z)\}\\
&\quad=(\mathcal A\mathcal C-D^2)\mathcal B
       +v(D-h-k)z(1+z),
\end{aligned}
\tag{3.3}
$$

and

$$
\mathcal A\mathcal C-D^2
 =(\mathcal A-D)\mathcal C+D(\mathcal C-D)>0.
$$

With D=h+k+g, g>0,

$$
\mathcal A-D=v+(k+g+v)z>0,\qquad \mathcal C-D=gz\ge0.
$$

## 4. The barrier gives the missing fixed-level height theorem

Retain the only exterior configuration not already handled by the positive-evaluation reduction:

$$
P=(x-p)(x-p_-)(x-p_+),\quad
 Q=(x-q_-)(x-q)(x-q_+),
$$

$$
q_-<0,\quad p,q\in(0,1),\quad 1<p_-<q_+<p_+.
\tag{4.1}
$$

The globally monotone anchor {2,3} has score

$$
\lambda_3-\lambda_2=(c-e)(1-x)+(d+f)x>0.
$$

Its complementary residual is, up to a strictly positive multiplier,

$$
A_1m_1e_0-A_0e_1.
$$

The derivative identity gives this expression atom by atom; B0 and B1 are annihilated. Since the normalization constants L_P=LC(e0)>0 and L_Q=LC(e1)<0 have opposite signs, the useful set is PQ<0, and its equation is

$$
\phi=\log|Q/P|-a\log x+b\log(1-x)=\Lambda,
$$

$$
\boxed{\Lambda=\log\frac{A_1L_P}{A_0(-L_Q)}.}
\tag{4.2}
$$

The coefficient level is fixed by the original coefficients and is not changed from component to component.

Deflate the physical roots and define

$$
\mathscr H(x)=
 \log\left|\frac{(x-q_-)(x-q_+)}{(x-p_-)(x-p_+)}\right|
 -a\log x+b\log(1-x).
$$

It is smooth on the entire interval (0,1), and

$$
\phi=\mathscr H+\log\left|\frac{x-q}{x-p}\right|.
\tag{4.3}
$$

### Lemma 4.1: large exterior roots make the deflated phase decrease

If a>=2 and p_->2, then

$$
\boxed{\mathscr H'<0\quad(0<x<1).}
\tag{4.4}
$$

Indeed the exact positive margin is

$$
\boxed{
\begin{aligned}
 \frac{2-a}{x}-\frac b{1-x}-\mathscr H'
 ={}&\frac{-q_-}{x(x-q_-)}
 +\frac{p_--2x}{x(p_--x)}\\
 &+\frac{p_+-q_+}{(q_+-x)(p_+-x)}>0.
\end{aligned}}
\tag{4.5}
$$

All three terms are strictly positive. The asserted upper bound for H' is itself strictly negative for a>=2 and b>0.

More generally, if p_->D>1, the same calculation gives

$$
\begin{aligned}
&\frac{D/(D-1)-a}{x}-\frac b{1-x}-\mathscr H'\\
&=\frac{-q_-}{x(x-q_-)}
 +\frac{p_--Dx}{(D-1)x(p_--x)}
 +\frac{p_+-q_+}{(q_+-x)(p_+-x)}>0.
\end{aligned}
\tag{4.6}
$$

Thus a>=D/(D-1) is another sufficient condition. Only the simpler a>2,D>2 consequence is needed for the full sector union.

### 4.1 Both possible physical root orders are covered

If p<q, the useful components are (0,p) and (q,1). For any U in the first and V in the second, H(U)>H(V). Moreover

$$
\log\left|\frac{U-q}{U-p}\right|>0,
 \qquad
 \log\left|\frac{V-q}{V-p}\right|<0.
$$

Therefore

$$
\boxed{\phi(U)>\phi(V).}
\tag{4.7}
$$

A fixed finite level can occupy at most one useful component.

The derivative numerator

$$
T=\rho(Q'P-QP')+[(a-b)x-a]PQ
$$

has degree seven, leading coefficient a-b>0, and positive nonzero values at both physical endpoints. Its physical root count with multiplicity is therefore even and at most six. On the one occupied component, Rolle gives at most seven residual roots. The two original pole-free Rolle steps give at most nine original roots.

If q<p, the useful components are (0,q) and (p,1). The singular logarithm in (4.3) has derivative

$$
\frac{q-p}{(x-q)(x-p)}<0
$$

on both components. Hence phi is strictly decreasing on each and the residual has at most two roots. This is more than enough for the target.

The special cofactor words 0231 and 1320 project respectively to these two physical root orders. The analytic theorem does not depend on the event enumeration.

## 5. Whole-sector assembly: order I is complete

Every generic row in order I is covered by the following exhaustive alternatives.

* If b>=1, use the preceding $b\ge1$ height reduction (together with its positive-evaluation exterior gate).
* If b<1 and a<=2, use the retained mixed rectangle (a,b).
* If b<1, a>2, and D=d+f<=2, use the retained mixed rectangle (c-e,d+f): order I gives c-e=h+k<D, so both entries are at most two.
* The only remaining case has a>2, b<1, D>2. If P(q_plus)>0, the retained exterior-contact theorem applies. Otherwise the generic remainder has (4.1). Lemma 3.1 forces p_->D>2, so Lemma 4.1 and the two-order argument give the original bound.

The three-physical-root e0 sector belongs to the positive-evaluation case and is not reopened. A common-root equality P(q_plus)=0 is a proper algebraic seam and is handled by the all-generic-row argument and original-root transfer, not by pretending that one open sign side is the other.

Thus

$$
\boxed{0<S_1<S_3<S_2\quad\Longrightarrow\quad Z(F)\le8.}
\tag{5.1}
$$

For generic original roots, the original A0 term dominates near zero and the positive A1 term dominates near one because b>f. Their endpoint signs are both positive. Hence the nine-root ceiling above improves to eight by parity.

For arbitrary distinct roots, make a sufficiently small shift of the positive constant coefficient. Odd-order roots retain a crossing for either shift sign. If e_plus,e_minus count even roots split by the two signs and o counts odd roots, the better shift retains at least o+2 max(e_plus,e_minus)>=o+e_plus+e_minus simple crossings. Choose a noncritical shift and disjoint compact sign-changing brackets. A sufficiently small generic support perturbation preserves them and remains in the proved strict sector. This gives the eight-distinct-root conclusion and the support closure with signs preserved. No unresolved open order-II region is absorbed as a boundary.
