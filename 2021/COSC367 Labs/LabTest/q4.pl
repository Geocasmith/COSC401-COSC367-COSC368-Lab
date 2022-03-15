pair(a, t).
pair(c, g).
match(X, Y) :- pair(X,Y); pair(Y, X).
dna([], []).   % Complete the base case
dna([H1|T1], [H2|T2]) :- match(H1,H2),dna(T1,T2).  % Complete