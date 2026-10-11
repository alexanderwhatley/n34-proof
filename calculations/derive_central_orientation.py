#!/usr/bin/env python3
"""Calculate the positive coefficient expansion for central contacts.

Starting with equation (14) of the central-contact orientation lemma,
this script clears the positive denominator after z=mu*v*q/K_n.
It then changes each unit-interval variable x to y/(1+y), clearing
the four denominators. Its output is the exact integer monomial table
used to prove positivity.
"""
import argparse
from pathlib import Path
from math import comb
from polynomial_data import polynomial_bundle, write_json
import sympy as sp


def orientation_polynomial():
    h, v, mu, q, z = sp.symbols("h v mu q z")
    H = 1-h
    a = h+H*v*mu
    k = 1-2*z
    Kn = h+H*mu*v*(2-v*mu)
    Qn = v*(1-mu)+z*(Kn-v)
    Rn = mu*v-z*Kn
    N = (v*(1-2*z)+2*a*z)*Qn-a*z*(1-v)*Rn
    Gn = 3*h*Qn*Qn-a*N
    Un = (-2*z*a*v*Qn**3-2*z*z*a**3*v*Qn*Qn
          -z*a*a*v*(2-v)*k*Qn*Qn+a*z*a*(4-v)*N*Qn
          +a*v*N*k*Qn-2*a*N*N+2*h*N*Qn*Qn-h*v*Qn**3*k)
    F = -2*Un-Rn*(1+mu)*Gn*Qn
    variables = (h, v, mu, q)
    result = sp.Poly(0, *variables)
    for (power,), coefficient in sp.Poly(F, z).terms():
        result += sp.Poly(coefficient*(mu*v*q)**power*Kn**(4-power), *variables)
    return variables, result


def open_cube_expansion(polynomial, degrees):
    """Clear x_i=y_i/(1+y_i) one variable at a time."""
    current = {powers:int(coefficient) for powers,coefficient in polynomial.terms()}
    for axis, degree in enumerate(degrees):
        expanded = {}
        for powers, coefficient in current.items():
            power = powers[axis]
            for extra in range(degree-power+1):
                new_powers = list(powers)
                new_powers[axis] += extra
                key = tuple(new_powers)
                expanded[key] = expanded.get(key,0)+coefficient*comb(degree-power,extra)
        current = {powers:coefficient for powers,coefficient in expanded.items() if coefficient}
    return current


def main(output):
    variables, polynomial = orientation_polynomial()
    degrees = tuple(polynomial.degree(variable) for variable in variables)
    rows = open_cube_expansion(polynomial, degrees)
    write_json(output/"central-orientation-unit-cube.json", polynomial_bundle(
        variables,{"K_n^4*F(z=mu*v*q/K_n)":polynomial.as_expr()}))
    output.mkdir(parents=True, exist_ok=True)
    with (output/"CENTRAL_POSITIVE_COEFFICIENTS.tsv").open("w",encoding="utf-8") as stream:
        stream.write("h_power\tv_power\tmu_power\tq_power\tcoefficient\n")
        for powers, coefficient in sorted(rows.items()):
            stream.write("\t".join(map(str,(*powers,coefficient)))+"\n")
    print("Unit-cube coordinate degrees:",degrees)
    print("Wrote",len(rows),"nonzero integer coefficient rows to",output)


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=Path("build/central-orientation"))
    main(parser.parse_args().output)
