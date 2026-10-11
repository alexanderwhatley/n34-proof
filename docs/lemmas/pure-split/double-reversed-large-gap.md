# Uniform double-reversed five-root theorem when the smaller outer gap is at least one

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## 1. The actual source theorem

Let

(u,p,a,b,q,z)>0, q<a, p<b,
alpha=u+q, beta=p+z,

A(t)=(u+pt)(a-bt)[a+u-(b-p)t]-(ap+bu)t(1+t),
B(t)=(q+zt)(a-bt)[(b+z)t-(a-q)]+(az+bq)t(1+t).

For every rho>0 put

H(t)=A(t)+rho t^alpha(1+t)^(beta-alpha)B(t), t>0.

**Theorem.** If min(alpha,beta)>=1, H has at most five distinct positive roots. No integrality restriction, upper gap cutoff, coefficient word, critical-root simplicity, or exponent-band subdivision is needed.

Reflection preserves positive-root counts and swaps alpha,beta, so it is enough to assume beta>=alpha>=1. Sections 2--5 give a direct proof in that orientation. The more general profile statement proved along the way applies whenever the positive events interlace and either alpha>=1 or the negative root magnitudes satisfy x>=y.

## 2. The source itself forces interlaced positive events

Put c=a/b. The exact endpoint and central signs are

A(0)=au(a+u)>0, A(c)=-(ap+bu)c(1+c)<0,
A3=bp(b-p)>0,

B(0)=-aq(a-q)<0, B(c)=(az+bq)c(1+c)>0,
B3=-bz(b+z)<0.

Therefore each cubic has exactly two simple positive roots, one on each side of c, and one simple negative root. Write

A/A3=(t+x)(t-Q)(t-R),
B/B3=(t+y)(t-P)(t-S),

with x,y>0, Q<c<R, P<c<S.

Here is the band-free source comparison proving P<Q and S<R. Set

gammaA=u/p, gammaB=q/z,
lambda=(a+u)/(b-p), mu=(a-q)/(b+z).

For t>0,t!=c define

bA(t)=p(t+gammaA)/(t-c)
 +(c+gammaA)t(1+t)/[(t+gammaA)(t-c)^2],

bB(t)=-z(t+gammaB)/(t-c)
 +(c+gammaB)t(1+t)/[(t+gammaB)(t-c)^2].

The exact normalized identities are

(b-p)(A/A3)/[(t+gammaA)(t-c)^2]=b-bA(t),
(b+z)(B/B3)/[(t+gammaB)(t-c)^2]=b-bB(t).

All prefactors preserve signs. Direct subtraction gives

bA(t)-bB(t)=N(t)/(t-c),
N(t)=alpha+beta t-(pq-uz)t(1+t)/[(u+pt)(q+zt)].

If pq-uz<=0, N(t)>0. Otherwise 0<pq-uz<pq and

(u+pt)(q+zt)>ptq,

so

N(t)>alpha-1+(beta-1)t>=0.

The strict first inequality makes N(t)>0 even on alpha=beta=1.

At P<c, bB(P)=b and the comparison gives bA(P)<b. Hence A(P)/A3>0. Since P<c<R, this forces P<Q. At R>c, bA(R)=b and bB(R)<b, so B(R)/B3>0. As R>c>P, this forces S<R. Consequently

0<P<Q<c<S<R.

This is a source-level comparison valid throughout min(alpha,beta)>=1; it does not invoke the old exceptional Pascal row or any integer band.

## 3. A Cauchy charge budget bounds the useful critical points

Let delta=beta-alpha>=0 and

F(t)=-A/[t^alpha(1+t)^delta B]>0.

Its three positive components are (0,P),(Q,S),(R,infinity). The logarithmic derivative is

L=F'/F
=1/(t+x)-1/(t+y)+1/(t-Q)+1/(t-R)
 -1/(t-P)-1/(t-S)-alpha/t-delta/(1+t).

Its finite source charges are +1 at -x,Q,R; -1 at -y,P,S; -alpha at 0; -delta at -1. Their total is -beta.

On a finite component (l,r), use X=(t-l)/(r-t) and rates lambda_s=(l-s)/(r-s). For each finite source s!=r,

(dt/dX)/(t-s)=1/(X+lambda_s)-1/(X+1).

Include the exact infinity padding +beta at rate 1, so the total charge is zero and the common gauge cancels. The padded original-coordinate term is zero, and its transformed identity is exactly 0=1/(X+1)-1/(X+1). Thus the transformed L is the Cauchy-square integral of its cumulative charge density:

(dt/dX)L(t(X))=int_0^infty w(v)/(X+v)^2 dv.

For the unbounded right component, translation X=t-R gives the same integral representation without padding.

**Left component.** The initial density is -alpha at source 0. The three negative-axis charges +1,-1,-delta occur before rate 1. Every partial density among them is nonpositive when alpha>=1: there is at most one positive unit jump and all other jumps are nonpositive. Their net charge is -delta, so the density after all three is -beta. The infinity padding brings it to zero; the remaining physical sources occur in rate order R,S,Q, with charges +1,-1,+1 and densities 1,0,1. Hence the zero-safe density has at most one sign variation.

**Middle component.** The initial Q charge gives density 1; the physical left source P subtracts one to zero; source 0 then gives -alpha. The same three negative-axis charges keep the density nonpositive and end at -beta. Padding brings it to zero; the physical right source R gives final density 1. Hence there are at most two sign variations.

**Right component.** In the translation chart, the physical sources R,S,Q,P give densities 1,0,1,0. Source 0 gives -alpha, and the three negative-axis charges keep the density nonpositive and end at -beta. Hence there is at most one sign variation.

The kernel (X+v)^(-2), X>0,v>=0, is strictly totally positive. Borchardt's identity expresses each collocation determinant as the positive Cauchy determinant times the positive permanent. Grouping the consecutive nonzero density pieces into ordered sign blocks and integrating against their positive magnitudes produces a strictly positive collocation determinant for the block transforms, by multilinearity and Fubini. A nontrivial signed sum of k such transforms cannot vanish at k distinct positive nodes. Infinite final blocks follow by monotone truncation, with determinant strictness supplied by finite positive-measure subintervals.

The number of distinct zeros of L on the three components is therefore at most

1,2,1,

respectively. By ordinary Rolle, any positive level of F has at most two hits on either outer component and at most three on the middle component. Critical multiplicities need no separate assumption for this distinct-root statement.

The same critical budget holds under the alternative condition x>=y, even when alpha<1: in every chart, the negative charge at -y then precedes the positive unit charge at -x, so that positive jump only undoes an earlier negative unit jump and never makes the negative-axis density positive.

Factor the positive profile as

F=C0 Pi(t) W(t), C0=-A3/B3>0,
Pi(t)=(t-Q)(t-R)/[(t-P)(t-S)],
W(t)=(t+x)/(t+y) t^(-alpha)(1+t)^(-delta).

For every l in (0,P), both ordered factor comparisons give Pi(l)>1. For every r>R, both give 0<Pi(r)<1.

W is strictly decreasing when alpha>=1. Indeed

(log W)'=(y-x)/[(t+x)(t+y)]-alpha/t-delta/(1+t),

and

1/t-(y-x)/[(t+x)(t+y)]
=[t^2+2tx+xy]/[t(t+x)(t+y)]>0.

Thus (log W)'<0 when alpha>=1. If x>=y, its first term is nonpositive and strict decrease holds for every alpha>0 as well.

Consequently, for every l in (0,P) and r>R,

F(l)>C0 W(l)>C0 W(r)>F(r).

No positive level can meet both outer components. At most one outer component contributes, with at most two hits, and the middle contributes at most three. Hence F=rho has at most five distinct roots, proving the theorem for beta>=alpha>=1.

## 5. Reflection and exact scope

The source reflection swaps the parameter sextuple as

(u,p,a,b,q,z) -> (z,q,b,a,p,u),

and swaps alpha,beta. If Anew,Bnew denote the reflected cubics, then

Anew(s)=-s^3 Bold(1/s), Bnew(s)=-s^3 Aold(1/s).

With rhonew=1/rho,

Hnew(s)= -s^(beta+3)(1+s)^(alpha-beta)/rho * Hold(1/s).

The prefactor never vanishes for s>0; reflection therefore preserves distinct positive roots. This completes the full min(alpha,beta)>=1 result.

The theorem includes equal gaps, integer gaps, singly integral gaps and internal critical-root collisions at the stated distinct-root scope. It needs only strict positive source magnitudes, q<a,p<b and the minimum-gap condition; source coordinate equalities outside those strict hypotheses still require the original perturbation. A stronger auxiliary multiplicity bound is not claimed here.

The broader profile argument proves F-level<=5 for any genuine interlaced source with beta>=alpha>0 satisfying x>=y. Interlacing must be checked independently if alpha<1; it is automatic from Section 2 when alpha>=1.

## 6. Original proof reduction

The theorem covers all six unordered exponent-band pairs whose indices lie in {1,2,3}:

I1xI1, I1xI2, I1xI3, I2xI2, I2xI3, I3xI3.

It also covers all their integer-gap walls and the entire positive-integer outer-gap lattice. Their main no-ten consequences now follow from this single analytical argument plus the retained projective interface.

In particular the middle I2xI2 paired-Darboux cofactor theorem is unnecessary for these double-reversed inputs. Its independent positive-column-rescaling warning remains valid; the present proof simply avoids that determinant altogether.

The four pairs involving I0, namely I0xI0,I0xI1,I0xI2,I0xI3, remain outside the unconditional minimum-gap theorem. The conditional x>=y extension may cover part of those sources after interlacing is verified. No entire low-gap pair is declared removed by that extension alone.
