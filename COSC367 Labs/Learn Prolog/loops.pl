% ---------- HOW TO LOOP ----------


% Use recursion to loop
count_to_10(10) :- write(10), nl.
%  ^if value equals 10 then write 10

count_to_10(X) :-
  write(X),nl,
  Y is X + 1,
  count_to_10(Y).
% ^ if not then keep looping with recursion

%   Example 2

guess_num :- loop(start).

% When they guess 15 they execute this message and exit

loop(15) :- write('You guessed it!').

loop(X) :-
  x \= 15,
  write('Guess Number '),
  read(Guess),
  write(Guess),
  write(' is not the number'), nl,
  loop(Guess).
