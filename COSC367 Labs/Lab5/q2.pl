swap12([Y, X | List],[X, Y | List]).


test_answer :-
    swap12([a, b, c, d], L),
    writeln(L).