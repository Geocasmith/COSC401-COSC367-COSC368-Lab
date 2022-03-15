unique([],[]).  % Complete the base case.

% In the following we consider two cases: a) The head does not appear in the tail; b) it does.

unique([H|T], [H|Set]) :-
    \+ member(H, T),
    unique(T, Set). % Complete

unique([H|T], Set) :-
    member(H, T), % Complete
    unique(T, Set).   % Complete