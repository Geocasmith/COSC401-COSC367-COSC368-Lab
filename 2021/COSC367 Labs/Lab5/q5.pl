%base case
remove(X,[],[]). %base case
remove(X,[X|As],B):-remove(X,As,B). %if head matches X, dont add head to list B
remove(X,[A|As],[A|B]):-remove(X,As,B). %if head matches X, add head to start of list B

test_answer :-
    remove(a, [a, b, a, c, d, a, b], L),
    writeln(L).