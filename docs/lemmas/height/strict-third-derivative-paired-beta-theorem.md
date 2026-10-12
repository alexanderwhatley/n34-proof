# Strict negative third derivative of every positive paired beta jump

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Analytic theorem, 2 October 2026. This strengthens the all-gap paired-curvature theorem and gives a shorter independent proof of its unique inflection conclusion. It does not assert an individual-branch common-line root bound.

## Theorem

Let

```math
q=x^A(1-x)^B,\qquad \beta=x^a(1-x)^b,
\qquad A,B,a,b>0,\qquad aB-bA>0.
```

For $`0<q_0<q_{\max}`$, let $`x_L<x_R`$ be the two original equal-$`q_0`$ points, and set

```math
D(q_0)=1/\beta(x_L)-1/\beta(x_R)>0.
```

Then

```math
\boxed{\ D_{q_0q_0q_0}<0\quad\text{throughout }(0,q_{\max}).\ }
```

Thus the paired curvature $`D_{q_0q_0}`$ is strictly decreasing, and the positive function $`-D_{q_0}`$ is strictly convex. The paired curvature has exactly one simple zero, changing from positive to negative, at every exponent scale and every positive angular gap.

## 1. Exact source density

Set

```math
t=\log x,\quad f(t)=At+B\log(1-e^t),\quad s=\log q_0,
```

```math
\lambda=b/B>0,\quad \kappa=(aB-bA)/B>0,\quad
L=f'(t_L)>0,\quad R=-f'(t_R)>0,
```

```math
S=A+B,\qquad M=A+S+\kappa B.
```

The exact identity $`\log\beta=\lambda s+\kappa t`$ gives

```math
J=\int_{t_L}^{t_R}e^{-\kappa t}\,dt>0,
\qquad D=\kappa e^{-\lambda s}J,
```

```math
J_s=-\pi,\qquad
\pi=\pi_L+\pi_R,\quad
\pi_L=e^{-\kappa t_L}/L,\quad
\pi_R=e^{-\kappa t_R}/R.
```

The original two source points give a strict density dominance

```math
\pi_L>\pi_R.
\tag{1}
```

Indeed $`f'`$ is strictly concave, since

```math
f'''(t)=-\frac{Be^t(1+e^t)}{(1-e^t)^3}<0.
```

Its integral between the two equal-level points is zero. Integrating its strict chord inequality therefore gives

```math
0>\tfrac12(t_R-t_L)\{f'(t_L)+f'(t_R)\}
=\tfrac12(t_R-t_L)(L-R).
```

Thus $`R>L`$, and

```math
\pi_L/\pi_R=e^{\kappa(t_R-t_L)}R/L>1.
```

This source linkage is essential; $`L,R`$ are not free independent slopes.

## 2. The left density has a stronger positive-score inequality

Direct differentiation gives

```math
L_s=-\frac{(A-L)(S-L)}{BL},\qquad
R_s=-\frac{(A+R)(S+R)}{BR}.
```

Write $`g_i=(\log\pi_i)_s`$. Then

```math
g_L=\frac{AS-ML+L^2}{BL^2},\qquad
g_R=\frac{AS+MR+R^2}{BR^2}>0,
```

```math
(g_L)_s=\frac{(2AS-ML)(A-L)(S-L)}{B^2L^4},\qquad
(g_R)_s=\frac{(MR+2AS)(A+R)(S+R)}{B^2R^4}>0.
\tag{2}
```

The left density is strictly convex, $`(\pi_L)_{ss}>0`$. If $`ML\le2AS`$, this follows from $`(g_L)_s\ge0`$ and $`g_L^2+(g_L)_s>0`$. If $`ML>2AS`$, put

```math
z=ML-2AS>0,\quad d_{*}=ML-AS-L^2=z+AS-L^2>0,
\quad F=(A-L)(S-L).
```

Because $`0<L<A<S`$,

```math
F<AS-L^2<d_{*},
```

and therefore

```math
\frac{(\pi_L)_{ss}}{\pi_L}
=\frac{d_{*}^2-Fz}{B^2L^4}
>\frac{d_{*}(AS-L^2)}{B^2L^4}>0.
\tag{3}
```

Whenever $`g_L>0`$, a stronger exact inequality holds:

```math
\boxed{\ (g_L)_s>2g_L^2.\ }
\tag{4}
```

To verify it, set $`d_0=AS-ML+L^2>0`$. Then

```math
F=d_0+\kappa BL,\qquad 2AS-ML=d_0+AS-L^2,
```

and (2) yields

```math
B^2L^4\{(g_L)_s-2g_L^2\}
=d_0L(M-2L)+\kappa BL(d_0+AS-L^2)>0.
\tag{5}
```

Every factor is positive, since $`M>A+S>2A>2L`$.

## 3. Density domination proves the third-derivative sign

Write $`\mu=\lambda+1>1`$. Exact differentiation of $`D=\kappa e^{-\lambda s}J`$ gives

```math
-D_{q_0q_0q_0}
=\kappa e^{-(\lambda+3)s}\mathcal W,
```

```math
\mathcal W=
\pi_{ss}-3\mu\pi_s+(3\mu^2-1)\pi
+\lambda\mu(\mu+1)J.
\tag{6}
```

Bound its two density summands separately.

If $`g_L\le0`$, strict convexity (3) gives

```math
(\pi_L)_{ss}-3\mu(\pi_L)_s+(3\mu^2-1)\pi_L
>(3\mu^2-1)\pi_L\ge2\pi_L.
```

If $`g_L>0`$, (4) gives the uniform lower bound

```math
\begin{aligned}
\frac{(\pi_L)_{ss}-3\mu(\pi_L)_s+(3\mu^2-1)\pi_L}{\pi_L}
&>3g_L^2-3\mu g_L+3\mu^2-1\\
&=3(g_L-\mu/2)^2+\tfrac94\mu^2-1
\ge\tfrac54.
\end{aligned}
```

Thus in either case the left summand exceeds $`5\pi_L/4`$.

The strictly log-convex right density in (2) gives

```math
\begin{aligned}
\frac{(\pi_R)_{ss}-3\mu(\pi_R)_s+(3\mu^2-1)\pi_R}{\pi_R}
&>g_R^2-3\mu g_R+3\mu^2-1\\
&=(g_R-3\mu/2)^2+\tfrac34\mu^2-1
\ge-\tfrac14.
\end{aligned}
```

Combining with the actual source dominance (1),

```math
\mathcal W>
\tfrac54\pi_L-\tfrac14\pi_R
+\lambda\mu(\mu+1)J>\pi_L>0.
```

Equation (6) proves the strict negative third derivative.

## 4. Unique simple inflection and original specialization

At the zero endpoint, the actual beta power laws give

```math
D\sim q_0^{-a/A},\qquad D_{q_0q_0}>0
```

eventually, because $`a/A>b/B`$. At the fold, the convergent inverse-branch expansion gives

```math
D=K\sqrt{q_{\max}-q_0}
+O((q_{\max}-q_0)^{3/2}),\qquad K>0,
```

so $`D_{q_0q_0}<0`$ eventually. These source expansions may be differentiated because they are convergent local inverse series. Strict negativity of the third derivative therefore gives exactly one curvature zero, and the zero is simple.

For the original comparable row with $`0<h<1`$, both paired jumps

```math
D=1/v_L-1/v_R,\qquad
T=q_0^n(v_L^{-H}-v_R^{-H})
```

are covered: the latter is the inverse jump for $`\beta_1=v/u`$, which has strict positive supports and determinant $`H\Delta>0`$. Hence

```math
D_{qqq}<0,\qquad T_{qqq}<0.
```

The first-derivative quotient theorem still supplies their strict ordered curvature zeros $`q_T<q_D`$. Together these are uniform third-derivative and one-inflection constraints on the exact paired branches. They do not determine the common symmetric part and do not yet replace the original seven-node common-line exclusion.
