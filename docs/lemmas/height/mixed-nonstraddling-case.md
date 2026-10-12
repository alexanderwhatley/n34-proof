# The mixed one-root original row only needs a new argument in the straddling cell

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

the earlier proof, 2026-10-02. Analytical positive-coefficient original-row theorem.

Let $`A,B,a,b,c,\nu>0`$, $`B>\nu,c>a`$, and

```math
f=1-E_0t^{-A}(1-t)^{-B}
-E_1t^a(1-t)^b-E_2t^c(1-t)^{-\nu},\qquad E_i>0.
```

Use the actual mixed cofactors $`R,H,K=H-R`$, and
$`V=\ell_2P_0-\ell_0P_2`$. Suppose $`R`$ has exactly one physical root
$`r`$, and

```math
\boxed{V(r)>0.}
\tag{1}
```

Then the original $`f`$ has at most eight distinct roots. Equivalently,
the condition is $`K(r)>0`$, or $`H(r)>0`$, because the exact cofactor
syzygy at $`R(r)=0`$ gives

```math
L(r)V(r)=\ell_2(r)K(r),\qquad L,\ell_2>0.
\tag{2}
```

Thus the negative $`V`$-band and the negative $`K`$-band do not straddle
the sole $`R`$-root. Both a band before $`r`$ and a band after $`r`$ are
covered. The result uses all three positive coefficients of the original
row, and does not claim a global seven-contact bound for $`\Phi`$.

The mode-aligned theorem already covers $`m_0\ge m_1`$, where
$`m_0=A/(A+B)`$, $`m_1=a/(a+b)`$; it also proves $`V(r)>0`$ there.
It remains to prove the result for $`m_0<m_1`$.

## The two positive derivative components

Normalize by the monotone atom exactly as in the theorem:

```math
u=-h_0'/h_2',\quad v=-h_1'/h_2',\quad U=E_0u+E_1v,
\quad f'=0\Longleftrightarrow U=E_2>0.
```

On $`(0,m_0)`$, $`u>0,v<0`$, and

```math
k_-=\frac{|v|}{u}=\frac{h_1}{h_0}\frac{\ell_1}{-\ell_0}
```

is strictly increasing, since

```math
(\log k_-)'=
\frac{\ell_1-\ell_0}{t(1-t)}
+\frac1{m_0-t}-\frac1{m_1-t}>0.
```

It increases from zero to infinity. The inverse-mode inequality gives $`u'<0`$
there, so $`U=u(E_0-E_1k_-)`$ strictly decreases wherever positive.
Its positive initial component therefore has exactly one contact of
each positive level.

On $`(m_0,m_1)`$, both $`u,v`$ are negative, so $`U<0`$.
On $`(m_1,1)`$, $`u<0,v>0`$, and

```math
k_+=\frac{|u|}{v}=\frac{h_0}{h_1}\frac{\ell_0}{-\ell_1}
```

has

```math
(\log k_+)''=
\frac{A+a}{t^2}+\frac{B+b}{(1-t)^2}
-\frac1{(t-m_0)^2}+\frac1{(t-m_1)^2}>0.
\tag{3}
```

It tends to infinity at both endpoints. Hence it has one strict minimum
at a point $`d\in(m_1,1)`$. The late positive set of
$`U=v(E_1-E_0k_+)`$ is empty or a single bounded interval containing $`d`$,
with zero $`U`$-limits at both ends.

## Positive critical points are before the sole R root

The pair hypothesis makes $`v`$ strictly increase to $`r`$ and decrease
after $`r`$. At $`r`$, $`v'(r)=0`$ and $`u=-v k_+`$, so
$`u'(r)=-v(r)k_+'(r)`$. The source derivative identity
$`u'=-(h_0/h_2)V/[t(1-t)\ell_2^2]`$ proves

```math
\operatorname{sign}V(r)=\operatorname{sign}k_+'(r).
```

Thus (1) means $`d<r`$. Before $`d`$, both positive factors $`v`$ and
$`E_1-E_0k_+`$ increase, whenever their product is positive.
After $`r`$, both decrease. Therefore every positive critical point of
the late $`U`$-component lies in $`(d,r)`$.

Such critical points are contacts of one positive level

```math
\Psi=\frac{h_1R}{h_0V}=E_0/E_1,
```

and lie before $`r`$, where $`R>0`$. The nonzero critical polynomial
of $`\Psi`$ has degree at most six, because its raw numerator is
$`-\ell_2 W`$ with $`W=\det[\ell;P;Q]`$.

If $`V`$ has no physical roots, the negative final $`\Psi`$-tail consumes
one critical point; the single positive component before $`r`$ has at
most six fixed-level contacts. If the negative $`V`$-band is after $`r`$,
the positive pole-pole $`\Psi`$-bowl consumes one critical point outside
the first positive component $`(0,r)`$, again giving at most six contacts
before $`r`$. If the negative $`V`$-band is before $`r`$, the negative
pole-pole component and the negative final tail consume two critical
points, giving at most $`(6-2)+2=6`$ full positive contacts.
The straddling case is excluded by (1).

Thus the late positive $`U`$-component has at most six critical points.
Its regular positive levels have at most seven contacts by Rolle, and
an even number because its endpoint limits are zero. They therefore have
at most six contacts. Adding the single initial contact gives at most
seven roots of the original derivative and at most eight roots of $`f`$.

The coefficient regularization is exactly the positive-row
argument: regular positive $`E_2`$-levels are dense, and hypothetical
original sign brackets persist under a small positive $`E_2`$
perturbation. Finite nonidentity original-row limits from this strict
cell inherit the bound by compact regularization and nearby generic
sources; nearby three-$`R`$-root sources use the universal
three-root theorem.

## Precise remaining strict one-root cell

After this theorem and the mode-aligned theorem, only the cell

```math
m_0<m_1,\qquad V(r)<0\quad\Longleftrightarrow\quad K(r)<0
```

requires a new argument. Its negative $`V`$-band straddles $`r`$, and
$`r<d`$. All positive critical points of $`U`$ are then confined to
$`(r,d)`$, within the second positive $`\Psi`$-component. The first
positive $`U`$-component remains strictly decreasing. Proving at most
six contacts of the one fixed level $`\Psi=E_0/E_1`$ on $`(r,d)`$
would close this last cell. This note makes no such additional claim.
