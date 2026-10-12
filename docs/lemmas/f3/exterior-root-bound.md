# Bounding exterior roots by their sum

Use the parameters and polynomials in
[the reciprocal-coordinate section of the appendix](../../appendix.md#reciprocal-coordinate-height-and-regional-bounds). This lemma bounds exterior contacts on the stated parameter region.
Its proof uses inequalities and two short polynomial expansions.

## Statement

Suppose

**(1)**

```math
g:=p-S>0,\qquad r\ge\frac74p,\qquad \mu\ge s.
```

Suppose $`P_p`$ has one real zero $`\beta>M`$ and two nonreal,
complex-conjugate zeros, and that $`\beta>s`$. Then

**(2)**

```math
\beta>3\mu-2M.
```

In the order $`\alpha<\delta<s<\gamma<\beta`$, suppose in addition
that the contact polynomial has positive values at both extreme events:

**(3)**

```math
R(\alpha)>0,\qquad R(\beta)>0.
```

Then the number of physical contacts in the two exterior intervals
$`(M,\alpha)`$ and $`(\beta,\infty)`$, counted with multiplicity,
is at most four. The original geometric argument uses precisely these
exterior contacts in this case.

The inequality $`\mu\ge s`$ can be checked without square roots as
$`Z<0`$ and $`Z^2\ge36Y`$. The strict parameter inequalities remain
in force; equality in $`r=7p/4`$ or $`\mu=s`$ is allowed.

## A barrier for the real root of the cubic

Put

```math
B=qy,\qquad C_{*}=(y+1)(y+g)+pq>0.
```

Then $`Z=C_{*}-gr`$. Translating the cubic gives

```math
P_p(M+w)=w^3-Lw^2+Cw-K,
```

where the value of $`C`$ will not be needed and

```math
L=p(r-S)-3M,\qquad
K=(pr-M)(M+pq)(M+py)>0.
```

If $`b=\beta-M`$, factor out the real root. The remaining quadratic is

```math
w^2+(b-L)w+K/b.
```

Its zeros are nonreal, so its discriminant is negative. Equivalently,

**(4)**

```math
n(b):=b(L-b)^2-4K<0.
```

Put $`m=\mu-M`$ and $`\ell=s-M`$. We have
$`m\ge\ell>0`$. Direct substitution gives

**(5)**

```math
2(L-3m)=(p+S)(r-p)+pg+C_{*}>0.
```

On the interval $`[\ell,3m]`$, the derivative of $`n(b)`$ with respect
to $`b`$ is $`(L-b)(L-3b)`$. By (5), its only possible interior
turning point is a maximum. Its minimum on this interval is therefore
at an endpoint. We will prove

**(6)**

```math
n(s-M)>0,\qquad n(3(\mu-M))>0.
```

Equations (4) and (6) then force $`b>3m`$, since $`b>\ell`$.
This is (2).

## Reducing the two endpoint signs to $`M=qy`$

Keep $`p,q,r,y`$ fixed and vary $`M`$. Literal differentiation gives

```math
\frac{d^2}{dM^2}n(s-M)=-8p<0,
```

```math
\frac{d^2}{dM^2}n(3(\mu-M))
 =8\{3M+p(q+y-r)\}<0
 \quad(-pq\le M\le B).
```

For the last sign, use $`q+y<p`$, $`B<p^2/4`$, and $`r\ge7p/4`$:

```math
3M+p(q+y-r)
 <\frac34p^2+p^2-\frac74p^2=0.
```

Thus both functions are concave in $`M`$. At $`M=-pq`$, $`K=0`$
and both their arguments are positive and less than $`L`$, by (5).
Their values there are strictly positive. It remains to prove positivity
at $`M=B`$. Concavity then proves positivity throughout
$`(-pq,B)`$, which contains the actual allowed interval.

## The calculation at $`M=B`$

Set

```math
\rho=\frac74,\qquad k=s/B.
```

The assumptions give

```math
gr\ge6s+C_{*}>6s,\qquad g/p>6/k,\qquad k>6,
\qquad pr=Bk^2,\qquad p^2\le pr/\rho.
```

Define the three elementary polynomials

```math
\begin{aligned}
Q_\rho(k)&=(2k^2-6k)/\rho+1,\\
H_\rho(k)&=(1-1/\rho)k^2+(6/\rho-1)k-2,\\
J_\rho(k)&=\{(\rho-1)k^2+3(2-\rho)k\}/\rho.
\end{aligned}
```

They are positive for $`k>6`$. At $`M=B`$, put
$`Q=(p+q)(p+y)`$. The useful strict bounds are

**(7)**

```math
Q<BQ_\rho(k),\qquad
L-(s-B)>BH_\rho(k),\qquad
L-3(\mu-B)>BJ_\rho(k).
```

Here are exact decompositions of their differences, so no estimate in
(7) is left implicit. Let

```math
D_{*}=pr-\rho p^2\ge0,\qquad \kappa=g-6p/k>0.
```

Then

```math
BQ_\rho-Q=\frac{2-6/k}{\rho}D_{*}+p\kappa+p>0,
```

```math
L-(s-B)-BH_\rho
 =\frac{1-6/k}{\rho}D_{*}+p\kappa>0,
```

```math
\begin{aligned}
L-3(\mu-B)-BJ_\rho
={}&\frac{S(r-\rho p)}2
 +\frac{2-\rho}{2\rho}(1-6/k)D_{*}\\
 &+\frac{(2-\rho)p\kappa}2+\frac{C_{*}}2>0.
\end{aligned}
```

At this boundary $`K=B(pr-B)Q`$ and $`s-B=B(k-1)`$. Using (7),

```math
n(s-B)>B^3(k-1)
 \{H_\rho^2-4(k+1)Q_\rho\},
```

```math
n(3(\mu-B))>B^3(k-1)
 \{3J_\rho^2-4(k+1)Q_\rho\}.
```

The second inequality also uses $`\mu-B\ge s-B`$. With $`w=k-6>0`$,
the two braces, multiplied by (49), are exactly

```math
9w^4+94w^3+401w^2+2436w+8820,
```

```math
27w^4+478w^3+3247w^2+11144w+18032.
```

Every coefficient is positive. This proves the two boundary signs,
then (6), and finally (2).

## Counting the exterior contacts

Since $`R(M)>0`$, (3), and the positive leading coefficient give
positive signs at both ends of each exterior interval, each interval
contains an even number of roots counted with multiplicity. Repeated
roots do not affect this parity statement: a root of odd multiplicity
changes the sign and a root of even multiplicity does not.

If the exterior contribution exceeded four, degree six and parity would
force all six roots of $`R`$ to be real physical exterior contacts. If
the upper interval contains roots, it contains at least two. The sum of
all six then exceeds

```math
2\beta+4M>2(3\mu-2M)+4M=6\mu.
```

This contradicts the coefficient identity saying that the sum is
$`-Z=6\mu`$. If the upper interval contains no roots, all six lie
below $`\alpha<s\le\mu`$, so their sum is less than $`6\mu`$, again
a contradiction. The exterior count is therefore at most four.

This theorem proves a conditional bound on a region. It does not prove
that every configuration with the displayed event order satisfies (1).
