# One common exterior witness for the actual mixed source

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

This theorem replaces the explicit A/B degree-cell dispatch in the actual
source geometry.  It proves the exact reciprocal coefficient interface
needed by the all-positive-exponent Hurwitz theorem.  It does not use the
old negative-d3 exclusion, one-G exclusion, exterior-pair order, or a
connectedness argument.  The proof has one forbidden witness order, not a
classification of the surviving support cells.

## 1. Literal theorem

Let

```math
a_1=-U<0<a_2<a_3,\qquad b_3<0<b_1=v<b_2,
\quad U,v>0,\quad d_i=a_i+b_i,
```

and define the actual `P1,P3,G,K6` by

```math
\lambda_i=a_i-d_i x,\quad w=x(1-x),\quad
\mathcal D=w\frac d{dx},\quad
L_{21}=\lambda_2-\lambda_1,\quad L_{32}=\lambda_3-\lambda_2,
```

**(1)**

```math
\begin{aligned}
P_1&=(\mathcal D\lambda_2)L_{21}
 -\lambda_2(\lambda_1L_{21}+\mathcal DL_{21}),\\
P_3&=\lambda_2(\lambda_3L_{32}+\mathcal DL_{32})
 -(\mathcal D\lambda_2)L_{32},\\
G&=(\lambda_3-\lambda_1)L_{21}L_{32}
 +(\mathcal DL_{32})L_{21}-(\mathcal DL_{21})L_{32},\\
w(P_1'P_3-P_1P_3')-(\lambda_3-\lambda_1)P_1P_3
 &=\lambda_2K_6,\qquad \deg K_6\le6.
\end{aligned}
```

The quotient in (1) is an actual polynomial identity.  Suppose `K6`
has six roots in `(0,1)`, **counted with multiplicity**.

Put `z=(1-x)/x` and homogenize

```math
A(z)=(1+z)^3P_1\left(\frac1{1+z}\right),\quad
P(z)=(1+z)^3P_3\left(\frac1{1+z}\right),\quad
H(z)=(1+z)^3G\left(\frac1{1+z}\right).
```

Then there exists **one common point `z*<0` with `P(z*)>0` and
`H(z*)>0`**.  Both reciprocal cubics consequently have two distinct
negative roots and one positive root, all simple.  Neither has a root at
`z=-1`.  Their zero-deleted coefficient words in constant-to-leading order
therefore have one transition, from negative to positive.

## 2. The actual reciprocal identities

Use the positive source differences

```math
A_0=a_2-a_1>0,\quad B_0=b_2-b_1>0,\quad
\Delta=a_3-a_2>0,\quad F=b_2-b_3>0,
```

and the reciprocal score linears

```math
\ell_i=a_i z-b_i,\qquad
J=A_0z-B_0,\qquad L=\Delta z+F.
```

To avoid confusing the cubic `A` with the source difference, `A0` denotes
the latter throughout.  Direct homogenization of (1) gives

**(2)**

```math
\begin{aligned}
A&=-d_2zJ-\ell_2\{\ell_1J-(d_2-d_1)z\},\\
P&=\ell_2\{\ell_3L-(d_3-d_2)z\}+d_2zL,\\
H&=(\ell_3-\ell_1)JL+(A_0F+B_0\Delta)z(1+z),\\
LA+JP&=\ell_2H.
\end{aligned}
```

Let `T(z)=(1+z)^6 K6(1/(1+z))`.  The transformed critical identity is

**(3)**

```math
-z(1+z)(A'P-AP')-(\ell_3-\ell_1)AP=\ell_2T.
```

The actual polynomial has

```math
K_6(0)=a_1a_2a_3(a_3-a_2)(a_3-a_1)(a_2-a_1)<0.
```

Thus `T` has degree six, negative leading coefficient, and its six roots
are positive, counted with multiplicity.  In particular

**(4)**

```math
T(z)<0\qquad(z\le0).
```

The exact evaluations at the seam `z=-1` are

**(5)**

```math
\begin{aligned}
A(-1)&=d_1d_2(d_2-d_1),\\
P(-1)&=-d_2d_3(d_3-d_2),\\
H(-1)&=-(d_3-d_1)(d_2-d_1)(d_3-d_2),\\
T(-1)&=d_1d_2d_3(d_2-d_1)(d_3-d_1)(d_3-d_2)<0.
\end{aligned}
```

All factors in the last line are nonzero.  Thus none of the three cubics
has a root at `-1`, and `Delta != F`.  Also the actual supports directly
give `d1<d2`, since `d1=v-U<v<b2<d2`.

The reciprocal `A` has positive constant and positive leading coefficient:

```math
A(0)=b_1b_2(b_2-b_1)>0,\qquad
[z^3]A=-a_1a_2(a_2-a_1)>0.
```

At `z_c=b2/a2>0`, the formula (2) gives `A(z_c)<0`.  Hence it has
one simple positive root on each side of `z_c`.  Its remaining root
`E` is real, simple, and negative: a third positive root would contradict
the positive constant and positive leading coefficient.  Therefore
`A'(E)>0`.  Equation (5) excludes `E=-1`.

Evaluate (3) at `E`.  Since `ell2(E)<0`, `T(E)<0`, and `-E>0`,

```math
-E(1+E)A'(E)P(E)=\ell_2(E)T(E)>0.
```

Consequently

```math
\operatorname{sgn}P(E)=\operatorname{sgn}(1+E).
```

At `E`, the Pluecker identity in (2) becomes `JP=ell2 H`.
Both `J(E)` and `ell2(E)` are negative, so

**(6)**

```math
\boxed{\operatorname{sgn}P(E)=\operatorname{sgn}H(E)
       =\operatorname{sgn}(1+E).}
```

The second fixed point is `L0=-F/Delta<0`, the zero of the reciprocal
linear `L`.  Exact substitution in (2) gives the two uniform product
identities

**(7)**

```math
\begin{aligned}
\Delta^2 P(L_0)&=-(\Delta-F)F(a_2F+b_2\Delta),\\
\Delta^2 H(L_0)&=-(\Delta-F)F(A_0F+B_0\Delta).
\end{aligned}
```

Their nonzero bracket factors are positive.  Since
`1+L0=(Delta-F)/Delta`,

**(8)**

```math
\boxed{\operatorname{sgn}P(L_0)=\operatorname{sgn}H(L_0)
       =-\operatorname{sgn}(1+L_0).}
```

```math
E<-1<L_0.
```

Since the other `A` roots are positive, this order gives `A(-1)>0`.
Equation (5) and `d2>d1` then imply `d1>0`.  Also `L0>-1` means
`Delta>F`, hence `d3>d2>d1>0`.  Every factor in `T(-1)` in (5) would
then be positive, contradicting (4).  Thus at least one of `E,L0` is a
common positive witness.  No surviving degree cell has been classified.

## 4. The root and coefficient interface follows immediately

For each of `P,H`, the constant term is negative and the leading
coefficient positive:

```math
\begin{aligned}
P(0)&=b_2b_3(b_2-b_3)<0,&[z^3]P&=a_2a_3\Delta>0,\\
H(0)&=(b_1-b_2)(b_2-b_3)(b_1-b_3)<0,
&[z^3]H&=(a_3-a_1)(a_2-a_1)\Delta>0.
\end{aligned}
```

Each is negative near negative infinity, positive at `z*`, negative at
zero, and positive near positive infinity.  The three disjoint intervals

```math
(-\infty,z_{*}),\qquad(z_{*},0),\qquad(0,\infty)
```

therefore contain one root apiece.  A cubic has room for precisely those
three distinct simple roots.  Equation (5) excludes roots at `-1`, so the
two negative roots correspond to finite real exterior roots of the actual
source cubics.  This argument also proves physical G simplicity and
eliminates a three-physical-G possibility without a separate theorem.

Finally, a positive-leading cubic with roots `-s,-t,r`, all three positive
in magnitude, has coefficients proportional to

```math
(-rst,\;st-r(s+t),\;s+t-r,\;1).
```

If its quadratic coefficient is nonpositive, `r>=s+t`, and its linear
coefficient is strictly negative.  If its linear coefficient is
nonnegative, `r<=st/(s+t)<s+t`, and its quadratic coefficient is strictly
positive.  Thus the middle signs cannot reverse from positive to negative.
Deleting any coefficient zeros leaves one negative block followed by one
positive block.  This is precisely the source interface consumed by the
all-positive-exponent Hurwitz theorem.

## 5. Scope and proof replacement

The preferred master proof can therefore replace the full A/B atlas by
this common-positive-witness theorem.  It retains the exact cubic source
identities, weighted saturation, the all-positive-exponent Hurwitz flag,
and exact reflection.  It no longer needs a negative-d3 exclusion,
surviving degree-cell table, exterior-root side counts, or labeled pair
orders.  There is no claimed change to the raw seven-root `R` examples.
