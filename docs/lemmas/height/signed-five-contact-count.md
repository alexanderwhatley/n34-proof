# A five-node signed height theorem without the leading-sign dispatch

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

This earlier assembly is now superseded by the complete
[rightmost small gap master height theorem](later-mode-small-gap-height.md). Its global Qv-one
standing assumption is no longer needed: the new physical derivative
core auxiliary ratio lemma supplies precisely the original-interval signs
used here. The component count and exact residue identities remain
valid under that weaker replacement.

## Statement

Retain the exactly realized source

```math
u=v^h q^{-m},\quad H=1-h,\quad 0<h<1,\quad0<m<H,
\quad m/h<r_1<r_2<r_3,\quad \Lambda>0,
```

and the linked $`C,E,D,A,B,V`$ of the original proof. Suppose C has
simple roots

```math
-1<\gamma_1<\gamma_2<0<r_3<\gamma_3,
```

the negative E root obeys $`\epsilon_-<\gamma_1`$, and
$`Q_v=mC-pE=-A`$ has exactly one simple real root. Work away from
internal algebraic coincidences and $`c_1=M=H u(x_q)`$, as in the
original generic reduction.

Consider one regular positive height $`c_1`$ with

```math
c_1<V(y)
```

at some positive central point $`\gamma_1<p(y)<\gamma_2`$.
Require at every V=c1 crossing the original positive coefficient inequalities:

| Branch and C sign | Downward V crossing requires | Upward V crossing requires |
|---|---|---|
| Left, C>0 | A/C>0 | B/C>0 |
| Left, C<0 | B/C>0 | A/C>0 |
| Right, C>0 | B/C>0 | A/C>0 |
| Right, C<0 | A/C>0 | B/C>0 |

**Theorem.** There are at most five such common-height nodes in the whole
original interval. No sign split on $`\ell=Hh-m\Lambda`$ is needed.
If $`E(\gamma_3)>0`$, the inequalities are already inconsistent on a single
forced positive component.

## Proof when the third D root is before the third C root

Suppose $`E(\gamma_3)<0`$. The actual central positive point forces
two central D roots $`\delta_1<\delta_2`$. Since $`D(r_3)>0`$
and $`D(\gamma_3)=E(\gamma_3)<0`$, the third root satisfies
$`r_3<\delta_3<\gamma_3`$. These exhaust the cubic D.
The positive components of V, in original x order, are:

1. The initial component $`(0,x(\delta_3))`$, with zero endpoint values.
2. The main component from $`x(\gamma_3)`$ through $`x_q`$ to
   $`x(\gamma_1)`$, with infinite endpoint values.
3. The positive central component $`(x(\delta_1),x(\delta_2))`$,
   with zero endpoint values.
4. The final tail $`(x(\gamma_2),1)`$, from infinity to zero.

At $`r_i`$, at $`\gamma_1`$, and at $`\gamma_2`$, Qv is
strictly positive. It is also positive at $`\gamma_3`$, because
$`Q_v(\gamma_3)=-\gamma_3E(\gamma_3)>0`$. A cubic with exactly
one simple real root cannot change sign between two such points of the
same sign. Thus Qv>0 between $`r_3`$ and $`\gamma_3`$, throughout
the central interval, and on the final right tail.

On the initial positive component, C>0 and A=-Qv<0. Any regular
positive level there has a downward crossing, which would require
A/C>0. Hence the initial component contributes no nodes. On the final
tail, C>0,A<0, so upward crossings are forbidden. Its endpoint values
then give exactly one downward node.

The original central orientation theorem (s132) makes every
stationary point of the central positive component a strict maximum.
Since the height lies below a positive central value, there are exactly
two central nodes.

### At most one left-main node, with no leading-sign split

The residues satisfy $`d_1<0<d_2,d_3`$ in
$`E/C=\sum_i d_i/(p-\gamma_i)`$. Put $`a_3=B/C`$. The exact
source identities are

```math
(a_3)_p=\sum_i\frac{d_i(\gamma_i+1)}{(p-\gamma_i)^2},
```

```math
\sum_i d_i(\gamma_i+1)
=\frac H\Lambda\{h(r_1+r_2+r_3+1+1/\Lambda)-2m\}>0.
\tag{1}
```

For $`p>\gamma_3`$, the negative contribution has the largest
denominator. Replacing the positive denominators by that denominator
strictly lowers the sum. Equation (1) therefore proves
$`(a_3)_p>0`$ on the entire left-main branch.

If two left-main nodes existed, the first crossing would be downward,
because V starts at infinity, and the second would be upward. The first
node supplies B/C>0, which propagates to the second. The upward node
supplies A/C>0, equivalently Qv>0 since C<0. Qv is positive at
$`\gamma_3`$ and has only one real root, so it is positive throughout
the interval from $`\gamma_3`$ to that second node. Thus A/C, B/C
and D/C are all positive between the first two nodes.

The original left positive-contact exclusion [left-contact monotonicity](left-contact-monotonicity.md) says that
V has no stationary point there. But a downward crossing followed by
an upward crossing forces a local minimum. Contradiction. Hence the
left main contributes at most one node. This proof never names the
leading coefficient of Qv or chooses its sign.

### At most one right-main node

The signed metric theorem
[signed source height metric master theorem](signed-height-comparison.md)
places every finite stationary value on $`p<\gamma_1`$ above every
positive central value, hence strictly above $`V(y)>c_1`$. The right
main ends at infinity. Two or more regular level hits there would force
a local minimum below $`c_1`$, contradicting this comparison. Its
initial value is $`M`$: it has no hits if $`M>c_1`$, and at most
one if $`M<c_1`$. Thus the whole main component contributes at most
two nodes.

Adding the bounds gives

```math
0+2+2+1=5.
```

## The forbidden-component alternative

If $`E(\gamma_3)>0`$, the two central D roots still exist, and the
third root obeys $`\delta_3>\gamma_3`$. The unique Qv root lies
between $`r_3`$ and $`\gamma_3`$, because its signs there are
positive and negative. Hence Qv is negative after that root and positive
before it.

On the positive component from $`x(\delta_3)`$ through the seam
to $`x(\gamma_1)`$, A/C is strictly negative on both physical
branches. Its endpoint values are zero and infinity. A regular positive
level must have an upward crossing, and every upward crossing on this
component is an L4 maximum requiring A/C>0. This is impossible. No
leading-coefficient split is needed for this alternative either.

The generic statement is proved. Internal equalities are treated by the
standing one-original-row regularization retaining root brackets; the
theorem is intended as a replacement input for the existing final
assembly, not as a multiplicity theorem for independently varied V nodes.
