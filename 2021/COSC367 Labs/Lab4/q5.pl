normal_tear_rate(RATE) :- RATE >= 5.
low_tear_rate(RATE) :- RATE < 5.
young(AGE) :- AGE < 45.

diagnosis(hard_lenses, AGE, yes, TEAR):- young(AGE),normal_tear_rate(TEAR).
diagnosis(soft_lenses, AGE, no, TEAR):- young(AGE),normal_tear_rate(TEAR).
diagnosis(no_lenses, _, _, TEAR):- low_tear_rate(TEAR).
    test_answer :-
    diagnosis(X, 19, no, 5),
    writeln(X).
