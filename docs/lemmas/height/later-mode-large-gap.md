# Rightmost-u exclusion when h-n >= 1

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Date: 2026-09-10. Together with *hge1 exclusion*, this extends the exclusion to h-n>=1. The new derivative-ratio proof below treats 0<h<1; the h>=1 part uses the preceding note. No bound restriction is used.

## Theorem and exact scope

For an original strict comparable row

```math
G=c_1-u+c_3v+c_4w,\quad c_1,c_3,c_4>0,
\quad0\prec\operatorname{supp}u\prec\operatorname{supp}v\prec\operatorname{supp}w,
```

let q=w/v and reflect so that rho_q<rho_w<rho_v. Write u=v^h q^n. If

```math
h>0,\qquad n<0,\qquad h-n\ge1,
```

then G has at most nine distinct roots. This covers all h>=1, and also 0<h<1,n<=h-1. The remaining rightmost-u subregion is exactly

```math
0<h<1,\qquad h-1<n<0.
```

The h>=1 part is already proved in *hge1 exclusion*. The new proof below assumes 0<h<1 and n<=h-1. The key equivalent geometric condition is rho_{v/u}<=rho_w. Indeed

```math
\det(\operatorname{supp}(v/u),\operatorname{supp}w)
=(1-h+n)\Delta.
```

## 1. At most two roots after the mode of v/u

Put a=v/u, b=w/u, R=G/u, and tau=rho_a. For 0<h<1,n<0, the modes obey

```math
\rho_q<\rho_b<\rho_a\le\rho_w<\rho_v<\rho_u.
```

Indeed a=v^{1-h}q^{-n} is a positive combination of the support vectors of v and q, and b=a q moves the mode toward q. Both a,b decrease after tau. Consequently R=c1/u-1+c3a+c4b decreases strictly on (tau,rho_u). On (rho_u,1), the exact formula

```math
R_x=\frac{-u_x}{u^2}\{c_1-c_3T_v-c_4T_w\},
\quad T_v=v\frac{L_u-L_v}{-L_u},
\quad T_w=w\frac{L_u-L_w}{-L_u}
```

has braces strictly increasing from minus infinity to c1. In fact each T is positive and strictly decreasing, because

```math
T_v=v\frac{S_a}{S_u}\frac{x-\rho_a}{x-\rho_u}
```

and both factors decrease; S_f is the sum of the two positive exponents of f. Thus R has one minimum on (tau,1) and at most two roots there.

In the following sections write f=v,g=w, with c_f=c3,c_g=c4. The notation permits the derivative identities to be displayed without long subscripts; no function or coefficient is exchanged.

## 2. Seven common derivative-ratio stationary nodes

Set

```math
S_f=f'/u',\quad S_g=g'/u',\qquad
P=c_f S_f+c_g S_g,
```

with the original positive coefficients assigned to f,g. On (0,tau), all u',f',g' are positive. Each S has a strictly concave logarithm there. For example

```math
\log S_f=\log(f/u)+\log(S_f^{\rm exp}/S_u^{\rm exp})
+\log(\rho_f-x)-\log(\rho_u-x).
```

Here the first term is a positive-exponent beta logarithm, whose second derivative is strictly negative. The last difference has second derivative

```math
-1/(\rho_f-x)^2+1/(\rho_u-x)^2<0.
```

Each ratio tends to zero at x=0, initially increases, and is strictly decreasing at tau: the beta ratio f/u (or g/u) has nonpositive logarithmic derivative there, and the linear-score ratio contributes a strictly negative derivative. Thus each S has exactly one stationary point alpha_f,alpha_g in (0,tau), a strict maximum.

A hypothetical ten-root G has at least eight roots before tau by Section 1. Rolle and G'=u'(P-1) give at least seven hits P=1 there, hence at least six P' zeros.

The raw derivative is

```math
P' =\frac{c_f f P_f+c_g g P_g}{u\omega L_u^2},
```

```math
P_f=(L_f-L_u)L_fL_u+
\omega(L_f'L_u-L_fL_u'),
```

Before tau, P' starts positive and ends negative. The number of its generic simple zeros there is therefore odd. It is at least six and globally at most seven, hence exactly seven.

At every such node,

```math
-\frac{S_f'}{S_g'}=\frac{c_g}{c_f}>0.
```

Both derivative signs can be opposite only between alpha_f and alpha_g; if the maxima coincide, there is only one stationary P node and an immediate contradiction. Thus all seven nodes lie in one open interval where the ratio above is smooth, at the same original positive coefficient ratio. Rolle forces six roots of

```math
S_f'S_g''-S_g'S_f''
=\frac{W(u',f',g')}{(u')^3}.
```

No independent coefficients or heights were introduced.

## 3. The sextic cannot have six roots before tau

Order the upper functions in the determinant as f=v,g=w. The quotient f/u has mode tau and g/u has an earlier mode. At tau, L_f=L_u=L>0. Write L_g=L+Q, where Q<=0 because the mode of g/u is no later than tau. Under h-n>=1, tau is no later than either upper mode, so L+Q>=0. In the strict, noncoincident case Q<0.

Let S_u,S_a,S_q denote exponent sums of u, f-u, and g-f respectively in the algebraic identity below. All of these exponent sums are positive, and their sum is S_g. Direct beta-jet expansion gives the raw top-Wronskian core at tau:

```math
W_{\rm raw}(\tau)
=S_a LQ\omega\{3S_g\omega+L^2-Q^2+(L+Q)\omega'\}.
```

The brace is positive. First L^2-Q^2>=0 since -L<=Q<=0. Next 3S_g omega+(L+Q)omega'>0: if omega'>=0 this is immediate; if omega'<0, use 0<=L_g<=S_g(1-x) to bound it below by S_g(1-x)(1+x)>0.

Thus W_raw(tau)<0. At x=0, strict support comparison gives

```math
W_{\rm raw}(0)=a_u a_v a_w(a_v-a_u)(a_w-a_u)(a_w-a_v)>0.
```

These are the required opposite endpoint signs.

The raw Wronskian has degree at most six and

```math
W(u',v',w')=uvw\,W_{\rm raw}/\omega^6.
```

Six distinct roots before tau would exhaust the degree and all would be simple, forcing the endpoint signs to agree. The opposite signs rule this out and contradict Section 2.

## 4. Weak faces and dependencies

The proof directly includes n=h-1 with 0<h<1: then tau=rho_w, so Q=-L at that endpoint and the brace remains strictly positive. At h=1 the earlier h>=1 theorem applies. Generic original-root regularization, retaining common coefficients and compact root brackets, is exactly as in *hge1 exclusion* and the global theorem. All strict-support original rows in the stated scope are excluded at distinct-root level.

Completed scope: **rightmost u with h-n>=1**, with no lambda bound. Remaining scope: **0<h<1, h-1<n<0**.
