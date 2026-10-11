# Every strict-low positive cubic has at most four central contacts

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Fix P,Q>1, let

$$
H=P(P-1)r^2-2PQr+Q(Q-1)
$$

have positive roots eta<xi, and put B=r(1+r). Let R be any cubic with strictly positive coefficients, Y=R-B, and assume Y(eta)>0,Y(xi)>0. For any one actual fixed-entropy graph uC, the normal-curvature equation

$$
B+Hu_C=R
$$

has at most FOUR roots on eta<r<xi, counted with analytic multiplicity. The statement permits comparable supports and does not require three real negative roots of R, coordinate antichain order, canonical source topology, or a physical source-seam component assumption.

Write

$$
G(x)=(1+x)^3R\left(\frac{\eta+\xi x}{1+x}\right)=\sum_{i=0}^3g_i x^i,
\quad a=B(\eta),\quad b=B(\xi).
$$

All gi>0, g0>a, and g3>b. For the forcing polynomial

$$
W=R(HY'-H'Y)-Y(H-PY)[Q-(P-1)r],
$$

the positive projective transform has coefficient signs

$$
\begin{array}{c|ccccccc}
i&0&1&2&3&4&5&6\\\hline
\operatorname{sign}C_i&+&+&*&*&*&-&-
\end{array}
$$

because C0=(g0-a)(3g0-a)>0, C1=4g1(g0-a)>0, C5=4g2(b-g3)<0, and C6=(3g3-b)(b-g3)<0. The three middle coefficients may have either sign or vanish. From C1 to C5 there are four possible transitions and opposite endpoint signs, so, after zeros are deleted, at most three sign changes occur. C0 and C6 add none. Descartes' rule gives at most three central root weights for W.

Let u0=Y/H and d=uC-u0. The exact ODE comparison reads

$$
d'=L(r)d-\frac{W}{H^2R}.
$$

Its coefficient L is analytic on the entire open central interval, since both ODE denominators B+HuC and B+Hu0=R are positive. This remains valid at a formal u0 outside the probability bounds. A positive integrating factor and weighted Rolle bound the central root weight of d by four. Multiplication by the nonzero H preserves all central contact orders.

For reference, d is positive near both walls: u0 tends to minus infinity from inside the central interval, while uC stays finite. Its total contact weight is therefore even; the possible central totals are 0,2,4. The four-weight bound already suffices for the theorem.

When combined with the canonical exterior-two theorem and the power-tangent height theorem, this contribution to the root count proves six normal-curvature contacts and original eight for canonical low-low sources without an antichain-only global forcing budget: the height theorem empties one outer component, the remaining outer contributes at most two, and the entire central interval contributes at most four.
