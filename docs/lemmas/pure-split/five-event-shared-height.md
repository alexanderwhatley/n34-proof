Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Literal joint-height theorem

Let the actual strict canonical mixed supports satisfy

$$
a_1<0<a_2<a_3,\qquad b_3<0<b_1<b_2.
$$

Use w=x(1-x), D=w d/dx, h_i=x^{a_i}(1-x)^{b_i},
lambda_i=a_i-(a_i+b_i)x, J=lambda2-lambda1, L=lambda3-lambda2.
In particular L>0 on (0,1). Retain the actual source polynomials

$$
\begin{aligned}
P_1&=(D\lambda_2)J-\lambda_2(\lambda_1J+DJ),\\
P&=P_3=\lambda_2(\lambda_3L+DL)-(D\lambda_2)L,\\
G&=(\lambda_3-\lambda_1)JL+(DL)J-(DJ)L.
\end{aligned}
\tag{1}
$$

Assume P has three simple physical roots and P1,P have no common
physical root. P1 automatically has two simple physical roots. Put

$$
F=-\frac{h_1P_1}{h_3P},\qquad W=\frac{h_1G}{P}.
\tag{2}
$$

**Joint-height theorem.** Every fixed positive rho level of F has at
most seven physical contact weights. If it has seven transverse contacts
r1<...<r7, then there is no real
threshold tau such that

$$
W(r_i)<\tau\quad(i\text{ odd}),\qquad
W(r_i)>\tau\quad(i\text{ even}).
\tag{3}
$$

The theorem retains two actual coupled profiles. G's physical root
count, multiplicities and interlacing are unrestricted. There is no
origin-quadratic wall restriction. The four old five-event order labels,
21 canonical allocation labels and 39 phase-tagged entries do not
select a proof step. Exact source reflection covers the opposite
mixed cone.

## 1. Exact critical identities and the five-weight budget

The source identities are

$$
LP_1+JP=\lambda_2G,
\tag{4}
$$

$$
(DP_1)P-P_1DP-(\lambda_3-\lambda_1)P_1P
=\lambda_2 K_6,
\qquad \deg K_6\le6,
\tag{5}
$$

$$
(DP-\lambda_1P)G-PDG=-L K_6.
\tag{6}
$$

They give

$$
DF=-\frac{h_1\lambda_2K_6}{h_3P^2},\qquad
DW=\frac{h_1 L K_6}{P^2}.
\tag{7}
$$

Define K_F=lambda2 K6. The earlier proof four-weight budget says
that when the actual mixed P has three physical roots, K6 has at most
four physical weights. Its proof uses equal nonzero negative endpoint
signs and the common exterior-witness theorem, which excludes
full-six physical exhaustion even with repeated critical roots.

Because lambda2 has its one simple physical zero at c, polynomial
divisor multiplicities add, and therefore

$$
Z_{(0,1),\mathrm{mult}}(K_F)\le5.
\tag{8}
$$

This count includes the mandatory c weight, including the possibility
that K6 also vanishes there. No critical simplicity is assumed at this
stage. It is a local actual-mixed-source budget, not a global F3 bound.

## 2. One event-count argument exhausts the entire budget

The actual source endpoint signs are P1(0),P1(1)>0 and
P(0)>0>P(1). At c, P1(c)<0<P(c). Degree at most three and these signs
give exactly two simple physical P1 roots rA<c<rB. The undivided
identity

$$
P=\lambda_2\lambda_3L+w(a_3b_2-a_2b_3)
$$

gives P>0 on (0,c], so all its physical roots lie to the right of c.
Thus the first of the five combined simple P1/P events is rA, and
the first positive F component contains c.

F is negative at the physical left end and positive at the right end;
its sign flips at each of the five events. Hence it has exactly three
positive components and two bounded negative event gaps. The endpoint
pairs of these negative gaps use the remaining four events: the other
P1 event rB and the three P events. Exactly one pair consists of two
P poles; the other pair is mixed. This deduction needs no four-word
event table.

On the negative P/P gap, 1/F is analytic and finite, strictly negative
inside, and continuous with value zero at both endpoints. P1 does not
vanish there. Rolle gives a root strictly inside this gap, where F and
1/F are finite and nonzero and their derivatives vanish together. Formula
(7) therefore gives an interior K_F root, distinct from every
positive-component contribution. The endpoint poles themselves are not
counted: at a simple P event, (5) gives K_F=-P1 DP, which is nonzero.

More generally, select any finite collection of F=rho contacts with
total weight N, on ell<=3 occupied positive components. Weighted Rolle
on those components supplies N-ell K_F weights. The negative P/P gap
supplies one further, disjoint weight. Hence

$$
N-\ell+1\le Z_{\mathrm{mult}}(K_F)\le5,
\qquad N\le\ell+4\le7.
\tag{9}
$$

This proves the weighted seven-contact ceiling without an EHT count or
endpoint parity. With seven known transverse contacts all are accounted
for, ell=3, and K_F has exactly five physical weights.
Every positive contact gap contains exactly one simple K_F root; the
negative P/P gap contains the remaining simple root. All the budget is
exhausted. In particular, the first positive component is occupied.

The mandatory c root is in that first positive component. If c lay
outside the span of its contacts, it would be an additional sixth
critical root. It cannot be a transverse contact, since DF(c)=0 by (7). Consequently
consecutive global contacts u=r_i and
v=r_(i+1) satisfy

$$
u<c<v,
$$

and c is their unique K_F root. In particular K6(c) is nonzero.

On the first positive component P>0, and

$$
R_\rho=h_1P_1+\rho h_3P=h_3P(\rho-F).
\tag{10}
$$

R_rho is positive near zero and its seven roots are transverse, so
its sign on (r_i,r_(i+1)) is (-1)^i. There are no additional R roots: the weighted seven-contact ceiling
in (9) has already exhausted all R roots.

Thus on (u,v), F-rho has sign (-1)^(i+1). If i is odd, c is F's
unique maximum there; DF is positive to its left and negative to its
right. If i is even, c is the unique minimum and these signs reverse.

The exact Legendre relation from (7) is

$$
DW=-\frac{h_3L}{\lambda_2}\,DF.
\tag{11}
$$

Its slope factor is negative left of c and positive right of c.
Although that factor has a pole, DW is regular by the second formula
in (7). Therefore W strictly decreases across the whole (u,v) when
i is odd and strictly increases when i is even. In either case,

$$
\operatorname{sgn}(W(v)-W(u))=(-1)^i.
\tag{12}
$$

But (3) demands W(v)>tau>W(u) for odd i and W(v)<tau<W(u) for even
i. Both contradict (12). This proves the joint-height theorem.

## 4. Exact application to the original coefficient-height window

For the original row

$$
f=1-E_1h_1-E_2h_2-E_3h_3,\qquad E_i>0,
$$

the retained projective entry fixes

$$
\rho=E_3/E_1>0,\qquad\kappa=E_1>0,
\quad B=h_1J-\rho h_3L,
\quad X=\lambda_2/B,
\quad M=-\lambda_2+\kappa B.
\tag{13}
$$

These are the actual original coefficients; rho and kappa are not
varied independently along contact nodes. Ten original simple roots
force seven transverse R_rho roots and the nine-hit auxiliary ratio equality,
on its retained generic chart. This entry excludes shared physical P1/P events and the relevant B/R
coincidences. Transversality also excludes contacts at c directly by (7).

The equality window has X(r_i)>kappa at useful odd nodes, and
0<X(r_i)<kappa at every even node. In the three-pole phase there may
be one non-useful node; it is odd and has X(r_i)<0. There are no other
exceptions. These are exactly the retained source s082 Section2
premises; they hold for both signs of B(c).

At each R node, (4) and P1=-rho h3 P/h1 give the UNDIVIDED identity

$$
\lambda_2G=P B/h_1.
$$

Since c is not a node, it follows that

$$
W(r_i)=B(r_i)/\lambda_2(r_i)=1/X(r_i).
\tag{14}
$$

Every useful odd node therefore has W(r_i)<1/kappa. The possible
non-useful odd node also has W(r_i)<0<1/kappa. Every even node has
W(r_i)>1/kappa. Thus the SAME threshold tau=1/kappa gives (3),
contradicting the joint-height theorem. This handles the non-useful
node without a separate height or pole phase table.

All strict generic five-event original equality configurations are
therefore excluded. The original-function aggregate
regularization and compact sign-bracket transfer retain the finite
nonidentity distinct-root conclusion on original support/coefficient
boundaries. No raw auxiliary multiplicity transfer at those boundaries
is inferred. The three-event, nested and DR modules
retain their separate literal scopes.
