# Independent divisor proof for one odd P3 event and physical common events

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Retain the strict actual mixed source and its exact identity

```math
Q=w(P_3'G-P_3G')-\lambda_1P_3G=-L_{32}K,
\quad \deg K\le6,\quad K(0)<0,\quad L_{32}>0.
```

The residual `S=P3-kappa h1 G`, kappa>0, is analytic, nonidentity,
negative near both endpoints, and has finite even total physical root
multiplicity N. A failed multiplicity-six ceiling therefore has N>=8.
The argument below proves the N-2 physical K budget in two circumstances:

1. P3 and G have no common physical root, and P3 has exactly one
   odd-order physical root, allowing a triple root or an additional double
   root;
2. P3 and G have any common physical root, with no restriction on the
   number of other P3 roots.

Sextic saturation then supplies the uniform geometry and all-positive-
exponent Hurwitz interface, contradicting N>=8. Thus S has physical
multiplicity at most six on either stated domain. This proof makes no
claim about a common-free P3 with three simple physical roots.

## No common physical root; one odd P3 event

At a numerator root of order r, Q has exact order r-1 with leading
coefficient `+r w P_leading G`. At a denominator root it has exact
order r-1 with leading coefficient `-r w P3 G_leading`. L32 is nonzero
there, so these are exact K weights. They are separate from ordinary
critical weights inside sign components.

First suppose the sole odd P3 event is simple and there is no even P3
root. The previously independently verified pole-divisor formula gives

```math
\operatorname{weight}_{\rm physical}K\ge N-2
+(d_G-e_G)+2e_{G,-}\ge N-2.
```

This depends on one numerator **sign flip**, not on its order relative
to P1 roots or on the sign of G at that event. If the sole odd P3 root
is triple, its two additional K weights only strengthen the budget.

The only remaining cubic possibility is one simple odd P3 root and a
distinct double root q. Delete q temporarily from the event divisor;
the sign of Y=P3/(h1 G) on both sides of q is the same. Restoring this
even numerator event contributes exact K weight one. If its sign is
positive, it splits one positive component and increases the useful
Rolle component subtraction by one, cancelling that weight. If its
sign is negative, it can remove at most one previously forced negative
G-G reciprocal-Rolle gap, again cancelling at most one weight. If it
instead lies in a mixed P-G gap, the negative P-P subgap supplies an
ordinary-Y Rolle critical and strengthens the estimate. In every case
the N-2 budget survives.

All counts are weighted. For r contact weights on an occupied positive
component, contact differentiation plus between-contact Rolle supplies
total weight minus one. A negative G-G gap uses inverse Y; a negative
P-P gap uses Y directly. These gap criticals are disjoint from event
weights and from useful components. This is one divisor insertion
argument, not a dispatch through critical allocations.

## Any physical common P3/G event

The actual source has P3>0 on x<=c and exactly two simple physical P1
roots, with only rB to the right of c. Pluecker therefore implies that
every physical P3/G common root is q=rB, and there is at most one.
Also its minimum common multiplicity is one, since otherwise P1 would
be multiple. Factor

```math
P_3=(x-q)A,\qquad G=(x-q)B.
```

The degree-at-most-two polynomials A,B have negative values at both
endpoints and no common physical root. Exact common-factor cancellation
gives

```math
Q=(x-q)^2\widehat Q,\qquad
K=(x-q)^2\widehat K,\qquad
\deg\widehat K\le4.
```

Set `T=A-kappa h1 B`, and let M be its total physical root multiplicity.
Its endpoint signs are positive and negative, so M is finite and odd.
The full S=(x-q)T has N=M+1, including if T itself has a contact at q.

The ratio V=A/(h1 B) is analytic on every interval between successive
physical B roots, including through any numerator A root. Since B has
degree at most two, there are at most three such pole-free intervals.
Every T root is a V=kappa contact there with the same order: A and B
have no common physical root, so no T root can be a pole. Weighted
Rolle on at most three occupied intervals supplies at least M-3
physical Khat weight. The fixed common factor adds two K weights, giving

```math
\operatorname{weight}_{\rm physical}K\ge M-3+2=N-2.
```

If a Khat critical occurs at q, its multiplicity adds to the fixed two
weights; the accounting does not require distinct critical positions.
Thus a failed ceiling six again forces degree-six physical saturation.

When the common event is odd and P3 has only one odd physical root,
A<=0 everywhere physically. Then every T contact lies in B<0, whose
at-most-two components give M<=6 by the degree-four Rolle bound. Odd
parity improves this to M<=5 and N<=6 directly, without the geometry
or Hurwitz input. This shorter subproof is compatible with the uniform
common-event budget and needs no preservation of even roots.

## Saturation conclusion and limits

In either main domain, N>=8 gives at least six physical K weights.
Degree at most six and nonzero K force complete physical exhaustion
counted with multiplicity. The uniform actual reciprocal geometry
has exactly this premise and no event-word or event-simplicity premise.
It forces P3 and G each to have one simple physical root and two real
exterior roots. The all-positive-exponent root-factor Hurwitz theorem
then gives S multiplicity at most six, including a common physical
P3/G root if present, contradicting N>=8.

This includes the strict three-event words113/131, their double/triple
event seams, and every actual physical common-event source within the
strict cone. The actual source reflection transfers the statement to
the opposite cone. Weak support exponents and common-free three-odd-
P3 five-event charts remain outside the statement.
