# A uniform low-gap last-pair separator without a coefficient-word gate

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. All variables are local to this document.

Assume the root-factor profile

```math
F=C{(t+x)(t-Q)(t-R)\over
t^\alpha(1+t)^{\beta-\alpha}(t+y)(t-P)(t-S)},
```

with

**(1)**

```math
0<\alpha<1,\quad\beta>2,\quad0<x<1,\quad y,C>0,
\quad0<P<Q<S<R,\quad P>{2\over\beta-1}.
```

Then its terminal component has exactly one simple maximum, and every
central critical height is strictly greater than that terminal maximum.
This holds for every $`\beta>2`$ in the stated domain, either ordering of the negative roots, and every choice of coefficient signs compatible with the source assumptions.

## A single scalar estimate

Write $`k=\beta-1>1`$, $`\delta=\beta-\alpha>k`$. For every
$`t>2/k`$,

**(2)**

```math
{x\over(t+x)^2}<{\delta\over(1+t)^2}.
```

Indeed, if $`t\ge1`$, the function $`s/(t+s)^2`$ is increasing for
$`0<s<1`$, so
$`x(1+t)^2/(t+x)^2<1<\delta`$. If $`t<1`$, then $`k>2`$, and
the scalar maximum at $`s=t`$ gives

**(3)**

```math
{x(1+t)^2\over(t+x)^2}
 \le{(1+t)^2\over4t}
 <{(k+2)^2\over8k}<k<\delta.
```

The middle strict inequality follows because
$`(1+t)^2/(4t)`$ decreases on $`(0,1)`$ and $`t>2/k`$.
The last is the elementary positive polynomial

```math
8k^2-(k+2)^2=7k^2-4k-4>0\qquad(k>2).
```

## Consequence for the deflated profile

Remove the last factor by setting $`Z_T=F(t-S)/(t-R)`$, and write

```math
E_T=t(\log Z_T)'=
{t\over t+x}-{t\over t+y}+{t\over t-Q}-{t\over t-P}
-\alpha-\delta{t\over1+t}.
```

For every $`t>Q>P>2/k`$,

**(4)**

```math
E_T'={x\over(t+x)^2}-{y\over(t+y)^2}
-{(Q-P)(t^2-PQ)\over(t-Q)^2(t-P)^2}
-{\delta\over(1+t)^2}<0
```

by (2). It decreases from positive infinity to $`-\beta`$, hence has a
unique simple zero $`H`$. The full terminal scaled derivative adds
$`tQ_2`$, whose derivative is also strictly negative terminally, so the
terminal full profile has a unique simple maximum $`T`$.

At every central full critical point $`v`$,
$`(\log Z_T)'(v)=-Q_2(v)<0`$, hence $`v>H`$. The reduced profile is
strictly decreasing from $`v`$ to $`T`$. Restoring the last-pair factors
therefore gives

```math
F(v)>Z_T(v)>Z_T(T)>F(T).
```

This is the same strict height conclusion as the earlier short separator,
now with no restriction on $`y`$ or on the exterior-root order. Three
central and two terminal distinct level intersections are incompatible;
four terminal intersections are impossible by the unique maximum.

## Source assumptions and use

For the actual support, $`p>u`$ gives $`0<x<1`$. The original source inequality $`P>2/r`$, where $`r=\lfloor\beta\rfloor-1`$, implies $`P>2/(\beta-1)`$. Thus the stated assumptions hold in the corresponding low-gap case.

The [complete component count](double-reversed-component-compatibility.md) extends this argument to the boundary $`\beta=2`$ directly and combines its strict height comparison with the [first-pair comparison](first-pair-height-comparison.md) and [mode-prefix inequality](all-coefficient-mode-prefix.md).
