# Identity exception for a weak least-support height theorem

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

the earlier proof fork lane, 2 October 2026. This elementary result is complete
and independent of any root-counting theorem.

Let u=t^A(1-t)^B, v=t^C(1-t)^D, w=t^E(1-t)^F, with all exponents
nonnegative and (A,B) componentwise no larger than (C,D),(E,F).
Let c1,c3,c4>0. Then

```math
c_1-u+c_3v+c_4w\equiv0
```

holds exactly in the following two situations:

1. All three support vectors are (0,0), and c1+c3+c4=1.
2. u=1, and after exchanging v,w,


```math
v=t,\qquad w=1-t,\qquad c_3=c_4=1-c_1\in(0,1).
```

## Proof

If A>0, then all three monomials tend to zero at t=0, so the alleged
identity tends to c1>0, a contradiction. Similarly B>0 is impossible
by t=1. Hence u=1. We need

```math
c_3v+c_4w=k:=1-c_1\gt0.
```

If either v or w is constant, positivity forces the other to be
constant too, giving the first situation. Otherwise, the positive
constant limit at t=0 requires one of v,w to have first exponent zero;
the positive limit at t=1 requires one to have second exponent zero.
These cannot be the same nonconstant monomial. After exchanging labels,
v=t^a and w=(1-t)^b, with a,b>0. The endpoint limits give c3=c4=k,
and the identity becomes

```math
t^a+(1-t)^b=1.
```

Its derivative gives a t^(a-1)=b(1-t)^(b-1). The logarithmic derivative
is (a-1)/t=-(b-1)/(1-t) throughout (0,1), which forces a=b=1.
Conversely both listed configurations visibly give the identity.

## Boundary-transfer caution

The finite-nine-sample height inequality transfers to weak least
supports without an endpoint-continuity argument. Its associated
at-most-eight distinct-root statement must exclude both identities
above. The second configuration is absent in a coordinatewise chain,
but is present in the weak incomparable boundary. Reusing only the
comparable theorem's all-zero identity exception would be incorrect.
