# Two real exterior cofactor roots force two exterior contact roots

The proof uses only the determinant of the actual four factors. Original coefficients and a ten-root assumption are not hypotheses.

A physical root of an $x$ polynomial lies in $(0,1)$; in the coordinate $t=x/(1-x)$ it is a positive root. A contact means a root of the contact determinant $K$, whose degree is at most six. Counting multiplicity means that a double polynomial root uses two degrees. A signed cofactor $e_i$ is the alternating three-by-three determinant obtained by omitting column $i$ from the first three derivative rows of the four factors. The four cofactors and $K$ share these actual factors; they are not independently chosen polynomials.

In the coordinate $t$, take the derivative $t(1+t)d/dt$. For an atom $m_i$, set $L_i=t(1+t)m_i'/m_i$. The first three normalized derivative rows are $1,L_i,L_i^2-S_it(1+t)$, where $S_i$ is its exponent sum in the original $x$ coordinate. Their signed cofactors are $E_i$. The four-row normalized determinant is $\mathcal K$. This specifies the signs used below.

## Statement

Keep the strict F3 family and exponent-sum order $0<e+d<a-b<c-f$:

$$
m_0=1,\quad m_1=x^a(1-x)^{-b},\quad
m_2=x^e(1-x)^d,\quad m_3=x^c(1-x)^{-f},
$$

$$
0<e<a<c,\quad0<f<b,\quad d>0,
\quad0<e+d<a-b<c-f.
$$

Assume all four signed cofactors have exactly one simple physical root. If either variable cofactor e1 or e3 has a real remaining pair, including a double real pair, then

$$
\boxed{K\text{ has at least two nonphysical polynomial roots,
counting multiplicity, and at most four distinct physical roots.}}
$$

The two nonphysical roots can be certified in negative odds, whose points other than $t=-1$ correspond to $x<0$ or $x>1$. Thus six jointly useful contacts are impossible in this entire real-pair region. The pure six-contact target reduces to the sector where **both variable cubics have genuinely nonreal conjugate pairs**.

This theorem does not require choosing either physical root order0231 or1320. It is distinct from original-level allocation theorems.

## 1. The odds polynomials and fixed-cofactor exterior roots

Write t=x/(1−x), and

$$
E_i(t)=(1+t)^3e_i(t/(1+t)),\qquad
\mathcal K(t)=(1+t)^6K(t/(1+t)).
$$

These are exactly the odds homogenizations of the original determinant, not independent cubics or a chosen sextic. Define

$$
A=a-e,\quad B=b+d,\quad r=c-a,\quad q=b-f,
$$

$$
L_1=a+bt,\quad L_2=e-dt,\quad L_3=c+ft,
\quad s_1=a-b,\quad s_2=e+d,\quad s_3=c-f.
$$

Order II says 0<s2<s1<s3, and A>B>0, r,q>0, B−q=f+d>0. Expanding the signed determinant gives the short identities

$$
E_2=L_1L_3(r-qt)-(bc-af)t(1+t),
$$

$$
E_0=(L_2-L_1)(L_3-L_1)(L_3-L_2)
+(Aq+Br)t(1+t),
$$

$$
E_3=L_1L_2(A+Bt)+(ad+be)t(1+t),
$$

$$
E_1=-\{L_2L_3(A+r+(B-q)t)+(cd+ef)t(1+t)\}.
\tag{1}
$$

Every formula follows directly from the normalized rows 1,L,L²−s*t; its determinant identities can be checked by hand.

The fixed cofactor E2 has negative leading coefficient and is positive at both negative infinity and t=−1, but

$$
E_2(-a/b)<0,\qquad\alpha_3:=-a/b<-1.
$$

Its two nonphysical roots therefore satisfy

$$
u_3<\alpha_3<v_3<-1.
$$

Its physical root supplies the third root, so these exterior roots are simple and are all its negative roots. E2 is positive outside (u3,v3) and negative inside it.

The fixed cofactor E0 has positive leading coefficient and is negative at negative infinity and t=−1. At

$$
\alpha_1:=-(c-e)/(f+d)=-(A+r)/(B-q)<-1
$$

its first determinant product vanishes and its remaining term is positive. Thus its two nonphysical roots satisfy

$$
u_1<\alpha_1<v_1<-1.
$$

Again the physical root supplies the third root; the two exterior roots are simple, E0 is negative outside (u1,v1), and positive inside. The same argument also brackets the other anchor zero −A/B, but that is not needed below.

## 2. Exact K evaluations at a variable-cofactor root

The determinant Jacobi identity, after the coordinate change, gives the full polynomial identities

$$
L_1\mathcal K=t(1+t)(E_2E_3'-E_3E_2')-(L_3-L_2)E_2E_3,
\tag{2a}
$$

$$
(L_3-L_2)\mathcal K=t(1+t)(E_0E_1'-E_1E_0')-L_1E_0E_1.
\tag{3a}
$$

The product terms in these identities also make the multiplicity arguments in Section 4 explicit. In particular, at an E3 zero

$$
\mathcal K(t)=\frac{t(1+t)E_2(t)E_3'(t)}{a+bt},
\tag{2}
$$

and at an E1 zero

$$
\mathcal K(t)=\frac{t(1+t)E_0(t)E_1'(t)}{c-e+(f+d)t}.
\tag{3}
$$

The anchor denominators vanish at alpha3 and alpha1 respectively. Neither can coincide with a relevant variable root: (1) gives

$$
E_3(\alpha_3)=(ad+be)\alpha_3(1+\alpha_3)>0,
$$

$$
E_1(\alpha_1)=-(cd+ef)\alpha_1(1+\alpha_1)<0.
\tag{4}
$$

The sextic has strict negative signs at each boundary of the two negative-odds slabs:

$$
\mathcal K(-\infty)<0,\qquad\mathcal K(-1)<0,
\qquad\mathcal K(0)<0.
\tag{5}
$$

At0 and infinity these are the source endpoint Vandermonde signs. At−1, the normalized jet columns are

$$
s_i,\quad s_i(s_i+1),\quad s_i(s_i+1)(s_i+2),
$$

so

$$
\mathcal K(-1)=s_1s_2s_3(s_2-s_1)(s_3-s_1)(s_3-s_2)<0.
$$

## 3. Two distinct real extra roots

Let C denote the variable cubic and P its partner: (C,P)=(E3,E2) or (E1,E0). Let sigma be their common sign at negative infinity,−1,0: sigma=+ for the first pair and sigma=− for the second. If the variable roots are a0<b0, their derivative signs are −sigma,+sigma.

If the pair lies in (−1,0), P has sign sigma there, the anchor numerator is positive, and t(1+t)<0. Equations (2)–(3) show that Kcal(a0)>0. Together with (5), this supplies two distinct negative-odds K roots.

If the pair lies in (−infinity,−1), it lies on one side of alpha. The fixed partner's roots u<alpha<v bracket alpha. On the left side of alpha, P changes sign once from sigma to −sigma; on the right it changes once from −sigma to sigma. Equations (2)–(3) give:

* left of alpha: signs Kcal(a0)=sigma*signP(a0), Kcal(b0)=−sigma*signP(b0);
* right of alpha: signs Kcal(a0)=−sigma*signP(a0), Kcal(b0)=sigma*signP(b0).

For both values to be negative, the fixed-partner sign would have to change in the wrong direction between a0 and b0. This is impossible. Hence Kcal is strictly positive at at least one of the variable roots. The negative signs at the ends of this slab again supply two distinct negative-odds K roots.

At a double extra root of C, (2)–(3) give Kcal(r)=0. If P(r)=0, the same local calculation gives multiplicity at least two. If P(r)!=0, differentiate the full Jacobi identity: the nonzero second derivative C''(r), partner P(r), and nonzero anchor show that Kcal'(r)!=0. Thus Kcal changes sign there; because it is strictly negative at both ends of its negative-odds slab, a second negative-odds root is necessary.

In every case at least two nonphysical degrees of the original K are consumed. Since degKcal<=6 and Kcal is nonzero by (5), at most four distinct physical K roots remain. This concludes the pure determinant theorem, including its real-pair boundary.
