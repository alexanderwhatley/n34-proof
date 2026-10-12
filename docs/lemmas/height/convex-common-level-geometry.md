# Convex common-level geometry for comparable supports

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Research note, 2 October 2026. This note proves a geometric reduction, not the proposed full master height theorem. The unresolved same-curvature budget is stated explicitly below.

## Exact original-source setting

Let

```math
G(x)=c_1-u(x)+c_3v(x)+c_4w(x),\qquad c_1,c_3,c_4\gt0,
```

where the beta monomial supports satisfy $`0\prec s_u\prec s_v\prec s_w`$. Put $`q=w/v`$. After reflection, suppose the modes of $`q,v`$ are distinct and

```math
v=x^a(1-x)^b,\quad q=x^A(1-x)^B,\quad
\Delta=aB-bA\gt0.
```

There are unique real $`h,n`$ such that $`u=v^h q^n`$. In this note the coordinates are

```math
y=\log v,\qquad s=\log q.
```

All statements retain the one original triple $`(c_1,c_3,c_4)`$. No levels are reset between components.

## One convex level set

Define

```math
F(y,s)=\log(c_1+c_3e^y+c_4e^{y+s})-hy-ns.
```

Then $`G(x)=0`$ is equivalent to $`F(\log v(x),\log q(x))=0`$, and $`G(x)\lt0`$ is equivalent to $`F\lt0`$.

Write the positive weights

```math
\omega_0=\frac{c_1}{Z},\quad \omega_3=\frac{c_3e^y}{Z},\quad
\omega_4=\frac{c_4e^{y+s}}{Z},\qquad
Z=c_1+c_3e^y+c_4e^{y+s}.
```

The Hessian of $`F`$ is the covariance matrix of the three distinct vectors $`(0,0),(1,0),(1,1)`$, with these weights. Explicitly,

```math
F_{yy}=\omega_0(1-\omega_0),\quad
F_{ys}=\omega_0\omega_4,\quad
F_{ss}=\omega_4(1-\omega_4),\quad
\det\nabla^2F=\omega_0\omega_3\omega_4\gt0.
```

Thus $`F`$ is strictly convex for every real $`h,n`$, independently of all mode and scale choices. At every regular boundary point,

```math
F_y=1-h-\omega_0,\qquad F_s=\omega_4-n.
```

If a boundary arc is written $`y=b(s)`$, its second derivative satisfies

```math
b''(s)=-\frac{(b',1)\nabla^2F(b',1)^T}{F_y}.
```

The numerator is strictly positive. Consequently the lower boundary is strictly convex and the upper boundary strictly concave.

## The two beta arcs

The equation $`q(x)=e^s`$, for $`s\lt s_{\max}:=\log q(A/(A+B))`$, has exactly two roots $`x_L(s)\lt A/(A+B)\lt x_R(s)`$. Let

```math
f_L(s)=\log v(x_L(s)),\qquad f_R(s)=\log v(x_R(s)).
```

With $`p=\lambda_v/\lambda_q`$, the original source identity gives

```math
f_L'=p_L,\quad f_R'=p_R,\qquad
f_L''=\frac{\Delta x_L(1-x_L)}{\lambda_q(x_L)^3}\gt0,
\quad
f_R''=\frac{\Delta x_R(1-x_R)}{\lambda_q(x_R)^3}\lt0.
```

Moreover $`f_L\lt f_R`$. Indeed equality of $`q`$ gives

```math
f_L-f_R=\frac{\Delta}{B}\log\frac{x_L}{x_R}\lt0.
```

These convexity and ordering conclusions hold throughout the full two physical branches.

## Uniform opposite-curvature bounds

Suppose $`0\lt h\lt1`$, and write $`H=1-h`$ and $`C(s)=c_3+c_4e^s`$. The equation $`F(y,s)=0`$, at fixed $`s`$, becomes

```math
\frac{1+t}{t^h}=k(s),\qquad
t=\frac{C(s)e^y}{c_1},\qquad
k(s)=c_1^{-H}\frac{e^{ns}}{C(s)^h}.
```

The left-hand side has its unique minimum at $`t=h/H`$, with minimum $`h^{-h}H^{-H}`$. Also

```math
(\log k)''=-\frac{h c_3c_4e^s}{C(s)^2}\lt0.
```

Therefore the admissible $`s`$-set is one interval. Where the minimum is strictly exceeded, there are exactly two boundary graphs $`b_-(s)\lt b_+(s)`$, with

```math
b_-''\gt0,\qquad b_+''\lt0.
```

It follows that the original roots assigned to the opposite-curvature pairings obey the uniform bounds

```math
\#\{s:f_L(s)=b_+(s)\}\le2,
\qquad
\#\{s:f_R(s)=b_-(s)\}\le2.
```

For example $`f_L-b_+`$ is strictly convex; a strictly convex function on an interval has at most two zeros. The second assertion follows because $`f_R-b_-`$ is strictly concave. These conclusions need no bound, cubic-root order, residue sign, or position of the $`u`$-mode.

For $`h\le0`$, $`F_y\gt0`$: the boundary, where it exists, is one strictly concave graph. Hence its intersections with the left beta arc number at most two. For $`h\ge1`$, $`F_y\lt0`$: the boundary is one strictly convex graph, whose intersections with the right beta arc number at most two. The equality values $`h=0,1`$ are valid on the interval where the finite graph exists.

## Precise remaining master target

At an original root, $`Z=u`$, so $`F_y=H-c_1/u`$. Thus lower-boundary roots satisfy $`c_1\lt u\lt c_1/H`$, and upper-boundary roots satisfy $`u\gt c_1/H`$. The upper roots lie in one central original-coordinate interval because $`u`$ is unimodal. The lower roots lie in its two exterior strips, restricted to the original-root hull $`u\gt c_1`$.

For the generic counting reduction, also exclude original roots at the $`q`$-mode and at a vertical boundary fold $`F_y=0`$. This is a proper additional generic choice. At fixed supports and $`c_1`$, the latter requires $`u=c_1/H`$, which has at most two original $`x`$ solutions. At each such solution the original-root equation is one affine constraint on $`(c_3,c_4)`$. Perturbing $`c_3`$ avoids the finite union while retaining any already chosen compact simple-crossing brackets. The $`q`$-mode similarly contributes one affine forbidden coefficient constraint. This choice permits every generic original root to be assigned to exactly one of the four open arc pairings.

For $`0\lt h\lt1`$, ten such generic original roots would require at least six roots in the *same-curvature pairings*

```math
f_L=b_-,\qquad f_R=b_+,
```

since the other two pairings together contribute at most four. Thus a genuinely sufficient master lemma is the following:

> Under the linked source constraints $`0\prec s_u\prec s_v\prec s_w`$, the two same-curvature pairings together cannot have six generic intersections when the opposite-curvature pairings are also present in the required original-root configuration.

The last qualification is material. No unrestricted bound on either same-curvature pairing is proved here. Arbitrary convex graphs can intersect arbitrarily often, so strict convexity alone cannot finish the problem. Any completion must use the linked beta structure, the one coefficient triple, or the forced original-root configuration.

This reduction supplies one convex-domain description for all mode cases and isolates two potentially oscillatory boundary comparisons. It does not yet replace the original comparable-support exclusions.
