% ---------- LISTS ----------

% You can store atoms, complex terms, variables, numbers and other

% lists in a list

% They are used to store data that has an unknown number of elements

write([albert|[alice, bob]]), nl. %add items to list with | constructor
[X1, X2, X3, X4|T] = [a,b,c,d]. %adding more variables to the left

length([1,2,3], X).% Get the length of a list using length

[H|T] = [a,b,c]. % We can divide a list into its head and tail with |

/*
We can use the anonymous variable _ when we need to reference a
variable, but we don't want its value Let's get the second value in the list
-Will return T =[] and X2=b
*/
[_, X2, _, _|T] = [a,b,c,d].

% We could also get all members of a list with a variable

% member(X, [a, b, c, d]).


% Reverse a list, assigns output to X

% reverse([1,2,3,4,5], X).


% Concatenate 2 lists

% append([1,2,3], [4,5,6], X).