second([Y, X | List],X).

test_answer :-
    second(L, X),
    writeln('OK').