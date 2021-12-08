pkg load symbolic
syms lambda
A = [1 4;
     0 5];
I = eye(rows(A));
M = A-I*lambda
d = det(M)
p = expand(d);
r = roots(sym2poly(p))
