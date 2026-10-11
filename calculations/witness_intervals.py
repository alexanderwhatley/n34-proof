#!/usr/bin/env python3
"""Compute outward-rounded sample enclosures for the nine-root example.

Inputs are decimal strings, interpreted exactly. mpmath's interval context
propagates endpoint rounding through exp and log at 100 decimal digits.
Each output interval encloses the exact function value at its sample point.
"""
import mpmath as mp

TERMS = [
    ("1.0087711983885019", "0.0020954782173229", "1.2835032616093814"),
    ("1.3358363059764513", "1.0252846058508502", "0.9082951710178624"),
    ("0.9900599367225573", "2.0673123701130679", "-0.0016847698173825"),
]
SAMPLES = ["-0.25", "-0.2135", "-0.16", "-0.09", "0", "0.09",
           "0.15", "0.22", "1", "5"]


def value(u):
    u = mp.iv.mpf(u)
    x = 1 / (1 + mp.iv.exp(-u))
    return 1 - sum(mp.iv.mpf(coefficient) * mp.iv.exp(
        mp.iv.mpf(a) * mp.iv.log(x) + mp.iv.mpf(b) * mp.iv.log(1-x))
        for coefficient, a, b in TERMS)


if __name__ == "__main__":
    mp.iv.dps = 100
    print("Exact sample u | enclosure of F(1/(1+exp(-u)))")
    for u in SAMPLES:
        print(u, "|", value(u))
