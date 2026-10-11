#!/usr/bin/env python3
"""Calculate the four positive coefficient expansions for the F24 bound.

The input is the exact F23 multiplier identity supplied with the proof.
From its multipliers this calculation builds A_E and R_E, then applies
the two positive-variable substitutions in the small-first-root lemma.
The output lists every nonzero integer coefficient of all four expansions.
"""
import argparse
import gzip
import json
from pathlib import Path
from math import comb
import sympy as sp


def polynomial(rows, variables):
    return sum(sp.Integer(coefficient)*sp.prod(v**p for v,p in zip(variables,powers))
               for powers,coefficient in rows)


def lift(expression, variables, bound, a_degree, h_degree):
    """Clear the displayed substitution denominator term by term."""
    result={}
    for powers, coefficient in sp.Poly(expression,*variables).terms():
        ia,id_,ic,ih,iz=powers
        if bound == "a_lt_one_seventh":
            prefactor=int(coefficient)*7**(a_degree-ia)*2**(h_degree-ih)
            v_power=ih
            v_extra_degree=h_degree-ih
        else:
            prefactor=int(coefficient)*2**(h_degree-ih)
            v_power=ia+ih
            v_extra_degree=h_degree-ia-ih
        for i in range(a_degree-ia+1):
            for j in range(v_extra_degree+1):
                key=(ia+i,id_,ic,v_power+j,iz)
                result[key]=result.get(key,0)+prefactor*comb(a_degree-ia,i)*comb(v_extra_degree,j)
    return [{"powers":list(powers),"coefficient":str(coefficient)}
            for powers,coefficient in sorted(result.items()) if coefficient]


def main(output):
    repo=Path(__file__).resolve().parents[1]
    source=repo/"calculation-data/positive/f24_certificate/NATURAL_F23_EXACT_INTEGER_CERTIFICATE.json.gz"
    with gzip.open(source,"rt",encoding="utf-8") as stream:
        data=json.load(stream)
    a,d,c,h,z=variables=sp.symbols("a d c h z")
    multipliers={}
    for name,powers,coefficient in data["weights"]:
        multipliers.setdefault(name,[]).append((powers,coefficient))
    H=polynomial(multipliers["H"],variables)
    PE=polynomial(multipliers["negative_E"],variables)
    P2=polynomial(multipliers["D2"],variables)
    Rpos=polynomial(data["remainder_terms"],variables)
    b,xi,L,M=a+d,a+d+c,a+z+1,a+d+z+1
    x,y=(a+h)*(xi-a),(b+h)*(xi-b)
    R2=L*L*(x+y+d*d)-6*L*M*x
    AE=3*L*M*PE+H*R2
    RE=3*L*M*(Rpos+P2*R2)
    output.mkdir(parents=True,exist_ok=True)
    for chart,parameters in [("a_lt_one_seventh",((4,3),(12,8))),
                             ("a_lt_two_h",((4,5),(12,13)))]:
        for name,expression,degrees in zip(("AE","RE"),(AE,RE),parameters):
            rows=lift(expression,variables,chart,*degrees)
            result={"variables":["u","d","c","v","z"],
                    "chart":chart,"polynomial":name,"terms":rows}
            target=output/(chart+"-"+name+".json.gz")
            temporary=target.with_suffix(".tmp")
            with gzip.open(temporary,"wt",encoding="utf-8") as stream:
                json.dump(result,stream,indent=2)
                stream.write("\n")
            temporary.replace(target)
            print(chart,name,": wrote",len(rows),"nonzero integer coefficients")


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=Path("build/f24-expansions"))
    main(parser.parse_args().output)
