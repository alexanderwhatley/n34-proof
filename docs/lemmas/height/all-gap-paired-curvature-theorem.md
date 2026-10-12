# One paired-curvature zero at every angular gap

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Analytic theorem, 2 October 2026. This proves the previously numerical all-gap conjecture for the physical inverse-beta branch difference. It does not by itself count the individual branches' intersections with a common coefficient line.

## Theorem

Let

```math
q=x^A(1-x)^B,\qquad \beta=x^a(1-x)^b,
\qquad A,B,a,b\gt0,
```

with $`aB-bA\gt0`$. For every $`0\lt q_0\lt q_{\max}`$, let $`x_L\lt x_R`$ be the two original points where $`q=q_0`$, and define

```math
D(q_0)=\frac1{\beta(x_L)}-\frac1{\beta(x_R)}\gt0.
```

Then $`D_{q_0q_0}`$ has exactly one zero on $`(0,q_{\max})`$. The zero is simple and changes sign strictly from positive to negative. There is no bound on the angular gap $`\kappa=(aB-bA)/B\gt0`$, and all original exponent scales are allowed.

## 1. The paired density is log-convex wherever it increases

Put $`t=\log x`$, $`f(t)=At+B\log(1-e^t)`$, $`s=\log q_0`$, and

```math
L=f'(t_L)\gt0,\quad R=-f'(t_R)\gt0,
\quad S=A+B,\quad M=A+S+\kappa B.
```

The positive density is

```math
\pi=\pi_L+\pi_R,
\qquad
\pi_L=e^{-\kappa t_L}/L,\quad
\pi_R=e^{-\kappa t_R}/R.
```

The exact slope equations are

```math
L_s=-\frac{(A-L)(S-L)}{BL}\lt0,
\qquad R_s=-\frac{(A+R)(S+R)}{BR}\lt0.
```

Writing $`g_L=(\log\pi_L)_s`$ and $`g_R=(\log\pi_R)_s`$, differentiation gives

```math
g_L=\frac{AS-ML+L^2}{BL^2},\qquad
g_R=\frac{AS+MR+R^2}{BR^2}\gt0,
```

```math
\frac{dg_L}{dL}=\frac{ML-2AS}{BL^3},\qquad
\frac{dg_R}{dR}=-\frac{MR+2AS}{BR^3}\lt0.
```

Thus the right density is strictly increasing and strictly log-convex.

If $`ML\le2AS`$, then $`g_{L,s}\ge0`$. The positive sum $`\pi_L+\pi_R`$ is strictly log-convex by the usual weighted logarithmic-curvature formula, whose variance term is nonnegative and whose right summand has strict positive logarithmic curvature.

If $`ML\gt2AS`$, set

```math
z=ML-2AS\gt0,\qquad
d_{*}=ML-AS-L^2=z+AS-L^2\gt0,
```

```math
F=(A-L)(S-L)\gt0.
```

Because $`0\lt L\lt A\lt S`$,

```math
F\lt AS-L^2\lt d_{*}.
```

The first strict inequality has positive difference $`L(A+S-2L)`$. We therefore obtain

```math
g_L=-\frac{d_{*}}{BL^2}\lt0,
```

```math
\frac{\pi_{L,ss}}{\pi_L}=g_L^2+g_{L,s}
=\frac{d_{*}^2-Fz}{B^2L^4}
\gt\frac{d_{*}(AS-L^2)}{B^2L^4}\gt0.
```

Thus in this second region the left density is strictly decreasing and strictly convex, even though it need not be log-convex.

Whenever the paired sum increases, $`\pi_s\gt0`$, this is enough. Indeed

```math
0\lt\pi_s\lt\pi_{R,s},\qquad
\pi_{ss}\gt\pi_{R,ss}\gt\frac{\pi_{R,s}^2}{\pi_R},
```

so

```math
\pi\pi_{ss}\gt\pi_s^2.
```

We have proved, for every $`\kappa\gt0`$, that $`\pi`$ is strictly log-convex wherever it increases.

## 2. The positive mixed kernel is log-convex wherever it increases

Let

```math
J=\int_{t_L}^{t_R}e^{-\kappa t}\,dt,
\qquad J_s=-\pi,
\qquad P=\pi+\lambda J,
\qquad\lambda=b/B\gt0.
```

If $`P_s\gt0`$, then $`\pi_s\gt\lambda\pi\gt0`$, so the preceding conditional log-convexity applies. The exact decomposition is

```math
\begin{aligned}
PP_{ss}-P_s^2
&=(\pi+\lambda J)
 \left(\pi_{ss}-\frac{\pi_s^2}{\pi}\right)\\
&\quad+\lambda(\pi_s-\lambda\pi)
 \left(J\frac{\pi_s}{\pi}+\pi\right)\gt0.
\end{aligned}
```

Thus $`P`$ is strictly log-convex wherever it increases.

## 3. Every curvature zero is a downward crossing

The exact source relation $`\log\beta=\lambda s+\kappa t`$ gives

```math
D=\kappa e^{-\lambda s}J,
\quad D_{q_0}=-\kappa e^{-(\lambda+1)s}P,
```

```math
D_{q_0q_0}=\kappa e^{-(\lambda+2)s}P
 \{\lambda+1-(\log P)_s\}.
```

At every curvature zero, $`(\log P)_s=\lambda+1\gt0`$, so $`P_s\gt0`$ and the preceding lemma gives $`(\log P)_{ss}\gt0`$. Therefore every zero of the brace is simple and crosses strictly downward. Two such zeros would require an intervening upward or nontransverse zero, contradicted by the same argument. There is at most one.

There is exactly one. At the zero endpoint, the positive beta power laws give

```math
D\sim q_0^{-a/A},\qquad D_{q_0q_0}\gt0
```

eventually; the other branch has strictly smaller inverse exponent $`b/B\lt a/A`$. At the fold, convergent inverse-branch expansion gives

```math
D=K\sqrt{q_{\max}-q_0}
 +O((q_{\max}-q_0)^{3/2}),\qquad K\gt0,
```

so $`D_{q_0q_0}\lt0`$ eventually. These endpoint expansions are differentiable to the needed order because they come from convergent local inverse series. The intermediate value theorem supplies the unique simple downward crossing.

## Ordered curvature zeros for two actual beta jumps

Suppose positive beta supports $`\beta_1\prec\beta_2`$ also satisfy

```math
0\lt\det(s_{\beta_1},s_q)\lt\det(s_{\beta_2},s_q).
```

Let $`D_1,D_2`$ be their inverse branch jumps. Their curvature zeros obey

```math
q_{\rm curv}(\beta_1)\lt q_{\rm curv}(\beta_2).
```

To prove this, the paired-branch quotient theorem gives strict increase of

```math
\mathcal J=\frac{(D_1)_s}{(D_2)_s}
=\frac{(D_1)_{q_0}}{(D_2)_{q_0}}.
```

At the curvature zero of $`D_2`$,

```math
(D_1)_{q_0q_0}
=\mathcal J_{q_0}(D_2)_{q_0}\lt0.
```

Since each curvature changes sign exactly once from positive to negative, the zero of $`D_1`$ is strictly earlier.

For the original comparable family with $`0\lt h\lt1`$, $`D_1=T`$ comes from $`\beta_1=v/u`$ and $`D_2=D`$ from $`\beta_2=v`$. Thus its two paired-curvature zeros are strictly ordered at every scale. This removes all phase routing for this paired comparison, while the individual original-branch common-level count remains a separate obligation.
