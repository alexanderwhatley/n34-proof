# Fractional-power basis and root-count tools

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

This document gives the common-level regularization, the fractional-power coefficient theorem, and the positive-kernel fact used in the split-support proofs. Each statement retains its printed assumptions.

## 1. Common-height regularization of the original row

Let a nonconstant real-analytic original row have $n$ selected distinct interior zeros. Choose disjoint compact neighborhoods with no other zeros. Let $o$ count the odd-order zeros and $e_+,e_-$ the even-order local minima and maxima. One sufficiently small sign of the common level shift $f=t$ yields at least $o+2e_+$ nearby roots; the other yields at least $o+2e_-$. The larger count is at least $n$. Choose the shift to be a regular value on the compact neighborhoods; the resulting roots are simple.

For $|t|<1$,

$$
\frac{f-t}{1-t}=1-\sum_i\frac{E_i}{1-t}x^{a_i}(1-x)^{b_i}.
$$

All coefficients undergo **one common positive scaling**. The simple roots persist in disjoint sign brackets under every sufficiently small support and coefficient perturbation. This supplies the open counterexample set used by the strict AP/PS reductions, without an assumed multiplicity bound.

The predecessor proves the direct global distinct ceiling eleven by two Rolle/Wronskian steps and the El Hilany–Tavenas bound for a beta factor times a cubic plus a cubic. Same endpoint signs and generic simplicity make a hypothetical count at least ten exactly ten. Opposite endpoint signs admit a zero-free first derivative divisor, lower the direct ceiling to ten, and force an odd count, hence at most nine. The original strict chamber classification can therefore be used exactly as archived.

Genericity must be applied in the original parameter family. Nontrivial polynomial discriminants, resultants, degree walls, support ties and integer exponent seams can be avoided inside the retained simple-root neighborhood. Critical values of a nonconstant one-variable analytic profile can be avoided when choosing its free common level. One must establish that a discarded wall is proper on the relevant chart; an identity case receives a lower-order argument. This does **not** discard an extremal or first-loss locus imposed by a subsequent proof. That distinction is decisive for COMP-REACH.

The complete original-root transfer is also given in [the limiting-cases lemma](../baseline/limiting-cases.md).

## 2. A strict fractional-power Descartes flag

The AP upper-fork and PS shuffle arguments require the ordered flag

$$
1,F(t),t,tF(t),t^2,t^2F(t),\ldots,
 \qquad F(t)=t^\gamma(1+t)^{\zeta-\gamma},\quad t>0,
$$

where $0\le\gamma,\zeta<1$. Away from the constant case, every finite ordered subfamily has strictly positive ordered Hermite evaluation determinants. In particular a nonzero finite combination has no more positive zeros, counted with multiplicity, than zero-deleted variations of its ordered coefficient row. Multiplication of all basis functions by a common positive factor is harmless. Integer powers and Pascal multiplication in the source arguments must retain their displayed ordering.

The next argument fixes the coefficient-matrix orientation and proves strictness by matching a finite list of derivatives.

### 2.1 Positive integral representation

For $\gamma>0$, use

$$
F(t)=t\int_0^\infty\frac{\mu(ds)}{t+s}.
$$

The measure has density

$$
\frac{\sin(\pi\gamma)}{\pi}s^{\gamma-1}(1-s)^{\zeta-\gamma}
 \quad(0<s<1),
$$

and

$$
\frac{\sin(\pi\zeta)}{\pi}s^{\gamma-1}(s-1)^{\zeta-\gamma}
 \quad(s>1).
$$

The second density is zero when $\zeta=0$. Both are nonnegative, the measure has infinite support, and $\int(1+s)^{-1}\mu(ds)<\infty$. The identity follows from the upper boundary imaginary part of the principal-branch function on the negative axis and the Cauchy integral formula; the arcs vanish because both endpoint exponents are below one and $F(0)=0$.

When $\gamma=0<\zeta$, apply the representation to $F-1$, with the positive density on $(1,\infty)$. Restoring the constant is a blockwise totally nonnegative shear on each adjacent pair $(t^k,t^k(F-1))$, with positive diagonal. When $\gamma=\zeta=0$, $F=1$; merge adjacent duplicate monomials and use ordinary Descartes. This constant case is not advertised as a strict two-column flag.

### 2.2 Correct rational Hurwitz orientation

For a finite positive atomic measure, write

$$
F_N(t)=t\sum_{j=1}^N\frac{a_j}{t+s_j}
       =\frac{t e(t)}{d(t)},\qquad a_j,s_j>0,
$$

with distinct $s_j$, $\deg d=N$, $\deg e=N-1$, and $\gcd(d,te)=1$. The function $e/d$ maps the upper half-plane to the lower half-plane and is positive on the positive real axis. Therefore $d/e$ is a meromorphic Pick function, nonnegative and regular on the nonnegative real axis.

Apply Theorem 1.4, equation (1.5), of Alexander Dyachenko, *Total nonnegativity of infinite Hurwitz matrices of entire and meromorphic functions*, [arXiv:1304.0801v1](https://arxiv.org/pdf/1304.0801v1). In that paper set $p=e/e(0)$, $q=d/e(0)$. Its “S-function” is $q/p=d/e$; this is the upper-half-plane convention. Its coefficient rows are, up to the same positive normalization,

$$
d,\ te,\ td,\ t^2e,\ t^2d,\ldots.
$$

They are exactly the polynomial coefficient rows of the desired rational flag after multiplication by $d$. This fixes the possible reciprocal/sign ambiguity in the phrase “Stieltjes–Hurwitz theorem.” The entire factors are polynomials, so the genus-zero condition holds. The external theorem is identified in [the references](../../references.md).

### 2.3 Why the determinants are strictly positive

Fix a finite ordered selection of flag functions and let $D$ be its largest power shift. For $N>D$, a polynomial relation among the selected rational functions, after multiplication by $d$, would read

$$
dP+teQ=0,\qquad\deg P,\deg Q\le D.
$$

Coprimality implies $d\mid Q$. Thus $Q=P=0$. The selected rows of the totally nonnegative coefficient matrix consequently have full row rank, so some maximal minor is positive. All ordered monomial evaluation minors at positive increasing nodes are positive. The same holds for consecutive Hermite jets at each node: the generalized Vandermonde is the ordinary Vandermonde times a Schur polynomial, and after confluence its remaining factors and that polynomial are positive. Cauchy–Binet now makes every selected rational evaluation determinant strictly positive.

One still needs to transfer strictness to the nonrational integral. Uniform approximation alone is insufficient. The transfer is exact at the finitely many jets being tested:

1. For nodes $t_i>0$ with multiplicities $m_i$, put $M=\sum_i m_i$, $y=s/(1+s)$, and let $\nu$ be the pushforward of $\mu/(1+s)$ to $[0,1]$. Then
   $F(t)/t=\int [t+(1-t)y]^{-1}\nu(dy)$.
2. Set $L_i(y)=t_i+(1-t_i)y$ and $Q_0(y)=\prod_i L_i(y)^{m_i}>0$. Use an $N$-node positive Gaussian quadrature rule for $\nu/Q_0$, choosing $N>D$ and $2N-1\ge M-1$.
3. Each required derivative of $F(t)/t$, after multiplication by $Q_0$, is a polynomial of degree at most $M-1$. The quadrature therefore matches every required jet **exactly**. Its nodes lie in $(0,1)$, and it yields positive atoms $s_j=y_j/(1-y_j)$, $a_j=\omega_j Q_0(y_j)/(1-y_j)$.
4. The determinant for the original function equals the determinant of this finite rational flag. Section 2.3 makes it strictly positive.

There is no finite upper bound on allowed shifts: choose $N$ after the finite flag has been chosen. Standard variation diminution for a strictly totally positive evaluation kernel, including its consecutive Hermite rows, gives the stated coefficient-sign zero bound. The source papers' central-prefix cofactor argument uses this strict positivity, not a supposed strict limit of positive numbers.

## 3. Cauchy-square input and the paired-cofactor distinction

The rational logarithmic-derivative arguments use the Cauchy-square kernel $(x+s)^{-2}$ on separated positive coordinates. Strict positivity of its distinct-node minors follows from Borchardt's Cauchy determinant identity; integration over successive nonempty sign blocks preserves strictness. If consecutive Hermite rows are used, strictness also follows from

$$
(x+s)^{-2}=\int_0^\infty u e^{-xu}e^{-su}\,du
$$

and the integral determinant formula with the ordered exponential kernels. This is the usual variation-diminishing input behind the cumulative-charge ceilings. The actual event order and the signs of the block density remain hypotheses; total positivity does not supply them.

The kernel statement is used together with the local pole order and the signs of the residue blocks. It does not supply those signs automatically. The [double-reversed component proof](double-reversed-component-compatibility.md) and its [positive-matrix prefix theorem](positive-matrix-prefix.md) give the additional comparisons used by the main argument.
