# Exactly one simple contact before the four roots in order $`0231`$

Use the actual F3 cofactors, assume one simple physical root for each, distinct physical roots in order $`0231`$, and genuinely nonreal conjugate pairs for the other roots of $`E_1`$ and $`E_3`$. There is exactly one contact before all four physical roots, and that contact is simple. This lemma supplies the left count; the separate right argument is still required.

## Scope and retained prerequisite

The source is

```math
m_1=x^a(1-x)^{-b},\quad m_2=x^e(1-x)^d,\quad m_3=x^c(1-x)^{-f},
```

with $`0<e<a<c`$, $`0<f<b`$, $`d>0`$, and $`0<e+d<a-b<c-f`$. In odds $`t=x/(1-x)`$, put $`\rho=t(1+t)`$ and $`\ell_1=a+bt,\ell_2=e-dt,\ell_3=c+ft`$. The cofactors and contact determinant use the convention in [the real exterior-pair lemma](f3-real-exterior-pairs.md).

The retained fixed-root theorem gives negative roots

```math
u_2<u_0<v_2<v_0<-1
```

for E2 and E0 respectively, and one simple positive root for each physical cofactor. Word 0231 means $`t_0<t_2<t_3<t_1`$. This prerequisite is proved in [the fixed exterior-interlacing lemma](f3-fixed-exterior-interlacing.md).

## Original sign convention and anchor

Before the first physical root, $`E_0<0`$ and $`E_2>0`$, so $`R=-E_0/E_2>0`$ and $`\Psi=m_2R>0`$. Its endpoints are zero: at $`t=0`$ this follows from $`e>0`$, and at $`t=t_0`$ from the simple E0 root and nonzero E2.

The generic score crossing is $`y=(c-a)/(b-f)>0`$. The original E2 source determinant gives

```math
E_2(y)=(af-bc)y(1+y)<0.
```

Here $`af-bc<0`$ follows directly from $`f<b`$ and $`a<c`$. Since E2 is positive at zero and has its unique physical zero at $`t_2`$, it follows that $`y>t_2>t_0`$. Thus $`\ell_3-\ell_1>0`$ throughout the left interval. The determinant Jacobi identity is

```math
\Psi'=-\frac{m_2(\ell_3-\ell_1)}{\rho E_2^2}K.
```

All prefactors are strictly nonzero. At a contact, the phase-curvature sign is therefore the negative of the K derivative sign. A positive local odds change preserves this statement. Notice that the point inequality $`LS\delta-GH>0`$ equals **minus** the locally cleared E0 value; this is consistent with E0 being negative on the left.

## Premode coverage, including the seam

Write E0/E2 as the ratio of its three root factors. Pair $`u_0`$ with $`u_2`$, $`v_0`$ with $`v_2`$, and $`t_0`$ with $`t_2`$. Each pair contributes strictly negatively to $`(\log R)''`$ on $`(0,t_0)`$, because its E0 root is closer to the point than the corresponding E2 root. Thus $`(\log R)''<0`$.

For $`0<t\le e/d`$,

```math
(\log m_2)''=-\frac{e+2et-dt^2}{t^2(1+t)^2}<0,
```

since $`dt^2\le et`$. Every critical point at or before the mode is consequently a nondegenerate maximum. Equality $`t=e/d`$ has strictly negative curvature, so there is no missing seam.

## Postmode chart covers every actual contact

At a postmode point define

```math
L=a(1-x)+bx,\quad P=dx-e(1-x),\quad L+G=c(1-x)+fx,
```

```math
z=bx/L,\quad v=fx/(L+G),\quad W=dx.
```

The original strict source gives $`L,P,G>0`$, $`W>P`$, and $`0<v<z<x<1`$. To see $`z<x`$, use $`a>b`$; likewise $`v<x`$ uses $`c>f`$. The inequality $`z>v`$ is the normalized form of $`bc-af>0`$. Also $`q=L(z-v)-Gv=x(b-f)>0`$.

Set $`r=z-v,\delta=G-r,U=L+P,S=U+G`$, and $`H=W-P(S+v)`$. The E1 left sign gives $`H>0`$, and the E0 left sign gives $`LS\delta-GH>0`$; hence $`\delta>0`$ and $`0<\tau=\delta/G<1`$. The denominator $`\Delta=GH+P\delta S`$ is strictly positive. Define

```math
\eta=GHU/\Delta,\quad J=P(LS\delta-GH)/\Delta>0,\quad D=UP\delta S/\Delta>0.
```

The displayed definitions give $`J=L-\eta`$, $`D=U-\eta=J+P`$, $`\lambda=G+\eta>\eta`$, and $`k=v-\eta(1-\tau)`$. There is no restriction $`k\ge0`$.

The reverse source identities, valid before imposing the contact equation, are

```math
W=P[D+\lambda+k+\eta+\lambda\eta\tau/D],
```

```math
\frac{K(0)}{L(L+G)}=\Delta\big[x-(L+\lambda+2P+3k-1)\big].
```

Therefore every actual contact is represented by the stated chart, with only strictly positive denominators. These identities give the inverse map as well as the forward map at a contact.

## Source normalizations and the short identity

Fix the original point $`t_{*}=x/(1-x)`$, and use the local coordinate $`u=t/t_{*}-1`$. The locally cleared cofactors are $`(1-x)^3 E_i(t_{*}(1+u))`$. The local cubics are $`A=E_3/L`$ and $`B=-E_1/(L+G)`$, with these local cleared values understood. Both multipliers are positive. Define the quadratic $`D_q`$ by the following determinant identity. The numerator on the left is exactly divisible by the linear factor $`P+Wu`$, so this definition is polynomial:

```math
(W-Pv)A-(W-Pz)B=-(P+Wu)D_q.
```

Let $`\bar A=D^2A/P`$, $`\bar D=D^2D_q/(PG)`$, $`M=S+k`$, and

```math
T=2D(1-P-\eta-2k)+3J\eta\tau^2,
```

```math
Z=3k^2+(2L+4P-3)k+(P-1)(U-1),\quad F=\lambda T-2DZ.
```

The original determinant gives

```math
K_1=\frac{PG\tau SU}{D^2}F
```

for the coefficient of u in K divided by $`L(L+G)`$. Thus a contact with nonnegative phase curvature would have $`F\le0`$.

The central polynomial identity is

```math
S\bar A+\lambda(1+Mu)\bar D=u^2(T_1+T_2u),
```

```math
2T_1=US(D+\lambda\tau)(F-\lambda\eta J\tau^2).
```

The constant and linear coefficients vanish identically. Every displayed multiplier is strictly positive; hence $`F\le0`$ implies $`T_1<0`$, including equality $`F=0`$.

## Fixed-pole and quadratic signs

Write $`F_s=a-b,S_s=e+d,C_s=c-f`$. The source formulas at the original nonphysical pole $`t=-1`$, which is $`u=-1/x`$, are

```math
\bar A(-1/x)=\frac{D^2(1-x)^3F_sS_s(F_s-S_s)}{PL}>0,
```

```math
\bar D(-1/x)=\frac{D^2x(1-x)^3}{PGL(L+G)}
\{S_s(af-bc)(F_s-S_s)-(ad+be)C_s(C_s-F_s)\}<0.
```

The inequalities use only the strict canonical source ordering. In particular they do not use a floating-point discriminant or a numerical root calculation.

Moreover $`\bar D(0)=-\tau SUD<0`$. With $`W_0=DW/P`$, $`C_\lambda=D+\lambda\tau`$, and $`\gamma=1-\tau`$, its leading coefficient is exactly

```math
(J\gamma-k)[DzW_0+DvUC_\lambda]+W_0Dzv+PW_0^2\gamma>0.
```

Here $`J\gamma-k=q/G>0`$ and $`W_0-Dz=UC_\lambda>0`$. Consequently the quadratic is strictly convex and negative throughout $`(-1/x,0)`$: it lies below the negative chord joining its endpoint values.

Finally $`Y=M-x=1-P-\eta-2k>0`$, because

```math
2Y=(1-x)+G+J\tau+q/G>0.
```

Evaluating the short identity at $`-1/x`$ gives $`T_1-T_2/x>0`$, since $`\bar A>0`$, $`\bar D<0`$, and $`1-M/x<0`$. Thus $`T_2<xT_1<0`$, and $`\ell=-T_1/T_2`$ lies strictly in $`(-1/x,0)`$.

## Resultant orientation and word sign

The exact formal degree-three/degree-two identity is

```math
\operatorname{Res}(\bar A,\bar D)
=\frac{\bar D(0)^2T_2^2}{S^2}\bar D(-T_1/T_2)<0.
```

The displayed definitions give this for generic coefficients in $`\bar D=d_0+d_1u+d_2u^2`$, independently of the source specialization. Its equivalent coefficient form is

```math
\frac{d_0^2}{S^2}(d_2T_1^2-d_1T_1T_2+d_0T_2^2).
```

Swapping resultant order introduces $`(-1)^{3\cdot2}=1`$, so no hidden sign reversal occurs.

On the other hand, both-complex word 0231 gives one real root $`\alpha`$ of A and one real root $`\beta>\alpha`$ of B, with the other roots conjugate. Both cubic leading coefficients are negative. Hence $`B(\alpha)>0`$. The common-quadratic identity gives

```math
D_q(\alpha)=\frac{(W-Pz)B(\alpha)}{P+W\alpha}>0.
```

The denominators are positive: $`\alpha>0`$ because the contact point lies before all physical cofactor roots, and $`W-Pz=A(0)+P(L+P)>0`$. Evaluating the degree-three/degree-two resultant at A's roots gives

```math
\operatorname{Res}(A,D_q)=a_{\rm lead}^2D_q(\alpha)|D_q(\zeta)|^2\ge0.
```

This contradiction excludes $`F\le0`$, so every postmode contact is a nondegenerate phase maximum.

## Uniqueness and multiplicity

Premode and postmode exhaust the interval and show every phase critical point is a nondegenerate maximum. The phase is positive inside and continuously zero at both endpoints, so it has an interior maximum. Two such maxima would require an intervening critical point whose derivative changes from negative to positive, or a degenerate stationary point; either contradicts strict negative curvature at every critical point. Thus the maximum is unique.

The exact Jacobi prefactor remains strictly nonzero on the entire left interval. Therefore the unique nondegenerate phase critical point corresponds to a simple K zero, not merely to one distinct zero of uncertain multiplicity.
