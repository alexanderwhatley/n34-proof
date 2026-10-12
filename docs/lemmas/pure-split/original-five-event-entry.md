# A phase-independent eight-root bridge for every mixed event order

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## 1. Result

Work in the strict mixed score quadrant

```math
C=b_1-b_2\lt0\lt\Delta=a_3-a_2
```

and retain

**(1)**

```math
R=h_1P_1+\rho h_3P_3,\qquad
 Y={P_3\over h_1G},\qquad
 S_\kappa=P_3-\kappa h_1G.
```

The six possible strict physical event orders are

**(2)**

```math
113,\quad131,\quad11333,\quad13133,\quad
 13313,\quad13331.
```

> **Universal eight-root bridge.**  If a hypothetical nine-hit auxiliary ratio
> equality has seven transverse roots of `R` in any word in (2), then its
> common positive critical level `kappa` forces at least eight distinct
> physical roots of `S_kappa`.  The conclusion is independent of the sign
> of `B(c)` and of the one-/three-projective-pole phase.

This strengthens the formerly recorded phase-independent seven-root bridge.
For word `131`, the additional forced interval is the gap from its physical
`P3` event to the first selected root in the terminal component.  The same
event-sign calculation works uniformly in all six words.

Reflection gives the identical theorem in `Delta<0<C` for

**(3)**

```math
133,\quad313,\quad11133,\quad13113,\quad
 11313,\quad31113.
```

## 2. Signs at selected roots

Let the seven roots of `R` be

```math
r_1\lt\cdots\lt r_7.
```

At such a root, the Pluecker identity gives `X(r_i)=Y(r_i)`.  The
hypothetical auxiliary ratio window has

**(4)**

```math
X(r_i)\gt\kappa\quad(i\text{ odd and useful}),
 \qquad 0\lt X(r_i)\lt\kappa\quad(i\text{ even}).
```

The unique possible non-useful root in the three-pole equality phase is
odd and has `X(r_i)<0`.  Thus `1-kappa/X(r_i)>0` there as well.  Consequently

**(5)**

```math
\boxed{\mathop{\mathrm{sgn}}\nolimits S_\kappa(r_i)
 =\mathop{\mathrm{sgn}}\nolimits P_3(r_i)(-1)^{i+1}.}
```

All signs in (5) are strict.

## 3. Signs at the `P3` events and endpoints

Every physical `P3` event lies to the right of

```math
c={a_2\over a_2+b_2}.
```

In this quadrant `L32>0` throughout the physical interval, while
`lambda2<0` to the right of `c`.  At a strict `P3` event `p`,

```math
L_{32}(p)P_1(p)=\lambda _2(p)G(p).
```

Hence `sgn G(p)=-sgn P1(p)` and therefore

**(6)**

```math
\boxed{\mathop{\mathrm{sgn}}\nolimits S_\kappa(p)
 =\mathop{\mathrm{sgn}}\nolimits P_1(p).}
```

The endpoint signs are also fixed.  Since `a1<0`, `h1(0+)=infinity`, and

```math
G(0)=(a_2-a_1)\Delta\{(a_2-a_1)+\Delta\}\gt0,
```

one has

```math
S_\kappa(0+)\lt0.
```

Since `b1>0`, `h1(1-)=0`, whereas `P3(1)<0`, so

**(7)**

```math
\boxed{S_\kappa(0+)\lt0,\qquad S_\kappa(1-)\lt0.}
```

No sign in (6)--(7) uses `B(c)`.

## 4. The finite sign count

Write `A_n^sigma` for a length-`n` alternating sign block beginning with
the sign `sigma`; omit the block when `n=0`.  An allocation lists the
numbers of `R` roots in the positive event components from left to right.
The event endpoint types force the parities in the second column below.
Equations (5)--(7) give the complete ordered nonzero sample trace in the
third column.  The isolated signs between alternating blocks are the signs
at successive physical `P3` events.

| word | allocation parity | ordered sign trace for `S_kappa` | variations |
|---|---|---|---:|
| `113` | `(even,odd)` | `- \| A_n^+ \| + \| A_m^- \| -` | 8 |
| `131` | `(odd,even)` | `- \| A_n^+ \| - \| A_m^+ \| -` | 8 |
| `11333` | `(even,even,odd)` | `- \| A_n^+ \| + \| A_m^- \| + \| + \| A_l^- \| -` | 8 |
| `13133` | `(odd,odd,odd)` | `- \| A_n^+ \| - \| A_m^+ \| + \| + \| A_l^- \| -` | 8 |
| `13313` | `(odd,odd,odd)` | `- \| A_n^+ \| - \| - \| A_m^- \| + \| A_l^- \| -` | 8 |
| `13331` | `(odd,even,even)` | `- \| A_n^+ \| - \| - \| A_m^- \| - \| A_l^+ \| -` | 8 |

Here the allocation entries sum to seven.  Direct zero-safe counting in
each row gives `7+1=8` variations, including every allowed zero component.
Successive samples occur in strict increasing physical order.  Each
variation therefore gives a root of `S_kappa` in a different open gap.
This proves the theorem on the transverse strict chart.

For the old word-`131` notation with allocation `(n,m)`, the trace contains

**(8)**

```math
S_\kappa(r_n)\gt0\gt S_\kappa(p),\qquad
 S_\kappa(p)\lt0\lt S_\kappa(r_{n+1}),
```

whenever `m>0`.  The second interval in (8) is the formerly omitted eighth
gap.  Its first terminal root has even global index, is necessarily useful,
and lies where `P3<0`, so its displayed positive sign is unconditional.

## 5. Reflection dictionary

Reflection followed by exchange of the outer labels sends a word to

**(9)**

```math
\mathcal R(w)=\mathop{\mathrm{swap}}\nolimits _{1\leftrightarrow3}
                 (\mathop{\mathrm{reverse}}\nolimits w),
```

and gives

**(10)**

```math
\begin{array}{cc}
113 & \leftrightarrow 133\\
11333 & \leftrightarrow 11133\\
131 & \leftrightarrow 313\\
13133 & \leftrightarrow 11313\\
13313 & \leftrightarrow 13113\\
13331 & \leftrightarrow 31113
\end{array}
```

It reverses the allocation and the sign of `B(c)`.  At an `R` root,

```math
Y_1=-{P_1\over h_3G}=\rho X.
```

Thus the reflected common-level equation is, up to a harmless overall
sign,

**(11)**

```math
-P_1-\kappa_1h_3G=0,\qquad \kappa_1=\rho\kappa,
```

and (9)--(10) carry the eight disjoint forced gaps to the reflected word.

## 6. Immediate Stieltjes propagation

Put

```math
U=-a_1\gt0,\qquad v=b_1\gt0,\qquad y={x\over1-x}.
```

Then

**(12)**

```math
h_1(y)=y^{-U}(1+y)^{U-v}.
```

If

**(13)**

```math
0\lt U\lt1,\qquad0\lt v\lt1,
```

this is a strict Stieltjes function with infinite-support positive measure.
After cubic homogenization, `S_kappa=0` has the form

```math
A_3+h_1B_3=0,\qquad \deg A_3,\deg B_3\le3.
```

The standard AT orthogonality argument forbids eight positive roots counted
with multiplicity; equivalently, the ceiling is seven.  The universal bridge
contradicts that ceiling.  Hence every word in (2), in both auxiliary ratio phases,
is closed at the no-nine-hit-equality scope throughout (13).

The reflected statement holds when

**(14)**

```math
0\lt-b_3\lt1,\qquad0\lt a_3\lt1,
```

using reciprocal odds and `h3`.

## 7. Propagation boundary

The bridge itself is stable under inserting an adjacent pair of type-`3`
events: the four five-event orders are obtained from `113` or `131` by such
an insertion, and the table still forces exactly eight common-level roots.
Thus any support-global theorem

**(15)**

```math
Z(P_3-\kappa h_1G)\le7\qquad(\kappa\gt0)
```

automatically deletes every mixed word, not just the base word used to
discover it.

What does **not** propagate formally is a ceiling whose proof assumes that
`P3` has only one physical root, or a word-specific exterior interlacing of
`P3` and `G`.  At the bridge-only stage, a natural remaining analytic target
was therefore a common-support version of (15) outside the Stieltjes box
(13), or a deflation theorem that removes the inserted `33` block while
preserving a seven-root ceiling.  The companion saturation and all-exponent
theorems close the mixed atlas by word-specific mechanisms; no such global
extension is asserted by this note.
