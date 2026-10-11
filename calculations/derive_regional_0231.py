#!/usr/bin/env python3
"""Calculate the small positive coefficient expansions for order 0231.

This produces the polynomial coefficients that occur in the regional
arguments after the displayed variable substitutions.
"""
import argparse
from pathlib import Path
import sympy as sp
from polynomial_data import coefficients, bernstein_groups, write_json


def expressions(p, q, r, y):
    h = p+r-q-y-3
    Y = p*q*r*y
    Z = (q+y+1)*(p+r-1)-p*r-q*y
    boundary = q*r*y-p*q*q+p*(r-y-2*q-1)**2/4
    return {"shape_gap": p*(3*q+2*(r-q-y-1))**2-9*q*r*y,
            "first_Newton_obstruction": 12*h*boundary-5*Z**2-12*Y,
            "height": h}


def main(output):
    q, e, a, t = sp.symbols("q e a t")
    cones = {}
    for name, c, k in [("p_at_least_5_S_over_2", sp.Rational(5,2), 1),
                       ("p_at_least_2_S_r_at_least_2_p", 2, 2),
                       ("p_at_least_S_r_at_least_3_p", 1, 3)]:
        p = c*(2*q+e+1)+a
        result = expressions(p, q, k*p+t, q+e)
        cones[name] = {"c": str(c), "k": str(k),
                       "polynomials": {label: coefficients(expr, (q,e,a,t))
                                       for label, expr in result.items()}}
    write_json(output/"three-cone-0231.json", {
        "variables": ["q", "e=y-q", "a=p-c*(q+y+1)", "t=r-k*p"],
        "cones": cones})
    Q, t, u, z = sp.symbols("Q t u z")
    S = Q+1
    p, r, q = z*S, 3*S/z+t, u*Q/2
    result = expressions(p, q, r, Q-q)
    clearing = {"shape_gap": z, "first_Newton_obstruction": z*z,
                "height": z}
    tables = {name: bernstein_groups(sp.cancel(clearing[name]*expr),
                                     (Q,t), (u,z))
              for name, expr in result.items()}
    write_json(output/"curved-0231.json", {
        "substitution": "S=Q+1,p=z*S,r=3*S/z+t,q=u*Q/2,y=Q-q",
        "domain": "Q,t>=0; 0<=u,z<=1; actual source Q>0,0<u<1,0<z<=1",
        "targets": tables})
    print("Wrote regional coefficient expansions to", output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("build/regional-0231"))
    main(parser.parse_args().output)
