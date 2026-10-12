# One comparable-atom theorem for F1 and endpoint cancellation

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

For an exponent vector $`s=(s_1,s_2)`$ write

```math
m_s=x^{s_1}(1-x)^{s_2},\quad \rho=x(1-x),\quad
 D=\rho\frac{d}{dx},\quad
 \lambda_s=s_1-(s_1+s_2)x.
```

 Comparability is coordinatewise and all displayed inequalities are strict.

#### Theorem.

Let $`A,B,C>0`$ and

```math
F=1+A m_u-Bm_v-Cm_w.
```

 Suppose all coordinates of $`u,v,w`$ are positive, $`u`$ and $`v`$ are comparable, and both lie northwest of $`w`$:

```math
u_1<w_1,\quad v_1<w_1,\qquad
 u_2>w_2,\quad v_2>w_2,
```

 with either $`u_1<v_1,\ u_2<v_2`$ or $`u_1>v_1,\ u_2>v_2`$. Then $`F`$ has at most eight distinct roots in $`(0,1)`$.

The case $`v<u`$ is the whole F1 domain. The case $`u<v`$ is the whole endpoint-cancellation domain of Theorem 6.1 of source s009. Thus the same proof replaces both domains; it does not require an exhaustion by affine inequalities or a regular-Wronskian small-gap complement.

#### Retained two-term counting input.

A nonidentity equation

```math
P(x)+x^\alpha(1-x)^\beta Q(x)=0
```

 with polynomial degrees $`p,q`$ has at most $`p+q+2`$ distinct roots in $`(0,1)`$, subject to the usual common-factor reduction. This is the input already stated as equation (1) of the review manuscript and Theorem 1.3 of El-Hilany–Tavenas, arXiv:2409.01651v1. The proof below only needs it for a quadratic and a cubic.

#### The endpoint operator.

For $`0<\theta<1`$ and $`k\leq1`$ let

```math
\mathcal L f=\rho f''+k(\theta-x)f'+kf.
```

 It annihilates $`\theta-x`$ and loses at most two distinct roots. For completeness, $`h_0=x^{1-\theta}(1-x)^\theta`$ satisfies

```math
\mathcal Lh_0/h_0=-(1-k)\theta(1-\theta)/\rho\leq0.
```

 Writing a kernel solution as $`h=h_0z`$ gives $`z''+pz'-Vz=0`$ with $`V=(1-k)\theta(1-\theta)/\rho^2\geq0`$. From interior data $`z=1,z'=0`$, the identity $`(\mu z')'=\mu Vz`$ for a positive integrating factor shows that $`z`$ never reaches zero on either side of the initial point. Hence $`h>0`$. The Wronskian of $`h`$ and $`\theta-x`$ is nonzero by Abel’s identity (and equals $`-h(\theta)`$ at $`x=\theta`$). For the regular coordinate $`\tau=(\theta-x)/h`$, writing $`f=hV_0(\tau)`$ gives $`\mathcal Lf=\rho h(\tau')^2 V_0''(\tau)`$, proving the two-root loss by Rolle.

For $`f_s=\lambda_{s-w}m_s`$, define its cubic core by

```math
\rho\mathcal Lf_s=m_s C_s,\qquad \deg C_s\leq3.
```

 If $`T_1=1-k\theta`$ and $`T_2=1-k(1-\theta)`$, direct differentiation gives

**(A)**

```math
C_s(0)=(s_1-w_1)s_1(s_1-T_1),\qquad
 C_s(1)=-(s_2-w_2)s_2(s_2-T_2).
```

#### A single auxiliary ratio.

Let $`r=\max(u,v)`$ and $`\ell=\min(u,v)`$ coordinatewise. Put

**(B)**

```math
\theta=\frac{w_1}{w_1+w_2},\qquad
 k_{*} =\min\left\{\frac{1-r_1}{\theta},
                  \frac{1-r_2}{1-\theta}\right\}.
```

 First consider $`k_{*}\leq1`$ and choose $`k=k_{*}`$. Then $`T_i\geq r_i`$ for both coordinates, with equality in at least one coordinate. Consequently the higher core $`C_r`$ has a factor $`x`$ or $`1-x`$. The lower core has the strictly positive endpoints

**(C)**

```math
C_\ell(0)>0,\qquad C_\ell(1)>0,
```

 since $`\ell_1<w_1`$, $`\ell_2>w_2`$ and $`\ell_i<r_i\leq T_i`$.

The first beta annihilation gives the exact identity

```math
G=(D-\lambda_w)F=-\lambda_w+A f_u-B f_v.
```

 Since $`\mathcal L\lambda_w=0`$, its operator residual is

**(D)**

```math
R=\rho\mathcal LG=A m_u C_u-Bm_v C_v,
 \qquad Z(F)\leq Z(R)+3.
```

 Absorb the endpoint factor of the higher core into its beta exponent. The residual becomes a beta-weighted quadratic plus a beta-weighted cubic, and so has at most seven distinct roots. Crucially, the lower atom dominates at *both* endpoints, even after an exponent of the higher atom has been increased by one. By (C), $`R`$ therefore has the same sign at both endpoints: positive if $`\ell=u`$, negative if $`\ell=v`$. For generic parameters and coefficients its roots are simple, hence there are at most six. Equation (D) gives at most nine original roots. Their positive original endpoint signs reduce this to eight. If $`R`$ vanishes identically, $`G`$ lies in the disconjugate kernel and has at most one root unless it vanishes identically; integrating the first annihilator then gives at most two original roots. That exception therefore also satisfies the theorem.

#### The complementary region uses the same interpolation lemma.

If $`k_{*}>1`$, (B) gives

```math
r_1<1-\theta,\qquad r_2<\theta.
```

 In particular $`0<u_1,u_2<1`$. No information about the modes of $`u`$ or $`v`$, or about a zero-free third Wronskian, is needed.

Set

```math
H(p,q)=\lambda_pD\lambda_q-\lambda_qD\lambda_p
        +\lambda_p\lambda_q(\lambda_q-\lambda_p),
```



```math
P=H(w-v,u-v),\qquad Q=-H(w-v,-v),\qquad
 L=\lambda_{w-v}>0.
```

 The pole-free negative-pair reduction is

**(E)**

```math
D\left(\frac{D(F/m_v)}{D(m_w/m_v)}\right)
 =\frac{m_{-w}}{L^2}\,[A m_uP-Q].
```

 Writing $`u=(a,b),v=(c,d),w=(e,f)`$, the cubic endpoints are

```math
P(0)=-(e-c)(e-a)(a-c),\qquad
 P(1)=(d-f)(b-f)(b-d).
```

 They have opposite signs because $`(a-c)(b-d)>0`$. Thus $`P`$ is nonzero and has an interior root.

The interior-root interpolation lemma of the review therefore applies: if $`P,Q`$ have degree at most three, $`P`$ has an interior root, and $`0<a,b<1`$, then $`Q=A x^a(1-x)^bP`$ has at most seven distinct solutions. Two Rolle steps in (E) give nine original roots, and positive endpoint parity gives eight in the generic case. The lemma is the same for both comparable orientations; its proof uses no source-specific cofactor order.

#### Distinct roots and seams.

The generic endpoint argument transfers to arbitrary distinct original roots as follows. For a finite set of distinct roots, a small change of the positive constant coefficient can be chosen to produce at least as many nearby simple crossings: odd-order roots each preserve one crossing, while one of the two shift signs splits at least half of the even-order roots into two. Avoiding the countably many critical values makes all crossings simple. Next perturb the supports and the other coefficients, preserving these compact crossing brackets, to a generic row of the proved strict domain. The signs of the coefficients and endpoint limits remain fixed. Thus a row with more than eight distinct roots would give a generic row with more than eight simple roots, a contradiction. This also covers $`k_{*}=1`$, equal auxiliary ratio branches, and nonidentity finite support limits of the stated domain.

#### What is eliminated.

The shared higher-atom auxiliary ratio replaces the separate F1 localization input, the two affine endpoint inequalities for the endpoint-cancellation family, their exhaustiveness argument, and its regular-Wronskian small-gap proof. The two retained analytic tools are the existing endpoint operator and interior-root interpolation; the polynomial counting input and generic-to-distinct transfer remain. No claim is made for incomparable $`u,v`$, for an atom lying southeast of $`w`$ in either coordinate, or for F2, F3, and F4.
