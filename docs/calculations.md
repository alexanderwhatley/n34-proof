# Calculations used in the proof

The proof uses two kinds of calculation: interval bounds for its nine-root
example, and exact polynomial expansions for a few inequalities. This
document explains the included code and the mathematical coefficient tables.
The arguments that use these calculations are in [the appendix](appendix.md).

## Running the calculations

Use Python 3.10 or later. From the repository's top-level folder, create a
virtual environment and install the two pinned dependencies:

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate with `.venv\Scripts\activate` instead of the second
command. Then run any calculation below. The polynomial scripts write their
results under `build/`, which Git ignores. The `--output` option can select
another output folder.

| Command | Mathematical calculation | Where the result is used |
| --- | --- | --- |
| `python calculations/witness_intervals.py` | Encloses the function value at ten specified points, with outward rounding at 100 decimal digits. The coefficients and sample points are exact decimal inputs. | The nine-root example in [the proof](proof.md). |
| `python calculations/derive_f3_coefficients.py` | Expands the determinant formed from the first three derivatives of three beta functions; clears positive normalization factors; lists the polynomials in the two remaining orders of events. | The [F3 argument in the appendix](appendix.md#f3-polynomial-inequalities). |
| `python calculations/derive_central_orientation.py` | Builds the polynomial in equation (14), makes the displayed unit-interval substitutions, and produces its integer coefficient expansion. | [Central-contact orientation](lemmas/height/central-contact-orientation.md). |
| `python calculations/derive_c3_support.py` | Expands five zero-slope boundary polynomials and two lower-endpoint derivative polynomials after their positive-variable substitutions. | [C3 slope support](lemmas/positive/c3-upper-tail-quadratic-slope-support-theorem.md). |
| `python calculations/derive_f24_expansions.py` | Uses the supplied integer multiplier identity to expand the two positive expressions in each of the two small-first-root parameter regions. | The [remaining upper-low middle pattern](lemmas/positive/upper-low-small-first-root-middle-pattern-theorem.md). |
| `python calculations/derive_entropy_coefficients.py` | Expands the common degree-six forcing polynomial and the entropy-curve derivative numerator. | The [positive-coefficient arguments](appendix.md#positive-coefficient-arguments). |
| `python calculations/derive_reciprocal_height.py` | Derives the normalized endpoint polynomials, the source-floor polynomial, and the four-dimensional Bernstein expansion. | The [reciprocal height lemma](lemmas/f3/reciprocal-height.md). |
| `python calculations/derive_regional_0231.py` | Expands the three linear parameter regions and the curved parameter region for the order-0231 shape exclusions. | The [shape exclusions](lemmas/f3/shape-exclusions.md). |

The largest symbolic expansions can take several minutes. To calculate only
one part of the F3 expansion, use `--sector 0231`, `--sector 1320-positive`, or
`--sector 1320-nonpositive`. To omit the largest reciprocal-height expansion,
use `--skip-box`.

`polynomial_data.py` supplies shared routines for writing exact rational
coefficients, clearing normalization factors, and changing polynomial basis.
It is imported by the calculation scripts.

## Reading a coefficient table

A **monomial** is a product of powers of variables. If the variable list is
`[a, d, h]`, a row with powers `[2, 0, 3]` and coefficient `7/5` means
$`(7/5)a^2h^3`$. A table is the sum of all its rows. Omitted rows have
coefficient zero. Integer and fraction strings are exact values.

Some tables list a **multiplier**, meaning a polynomial that is multiplied by
one of the displayed inequalities. For example, a row labeled `A` means
its monomial and coefficient multiply the polynomial named $`A`$ in the
corresponding argument. A product label such as `A_H3` means $`A H_3`$.
The proof establishes the required signs of those factors before using the
identity. Positive coefficients by themselves do not establish their signs.

The **Bernstein basis** on $`0\le z\le1`$ consists of

```math
B_i^d(z)=\binom di z^i(1-z)^{d-i},\qquad 0\le i\le d.
```

Each basis function is nonnegative. Thus a polynomial with nonnegative
coefficients in this basis is nonnegative throughout that interval.
For several interval variables, take products of these basis functions.
An interval of length $`L`$ uses $`B_i^d(z/L)`$. The tables record the degree,
interval length, and basis index of every coefficient. When positive
variables are also present, each group is multiplied by its specified
monomial in those variables. Strict positivity still requires a positive
term that cannot vanish on the actual domain; that step is stated in the
corresponding lemma.

Files ending in `.json.gz` contain ordinary JSON compressed with gzip.
They can be opened by a gzip utility or read with Python's `gzip` module.
Compression preserves every exact coefficient.

## Tables for the main proof

| Files | Identity or expansion |
| --- | --- |
| [0231 third coefficient](../calculation-data/f3/0231-third-head.json), [fourth coefficient](../calculation-data/f3/0231-fourth-head.json), [terminal fourth coefficient](../calculation-data/f3/0231-terminal-fourth-head.json) | The sum of the listed weighted generator products and the positive remainder is identically zero. Under the proposed bad coefficient signs, every summand is nonnegative and the remainder is strictly positive, giving a contradiction. The generator names and variable order are reconstructed by `derive_f3_coefficients.py`. |
| [1320 first adjacent pair](../calculation-data/f3/1320-first-adjacent.json), [second adjacent pair](../calculation-data/f3/1320-second-adjacent.json) | The first sum is zero. The second sum is $`-rGkPhzE`$. All seven variables in this normalization are positive; the sign contradiction is explained in the F3 appendix. |
| [1320 low height](../calculation-data/f3/1320-low-height.json), [derivative gap](../calculation-data/f3/1320-derivative-gap.json), [cubic gap](../calculation-data/f3/1320-cubic-gap.json) | Each `terms` array expresses its displayed `target` as a positive linear combination of products of the listed generators. `generator_exponents` follows `generator_order`. These are the three nonpositive-$`GT`$ inequalities derived by `derive_f3_coefficients.py`. |
| [Central orientation integer table](../calculation-data/height/CENTRAL_POSITIVE_COEFFICIENTS.tsv), [preceding unit-cube expansion](../calculation-data/height/central-orientation-unit-cube.json) | The TSV lists the 2,331 nonzero positive integer coefficients after all four substitutions $`x_i=y_i/(1+y_i)`$ and denominator clearing. Its first four columns are powers; its final column is the coefficient. The coordinate degrees before the substitutions are $`(5,13,13,4)`$. |
| [C3 endpoint tables](../calculation-data/positive/c3_endpoint_certificate) | The raw source-cap numerator and the three positive expansions at the two possible lower endpoints. See [the endpoint lemma](lemmas/positive/c3-native-lower-endpoint-and-derivative-lemmas.md) for the variables and clearing factors. |
| [C3 zero-slope boundary](../calculation-data/positive/c3_support/C3_D3ZERO_POSITIVE_CERTIFICATE.json), [C3 lower-endpoint shape](../calculation-data/positive/c3_support/C3_CUBIC_SHAPE_AT_B_COEFFICIENTS.json) | The five positive lifts of the degree-two boundary Bernstein coefficients, followed by the positive expansions of $`I_1`$ and $`I_2`$. `F_variables` names the variables of the boundary quadratic; its local `H` denotes $`h`$ and `L` denotes $`s`$ in the lemma. `homogeneous_terms` gives the expansion with the common positive clearing factor; `terms` in the endpoint file gives the corresponding endpoint expansion. |
| [C45 tables](../calculation-data/positive/c45_certificate) | The compact linear coefficient numerators, the two boundary identities and positive remainders, and the positive expansions for the three complete parameter regions. See [the C45 lemma](lemmas/positive/upper-low-band-c45-blended-cap-theorem.md). Each file gives its variable order and exact monomial coefficients. |
| [F23 integer identity](../calculation-data/positive/f23_certificate/F23_EXACT_INTEGER_CERTIFICATE.json.gz) | The integer multiplier identity with 189 weights and 1,829 positive remainder terms. A weight row names the multiplier polynomial, its monomial powers, and its integer coefficient. See [the nonnegative-slope argument](lemmas/positive/upper-low-f23-threshold-gate.md). |
| [F24 underlying integer identity](../calculation-data/positive/f24_certificate/NATURAL_F23_EXACT_INTEGER_CERTIFICATE.json.gz), [its four positive expansions](../calculation-data/positive/f24_certificate) | The alternative F23 identity with 184 weights and 1,828 positive remainder terms used to obtain F24. `a_lt_one_seventh-AE` and `a_lt_one_seventh-RE` list the expansions for $`a<1/7`$; `a_lt_two_h-AE` and `a_lt_two_h-RE` list those for $`a<2h`$. Their variable order is $`(u,d,c,v,z)`$. The substitutions and positive clearing factors are in [the small-first-root argument](lemmas/positive/upper-low-small-first-root-middle-pattern-theorem.md). |

The words “third” and “fourth” in filenames refer to polynomial coefficient
indices, as defined in the F3 appendix. The digit strings `0231` and `1320`
are short labels for two orders of four events; their interpretation is
given there. They are not extra hypotheses or unidentified case numbers.

## Tables for the reciprocal-coordinate lemmas

The following tables accompany [the reciprocal-coordinate lemmas](appendix.md#reciprocal-coordinate-height-and-regional-bounds).
Their stated parameter regions are part of each theorem.

| File | Meaning |
| --- | --- |
| [Height source-floor identity](../calculation-data/reciprocal/height-floor.json) | The `support` rows express the source-floor target as a sum of positive monomials times the specified source inequalities. The target and named factors are derived in `height-floor-polynomials.json` by `derive_reciprocal_height.py`. |
| [Full reciprocal-height Bernstein expansion](../calculation-data/reciprocal/full-height-bernstein.json) | The exact expansion of the cleared target polynomial on the stated box. It has 13,125 positive entries and 375 zero entries. `a_exponent` names the positive-variable group; the four `indices` name the Bernstein basis functions. Zero entries are omitted. |
| [Three linear shape regions](../calculation-data/reciprocal/three-cone-0231.json) | Exact coefficient expansions after $`y=q+e`$, $`p=c(q+y+1)+a`$, and $`r=kp+t`$. The table specifies $`c,k`$ for each region. |
| [Curved shape region](../calculation-data/reciprocal/curved-0231.json) | Mixed power/Bernstein expansions after $`p=zS`$, $`r=3S/z+t`$, $`S=Q+1`$, $`q=uQ/2`$, and $`y=Q-q`$. The theorem states the strict source conditions that allow these substitutions. |

The supplied polynomial calculations and coefficient tables are the
supporting computational parts of the proof. They are intended to make
the displayed algebra available without the earlier research archives.
