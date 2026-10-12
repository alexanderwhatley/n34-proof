# A least support and comparable pairs

For a support vector $`s=(s_1,s_2)`$, put $`m_s=x^{s_1}(1-x)^{s_2}`$. A vector $`v`$ is coordinatewise below $`w`$ if $`v_1\le w_1`$ and $`v_2\le w_2`$. The number $`Z(F)`$ counts distinct roots in $`(0,1)`$; identities are excluded.

The principal statement is

```math
F=1+\alpha m_u-\beta m_v-\gamma m_w,\quad \alpha,\beta,\gamma>0,\quad u,v,w\ge0,\quad v\le w
\quad\Longrightarrow\quad Z(F)\le8.
```

This explains the name “least support”: the constant factor has support $`(0,0)`$ and lies below all the other supports. A companion statement gives $`Z(F)\le9`$ when each same-sign pair among four factors is coordinatewise comparable.

Two inputs are used. First, the two-polynomial beta-factor bound says a nonidentity $`P+x^a(1-x)^bQ`$ has at most $`\deg P+\deg Q+2`$ distinct roots. We abbreviate this bound by EHT below. Second, the retained lower-fork theorem gives eight when $`0<v_i<\min(u_i,w_i)`$ for both coordinates. The proof below explicitly identifies where this second input is used. The [limiting-cases lemma](limiting-cases.md) transfers strict conclusions to ties and multiple original roots.

Here $`\rho=x(1-x)`$, $`D=\rho\,d/dx`$, and $`\lambda_s=s_1-(s_1+s_2)x`$. A mode is the interior zero of this affine logarithmic-derivative factor when that zero exists. A Wronskian is the determinant whose rows contain successive derivatives of its columns. Its nonvanishing permits the divisions used in the repeated Rolle arguments.

The section and equation numbers below are local to this proof. They are retained to make cross references between the identities unambiguous.

## 3. A one-pole derivative budget and two immediate new rows

Set

```math
\rho=x(1-x),\qquad D=\rho\frac d{dx},\qquad
\lambda_s=s_1-(s_1+s_2)x.
```

For two support vectors define the cubic

```math
H(r,s)=\lambda_rD\lambda_s-\lambda_sD\lambda_r
       +\lambda_r\lambda_s(\lambda_s-\lambda_r).
\tag{3.1}
```

Its endpoint values are

```math
H(r,s)(0)=r_1s_1(s_1-r_1),\qquad
H(r,s)(1)=-r_2s_2(s_2-r_2).
\tag{3.2}
```

For the strict global-least F put

```math
S=\alpha m_u H(v,u)-\gamma m_w H(v,w),
\qquad g=\frac{DF}{Dm_v}.
```

Differentiation gives

```math
\boxed{Dg=\frac{m_vS}{(Dm_v)^2}.}
\tag{3.3}
```

The coefficient beta disappears. After division by a positive beta atom, S is a sum of two beta-weighted cubics; the external theorem gives Z(S)<=8. On a generic row, Dm_v has a single genuine pole location for g,

```math
\theta_v=\frac{v_1}{v_1+v_2},\qquad DF(\theta_v)\ne0.
```

If DF has M roots, distributed n_L,n_R over its two pole branches, branchwise Rolle gives

```math
Z(S)\ge\max(n_L-1,0)+\max(n_R-1,0)\ge M-2.
```

Therefore

```math
Z(DF)\le10.
\tag{3.4}
```

If S has opposite nonzero endpoint signs and all its roots are simple, its root count is odd, hence at most seven. In that case

```math
Z(DF)\le9.
\tag{3.5}
```

Generic support perturbations avoid proper exceptional identities. For fixed nonexceptional supports, varying the ratio of the two residual coefficients avoids critical values of their analytic ratio, so residual roots can be taken simple. A subsequent small change of the original coefficients preserves the selected original-root brackets. The limiting-cases lemma extends the resulting conclusion.

### 3.1 Endpoint contribution to the number of DF roots

For a generic global-least F with N roots, the first crossing is downward and the last crossing upward. Ordinary Rolle supplies N-1 roots of DF between consecutive F roots.

Because v<w coordinatewise, if u_i<v_i then the positive u atom dominates DF at the corresponding endpoint. At the left endpoint this makes DF positive, opposite to its sign at the first F crossing. At the right endpoint this makes DF negative, opposite to its sign at the last crossing. Each such endpoint supplies a further distinct derivative root outside the selected F-root range. Consequently

```math
Z(DF)\ge N-1+
\mathbf 1_{u_1<v_1}+\mathbf 1_{u_2<v_2}.
\tag{3.6}
```

There is no assumption that the derivative has no exterior roots. The additional roots are counted rather than forbidden.

### 3.2 Positive atom below both negative atoms

If 0<u<v<w coordinatewise, (3.6) gives Z(DF)>=N+1, while (3.4) gives Z(DF)<=10. Hence N<=9; endpoint parity makes N<=8. the limiting-cases lemma supplies the distinct-root and boundary extension.

This row does not use (LF).

### 3.3 Opposite ordering beyond the upper negative support

Suppose

```math
0<u_1<v_1<w_1,\qquad 0<v_2<w_2<u_2.
\tag{3.7}
```

At zero, the positive u contribution dominates S and H(v,u)(0)<0, so S<0. At one, the negative w contribution dominates S and H(v,w)(1)<0, so S>0. Equation (3.5) therefore applies. Equation (3.6) gives Z(DF)>=N, so N<=9 and hence N<=8 by parity. Reflection handles the other coordinate orientation.

This row also does not use (LF).

## 4. The crossed middle ordering: a zero-free third Wronskian

It remains, up to reflection, to treat

```math
0<u_1<v_1<w_1,\qquad 0<v_2<u_2<w_2.
\tag{4.1}
```

This is a genuine open chart. It is not part of the strict lower fork. The following small-gap lemma handles one part of it by a different, regular Wronskian flag.

### Lemma 4.1 — small opposite gaps

Assume u and v are positive and

```math
c=v_1-u_1\in(0,1],\qquad d=u_2-v_2\in(0,1].
\tag{4.2}
```

Then

```math
\boxed{H(v,u)(x)<0\quad\text{for every }0<x<1.}
\tag{4.3}
```

**Proof.** Put

```math
A=\lambda_v,\qquad B=-\lambda_u,\qquad
h=A+B=c(1-x)+dx,\qquad K=v_1u_2-u_1v_2>0.
```

The cubic (3.1) has the identity

```math
H(v,u)=hAB-K\rho.
\tag{4.4}
```

Since 0<h<=1, if AB<=0 the right side is strictly negative. If AB>0, use the exact rational sum-of-squares identity

```math
\boxed{
 v_1(K\rho-AB)=u_1[\lambda_v(x)]^2+v_2Kx^2>0.
}
\tag{4.5}
```

Thus hAB<=AB<Krho and (4.3) follows. This proves the sign on the entire interval, not only at a finite collection of points. QED.

### Lemma 4.2 — a regular three-function flag gives nine

Use the ordered basis

```math
f_1=m_v,\qquad f_2=m_u,\qquad f_3=1.
```

Its first three D-Wronskians are zero-free under (4.2):

```math
W_1=m_v>0,
\quad W_2=m_vm_u(\lambda_u-\lambda_v)=-h m_vm_u<0,
\quad W_3=m_vm_uH(v,u)<0.
\tag{4.6}
```

For any test function f, successively differentiate after division by these nonvanishing transformed basis functions. Explicitly,

```math
T_1f=D(f/f_1),\qquad
T_2f=D\left(\frac{T_1f}{T_1f_2}\right),\qquad
T_3f=D\left(\frac{T_2f}{T_2f_3}\right).
```

The determinant identities give

```math
T_1f_2=W_2/f_1^2,\qquad
T_2f_3=f_1W_3/W_2^2,
```

and

```math
T_3f=\frac{W_2}{W_3^2}W_D(f_1,f_2,f_3,f).
\tag{4.7}
```

Every divisor used here is zero-free. Three ordinary Rolle steps lose at most three roots. The fourth Wronskian of beta atoms has a beta factor times a polynomial of degree at most six: D^j m_s/m_s has degree at most j, so every determinant summand has degree at most 0+1+2+3=6. The constant column only simplifies this bound.

For F=1+alpha*m_u-beta*m_v-gamma*m_w, its fourth Wronskian is -gamma times the fourth Wronskian with m_w. Unless that fourth Wronskian vanishes identically, (4.7) proves

```math
Z(F)\le6+3=9.
\tag{4.8}
```

If it vanishes identically, m_w belongs to the span of the three regular basis functions: equivalently T_3 m_w=0 can be integrated through the two preceding nonvanishing transformations. Then a nonidentity F belongs to that three-function Chebyshev space and has at most two roots. This exceptional case is therefore harmless.

Consequently (4.8) holds for arbitrary distinct roots under (4.2). In the positive global-least family, generic endpoint parity and the limiting-cases lemma improve it to eight. No external two-polynomial theorem is needed for this small-gap argument.

## 5. The crossed ordering outside the small rectangle: endpoint cancellation

We now close the rest of (4.1). Put

```math
\theta=\frac{w_1}{w_1+w_2}\in(0,1).
```

### 5.1 A safe second-order operator

For k<=1 define, using ordinary derivatives,

```math
\mathcal L_{\theta,k}f
=\rho f''+k(\theta-x)f'+kf.
\tag{5.1}
```

This annihilates g_0=theta-x. It also admits a positive kernel solution h on (0,1). Here is the complete argument.

Take h_0=x^(1-theta)(1-x)^theta. Direct differentiation gives

```math
\frac{\mathcal L_{\theta,k}h_0}{h_0}
=-\frac{(1-k)\theta(1-\theta)}\rho\le0.
\tag{5.2}
```

Writing h=h_0*zeta, the kernel equation becomes

```math
\zeta''+p\zeta'-V\zeta=0,
\qquad V=\frac{(1-k)\theta(1-\theta)}{\rho^2}\ge0.
```

Choose interior initial data zeta=1, zeta'=0. For a positive integrating factor mu,

```math
(\mu\zeta')'=\mu V\zeta.
```

On any interval of positivity extending from the initial point, zeta is nondecreasing when moving to either side away from that point. Thus zeta>=1 and cannot have a first zero. Linear-ODE continuation on compact subintervals gives h>0 throughout (0,1).

The ordinary Wronskian W(h,g_0) satisfies Abel's scalar equation and has value -h(theta)<0 at theta. It is therefore nowhere zero. With the regular decreasing coordinate z=g_0/h,

```math
\mathcal L_{\theta,k}f
=\rho h(z')^2\frac{d^2}{dz^2}(f/h).
\tag{5.3}
```

Hence L loses at most two roots under Rolle.

First annihilate m_w:

```math
G=(D-\lambda_w)F=m_wD(F/m_w)
=-\lambda_w+\beta f_v-\alpha f_u,
```

where

```math
f_s=\lambda_{w-s}m_s\quad(s=u,v).
```

Both coordinates of w-u and w-v are positive in (4.1). Since L annihilates lambda_w, the first derivative step and (5.3) imply

```math
Z(F)\le Z(\mathcal L_{\theta,k}G)+3
\tag{5.4}
```

when the residual is not identically zero. If the residual is zero, G is in the two-dimensional kernel of L, so G has at most one zero unless it is identically zero. In the latter case F is a constant multiple of m_w and has no roots unless identically zero. Thus the exceptional cases do not threaten any claimed bound.

### 5.2 Exact cubic and endpoint factors

For ell=L(1-x)-Nx, f=ell*x^r(1-x)^t, define

```math
C_1=Lr(1-x)^2-[L(t+1)+N(r+1)]x(1-x)+Nt x^2,
```

```math
\begin{split}
C_2={}&Lr(r-1)(1-x)^3-r[2L(t+1)+N(r+1)]x(1-x)^2\\
&+t[L(t+1)+2N(r+1)]x^2(1-x)-Nt(t-1)x^3.
\end{split}
```

Then

```math
\mathcal L_{\theta,k}f=x^{r-1}(1-x)^{t-1}C,
\qquad
C=C_2+k[(\theta-x)C_1+\rho\ell],
\tag{5.5}
```

with degree at most three. Its endpoint factors are

```math
C(0)=Lr(r-T_1),\qquad
C(1)=-Nt(t-T_2),
\quad T_1=1-k\theta,\quad T_2=1-k(1-\theta).
\tag{5.6}
```

Let C_u,C_v be these cores for f_u,f_v, with L=w_1-s_1 and N=w_2-s_2. Multiplying the operator residual by the positive rho gives

```math
\widetilde R=\rho\mathcal L_{\theta,k}G
=\beta m_v C_v-\alpha m_u C_u.
\tag{5.7}
```

Define the affine support functional

```math
E(s)=(1-\theta)(s_1-1)-\theta(s_2-1).
\tag{5.8}
```

In the crossed ordering,

```math
E(v)-E(u)=(1-\theta)(v_1-u_1)+\theta(u_2-v_2)>0.
\tag{5.9}
```

### 5.3 Endpoint gate U

Assume

```math
u_2\ge\theta,\qquad E(u)<0.
\tag{U}
```

Choose k=(1-u_2)/(1-theta)<=1. Then T_2=u_2, so C_u(1)=0 and

```math
C_u=(1-x)\widehat C_u,\qquad \deg\widehat C_u\le2.
```

Moreover

```math
T_1-u_1=-E(u)/(1-\theta)>0,
```

so C_u(0)<0. At one,

```math
C_v(1)=-(w_2-v_2)v_2(v_2-u_2)>0.
```

At zero, the negative u term in (5.7) dominates because u_1<v_1 and C_u(0)<0, so the residual is positive. At one, the positive v term dominates because v_2<u_2 and C_v(1)>0, so the residual is again positive.

After its positive beta normalization, (5.7) is a cubic plus a beta-weighted quadratic, because the factor (1-x) has been absorbed into the u beta exponent. EHT bounds its distinct roots by seven. Generic coefficient ratios make the roots simple, and the equal positive endpoint signs force an even total, hence at most six. Equation (5.4) gives Z(F)<=9, and original endpoint parity gives eight.

### 5.4 Endpoint gate V

Assume

```math
v_1\ge1-\theta,\qquad E(v)>0.
\tag{V}
```

Choose k=(1-v_1)/theta<=1. Now T_1=v_1, so C_v=x*widehat C_v with degree at most two. Also

```math
T_2-v_2=E(v)/\theta>0.
```

Thus C_u(0)<0 and C_v(1)>0. The same endpoint dominance gives positive signs at both ends of (5.7). The x factor is absorbed into the v exponent, and the residual is again a beta-weighted quadratic plus a beta-weighted cubic. The identical seven-to-six parity improvement and (5.4) prove eight roots.

Both arguments concern the actual positive coefficients alpha,beta; no arbitrary residual level has been substituted. Generic coefficient ratios avoid critical values of the reduced ratio; the limiting-cases lemma covers support equalities.

### 5.5 Exhaustive gate coverage

If u_2>=theta and E(u)<0, use U. If u_2>=theta but E(u)>=0, then

```math
u_1\ge1+\frac{\theta}{1-\theta}(u_2-1)\ge1-\theta.
```

Because v_1>u_1 and E(v)>E(u), gate V applies.

Conversely, if v_1>=1-theta and E(v)>0, use V. If v_1>=1-theta but E(v)<=0, then

```math
v_2\ge1+\frac{1-\theta}{\theta}(v_1-1)\ge\theta.
```

Because u_2>v_2 and E(u)<E(v), gate U applies.

Therefore U or V closes every crossed row except possibly

```math
\boxed{u_2<\theta,\qquad v_1<1-\theta.}
\tag{5.10}
```

But in (5.10), positivity and the crossed inequalities imply

```math
0<v_1-u_1<1-\theta<1,
\qquad
0<u_2-v_2<\theta<1.
```

These are exactly the small-gap hypotheses of Lemma 4.1. That lemma closes the complement. **No crossed middle row remains.** Reflection supplies the opposite orientation.

## 6. Complete global-least assembly

At each coordinate, with 0<v_i<w_i, the positive support u has exactly three generic positions:

- A: u_i<v_i<w_i;
- B: v_i<u_i<w_i;
- C: v_i<w_i<u_i.

Their two-coordinate Cartesian product has nine cells:

| Coordinate slots | Proof |
|---|---|
| BB, BC, CB, CC | Strict lower-fork theorem (the positive support and upper negative support both lie above the lower negative support) |
| AA | Section 3.2, two exterior derivative roots |
| AC, CA | Section 3.3, opposite residual endpoint signs and one exterior derivative root |
| AB, BA | Sections 4–5, endpoint gates or the zero-free Wronskian flag |

Every generic strict global-least row has at most eight simple roots. the limiting-cases lemma extends the conclusion to all distinct roots, all internal support/event walls, and the weak support closure in Theorem A.

The nine coordinate-position combinations exhaust the strict global-least family.

## 7. Scope of the repaired double-turning theorem

Let the positive supports be p_0,p_1 and the negative supports n_0,n_1. First assume strict generic coordinate comparisons and suppose both same-sign pairs are comparable. Orient each pair from its lower to its upper support.

If the two lower supports are comparable, the smaller one is least among all four supports. Divide by its positive beta atom and coefficient, and negate the equation if its original sign was negative. The resulting equation has exactly the form of Theorem A, with the other same-sign atom denoted by u and the opposite-sign pair denoted by v<w. Hence it has at most eight roots.

If the two lower supports are incomparable, different coefficient signs dominate at zero and at one. There is a monotone atom ratio between those two supports. Section 8 gives at most ten distinct roots; for a generic equation all roots are simple and opposite endpoint signs make their total odd. Thus there are at most nine. the limiting-cases lemma extends the nine-root bound to nonidentity limiting rows.

Weak comparability of either same-sign pair is a support limit of strict comparability, with the same coefficient signs. Consequently Theorem B includes those boundaries, same-support mergers, and parallel directions as stated.

## 8. The monotone-pair ten-root bound used above

This section reconstructs the needed upper bound independently of the historical equality cascade. The anchor pair may have either the same or opposite coefficient signs.

Suppose any two support vectors s_0,s_1 are strictly coordinatewise incomparable. After division by m_(s_0), write

```math
F_0=c_0+c_1m_a+c_2m_b+c_3m_c,
\qquad a=s_1-s_0.
```

The two coordinates of a have opposite signs. Hence lambda_a is zero-free and m_a is strictly monotone on (0,1). Differentiate F_0, divide by Dm_a, and differentiate once more. The exact identity (3.3), with the corresponding coefficients and supports, gives a residual

```math
S_0=c_2m_b H(a,b)+c_3m_c H(a,c)
```

with at most eight distinct roots by EHT. There is **no pole**, so the two Rolle steps lose at most two roots:

```math
\boxed{Z(F_0)\le Z(S_0)+2\le10.}
\tag{8.1}
```

If S_0 is identically zero, the derivative quotient is constant, so F_0=c+d*m_a. Its nonidentity root count is at most one because m_a is monotone. Thus the identity exception is also covered.

For completeness, this also reconstructs the retained universal four-beta ten-root ceiling. If no support pair is incomparable on a strict generic row, the supports form a coordinatewise total chain. Divide by the least beta atom. The resulting F has equal endpoint signs. Choosing any remaining atom as the first derivative anchor introduces at most one pole; (3.3) and EHT give at most eleven roots. Generic parity improves eleven to ten. If the residual is identically zero, integration gives a two-atom expression with at most two roots. the limiting-cases lemma handles all nongeneric distinct-root limits.

The universal ten-root bound is not a proof that ten roots force exactly nine roots of DF for a particular normalization. The latter would require an additional argument, and none is used here.
