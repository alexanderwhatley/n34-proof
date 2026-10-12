# Passing a bound from strict cases to limiting cases

Write $`m_s(x)=x^{s_1}(1-x)^{s_2}`$ for $`0\lt x\lt1`$. This factor is always positive, even when its exponents are negative. A root is counted once in the original function, regardless of its multiplicity. A nonidentity function is a function that is not identically zero.

The argument applies to a finite sum of these factors with real exponents. A strict case has strict inequalities between the relevant parameters. A generic case additionally avoids the finitely or locally finitely many equalities explicitly excluded by the argument. Those equalities must define proper exceptional sets; a condition that holds identically cannot be removed this way.

## The root transfer lemma

Assume every generic strict member of a coefficient-sign family has at most $`B`$ simple roots, uniformly in the allowed coefficient magnitudes. Then every nonidentity member in the closure of the proved strict regions has at most $`B`$ distinct roots, provided the following perturbations preserve the coefficient signs.

**Proof.** Suppose an original function $`F`$ has $`N`$ selected distinct roots. Choose disjoint small compact neighborhoods around these roots, all lying inside $`(0,1)`$. Choose one positive factor $`m`$ whose coefficient is allowed to vary and put $`H=F/m`$. Varying that coefficient by $`\varepsilon`$ changes the root equation to $`H+\varepsilon=0`$.

At an odd-order zero, either sufficiently small nonzero sign of $`\varepsilon`$ retains a crossing. At an even-order zero, one sign splits it into two crossings, and the opposite sign removes it. If there are $`o`$ odd-order zeros and $`e_+,e_-`$ even-order zeros split by the two respective signs, choose the better sign. It produces at least

```math
o+2\max(e_+,e_-)\ge o+e_++e_-=N
```

crossings. Analyticity permits a sufficiently small shift avoiding critical values, so these crossings can be taken simple. The shift preserves the original coefficient sign.

Choose compact sign-changing brackets around the resulting roots. A sufficiently small change of the real exponents and coefficients preserves their endpoint signs, and therefore retains at least $`N`$ roots. Choose that change in the dense generic strict part of the proved parameter region, then regularize its remaining selected roots if needed. A hypothetical $`N\gt B`$ gives a contradiction. $`\square`$

The proof preserves a sufficient total number of original roots. It does not claim that each even root persists individually, or that auxiliary repeated roots remain real.

## Boundaries covered by this argument

Once all adjacent strict original cases have been proved, the lemma covers zero coefficients by approximation with the prescribed sign, zero or repeated exponents, repeated factors, coordinate ties, coincident modes, and simultaneous intersections of such finite parameter equalities. It also covers proper exceptional equalities involving auxiliary polynomials, such as common roots, repeated roots, or a vanishing leading coefficient. An identity remains excluded from the theorem.

Only the selected compact interior brackets are needed. Roots approaching $`0`$ or $`1`$ along a different sequence do not create an additional case. Infinite parameter values are not members of the theorem.

An equality reached inside a continuation argument needs that argument's own local proof. This final transfer lemma cannot replace a first-entry or first-loss argument, and cannot turn an unproved open parameter region into a proved boundary.

## Endpoint parity

A generic function with finitely many simple roots changes sign at each root. Equal signs near $`0`$ and $`1`$ force an even number of roots; opposite signs force an odd number. Thus a generic ceiling of nine becomes eight in an equal-endpoint-sign family. A generic ceiling of ten becomes nine in an opposite-endpoint-sign family. Apply the transfer lemma afterward to recover a statement about distinct roots.
