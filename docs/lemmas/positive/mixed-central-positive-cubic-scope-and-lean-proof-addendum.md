# The mixed Bernstein proof needs only positive cubic coefficients

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

The mixed central-three proof extends from negative-rooted positive cubics to EVERY cubic R=R0+R1 r+R2 r^2+R3 r^3 with Ri>0. No new entropy or forcing argument is needed. The root factorization used in the original positive-sum proof can be replaced by two short coefficient identities.

Retain its wall/projective notation eta<xi, Delta=xi-eta,

$$
G(x)=(1+x)^3R\left(\frac{\eta+\xi x}{1+x}\right)
=g_0+g_1x+g_2x^2+g_3x^3.
$$

All gi>0, and direct expansion gives

$$
g_2-g_1=\Delta[R_1+(\eta+\xi)R_2+3\eta\xi R_3]>0,
$$

$$
g_3+g_1-g_2-g_0=\Delta^3R_3>0.
$$

For strict mixed walls g0>a=B(eta) and g3<b=B(xi), define

$$
E=(g_3+g_1)^2-(g_2+g_0)^2>0,
$$

$$
J=(g_2+g_0)^2+2g_1g_3-g_1^2
=(g_2-g_1)(g_2+g_1)+2g_0g_2+g_0^2+2g_1g_3>0.
$$

The original normalized four-term decomposition is equivalent to

$$
\boxed{g_3(C_2+C_4)
=b g_3(b-g_3)+bE+(b-g_3)J
+g_3(g_0-a)(4g_2+g_0+a)>0.}
$$

Every term has a strict positive sign. This proves C2+C4>0 directly from the original cubic coefficients, without negative roots, elementary symmetric root functions, or a computer-algebra sign certificate.

The seven forcing coefficient identity is already algebraically universal. Thus its positive C0,C1,C3,C5 and this sum still give at most three variations when C6 is unrestricted. The full central ODE comparison and opposite wall phases prove at most three weighted central contacts. The mixed exterior proof also uses only R0,R3>0, the opposite strict wall signs, and the source residues; it is unchanged. Hence the abstract mixed comparison has at most 2+3+1=6 total contact weights, for every positive-coefficient cubic R, one actual entropy C, and P,Q>1.

Reflection gives the opposite mixed-wall orientation. This addendum changes no previously file and enlarges only the abstract source-cubic scope; the geometric original-eight strong-fork corollary already lies in that scope.
