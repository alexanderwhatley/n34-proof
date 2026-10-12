# Prefix signs for a strict totally positive circuit

Read [the appendix terminology](../../appendix.md#terminology) before this technical lemma. All variables are local to this document.

A matrix is **strictly totally positive** if every square minor, of every possible size, is positive. A matrix is **totally nonnegative** if all of its square minors are nonnegative. A **prefix** here means the contribution from the first specified columns to a matrix product. A **kernel vector** is a nonzero vector sent to zero by the matrix.

## Statement

Let $`n\ge1`$, let $`M`$ be a strictly totally positive real matrix of size $`n\times(n+1)`$, and let $`v`$ be a kernel vector whose first coordinate is positive. Then its coordinates strictly alternate in sign. For every cut $`1\le k\le n`$, every coordinate of the complete prefix

```math
y=M_{[:,1:k]}v_{1:k}
```

is nonzero and has sign

```math
\boxed{\mathop{\mathrm{sign}}\nolimits (y_i)=(-1)^{k+1}.}
```

In particular, a strictly totally positive $`4\times5`$ block-collocation matrix annihilating $`(1,-1,1,-1,1)`$ has **strictly negative first-two complete-block prefix at every one of its four nodes**. Its first-three complete-block prefix is strictly positive at every node.

The theorem is an ordinary distinct-node matrix statement. It is not a paired-cofactor ratio inequality or a confluent extension.

## Proof

All maximal minors of $`M`$ are positive, so it has rank $`n`$. Its canonical kernel circuit is

```math
v_j=(-1)^{j-1}\det M_{\widehat j},\qquad1\le j\le n+1.
```

A general kernel vector with positive first coordinate is a positive multiple of this vector.

Use rectangular Neville factorization, that is, Gaussian elimination without row exchanges applied to a matrix whose minors are all positive:

```math
M=LU,
```

where $`L`$ is lower triangular totally nonnegative with positive diagonal, $`U`$ is upper echelon, and every minor of $`U`$ not forced to vanish by its echelon pattern is strictly positive. The input is a statement for arbitrary rectangular strictly totally positive matrices; no odd/even dimension condition enters that factorization.

Partition after the first $`k`$ rows and columns:

```math
U=\begin{pmatrix}A&B\\0&C\end{pmatrix}.
```

The bottom block $`C`$ has size $`(n-k)\times(n+1-k)`$. Put $`m=n+1-k`$, define positive maximal cofactors $`\Delta _j=det C_hat_j`$, and let

```math
d_j=(-1)^{j-1}\Delta_j,\qquad1\le j\le m.
```

Then $`Cd=0`$. All $`\Delta _j`$ are strictly positive admissible minors of $`U`$: after deleting a right-block column, its increasing selected column indices still dominate its increasing bottom-row indices. This includes the empty-row case $`k=n`$, with the empty determinant defined as one.

Because $`Uv=0`$ and $`ker C`$ is one-dimensional, the right tail of the original circuit obeys

```math
v_R=(-1)^k\lambda d,\qquad\lambda\gt0.
```

The orientation follows from the first right coordinate, whose index is $`k+1`$ and whose sign is $`(-1)^k`$.

For each top row $`b_i`$ of $`B`$, the bordered determinant

```math
E_i=\det\begin{pmatrix}b_i\\C\end{pmatrix}
```

is a strictly positive admissible minor of $`U`$. Expanding along its first row gives $`E_i=b_i d`$. Thus the prefix in the $`U`$ rows is

```math
(y^U)_i=-b_i v_R=(-1)^{k+1}\lambda E_i\quad(1\le i\le k),
```

and zero for the remaining rows. Its top $`k`$ entries therefore have the desired strict common sign.

Now $`y=Ly^U`$. Nonnegative entries of $`L`$ preserve the weak common sign. The first $`k`$ rows are strict because their positive diagonal terms are nonzero. For every later row, its first-column term is nonzero: upper-echelon $`U`$ has only one nonzero entry in its first column, so

```math
L_{i1}=M_{i1}/U_{11}\gt0.
```

Every row is consequently strict with sign $`(-1)^(k+1)`$. This proves the theorem.

## Explicit 4-by-5 algebra

Write

```math
U=\begin{pmatrix}
a&b&c&d&e\\0&f&g&h&i\\0&0&j&k&\ell\\0&0&0&m&n
\end{pmatrix}.
```

The bottom-right $`2\times3`$ circuit is

```math
(\Delta_1,-\Delta_2,\Delta_3),\qquad
\Delta_1=kn-\ell m\gt0,\quad\Delta_2=jn\gt0,\quad\Delta_3=jm\gt0.
```

The canonical full circuit's last three entries are $`af`$ times this vector. Define its positive bordered minors

```math
E_1=c\Delta_1-d\Delta_2+e\Delta_3\gt0,\qquad
E_2=g\Delta_1-h\Delta_2+i\Delta_3\gt0.
```

Then the first-two prefix in the upper rows is exactly

```math
(-afE_1,-afE_2,0,0)^T.
```

The lower totally nonnegative factor makes all four coordinates strictly negative, as above.

## Application to ordered sign blocks

For a strictly totally positive collocation kernel, disjoint ordered positive-measure sign blocks produce a strictly totally positive block matrix by determinant multilinearity and Fubini. If four distinct nodes are zeros of a signed sum with five nonempty ordered blocks beginning positive, absorb each block's positive magnitude into its column. The vector $`(1,-1,1,-1,1)`$ is then its circuit, so its first-two complete-block sum is strictly negative at all four nodes. No independent column normalization is being compared across different cofactors.

The statement gives only that prefix sign. A PS exclusion still needs to identify the complete blocks correctly and supply a pointwise comparison or a support landmark contradicting it. It does not by itself close a four-critical-point region. Raw Hermite rows and nonconsecutive/overlapping block grouping are outside the literal hypotheses.
