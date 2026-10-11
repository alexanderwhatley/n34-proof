# A simplified proof that N(3,4) = 9

This repository contains our simplified proof of the sharp bound of nine positive isolated solutions for a system of two real polynomial equations, with at most three terms in one equation and four in the other.

A **positive solution** has both coordinates greater than zero. An **isolated solution** has a neighborhood containing no other solution. We count solutions, rather than their multiplicities. The proof also establishes the same maximum for solutions where the two curves cross with a nonzero Jacobian determinant.

The central step is a statement about one variable: a nonzero function

$$
F(x)=\sum_{i=0}^{3}c_i x^{a_i}(1-x)^{b_i},\qquad 0<x<1,
$$

has at most nine distinct zeros, for arbitrary real coefficients and exponents. A change of coordinates reduces the original polynomial system to this statement. An explicit example attains nine.

## Reading the proof

Start with the [reading guide](docs/reading-guide.md). The documents then follow this order:

| Document | What it contains |
| --- | --- |
| [Main proof](docs/proof.md) | The reduction to one variable, the upper-bound argument, and the example with nine solutions. |
| [Appendix](docs/appendix.md) | The supporting calculations and the precise assumptions of each specialized lemma. It links to the longer proofs kept in this repository. |
| [Further simplifications](docs/further-simplifications.md) | The later height and event-order results, with the regions where they replace longer arguments. |
| [Calculation guide](docs/calculations.md) | The exact calculations used in the proof and how to run them. |
| [References](docs/references.md) | The external theorem used in the proof and the origins of the mathematical documents. |

The main argument is the complete fifth simplification revision. The later results supply additional replacements on their stated regions. They do not replace the arguments for an entire remaining event order. Those original arguments are retained, so an unproved broader shortcut is never a premise of the proof.

The proof uses exact computer algebra for some polynomial identities. Their coefficient tables are mathematical proof data, and are included. The repository contains only calculation code used in the proof work; it does not contain verification, audit, replay, or test scripts.

## Repository contents

- `docs/` contains the proof, appendix, terminology, and supporting mathematical arguments.
- `calculations/` contains the proof calculation programs.
- `calculation-data/` contains exact coefficient tables used in positive-sum identities.
- `requirements.txt` lists the Python libraries needed for the calculations.

The documents can be read on GitHub without running any code. GitHub renders the mathematical formulas in the Markdown files.

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

## Run the proof calculations

Python 3 is required. From the repository root, create an environment and install the dependencies:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
```

Follow the [calculation guide](docs/calculations.md) for the individual commands and their mathematical purpose. Calculation outputs belong in `build/`, which Git ignores.
