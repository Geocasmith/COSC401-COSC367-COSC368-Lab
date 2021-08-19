/*
Structures provide context to what and object is

Structure is made of functor followed by arguments.
Arity is number of arguments
eg owns(albert,pet). the functor owns has arity of 2 w/ arguments alber and pet

*/

owns(albert, pet(cat,olive)).
%eg owns(albert, pet(X,olive)).

/*
More use of structures.
Hint: use _ for variables you do not care about.

Input below: customer(sally, _, Balance).
You want to store 120.55 in Balance, do not care about sallys last name
and match sally
*/

customer(tom, smith, 20.55).
customer(sally, smith, 120.55).

get_cust_bal(FName, LName) :- customer(FName, LName, Bal),
  write(FName), tab(1),
  format('~w owes us $~2f ~n', [LName, Bal]).

/*
Example: defining vertical and horiz lines

Input: vertical(line(point(5, 10), point(5, 20))).
Input to ask what val for vert: vertical(line(point(5, 10), point(X, 40))).
Input to ask what line point needed(put in var as point):
 vertical(line(point(5,10),X)).
*/
vertical(line(point(X, Y), point(X, Y2))).
horizontal(line(point(X, Y), point(X2, Y))).
