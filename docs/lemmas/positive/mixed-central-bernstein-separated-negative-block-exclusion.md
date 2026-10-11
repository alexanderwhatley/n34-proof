# Mixed central Bernstein coefficients have no separated negative blocks

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

This is a universal analytical lemma for a negative-rooted positive cubic. It does not assume numerical evidence, antichain ordering, or a bound on the high-wall ratio. Its application to a forcing root count also requires the surrounding Bernstein coefficients to have the appropriate signs.

Let

$$
0<\eta<\xi,\qquad a=\eta(1+\eta),\quad b=\xi(1+\xi),
\qquad R(r)=k\prod_{i=1}^3(r+A_i),\quad k,A_i>0.
$$

Assume the mixed-wall inequalities $R(\eta)>a$ and $R(\xi)<b$. Write

$$
(1+x)^3R\left(\frac{\eta+\xi x}{1+x}\right)
=g_0+g_1x+g_2x^2+g_3x^3.
$$

Define

$$
C_2=g_1^2+2g_2(g_0-2a)-a^2-2ab-(\xi-\eta)^2,
$$

$$
C_4=b^2+2ab+(\xi-\eta)^2+2g_1(2b-g_3)-g_2^2.
$$

Then $C_2+C_4>0$. In particular these two coefficients cannot both be negative, or both be zero.

To prove this, put

$$
z_i=\frac{\eta+A_i}{\xi+A_i}\in(0,1),\quad
e_1=z_1+z_2+z_3,\quad e_2=z_1z_2+z_1z_3+z_2z_3,\quad p=z_1z_2z_3,
$$

$$
s=\frac{g_3}{b}\in(0,1),\qquad m=\frac ab.
$$

The transformed source has $g_0=sbp$, $g_1=sb e_2$, $g_2=sb e_1$, $g_3=sb$, so the left-wall inequality is $sp>m$. Introduce

$$
D=\prod_{i=1}^3(1-z_i^2)>0,\qquad
J=(e_1+p)^2+2e_2-e_2^2>0.
$$

The latter sign follows from $e_1>e_2>0$, since

$$
2(e_1-e_2)=\sum_{i=1}^3 z_i(2-z_j-z_k)>0
$$

with $\{i,j,k\}=\{1,2,3\}$. The exact identity

$$
\boxed{\frac{C_2+C_4}{b^2}
=(1-s)+sD+s(1-s)J+(sp-m)(4s e_1+sp+m)}
$$

finishes the proof: every displayed term on the right is positive. The identity uses

$$
D=(1+e_2)^2-(e_1+p)^2.
$$

Consequently a degree-six coefficient sequence with positive entries at positions 0,1,3,5,6 and these entries at positions 2,4 has at most two sign variations after zero coefficients are deleted. Descartes' rule then gives at most two positive roots, counted with multiplicity. This final sentence is conditional on the five surrounding coefficient signs, and does not independently establish those signs for an arbitrary forcing polynomial.
