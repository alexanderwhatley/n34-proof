#!/usr/bin/env python3
"""Derive the exact polynomial coefficients used in the two F3 arguments.

The determinant is built from the first three derivatives of the original
three atoms. Output contains the coefficients and the polynomial factors
used in the positive-sum identities.
"""
import argparse
from pathlib import Path
import sympy as sp
from polynomial_data import homogeneous, polynomial_bundle, write_json


def determinant(first, second, third):
    return (first[0]*(second[1]*third[2]-second[2]*third[1])
            -first[1]*(second[0]*third[2]-second[2]*third[0])
            +first[2]*(second[0]*third[1]-second[1]*third[0]))


def quotient(expression, divisor, variables):
    return sp.Poly(expression, *variables).div(
        sp.Poly(divisor, *variables))[0].as_expr()


def order_0231(output):
    P,r,v,ell,lam,eta,w = sp.symbols("P r v ell lam eta w")
    source = (P,r,v,ell,lam,eta)
    x = P+r+v
    y = 1-x
    L = 1-P-r+ell
    V = 1-r+ell
    b_num = L*r+V*eta
    a_num = x*L*(1-r)+V*(y*eta-lam)
    first = [x*L+V*(eta-lam)+b_num*w,
             -P*x-P*(1+ell)*w, L*x+L*r*w]
    sums = [P*(L-v)+V*(v-lam),P*(L-v),L*(P+v)]
    second = [u*u-x*z*(x+w) for u,z in zip(first,sums)]
    third = [u**3-3*x*z*(x+w)*u-x*x*z*(x+w)*(1-2*x-w)
             for u,z in zip(first,sums)]
    core = quotient(determinant(first,second,third), P*L*V**2,
                    (*source,w))
    q = [sp.expand(core).coeff(w,j) for j in range(7)]
    Y = ell+r-v
    A = (1+ell)*(P+r)*r
    C = x*(P+2*r)*ell+r*(P+r)*(1+x)-v*(P+v)
    G = (eta-lam)*(x*(V+v)+V*(eta-lam))+x*x*lam
    raw = {"Bgap_nonnegative": (x-b_num-P*(1+ell),2),
           "Y": (Y,1), "dlt1": (r+v-P*ell,2),
           "c-a": (lam-y*eta,2), "G": (G,3),
           "E1complex": (4*x*x*Y*A-C*C,6),
           "A4": (a_num-x*P*ell-4*x*y,3),
           "circle_gap": (a_num*(x+L*r)-b_num*x*(2*y+L*(1-r)),5),
           "height25": (Y*(x*(L-sp.Rational(5,2)-v)+V*(eta-lam))-2*C,3)}
    for j in range(7):
        raw[f"q{j}pos"] = (q[j],8)
        raw[f"q{j}neg"] = (-q[j],8)
    raw["target_q3neg"] = raw["q3neg"]
    raw["target_q4neg"] = raw["q4neg"]
    raw["target"] = raw["q4neg"]
    products = [("Y","height25"),("G","height25"),
                ("c-a","height25"),("dlt1","height25"),
                ("A4","Y"),("A4","c-a"),("G","c-a"),
                ("A4","dlt1"),("A4","G")]
    for a,b in products:
        raw[a+"__"+b] = (raw[a][0]*raw[b][0],raw[a][1]+raw[b][1])
    mu,rho = sp.symbols("mu rho")
    destination = (P,r,lam,mu,ell,eta,rho)
    h = P+r+lam+mu+rho
    replacement = (P,r,lam+mu,ell,lam,eta)
    polynomials = {name: homogeneous(expr,source,destination,replacement,d,h)
                   for name,(expr,d) in raw.items()}
    write_json(output/"0231-polynomials.json", polynomial_bundle(destination,polynomials))
    print("Derived order 0231 coefficients and factors")


def order_1320(output):
    x,L,G,k,P,E,w = sp.symbols("x L G k P E w")
    source = (x,L,G,k,P,E)
    first = [L+L*(x-k)*w,-P-(P+E)*w,
             L+G+(L+G)*(x-k-G)*w]
    sums = [L*k,P*(1-x)+E,(L+G)*(k+G)]
    second = [u*u-z*(1+w) for u,z in zip(first,sums)]
    third = [u**3-3*z*(1+w)*u-z*(1+w)*(1-2*x-x*w)
             for u,z in zip(first,sums)]
    core = quotient(determinant(first,second,third), G*L*(L+G), (*source,w))
    c = [sp.expand(core).coeff(w,j) for j in range(7)]
    F1 = -(first[1]*second[2]-first[2]*second[1])
    F3 = first[0]*second[1]-first[1]*second[0]
    r,h,z = sp.symbols("r h z")
    destination = (r,G,k,P,h,z,E)
    X = r+k+G
    LD = r+z
    h0 = X+h
    replacement = (X,LD,G,k,P,E)
    def hom(expr,degree):
        return homogeneous(expr,source,destination,replacement,degree,h0,
                           (1,1,1,1,1,2))
    base = {"E": E, "B": X*h0-E-P*h0-LD*(r+G), "gap": z,
            "GT": P*(LD*(h+k)-h*h0)+E*(LD-h0-X),
            "A": LD*(h+k)-E-4*h*h0,
            "H1": LD*k-P*h-E, "H3": P*(LD+P-k-h)-E,
            "Det": (X+2*h)*k-X*h-(LD+G)*G,
            "U": k*(X+4*h)-3*X*h-E-P*(h+k),
            "two_k_G": 2*k-G, "Z": LD+P-k-h, "V": X-P}
    factors = {"plain": sp.Integer(1), **base}
    for a,expr in base.items():
        for b,other in base.items():
            factors[a+"_"+b] = expr*other
    for j in range(7):
        factors[f"c{j}"] = hom(c[j],j+3)
        factors[f"negc{j}"] = -factors[f"c{j}"]
    for j in (3,4):
        for name,expr in base.items():
            factors[f"c{j}_"+name] = factors[f"c{j}"]*expr
            factors[f"negc{j}_"+name] = -factors[f"c{j}"]*expr
    factors["E1_1/2"] = hom(quotient(F1.subs(w,sp.Rational(1,2)),L+G,source),5)
    factors["E3_1"] = hom(quotient(F3.subs(w,1),L,source),5)
    write_json(output/"1320-positive-polynomials.json",polynomial_bundle(destination,factors))
    print("Derived order 1320 coefficients and factors for nonnegative GT")


def nonpositive_GT(output):
    p,q,R,E,m = sp.symbols("p q R E m")
    variables = (p,q,R,E,m)
    r,y = p+R,q+E
    M = -m
    A = p+q
    Delta = p+r-q-y
    h = Delta-3
    Y = y*p*q*r
    D = p*q*r+y*(p*r-q*(p+r))
    Z = (y+1)*(y+Delta-1)-(p*r-q*(p+r))
    W = r*(A*y+(A-1)*p)
    Dlambda = M*M+M*D+Y*(Delta-1)
    lambdaG = (M+W)/2
    H = 6*M+Z
    C2G = 15*m*m-m*(5*Z-sp.Rational(3,2)*h)-h*D-Y+h*W/2
    TG = 2*(p*r-q*y)*q*y*(y+p)*A-p*(q*y+m)*(-m+W+2*q*y+2*m)
    QGN = 5*Z*Z+12*Y+12*h*D-18*h*m-6*h*W
    c3G = (20*M**3+(10*Z-7*h-9)*M*M-((4*h+6)*D+4*Y)*M
           -D*D-Y*(h*h+h-2+2*Z)+3*(Delta*M+D)*lambdaG-2*lambdaG*lambdaG)
    low = [p,q,R,E,m,A-2,Delta,3-Delta,p*q-m,6*m-Z,Z,p*r-q*y,Dlambda,TG]
    high = [p,q,R,E,m,A-2,h,p*q-m,6*m-Z,Z,p*r-q*y,QGN,Dlambda]
    result = polynomial_bundle(variables,{"low_target":-2*C2G,
        "derivative_target":4*lambdaG-3*(Delta*M+D),
        "cubic_target":-54*(c3G-sp.Rational(5,54)*H**3),
        **{f"low_generator_{i}":value for i,value in enumerate(low)},
        **{f"high_generator_{i}":value for i,value in enumerate(high)}})
    write_json(output/"1320-nonpositive-polynomials.json",result)
    print("Derived the three polynomials for nonpositive GT")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=Path("build/f3"))
    parser.add_argument("--sector", choices=["all","0231","1320-positive","1320-nonpositive"],default="all")
    args = parser.parse_args()
    if args.sector in ("all","0231"): order_0231(args.output)
    if args.sector in ("all","1320-positive"): order_1320(args.output)
    if args.sector in ("all","1320-nonpositive"): nonpositive_GT(args.output)
