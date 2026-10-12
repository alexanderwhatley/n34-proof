# One shifted Hurwitz theorem for all positive endpoint exponents

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## 1. Literal root-factor statement

Let `P,G` be real cubics. Suppose each has one root in `(0,1)` and two real
roots outside `[0,1]`, and

```math
P(0),G(0)>0,\qquad P(1),G(1)<0.
```

The exterior roots need not be distinct; roots of different polynomials
need not be disjoint or ordered. For **every**

```math
U>0,\qquad v>0,\qquad\kappa>0,
```

the common-level function

```math
S_\kappa(x)=P(x)-\kappa x^{-U}(1-x)^vG(x)
\tag{1}
```

has at most **six roots in `(0,1)`**, counted with multiplicity. This includes
equal endpoint exponents, all integer walls, coefficient zeros, and repeated
exterior roots. No comparison of component heights or critical-point
allocation is a hypothesis.

The real-cofactor hypothesis is essential to the proof. The theorem is not
an unrestricted assertion for arbitrary cubic pairs or for the raw source
equation `R=h1 P1+rho h3 P3`.

## 2. Orient the endpoint exponents by exact profile duality

The duality sends

```math
(P,G,U,v,\kappa)\longmapsto
(-G(1-y),-P(1-y),v,U,1/\kappa),\qquad y=1-x.
\tag{2}
```

Its residual is `S_kappa(1-y)/(kappa h(1-y))`, where the divisor is positive
and real analytic. Both endpoint orientations and both real-cofactor
conditions are preserved, and root multiplicities are preserved. We may
therefore orient the pair so that

```math
U\ge v>0.
```

Write

```math
U=n+\zeta,\quad v=m+\eta,\quad
n=\lfloor U\rfloor\ge m=\lfloor v\rfloor\ge0,
\quad0\le\eta,\zeta<1.
\tag{3}
```

Set `z=(1-x)/x` and take the reciprocal cubics as in the theorem.
The real negative reciprocal cofactors give one-transition coefficient
words for

```math
A=-\bar P:\quad +\cdots-,\qquad
C=(1+z)^{n-m}\bar G:\quad -\cdots+.
\tag{4}
```

These words follow from the retained log-concavity threshold lemma,
including all coefficient zeros. The equation is exactly

```math
A+\kappa z^m F C=0,
\qquad F=z^\eta(1+z)^{\zeta-\eta}.
\tag{5}
```

The integer multiplier is always a polynomial: (3) gives `n-m>=0`.

## 3. The same fractional flag covers every nonconstant F

If `eta>0`, then `0<eta<1`, and the strict fractional
Stieltjes--Hurwitz flag applies literally to `F`, including `zeta=0`:

```math
1,F,z,zF,z^2,z^2F,\ldots.
\tag{6}
```

For the remaining nonconstant wall `eta=0,zeta>0`, put

```math
F_0=(1+z)^\zeta-1.
```

This is a complete Bernstein function with `F0(0)=0`, `F0(z)/z->0`, and
an infinite-support positive Stieltjes representation

```math
\frac{F_0(z)}z=
rac{\sin(\pi\zeta)}\pi
\int_1^\infty\frac{(s-1)^\zeta}{s(z+s)}\,ds.
\tag{7}
```

For a direct check, put `t=s-1` and use

```math
\frac{z t^\zeta}{(t+1)(t+1+z)}
=(1+z)\frac{t^{\zeta-1}}{t+1+z}
-\frac{t^{\zeta-1}}{t+1}.
```

Integrating and applying the Euler integral gives `(1+z)^zeta-1` after
multiplication by `sin(pi zeta)/pi`. Thus the retained generic finite
Stieltjes--Hurwitz lemma supplies a strict flag for `F0`.

Since `F=1+F0`, each adjacent pair of columns is transformed by

```math
(z^j,z^jF_0)\longmapsto(z^j,z^j+z^jF_0)
=(z^j,z^jF).
\tag{8}
```

The corresponding coefficient transformation is a block-diagonal matrix
with blocks `[[1,1],[0,1]]`. It is totally nonnegative, and all its principal
minors equal one. Cauchy--Binet therefore preserves every strict positive
ordered collocation minor and Wronskian: the matching principal-minor term
alone is strictly positive. This proves the strict flag (6) also on this
wall. Equivalently, `F/z` has the positive measure in (7) plus a unit atom
at zero; no strictness is inferred by taking a parameter limit.

Thus every nonconstant F in (5) has the required strict flag. The one
constant possibility, `eta=zeta=0`, is treated by ordinary polynomial
Descartes in Section5, with the same coefficient argument.

## 4. One insertion proof bounds every shifted merge

In (6), the column `z^(m+j)F` lies immediately after the monomial column
`z^(m+j)`. First fill zeros in A and C preserving their one-transition
words; zero deletion can only lower the variation of the merged row.

Begin with the A prefix through index `min(m,3)`, followed by the full C
coefficient row. This baseline always has exactly two variations. Indeed,
the A prefix starts positive and switches at most once to negative, C
starts negative, and C later switches once to its positive last entry.

The remaining A coefficients, if any, are inserted into successive C
seams. There are at most three such insertions. Each adds either zero or
two variations, and adds two only if its two C neighbors agree and have
the opposite sign. If at most two A coefficients remain, the bound six
is immediate. If three remain, necessarily `m=0`. All three adding two
would force `sgn(A1)=sgn(A2)=sgn(A3)=-sgn(c0)`;
because `A3<0,c0<0`, that is impossible.
Hence at most two insertions add two in every shift, and the bound is

```math
V(\text{merged row})\le2+2+2=6.
\tag{9}
```

The tail length and transition position do not enter the argument.
Generalized Descartes for the strict flag proves the theorem whenever F
is nonconstant. No threshold table or allocation table is used.

## 5. Pure integer endpoint exponents

When `eta=zeta=0`, equation (5) is the polynomial `A+kappa z^m C`.
Its ordinary monomial coefficient row is obtained from the same formal
merged row by summing the adjacent entries representing equal monomials.
Such an aggregation cannot increase zero-safe variation: a nonzero sum
of two real numbers has the sign of at least one summand, so its sign
word is a subsequence of the unaggregated word; zero sums are deleted.
Applying this observation successively gives at most six variations by
(9). Because positive integer v has `m>=1`, the polynomial has constant
coefficient `A0>0` and is not identically zero. Ordinary polynomial
Descartes, including multiplicities, proves
the same literal ceiling. This is an exact polynomial argument at the
integer walls, not a perturbation of source parameters.

## 6. Actual mixed integration and proof reduction

The separately verified saturated one-G actual-source atlas supplies the
two real exterior cofactors of both `P3` and `G`. The present theorem then
gives `Z(P3-kappa h1 G)<=6` for every positive endpoint exponent pair.
The retained phase-independent bridge would give at least eight distinct
roots from a hypothetical ten-root original row, a contradiction.

Consequently the preferred saturated `131/313` proof needs only the actual
source exterior atlas, this single shifted Hurwitz theorem, the eight-root
bridge, and the correct original source reflection. It uses **neither**
the Cauchy count excluding `U>=1,v>=1` **nor** a Theta height comparison.
It also avoids `1+5/3+3/5+1` routing, ell ordering, and endpoint-exponent
threshold routing after the atlas is supplied.

The theorem's profile duality (2) is still distinct from the actual source
reflection exchanging outer labels1 and3. Unsaturated actual sources
without the displayed real-cofactor property and boundaries outside the
strict saturated atlas retain their original proof routes. Earlier
Cauchy and height modules remain valid independent backups.
