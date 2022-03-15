/*
COMPARISON:
Use = for comparison
eg alice=alice.

use \+ for negation
eg \+ (alice=albert).

Use > or <
=< or <=
eg 3=<15.


TRACE:
use trace.
then enter your inputs.

Call: means it calls function
Exit means it exits the called function (after checking)
Fail: means it failed the call function
Example:
*/
warm_blooded(penguin).
warm_blooded(human).

produce_milk(penguin).
produce_milk(human).

have_feathers(penguin).
have_hair(human).

mammal(X) :-
  warm_blooded(X),
  produce_milk(X),
  have_hair(X).
