#!/usr/bin/env python3
"""Calculate the degree-six forcing polynomial for positive coefficients.

The entropy-curve comparison in the appendix uses u0=(R-B)/H. Its
forcing numerator is W=R*(H*Y'-H'*Y)-Y*(H-P*Y)*j. This calculation
expands W and the displayed derivative numerators at exact coefficients.
"""
import argparse
from pathlib import Path
import sympy as sp
from polynomial_data import polynomial_bundle, write_json


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=Path("build/entropy"))
    output = parser.parse_args().output
    r,P,Q,K,r0,r1,r2,r3,u = sp.symbols("r P Q K r0 r1 r2 r3 u")
    B = r*(1+r)
    H = P*(P-1)*r*r-2*P*Q*r+Q*(Q-1)
    j = Q-(P-1)*r
    R = r0+r1*r+r2*r*r+r3*r**3
    Y = R-B
    W = R*(H*sp.diff(Y,r)-sp.diff(H,r)*Y)-Y*(H-P*Y)*j
    elasticity = -(1-P*u)*(r-Q*u)*(u*(H+K*r)**2+K*r*r*(1+r-K*u))
    write_json(output/"entropy-polynomials.json",polynomial_bundle(
        (r,P,Q,K,r0,r1,r2,r3,u),{"forcing_W":W,
                                "elasticity_derivative_numerator":elasticity}))
    print("Wrote the entropy forcing and derivative coefficient tables to",output)
