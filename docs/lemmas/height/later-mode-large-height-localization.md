# Rightmost-u mode: complete exclusion for h >= 1

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Date: 2026-09-10. This note closes the h >= 1 part of the assigned rightmost-u region. The 0 < h < 1, n < 0 part is still separate and is not declared closed here.

## Theorem

Let

```math
G=c_1-u+c_3v+c_4w,
\quad c_1,c_3,c_4>0,
\quad0\prec\operatorname{supp}u\prec\operatorname{supp}v
\prec\operatorname{supp}w,
```

with beta functions on (0,1). Reflect so that q=w/v has mode before w and v, and write u=v^h q^n in the nondegenerate chart. If h>=1 and n<0, then G has at most nine distinct roots. There is no bound restriction on lambda.

## 1. A tail lemma for the original row

Put a=v/u and b=w/u, and divide the entire row by u:

```math
R=G/u=c_1/u-1+c_3a+c_4b.
```

Both a and b are positive-exponent beta functions. Let rho_a,rho_b,rho_u be their modes. The determinant identity

```math
\det(\operatorname{supp}(v-u),\operatorname{supp}q)
=(1-h)\Delta\le0
```

is an identity of exponent vectors; equivalently, supp(v/u)=supp(v)-supp(u). Thus rho_a<=rho_q. Since b=a q, rho_b is between rho_a and rho_q. In particular both a and b decrease on (rho_q,1). Also rho_u>rho_v>rho_w>rho_q in this mode chart. Consequently R is strictly decreasing on (rho_q,rho_u).

For x>rho_u, set L_f=A_f-(A_f+B_f)x for each beta function f and define

```math
T_v=v\frac{L_u-L_v}{-L_u},
\qquad T_w=w\frac{L_u-L_w}{-L_u}.
```

Then

```math
R_x=\frac{-u_x}{u^2}
\{c_1-c_3T_v-c_4T_w\}.
```

For example,

```math
\frac{L_u-L_v}{-L_u}
=\frac{A_a+B_a}{A_u+B_u}
\frac{x-\rho_a}{x-\rho_u}.
```

This ratio is positive and strictly decreasing for x>rho_u, since rho_a<rho_u. The function v is also strictly decreasing there. Thus T_v is positive and strictly decreasing from infinity to zero; the same holds for T_w. The braces have exactly one zero, crossing from negative to positive. Therefore R has a single minimum on (rho_q,1) and has at most two roots on that interval.

All coefficients in this argument are the original fixed positive c1,c3,c4.

## 2. Ten roots force seven curvature nodes before the q-mode

```math
K_0=c_1C_0-uD_0.
```

The preceding tail lemma leaves at least eight original roots before rho_q. Apply Rolle to G/v on that single interval. There are at least seven hits of L4=c4 before rho_q, and therefore at least six zeros of (L4)_x, equivalently at least six roots of K0, before rho_q.

The raw endpoint signs are

```math
K_0(0)>0,
\qquad K_0(\rho_q)
=-\Delta\omega(\rho_q)\{c_1-(1-h)u(\rho_q)\}<0.
```

Consequently the number of generic simple K0 roots before rho_q is odd. It is at least six and the global ceiling is seven, so it is exactly seven. There are no other K0 roots.

Notice that this step used a single original subinterval and the actual c4. There is no loss at a projective seam and no independent choice of node coefficients.

## 3. Those seven nodes lie in one smooth common-height interval

On the left branch p>r3 the common height is

```math
V=uD/C,
\quad C=p(p+1)-\Pi,
\quad\Pi=\lambda\prod_{i=1}^3(p-r_i),
```

```math
D=E-(h-1)C,
\qquad E=(h-1)hp^2+2(h-1)np+n(n-1).
```

For h>1 the discriminant of E is

```math
4(h-1)n(h-n)<0,
```

and its leading coefficient is positive. Therefore E>0 on R. For h=1, E=n(n-1)>0 as well.

At any original common-height node, D/C=c1/u>0. If C<0, then D=E-(h-1)C>0, impossible. Thus every such node has C>0.

There is exactly one root gamma>r3 of C on this branch. Indeed

```math
\frac{\Pi}{p(p+1)}
```

increases strictly from zero to infinity for p>r3: its logarithmic derivative is sum_i 1/(p-r_i)-1/p-1/(p+1)>0. Hence C>0 precisely on (r3,gamma).

All seven nodes therefore lie in (r3,gamma), where V is smooth, and all satisfy the same equation V=c1. Rolle forces six distinct roots of V_p there. The exact raw-to-p identity gives

```math
V_p=-\frac{uJ}{\Pi C^2},
\qquad
J=\Pi(EC'-E'C)-(hp+n)CD.
```

Thus J must have six distinct roots on p>r3.

## 4. A two-coefficient obstruction to six left J roots

Set

```math
s=h-1>0,\quad b=r_2-r_1>0,\quad c=r_3-r_2>0,
```

```math
a=-\{(h-1)r_3+n\}>0,
\qquad z=hr_1+n>0.
```

The strict support inequalities make a,z positive, and conversely these variables give the full h>1 support chart via

```math
r_1=a+s(b+c)+z,\quad r_2=r_1+b,\quad r_3=r_2+c,
```

```math
h=1+s,\qquad n=-s r_3-a,
\qquad\lambda>0.
```

| Coefficient | Number of monomials | Every nonzero coefficient |
| --- | ---: | --- |
| j0 | 117 | Strictly negative |
| j5 | 42 | Strictly negative |

In particular j0<0 and j5<0. The j0 sign can also be read directly from J(r3)=-(hr3+n)r3(r3+1)D(r3), since D(r3)=k(r3)(k(r3)-1)>0.

A degree-six real polynomial with six positive roots must be a nonzero scalar multiple of product_{i=1}^6(t-t_i), t_i>0. Its constant term and degree-five coefficient then have opposite signs. The displayed signs therefore rule out six roots on t>0. A degree drop below six rules them out immediately. For h=1 the same exact formula has degree five, so the conclusion holds directly at that face.

This contradicts Section 3 and excludes ten generic simple original roots.

## 5. Nongeneric original roots and scope

For a hypothetical row with ten distinct roots, the original-row regularization in the common-height package first chooses a small common c1 perturbation producing at least ten simple roots. Those roots have compact disjoint sign brackets. All further generic perturbations are chosen within the strict support and strict rightmost-mode chart. For h>1 this chart is open. For h=1 one can perturb slightly into h>1 while retaining every bracket and the strict support inequalities. The forbidden generic configuration would persist, proving the claimed distinct-root exclusion.

**Completed:** rightmost-u h>=1, n<0, all lambda>0.

**Still open in this assigned region:** rightmost-u 0<h<1,n<0. This note does not certify the complete #1 obligation or the chamber.
