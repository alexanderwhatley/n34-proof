# Auxiliary lemmas for the upper-low C3 slope support theorem

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Let 0<h<1/2, l>1, 0<a<b<xi, d=b-a, L=a+l, M=b+l. Normalize the wall polynomial by H/[P(P-1)]=(r+h)(r-xi). Write x=(a+h)(xi-a), z=(b+h)(xi-b), y=x+z+d², and C3=A3+kD3 with D3=2d²(L²z-M²x). Set

```
A=a+h, B=b+h, s=l-h, S=A+B, T=AB,
X=xi+h, e=1-2h, tH=2h(1-h), la=a+l, G=a+b+2ab.
```

The exact symmetric formula is A3=d F(X)/X², where

```
F(X)=f3 X³+f2 X²-f1 X+f0,
f3=4S(T-e s)+tH(2s-S),
f2=4e(sS²+2ST+2sT)+2sST-4T²+tH(S²+sS+2T),
f1=6eT(2T+sS)+3tH(3ST+sS²+2sT),
f0=6tH T(2T+sS).
```

Thus f1>0. The wall relation used in this normalization is P-1=2[xi-h(1+2xi)]/(xi+h)² and Q=(P-1)(xi-h)/2.

## Positive middle coefficient at the zero-slope boundary

The slope condition is

```
L²z-M²x=d[(s²-T)X-s(2T+sS)].
```

At D3=0 one necessarily has E=s²-T>0 and X=s(2T+sS)/E. Direct substitution gives

```
A3=2AB*d*Fboundary/(s² E),
```

where Fboundary is the quadratic polynomial in T stored as F_terms in [the zero-slope coefficient table](../../../calculation-data/positive/c3_support/C3_D3ZERO_POSITIVE_CERTIFICATE.json). Its coefficients are

```
[T²] = 3h²+6hs-3h+2s²-3s,
[T]  = -s(4h²s-3h²S+4hs²-8hsS-4hs+3hS
           +2s³-3s²S-2s²+4sS),
[T⁰] = -s²(3h²s²+3h²sS-h²S²+2hs³-3hs²
           -4hsS²-3hsS+hS²-s³S-s³-2s²S²+2sS²).
```

Here S>2h and 0<T<min(s²,S²/4). Express this quadratic in the degree-two Bernstein basis on [0,Tmax]. The coefficients are b0=Fboundary(0), b1=b0+(Tmax/2)Fboundary'(0), b2=Fboundary(Tmax).

For S>=2s use Tmax=s² and S=2s+z. For 2h<S<2s use Tmax=S²/4 and S=2h+2(1-2h+t)w/(1+w). In both cases s=1-h+t with t=l-1>0 and h=u/[2(1+u)]. The common b0 certificate uses S=2h+z. After clearing positive denominators, the five lifts have respectively 118,125,123,336,335 strictly positive coefficients. This proves Fboundary>0 and hence A3>0 at D3=0. The S=2s boundary belongs to the first chart.

The source bound kd²L<G reduces the negative-slope problem to positivity of

```
Z=la*F(X)+2G X²[(s²-T)X-s(2T+sS)]
 =K3 X³+K2 X²+K1 X+K0,
K3=la*f3+2G(s²-T), K2=la*f2-2G*s(2T+sS),
K1=-la*f1<0, K0=la*f0>0.
```

For the native lower endpoint B, the condition (1-2h)B>2h(1-h) is equivalent to h<b/(1+2b). The complete positive chart is

```
b=a+d, h=b*q/[(1+2b)(1+q)], l=1+t,
a,d,q,t>0.
```

The following two polynomials have 430 and 327 strictly positive coefficients, listed in [the cubic-shape table](../../../calculation-data/positive/c3_support/C3_CUBIC_SHAPE_AT_B_COEFFICIENTS.json), after multiplying by the positive wall-chart denominator cubed:

```
I1=Z'(B)-(d/4)Z''(B)>0,
I2=B*K3+K2>0.
```

If K3>=0, then Z''(B)=2I2+4BK3>0 and Z'(B)>0. Since K1<0, the quadratic Z' has one positive zero (or the linear limiting case has one), so Z'>0 after B.

If K3<0 and Z'(B)<0, then I1>0 implies Z''(B)<0. Since Z'' decreases with X, Z' stays negative after B. If K3<0 and Z'(B)>=0, the concave quadratic Z' can cross from positive to negative only once after B. In every case Z has no interior minimum on an interval beginning at B.

## Positive leading coefficient on an unbounded support interval

If T>=s², then D3<=0 holds for all X>0. The leading coefficient satisfies the exact identity

```
K3=(T-s²)(4laS-2G)
   +la[S(tH+4t(1+t))+2s*tH],  t=l-1,
4laS-2G=2[2a²+(2l-1)(a+b)+4h(a+l)]>0.
```

Therefore $K_3>0$, so together with the endpoint shape statements the cubic increases on the unbounded interval.

## Scope of the complete support argument

For $T<s^2$, the condition $D_3\le0$ restricts $X$ to the interval from $\max(B,t_H/e)$ to $X_0=s(2T+sS)/(s^2-T)$. The boundary lemma proves $Z(X_0)>0$ because the slope term vanishes there. Positivity at the lower endpoint and the no-interior-minimum argument then give $Z>0$ throughout the interval. When $t_H/e$ is the lower endpoint, the [native endpoint lemma](c3-native-lower-endpoint-and-derivative-lemmas.md) supplies $Z'(t_H/e)>0$, including equality of the two possible lower endpoints.

For $T\ge s^2$, the positive leading-coefficient identity and the endpoint shape statements give positivity on the whole unbounded interval. With $kd^2L<G$, this proves $C_3>0$ whenever $D_3\le0$. The [full support theorem](c3-upper-tail-quadratic-slope-support-theorem.md) combines these auxiliary statements and the native endpoint signs.
