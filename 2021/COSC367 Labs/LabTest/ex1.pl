mirror(leaf(X),leaf(X)).
mirror(tree(L1,R1),tree(L2,R2)):-mirror(L1,R2),mirror(L2,R1)