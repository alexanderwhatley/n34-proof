# A negative metric-root certificate for the full one-positive-wall model

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Let P>1, 0<Q<1, B=r(1+r), H=P(P-1)r^2-2PQr+Q(Q-1), j=Q-(P-1)r, and let R be any cubic with all four coefficients strictly positive. Write Y=R-B. At every finite actual entropy level the positive graph u_C solves

u_C'=j u_C(1-Pu_C)/(B+Hu_C),

and its curvature numerator is D_C=B+Hu_C-R. Let xi>0 be the unique positive H root. Define

t=(1-Q)/P.

**Theorem.** If R has a negative real zero -A with **t<=A<=1**, then D_C has at most **six positive zero weights**, counted with analytic multiplicity. This holds for both strict wall signs and for the unit wall. In a geometric positive-support chart to which the two weighted normal Rolle reductions apply, it supplies the original weighted-eight bound.

This is a sufficient source criterion, not a proof that every ONE-EDGE source satisfies it.

## Nonunit proof

Let

W=R(Y'H-YH')-Yj(H-PY),  deg W<=6.

The closed endpoint theorem supplies curvature-six whenever w0=W(0)<=0 or the degree-six coefficient w6<=0. It remains to treat w0,w6>0, so W has degree exactly six and is positive at both negative infinity and zero.

At a negative zero -A of R one has Y(-A)=-B(-A). Consequently

W(-A)=B(-A) j(-A)[H(-A)+P B(-A)].

The two exact factors are

H+PB=(Pr-Q)(Pr-Q+1),

B(-A)=A(A-1),   j(-A)=Q+(P-1)A>0.

If t<A<1, then B(-A)<0 and both factors of H(-A)+PB(-A) are negative, so W(-A)<0. There is therefore a negative root of W on each side of -A, and total negative root weight is at least two.

If A=t or A=1, then W(-A)=0. The total negative root weight is even because W has equal positive signs at negative infinity and zero and is nonzero at those two endpoints. The negative zero at -A thus again forces total negative weight at least two. This uses ordinary real-analytic sign parity and covers all multiple roots without perturbation.

A degree-six polynomial with at least two negative zero weights has at most **four positive zero weights**. On each of the two whole positive wall intervals the analytic secant ODE identity gives a positive integrating factor mu satisfying

(mu(u_C-Y/H))'=-mu W/(H^2 R).

The denominator is positive because R>0 and H!=0. There is at most one ordinary weighted Rolle contribution to the root count per interval, giving at most four forcing weights plus two payments, hence **six graph-contact weights** in total. Multiplication by H preserves their orders, and the nonunit wall itself is not a zero because D_C(xi)=-Y(xi)!=0. This proves the result for either nonunit wall sign.

## Unit wall

When Y(xi)=0, the exact wall-deflation theorem already gives curvature-six for every positive-coefficient cubic R. No negative metric-root condition is needed for that part. Combining the cases proves the stated theorem at every wall ratio.

## Geometry and practical scope

For the usual positive-support affine chart,

R=(d1+r d3)(a1+r a3)(b1+r b3)/gamma^2,  di=ai+bi,

gamma=a3 b1-a1 b3>0,

all its roots are real and negative, with root distances

A_d=d1/d3, A_a=a1/a3, A_b=b1/b3.

Thus **any one** of these three metric ratios in [(1-Q)/P,1] certifies the theorem. Neither a central source band nor the sign of Y(xi), nor a negative-wall residue sign, is required. Identification of the full original nongeneric ONE-EDGE scope remains a separate geometric question.

## A shorter route for the low-band region

The preceding degree budget also shortens the separately h<=l<=1 low-band proof. Its exact test at the negative root of Y establishes at least two negative root weights of W; immediately, W has at most four positive forcing weights and the two whole-interval Rolle payments give curvature-six. The exterior-two theorem is unnecessary for that regional global conclusion.
