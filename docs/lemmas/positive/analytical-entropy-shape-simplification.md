Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

This supplements
*equal degree equal weight full master*. It replaces the log-concavity
and central-third Bernstein sign proofs by explicit positive expressions.
The high-tail quintic certificate remains a separate premise.

Use that master's notation: $p>1$, $a=1/p$, $\beta=2-a$,
$K=2p-1$, $q^2=a/\beta$, $v=(1-z^2)/4$, $T=pu$,
$t=2T$, and $V_j=u^jv_c^{(j)}$. The entropy curve is increasing and
strictly concave as a function of $u$; its inverse $u_c(z)$ is even.
All probabilities are positive, so $0<t<1-|z|$.

## Strict log concavity: a two-term positive expression

Put $Z=k(1-t)^2/4$, with $0<k\le1$. The exact identity is

$$
2V_1^2+z^2(V_1+V_2)
=\frac{(1-t)^2}{2(at-2t+2)^2}\,P,
$$

$$
P=t(1-t)(at-2t+2)^2(1-k)^2
+a^2k[1+(1-t)(1-k)].
\tag{A1}
$$

Both terms are nonnegative, and the second is strictly positive. Thus
$(\log u_c)''=-(2V_1^2+z^2(V_1+V_2))/(4V_1^3)<0$ on all $(-1,1)$,
including the center $k=1$. No coefficient enumeration is needed.

## Central third derivative of the inverse radial curve

Let

$$
J=-6V_2V_1^2-z^2(3V_2^2-V_1V_3).
$$

Inverse differentiation gives $u_c'''=uzJ/(8V_1^5)$. Its factorization is

$$
J=\frac{-a(1-t+z)(t+z-1)}{4(at-2t+2)^4}\,P_0(a,t,z).
\tag{A2}
$$

For $0<z<q$, substitute
$a=2q^2/(1+q^2)$, $z=q\omega$, $t=(1-q\omega)h$,
where $q,\omega,h\in(0,1)$. Then

$$
P_0=\frac{8q^4(1-q\omega)}{(1+q^2)^3}R,
$$

$$
R=(1-q^2)(1+q\omega)(3-\omega^2)
+2h(1-\omega^2)[q^2(3-2\omega^2)-\omega^2]
-3h^2(1-q\omega)(1-\omega^2)^2.
\tag{A3}
$$

The quadratic $R$ is concave in $h$. Its two endpoint values are

$$
R(0)=(1-q^2)(1+q\omega)(3-\omega^2)>0,
$$

$$
R(1)=(q+\omega)[(1-q^2)\omega(3-\omega^2)
+3q(1-\omega^2)^2]>0.
\tag{A4}
$$

Therefore $R>0$ for $0<h<1$. Every other factor in (A2)--(A3) is
positive, because $t+z<1$. This proves

$$
\boxed{u_c'''(z)>0\quad(0<z<q),\qquad u_c'''(z)<0\quad(-q<z<0).}
$$

The same inequalities extend to the two wall points by the positive endpoint
expressions; the center zero follows from evenness.

## The central metric derivative follows immediately

The already derived inverse-inflection identity gives $u_c''<0$ centrally,
while $u_c'<0$ on the positive half. For
$Q_c=v+(pK/2)(z^2-q^2)u_c$,

$$
Q_c'''=\frac{pK}{2}[(z^2-q^2)u_c'''+6z u_c''+6u_c']<0
\qquad(0<z<q).
$$

Every summand has strictly negative sign. Reflection gives the other half.
The simple center zero remains justified by the explicit negative
$Q_c''''(0)$ formula in the master proof. Thus the central four-contact
bound and mixed-wall parity improvement require no Bernstein certificate.
