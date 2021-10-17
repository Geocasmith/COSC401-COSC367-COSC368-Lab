eats(bob,Thing):-hungry(bob),edible(Thing).
eats(alice,Thing):-hungry(alice),edible(Thing), \+ fast_food(Thing).