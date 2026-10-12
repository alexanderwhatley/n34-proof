# Two elementary orders of the exponent sums

The family is

```math
F=A_0+A_1x^a(1-x)^{-b}-B_0x^e(1-x)^d-B_1x^c(1-x)^{-f},
```

where all four coefficient magnitudes are positive, $`0<e<a<c`$, $`0<f<b`$, and $`d>0`$. Put $`S=(0,a-b,e+d,c-f)`$. The label string $`0123`$ means $`S_0<S_1<S_2<S_3`$; it is an order of exponent sums, rather than an order of polynomial roots.

Use the actual signed cubic cofactors $`e_i`$ and contact determinant $`K`$. A physical root means a root in $`(0,1)`$; an exterior root lies outside $`[0,1]`$. A monotone anchor pair allows two pole-free Rolle steps. On $`j`$ useful components, the reduced original equation has at most the useful contact count plus $`j`$ roots. These definitions and identities are the same as in [the disjoint-contact lemma](disjoint-contact-exclusion.md).

In this normalization, S_0<S_2 and S_1<S_3 always. Hence there are exactly six strict possible total-degree orders. Both original endpoint signs of K are negative.

If the order is (0,1,2,3) or (1,0,3,2), the total-degree Vandermonde is positive. Thus K has two exterior roots and at most four physical roots, by the endpoint signs and the degree-six leading coefficient.

All four F3 cofactor endpoint signs reverse: at zero they are (-,-,+,+), and at one (+,+,-,-). In total order (0,1,2,3), the cubic e_0 has negative leading coefficient, whereas e_0(0)<0<e_0(1). It therefore has one root on each exterior half-line and at most one physical root. In total order (1,0,3,2), the same statement holds for e_1.

In either case use the monotone anchor {2,3}, with complementary useful pair {0,1}. Both endpoints are useful. One of the two cofactors has at most one physical root, the other at most three. Hence there are at most (1+3+2)/2=3 useful components. The residual has at most 4+3=7 roots, giving at most nine original roots and thus eight distinct roots after parity/regularization.
