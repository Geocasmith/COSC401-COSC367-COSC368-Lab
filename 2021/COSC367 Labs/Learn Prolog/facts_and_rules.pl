/*
NOTE: use [filename]. instead of consult(filename).
*/

%loves(romeo, juliete). Atoms romeo and juliet are inside predicate loves()

% "Rule, if item on right is true then item on left is true. AND = ,"
loves(juliet,romeo):-loves(romeo,juliet).

%Variable, represented by uppercase.



%"Facts. Typing male(X),female(Y). will plug in male to X and female to Y. Typing ';' will cycle"
%"until all possibilities done"
male(albert).
male(bob).
male(bill).
male(carl).
male(charlie).
male(dan).
male(edward).

female(alice).
female(betsy).
female(diana).


%"Rules, a fact is defined by other facts. (:- means if). (AND = ,) (Use 2 rules w/ diff bodies for OR)"
%"write() command prints"
%"If you try run rules w/o defined facts you will get error"
happy(albert).
happy(alice).
happy(bob).
happy(bill).
with_albert(alice).

runs(albert):-happy(albert).

dances(alice):-happy(alice), with_albert(alice).

does_alice_dance:-dances(alice), write('When alice happy she dances w albert').

% "OR statement example:"
swims(bill):- happy(bill).
swims(bill):- near_water(bill).

/*"Variables"
"Query parent(X,bob) will find constants that fit X in rules"
*/
parent(albert, bob).
parent(albert, betsy).
parent(albert, bill).

parent(alice, bob).
parent(alice, betsy).
parent(alice, bill).

parent(bob, carl).
parent(bob, charlie).

/*
More complicated variable queries
Can do more complicated queries like parent(X,bob),dances(X).

Logic queries
Example: find carls gandparents
Query: parent(Y,carl),parent(X,Y).
Explanation: it will look for Y which is parents of carl
it will then check for values of X which are parents of Y

Example: find alberts grandchildren
Query: parent(albert,X),parent(X,Y).
Explanation: asks is albert parent, then asks are children parents
*/

/* Format function format().
Can put in a list of stuff
~w for variable
~s for string
~n for newline
~regular strings for strings
EXAMPLE:
*/

get_grandparent:-
    parent(X,carl),
    parent(X,charlie),
    format('~w ~s grandparent ~n',[X, "is the"]).

grand_parent(X,Y):-parent(Z,X),parent(Y,Z).

/*
Example: romeo hates x if x stabs mercucio with sword
*/
hates(romeo,X):-stabs(X,mercutio,sword).

/*
Anonymous variables:checks for existance of predicate.
Use _ instead of variable
Eg. male(_).
*/
