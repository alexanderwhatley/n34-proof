# The complete mixed positive-coefficient height theorem

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

## Original-row theorem

Let A,B,a,b,c,nu>0 and B>nu. For arbitrary real C0 and positive
E0,E1,E2, put

f(t)=C0-E0*t^(-A)*(1-t)^(-B)
            -E1*t^a*(1-t)^b-E2*t^c*(1-t)^(-nu),  0<t<1.

Then f has at most eight distinct interior zeros. There is no restriction
on c versus a or nu, on c-a versus b+nu, on the relative modes, or on
any physical/exterior/conjugate cofactor root pattern.

If C0<=0 the row is strictly negative. If C0>0, divide all coefficients
by C0 when applying a source lemma stated with constant one.

## Complete strict dispatch

Use rho=t(1-t), D=rho*d/dt, the slopes

ell0=-A+(A+B)t, ell1=a-(a+b)t, ell2=c-(c-nu)t,
    Pi=elli^2+Delli,
    R=ell1*P2-ell2*P1, V=ell2*P0-ell0*P2,
    C=ell0*P1-ell1*P0, W=det[ell;P;Q], Qi=elli*Pi+DPi.

On a generic source with c>a, R(0)>0 and R(1)<0. Its degree is at
most three, so it has one or three physical roots. Write
mu=A/(A+B), m=a/(a+b). The following cases are exhaustive.

| Source condition | Proved input |
|---|---|
| c<a | reversed-first-gap theorem, the earlier proof |
| c>a, three physical R roots | all-scale three-R-root theorem, the earlier proof |
| c>a, one physical R root r, mu>m | mode-aligned theorem, the earlier proof |
| c>a, one physical R root r, mu<m, V(r)>0 | nonstraddling theorem, the earlier proof |
| c>a, one physical R root r, V(r)<0 | New analytical straddling endpoint theorem, the earlier proof |

Each entry gives the eight-distinct-root bound. The three-R-root source
automatically satisfies the translated pair lemma's additional conditions;
these are conclusions of its root geometry, not missing assumptions.
Neither one-R-root estimate requires c>nu or a relative-gap condition.

The new endpoint proof has one quantitative step. At the late root d of C,
its positive quadratic quotient gives

C''(d)/C'(d)<4/(d-m),
    ell0(d)/rho(d)<1/(d-m),
    W'(d)/W(d)=C''(d)/C'(d)
                +(rho'(d)-ell2(d)+ell0(d))/rho(d)-1/(d-m).

Consequently (d-r)W'(d)/W(d)<5. Since W(r)<=0, W(d)<0 and
deg(W)<=6, the endpoint root-budget lemma gives at most four distinct
W roots on (r,d), without assuming W is negative throughout it.
The auxiliary ratio has at most five fixed-level contacts there; the late
positive original-derivative component has at most six level contacts,
and the initial component at most one. Thus f' has at most seven roots
and f at most eight. This replaces every internal straddling C-type and
nonphysical-pair split by one argument.

## All source equality and collision faces

Suppose an exceptional strict row had nine distinct zeros. Analyticity
makes those selected zeros isolated. A small constant shift retains one
crossing near each odd-order zero and splits the larger group of even
minima or maxima, giving at least nine simple zeros in disjoint compact
sign brackets. Avoid critical levels and then perturb the original
supports generically in those brackets. All six positivity inequalities
and B>nu remain open; the finite proper algebraic source exceptions
can be avoided. Their properness witnesses and lower-order alternatives
are part of the source inputs and the complete assembly above.

## Nonnegative support faces and identities

The original-row bound extends to A,B,a,b,c,nu>=0, B>=nu, provided
the row is not identically zero. Shift nine hypothetical isolated zeros
into compact sign brackets as above and approximate, for epsilon>0, by

(A+epsilon,B+2epsilon,a+epsilon,b+epsilon,c+epsilon,nu+epsilon).

These are strict source parameters with B'>nu'; their original functions
converge on the selected compact brackets, giving the same contradiction.

For positive E0,E1,E2, the only weak original-row identities are:

1. A=B=a=b=c=nu=0 and C0=E0+E1+E2;
2. A=B=nu=a=0, b=c=1 and E1=E2=C0-E0>0.

Indeed an identity forces A=B=0 by the inverse atom's endpoint blowup,
then nu=0. The two remaining positive beta atoms can sum to a constant
only in the all-constant case or the affine identity t+(1-t)=1, as
proved in [the least-support identity proof](least-support-identities.md).

## Mixed height consequence

Let

u=t^A*(1-t)^B,
    v=t^(A+a)*(1-t)^(B+b),
    w=t^(A+c)*(1-t)^(B-nu), S=u-c3*v-c4*w,

with nonnegative parameters B>=nu and c3,c4>0. Every positive-level
equation S=c1 has at most eight distinct roots unless it is an identity.
The same parameters satisfy the nine-sample master height inequality

min(S(x1),S(x3),S(x5),S(x7),S(x9))
       <= max(0,S(x2),S(x4),S(x6),S(x8))

for every ordered nine interior samples. A strict-support violation gives
ten level crossings because all actual atoms vanish at both endpoints;
weak supports follow by fixed-sample continuity. There is no relative
gap, lobe, mode, or cofactor-type condition left in this mixed theorem.

## Dependencies and source-level impact

The inputs are the earlier proof reversed-gap, three-R-root,
mode-aligned and nonstraddling theorems; the self-contained new
straddling theorem; and compact original-row regularization. The prior
small-gap, exterior-pair, three-C-root and quadratic four-root statements
remain valid stronger/signed corollaries but are not needed in this
positive-coefficient assembly.

The theorem replaces both complete original inputs NOLOBE and GENUINE
at the main proof's distinct-root scope: all six NOLOBE event families
and all nine GENUINE decisions. It does not claim the older standalone
GENUINE multiplicity theorem. The exact original-source map is separate.
An unrestricted nonnegative-support height corollary additionally uses
the retained local SUPPORT refinement and the least-support master; that
broader implication must not be confused with this mixed normal form.
