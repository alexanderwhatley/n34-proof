# A pole-free mixed theorem for the reversed first-coordinate gap

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. Its variables are local to this document.

Let A,B,a,b,c,nu>0, with B>nu and c<=a. For E0,E1>0 and any real E2,

f=1-E0 h0-E1 h1-E2 h2,
    h0=t^(-A)(1-t)^(-B),
    h1=t^a(1-t)^b, h2=t^c(1-t)^(-nu),

has at most eight distinct interior roots. Neither c>nu nor positivity
of E2 is required. In the original height coordinates,

u=t^A(1-t)^B,
    v=t^(A+a)(1-t)^(B+b),
    w=t^(A+c)(1-t)^(B-nu),

the nine-sample inequality holds for S=u-E1 v-E2 w. All six actual beta
exponents are positive. This gives a mixed family beyond the least-support
master, and permits either sign for the coefficient of w.

## One monotone derivative anchor

For c<a, use rho=t(1-t), D=rho d/dt, and

ell0=-A+(A+B)t, ell1=a-(a+b)t, ell2=c-(c-nu)t,
    Pi=elli^2+D elli, Qi=elli Pi+D Pi,
    R=ell1 P2-ell2 P1,
    V=ell2 P0-ell0 P2,
    W=det[[ell0,ell1,ell2],[P0,P1,P2],[Q0,Q1,Q2]].

Since ell2=c(1-t)+nu t>0, h2'>0 everywhere. Put

r0=h0'/h2', r1=h1'/h2'.

Ordinary differentiation gives the exact identities

r0'=(h0/h2)V/(rho ell2^2),
    r1'=-(h1/h2)R/(rho ell2^2).                    (1)

Ten original roots therefore give nine zeros of

-f'/h2'=E0 r0+E1 r1+E2,

and then eight zeros of G=E0 r0'+E1 r1'. At a generic core source these
are eight contacts of the one positive auxiliary ratio level

Psi=(h1/h0)R/V=E0/E1, RV>0.                   (2)

The coefficient E2 has disappeared through differentiation. No source
interval I and no pole of a nonmonotone beta ratio is introduced.

## Five critical points and two useful intervals

R and V are cubics. Their endpoint signs are

R(0)=ac(c-a)<0, R(1)=-b nu(b+nu)<0,
    V(0)=Ac(A+c)>0, V(1)=B nu(B-nu)>0.

Each has either zero or two simple physical roots on the generic source.
Their opposite-sign loci are therefore single intervals or empty.
The useful set {RV>0} is the symmetric difference of {R>0} and {V<0},
so it has at most two components. V never vanishes inside this useful set.

The direct source Jacobi identity is

rho(R'V-RV')+(ell1-ell0)RV=-ell2 W.             (3)

Consequently

Psi'=-(h1/h0)ell2 W/(rho V^2).

W has degree at most six and endpoint values

W(0)=Aac(A+a)(A+c)(a-c)>0,
    W(1)=-B b nu(B-nu)(B+b)(b+nu)<0.

Opposite endpoint signs force odd total physical multiplicity. Thus a
degree-at-most-six W has at most five physical roots, with multiplicity.
The auxiliary ratio has at most five physical critical points, and componentwise
Rolle gives at most 5+2=7 contacts of one common positive level in {RV>0}.
This contradicts the eight contacts forced by ten original roots.

## Nongeneric rows and the equality face

If a strict original row had nine distinct roots, an arbitrarily small
common constant shift retains at least nine simple roots in compact
brackets. Odd zeros retain a crossing in either direction; even minima
and maxima split under opposite shifts, so choose the larger group.
Both endpoint germs of f are negative infinity (A>0,B>nu), regardless of
the real E2. Hence a regular nearby row has an even simple-root count
and at least ten roots. Perturb its supports generically within c<a,
preserving the compact sign brackets, to obtain the contradiction above.

The equality c=a follows by approximation from c<a preserving all
selected finite brackets. A strict nine-sample height violation also
persists under that approximation and produces ten crossings toward
the two zero endpoints of the actual beta atoms. This proves the stated
height inequality and root bound on the closed first-gap face.

This proof invokes no complete mixed decision table, complete N(3,4)
theorem, exterior-root atlas or computer-algebra sign certificate. The
companion standard-library script checks the displayed source identities
and one properness witness. Its finite witness is not a universal proof.
