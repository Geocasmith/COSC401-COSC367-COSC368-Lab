reversed([],[]). %base case
reversed([A|As],B):- reversed(As,Bs),append(Bs,[A],B).

test_answer :-
    reversed([1, 2, 3, 4, 5], L),
    writeln(L).