# Closed two-pole comparison for source height boundaries

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Let

```math
0<b<a\le R_i<c\quad(i=1,2,3),\qquad d>0,
```

with at most one $`R_i=a`$. Put

```math
Q(s)=\prod_i(s+R_i),\qquad
 f(s)=\frac{s(s+c)}{(s+b)(s+c+d)},
```

```math
\mathscr R(s)=\frac{Q(s)}{s+a}
  \left\{\frac b{s(s+b)}+
          \frac d{(s+c)(s+c+d)}\right\}.
```

Then $`(s+c+d)^2\mathscr R'(s)`$ is strictly increasing and
$`\mathscr R(s)\to b+d`$ at infinity. If
$`\mathscr R(s_{*})\ge b+d`$, then

```math
\mathscr R'(s)<0\quad(0<s\le s_{*}),\qquad
 \mathscr R(s)>\mathscr R(s_{*})\quad(0<s<s_{*}).            \tag{1}
```

For the scaled derivative, split the two summands. Match the metric
roots with denominator shifts 0,b,a. The first summand is b times a
product $`\prod_i(1+(R_i-d_i)/(s+d_i))`$, with nonnegative numerator
increments. The zero increment allowed when $`R_i=a`$ deletes that
factor. Each term of the negative derivative, after multiplication by
$`(s+c+d)^2`$, is strictly decreasing or vanishes; at least one is
strictly decreasing. The second summand has partial fractions

```math
d+\frac{A}{s+a}+\frac{B}{s+c}-\frac{C}{s+c+d},
 \qquad A\ge0,\quad B,C>0.
```

The signs follow from $`a\le R_i<c`$, and A=0 when a metric root
equals a. Its scaled derivative is

```math
C-A\left(\frac{s+c+d}{s+a}\right)^2
   -B\left(\frac{s+c+d}{s+c}\right)^2,
```

strictly increasing. This proves the scaled derivative assertion.

If the scaled derivative were nonnegative at a point with
$`\mathscr R(s_{*})\ge b+d`$, strict increase would force
$`\mathscr R`$ strictly above that value thereafter. This contradicts
its limit b+d, including the equality case. Hence it is negative at
s*, and at every earlier s. This proves (1).

Now let p increase as $`s=\eta_0-p`$ decreases. Suppose

```math
\frac{u_p}{u}=K\frac{s+a}{Q(s)},\qquad K>0,
```

and define the normalized full contact ratio

```math
\chi/H=f(s)+\frac\zeta{s-k},\qquad k>0,\quad\zeta\ge0.
```

Keep the source balance

```math
K+\zeta=b+d.                                             \tag{2}
```

Let $`p_{*}`$ be a finite stationary point of $`V=u\chi`$ with
$`s_{*}>k`$, and let a positive central comparison point have
$`0<s<k`$. Then

```math
\boxed{V(p)<V(p_{*}).}                                      \tag{3}
```

To prove it, stationarity gives

```math
\mathscr R(s_{*})=K+\zeta\mathscr B(s_{*}),\qquad
 \mathscr B(s)=
 \frac{K+Q(s)/((s+a)(s-k))}{f(s)(s-k)}>1.
```

The last inequality uses $`0<f<1`$, $`s>k`$, and
$`Q(s)/(s+a)>s^2`$. That strict inequality still holds when one
metric root equals a, because the two remaining roots are positive.
Thus $`\mathscr R(s_{*})\ge K+\zeta=b+d`$. By (1),
$`\mathscr R(s)>K`$ at every smaller s. The deleted height
$`V_0=uHf`$ therefore strictly decreases as p increases from p*
through every positive central point. The removed term is nonnegative
on the exterior and nonpositive on the central interval, so

```math
V(p)\le V_0(p)<V_0(p_{*})\le V(p_{*}).
```

The middle inequality is strict even when $`\zeta=0`$.

There are two source applications:

- At cancellation of the negative E/C residue, $`\zeta=0`$ and
  K=b+d. The original two positive poles remain, and (3) gives the
  actual exterior-to-central height comparison directly.
- At $`b_u=0`$, the source u metric has $`r_1=m/h`$; in the shifted
  variables its first metric root equals a. The displayed proof allows
  this equality. The coefficient identity
  $`d_1+d_2+d_3=Hh/\lambda`$ gives the unchanged balance (2), with
  $`\zeta=-d_1/H`$ and $`K=h/\lambda`$.

Both applications retain the actual signed source pole order and a
nonempty positive central interval. The [metric-boundary argument](metric-deformation-root-cell-boundaries.md) establishes the source mapping. An arbitrary rational ratio does not automatically satisfy the residue balance (2).
