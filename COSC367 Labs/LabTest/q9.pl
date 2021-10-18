merge([], ListB, ListB).   % Complete one of the two base cases
merge(ListA, [], ListA).    % Complete the other base case

merge([X | ListA], [Y | ListB], [X | Merged]) :-
    X < Y,
    merge(ListA, [Y | ListB], Merged).

merge([X | ListA], [Y | ListB], [Y | Merged]) :-
    Y < X,
    merge([X | ListA], ListB, Merged).