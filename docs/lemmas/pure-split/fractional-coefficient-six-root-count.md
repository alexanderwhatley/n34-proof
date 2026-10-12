# One reciprocal Hurwitz theorem for the low-v mixed branch

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## 1. A literal root-factor theorem

Let `P` be any real polynomial of degree at most three. Let `G` be a real
polynomial of degree three with one root in `(0,1)` and two real roots in
`(-infinity,0) union (1,infinity)`. Suppose

```math
P(0),G(0)>0,\qquad P(1),G(1)<0.
\tag{1}
```

The two exterior roots of `G` may coincide. No root-reality or individual
root-count assumption is made for `P`; there is no ordering assumption
between roots belonging to different polynomials. For any

```math
U>0,\qquad 0<v<1,\qquad\kappa>0,
```

the function

```math
S_\kappa(x)=P(x)-\kappa x^{-U}(1-x)^vG(x)
\tag{2}
```

has at most **six distinct roots in `(0,1)`**. In fact the proof gives the
same ceiling when roots are counted with multiplicity. It includes integer
`U`, coefficient zeros, and coincident roots of the two polynomials.

This is a conditional root-factor theorem: the two-real-exterior-root
assumption for `G` is part of its statement. No conclusion for arbitrary
`G` cubics with complex exterior cofactors is asserted. More generally,
the proof needs only a one-transition reciprocal coefficient row for `G`.

## 2. Reciprocal cubics and one-transition coefficients

Put `z=(1-x)/x`. The map is a smooth bijection from `(0,1)` to `(0,infinity)`
with nonzero derivative. Define

```math
\bar P(z)=(1+z)^3P\left(\frac1{1+z}\right),\qquad
\bar G(z)=(1+z)^3G\left(\frac1{1+z}\right).
\tag{3}
```

The reciprocal cubic `Gbar` has two negative roots and one positive root.
A root `x<0` maps to `z<-1`, and a root `x>1` maps to `-1<z<0`. Also

```math
\bar P(0)=P(1)<0,\quad \operatorname{lc}(\bar P)=P(0)>0,
\tag{4}
```

and the same identities hold for `G`. Thus

```math
\bar G=\sigma_G(z-r_G)(z+s_G)(z+t_G),
\tag{5}
```

where all displayed parameters are positive.

Here is the elementary coefficient input, with no sign-cell table.

**One-transition lemma.** If

```math
Q(z)=\prod_{j=1}^m(z+s_j)=\sum_{j=0}^m q_jz^j,
\qquad s_j>0,
```

then `q_j>0` and `q_j^2>=q_(j-1)q_(j+1)`. Consequently the zero-deleted
coefficient word of `(z-r)Q`, for `r>0`, is one negative block followed by
one positive block.

For completeness, positive two-entry convolution preserves log-concavity.
If `c_j=a b_j+b b_(j-1)`, its log-concavity difference is exactly

```math
\begin{aligned}
c_j^2-c_{j-1}c_{j+1}
={}&a^2(b_j^2-b_{j-1}b_{j+1})
 +b^2(b_{j-1}^2-b_{j-2}b_j)\\
 &+ab(b_jb_{j-1}-b_{j-2}b_{j+1}).
\end{aligned}
\tag{6}
```

The last bracket is nonnegative by the ordered adjacent ratios of a
positive log-concave sequence. Endpoint zeros outside its positive block
cause no exception. Induction over the factors proves log-concavity of
`q`. The coefficients of `(z-r)Q` are

```math
-rq_0,\quad q_0-rq_1,\ldots,q_{m-1}-rq_m,\quad q_m.
\tag{7}
```

The thresholds `q_(j-1)/q_j` are nondecreasing, so their signs can switch
only once, from negative to positive. An equality makes a coefficient zero
and is simply deleted. This proves the lemma.

Write

```math
U=n+\zeta,\qquad n=\lfloor U\rfloor\ge0,
\qquad0\le\zeta<1,
```

and set

```math
A=-\bar P,\qquad C=(1+z)^n\bar G,\qquad
F(z)=z^v(1+z)^{\zeta-v}.
\tag{8}
```

The cubic `A` has `A0=-P(1)>0` and `A3=-P(0)<0`; its two interior
coefficients are unrestricted. By the lemma, `C` has coefficient word
`-...+`. The negative root `-1` is repeated `n` times; the lemma allows
such repetitions. The single C transition is zero-safe.
Alternatively, multiplying a one-transition row `-...+` by `(1+z)`
preserves that transition: adjacent coefficient sums are negative before
the transition and positive after it, with at most one mixed sum between
the two blocks. Coefficient zeros introduce no additional sign change;
iteration proves the broader one-transition reciprocal-G formulation.
Multiplying (2) by the nonzero factor `-(1+z)^3` gives exactly

```math
A(z)+\kappa F(z)C(z)=0.
\tag{9}
```

There is no degree-cell, critical-allocation, exterior-pairing, or ell-order
condition in (8)-(9).

## 3. The fractional flag is strict, including integer U

The representation used in the retained Stieltjes--Hurwitz proof is

```math
\frac{F(z)}z=\int_0^\infty\frac{d\mu(s)}{z+s},
\qquad z>0,
\tag{10}
```

where

```math
\frac{d\mu}{ds}=\frac1\pi
\begin{cases}
\sin(\pi v)s^{v-1}(1-s)^{\zeta-v},&0<s<1,\\
\sin(\pi\zeta)s^{v-1}(s-1)^{\zeta-v},&s>1.
\end{cases}
\tag{11}
```

For `0<zeta<1`, this follows from the negative-axis jumps of the principal
branches, or the usual Cauchy representation for a Stieltjes function.
The endpoint exponents make the first density locally integrable; the
weighted tail is integrable because `zeta<1`. The measure is strictly
positive on `(0,1)`, hence has infinite support.

When `zeta=0`, the second density is zero, and (10) is the direct identity

```math
F(z)=\frac{\sin(\pi v)}\pi
\int_0^1\frac{z}{z+s}s^{v-1}(1-s)^{-v}\,ds.
\tag{12}
```

Putting `s=r/(1+r)` and then `r=z w/(1+z)` reduces the integral to
`z^v(1+z)^(-v)` times `int_0^infinity w^(v-1)/(1+w) dw`.
The latter Euler integral equals `pi/sin(pi v)`. Thus this wall has its
own positive infinite-support measure; its strictness is not deduced by
passing to a limit from nonintegral `U`.

The retained finite Stieltjes--Hurwitz lemma, in its exact column
orientation, therefore applies to every finite ordered subfamily of

```math
1,F,z,zF,z^2,z^2F,z^3,z^3F,z^4,z^4F,\ldots.
\tag{13}
```

Here is its strictness mechanism, to make the dependency precise. For a
finite positive Stieltjes measure at distinct nodes `s_j>0`, write

```math
F_N=z e/d,\qquad
d=\prod_j(z+s_j),\qquad
e=\sum_j a_j\frac d{z+s_j},\quad a_j>0.
```

Multiplication by the positive polynomial `d` sends the full alternating
flag to the transpose-Hurwitz coefficient columns

```math
D_0,E_1,D_1,E_2,D_2,E_3,\ldots,
\qquad D_j=z^jd,\quad E_j=z^je.
\tag{14}
```

The finite positive Stieltjes continued-fraction factorization makes this
coefficient array totally nonnegative. It is the exact finite lemma proved
in [the fractional-power basis proof](fractional-root-factor-argument.md), Section 2.
Cauchy--Binet with the positive confluent monomial-jet minors then gives
nonnegative Wronskians. Choose the number of nodes larger than the largest
polynomial shift in the selected family. Because `gcd(d,ze)=1`, an identity
`d P+ze Q=0` forces `d|Q`, then `Q=P=0`; the selected columns therefore have
full rank. Some Cauchy--Binet term is positive, so the Wronskians are strict.

For the measure (11), this finite proof applies at each chosen point
literally. Fix `z0>0` and push forward
`dnu=dmu/(z0+s)` by `w=1/(z0+s)`. This is a finite positive measure on
`[0,1/z0]` with infinite support. Its `N`-node Gaussian rule has positive
weights and distinct interior nodes and exactly matches moments through
degree `2N-1`. Those moments give the derivatives of `F/z` at `z0`.
Taking `N` above both the largest selected shift and half the largest jet
order produces a finite atomic `F_N` matching every jet used in the
selected Wronskian. Thus the same Wronskians are strictly positive for
`F`; the preceding finite argument proves it at `z0`, without a strict
positivity claim inferred from approximation.

Consequently (13) is the required strict Descartes flag. The generalized
Descartes theorem bounds the zeros of (9), including multiplicities, by
the zero-deleted variations of its coefficient row in that order.

## 4. One insertion argument replaces the threshold table

Write `C=sum_(j=0)^(n+3) c_j z^j`. The merged row in (13) is

```math
(A_0,\kappa c_0,A_1,\kappa c_1,A_2,\kappa c_2,
A_3,\kappa c_3,\kappa c_4,\ldots,\kappa c_{n+3}).
\tag{15}
```

Positive `kappa` does not affect any signs. First fill coefficient zeros
within the C word without adding a component variation. Such a filling
exists: place its one transition somewhere between the last negative and
the first positive coefficient. Fill any A coefficient zeros arbitrarily.
Inserting nonzero signs in formerly zero merged positions cannot decrease
its variation. It therefore suffices to bound the filled row; the A word
does not need to have one transition.

Start from `(A0,c0,c1,...,c_(n+3))`. It has two variations: `A0>0`,
`c0<0`, and the C word switches once to its positive final coefficient.
Inserting `Ai`, for `i=1,2,3`, between `c_(i-1),c_i` adds either zero or
two variations; it adds two exactly if

```math
\operatorname{sgn}c_{i-1}=\operatorname{sgn}c_i
=-\operatorname{sgn}A_i.
\tag{16}
```

All three insertions cannot add two. If they did, their common neighbors
would force

```math
\operatorname{sgn}A_1=\operatorname{sgn}A_2
=\operatorname{sgn}A_3
=-\operatorname{sgn}c_0.
```

But `A3<0` and `c0<0`, a contradiction. At most two insertions add two;
the bound is therefore `2+2+2=6`. This proves the theorem for every
`n>=0` at once. The proof has no transition-index table and no unit-tail
casework. The final row can be short (`n=0`) or arbitrarily long.

## 5. Actual mixed application and its limits

In the original strict mixed support dictionary,

```math
a_1=-U<0<a_2<a_3,\qquad b_3<0<b_1=v<b_2,
```

the actual polynomials are

```math
\begin{aligned}
P_3&=\lambda_2(\lambda_3 L_{32}+D L_{32})
       -(D\lambda_2)L_{32},\\
G&=(\lambda_3-\lambda_1)L_{21}L_{32}
       +(D L_{32})L_{21}-(D L_{21})L_{32},
\end{aligned}
\tag{17}
```

where `D=x(1-x)d/dx`, `lambda_i=a_i-(a_i+b_i)x`, and
`L_ji=lambda_j-lambda_i`. The separately retained saturated one-G
exterior atlas ([actual reciprocal root geometry](reciprocal-root-geometry.md), Section2) gives exactly the G hypotheses (1)-(5)
throughout its actual degree cells. A new source-dictionary module may
replace that atlas input; the present root-factor proof does not assume
the cells can be inferred from free cubics alone.

Therefore, on **every saturated actual one-G word-131 chart with
`0<v<1`**, the same theorem gives

```math
Z_{(0,1)}(P_3-\kappa h_1G)\le6.
\tag{18}
```

The phase-independent universal bridge ([s082](original-five-event-entry.md)) would force at least
eight distinct roots of this same equation from a hypothetical ten-root
original row. Equations (18) and that bridge are incompatible. This
removes all three critical allocations at once and uses neither the sign
of `B(c)` nor an ell-before/ell-after routing decision.

The reflected `313` application must use the original transformation
`x->1-x` together with exchange of labels1 and3. Its equation is
`-P1-kappa1 h3 G=0`, with `kappa1=rho kappa`; an independent permutation
of arbitrary cubic roots is not a reflection dictionary.

This application does not claim a bound for the raw equation
`R=h1 P1+rho h3 P3`, for arbitrary G cubics lacking the required real
exterior roots or one-transition reciprocal coefficient row,
for the `v>=1` region, or for event/source boundaries outside the strict
original mixed chart. Those are distinct inputs or targets. All original
mixed no-ten branches were already established; this is a consolidation
of their proofs, not the announcement of a formerly missing global case.
