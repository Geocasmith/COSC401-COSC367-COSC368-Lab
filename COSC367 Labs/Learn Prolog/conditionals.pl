/*
If statements dont exist but can use case statements to replicate
Use same predicate w/ different input and bodies
Example of if:
*/
what_grade(5):-write('Go to kindergarten').
what_grade(6):-write('Go to 1st grade').

/*
Use arithmetic:
Equals(=): is
Use regular + and -

Type in what_grade(8).
*/
what_grade(Other):-
    Grade is Other - 5,
    format('Go to grade ~w',[Grade]).