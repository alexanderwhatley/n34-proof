# The straddling one-pair-root mixed source closes by an endpoint bound

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

checkable from source identities. No original complete root theorem or
appendix case atlas is invoked.

Consider

```math
f=C_0-E_0h_0-E_1h_1-E_2h_2,
\quad h_0=t^{-A}(1-t)^{-B},\quad h_1=t^a(1-t)^b,
\quad h_2=t^c(1-t)^{-\nu},
```

where all six exponents and all three $`E_i`$ are positive,
$`B>\nu`$, $`c>a`$, and $`C_0`$ is arbitrary real. There is no
condition on the sign of $`c-\nu`$ or the relative size of
$`c-a`$ and $`b+\nu`$.
Put $`\rho=t(1-t)`$,

```math
\ell_0=-A+(A+B)t,\quad \ell_1=a-(a+b)t,
\quad\ell_2=c-(c-\nu)t>0,
```

```math
P_i=\ell_i^2+\rho\ell_i',\quad
Q_i=\ell_iP_i+\rho P_i',\quad
W=\det[\ell_i;P_i;Q_i],
```

and use the cofactors

```math
R=\ell_1P_2-\ell_2P_1,\quad
V=\ell_2P_0-\ell_0P_2,\quad
C=\ell_0P_1-\ell_1P_0.
```

The cofactor $`C`$ is unrelated to the constant coefficient $`C_0`$.

**Theorem.** If $`R`$ has exactly one distinct physical root $`r`$ and
$`V(r)<0`$, then $`f`$ has at most eight distinct roots in $`(0,1)`$.
No condition on the other roots of $`C`$, no quadratic parameter inequalities, and no
simple-root assumption on $`R`$ are needed.

## The actual late interval

Write

```math
M_0=A+B,\quad M=a+b,\quad\mu=A/M_0,\quad m=a/M.
```

The actual source gives $`\mu<m<r<d<1`$, where $`d`$ is the unique
minimum of the late ratio

```math
k=|u|/v,\qquad u=-h_0'/h_2',\quad v=-h_1'/h_2'>0
\quad(t>m).
```

It is the unique late root of $`C`$. The same source geometry gives
$`R,C,V<0`$ throughout $`I=(r,d)`$. For completeness, the ingredients
are proved below; its conclusions do not involve the unproved quartic
monotonicity target.

Set $`x=t-m`$ and $`\delta=m-\mu>0`$. The exact source cubic is

```math
\bar C(x):=C/(M_0M)
=x(x+\delta)[M_0(x+\delta)+Mx]-\delta\rho(m+x).
\tag{2}
```

Its leading coefficient is $`T=M_0+M>0`$, its quadratic coefficient is
$`\delta(2M_0+M+1)>0`$, and its constant coefficient is
$`-\delta m(1-m)<0`$. Its second derivative is strictly positive for
$`x>0`$, so it has exactly one positive root $`\beta=d-m`$ and crosses
there with positive derivative.

Dividing at this root gives

```math
\bar C(x)=(x-\beta)H(x),\qquad
H(x)=Tx^2+ux+v,
\tag{3}
```

with

```math
u=\delta(2M_0+M+1)+T\beta>0,
\qquad v=\frac{\delta m(1-m)}\beta>0.
```

Thus all three coefficients of the quadratic quotient are positive. This
fact holds whether the other two roots of $`C`$ are real or conjugate.

## The endpoint logarithmic derivative

The exact derivative identity for the auxiliary auxiliary ratio is

```math
B_{*}:=\rho(R'C-RC')+(\ell_2-\ell_0)RC=\ell_1W.
\tag{4}
```

At $`t=d`$, $`C=0,C'>0,R<0,\ell_1<0`$, so

```math
B_{*}(d)=-\rho(d)R(d)C'(d)>0,
\qquad W(d)<0.
\tag{5}
```

Differentiating (4), then using $`C(d)=0`$, gives

```math
\frac{W'}W(d)
=\frac{C''}{C'}(d)+
\frac{\rho'-\ell_2+\ell_0}{\rho}(d)-\frac1{d-m}.
\tag{6}
```

The terms containing $`R'`$ cancel. This cancellation is why the endpoint
argument does not require monotonicity of $`R/C`$ on the whole interval.

Let $`\beta=d-m`$. From (3),

```math
\frac{C''}{C'}(d)=2\frac{H'(\beta)}{H(\beta)}<\frac4\beta,
\tag{7}
```

because
$`4H(\beta)-2\beta H'(\beta)=2u\beta+4v>0`$.
From (2) evaluated at its root,

```math
\rho(d)\delta
=\beta(\beta+\delta)[M_0(\beta+\delta)+M\beta].
```

Consequently

```math
\frac{\ell_0(d)}{\rho(d)}
=\frac{M_0\delta}{\beta[M_0(\beta+\delta)+M\beta]}
<\frac1\beta.
\tag{8}
```

Also $`\ell_2(d)>0`$ and

```math
\frac{\rho'}\rho(d)=\frac1d-\frac1{1-d}<\frac1d<\frac1\beta.
```

Combining these strict bounds with (6),

```math
\boxed{\frac{W'}W(d)<\frac5\beta},\qquad
\boxed{(d-r)\frac{W'}W(d)<5},
\tag{9}
```

since $`0<d-r<\beta`$.

## At most four distinct critical-polynomial roots inside

Every determinant term defining $`W`$ has degree at most six in $`t`$.
Equation (5) shows that $`W`$ is not the zero polynomial.
If all six roots, counted with multiplicity, belonged to $`[r,d)`$, then

```math
\frac{W'}W(d)=\sum_j\frac{m_j}{d-t_j}
\ge\frac6{d-r},
```

contradicting (9). The inequality is strict when any root lies in $`(r,d)`$.

At the other endpoint, the unique physical $`R`$-root crosses from positive
to negative: $`R(0)=ac(c-a)>0`$ and
$`R(1)=-b\nu(b+\nu)<0`$. Therefore $`R'(r)\le0`$, including a possible
triple root. Using (4), $`C(r)<0`$ and $`\ell_1(r)<0`$, gives

```math
W(r)=\rho(r)R'(r)C(r)/\ell_1(r)\le0.
\tag{10}
```

Suppose $`W`$ had five distinct roots in $`(r,d)`$. If $`W(r)<0`$,
the same negative signs at both endpoints imply that the total interior
root multiplicity is even, hence at least six. If $`W(r)=0`$, that
endpoint root plus the five distinct interior roots already gives at least
six roots in $`[r,d)`$. In either case degree at most six forces all six
roots, counted with multiplicity, into $`[r,d)`$, contradicting (9).
Thus

```math
\boxed{W\text{ has at most four distinct zeros on }(r,d).}
\tag{11}
```

## Original-row root count without regularization

Since $`h_2'>0`$,

```math
f'/h_2'=U-E_2,\qquad U=E_0u+E_1v.
```

The opposite-mode source geometry gives one strictly decreasing initial
positive $`U`$-component and at most one bounded late positive component.
Every positive late critical point lies in $`(r,d)`$ and solves

```math
\Psi=(h_1/h_0)R/V=E_0/E_1.
```

Its exact derivative identity is

```math
\rho\Psi'=-\frac{h_1}{h_0}\frac{\ell_2W}{V^2}.
\tag{12}
```

By (11) and Rolle, any one level of $`\Psi`$ has at most five contacts
inside $`(r,d)`$. Thus the late positive $`U`$-component has at most
five critical points. Any one positive level $`E_2`$ consequently has at
most six contacts on it, including critical level contacts. The initial
component supplies at most one. Hence $`f'`$ has at most seven distinct
roots and $`f`$ has at most eight, by ordinary Rolle. No parity argument,
simple original roots, coefficient perturbation, or generic-source limit is
needed.

The source geometry used here follows directly, including when
$`c\le\nu`$ or $`c-a\le b+\nu`$. First,

```math
R=\ell_1\ell_2(\ell_2-\ell_1)+\rho(a\nu+bc),
\quad\ell_2-\ell_1=(c-a)(1-t)+(b+\nu)t>0.
```

Thus $`R>0`$ whenever $`t\le m`$, so $`r>m`$. Before the inverse mode
$`\mu`$, the ratio

```math
u=\frac{h_0}{h_2}\frac{-\ell_0}{\ell_2}>0
```

is strictly decreasing: its logarithmic derivative is

```math
\frac{\ell_0-\ell_2}{\rho}
+\frac{B c+A\nu}{\ell_0\ell_2}<0.
```

Consequently $`V>0`$ there. If $`\mu\ge m`$ and $`r>\mu`$,
the equation $`R(r)=0`$ gives $`P_2/\ell_2=P_1/\ell_1`$, hence

```math
\frac{V(r)}{\ell_2(r)}
=\ell_0(r)\left[\ell_0(r)-\ell_1(r)+
\rho(r)\left(\frac1{r-\mu}-\frac1{r-m}\right)\right]>0.
```

At $`r=\mu`$, $`V=\ell_2P_0>0`$. Thus $`V(r)<0`$ forces
$`\mu<m`$, independently of the sign of $`c-\nu`$.

On $`(0,\mu)`$, $`u>0,v<0`$. The logarithmic derivative of
$`k_-=|v|/u=(h_1/h_0)\ell_1/(-\ell_0)`$ is

```math
\frac{\ell_1-\ell_0}{\rho}
-\frac{MM_0(m-\mu)}{\ell_1\ell_0}>0,
```

so $`U=u(E_0-E_1k_-)`$ strictly decreases wherever positive.
On $`(\mu,m)`$, both $`u,v`$ are negative. On $`(m,1)`$,

```math
\log k=-(A+a)\log t-(B+b)\log(1-t)+\log(t-\mu)-\log(t-m)
+\text{constant},
```

so

```math
(\log k)''=\frac{A+a}{t^2}+\frac{B+b}{(1-t)^2}
-\frac1{(t-\mu)^2}+\frac1{(t-m)^2}>0.
```

It has one minimum $`d`$, with infinite limits at both ends; the late
positive set of $`U=v(E_1-E_0k)`$ is consequently empty or one bounded
interval. The single $`R`$-root is the unique maximum of $`v`$.
At that root, $`V(r)<0`$ gives $`k'(r)<0`$, hence $`r<d`$.
The exact derivative identity

```math
\rho k'=\frac{h_0}{h_1}\frac{C}{\ell_1^2}
```

detects this late minimum; (3) shows
$`C<0`$ on $`(m,d)`$. Finally the cofactor relation
$`\ell_0R+\ell_1V+\ell_2C=0`$ gives $`V<0`$ on $`(r,d)`$.
Before $`r`$, $`v'>0,k'<0`$; after $`d`$, $`v'<0,k'>0`$.
Thus $`U'=v'(E_1-E_0k)-E_0vk'`$ cannot vanish on a positive late
component outside $`(r,d)`$. These statements agree with the earlier proof opposite-mode source interfaces.

This theorem proves the eight-root target in the entire straddling
one-pair-root mixed region. It does **not** prove the stronger quartic sign
$`R'C-RC'\ge0`$, or a universal four-root count.
