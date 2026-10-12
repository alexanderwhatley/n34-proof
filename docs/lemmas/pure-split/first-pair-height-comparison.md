# A uniform first-pair separator for three left critical points

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. All variables are local to this document.

Let $`\alpha,\beta,x,y,C\gt0`$, $`0\lt P\lt Q\lt S\lt R`$, and

**(1)**

```math
F=C{(t+x)(t-Q)(t-R)\over
t^\alpha(1+t)^{\beta-\alpha}(t+y)(t-P)(t-S)}.
```

Suppose $`0\lt k_1\lt k_2\lt k_3\lt P`$ are three full critical points on the left
positive component, and $`M\in(Q,S)`$ is any central full critical
point. Then

**(2)**

```math
\boxed{F(k_3)\gt F(M).}
```

No exponent band, negative-root order, support identity, mandatory
central point, or physical-sextic classification is needed.

## Proof

Remove the first event pair:

**(3)**

```math
F={t-Q\over t-P}Z_L,\qquad
Z_L=C{(t+x)(t-R)\over
t^\alpha(1+t)^{\beta-\alpha}(t+y)(t-S)}.
```

The reduced profile is positive and analytic throughout $`(0,S)`$.
Write $`D_L=(\log Z_L)'`$,

```math
D_L=D_0+Q_2,
 \quad D_0={1\over t+x}-{1\over t+y}-{\alpha\over t}
                          -{\beta-\alpha\over1+t},
 \quad Q_2={R-S\over(t-R)(t-S)}.
```

At each full critical point on the left or central component,

**(4)**

```math
D_L(v)=-Q_1(v)\lt0,
 \qquad Q_1={Q-P\over(t-Q)(t-P)}.
```

Suppose $`F(k_3)\le F(M)`$. The removed factor in (3) is greater than
one at $`k_3`$ and lies between zero and one at $`M`$, giving
$`Z_L(k_3)\lt Z_L(M)`$. Along with the negative endpoint derivatives (4),
this forces two sign-changing roots $`a\lt b`$ of $`D_L`$ in
$`(k_3,M)`$.

Let

**(5)**

```math
\begin{aligned}
M_0&=t(1+t)(t+x)(t+y),\\
N_0&=(y-x)t(1+t)-(\alpha+\beta t)(t+x)(t+y),\\
N_L&=N_0(t-S)(t-R)+(R-S)M_0.
\end{aligned}
```

Then $`D_L=N_L/[M_0(t-S)(t-R)]`$. The leading coefficient is
$`-\beta`$, the constant coefficient is $`-\alpha xyRS\lt0`$,
$`N_L(S)\gt0`$, and $`N_L(R)\gt0`$. Since $`N_L(M)\lt0`$, these signs
add a root $`d\in(M,S)`$, a root $`e\gt R`$, and a negative root.
Together with $`a,b`$, five distinct roots exhaust the quintic, and all
are simple. Write the negative root as $`-\eta`$. Then

```math
0\lt k_1\lt k_2\lt k_3\lt a\lt b\lt M\lt d\lt S\lt R\lt e,
```

and on $`(0,a)`$,

**(6)**

```math
H:=-D_L=
 {\beta(t+\eta)(a-t)(b-t)(d-t)(e-t)\over
 t(1+t)(t+x)(t+y)(R-t)(S-t)}\gt0.
```

Its logarithmic derivative is

**(7)**

```math
\begin{aligned}
{H'\over H}={}&{1\over t+\eta}-{1\over t}-{1\over1+t}
  -{1\over t+x}-{1\over t+y}\\
 &-{1\over a-t}-{1\over b-t}-{1\over d-t}-{1\over e-t}
  +{1\over R-t}+{1\over S-t}.
\end{aligned}
```

Pair $`1/(t+\eta)\lt1/t`$, $`1/(R-t)\lt1/(b-t)`$, and
$`1/(S-t)\lt1/(d-t)`$. Every remaining summand is negative, so
$`H'\lt0`$ throughout $`(0,a)`$.

On the left component $`Q_1\gt0`$ and $`Q_1'\gt0`$. Hence

```math
(\log F)'=Q_1-H
```

is strictly increasing on $`(0,\min(a,P))`$, which contains the three
distinct roots $`k_1,k_2,k_3`$. This contradiction proves (2).

## Use in the complete root count

Four intersections on the left component place the later minimum below the chosen regular level. Three intersections on the central component place a central maximum above that same level. The strict height comparison just proved makes those two requirements incompatible. The [complete component count](double-reversed-component-compatibility.md) combines this comparison with the other height and derivative bounds.
