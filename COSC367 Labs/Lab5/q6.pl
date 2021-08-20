split_odd_even([],A,B). %base case
split_odd_even([L|Ls],A,B).

%use length of list, if length even, last is even