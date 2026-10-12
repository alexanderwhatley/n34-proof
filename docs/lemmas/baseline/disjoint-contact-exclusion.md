A contact here means a root of the degree-at-most-six determinant polynomial $`K`$. For a complementary pair $`i,j`$, its useful set $`U_{ij}`$ consists of the points where $`c_ie_i`$ and $`c_je_j`$ have the same sign: these are the intervals on which the reduced original equation can vanish. The signed cubic cofactor $`e_i`$ omits column $`i`$ from the three-row derivative matrix, with its alternating sign. All are the cofactors of the actual four beta factors, rather than independently chosen cubics.

For two supports use

```math
\rho=x(1-x),\quad D=\rho\frac d{dx},\quad \lambda_s=s_1-(s_1+s_2)x,
```

```math
H(r,s)=\lambda_rD\lambda_s-\lambda_sD\lambda_r+\lambda_r\lambda_s(\lambda_s-\lambda_r).
```

The standard derivative reduction loses at most two original roots for a monotone anchor pair. On $`j`$ useful components, the reduced equation has at most $`j`$ plus the number of useful contacts roots. These general determinant and Rolle identities are the prerequisites of the argument below.

For $`\alpha,\beta,\gamma>0`$, let

```math
F=1+\alpha m_u-\beta m_v-\gamma m_w,
```

with

**(5.1)**

```math
\boxed{0<v_1<u_1<w_1,\qquad 0<w_2<u_2<v_2.}
```

Then $`Z(F)\le8`$. Reflection $`x\mapsto1-x`$ and relabeling the two negative terms give the same conclusion.

**Proof.** Label $`s_0=0,s_1=u,s_2=v,s_3=w`$. The three nonconstant supports are pairwise incomparable, and their modes obey

**(5.2)**

```math
\theta_v<\theta_u<\theta_w,\qquad \theta_s=s_1/(s_1+s_2).
```

The determinant cofactors have the following signs at both endpoints:

**(5.3)**

```math
(\operatorname{sgn}e_0,\operatorname{sgn}e_1,
  \operatorname{sgn}e_2,\operatorname{sgn}e_3)=(-,-,+,+).
```

The two endpoint signs of K are opposite, so there are at most five physical K roots. The complementary useful sets for the three monotone pairs among u,v,w are $`U_{01},U_{02},U_{03}`$.

Suppose F had ten generic roots. By the two derivative reductions and the useful-component root count, each of e_0,e_1,e_2,e_3 must have two roots; every one of the five physical K roots must be useful for **all three** of these sets. This follows because each relevant component count is at most three, and eight residual roots require at least five useful contacts.

Now examine e_3, the signed cubic for the triple $`1,m_u,m_v`$. Since

```math
\Delta_3=u_1v_2-v_1u_2>0,\qquad
 T_3=\lambda_u\lambda_v(\lambda_v-\lambda_u)-\rho\Delta_3,
```

and $`\lambda_v-\lambda_u<0`$ everywhere, T_3 is strictly negative outside $`(\theta_v,\theta_u)`$. Thus both roots $`r_1<r_2`$ of e_3 lie in that interval, and

**(5.4)**

```math
e_3<0\quad(r_1,r_2).
```

On the entire same interval e_2 is strictly positive. Indeed e_2 is the cubic for $`1,m_u,m_w`$, for which $`\Delta_2=u_1w_2-w_1u_2<0`$, and both $`\lambda_u,\lambda_w`$ are positive before $`\theta_u`$. The determinant cubic formula therefore gives $`e_2>0`$.

The exact contact identity for k=2,l=3, at a zero of e_3, reduces to

**(5.5)**

```math
\boxed{\lambda_u K=e_2De_3.}
```

Since $`\lambda_u>0`$ and $`e_2>0`$ there, $`K(r_1)<0<K(r_2)`$. A K root lies between them. But throughout that interval

```math
\operatorname{sgn}(c_2e_2)=-1,
 \qquad \operatorname{sgn}(c_3e_3)=+1.
```

Regardless of the sign of $`c_0e_0`$, that K root cannot belong to **both** $`U_{02}`$ and $`U_{03}`$. This contradicts the five jointly useful contacts forced above.

There is no ten-root row. Equal positive original endpoint signs give at most eight simple roots, and the limiting-cases lemma extends the bound to all distinct roots and support limits of this proved region. QED.
