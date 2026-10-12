# Source-bound mixed central forcing Bernstein identity

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

This addendum binds the coefficient lemma to the actual projective entropy forcing polynomial. It also gives an independent analytical proof of the central contact bound. The exterior contact count and original-boundary transfer are separate modules.

Let $`P,Q>1`$ and

```math
H=P(P-1)r^2-2PQr+Q(Q-1)=P(P-1)(r-\eta)(r-\xi),\qquad 0<\eta<\xi.
```

Let $`B=r(1+r)`$, $`R=k\prod_{i=1}^3(r+A_i)`$, $`k,A_i>0`$, and $`Y=R-B`$. Assume the strict mixed inequalities $`Y(\eta)>0>Y(\xi)`$. Put $`j=Q-(P-1)r`$ and

```math
W=R(HY'-H'Y)-Y(H-PY)j.
```

Set $`\Delta=\xi-\eta`$, $`a=B(\eta)`$, $`b=B(\xi)`$, $`c=\eta+\xi+2\eta\xi`$, and

```math
G(x)=(1+x)^3R\left(\frac{\eta+\xi x}{1+x}\right)=\sum_{i=0}^3g_i x^i.
```

Then

```math
\boxed{(1+x)^6W\left(\frac{\eta+\xi x}{1+x}\right)
=\frac{P(P-1)\Delta}{2}\sum_{i=0}^6 C_i x^i,}
```

where

```math
\begin{aligned}
C_0&=(g_0-a)(3g_0-a),\\
C_1&=4g_1(g_0-a),\\
C_2&=g_1^2+2g_2(g_0-2a)-a^2-c^2+2ab,\\
C_3&=4(bg_0-ag_3),\\
C_4&=b^2+c^2-2ab+2g_1(2b-g_3)-g_2^2,\\
C_5&=4g_2(b-g_3),\\
C_6&=(3g_3-b)(b-g_3).
\end{aligned}
```

All factors in $`C_0,C_1,C_3,C_5`$ are strictly positive: $`g_0>a`$ and $`g_3<b`$, while $`g_i>0`$. $`C_6`$ has no prescribed sign. Since $`c^2-4ab=\Delta^2`$, $`C_2,C_4`$ are exactly the pair in the companion separated-negative-block lemma, which proves $`C_2+C_4>0`$. Hence, after zero coefficients are deleted, the seven coefficients have at most three sign variations. If $`C_6\ge0`$ there are at most two. Descartes' rule proves that $`W`$ has at most three roots on $`(\eta,\xi)`$, counted with multiplicity. No high-wall ratio bound is needed.

For completeness, the identity has a particularly short derivation. Put $`A=a+cx+bx^2`$ and $`E=G-(1+x)A`$. The wall identities are

```math
(P-1)\Delta^2=2c,\quad
Q-(P-1)\eta=\frac{(P-1)\Delta}{2},\quad
Q-(P-1)\xi=-\frac{(P-1)\Delta}{2}.
```

Clearing the projective denominators in $`W`$ gives the exact polynomial identity

```math
-2G\{x(1+x)E'-(2x+1)E\}
+E\{2cx(1+x)+E\}(1-x)
=(1+x)\sum_{i=0}^6C_i x^i.
```

Expanding this one identity supplies the printed coefficients.

Now fix any actual common entropy curve $`u_C`$, which is analytic on all $`r>0`$ and has $`0<u_C<\min(1/P,r/Q)`$. The source-independent entropy ODE is

```math
u_C'=F(r,u_C),\qquad
F(r,u)=\frac{u(1-Pu)j}{B+Hu}.
```

On the open central interval let $`u_0=Y/H`$. Its formal ODE denominator is $`B+Hu_0=R>0`$, even when $`u_0`$ lies outside the probability domain. Also $`B+Hu_C>0`$. Since the denominator is affine in $`u`$, it remains strictly positive along every segment joining $`u_0`$ and $`u_C`$. Consequently the secant coefficient

```math
L(r)=\int_0^1 F_u\bigl(r,u_0+t(u_C-u_0)\bigr)\,dt
```

is analytic, including at any contact. With $`d=u_C-u_0`$ one has

```math
d'=Ld-\frac{W}{H^2R}.
```

Multiplication by the positive integrating factor $`\exp(-\int L)`$ gives an analytic function whose derivative is a positive nonvanishing factor times $`-W`$. Thus Rolle's theorem, with multiplicities, bounds the total central contact weight by four.

The endpoint phases improve four to three. At $`\eta`$ from the right, $`H<0`$ and $`Y(\eta)>0`$, so $`u_0`$ tends to minus infinity and $`d`$ is positive. At $`\xi`$ from the left, $`Y(\xi)<0`$ and $`H<0`$, so $`u_0`$ tends to plus infinity and $`d`$ is negative. The actual curve remains finite at both walls. The finite total contact weight must therefore be odd, and a bound of four gives at most three. The strict mixed signs also exclude contacts at either wall.

This proof uses only a short universal polynomial identity, the analytical positive decomposition, Descartes' rule, the fixed-entropy ODE, and weighted Rolle/parity. No numerical root exclusion or expanded computer-algebra sign certificate is required.
