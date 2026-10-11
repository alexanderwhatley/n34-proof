# References

## Problem and prior results

Tien-Yien Li, J. Maurice Rojas, and Xiaoshen Wang, *Counting Real Connected Components of Trinomial Curve Intersections and m-nomial Hypersurfaces*, 2003, [arXiv:math/0212178](https://arxiv.org/abs/math/0212178). Definition 1 gives the counting conventions; Theorem 1 proves $N(3,3)=5$ and $N(3,m)\le2^m-2$, hence $N(3,4)\le14$.

Joel Gomez, Andrew Niles, and J. Maurice Rojas, *New Complexity Bounds for Certain Real Fewnomial Zero Sets*, 2007 preprint, [arXiv:0709.2405](https://arxiv.org/abs/0709.2405). Theorem 1 supplies a three-term/four-term system attaining seven positive roots, giving $N(3,4)\ge7$.

Boulos El Hilany and Sébastien Tavenas, *Improved fewnomial upper bounds from Wronskians and dessins d'enfant*, 2024 preprint, [arXiv:2409.01651](https://arxiv.org/abs/2409.01651). Theorem 1.1 and Table 1 give an upper bound of eleven for the three-term/four-term case. The same paper supplies the polynomial estimate used below.

## External theorems used in the proof

Boulos El Hilany and Sébastien Tavenas, *Improved fewnomial upper bounds from Wronskians and dessins d'enfant*, 2024, [arXiv:2409.01651](https://arxiv.org/abs/2409.01651).

The proof uses the following consequence, labeled **[EHT]** in the mathematical documents. For nonzero real polynomials $P,Q$ and real exponents $\alpha,\beta$, the function

$$
P(x)+x^\alpha(1-x)^\beta Q(x)
$$

has at most $\deg P+\deg Q+2$ distinct zeros in $(0,1)$ unless it is identically zero. Cases where one polynomial vanishes identically are handled directly. If a common polynomial factor is removed, its distinct roots must be accounted for separately.

This is an external mathematical input. The repository states precisely the result it uses; it does not claim to supply a new proof of that external theorem. The statement, rather than a theorem number that varies between versions, identifies the input.

Alexander Dyachenko, *Total nonnegativity of infinite Hurwitz matrices of entire and meromorphic functions*, 2013, [arXiv:1304.0801v1](https://arxiv.org/abs/1304.0801). The specific input is Theorem 1.4, with the matrix convention in equation (1.5).

The proof uses its polynomial consequence: for coprime real polynomials $p,q$, with $p(0)=1$ and $q(0)\geq0$, a ratio $q/p$ that maps the upper half-plane into itself and is regular and nonnegative on the nonnegative real axis yields the corresponding totally nonnegative Hurwitz-type coefficient matrix. “Coprime” means that the two polynomials have no common nonconstant factor. “Totally nonnegative” means that every finite minor is nonnegative. The matrix has alternating coefficient rows from $q$, $zp$, $zq$, $z^2p$, and their further shifts.

The supporting argument applies this with $p=e/e(0)$ and $q=d/e(0)$, where $e/d$ is a positive sum of fractions $a_j/(z+s_j)$ with $a_j,s_j>0$. The relevant ratio is therefore $d/e$. The appendix's fractional-power argument explains how this matrix result gives the required zero bound, including strictness and the constant-function exception. That application is part of the included proof, rather than an additional unnamed external input.

## Origins of the documents

The included mathematical arguments come from *N34 Proof Simplification Revision 5*, dated 5 October 2026, its accompanying proof sources, and the continuation sources. They are organized as one proof, with the common argument in the main document and the detailed supporting inequalities in the appendix and its linked lemma proofs.

The upper bound has both analytic arguments and exact positive-sum polynomial identities. The lower bound uses the exact terminating-decimal example printed in the main proof and interval enclosures establishing alternating signs.

The original proof uses short reference labels such as **F2**, **F3**, **F4**, **SUPPORT**, and **EASY**. They identify specific lemmas or cases, not additional assumptions. Their definitions and actual statements are given in the main proof and appendix. The appendix links those statements to the supporting mathematical files included here.

Regional lemmas retain their precise hypotheses and are applied only on the stated parameter regions. The proof includes the arguments covering all remaining configurations.
