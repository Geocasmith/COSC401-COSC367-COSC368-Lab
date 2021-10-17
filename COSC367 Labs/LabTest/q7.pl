postorder(leaf(X), [X]).
postorder(tree(Root, Left, Right), Traversal) :-
    postorder(Left, LeftTraversal),  % Complete
    postorder(Right, RightTraversal),  % Complete
    append(RightTraversal, LeftTraversal, LeftRightTraversal),
    append(LeftRightTraversal, [Root], Traversal).  % Complete

test_answer :- inorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
               writeln(T).