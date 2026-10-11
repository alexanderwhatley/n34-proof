# An analytic two-coefficient obstruction in the h >= 1 source

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Use the original linked source polynomials

$$
\Pi=\Lambda\prod_{i=1}^3(p-r_i),\quad
C=p(p+1)-\Pi,\quad
E=-(1-h)hp^2-2(1-h)np+n(n-1),
$$

$$
D=(1-h)C+E,\qquad
J=\Pi(EC'-E'C)-(hp+n)CD.
$$

For $h>1$, the full actual source cone can be parametrized by

$$
g=h-1>0,\quad b=r_2-r_1>0,\quad c=r_3-r_2>0,
\quad a=-gr_3-n>0,\quad z=hr_1+n>0,
$$

$$
r_1=a+g(b+c)+z,\quad r_2=r_1+b,\quad r_3=r_2+c,
\quad n=-gr_3-a,\quad \Lambda>0.
$$

Let $u_0=a+g(b+c)>0$, and expand
$J(r_3+t)=\sum_{i=0}^6j_it^i$. Define

$$
\begin{aligned}
P_2={}&3(g+1)u_0(u_0+1)
 +g(g+1)(6b^2+12bc+5c^2)\\
&+3gz(2u_0+z+1)+2gz(5b+7c)>0,\\
P_1={}&g(g+1)\{6a+2(g+2)b+(g+5)c+3z+3\}>0.
\end{aligned}
$$

The entire former 42-monomial sign assertion is the single identity

$$
\boxed{-j_5=\Lambda^2P_2+\Lambda P_1+g^2(g+1)>0.}
$$

The constant coefficient has the direct source expression

$$
j_0=-(hr_3+n)r_3(r_3+1)D(r_3)<0.
$$

Indeed $0<hr_3+n<r_3$, and
$D(r_3)=k(k-1)>0$ with $k=n-(1-h)r_3=-a<0$.
No 117-monomial expansion of the constant term is needed.

A degree-six polynomial with six distinct positive roots must have
opposite signs in its constant and degree-five coefficients. The two
strictly negative signs therefore rule out six roots of $J$ on
$p>r_3$. A degree drop makes the exclusion immediate. At $h=1$,
the linked polynomial has degree at most five, so that face needs no
coefficient sign certificate either.

This replaces the computer-algebra positivity table by a displayed
analytic identity. The companion verifier checks the identity directly;
it expands the displayed formula; it does not supply a separate
sign computation.
