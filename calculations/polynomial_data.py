"""Exact coefficient tables used by the proof calculations.

Each row represents coefficient * product(variable ** exponent).
The routines here calculate the polynomial expansions used in the proof.
"""
import json
from pathlib import Path
import sympy as sp


def coefficients(expression, variables):
    """Convert an exact expression to a sparse, rational coefficient table."""
    polynomial = sp.Poly(sp.expand(expression), *variables)
    return [{"powers": list(powers), "coefficient": str(value)}
            for powers, value in polynomial.terms()]


def homogeneous(expression, source_variables, destination, substitutions,
                degree, scale=1, weights=None):
    """Clear a normalization by adding powers of its positive scale.

    `substitutions` is the list of replacement variables. `scale` replaces
    the constant one. A source monomial of weighted degree d receives
    scale**(degree-d). This is ordinary homogeneous clearing of denominators.
    """
    weights = weights or [1] * len(source_variables)
    result = sp.Poly(0, *destination)
    for powers, coefficient in sp.Poly(expression, *source_variables).terms():
        d = sum(p * w for p, w in zip(powers, weights))
        term = coefficient * scale ** (degree - d)
        for value, exponent in zip(substitutions, powers):
            term *= value ** exponent
        result += sp.Poly(term, *destination)
    return result.as_expr()


def bernstein_groups(expression, positive_variables, interval_variables,
                     interval_lengths=None, degrees=None):
    """Expand in powers of positive variables and Bernstein basis on a box.

    B_i^d(z)=binomial(d,i)*z**i*(1-z)**(d-i), for 0<=z<=1.
    If an interval length is L, the coordinate is z/L. The conversion
    coefficient of z**m at basis index i is binomial(i,m)/binomial(d,m).
    """
    lengths = interval_lengths or [sp.Integer(1)] * len(interval_variables)
    expression = sp.expand(expression)
    all_variables = (*positive_variables, *interval_variables)
    polynomial = sp.Poly(expression, *all_variables)
    degrees = degrees or [polynomial.degree(z) for z in interval_variables]
    groups = {}
    n = len(positive_variables)
    for powers, coefficient in polynomial.terms():
        head, tail = powers[:n], powers[n:]
        groups.setdefault(head, {})[tail] = coefficient * sp.prod(
            length ** exponent for length, exponent in zip(lengths, tail))
    from itertools import product
    from fractions import Fraction
    from math import comb
    rows = []
    for head, terms in sorted(groups.items()):
        # Apply the one-variable conversion successively along each axis.
        # This is the same tensor-product expansion without a large dense sum.
        current = {powers: Fraction(str(value)) for powers,value in terms.items()}
        for axis, degree in enumerate(degrees):
            converted = {}
            for powers, value in current.items():
                m = powers[axis]
                for i in range(m, degree+1):
                    indices = list(powers)
                    indices[axis] = i
                    indices = tuple(indices)
                    converted[indices] = converted.get(indices,Fraction(0)) + value*Fraction(comb(i,m),comb(degree,m))
            current = {indices:value for indices,value in converted.items() if value}
        for indices in product(*(range(d + 1) for d in degrees)):
            value = current.get(indices,Fraction(0))
            rows.append({"positive_powers": list(head),
                         "bernstein_indices": list(indices),
                         "coefficient": str(value)})
    return {"positive_variables": [str(z) for z in positive_variables],
            "interval_variables": [str(z) for z in interval_variables],
            "interval_lengths": [str(z) for z in lengths],
            "degrees": degrees, "rows": rows}


def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def polynomial_bundle(variables, expressions):
    return {"variables": [str(z) for z in variables],
            "polynomials": {name: coefficients(expr, variables)
                            for name, expr in expressions.items()}}
