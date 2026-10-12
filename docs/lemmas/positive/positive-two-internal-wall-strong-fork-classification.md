# Two internal origin walls are exactly the positive strong forks

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Let s_i=(a_i,b_i), i=1,2,3, have strictly positive coordinates and be affinely noncollinear. Put d_i=a_i+b_i, theta_i=a_i/d_i, and let

```math
I=(\min_i\theta_i,\max_i\theta_i)
```

be the positive-normal interval. Let alpha be the unique origin barycentric vector, so sum alpha_i=1 and sum alpha_i s_i=0, and define

```math
V_0(x)=\sum_i\alpha_i(a_i-d_i x)^2.
```

Then V0 has two distinct internal zeros in I if and only if, after relabeling,

```math
\boxed{s_2=P s_1+Q s_3,\qquad P,Q\gt1.}
```

The outer modes can be ordered theta1<theta3. Their coordinates may be comparable or incomparable; no strict coordinate permutation is required. The two walls are simple. Thus a master covering every positive strong fork P,Q>1 covers EVERY strictly positive affinely noncollinear source with two internal origin-quadratic walls, including comparable outer supports. The word internal here refers to the actual positive-normal interval I, rather than the larger interval (0,1) independently of the support modes.

Because every a_i,b_i is positive, alpha cannot be nonnegative. Since its coordinates sum to one, it has at least one positive coordinate. If it has only one positive coordinate, label it alpha1=t=1+u+v with alpha2=-u, alpha3=-v, u,v>=0. Write lambda_i=a_i-d_i x. Origin balance gives t lambda1=u lambda2+v lambda3 and hence

```math
V_0=-\lambda_1^2-u(\lambda_2-\lambda_1)^2-v(\lambda_3-\lambda_1)^2\le0.
```

If u,v are positive, equality would make all three scores zero and all three supports lie on one ray, contradicting affine noncollinearity. If one of u,v vanishes, equality is the common mode of the two active supports. The third support has a different mode by affine noncollinearity, so this common mode is an endpoint of I. Thus this case has no internal wall.

The remaining case has two positive barycentric coordinates. Relabel them alpha1=A, alpha3=B, alpha2=-k, where k=A+B-1>0. Origin balance gives

```math
s_2=\frac Aks_1+\frac Bks_3,
\qquad P=\frac Ak\gt0,\quad Q=\frac Bk\gt0,\quad P+Q\gt1.
```

The two outer supports are linearly independent: if they lay on the same ray, this positive representation would make all three supports affinely collinear. Order their distinct modes theta1<theta3. The middle mode is a strict positive weighted mean of them, so I=(theta1,theta3).

On I, set r=-lambda1/lambda3. This is an analytic increasing bijection I to (0,infinity). In fact, with gamma=a3 b1-a1 b3>0,

```math
x=\frac{a_1+r a_3}{d_1+r d_3},\qquad
\lambda_3=\frac\gamma{d_1+r d_3},\qquad
\frac{dr}{dx}=\frac\gamma{\lambda_3^2}\gt0.
```

Let D=P+Q-1>0. The origin barycentrics are exactly (P,-1,Q)/D, and lambda2=P lambda1+Q lambda3. Direct expansion yields

```math
\boxed{V_0(x(r))=-\frac{\lambda_3(r)^2}{D}H(r),\qquad
H=P(P-1)r^2-2PQr+Q(Q-1).}
```

The gauge is nonzero throughout I and the coordinate derivative is positive, so wall orders are preserved. The discriminant of H is 4PQD>0. If P,Q>1, its leading and constant coefficients are positive and its middle coefficient negative, so it has exactly two distinct positive roots. If P>1,Q<=1 or P<=1,Q>1, opposite endpoint signs (or a linear/zero-root boundary case) give at most one positive root. If P,Q<=1, every nonzero coefficient of H is negative for r>0 and there is no positive root. Thus there are two internal walls exactly when P,Q>1.

Equivalently, the positive origin barycentrics A,B both lie below one, because

```math
P-1=\frac{1-B}{k},\qquad Q-1=\frac{1-A}{k}.
```

