parent(albert, bob).
parent(albert, betsy).
parent(albert, bill).

parent(alice, bob).
parent(alice, betsy).
parent(alice, bill).

parent(bob, carl).
parent(bob, charlie).

/*
Recursion will pass the parent function into the child of a parent when called again

query related(albert,carl).
or related(Z,carl).
*/
%Base case
related(X, Y) :-
  parent(X, Z),
%Recursive case
related(X, Y) :-
  parent(X, Z),
  related(Z, Y).