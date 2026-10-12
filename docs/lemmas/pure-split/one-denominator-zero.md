# Exactly one projective denominator root in the actual mixed source

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Use the actual strict canonical mixed supports

```math
a_1\lt0\lt a_2\lt a_3,\qquad b_3\lt0\lt b_1\lt b_2,
```

with lambda_i=a_i-(a_i+b_i)x, h_i=x^{a_i}(1-x)^{b_i},
J=lambda2-lambda1 and L=lambda3-lambda2. For every rho>0 let

```math
B=h_1J-\rho h_3L.
```

**Lemma.** B has exactly one simple physical zero, lying before the
unique physical zero ell of J. No genericity assumption, event topology
or EHT bound is needed for this statement.

Indeed,

```math
J=(a_2-a_1)(1-x)+(b_1-b_2)x,
\qquad
L=(a_3-a_2)(1-x)+(b_2-b_3)x\gt0.
```

Thus J is positive before ell in (0,1) and nonpositive after it. On
(0,ell),

```math
\left(\frac{J}{L}\right)'
=\frac{(b_1-b_2)(a_3-a_2)-(a_2-a_1)(b_2-b_3)}{L^2}\lt0.
```

Also lambda1<0<lambda3 everywhere physically, so

```math
\left(\log\frac{h_1}{h_3}\right)'
=\frac{\lambda_1-\lambda_3}{x(1-x)}\lt0.
```

Consequently the positive function

```math
T=\frac{h_1}{h_3}\frac{J}{L}
```

has strictly negative derivative on (0,ell), tends to infinity at zero,
and tends to zero at ell. It hits the fixed rho exactly once, with
nonzero derivative. Since B=h3 L(T-rho), that hit is a simple B zero.
For x>=ell, h1 J<=0 and -rho h3 L<0, so there are no other zeros.

Exact source reflection proves the corresponding denominator statement
in the opposite mixed cone with its actual reflected dictionary.

On the generic b!=c chart the useful auxiliary ratio set {lambda2 B>0} has
exactly two components. The physical source has no three-B-pole phase.
Thus the linear/linear EHT bound used to limit B in the general pure-split
entry can be replaced by this elementary monotonicity argument in the
mixed branch. The joint-height theorem was deliberately written
to work with the old phase-free entry and does not require this stronger
input.
