# Two negative-exponent terms and one positive-exponent term

This is the proof labeled **[EASY]** in the main argument. In this document the signs describe the two exponents, rather than the coefficient of a term.

Let

```math
f(x)=1-E_1h_1(x)-E_2h_2(x)-E_3h_3(x),\qquad E_i\gt0,
```

where $`h_i=x^{a_i}(1-x)^{b_i}`$ on $`(0,1)`$, $`a_1,b_1,a_3,b_3\lt0`$, and $`a_2,b_2\gt0`$. Then **$`f`$ has at most four zeros**, even when zeros are counted with their multiplicities. In particular it cannot have ten distinct zeros. No comparison between the magnitudes of the exponents is required.

## A factored second-derivative identity

Use the logarithmic coordinate $`t=\log(x/(1-x))`$, so that

```math
D=\frac{d}{dt}=r\frac{d}{dx},\qquad r=x(1-x)\gt0.
```

For one of the terms $`h=x^a(1-x)^b`$, put

```math
s=a+b,\quad c=a/s,\quad y=x-c,\quad R=r-sy^2,\quad T=\frac{D^2h}{r}=-s\frac{h}{r}R.
```

Here $`s\ne0`$ and $`0\lt c\lt1`$ because both exponents have the same strict sign. The formula for $`T`$ follows from $`D\log h=-sy`$ and $`D(-sy)=-sr`$.

Put $`p=1-2c`$ and $`q=c(1-c)\gt0`$. Then

```math
r=q+py-y^2,\qquad R=q+py-(s+1)y^2.
```

On an interval where $`R\ne0`$, direct differentiation gives the exact identity

```math
D^2\log|T|=-\frac{sr}{R^2}\,B,
```

**(1)**

```math
B=\bigl((s+1)y^2-py\bigr)^2+(py+q)(py+3q).
```

Here are the intermediate steps, so that no computer calculation is needed. Write $`A=p-2(s+1)y`$, so that $`DR=rA`$ and

```math
D^2R=r\bigl((p-2y)A-2(s+1)r\bigr).
```

Since $`D^2(\log h-\log r)=(2-s)r`$, the numerator of $`D^2\log|T|`$ after removing $`r/R^2`$ is

```math
K=(2-s)R^2+R\bigl((p-2y)A-2(s+1)r\bigr)-rA^2.
```

Expansion yields

```math
K=-s\bigl((s+1)^2y^4-2p(s+1)y^3+2p^2y^2+4qpy+3q^2\bigr)=-sB,
```

proving (1).

Both factors in its last product are strictly positive. Indeed $`py+q=r+y^2\gt0`$. The affine function $`py+3q`$ has endpoint values $`c(2-c)\gt0`$ at $`x=0`$ and $`(1-c)(1+c)\gt0`$ at $`x=1`$. Thus $`B\gt0`$ throughout $`(0,1)`$.

If $`a,b\lt0`$, then $`s\lt0`$, $`R=r+|s|y^2\gt0`$, and $`T\gt0`$ with $`D^2\log T\gt0`$. If $`a,b\gt0`$, then $`s\gt0`$ and $`D^2\log|T|\lt0`$ wherever $`T\ne0`$. The inequality $`T\lt0`$ holds on exactly one interval: $`R`$ is a strictly concave quadratic, is positive at $`c`$, and is negative at both endpoints.

## Counting the zeros

Outside that single interval for $`h_2`$, all three $`D^2h_i`$ are nonnegative and the two negative-exponent terms are strictly positive. Hence $`D^2f`$ cannot vanish there. Inside it, $`D^2f=0`$ is equivalent to

```math
E_1Q_1+E_3Q_3=E_2,\qquad Q_i=\frac{D^2h_i}{-D^2h_2}\gt0\quad(i=1,3).
```

The common factor $`r`$ cancels in these quotients. Formula (1) gives

```math
D^2\log Q_i=D^2\log T_i-D^2\log(-T_2)\gt0,
```

and therefore

```math
D^2Q_i=Q_i\bigl(D^2\log Q_i+(D\log Q_i)^2\bigr)\gt0.
```

Consequently $`E_1Q_1+E_3Q_3`$ is strictly convex in $`t`$. A strictly convex function meets a horizontal line at most twice. A tangent intersection has order exactly two and is its only intersection; two intersections are simple. Thus $`D^2f`$ has at most two zeros counted with multiplicity. Two applications of Rolle's theorem in $`t`$ give at most four zeros of $`f`$. The change from $`x`$ to $`t`$ preserves both distinct roots and their orders. This proves [EASY].

## A related elementary one-corner case

For completeness, the same recovered argument gives a short proof when the exponent signs are $`(-,-),(+,-),(+,-)`$. Write

```math
h_1=x^{-A}(1-x)^{-B},\qquad h_j=x^{C_j}(1-x)^{-D_j}\quad(j=2,3),
```

with all magnitudes positive. The one-corner assumption requires $`B\gt D_j`$: the first support is below both others in each coordinate. Put $`g_i=Dh_i`$ and $`N=\sum E_i g_i=-Df`$. For $`x\ge A/(A+B)`$ all $`g_i`$ are nonnegative, with $`g_2,g_3\gt0`$, so $`N\gt0`$. To the left set

```math
u=A-(A+B)x\gt0,\quad v_j=C_j(1-x)+D_jx\gt0,\quad q_j=g_j/(-g_1)\gt0.
```

Direct logarithmic differentiation gives

```math
D\log q_j=u+v_j+\frac{r(BC_j+AD_j)}{uv_j}\gt0.
```

Thus $`N=0`$ becomes $`E_2q_2+E_3q_3=E_1`$ with a strictly increasing left side. It has at most one solution; Rolle gives at most two zeros of $`f`$. This related statement does not extend [EASY] to two positive-exponent terms. Those terms are handled by the separate height arguments in the main proof.
