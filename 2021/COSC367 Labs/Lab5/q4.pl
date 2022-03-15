%base case, stopping point
twice([],[]).

%Recursion
twice([A|As],B):-
    append([A,A],C,B),
    twice(As,C).

test_answer :-
    twice([a, b, c, d], L),
    writeln(L).

/*
twice([A|As],[B|Bs]):-
    B = [A,A],
    twice(As,Bs).
   */