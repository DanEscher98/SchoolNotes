---
autor: Daniel Sanchez
title: Operaciones con matrices
header-includes:
- \usepackage{ amsmath }
- \usepackage{ amssymb }
- \usepackage{ mathrsfs }
---


$$\begin{aligned}
Ax &= B \\
A^{-1}Ax &= A^{-1}B \\
Ix &= \frac{\text{adj}(A)}{\text{det}(A)}B \\
x &= \frac{\text{adj}([a_{ij}]_{n \times n})}{\text{det}(A)}B \\
x &= \frac{[A_{ij}]_{n \times n}^T}{\text{det}(A)}B \\
x &= \frac{[(-1)^{i+j}M_{ij}]^T}{\text{det}(A)}B \\
\frac{\text{cof}(A)^T}{|A|}B &= x
\end{aligned}$$

$$\begin{aligned}
Au &= \lambda u \\
Au - \lambda u &= 0 \\
(A - \lambda I) &= 0 \\
|A - \lambda I| &= 0
\end{aligned}$$

$$|A_n| = \begin{cases}
    a &,\: A_1 = [a] \\
    \sum_{j=0}^{n-1}(-1)^j a_{0j} |M_{0j}|
\end{cases}$$
