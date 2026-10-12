# A uniform PS mode-prefix theorem for every B coefficient word

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. All variables are local to this document.

## Statement

Use six positive actual PS support parameters $`u,p,a,b,q,z`$, with
$`q<a`$, $`p<b`$, and $`p>u`$. Define

```math
\alpha=u+q\in(0,1),\qquad\beta=p+z\ge2,\qquad c=a/b.
```

The actual cubics are

```math
\begin{aligned}
A(t)&=(u+pt)(a-bt)[a+u+(p-b)t]-(ap+bu)t(1+t),\\
B(t)&=(q+zt)(a-bt)[(b+z)t-(a-q)]+(az+bq)t(1+t).
\end{aligned}
```

Assume

```math
A/A_3=(t+x)(t-Q)(t-R),\quad
B/B_3=(t+y)(t-P)(t-S),\quad
0<P<Q<c<S<R,
```

where $`x,y>0`$, and suppose

**(1)**

```math
P>{2\over\beta-1}.
```

Then

**(2)**

```math
\boxed{K(c)={Q-P\over(c-Q)(c-P)}-
                 {\alpha x\over c(c+x)}>0.}
```

There is no B coefficient sign, A coefficient word, unused-root
ordering, upper exponent cutoff, or computer-algebra sign premise.

## 1. Two actual-source estimates

Put $`U(t)=u+pt`$, $`V(t)=q+zt`$, and $`T=pq-uz`$. The score

```math
N(t)=\alpha+\beta t-{Tt(1+t)\over U(t)V(t)}
```

satisfies the exact identity

**(3)**

```math
{A(t)\over U(t)}+{B(t)\over V(t)}=(a-bt)N(t).
```

For every $`t>0`$, $`N(t)>\alpha-1+(\beta-1)t`$: if $`T\le0`$
this is immediate, and otherwise $`Tt<U(t)V(t)`$, whose positive
difference is $`uq+2uzt+pzt^2`$. At the root $`P`$, therefore,

**(4)**

```math
A(P)=U(P)(a-bP)N(P),\qquad N(P)>1+\alpha.
```

Let $`\mu=(a-q)/(b+z)`$. Since
$`B(\mu)=(az+bq)\mu(1+\mu)>0`$, the B factorization gives
$`P<\mu<S`$. From (1) and $`b>p`$,

**(5)**

```math
a-q>\frac{2(b+z)}{\beta-1}>\frac{2\beta}{\beta-1}>2.
```

The exact negative-one value
$`A(-1)=-(p-u)(a+b)[a+b-(p-u)]<0`$ gives $`x<1`$.
At its negative root, with $`v=px-u`$,

**(6)**

```math
v(a+bx)[a+u+(b-p)x]=(ap+bu)x(1-x).
```

Thus $`v>0`$, and $`(ap+bu)/(a+bx)<p`$. The bracket in (6)
is greater than $`a+u>2+\alpha`$, so

**(7)**

```math
0<v<\frac{px}{2+\alpha},\qquad
\varepsilon:=\frac vu<\frac1{1+\alpha}.
```

These are the only negative-root estimates used below.

## 2. The exact mode factorization

Write

```math
U=u+pc,\quad w=c(1+c),\quad d=c-P,\quad
Q_1={Q-P\over(c-Q)(c-P)},\quad
h={\alpha x\over c(c+x)},\quad r_R={1\over R-c}.
```

The actual mode values are
$`A(c)=-bUw`$ and $`A'(c)=-bU(1+2c+U)`$. Consequently

```math
L_A={1\over c-Q}-{1\over R-c}
   ={1+2c+U\over w}-{1\over c+x},
```

and

**(8)**

```math
L_A-h={U+c\over w}+{(1-\alpha)x\over c(c+x)}.
```

Comparing the root-factor values of $`A(P)`$ and $`A(c)`$ in (4) gives

**(9)**

```math
N(P)=wQ_1\lambda(1+dr_R),\qquad
\lambda={U\over U(P)}{P+x\over c+x}.
```

Also

**(10)**

```math
1+dr_R=2+d(Q_1-L_A).
```

Suppose for contradiction that $`Q_1\le h`$. The bracket in (10)
is positive. Thus (8)--(10) imply

**(11)**

```math
N(P)\le wh\lambda\{2-d(L_A-h)\}.
```

The brace on the right is also positive.

## 3. A scalar upper bound

Since $`px=u+v=u(1+\varepsilon)`$,

```math
\lambda={x+(1+\varepsilon)c\over x+(1+\varepsilon)P}
        {P+x\over c+x}.
```

The first ratio increases strictly with $`\varepsilon`$: its derivative
is $`x(c-P)/[x+(1+\varepsilon)P]^2>0`$. Put

```math
H=1+\alpha,\quad J=2+\alpha,\quad k=J/H.
```

By (7),

**(12)**

```math
\lambda<{x+kc\over x+kP}{P+x\over c+x}.
```

In (8), dropping the positive term $`U/w`$ strictly increases the brace
in (11). Hence

**(13)**

```math
N(P)<\mathcal N(c,x,P):=
{\alpha x(1+c)\over c+x}
 {x+kc\over x+kP}{P+x\over c+x}
\left\{2-{c-P\over1+c}
 -{(1-\alpha)(c-P)x\over c(c+x)}\right\}.
```

Every replaced brace is positive because it bounds the positive brace
in (11) from above.

Set $`r=x/c>0`$ and $`t=P/c\in(0,1)`$. Then

**(14)**

```math
\mathcal N=
{\alpha r\over1+r}
{(r+k)(t+r)\over(r+kt)(1+r)}
\left\{2+c+ct-{(1-\alpha)r(1+c)(1-t)\over1+r}\right\}.
```

At fixed $`\alpha,r,t`$, this expression is affine and strictly increasing
in $`c`$, since its linear coefficient has the positive factor

```math
1+t-{(1-\alpha)r(1-t)\over1+r}>1+t-(1-t)=2t>0.
```

The source estimate $`x<1`$ means $`c<1/r`$. Therefore

**(15)**

```math
\mathcal N<\mathcal N_{*}:=
{\alpha(r+k)(t+r)[1+t+r\{H+(1-\alpha)t\}]
 \over(r+kt)(1+r)^2}.
```

## 4. Three visible positive products

We claim $`\mathcal N_{*}<H=1+\alpha`$. After multiplication by its
positive denominator, this is exactly $`\mathcal F>0`$, where

```math
\mathcal F=H(Hr+Jt)(1+r)^2
 -\alpha(Hr+J)(t+r)[1+t+r\{H+(1-\alpha)t\}].
```

The gap is a strictly concave quadratic in $`t`$, whose quadratic
coefficient is

```math
-\alpha(Hr+J)[1+(1-\alpha)r]<0.
```

Its endpoint values are the visible positive products

**(16)**

```math
\begin{aligned}
\mathcal F(0)&=r[1+(1-\alpha)HJr+(1-\alpha)H^2r^2],\\
\mathcal F(1)&=(1-\alpha)(1+r)^2(Hr+J).
\end{aligned}
```

Therefore it is strictly positive throughout $`0<t<1`$. Equivalently,
the entire sign proof is the one exact identity

**(17)**

```math
\mathcal F=(1-t)\mathcal F(0)+t\mathcal F(1)
 +\alpha(Hr+J)[1+(1-\alpha)r]t(1-t),
```

whose three summands are positive. This proves $`\mathcal N_{*}<H`$.

Equations (11)--(17) now give $`N(P)<1+\alpha`$, contradicting (4).
This proves (2).

## Integration and limits

The [central-critical prefix](central-critical-prefix.md)
requires $`K(c)<0`$ at the mandatory actual central critical point
$`c=a/b`$. The present theorem contradicts that condition for every B
coefficient word and excludes four distinct central critical points uniformly for
$`\alpha<1,\beta\ge2`$. No split by the signs of individual B coefficients is needed.
