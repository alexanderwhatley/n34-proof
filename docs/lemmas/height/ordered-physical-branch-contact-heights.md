# Ordered physical-branch contact heights

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

This strengthens the one-crossing theorem to the original quotient and both original tangent coefficient functions. It does not assert a total contact count.

## The under the stated parameter assumptions theorem

Retain the actual comparable beta supports

```math
v=x^a(1-x)^b,\quad q=x^A(1-x)^B,\quad
u=v^h q^n,\quad 0\prec s_u\prec s_v,
```

where $`a,b,A,B>0`$, $`\Delta=aB-bA>0`$, and $`0<h<1`$. Put

```math
H=1-h,\quad \alpha=b/B,\quad k=\Delta/B,
\quad\sigma=n+h\alpha.
```

The second-coordinate source constraints give

```math
0<\sigma<\alpha,\qquad
\lambda_T:=H\alpha-n=\alpha-\sigma>0.
```

At the two original points with one common $`q_0`$, define

```math
D=\frac1{v_L}-\frac1{v_R}>0,\qquad
T=q_0^n(v_L^{-H}-v_R^{-H})>0.
```

Here $`s=\log q_0`$, and the subscript $`s`$ means differentiation with respect to this one common variable. Set

```math
\mathcal I=\frac TD,\qquad
\mathcal J=\frac{T_s}{D_s},\qquad
\mathcal K=\frac{T-T_s}{D-D_s}.
```

All three are positive and strictly increasing on $`0<q_0<q_{\max}`$, with

```math
0<\mathcal J<\mathcal K<\mathcal I,
\qquad
\frac{d\log\mathcal I}{ds}>\sigma,
\frac{d\log\mathcal J}{ds}>\sigma,
\quad\frac{d\log\mathcal K}{ds}>\sigma.
```

Their common lower endpoint limit is zero, and their common upper endpoint limit is

```math
M=H u(A/(A+B)).
```

For a fixed original $`c_1>0`$, let $`R_L,R_R`$ be the original quotients $`(u-c_1)/v`$. At each branch let

```math
L_4=\frac{dR}{dq_0},\qquad L_3=R-q_0L_4.
```

If $`c_1<M`$, there are unique heights $`q_I<q_K<q_J`$ at which respectively $`\mathcal I,\mathcal K,\mathcal J`$ equal $`c_1`$. The three actual branch differences have exactly these strict crossing orders:

```math
R_L-R_R:\ -\ \text{to}\ +\ \text{at }q_I,
```

```math
L_{3,L}-L_{3,R}:\ -\ \text{to}\ +\ \text{at }q_K,
```

```math
L_{4,L}-L_{4,R}:\ +\ \text{to}\ -\ \text{at }q_J.
```

If $`c_1\ge M`$, all three differences keep their initial strict signs. This is one uniform ordering across all allowed $`n`$, all scales, and all cubic root configurations in the $`0<h<1`$ source cone.

## 1. Geometry of the paired beta points

Use $`t=\log x`$, with the two points $`t_L<t_R`$. Write

```math
m=(t_L+t_R)/2,\quad d=(t_R-t_L)/2>0,
\quad u_0=-d_s>0,\quad v_0=m_s>0.
```

The notation $`u_0,v_0`$ in this proof denotes geometric speeds, not the original beta monomials. Put $`r=A/B>0`$. Equality of $`q`$ at the two points can be solved explicitly:

```math
e^m=\frac{\sinh(rd)}{\sinh((r+1)d)},
```

```math
s(d)=B\{r\log\sinh(rd)+\log\sinh d
 -(r+1)\log\sinh((r+1)d)\}.
```

The width $`d`$ strictly decreases as the common height $`q_0`$ increases. Define

```math
\eta=\frac{v_0}{u_0}=-m_d
=(r+1)\coth((r+1)d)-r\coth(rd).
```

Then

```math
0<\eta<1,\qquad \eta_s<0,
\qquad u_{0,s}>0,
\qquad 0<\frac{d\,u_{0,s}}{u_0^2}<1.
\tag{1}
```

Here are proofs of all four claims.

First, $`z\coth z`$ strictly increases on $`z>0`$, giving $`\eta>0`$. The function $`z/(e^{2dz}-1)`$ strictly decreases in $`z>0`$, giving $`\eta<1`$. Also

```math
\eta_d=r^2\operatorname{csch}^2(rd)
 -(r+1)^2\operatorname{csch}^2((r+1)d)>0,
```

since $`z/\sinh z`$ strictly decreases. As $`d_s<0`$, this proves $`\eta_s<0`$.

Second, let $`L=f'(t_L)>0`$, $`R=-f'(t_R)>0`$, where $`f(t)=At+B\log(1-e^t)`$. Both positive slopes decrease with $`s`$, because $`f''<0`$. Thus $`u_0=(L^{-1}+R^{-1})/2`$ strictly increases. Furthermore $`t_{L,ss}>0`$.

For the final claim it suffices to prove $`(d^2)_{ss}>0`$, since

```math
(d^2)_{ss}=2u_0^2-2d u_{0,s}.
```

Define

```math
g(z)=\coth z+z\operatorname{csch}^2z,qquad
P(z)=z^2g(z).
```

The function $`P(z)/z=z\coth z+z^2\operatorname{csch}^2z`$ strictly increases. Multiplying its derivative by $`\sinh^3z`$ gives

```math
N(z)=\cosh z\sinh^2z+z\sinh z-2z^2\cosh z.
```

Its coefficient at $`z^{2j}/(2j)!`$ is

```math
c_j=(9^j-1)/4+6j-8j^2.
```

The first three coefficients vanish; $`c_3=128`$, and

```math
c_{j+1}=9c_j+64j(j-1)>0\quad(j\ge3).
```

Thus $`N(z)>0`$ for $`z>0`$, and $`P`$ is strictly superadditive. Direct differentiation of $`s(d)`$ gives

```math
s_d-ds_{dd}=\frac B{d^2}
 \{P(rd)+P(d)-P((r+1)d)\}<0.
```

As $`s_d<0`$,

```math
(d^2)_{ss}=\frac{2(s_d-ds_{dd})}{s_d^3}>0.
```

This proves (1), using only the actual paired beta geometry.

## 2. A positive mixed integral kernel

For $`\kappa>0`$, define

```math
J_\kappa(s)=\int_{t_L}^{t_R}e^{-\kappa t}\,dt,
\quad
\pi_\kappa(s)=\frac{e^{-\kappa t_L}}L
 +\frac{e^{-\kappa t_R}}R=-J_{\kappa,s}.
```

For $`\lambda\ge0`$, let

```math
P_{\kappa,\lambda}=\pi_\kappa+\lambda J_\kappa>0.
```

We prove that, whenever $`0<\kappa_2<\kappa_1`$ and $`0\le\lambda_2<\lambda_1`$,

```math
\frac{d}{ds}\log
 \frac{P_{\kappa_2,\lambda_2}}{P_{\kappa_1,\lambda_1}}>0.
\tag{2}
```

### Variation in $`\kappa`$

Set $`w=\kappa d`$, $`b_0=\lambda d/u_0`$, and

```math
\mathcal B(w,\eta,b_0)
=\cosh w+\eta\sinh w+b_0\frac{\sinh w}{w}.
```

Then $`P_{\kappa,\lambda}=2e^{-\kappa m}u_0\mathcal B`$. Let $`Q=\mathcal B_w/\mathcal B`$. The exponential-tilted mean of $`t`$ in this kernel is

```math
\mu_{\kappa,\lambda}=-\partial_\kappa\log P_{\kappa,\lambda}=m-dQ.
```

For $`w>0`$, $`0<\eta<1`$, and $`b_0\ge0`$,

```math
Q_\eta>0,\qquad Q_{b_0}<0.
```

The first sign follows by differentiation: its numerator is $`1+b_0\sinh^2(w)/w^2>0`$. For the second, the endpoint distribution has mean at least $`\tanh w`$, whereas the uniform-interval distribution has mean $`\coth w-1/w<\tanh w`$. Adding uniform weight therefore lowers the tilted mean.

Since $`\eta_s<0`$ and

```math
(b_0)_s=-\lambda\left(1+\frac{d u_{0,s}}{u_0^2}\right),
```

the geometric bounds (1) imply

```math
\begin{aligned}
\mu_{\kappa,\lambda,s}
&=u_0\{\eta+Q+wQ_w\}-dQ_\eta\eta_s-dQ_{b_0}(b_0)_s\\
&\ge u_0\{\eta+Q+wQ_w+2b_0Q_{b_0}\}>0.
\end{aligned}
\tag{3}
```

For completeness the last strict sign is an elementary positive polynomial. Multiply its bracket by $`\mathcal B^2`$. The coefficients in $`\eta,b_0`$ are:

| Power of $`\eta`$ | Power of $`b_0`$ | Coefficient |
|---:|---:|---|
| 3 | 0 | $`\sinh^2w`$ |
| 2 | 1 | $`2\sinh^2w/w`$ |
| 2 | 0 | $`(3\sinh(2w)-2w)/2`$ |
| 1 | 2 | $`\sinh^2w/w^2`$ |
| 1 | 1 | $`(4w\sinh(2w)-4w^2-\cosh(2w)+1)/(2w^2)`$ |
| 1 | 0 | $`3\sinh^2w+2`$ |
| 0 | 2 | $`(\sinh(2w)-2w)/(2w^2)`$ |
| 0 | 1 | $`(2w\cosh(2w)-\sinh(2w))/(2w^2)`$ |
| 0 | 0 | $`(2w+\sinh(2w))/2`$ |

Every coefficient is positive for $`w>0`$. For the only less immediate numerator, its quadratic coefficient is $`2w^2`$; every higher even coefficient is positive, since the coefficient of $`w^{2j}`$ in $`4w\sinh(2w)-\cosh(2w)+1`$ is $`2^{2j}(4j-1)/(2j)!`$. The other signs follow from $`\sinh z>z`$ and $`z\cosh z>\sinh z`$.

Equation (3) gives $`\partial_s\partial_\kappa\log P_{\kappa,\lambda}<0`$.

### Variation in $`\lambda`$

The interval hazard is

```math
\frac{\pi_\kappa}{J_\kappa}
=\kappa\{u_0\coth(\kappa d)+v_0\}.
```

Its derivative is strictly positive, because

```math
\frac1\kappa\left(\frac{\pi_\kappa}{J_\kappa}\right)_s
=(u_{0,s}+v_{0,s})
 +u_{0,s}\{\coth(\kappa d)-1\}
 +\kappa u_0^2\operatorname{csch}^2(\kappa d)>0.
```

The first term is $`t_{L,ss}>0`$. Hence

```math
\partial_s\partial_\lambda\log P_{\kappa,\lambda}
=\partial_s\frac1{\pi_\kappa/J_\kappa+\lambda}<0.
```

Decreasing $`\kappa`$ and then $`\lambda`$ therefore proves (2).

## 3. Application to the three original height functions

The exact source relation $`\log v=\alpha s+kt`$ gives

```math
D=e^{-\alpha s}kJ_k,
\qquad
T=e^{-\lambda_Ts}HkJ_{Hk}.
```

In particular both $`D_s,T_s`$ are strictly negative, and

```math
\mathcal J
=H e^{\sigma s}
 \frac{P_{Hk,\lambda_T}}{P_{k,\alpha}},
\qquad
\mathcal K
=H e^{\sigma s}
 \frac{P_{Hk,1+\lambda_T}}{P_{k,1+\alpha}}.
```

Both kernel ratios strictly increase by (2), since $`Hk<k`$ and $`0<\lambda_T<\alpha`$. This proves the strict logarithmic derivative margins.

No earlier one-crossing theorem is needed for $`\mathcal I`$. Indeed

```math
\mathcal I=H e^{\sigma s}\frac{J_{Hk}}{J_k},\qquad
\frac{d\log\mathcal I}{ds}
=\sigma+\frac{\pi_k}{J_k}-\frac{\pi_{Hk}}{J_{Hk}}>\sigma.
```

The last sign follows because the hazard $`\kappa\{u_0\coth(\kappa d)+v_0\}`$ strictly increases in $`\kappa`$: its derivative is

```math
u_0\{\coth w-w\operatorname{csch}^2w\}+v_0>0.
```

Consequently

```math
\mathcal I_s=\frac{D_s}{D}(\mathcal J-\mathcal I)>0
\quad\Longrightarrow\quad \mathcal J<\mathcal I.
```

And

```math
\mathcal K=
rac{D\mathcal I+(-D_s)\mathcal J}{D+(-D_s)}
```

is a strict weighted mean, so $`\mathcal J<\mathcal K<\mathcal I`$.

For $`\mathcal I`$, write $`z=v_R/v_L>1`$. Then

```math
\mathcal I=u(x_L)\frac{1-z^{h-1}}{1-z^{-1}}.
```

As $`q_0\downarrow0`$, the two beta endpoint power laws give $`z\to\infty`$ because $`a/A>b/B`$, while positivity of the left exponent of $`u`$ gives $`u(x_L)\to0`$. Thus $`\mathcal I\to0`$. As the two points merge, the displayed factor tends to $`H`$, so $`\mathcal I\to Hu(A/(A+B))`$.

The zero endpoint limits of $`\mathcal J,\mathcal K`$ follow by squeezing below $`\mathcal I`$. At the other endpoint $`t_L,t_R\to t_0=\log(A/(A+B))`$, $`J_\kappa\to0`$ and $`\pi_\kappa\to\infty`$, so

```math
\frac{P_{Hk,\lambda_T+c}}{P_{k,\alpha+c}}
\longrightarrow e^{hk t_0}\qquad(c=0,1).
```

Thus both limits are $`H e^{\sigma s_{\max}+hk t_0}=Hu(A/(A+B))`$, as claimed.

Finally, the actual branch differences are exactly

```math
R_L-R_R=D(\mathcal I-c_1),
```

```math
L_{4,L}-L_{4,R}=
rac{-D_s}{q_0}(c_1-\mathcal J),
```

```math
L_{3,L}-L_{3,R}=(D-D_s)(\mathcal K-c_1).
```

All prefactors are positive. The inequalities $`\mathcal J<\mathcal K<\mathcal I`$, strict monotonicity, and endpoint limits prove the ordered crossing theorem.

## Scope

This theorem is uniform for the three hard mode regions with $`0<h<1`$, including either sign of $`n`$. It proves one ordered comparison for the original height curve and both actual tangent coefficient functions, without any cubic-root or signed-residue routing. It still leaves open whether these three ordered crossings, together with the original beta curvature, exclude the full seven-node common-coefficient window configuration.
