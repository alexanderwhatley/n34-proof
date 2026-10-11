# The master height theorem with one least support

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Let m_s(t)=t^(s_1)(1-t)^(s_2), 0<t<1. Assume

0<=s_u<=s_v, 0<=s_u<=s_w componentwise,

with all support coordinates nonnegative. There is NO relative order
assumption between s_v and s_w. Put

S=u-c3 v-c4 w, c3,c4>0.

For every nine ordered interior samples t1<...<t9,

min{S(t1),S(t3),S(t5),S(t7),S(t9)}
 <= max{0,S(t2),S(t4),S(t6),S(t8)}.                    (LSMH)

## Strict source assembly

First suppose s_u has both coordinates positive and each of s_v-s_u and
s_w-s_u has both coordinates positive. Off equality faces, v and w are
either strictly comparable or strictly incomparable. In the comparable
case, exchange v,w and their coefficients if necessary and apply the
comparable master theorem from the earlier proof. In the incomparable
case, reflect and exchange the two positive atoms to write

u=t^A(1-t)^B,
v=t^(A+a)(1-t)^(B+b+q),
w=t^(A+a+p)(1-t)^(B+b),

with all A,B,a,b,p,q>0. The new fork analytical theorem proves LSMH and
the eight-root bound. It uses direct original-function Rolle extraction,
a degree-six Wronskian with opposite endpoint signs, and two geometric
kernels: separated negative bands consume an unavailable critical root;
overlapping bands admit one common log-concave factor and a two-pole
height comparison. The old complete INC theorem, old event atlas, old
post-pole inequality and old dome proofs are not imports.

The strict result at coordinate-order or auxiliary equality faces follows
by original-root or sample perturbation inside the strict least-support
cone. In particular, coincident v,w supports or one coordinate equality
are not a new chamber obligation.

## All weak nonnegative supports

For epsilon>0 replace the supports by

s_u+epsilon(1,1),
s_v+2epsilon(1,1),
s_w+3epsilon(1,1).

These supports have strictly positive coordinates and strictly positive
differences from the least support. The strict assembled theorem applies.
At each fixed interior sample, all monomials converge to the original
ones as epsilon tends to zero. The finite minimum and maximum of their
values are continuous. Passing to the limit proves LSMH. This proof uses
no endpoint limit when a coordinate vanishes.

If a nonidentity weak G had nine distinct roots, choose disjoint compact
neighborhoods and regularize the common constant c1 by a sufficiently
small nonzero shift preserving c1>0. At odd zeros either direction
produces one nearby simple crossing; at even zeros one direction produces
two. Choose the direction splitting the larger even-zero group, so at
least nine simple compact crossings persist. Now perform the strict
support perturbation above. Uniform convergence on the selected compact
brackets preserves every crossing, contradicting the strict at-most-eight
bound. Identity rows have no finite-order isolated-root reduction and are
explicitly excluded from this corollary.

## Exact original proof impact

The main manuscript's comparable and incomparable one-corner branches
can now both call this one statement. Its proof has the four
comparable regional modules and the new two fork geometric kernels.

The earlier proof comparable count remains twelve terminal manuscript routes
absorbed by the theorem interface. The new independent fork proof replaces
the entire original [INC] dependency, whose assembled navigation had six
event-family rows. These six family rows and the twelve terminal routes
are counted at different depths and should not be added as a canonical
global case count.

The mixed NOLOBE/GENUINE, AP, pure-split and other coefficient-sign
branches are not all replaced by LSMH. Separate new affine-line,
convexity and conditional mixed results have their own exact scopes.
