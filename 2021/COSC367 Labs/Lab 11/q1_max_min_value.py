import math

def max_value(state_tree):

    #check if terminal
    if isinstance(state_tree,int):
        return state_tree
    
    #initialise v to neg infinity
    v=-math.inf

    for a in range(len(state_tree)):
        v = max(v,min_value(state_tree[a]))

    return v

def min_value(state_tree):
    # check if terminal
    if isinstance(state_tree,int):
        return state_tree

    #initialise v to infinity
    v=math.inf

    #cycles through tree
    for a in range(len(state_tree)):
        v = min(v, max_value(state_tree[a]))
    return v


def terminal_test(state_tree):

    # checks if terminal node
    if isinstance(state_tree, int):
        return True
    return False

game_tree = [[1, 2], [3]]

print(min_value(game_tree))
print(max_value(game_tree))
