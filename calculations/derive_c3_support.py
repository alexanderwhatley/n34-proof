#!/usr/bin/env python3
"""Calculate the positive coefficient expansions for C3 slope support.

The boundary quadratic and the two endpoint derivative expressions are
given in the appendix. This script applies their stated positive-variable
substitutions and clears only positive denominators. Its output contains
the resulting exact polynomial coefficients.
"""
import argparse
from pathlib import Path
import sympy as sp
from polynomial_data import polynomial_bundle, write_json


def boundary_polynomials():
    h,s,S,T = sp.symbols("h s S T")
    F = ((3*h*h+6*h*s-3*h+2*s*s-3*s)*T*T
         -s*(4*h*h*s-3*h*h*S+4*h*s*s-8*h*s*S-4*h*s
             +3*h*S+2*s**3-3*s*s*S-2*s*s+4*s*S)*T
         -s*s*(3*h*h*s*s+3*h*h*s*S-h*h*S*S+2*h*s**3
               -3*h*s*s-4*h*s*S*S-3*h*s*S+h*S*S-s**3*S
               -s**3-2*s*s*S*S+2*s*S*S))
    b0 = F.subs(T,0)
    b1 = lambda cap: b0+cap*sp.diff(F,T).subs(T,0)/2
    source = {
        "b0_universal":b0,
        "b1_largeS":b1(s*s), "b2_largeS":F.subs(T,s*s),
        "b1_smallS":b1(S*S/4),"b2_smallS":F.subs(T,S*S/4)}
    z,t,u = sp.symbols("z t u")
    variables = (z,t,u)
    result = {}
    for name,expression in source.items():
        D = 2*(1+u)
        Hn = u
        sn = D*(1+t)-u
        if name.endswith("smallS"):
            Sn = 2*u*(1+z)+4*z*(1+t*(1+u))
            Hn *= 1+z
            sn *= 1+z
            D *= 1+z
        elif name == "b0_universal":
            Sn = 2*Hn+z*D
        else:
            Sn = 2*sn+z*D
        cleared = sp.Poly(0,*variables)
        for powers,coefficient in sp.Poly(expression,h,s,S).terms():
            term = coefficient*Hn**powers[0]*sn**powers[1]*Sn**powers[2]*D**(6-sum(powers))
            cleared += sp.Poly(term,*variables)
        result[name] = cleared.as_expr()
    return variables,result


def endpoint_polynomials():
    a,d,t,h,X = sp.symbols("a d t h X")
    b=a+d
    A,B,s,L,G = a+h,b+h,1+t-h,a+1+t,a+b+2*a*b
    S,T = A+B,A*B
    e,th = 1-2*h,2*h*(1-h)
    f3 = 4*S*(T-e*s)+th*(2*s-S)
    f2 = 4*e*(s*S*S+2*S*T+2*s*T)+2*s*S*T-4*T*T+th*(S*S+s*S+2*T)
    f1 = 6*e*T*(2*T+s*S)+3*th*(3*S*T+s*S*S+2*s*T)
    f0 = 6*th*T*(2*T+s*S)
    K3,K2 = L*f3+2*G*(s*s-T),L*f2-2*G*s*(2*T+s*S)
    Z = K3*X**3+K2*X*X-L*f1*X+L*f0
    raw = {
        "der_minus_d4_curv":sp.diff(Z,X).subs(X,B)-d*sp.diff(Z,X,2).subs(X,B)/4,
        "B_k3_plus_k2":B*K3+K2}
    q=sp.symbols("q")
    variables=(a,d,t,q)
    D = (1+2*b)*(1+q)
    Hn=b*q
    result={}
    for name,expression in raw.items():
        cleared=sp.Poly(0,*variables)
        for (power,),coefficient in sp.Poly(expression,h).terms():
            cleared += sp.Poly(coefficient*Hn**power*D**(3-power),*variables)
        result[name]=cleared.as_expr()
    return variables,result


def main(output):
    for name,calculation in [("zero-slope-boundary",boundary_polynomials),
                             ("lower-endpoint-shape",endpoint_polynomials)]:
        variables,expressions=calculation()
        write_json(output/(name+".json"),polynomial_bundle(variables,expressions))
    print("Wrote the five boundary and two endpoint coefficient tables to",output)


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=Path("build/c3-support"))
    main(parser.parse_args().output)
