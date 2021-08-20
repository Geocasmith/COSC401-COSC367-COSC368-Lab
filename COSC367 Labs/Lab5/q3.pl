tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

write_list([Head|Tail]) :-
  write(Head), nl,
  write_list(Tail).

listtran([],[]).
listtran([A|As],[B|Bs]) :-
    tran(A,B),              %sets head of 2nd list to translation of head of 1st list
    listtran(As,Bs).        %calls recursive on tails
    %When exiting the recursion it translates the heads and adds them to list



test_answer :-
    listtran(X, [one, seven, six, two]),
    writeln(X).

/*
listtran([Head|Tail],[X]) :-
    Translated = tran(Head,Y).
  ([Translated|X],newList),
  listtran([Tail],newList).
*/