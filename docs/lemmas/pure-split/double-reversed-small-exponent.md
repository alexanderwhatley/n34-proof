# A uniform low-beta double-reversed Hurwitz five-root theorem

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Statement and actual-source scope

Let

```math
u,p,a,b,q,z\gt0,\qquad q\lt a,\quad p\lt b,
\qquad \alpha=u+q\in(0,1),\quad \beta=p+z\in(0,2).
```

Retain the actual double-reversed source cubics

```math
A=(u+pt)(a-bt)[a+u-(b-p)t]-(ap+bu)t(1+t),
```

```math
B=(q+zt)(a-bt)[(b+z)t-(a-q)]+(az+bq)t(1+t).
```

For every $`\rho\gt0`$,

**(1)**

```math
\boxed{H=A+\rho t^\alpha(1+t)^{\beta-\alpha}B
\text{ has at most five distinct positive roots}.}
```

The seam $`\beta=1`$ is included. No ordering between $`\alpha`$ and
$`\beta`$ is required. Raw coefficient zeros and cross-cubic positive-event
coincidences are included: the proof uses coefficients rather than strict
ordering of the roots of the two cubics. The boundary $`\beta=2`$ is not part
of this statement. Original-row no-ten perturbation handles that boundary
without a new raw seam theorem.

Under the usual reflection to $`\beta\ge\alpha`$, this one argument covers
both remaining low pairs $`I_0\times I_0`$ and $`I_0\times I_1`$, including
their $`\beta=1`$ wall. It removes the old low-band fourth-derivative
annihilator from the original distinct no-ten route.

## 1. Actual cubics supply two coefficient variations

Put $`c=a/b`$. Their endpoint, leading and mode signs are

```math
A_0=au(a+u)\gt0,\quad A_3=pb(b-p)\gt0,\quad
A(c)=-b(u+pc)c(1+c)\lt0,
```

**(2)**

```math
B_0=-aq(a-q)\lt0,\quad B_3=-zb(b+z)\lt0,\quad
B(c)=b(q+zc)c(1+c)\gt0.
```

Thus each cubic has two positive roots. Ordinary polynomial Descartes and
their endpoint coefficient signs give exactly two zero-deleted coefficient
variations each. After coefficient zeros are filled without increasing
their variations, the A word is one of

**(3)**

```math
\texttt{++-+},\qquad\texttt{+-++},\qquad\texttt{+--+},
```

while B has one positive coefficient block between its negative ends.

Write

```math
n=\begin{cases}0,&0\lt\beta\lt1,\\1,&1\le\beta\lt2,\end{cases}
\qquad \zeta=\beta-n\in[0,1),
```

**(4)**

```math
G=t^\alpha(1+t)^{\zeta-\alpha},\qquad
C=(1+t)^nB=\sum_{j=0}^{n+3}c_jt^j.
```

Pascal convolution is variation diminishing, so $`V(C)\le2`$.
Multiplication by the positive factor $`(1+t)^n`$ preserves the two
positive roots of B; polynomial Descartes therefore gives $`V(C)=2`$.
Its endpoints are $`c_0=B_0\lt0`$ and $`c_{n+3}=B_3\lt0`$.
Its zero-deleted sign word is precisely $`\texttt{-+-}`$.

## 2. The same fractional flag applies when n is zero or one

For $`0\lt\zeta\lt1`$, G is the complete Bernstein function from frozen
[fractional-power basis proof](fractional-root-factor-argument.md), Section2. Its positive Stieltjes measure has density

**(5)**

```math
\frac{d\mu}{ds}=\frac1\pi
\begin{cases}
\sin(\pi\alpha)s^{\alpha-1}(1-s)^{\zeta-\alpha},&0\lt s\lt1,\\
\sin(\pi\zeta)s^{\alpha-1}(s-1)^{\zeta-\alpha},&s\gt1.
\end{cases}
```

It has infinite support, $`G(0)=0`$ and $`G(t)/t\to0`$.
The source's strict Stieltjes--Hurwitz/Gaussian argument consequently
applies to every finite subfamily of

**(6)**

```math
1,G,t,tG,t^2,t^2G,t^3,t^3G,t^4G,\ldots.
```

That argument depends on the fractional factor G, not on a condition
$`n\gt0`$: the finite polynomial multiplier is expanded only afterward.
Thus the cross-band source's initial scope restriction $`n\gt m`$ is not a
restriction on this flag lemma. Here $`m=0`$, and n may equally be zero.

For the included seam $`\beta=1`$, one has $`n=1,\zeta=0`$ and
$`G=t^\alpha/(1+t)^\alpha`$. It has the exact representation

**(7)**

```math
G(t)=\frac{\sin(\pi\alpha)}\pi
\int_0^1\frac{t}{t+s}s^{\alpha-1}(1-s)^{-\alpha}\,ds.
```

To verify (7), put $`s=r/(1+r)`$. The integral without its constant
becomes

```math
t\int_0^\infty\frac{r^{\alpha-1}}{t+(1+t)r}\,dr
=t^\alpha(1+t)^{-\alpha}
\int_0^\infty\frac{v^{\alpha-1}}{1+v}\,dv,
```

and the last Euler integral is $`\pi/\sin(\pi\alpha)`$.
The measure is strictly positive on $`(0,1)`$, has infinite support,
and G is bounded with $`G(0)=0`$. Thus the same strict finite-quadrature
proof applies at this wall; this is not an inference of strictness from a
limit. Gaussian quadrature for the weighted pushforward measure matches
the finitely many jets at each chosen positive point, with more nodes than
the largest selected shift. The finite Hurwitz coefficient columns then
have full rank by coprimeness of their Stieltjes numerator/denominator.
This is the literal strictness mechanism retained from frozen [fractional-power basis proof](fractional-root-factor-argument.md),
Section5.2, and [fractional-power basis proof](fractional-root-factor-argument.md), Section2.

Generalized Descartes for (6) bounds the zeros of H by the zero-safe
variations of its merged coefficient row. The retained flag theorem gives
the stronger multiplicity count, although only distinct roots are claimed
in (1).

## 3. A short coefficient prefix makes seven variations impossible

In the flag order (6), the exact merged row is

**(8)**

```math
(A_0,\rho c_0,A_1,\rho c_1,A_2,\rho c_2,
A_3,\rho c_3,\rho c_4),
```

where the final entry is omitted for n=0. Positive $`\rho`$ does not
change any sign.

First fill coefficient zeros in A and C without increasing either word's
two variations. Such completions exist because their nonzero words begin
and end in the same sign and have exactly one block of the opposite sign.
Inserting any nonzero sign at a formerly zero position cannot decrease the
merged row's variation. It therefore suffices to bound the completed rows.

Start with $`(A_0,c_0,\ldots,c_{n+3})`$, which has three variations.
Inserting A1, A2 or A3 between consecutive C signs changes the variation
by two exactly when the two neighbors agree and oppose the inserted sign;
otherwise it changes it by zero. Since $`c_0\lt0`$, the three A words in (3)
have these consequences:

- For $`\texttt{++-+}`$, the A1 and A2 two-change conditions are mutually
  exclusive. Two insertions can contribute only through A1 and A3, forcing
  $`c_0,c_1,c_2,c_3\lt0`$.
- For $`\texttt{+-++}`$, A1 contributes zero. Two insertions require A2
  and A3, again forcing $`c_0,c_1,c_2,c_3\lt0`$.
- For $`\texttt{+--+}`$, A1 contributes zero and the A2/A3 conditions are
  mutually exclusive, so there are at most five variations immediately.

In the first two words, seven variations therefore require
$`c_0,c_1,c_2,c_3\lt0`$, followed by a later nonempty positive block and
the final negative block of C. This is impossible here. For n=0 all four
C coefficients have already been listed; for n=1 the only later coefficient
is $`c_4=B_3\lt0`$. Thus every merged row has at most five zero-safe
variations. Generalized Descartes proves (1).

## 4. Boundary and integration requirements

The theorem includes every raw coefficient-zero seam inside its displayed
support/gap domain and does not require distinct events between A and B.
The gap boundary $`\alpha=1`$ is already included by the minimum-gap-one theorem when both gaps are at least one. Original no-ten
regularization and reflection cover other gap seams and $`\beta=2`$ by
perturbing a hypothetical ten-simple-root source into an adjacent proved
open chart. No new arbitrary multiplicity theorem on event-collision or
gap-two walls is asserted here.

The original low-band annihilator and Bernstein seam proof are thereby
unnecessary in the new double-reversed no-ten pipeline. The common
fractional flag, Pascal expansion and source dictionary remain. They are
also used for the high-beta exceptional entry, so this is substantive
proof-module consolidation rather than another band-table relabeling.
