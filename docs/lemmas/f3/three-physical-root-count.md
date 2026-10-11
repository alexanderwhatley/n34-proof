# An allocation-free proof of the uniform F3-THREE theorem

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

This is a shorter proof of the retained scalar theorem at its original
scope. It removes the five eight-level allocation rows and the eleven
alpha/beta sign-cell checks as proof selectors. It does not strengthen the
theorem, retire the F3-THREE input itself, or prove the open generic F3
height envelope. Three coarse placement regions are used; the last region
has two sign orientations. The four historical placement labels remain
coverage labels, not four deleted original manuscript cases.

## 1. The theorem and its exact original-source application

Let

$$
P=(x-p)(x-u)(x-v),\qquad Q=\prod_{i=1}^3(x-q_i),
 \qquad 0<p<1<u<v,\quad 0<q_1<q_2<q_3<1,
$$

with disjoint roots, and let alpha>beta>0 and kappa>0. Then

$$
Z_{(0,1)}\bigl(Q-\kappa x^\alpha(1-x)^{-\beta}P\bigr)\le6
\tag{1}
$$

for distinct roots.

The actual oriented-II F3 source is

$$
F=A_0+A_1m_1-B_0m_2-B_1m_3,
 \quad m_1=x^a(1-x)^{-b},\quad m_2=x^e(1-x)^d,
 \quad m_3=x^c(1-x)^{-f},
$$

where all four magnitudes are positive,
0<e<a<c, 0<f<b, d>0, and
0<e+d<a-b<c-f. The retained actual E2 geometry supplies the P in
(1). If E1 has three physical roots, Qraw=E1,
alpha=a-e, beta=b+d, kappa_raw=A1/B0. If E3 has three physical
roots, Qraw=-E3, alpha=c-e, beta=d+f, kappa_raw=B1/B0.
Praw=-E2. Their positive leading coefficients are

$$
L_P=(a-b)(c-f)[(c-f)-(a-b)],
$$

$$
L_{E1}=(e+d)(c-f)[(c-f)-(e+d)],\qquad
 L_{-E3}=(a-b)(e+d)[(a-b)-(e+d)].
$$

Normalizing both cubics once gives kappa=kappa_raw LP/LQ. This is
one actual original coefficient ratio on every component. Two zero-free
original anchor operations lose at most two roots, so (1) gives at most
eight original roots. The retained original regularization/reflection
and boundary-transfer arguments are unchanged. No auxiliary-root
multiplicity persistence or new boundary theorem is asserted here.

## 2. One cumulative-residue lemma and one symbolic tail bound

We use the elementary Stieltjes variation lemma from the retained proof:
if S is a bounded step function on [0,infinity) with k sign changes
after zero intervals are removed, then

$$
\int_0^\infty S(r)(t+r)^{-2}\,dr
$$

has at most k zeros, including multiplicity. For completeness, induction
uses

$$
\frac d{dt}\left[(t+c)^m\int_0^\infty
 \frac{R(r)}{(t+r)^m}\,dr\right]
 =m(t+c)^{m-1}\int_0^\infty
 \frac{(r-c)R(r)}{(t+r)^{m+1}}\,dr.
$$

Choosing c at the first sign change reverses the first block and merges
it with the second. Rolle proves the induction; all tails are O(r^-2).
For a rational sum sum c_j/(t+r_j), exact integration identifies S
with the cumulative sums of its ordered residues. Coincident sites are
combined and zero cumulative sums removed.

Set

$$
\phi=\log|Q/P|-\alpha\log x+\beta\log(1-x),
 \qquad \Lambda=\log\kappa.
$$

Only PQ>0 is useful. The x-pole residues of phi' are -alpha at 0,
beta at 1, +1 at each qi, and -1 at p,u,v. Under
x=(L+Rt)/(1+t), their cumulative order is: left endpoint and
left poles in decreasing x order; virtual infinity; right poles in
decreasing x order. The virtual residue is alpha-beta.

The only three-contact bound needed below has a nonnegative initial
cumulative block followed by

$$
2-\alpha,\quad 2-\beta,\quad 1-\beta,\quad-\beta.
\tag{2}
$$

There may be final zeros and another negative entry. Since alpha>beta,
the first of these is smaller than the second; after the second the
sequence strictly decreases and ends negative. Inserting the first
entry can add at most two sign changes to this final positive-to-negative
pass. Thus the complete sequence has at most three sign changes. No
alpha/beta threshold-cell dispatch is needed, including equality at
alpha=2 or beta=1,2.

For p<q1 the first two useful intervals have cumulative sequences

$$
[-\alpha,-\beta,-\beta-1,-\beta-2,-2,-1,0,1],
$$

$$
[1,0,-\alpha,-\beta,-\beta-1,-\beta-2,-2,-1],
\tag{3}
$$

so each has at most one stationary phase point.

For q1<p<q2, the first two useful intervals are strictly decreasing by
direct pole pairing. On (0,q1), pair q1 with p, q2 with u, q3 with
v; each +Q pole dominates its paired negative P pole. On (p,q2),
pair q1 with p again, now both on the left, and retain the other two
pairs on the right. The endpoint terms are strictly negative. The last
useful interval has cumulative sequence

$$
[1,2,1,2,2-\alpha,2-\beta,1-\beta,-\beta],
\tag{4}
$$

and hence at most three contacts by (2). Consequently its level counts
are at most 1+1+4=6, proving this entire middle placement region.

For p>q2, the first useful interval (0,q1) is likewise strictly
decreasing, so it has exactly one intersection with each finite level.
The useful interval on the Q side of the adjacent pair p,q3 has at
most three contacts. Its cumulative sequence is, respectively,

$$
[1,0,1,2,2-\alpha,2-\beta,1-\beta,-\beta]
 \quad(p<q3),
$$

$$
[1,2,2-\alpha,2-\beta,1-\beta,-\beta,0,-1]
 \quad(q3<p).
\tag{5}
$$

Both obey the same tail bound (2).

The contact polynomial is

$$
T=\rho(Q'P-QP')+[(\alpha-\beta)x-\alpha]PQ,
 \quad \rho=x(1-x),\qquad \phi'=T/(\rho PQ).
$$

It has degree seven and leading coefficient alpha-beta>0. At the
two exterior P roots, T(u)<0<T(v), so at least one degree is
nonphysical. Physical contact weight is therefore at most six.

When p<q1, T(q2)<0<T(q3) forces one contact in the non-useful
Q/Q gap. When p>q2, the same argument gives one in (q1,q2).
Thus useful contact weight is at most five in these two regions.
Weighted Rolle on at most three occupied useful components gives at most
eight generic level intersections.

Suppose eight transverse intersections occur. Rolle exhausts all five
useful contacts and forces all three useful components to be occupied.
Every useful contact is simple, and every one is between consecutive
level intersections in its own component. The non-useful contact and
the exterior witness account for the remaining two degrees of T.
In particular no extra contact can occur before the first or after the
last intersection on an occupied component.

For p<q1, the one-contact bounds (3) and even endpoint parity of the
first two components force two intersections in each; the right
component therefore has four intersections and three contacts.

For p>q2, the first component contributes one intersection and no
contact. The last two components therefore contribute seven
intersections and exactly five contacts. The Q-side component has equal
-infinity endpoint limits, so its nonempty level count is even. By (5)
it has at most four intersections. Hence it has an extremum, and the
P-side component has at least three intersections and also an extremum.
This is the entire allocation step: no five-row list is selected.

## 4. A common-height gap exhausts an adjacent quintic

For the adjacent Q root s, put

$$
\widetilde P=(x-u)(x-v),\qquad \widetilde Q=Q/(x-s),
$$

$$
H=\log|\widetilde Q/\widetilde P|-
       \alpha\log x+\beta\log(1-x),
$$

$$
N=\rho(\widetilde Q'\widetilde P-
         \widetilde Q\widetilde P')+
       [(\alpha-\beta)x-\alpha]\widetilde P\widetilde Q.
$$

Then

$$
H'=N/(\rho\widetilde P\widetilde Q),\quad
 \phi=H+\log\left|\frac{x-s}{x-p}\right|,
$$

$$
T=(x-p)(x-s)N+(s-p)\rho\widetilde P\widetilde Q,
 \qquad \deg N=5,\quad [x^5]N=\alpha-\beta>0.
\tag{6}
$$

### Left adjacent gap, p<q1

Choose s=q1, U the left component's minimum and V the middle
component's maximum. Then U<p<s<V<q2 and
phi(U)<Lambda<phi(V). H is smooth on (0,q2). Its two forced roots
z1,z2 lie in (U,V); the signs at q2,q3,1,u,v force the other three:

$$
U<z_1<z_2<V<q2<z_3<q3<z_4<1<u<z_5<v.
\tag{7}
$$

These exhaust degree five and are simple.

On (q3,z4), N>0 and H'>0, so phi'>0. On (z4,1), let

$$
M=-\frac{(x-p)(x-s)H'}{s-p}>0.
$$

Phase contacts are M=1. The logarithmic derivative has positive
residues at p,s,z1,...,z5 and negative residues at 0,1,u,v,q2,q3.
The pairs (p,0), (z3,q2), (z4,q3), and (z5,u) each contribute
strictly positively on (z4,1). Every unpaired contribution is also
positive. Thus M is strictly increasing and the right component has
at most one contact, contradicting its required three.

### Right adjacent gap, p>q2

Choose s=q3. This one gap handles both remaining placements. Write
r_mid and r_right for the contact counts on its two useful components.
Section 3 gives r_mid+r_right=5.

If p<s, choose U the last middle minimum and V the first right
maximum. They are respectively the last and first contacts of those
components; q2<U<p<s<V<1 and phi(U)<Lambda<phi(V).
The two height-forced roots plus N(q1)<0<N(q2), N(U)<0 and
N(u)<0<N(v) exhaust the quintic in the order

$$
q1<z_1<q2<z_2<U<z_3<z_4<V<1<u<z_5<v.
\tag{8}
$$

All middle contacts lie in I=(z2,min(p,z3)). There M is positive
for M=-(x-p)(x-s)H'/(s-p), and phase contacts are M=1.
Moreover x(log M)' is strictly decreasing. To see this directly,
pair the numerator poles z1,z2 with denominator poles q1,q2;
pair numerator poles p,s,z3 with denominator poles 1,u,v;
the unpaired positive poles z4,z5 are to the right of I, and the
unpaired negative pole is 0. Every paired term in x(log M)' is
strictly decreasing, as are the two unpaired positive terms; the 0
term is constant. Thus M'=0 at most once and r_mid<=2.

All right contacts lie on [V,1), where (log M)'>0. Pair
(p,0), (z1,q1), (z2,q2), and (z5,u); every remaining term is
positive. Hence r_right<=1. Both bounds apply at the same time:
r_mid+r_right<=3, contradicting five. Neither possible old
eight-level allocation is used.

If s<p, choose U the last middle maximum and V the first right
minimum. Then q2<U<s<p<V<1 and phi(U)>Lambda>phi(V).
The signs and common-height comparison exhaust N as

$$
q1<z_1<q2<U<z_2<z_3<V<z_4<1<u<z_5<v.
\tag{9}
$$

Set M=(x-s)(x-p)H'/(p-s). On (q2,U], (log M)'<0:
the negative terms dominate the positive terms in the pairs
(q2,z1), (1,p), (u,z4), and (v,z5); every remaining term is
negative. Thus r_mid<=1.

All right contacts lie in I=(max(p,z3),z4), where M>0. Its
logarithmic derivative has the same seven positive and six negative
pole residues as above, now with denominator q1,q2. On the left of
I, the four poles p,s,z2,z3 have the same +1 residue, so their
internal ordering cannot affect cumulative sums. Their common collection,
the fixed q2,z1,q1,0 collection, virtual infinity, and the fixed v,z5,u,1
collection give exactly

$$
[1,2,3,4,3,4,3,2,1,0,1,0,-1].
\tag{10}
$$

There is one sign change. The cumulative-residue lemma gives at most
one zero of (log M)', hence r_right<=2. Again both bounds apply
simultaneously and r_mid+r_right<=3, contradicting five. No six
interleavings of same-residue poles are checked or selected.

Eight generic level intersections are now excluded in every placement
region. The scalar residual is negative near both endpoints, so its
transverse root count is even and at most six.

## 5. Distinct roots and the exact replacement scope

For nongeneric finite distinct scalar roots, make one sufficiently small
common shift of Lambda. If o selected roots have odd order and e+,e-
selected roots have even order with opposite local signs, one of the
two shifts gives at least o+2max(e+,e-) roots, at least the number
selected. Avoiding the finitely many physical critical values of phi
makes the shifted roots transverse. A hypothetical seven distinct roots
would therefore yield at least eight transverse roots by endpoint
parity, already excluded. This proves (1).

The retained Session22 source lists exactly these five live allocations:
(2,2,4) in PQQQ; (1,3,4),(1,5,2) in QQPQ; and
(1,2,5),(1,4,3) in QQQP. The present proof replaces that entire
allocation-selection step by one exhausted contact budget and the
simultaneous collection bounds above. It also replaces eleven alpha/beta
sign cells by the symbolic cumulative tail (2). The four placement
labels still describe the scalar geometry, and the two orientations in
the right-gap argument still require their stated sign proofs. The
original manuscript's single F3-THREE theorem reference is unchanged.

No prior artifacts or manuscript bytes were edited.
