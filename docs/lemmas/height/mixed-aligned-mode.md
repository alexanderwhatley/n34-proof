# A positive-level argument closes the mode-aligned mixed one-root region

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Let $`A,B,a,b,c,\nu>0`$, $`B>\nu`$, $`c>a`$, and consider

```math
f=1-E_0h_0-E_1h_1-E_2h_2,\quad
h_0=t^{-A}(1-t)^{-B},\quad
h_1=t^a(1-t)^b,\quad h_2=t^c(1-t)^{-\nu},\quad E_i>0.
```

Suppose the pair cofactor $`R=\ell_1P_2-\ell_2P_1`$ has exactly one
physical root $`r`$, and

```math
\boxed{m_0=\frac A{A+B}\ge m_1=\frac a{a+b},}
\qquad\text{equivalently }Ab\ge aB.
\tag{1}
```

Then $`f`$ has at most eight distinct roots. This is uniform in all
positive coefficients and in every common dilation of an admitted
support shape, conditional only on the current pair remaining in its
one-root region. If a dilation enters the three-root region, the universal three-root theorem gives the same eight-root conclusion.

This theorem uses the positive third coefficient in the original row.
It does not claim a global seven-contact bound for the scalar auxiliary ratio
$`\Phi=t^A(1-t)^B R/H`$.

## Normalize the original derivative by the monotone atom

Since $`h_2'>0`$, put

```math
u=-h_0'/h_2',\qquad v=-h_1'/h_2',\qquad
U=E_0u+E_1v.
```

The original equation $`f'=0`$ is precisely $`U=E_2>0`$.
With $`\mathscr D=t(1-t)d/dt`$, define

```math
\ell_0=-A+(A+B)t,\quad
\ell_1=a-(a+b)t,\quad
\ell_2=c-(c-\nu)t>0,\quad
P_i=\ell_i^2+\mathscr D\ell_i,
```

```math
V=\ell_2P_0-\ell_0P_2,\qquad
\Psi=\frac{h_1R}{h_0V}.
```

The exact derivative identities are

```math
\mathscr Du=-\frac{h_0}{h_2}\frac V{\ell_2^2},\qquad
\mathscr Dv=\frac{h_1}{h_2}\frac R{\ell_2^2}.
\tag{2}
```

Hence every critical point of $`U`$ away from a simultaneous cofactor zero
is a contact of the same positive level $`\Psi=E_0/E_1`$.
The one-root hypothesis gives $`r>m_1`$, $`R>0`$ before $`r`$, and
$`R<0`$ afterwards. Thus $`v`$ strictly increases up to $`r`$ and
strictly decreases afterwards; $`v>0`$ after $`m_1`$.

## Positive U has at most two components

First assume $`m_0>m_1`$. Before $`m_1`$, $`u>0,v<0`$, and

```math
k_-=\frac{|v|}{u}
=\frac{h_1}{h_0}\frac{\ell_1}{-\ell_0}.
```

It tends to zero at both endpoints of $`(0,m_1)`$, and

```math
(\log k_-)''=
-\frac{A+a}{t^2}-\frac{B+b}{(1-t)^2}
-\frac1{(m_1-t)^2}+\frac1{(m_0-t)^2}<0.
\tag{3}
```

Its superlevel sets are intervals, so
$`U=u(E_0-E_1k_-)>0`$ has at most an initial and a final component
before $`m_1`$. The final one joins the strictly positive interval
$`(m_1,m_0)`$, where both $`u,v`$ are positive.

After $`m_0`$, $`u<0,v>0`$, and

```math
k_+=\frac{|u|}{v}
=\frac{h_0}{h_1}\frac{\ell_0}{-\ell_1}
```

is strictly increasing, because

```math
(\log k_+)'=
\frac{\ell_0-\ell_1}{t(1-t)}
+\frac1{t-m_0}-\frac1{t-m_1}>0.
\tag{4}
```

It increases from zero to infinity. Therefore the positive set of
$`U=v(E_1-E_0k_+)`$ after $`m_0`$ is a single initial interval,
which joins the preceding final positive component. Consequently
$`\{U>0\}`$ has at most two components on the full physical interval.

## No positive critical point of U is after r

The inverse-atom derivative ratio satisfies $`V>0`$ at and before $`m_0`$;
equivalently $`u'<0`$ there. A proof is included below.
If $`r<t<m_0`$, both $`u,v`$ are positive and strictly decreasing,
so $`U'<0`$. If $`t>\max(r,m_0)`$ and $`U>0`$, (4) gives

```math
U'=v'(E_1-E_0k_+)-E_0v k_+'<0,
\tag{5}
```

since $`v'<0`$ and the first bracket is positive.
Thus every critical point with $`U>0`$ is before $`r`$.

Moreover $`V(r)>0`$. If $`r\le m_0`$, this follows from the inverse
mode inequality. If $`r>m_0`$, then $`v'(r)=0`$ and
$`u'(r)=-(v k_+)'(r)=-v(r)k_+'(r)<0`$, so (2) gives $`V(r)>0`$.
The negative $`V`$-band therefore cannot straddle $`r`$.

## At most six positive critical points of U

The actual critical polynomial of $`\Psi`$ is the nonzero sextic

```math
W=\det[\ell;P;Q],\qquad Q_i=\ell_iP_i+\mathscr DP_i,
```

because its raw phase derivative numerator equals $`-\ell_2W`$.
The cubic $`V`$ has positive endpoint values
$`V(0)=Ac(A+c)`$, $`V(1)=B\nu(B-\nu)`$, so it has zero or two
physical roots on a strict generic source.

If $`V`$ has no physical roots, the negative $`\Psi`$-tail $`(r,1)`$
has zero limits at both ends, consuming one critical point.
The one positive component $`(0,r)`$ consequently has at most five
critical points and at most six contacts of any fixed positive level.

If the negative $`V`$-band is after $`r`$, the positive pole-pole
$`\Psi`$-component has limits $`+\infty`$ at both ends, consuming one
critical point outside $`(0,r)`$. Again, the first positive component
$`(0,r)`$ has at most six contacts. By (5), only its contacts can be
positive critical points of $`U`$.

If the negative $`V`$-band is before $`r`$, the negative pole-pole
$`\Psi`$-component and the negative final tail each consume one critical
point. There are two positive $`\Psi`$-components; their total fixed-level
count is at most $`(6-2)+2=6`$. Hence in every case $`U`$ has at most six
critical points at which $`U>0`$.

## Positive derivative levels have at most seven contacts

Each component of $`\{U>0\}`$ contributes at most one more regular
positive-level contact than its positive critical-point count. The two
preceding bounds therefore give at most $`6+2=8`$ contacts of $`U=E_2`$.
But

```math
U(t)\longrightarrow+\infty\quad(t\to0),\qquad
U(t)\longrightarrow-\infty\quad(t\to1).
```

A regular positive level has an odd total number of contacts. Thus its
total is at most seven. The original $`f'`$ has at most seven roots,
so Rolle gives at most eight roots of $`f`$.

For arbitrary positive coefficients, regular positive $`E_2`$-levels are dense,
and any hypothetical nine or more original roots can first be made simple
by a small common constant shift and positive coefficient rescaling.
Their sign brackets survive a small independent $`E_2`$ perturbation.
The contradiction above therefore applies without a generic-coefficient
restriction. The wall $`m_0=m_1`$ and degenerate support sources use
compact original-row regularization and nearby strict mode-aligned
generic sources; a nearby three-$`R`$-root source is covered by the
universal three-root theorem.

## Short inverse-mode proof

For $`t<m_0`$, put $`d_0=A-(A+B)t>0`$. Then

```math
\frac{h_0''}{h_0'}=
-\frac A t+\frac B{1-t}-\frac{A+B}{d_0}
-\frac1t+\frac1{1-t}<-\frac1t,
```

since the first two terms have negative sum and
$`(A+B)/d_0>1/(1-t)`$. Writing $`e=c(1-t)+\nu t>0`$ gives

```math
\frac{h_2''}{h_2'}=
\frac{c-1}t+\frac{\nu+1}{1-t}+\frac{\nu-c}e>-\frac1t.
```

The last inequality follows because the numerator of its last two terms,
after multiplication by $`(1-t)e`$, is
$`\nu[(c+1)(1-t)+(\nu+1)t]>0`$.
Since $`h_0'/h_2'<0`$, its derivative is positive. At $`m_0`$ the
same sign follows from $`h_0'=0,h_0''>0`$.
Thus $`u'<0`$ and $`V>0`$ before and at the inverse mode.
