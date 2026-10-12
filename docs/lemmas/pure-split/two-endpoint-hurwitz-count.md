# One dual-endpoint Hurwitz ceiling; no height comparison

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## 1. Literal theorem

Let `P,G` be real cubics. Suppose each has one root in `(0,1)` and two real
roots outside `[0,1]`, and

```math
P(0),G(0)>0,\qquad P(1),G(1)<0.
```

Exterior repeated roots and cross-polynomial coincidences are permitted.
For every

```math
U>0,\quad v>0,\quad \min(U,v)<1,\quad\kappa>0,
```

the function

```math
S_\kappa(x)=P(x)-\kappa h(x)G(x),
\qquad h(x)=x^{-U}(1-x)^v,
\tag{1}
```

has at most **six roots in `(0,1)`**, counted with multiplicity and hence
also as distinct roots. Integer values of the other endpoint exponent are
included by the literal strict fractional flag.

If `v<1`, this is exactly the root-factor theorem: only the G
exterior geometry is needed in that subregion. If `U<1`, only the P
exterior geometry is needed. The symmetric statement above supplies both.

## 2. Exact profile duality

Put

```math
y=1-x,\qquad
P^\vee(y)=-G(1-y),\qquad G^\vee(y)=-P(1-y),
```

```math
U^\vee=v,\quad v^\vee=U,\quad
\kappa^\vee=\frac1\kappa,\quad
h^\vee(y)=y^{-v}(1-y)^U=\frac1{h(1-y)}.
\tag{2}
```

Then, literally,

```math
\boxed{
P^\vee(y)-\kappa^\vee h^\vee(y)G^\vee(y)
=\frac{S_\kappa(1-y)}{\kappa h(1-y)}.}
\tag{3}
```

The endpoint signs remain in the orientation:

```math
P^\vee(0)=-G(1)>0,\quad P^\vee(1)=-G(0)<0,
```

```math
G^\vee(0)=-P(1)>0,\quad G^\vee(1)=-P(0)<0.
\tag{4}
```

The affine root map `r->1-r` takes a physical root to a physical root and
an exterior root to an exterior root, swapping the two exterior rays. It
preserves multiplicity. The divisor on the right of (3) is strictly
positive and real analytic on `(0,1)`, so division also preserves every
root and its multiplicity. When `U<1`, the transformed parameter
`v^vee=U` lies in the low-v interval, while `U^vee=v>0` is
arbitrary. Applying the theorem to (3) proves the conclusion.

There is no need to reprove a second Stieltjes density, exchange Hurwitz
columns, or compare the heights of two components. This is an exact
application of the same theorem to a different polynomial pair.

## 3. The missing high-v route needs no Theta theorem

The actual one-G root geometry supplies the real
exterior cofactors of **both** `P3` and `G`. The retained Cauchy-square
count module eliminates every such saturated chart with `U>=1,v>=1`.
Consequently every surviving chart has `min(U,v)<1` and is excluded by
the theorem above plus the phase-independent eight-root bridge.

In particular, the former high-v cell B (`v>=1,0<U<1`) is sent to the
low-v theorem by (2). It no longer needs the cross-gap Theta
height inequality, exterior-count matching to `3+3`, or an allocation
table. The Cauchy module is still necessary to exclude the both-at-least-one
region; this addendum does not assert a six-root theorem there.

The actual `313` reflection is a separate step: it changes the support
dictionary by `x->1-x` and exchange of outer labels1 and3, taking its
common-level equation to `-P1-kappa1 h3 G=0`, where `kappa1=rho kappa`.
That source reflection and the profile duality (2) must not be identified.

No raw ceiling for `R=h1 P1+rho h3 P3`, no assertion for complex exterior
cofactors, and no new claim about boundaries of the strict saturated
actual chart is made. The alternative height theorem remains a
valid backup proof, although it is not an input to this preferred route.
