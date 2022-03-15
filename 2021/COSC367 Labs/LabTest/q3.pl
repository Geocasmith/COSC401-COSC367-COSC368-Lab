zero_or_one(D):- D = 0; D = 1.  % Complete
zero_or_one_sequence([H|T]) :- zero_or_one(H), (T=[]; zero_or_one_sequence(T)).
binary_number([0, b | Ds]) :- zero_or_one_sequence(Ds).

test_answer :- binary_number([0, b, 1, 0, 1]),
               writeln('OK').
