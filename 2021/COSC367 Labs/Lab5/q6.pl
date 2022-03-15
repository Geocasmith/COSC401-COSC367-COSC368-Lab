split_odd_even([],[],[]). %base case
split_odd_even([X],[X],[]). %base case cannot be recursive
split_odd_even([L,M|Ls],[L|A],[M|B]):-split_odd_even(Ls,A,B).

%When it hits the base case there are two empty lists, when it recurses up from
%there L is added to the first empty list, M is added to the other
%When it comes back up they are added to the front of the lists

test_answer :-
    split_odd_even([1,2,3,5], A, B),
    write(A),
    writeln(B).

%use length of list, if length even, last is even