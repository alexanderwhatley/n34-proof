# A quadratic-ratio common-level theorem

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

the earlier proof fork lane, 2 October 2026. The proof is elementary. It is
independent of any beta-root counting theorem or event-word source atlas.

Let v>0 be C2 on (a,b), strictly log-concave, and tending to zero at both
endpoints. Let r1<r2 and h1<h2 be distinct points of (a,b), and set

```math
q(t)=\frac{(t-r_1)(t-r_2)}{(t-h_1)(t-h_2)},\qquad \Phi=vq.
```

Assume the two zero/pole pairs overlap: the order is one of

```math
r_1<h_1<r_2<h_2,\quad h_1<r_1<h_2<r_2,\quad
h_1<r_1<r_2<h_2,\quad r_1<h_1<h_2<r_2.
\tag{1}
```

If Phi has at most five distinct critical points on (a,b) away from its
poles, then every positive level has at most six distinct contacts on
the entire positive locus {q>0}. Hence the same is true on any subset.
Critical auxiliary ratio levels and multiple critical roots are allowed.

## Residue-cone geometry

For the first three orders in (1), the uniform residue-cone lemma in
UNIFORM_RESIDUE_CONE_HEIGHT_LEMMA.md gives the following dichotomy.
A level meeting the distinguished positive dome has at most four
contacts. A level missing that dome occupies at most two positive
components. The dome tends to zero at both endpoints and has at least
one critical point, which is unavailable in the occupied components.
Thus Rolle gives at most four remaining critical points plus two
components, or six contacts. This is one exact tangent identity and
one log-concavity argument; no orientation of external roots or gap
parameters is part of this abstract step.

## Complementary cross-component concavity

Consider the fourth order r1<h1<h2<r2. The positive components are

```math
(a,r_1),\quad (h_1,h_2),\quad (r_2,b).
```

Suppose x in the left component and z in the right component are contacts
of the same positive level c. We prove that every y in the middle
component has Phi(y)>c. Consequently c cannot occupy all three
components. Each outer positive component has endpoint limits zero
and zero, while the middle component has endpoint limits positive
infinity and positive infinity. Each therefore has a critical point.
An unoccupied component consumes at least one of the five available
critical points. Rolle on the remaining at most two occupied components
gives at most four plus two, or six contacts.

Fix x<y<z and set theta=(y-x)/(z-x). Affinely normalize the three
points to 0,theta,1. The four roots/poles become numbers s in (0,1),
with r1<h1<theta<h2<r2. Define

```math
F_\theta(s)=\log|\theta-s|
 -(1-\theta)\log s-\theta\log(1-s).
```

Direct differentiation gives

```math
F_\theta'(s)=
\frac{\theta(1-\theta)}{s(1-s)(s-\theta)}.
\tag{2}
```

Thus F_theta is strictly decreasing left of theta and strictly
increasing right of theta. The root/pole order gives

```math
F_\theta(r_1)>F_\theta(h_1),\qquad
F_\theta(r_2)>F_\theta(h_2).
```

Adding these inequalities proves the exact three-component relation

```math
\log q(y)>(1-\theta)\log q(x)+\theta\log q(z).
\tag{3}
```

The affine length factors cancel because q has the same number of
numerator and denominator factors. All three q values are positive,
so the logarithms are legitimate. Add the concavity chord inequality
for log v. Since Phi(x)=Phi(z)=c, the result is log Phi(y)>log c.
This proves the asserted exclusion without comparing derivatives across
a pole and without a physical mode-side distinction.

The identity (2) and the fourth-order proof were independently supplied
by the earlier proof algebra lane. The fork lane verified their deduction
and integrated them with its residue-cone lemma.

## Proof status

This is a complete abstract theorem. Its INC application uses the
separately actual-source exterior-factor log-concavity theorem
on overlapping negative R,K bands. That lemma is stronger than an
arbitrary cubic factorization and retains the original support parameters.
The six-contact strengthening and both geometric arguments have also
received an independent analytical hand review.
