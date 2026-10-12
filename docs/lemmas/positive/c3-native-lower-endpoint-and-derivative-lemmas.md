# C3 inequalities at the lower endpoints

Read [the appendix terminology](../../appendix.md#terminology) before this lemma. Its variables are local. The notation comes from [the C45 argument](upper-low-band-c45-blended-cap-theorem.md). The cubic $`\operatorname{LinN3}`$ is explicitly defined in the final section below.

Let

```math
\begin{aligned}
&0<a<b,\quad l>1,\quad d=b-a,\quad L=a+l,\quad M=b+l,\\
&x=(a+h)(\xi-a),\quad y=(b+h)(\xi-b),\\
&\Gamma=(\xi+h)^2,\quad \Phi=\xi-h(1+2\xi),\quad G=a+b+2ab.
\end{aligned}
```

Define the numerator at the largest permitted scale by

```math
Z=L\operatorname{LinN3}+2\Gamma G(L^2y-M^2x).
```

For the one-wall parameters in that argument, positive coefficients of $`R`$ imply $`kd^2L<G`$. If $`L^2y-M^2x\le0`$, the value of $`C_3/(kd\gamma)`$ at this scale is $`Z/(\Gamma L)`$. Thus positivity of $`Z`$ at the following lower endpoints supplies the required inequality.

## Lower endpoint $`\xi=b`$

For $`\xi=b`$ and $`a,d,t,q>0`$, set

```math
b=a+d,\qquad h=\frac{bq}{(1+2b)(1+q)},\qquad l=1+t,\qquad
H_d=(1+2b)(1+q).
```

The integer polynomial $`H_d^3Z`$ has 406 nonzero coefficients, all strictly positive. Their full list is [the lower-endpoint coefficient table](../../../calculation-data/positive/c3_endpoint_certificate/LOWER_B_POSITIVE_CHART.json.gz). Therefore $`Z>0`$ whenever $`\xi=b`$ and $`0<h<b/(1+2b)`$.

Its highest power of $`q`$ is three. The coefficient of $`q^3`$ is a nonzero polynomial with strictly positive coefficients, and satisfies

```math
[q^3](H_d^3Z)=(1+2b)^3Z\bigl(h=b/(1+2b)\bigr).
```

Here $`[q^3]`$ means taking the coefficient of $`q^3`$. The identity also covers equality at $`h=b/(1+2b)`$.

## Lower endpoint $`\Phi=0`$

For $`u,v,w,t>0`$, set

```math
\xi=\frac u2,\qquad h=\frac{u}{2(1+u)},\qquad
b=\frac{\xi v}{1+v},\qquad a=\frac{bw}{1+w},\qquad l=1+t.
```

These parameters cover $`\Phi=0`$, $`0<a<b<\xi`$, $`0<h<1/2`$, and $`l>1`$. Write $`c=\xi-b`$, and define

```math
\begin{aligned}
D_A&=2(1+v)(1+w),&D_H&=2(1+u),\\
a&=\frac{uvw}{D_A},&d&=\frac{uv}{D_A},\\
c&=\frac{u(1+w)}{D_A},&h&=\frac{u}{D_H}.
\end{aligned}
```

The cleared polynomial $`D_A^8D_H^3Z`$ has 950 nonzero strictly positive coefficients. Next differentiate $`Z`$ with respect to $`\xi`$ while keeping $`a,b,h,l`$ fixed; equivalently, differentiate with respect to $`c`$. The cleared derivative

```math
D_A^7D_H^3\frac{\partial Z}{\partial\xi}
```

has 727 nonzero strictly positive coefficients. Thus $`Z>0`$ and $`\partial Z/\partial\xi>0`$ at the lower endpoint $`\Phi=0`$. The full lists are [the value table](../../../calculation-data/positive/c3_endpoint_certificate/LOWER_NATIVE_POSITIVE_CHART.json.gz) and [the derivative table](../../../calculation-data/positive/c3_endpoint_certificate/LOWER_NATIVE_DERIVATIVE_POSITIVE_CHART.json.gz).

## The cubic in symmetric variables

Put

```math
\begin{aligned}
&A=a+h,\quad B=b+h,\quad S=A+B,\quad T=AB,\\
&s=l-h,\quad X=\xi+h,\quad e=1-2h,\quad t_H=2h(1-h).
\end{aligned}
```

Then $`\operatorname{LinN3}/d=F(X)`$, where

```math
F(X)=A_3X^3+A_2X^2-A_1X+A_0,
```

with

```math
\begin{aligned}
A_3={}&4S(T-es)+t_H(2s-S),\\
A_2={}&4e(sS^2+2ST+2sT)+2sST-4T^2+t_H(S^2+sS+2T),\\
A_1={}&6eT(2T+sS)+3t_H(3ST+sS^2+2sT),\\
A_0={}&6t_HT(2T+sS).
\end{aligned}
```

Also,

```math
L^2y-M^2x=d\bigl[(s^2-T)X-s(2T+sS)\bigr].
```

These identities follow by polynomial substitution and determine the cubic used in the larger support argument. The [calculation guide](../../calculations.md) explains the exact tables.
