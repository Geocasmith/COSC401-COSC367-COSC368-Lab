max(X,Y,X) :- X >= Y.
max(X,Y,Y) :- Y >= X.

max([X], X).   % Complete the base case (when the list has one element)
max([Head|Tail],Max) :-
    Tail = [_|_], % tail is not empty (i.e. the list has two or more elements)
    max(Tail, TailMax),
    max(###, ###, ###).  % Complete