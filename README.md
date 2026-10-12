# N(3,4) = 9

Fewnomial theory asks how the number of terms in polynomial equations limits their number of solutions, independently of their degrees. The case $`N(3,4)`$ concerns two equations in two variables: one with at most three monomial terms and the other with at most four.

This repository proves **$`N(3,4)=9`$**: nine is the largest possible number of isolated solutions with $`x,y>0`$. The [main proof](docs/proof.md) states the precise counting conventions. The result combines a bound that applies to every such system with an explicit example attaining nine.

## The problem and prior results

In one variable, Descartes' rule of signs gives a bound from the number of terms, even when the polynomial's degree is large. Obtaining sharp bounds for systems in several variables is much harder. A key earlier exact result is $`N(3,3)=5`$, proved by [Li, Rojas, and Wang](https://arxiv.org/abs/math/0212178): two equations with three terms each can have five solutions under the same counting convention.

For the three-term/four-term case, the following results set the context:

| Work | Result for $`N(3,4)`$ |
| --- | --- |
| [Li, Rojas, and Wang (2003)](https://arxiv.org/abs/math/0212178) | Their bound $`N(3,m)\le 2^m-2`$ gives an upper bound of fourteen. |
| [Gomez, Niles, and Rojas (2007 preprint)](https://arxiv.org/abs/0709.2405) | A system attaining seven gives a lower bound of seven. |
| [El Hilany and Tavenas (2024 preprint)](https://arxiv.org/abs/2409.01651) | Their improved fewnomial bound gives an upper bound of eleven. |
| This repository | A universal upper bound of nine and a nine-solution example give the exact value. |

The value nine closes the gap between those lower and upper bounds. It advances a basic case beyond $`N(3,3)=5`$ from an estimate to a sharp answer: the number of terms alone determines the maximum, without a restriction on polynomial degree. Both parts matter. An upper bound rules out a tenth solution; the example shows that the bound cannot be lowered.

## Reading the proof

Start with the [reading guide](docs/reading-guide.md), then read the main argument and follow its appendix references where needed.

| Document | What it contains |
| --- | --- |
| [Main proof](docs/proof.md) | The reduction to one variable, the upper bound, and the example attaining nine. |
| [Appendix](docs/appendix.md) | Supporting lemmas, their precise hypotheses, and the polynomial calculations used in the proof. |
| [Calculation guide](docs/calculations.md) | How to run the exact calculations and read their coefficient tables. |
| [References](docs/references.md) | Prior results, external mathematical inputs, and the sources of the included arguments. |

The reduction turns the system into a four-term function

```math
F(x)=\sum_{i=0}^{3}c_i x^{a_i}(1-x)^{b_i},\qquad 0<x<1.
```

The proof shows that a nonzero function of this form has at most nine distinct zeros for arbitrary real coefficients and exponents, then transfers that bound back to the polynomial system. The appendix supplies the specialized inequalities needed in the argument, including their parameter restrictions.

## Repository contents

- `docs/` contains the main proof, appendix, reading guide, references, and detailed lemma proofs.
- `calculations/` contains the calculation programs used in the proof.
- `calculation-data/` contains exact coefficient tables for the polynomial identities.
- `requirements.txt` lists the Python libraries needed for the calculations.

The documents can be read on GitHub without running any code. The repository includes proof calculation code and mathematical data; verification, audit, replay, and test scripts are excluded.

## Run the proof calculations

Python 3 is required. From the repository root, create an environment and install the dependencies:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
```

Follow the [calculation guide](docs/calculations.md) for the individual commands and their mathematical purpose. Calculation outputs belong in `build/`, which Git ignores.

## Push to GitHub

This is a local Git repository with an initial commit. After extracting the package, create an empty repository on GitHub, then run these commands from the extracted `n34-proof` folder. Replace the example address with your repository's address.

```sh
git remote add origin https://github.com/YOUR-ACCOUNT/n34-proof.git
git push -u origin main
```

Leave GitHub's automatic README, license, and `.gitignore` options unchecked when creating that empty repository; this package already supplies its README and `.gitignore`. No license has been selected on your behalf.

For a copy extracted without its `.git` directory, first run:

```sh
git init -b main
git add .
git commit -m "Add simplified proof of N(3,4) = 9"
```
