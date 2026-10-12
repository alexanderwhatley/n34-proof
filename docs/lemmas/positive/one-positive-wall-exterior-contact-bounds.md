# One positive wall: exterior two in the low band and exterior one at a high wall

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Analytical follow-up, 4 October 2026. Let $`P>1`$, $`0<Q<1`$, $`K=P+Q-1`$, and retain the actual entropy chart, positive cubic $`R`$, and notation of the one-positive-wall geometry note. Write

```math
H=h_0(r+h)(r-\xi),\qquad h_0=P(P-1),\quad h>0,\quad\xi>\beta=Q/(P-1).
```

In particular every actual curve satisfies $`\theta_C'<0`$ and $`\eta_C'<0`$ on the exterior $`r>\xi`$, with $`\eta_C=r\theta_C'/\theta_C<0`$.

## Low wall with a central source band

Assume

**(1)**

```math
Y=R-r(1+r)=k(r+l)(r-c_1)(r-c_2),\qquad
k,l>0,\quad0<c_1<c_2<\xi.
```

Then at every actual level, the entire exterior $`(\xi,\infty)`$ has at most **two curvature contact weights**. No restriction on $`l/h`$, no negative-wall residue sign, and no simple-contact hypothesis is required.

This factorization follows automatically if the positive wall is strict low, $`Y(\xi)>0`$, and there is any actual central contact in $`(0,\xi)`$: at that contact $`Y=H\theta_C<0`$, while $`Y(0)>0`$ and $`Y(\xi)>0`$. The two sign-changing positive roots lie centrally and are simple; the remaining cubic root is negative. The conclusion is not claimed for every low wall without this central-band hypothesis.

For the positive exterior source $`\theta_0=Y/H`$, its elasticity is

**(2)**

```math
\eta_0=p-q,\qquad
p=\frac r{r-c_1}+\frac r{r+l}-\frac r{r+h}>0,
\quad
q=\frac{r(\xi-c_2)}{(r-\xi)(r-c_2)}>0.
```

Indeed, if $`l\le h`$ both terms after the first in $`p`$ have nonnegative sum. If $`l>h`$, their sum is greater than $`-1`$, whereas the first term exceeds one. More explicitly

```math
p=\frac{rN}{(r-c_1)(r+l)(r+h)},\quad
N=r^2+2hr+lh+(l-h)c_1>0.
```

Let $`\lambda_p=p'/p`$ and $`\lambda_q=q'/q`$. Then $`\lambda_q<0`$, and

**(3)**

```math
\lambda_p-\lambda_q
=\frac{N'}N-\frac1{r+l}
 +\left[\frac1{r-\xi}-\frac1{r+h}\right]
 +\left[\frac1{r-c_2}-\frac1{r-c_1}\right]>0.
```

The first bracket-free difference is positive because

```math
N'(r+l)-N
=r^2+2lr+lh-(l-h)c_1
=r^2+l(2r-c_1)+h(l+c_1)>0.
```

Consequently

**(4)**

```math
\eta_0'=p(\lambda_p-\lambda_q)+(p-q)\lambda_q>0
\quad\hbox{whenever }\eta_0\le0.
```

At a stationary point of source entropy $`J_0(r)=J(r,\theta_0(r))`$, the source is tangent to its actual level graph, so $`\eta_0=\eta_C<0`$. The derivative of the ODE discrepancy at that point gives

**(5)**

```math
J_0''=J_\theta\frac{\theta_0}r(\eta_0'-\eta_C')<0.
```

Thus every exterior stationary point is a strict, nondegenerate maximum.

There is at most one physical exterior component. Since $`r>\xi>Q/P`$, only the bound $`\theta<1/P`$ is active, and physicality is exactly

```math
R(r)<T_R(r),\qquad T_R=B+H/P=(Pr-Q)(Pr-Q+1)/P.
```

Shift $`r=t+Q/P`$. Then $`T_R=t+Pt^2`$, and $`R(t+Q/P)=a_0+a_1t+a_2t^2+a_3t^3`$ with every $`a_i>0`$. The numerator of $`(R/T_R)'`$ is

```math
-a_0-2Pa_0t+(a_2-Pa_1)t^2+2a_3t^3+Pa_3t^4.
```

Its coefficient sequence has exactly one sign variation, hence exactly one positive root, counting multiplicity. The ratio has one strict minimum. At the wall $`R/T_R>1`$, and at infinity the ratio tends to infinity, so its exterior strict sublevel is empty or one interval. Both endpoints of that interval have zero first probability and source entropy tending to negative infinity.

On a nonempty interval, entropy has a maximum; (5) shows it has only one stationary point, since two strict maxima require a intervening stationary point that is not a maximum. It rises then falls strictly. Every common level consequently has at most two contacts counted with analytic multiplicity; at its maximum the single contact has order exactly two. Equation (1)'s curvature numerator differs from the entropy-level equation by nonzero analytic factors on the physical source, so the weights agree.

## High wall: one exterior simple contact

Assume instead $`Y(\xi)<0`$. Positivity of $`Y(0)`$ and its leading coefficient gives exactly the simple real factorization

```math
Y=k(r+l)(r-c_1)(r-c_2),\quad
k,l>0,\quad0<c_1<\xi<c_2.
```

The source is negative on $`(\xi,c_2)`$, so no actual positive curve contacts it there. For $`r>c_2`$,

**(6)**

```math
\eta_0=\frac r{r+l}
 +\frac{r(c_1+h)}{(r-c_1)(r+h)}
 +\frac{r(c_2-\xi)}{(r-c_2)(r-\xi)}>0.
```

Hence $`\theta_0'>0`$, while $`\theta_C'<0`$. At $`c_2`$ the source is zero and the actual curve is positive; at infinity the source grows linearly while the actual curve tends to zero. There is exactly **one** exterior contact, and its nonzero derivative difference makes it simple. This holds for every finite actual entropy level and requires only positive cubic coefficients.

These are exterior theorems. A full unrestricted nonunit one-wall curvature-six theorem still requires an appropriate central weighted budget and a scope argument for sources without a central band. No original ONE-EDGE replacement is inferred from these exterior bounds alone.
