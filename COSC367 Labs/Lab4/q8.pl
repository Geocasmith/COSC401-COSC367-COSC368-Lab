
mirror(leaf(X),leaf(X)).
mirror(tree(L1,R1),tree(L2,R2)):-mirror(L1,R2), mirror(R1,L2).

test_answer :-
    mirror(tree(leaf(foo), leaf(bar)), tree(leaf(bar), leaf(foo))),
    write('OK'),
    halt.

test_answer :-
    write('Wrong answer!'),
    halt.
