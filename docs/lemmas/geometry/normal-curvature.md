# Recovered signed normal-curvature and nested pure-PS proof

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Statements and exact scope

For real supports $`s_i=(a_i,b_i)`$, positive coefficients $`E_i`$, and
positive level $`L`$, write

```math
S(t)=\sum_{i=1}^3 E_i t^{a_i}(1-t)^{b_i},\qquad f(t)=L-S(t),\quad 0<t<1.
```

The reconstructed results are:

1. If the supports are affinely independent and the origin is strictly
   inside their triangle, every original level has at most **eight roots
   counted with multiplicity**.
2. If the supports are affinely independent, their triangle misses the
   open negative quadrant, and the origin quadratic below is zero-free
   on the actual positive-normal arc, every nonidentity row has at most
   **nine root weights**. Equal eventual nonzero endpoint signs improve
   this to **eight**.
3. For the entire strict nested pure-PS source


```math
s_1=(-U,b_1),\quad s_2=(a_2,b_2),\quad s_3=(a_3,-F),
```

   with all six magnitudes positive, $`a_3>a_2`$, $`b_1>b_2`$, every
   original level has at most **eight distinct roots**. The ceiling is
   **eight counted with multiplicity** when the supports are not
   affine-collinear. The collinear seam below deliberately retains the
   distinct-only conclusion of its standing input.
4. The finite weak closure of this source, with
   $`U,F,a_2,b_2\ge0`$, $`a_3\ge a_2`$, $`b_1\ge b_2`$, $`E_i\ge0`$
   and $`L>0`$, has at most **eight distinct roots**, provided f is not
   identically zero. No weak-boundary multiplicity assertion is made.

These are regional results, not the unrestricted new (3,1) master
theorem. Original physical endpoints are never counted. All support
parameters in the closure statement are finite.

## 1. Universal actual-level normal flow

Put

```math
G(z)=\log\sum_i E_i e^{s_i\cdot z},\quad
q(z)=e^{z_1}+e^{z_2},\quad \ell=\log L.
```

Original roots are exactly intersections of $`G=\ell`$ and $`q=1`$,
through $`z=(\log t,\log(1-t))`$. Affine independence makes the Gibbs
covariance Hessian of G positive definite everywhere.

Define

```math
\begin{gathered}
\Delta=\det[1;a;b],\qquad
\alpha_i=(a_jb_k-a_kb_j)/\Delta\quad\text{(cyclic)},\\
d_i=a_i+b_i,\quad \lambda_i=a_i-d_i x,
\quad w=x(1-x),\quad n_x=(x,1-x),\quad l_x=(1-x,-x),\\
\beta=(\lambda_3-\lambda_2,\lambda_1-\lambda_3,
             \lambda_2-\lambda_1)/\Delta.
\end{gathered}
```

The identities
$`\sum\alpha_i=1`$, $`\sum\alpha_i s_i=0`$,
$`\sum\beta_i=0`$, $`\sum\beta_i s_i=n_x`$
are direct determinant identities. On an actual positive-normal level
branch, $`\nabla G=\tau n_x`$, $`\tau>0`$; its actual Gibbs weights are

```math
p_i=\frac{E_i e^{s_i\cdot z}}{e^\ell}=\alpha_i+\tau\beta_i>0.
```

Let

```math
\begin{aligned}
V&=\sum p_i\lambda_i^2>0,&C&=\sum p_i\lambda_i d_i,&\rho&=\tau/V>0,\\
V_0&=\sum\alpha_i\lambda_i^2,&V_1&=\sum\beta_i\lambda_i^2,\\
C_0&=\sum\alpha_i\lambda_i d_i=-V_0'/2,&
C_1&=\sum\beta_i\lambda_i d_i,\\
\Lambda&=\sum\lambda_i,&\Pi&=\lambda_1\lambda_2\lambda_3.
\end{aligned}
```

Differentiating the actual normal equation gives

```math
z'=\rho l_x,\quad p_i'=\rho p_i\lambda_i,\quad
\tau'=\rho C,\quad V'=\rho\sum p_i\lambda_i^3-2C.
\tag{1}
```

For example, dotting the differentiated normal equation with l gives
$`\rho V=\tau`$; summing its two coordinates gives the equation for
$`\tau'`$. The mean score is zero, so the cubic polynomial with roots
$`\lambda_i`$ gives
$`\sum p_i\lambda_i^3=\Lambda V+\Pi`$.
Also $`V=V_0+\tau V_1`$, $`C=C_0+\tau C_1`$, and
$`V(1-\rho V_1)=V_0`$. Eliminating V proves

```math
V_0\rho'=3C_0\rho+B\rho^2+\Pi V_1\rho^3,
\qquad B=3C_1V_0-3C_0V_1-\Lambda V_0-\Pi.
\tag{2}
```

Compare $`\rho_0=1/w`$. On a connected zero-free V0 interval,
$`d=\rho-1/w`$ obeys

```math
d'=A(x)d+\frac{T(x)}{V_0w^3},\quad
T=3C_0w^2+Bw+\Pi V_1+V_0(1-2x)w.
\tag{3}
```

A is analytic, obtained by dividing the difference of the cubic in (2)
by $`\rho-\rho_0`$. Crucially, $`\deg T\le6`$: V0 has degree at most
two, V1 at most three, C0 at most one, C1 at most two, B at most four,
and Pi at most three. This degree bound needs no computer algebra
cancellation. One may additionally verify the exact identity
$`T=K_6/\Delta`$, where

```math
K_6=\det\begin{bmatrix}
\lambda_i\\
\lambda_i^2-wd_i\\
\lambda_i^3-3wd_i\lambda_i-w(1-2x)d_i
\end{bmatrix}_{i=1,2,3},
\tag{4}
```

but (4) is not necessary for the bounds proved here.

A positive integrating factor makes the derivative of d a nonzero
analytic unit times T. Weighted Rolle therefore gives at most seven
zero weights of d if T is nonzero. For

```math
H=\log\frac{x}{1-x}-z_1+z_2,
\quad H'=1/w-\rho=-d,
```

it gives at most eight zero weights of H, and

```math
\frac{d}{dx}q(z(x))=\rho e^{z_2}x(e^{-H}-1)
\tag{5}
```

shows that these are exactly the critical weights of q on that branch.
All weighted statements follow by selecting a finite root collection:
an analytic function with root orders r_i forces derivative orders
$`r_i-1`$ at those roots and one root between consecutive distinct roots.
Thus no advance finiteness assumption or simple-root hypothesis is used.

If T is identically zero, (3) is homogeneous. Either d is nowhere zero,
making H strictly monotone, or d is identically zero and H constant.
This exceptional alternative is treated explicitly in each geometry
below; it is not discarded as a genericity condition.

## 2. Full proof of the signed compact-oval eight-weight theorem

Assume $`\alpha_i>0`$. The origin is strictly inside the source triangle.
Its convex hull contains a small Euclidean ball about zero, so
$`\max_i s_i\cdot z\ge c|z|`$ for some $`c>0`$. Thus G is coercive,
strictly convex, and has a unique minimum. Levels below that minimum
are empty. A level at the minimum is a singleton. If the singleton
lies on q=1, then along the physical curve the second derivative of G
is a strictly positive Hessian quadratic form; the original contact
has order exactly two. This case satisfies the bound.

Every higher G level is a compact strictly convex analytic oval. Its
Gauss normal is a global analytic coordinate, so its positive-normal
arc is precisely $`0<x<1`$, with finite boundary points at x=0 and x=1.
Since every alpha is positive and the three scores cannot simultaneously
vanish for affinely independent supports, V0 is strictly positive on
the whole interval. The comparison in Section1 applies.

Moreover H tends to minus infinity at x=0 and plus infinity at x=1,
because z has finite endpoint limits. If T is nonzero, H has at most
eight zero weights and these opposite endpoint signs make that total
odd: it is at most seven. If T is zero, the identically-zero d alternative
would make H constant and contradict these limits. Thus H is strictly
monotone and contributes at most one simple zero. In every case the
positive-normal arc has at most seven q critical weights.

On the negative-normal arc there is exactly one q critical, the unique
minimum of q on the convex compact sublevel $`K=\{G\le\ell\}`$. The
minimum is unique by strict convexity, is on the boundary because
$`\nabla q\ne0`$, and satisfies $`\nabla q=-c\nabla G`$, $`c>0`$.
The constrained tangent Hessian is
$`\operatorname{Hess}q+c\operatorname{Hess}G`$, strictly positive.
This critical is nondegenerate and its derivative weight is one.
Mixed and axis normals cannot be proportional to the strictly positive
gradient of q, so have no q criticals.

Consequently q has at most eight critical weights around the entire
oval. It is nonconstant, already apparent from H's opposite limits.
Periodic weighted Rolle gives at least as many derivative weights as
level-contact weights: include a derivative root in every cyclic gap
as well as the inherited r_i-1 weights at each contact. Therefore q=1
has at most eight contact weights on the oval.

These are the original physical root orders. A transverse intersection
is simple in both descriptions. At a tangency, the nonzero proportional
gradients have nonzero second coordinates. Both curves are locally
analytic graphs over z1, and each defining restriction is a nonzero
analytic unit times their same graph difference. The coordinate
$`t=e^{z_1}`$ on q=1 is locally an analytic diffeomorphism. Thus contact
orders, including tangencies of either normal sign, agree. This completes
the signed origin-interior eight-weight theorem without an original
EHT ceiling or projective event atlas.

## 3. Full open-boundary proof when the hull misses the negative quadrant

Suppose the source triangle misses $`( -\infty,0)^2`$. Separation gives
$`n\in[0,\infty)^2\setminus\{0\}`$ with $`n\cdot s_i\ge0`$ for all i.
At least one dot product is strict by affine independence. Therefore
$`\partial_nG>0`$ everywhere. In coordinates $`z=yv+un`$, $`v\perp n`$,
G is strictly increasing in u, with upper limit infinity and lower limit

```math
G_F(y)=\log\sum_{n\cdot s_i=0}E_i e^{y s_i\cdot v},
```

interpreted as minus infinity for an empty face. The whole nonempty G
level is one regular analytic graph over
$`\{y:G_F(y)<\ell\}`$, an open interval by convexity. All original
contacts, including mixed-normal contacts, lie on this one graph.

The source-only positive-normal domain is

```math
I_+=\{x\in(0,1):\exists p_i>0,\ \sum p_i=1,
\ \sum p_i s_i=\tau(x,1-x)\text{ for some }\tau>0\}.
```

This is one open interval, possibly empty: the source cone is contained
in the separating half-plane and its interior positive rays form one
angular interval. Its interior rays are exactly combinations with all
three coefficients positive. For every such normal the supporting bound
of K is compact. To see this, write the normal as $`\sum c_i s_i`$,
$`c_i>0`$; all $`s_i\cdot z`$ have upper bounds on K. An escaping
sequence in an upper bound, normalized to a limiting direction d, would
have $`s_i\cdot d\le0`$ and $`\sum c_i s_i\cdot d\ge0`$, forcing all
$`s_i\cdot d=0`$. The supports span the plane, a contradiction.
Strict convexity makes the supporting point unique, and its positive
definite Hessian gives the analytic actual-normal parametrization used
in Section1. Every positive-normal boundary point occurs there.

There is no negative-normal q critical, because its Gibbs mean would
lie strictly in the negative quadrant. Axis and mixed normals have
none either. If V0 is zero-free on I+, Section1 bounds the whole graph's
q critical weights by eight, hence q=1 contacts by nine via ordinary
weighted Rolle. Empty I+ gives no criticals.

For T identically zero, the nowhere-zero d alternative gives at most
one critical. If d is identically zero, H is constant. A nonzero H makes
q strictly monotone on the positive branch. If H=0, q is constant on
an open branch and hence on the full connected analytic graph. Its
constant either differs from one, giving no original roots, or equals
one, forcing the original analytic row to be an identity. This is why
the nonidentity hypothesis is explicit. Root orders transfer by the
same local graph argument as in Section2. Equal eventual nonzero
original endpoint signs make total root weight even, improving nine
to eight. This theorem also needs no original EHT ceiling.

## 4. Exact source dispatch for every strict nested pure-PS row

Set

```math
R=a_3b_1-UF,
\quad N_1=-(a_2F+a_3b_2),\quad N_2=R,
\quad N_3=-(Ub_2+a_2b_1),\quad\Delta=N_1+N_2+N_3.
\tag{6}
```

These are the cyclic origin numerators. N1 and N3 are strictly negative.
If R<0, all three alpha=N/Delta are strictly positive, so Section2
gives eight root weights directly.

If R>=0, the positive vector n=(b1,U) has dots
$`0,a_2b_1+Ub_2,R`$ against the three supports. Hence the hull misses
the open negative quadrant. We verify Section3's quadratic inequality on the
entire physical interval, stronger than the actual-arc requirement.
The strict nested inequalities imply

```math
\lambda_1<0<\lambda_3,\qquad \lambda_1<\lambda_2<\lambda_3,
\tag{7}
```

because the two score gaps are
$`(a_2+U)(1-x)+(b_1-b_2)x`$ and
$`(a_3-a_2)(1-x)+(b_2+F)x`$, both positive.

For Delta>0, alpha1,alpha3<0 and alpha2>1. Put
$`\theta=-\alpha_1/\alpha_2>0`$, $`\eta=-\alpha_3/\alpha_2>0`$.
The origin identity gives $`\lambda_2=\theta\lambda_1+\eta\lambda_3`$
and $`\theta+\eta=1-1/\alpha_2<1`$. Thus

```math
V_0=-\alpha_2\bigl[(1-\theta-\eta)
(\theta\lambda_1^2+\eta\lambda_3^2)
+\theta\eta(\lambda_1-\lambda_3)^2\bigr]<0.
\tag{8}
```

For Delta<0 and R>=0, alpha1,alpha3>0 and alpha2=-k<=0. The zero
origin score mean gives the exact identities

```math
\begin{aligned}
V_0&=\alpha_1(-\lambda_1)(\lambda_3-\lambda_1)
  +k\lambda_2(\lambda_3-\lambda_2),&&\lambda_2\ge0,\\
V_0&=\alpha_3\lambda_3(\lambda_3-\lambda_1)
  +k(-\lambda_2)(\lambda_2-\lambda_1),&&\lambda_2\le0.
\end{aligned}
\tag{9}
```

The first terms are strictly positive and second terms nonnegative.
Hence V0>0. This includes R=0 (k=0) and lambda2=0 directly, without
any limiting or simplicity assumption.

Section3 therefore gives nine weights in both noncollinear outside
dispatches. The first atom diverges at t=0 and the third at t=1, so f
is eventually negative at both endpoints and cannot be an identity.
Parity improves nine to eight weights.

If Delta=0, the three distinct supports lie on an affine line whose
direction $`s_3-s_1=(a_3+U,-F-b_1)`$ has opposite coordinate signs.
The following standing affine-collinear argument supplies eight
distinct roots. For n supports $`p+c_i v`$, $`v_1v_2\le0`$, v nonzero,
put D=t(1-t)d/dt, q_v=v1-(v1+v2)t, ell_p=p1-(p1+p2)t. The monotone
coordinate y=log(beta_v) has derivative d/dy=D/q_v. Divide the original
row by beta_p and apply the n commuting annihilators (d/dy-c_i).
Each loses at most one distinct root. Applied to g=1/beta_p, their
result is g P_n/q_v^(2n-1), where

```math
P_1=-\ell_p-c_1q_v,\qquad
P_{j+1}=t(1-t)(q_vP_j'-(2j-1)q_v'P_j)
             -q_v(\ell_p+c_{j+1}q_v)P_j.
```

Inductively deg P_j<=2j-1, giving n+2n-1=3n-1 distinct roots; for
n=3 this is eight. If P_n is identically zero, the divided original row
lies in a real-exponential Chebyshev kernel and has at most n-1 roots
unless identity. Repeated supports may be merged. This reconstructs
the prior collinear input; its historically stated distinct scope is
retained without claiming a new multiplicity upgrade.

## 5. Finite weak nested closure, distinct roots only

Assume the weak source and coefficient conditions in Statement4 and
f nonidentity. If f had nine distinct roots, select nine disjoint
interior neighborhoods. At an odd-order zero a sufficiently small
nonzero common level shift f-eta has one nearby crossing for either
sign. At an even-order zero it has two for one sign, none for the other.
For o odd roots and e+,e- of the two even types,
$`\max(o+2e_+,o+2e_-)\ge o+e_++e_-=9`$. Choose that one sign for all
neighborhoods and eta arbitrarily small, |eta|<L/2, avoiding the
countable critical-value set of the nonconstant analytic f. At least
nine resulting simple roots can be chosen. The single perturbed level
L'=L-eta is positive. Give those roots nine compact disjoint sign
brackets; no assertion preserves every even-root neighborhood.

Explicit strict approximants are

```math
\begin{gathered}
U_\varepsilon=U+\varepsilon,\quad F_\varepsilon=F+\varepsilon,
\quad a_{2,\varepsilon}=a_2+\varepsilon,
\quad b_{2,\varepsilon}=b_2+\varepsilon,\\
a_{3,\varepsilon}=a_3+2\varepsilon,
\quad b_{1,\varepsilon}=b_1+2\varepsilon,
\quad E_{i,\varepsilon}=E_i+\varepsilon.
\end{gathered}
```

They have strictly positive magnitudes and coefficients and both nested
gaps at least epsilon. Evaluation at each fixed interior bracket endpoint
is continuous in all finite supports and coefficients, so the nine
strict sign brackets persist. Every strict approximant, including a
collinear one, has at most eight distinct roots by Section4: contradiction.
This is the abstract original-row aggregate regularization
and compact-bracket transfer interface, reconstructed in its concrete
application. It needs no auxiliary discriminant, event-word density,
or root-simplicity exclusion. The weak identity exclusion is necessary:
supports (0,1),(1,0),(1,0), coefficients (1,1,0), level1 give f identically0.
