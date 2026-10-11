#!/usr/bin/env python3
"""Calculate normalized endpoint polynomials for the reciprocal height lemma.

The last step constructs their Bernstein coefficient expansion on the
displayed four-dimensional box.
"""
import argparse
from pathlib import Path
import sympy as sp
from polynomial_data import polynomial_bundle, bernstein_groups, write_json


def endpoint_polynomials():
    A,Delta,v,u,k = sp.symbols("A Delta v u k")
    N = (A*A-Delta*Delta)/4
    n = 1-k
    Z = (A*A+Delta*Delta)/2-3*Delta+2+v*(Delta-1)+N*u
    t = (A-Delta)*u+(A-2)*k+v-1
    d = 3-v+Delta*u
    w = A*(u+k)+n
    f = -v*t-N*(1+u)-5*n*Z+15*N*n*n
    c3 = -(1+v)*n*w-2*t*t-d*t-(1+u)*(v*v-v-2+2*Z)
    g = -c3-4*v*n*t-4*N*n*(1+u)-10*n*n*Z+20*N*n**3
    c4 = -(5*t+2*d)*n*w+(1+u)*(2-v)*(2*d+3*t)-N*(1+u)**2
    e4 = c4-3*n*c3-6*v*n*n*t-6*N*n*n*(1+u)-10*n**3*Z+15*N*n**4
    ell = 2*e4-n*g
    s = 3*(-3*d*n+(4-2*v)*(1+u)+(5-v)*n*n)
    d3 = (4*A-3*Delta)*u+k*(4*A-9+3*v)
    j = s*f+v*ell
    r0 = 4*n*f-7*g
    qr = -14*ell*ell+s*ell*(4*n*v+7*d3)+s*s*r0
    return (A,Delta,v,u,k), {"f":f,"g":g,"ell":ell,"s":s,
                              "d3":d3,"j":j,"r0":r0,"qr":qr}


def source_floor(output):
    p,q,e,t,delta = sp.symbols("p q e t delta")
    variables = (p,q,e,t,delta)
    r,y = p+t,q+e
    n = p*q-delta
    A = p+q
    v = 3+2*q+e-2*p-t
    h = -v
    Y = p*q*r*y
    D = p*q*r+y*(p*r-q*(p+r))
    Z = (y+1)*(p+r-q-1)-p*r+q*(p+r)
    lam = A*(y*r-n)
    T = lam+2*n-D
    W = -n*(lam+n)
    C = [sp.Integer(1),Z,h*T-Y,
         (1-h)*W-2*T*T-D*T-Y*(h*h+h-2+2*Z),
         (5*T+2*D)*W+Y*(h+2)*(2*D+3*T)-Y*Y]
    E = [(-1)**j*sum(C[i]*sp.binomial(6-i,6-j)*(-n)**(j-i)
                    for i in range(j+1)) for j in range(5)]
    factors = {"one":sp.Integer(1),"a":A-4,"v":v,
               "sharp_d":sp.Rational(4,15)*p*q-delta,"E2floor":E[2]}
    for name in ("sharp_d","E2floor"):
        for base in ("a","v"):
            factors[base+"*"+name] = factors[base]*factors[name]
    for i in range(4):
        for j in range(4-i):
            if i+j>=2: factors[f"a{i}v{j}"] = (A-4)**i*v**j
    factors["floor_target"] = 2*E[4]-n*E[3]
    write_json(output/"height-floor-polynomials.json",polynomial_bundle(variables,factors))


def main(output, include_box):
    variables, expressions = endpoint_polynomials()
    write_json(output/"height-normalized-polynomials.json",
               polynomial_bundle(variables,expressions))
    source_floor(output)
    if include_box:
        A,Delta,v,u,k = variables
        a,w,rho = sp.symbols("a w rho")
        aa = a+4
        vv = rho*(3+aa*(2+u*w))
        numerator = u*aa*(2*w-1)-2*vv+6
        # qr has degree at most four in Delta. Clear its denominator
        # monomial by monomial instead of performing rational expansion.
        expr = sp.Poly(0,a,u,k,w,rho)
        for powers,coefficient in sp.Poly(expressions["qr"],*variables).terms():
            ma,md,mv,mu,mk = powers
            term = -coefficient*aa**ma*numerator**md*vv**mv*u**mu*k**mk*(u+4)**(4-md)
            expr += sp.Poly(term,a,u,k,w,rho)
        data = bernstein_groups(expr.as_expr(),(a,),(u,k,w,rho),
                                (sp.Rational(3,4),sp.Rational(4,15),1,1),
                                (11,8,4,4))
        data["target"] = "-(u+4)^4*qr under the stated normalized substitution"
        data["substitution"] = "A=4+a,v=rho*(3+A*(2+u*w)),Delta=(u*A*(2*w-1)-2*v+6)/(u+4)"
        write_json(output/"full-height-bernstein.json",data)
    print("Wrote reciprocal height calculation data to",output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=Path("build/reciprocal-height"))
    parser.add_argument("--skip-box",action="store_true",help="derive only the endpoint and source-floor polynomials")
    args = parser.parse_args()
    main(args.output,not args.skip_box)
