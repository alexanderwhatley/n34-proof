# Reading guide and terminology

The aim is to count solutions of two polynomial equations with very few terms. The difficulty is that the exponents can be very large. A degree bound therefore gives little useful information. The proof instead uses the number of terms and the way their derivatives interact.

The reduction in the main proof gives four positive functions of the form $x^a(1-x)^b$ on $0<x<1$. Their coefficients may have either sign. If all coefficients have the same sign, the sum has no zeros. After changing the overall sign if necessary, the substantive cases are two positive and two negative coefficients, and three positive and one negative coefficient.

The supporting arguments turn a hypothetical excess of zeros into an excess of derivative zeros or tangencies. Polynomial identities and height comparisons then rule out that excess. The example at the end establishes that nine is attainable.

The main proof contains the common argument. The appendix gives the specialized statements, their assumptions, and their longer proofs. A statement with extra assumptions is used only where those assumptions have been established. The reciprocal-coordinate height and regional bounds are included in the appendix, alongside the F3 arguments that cover all remaining parameters.

## Terms used in the documents

Standard mathematical words are retained when they are needed, and their meanings are given here. Each local argument also defines its variables. A letter can have a different meaning in a separately stated lemma; it must be read with that lemma's definitions.

| Term | Meaning here |
| --- | --- |
| Monomial term | A coefficient times a product of powers, such as $cX^uY^v$. |
| Trinomial / quadrinomial | A polynomial with at most three / four nonzero monomial terms. |
| Support | The set of exponent pairs belonging to the nonzero terms of a polynomial. |
| Exponent vector | The ordered pair $(a,b)$ in $x^a(1-x)^b$. |
| Beta monomial; atom in some supporting proofs | The positive function $x^a(1-x)^b$ on $(0,1)$. The word does not introduce an additional object. |
| Nonidentity | A function that is not identically zero. This matters because the zero function has infinitely many zeros. |
| Distinct zeros | Different zero locations, each counted once. |
| Multiplicity; root weight | The order to which a function vanishes. Some derivative arguments count this order even though the final theorem counts distinct solutions. |
| Nondegenerate solution | A solution at which the Jacobian determinant is nonzero. Locally the two equations intersect without tangency. |
| Sign case; coefficient-sign chamber | A case specifying which coefficients are positive and which are negative. For example, $(2,2)$ means two of each. |
| Coordinatewise order | $(a,b)\preceq(c,d)$ means $a\leq c$ and $b\leq d$. |
| Comparable / incomparable vectors | Two vectors are comparable if one is coordinatewise no larger than the other. Strictly incomparable vectors have one coordinate larger and the other smaller. |
| Generic parameters | Parameters avoiding the particular equalities and repeated roots excluded in an argument. The proof separately explains how to pass back to the excluded cases. |
| Boundary; wall; equality face | A parameter equality separating strict cases, rather than a new geometric object. |
| Perturbation | A sufficiently small change in coefficients or exponents. The proof uses it while preserving specified sign changes. |
| Anchor | A selected positive function used to divide the equation or choose a derivative coordinate. |
| Cofactor polynomial | A signed determinant obtained by deleting a column of the derivative matrix, with known nonzero factors removed. Formula (5) in the main proof specifies it. Its zeros divide the intervals used in derivative counts. |
| Core | A polynomial factor remaining after specified factors that never vanish have been removed from an expression. |
| Chart | A change of variables, used together with its stated inverse and domain conditions. |
| Common level | A fixed value of a function being compared across several intervals. |
| Height comparison; height theorem | An inequality comparing function values at different critical points. It prevents too many crossings of a single fixed level. |
| Contact | A point where a curve is tangent to a level or where a derivative vanishes, as defined in the local argument. |
| Useful contact | A contact in an interval contributing to the original zero count, rather than every root of an auxiliary polynomial. |
| Physical root or interval | A root or interval inside the domain corresponding to the original problem. Roots elsewhere may be used in the argument but are not original solutions. |
| Event; event order; event word | A designated root, and the left-to-right order of designated roots. A digit string such as $1320$ lists their labels in order; it is not a number. |
| Cap | An upper bound on a count. The documents prefer the phrase “at most” when possible. |
| Source | The original linked functions or polynomials from which an auxiliary calculation is derived. Their relations cannot be dropped when applying a lemma. |
| Gate | A necessary inequality restricting the parameters. It is an assumption or consequence to establish, not a proof by itself. |
| Head | A specified coefficient of a polynomial, commonly one near its highest-degree term. The local formula identifies the coefficient. |
| Newton inequalities | Inequalities between consecutive elementary symmetric functions of positive numbers. They supply necessary conditions when all roots in question are positive. |
| Discriminant | A polynomial in the coefficients detecting repeated roots; for a real cubic, a negative discriminant means one real root and two nonreal conjugate roots. |
| Positive-sum identity; certificate | An exact polynomial equality expressing a target as a sum of positive coefficients times products of quantities known to be nonnegative. It proves the target's sign. |
| Generator | One of those quantities known to be nonnegative. Its name does not mean a software component. |
| Bernstein coefficients | Coefficients in a polynomial basis whose basis functions are nonnegative on a specified box. Nonnegative coefficients therefore prove nonnegativity on that box. |
| Resultant | A polynomial expression used to eliminate a variable from two polynomial equations. |
| Reciprocal variable | A variable introduced by taking an inverse or a related rational change of coordinates. Its domain must also be transformed. |

## What the computer algebra contributes

A numerical search can suggest an identity. The proof uses the resulting exact rational identity, together with its explicit sign assumptions. The calculation files construct the polynomials or exact coefficients used in those identities. Coefficient tables in `calculation-data/` record the finite sums, so the reader does not need any discovery search or optimization log.

This distinction is especially important for a regional result. Showing a polynomial has the required sign on one region does not establish that sign on all possible parameters. The reciprocal-coordinate lemmas state their regions explicitly.

## What to read first

For the theorem and its meaning, read the opening of the main proof and its final nine-solution example. For the reasoning behind the upper bound, continue through the common analytic tools and the two coefficient-sign cases. When a named lemma is invoked, follow its appendix link. The appendix's [reciprocal-coordinate section](appendix.md#reciprocal-coordinate-height-and-regional-bounds) groups its common definitions and region-specific results.
