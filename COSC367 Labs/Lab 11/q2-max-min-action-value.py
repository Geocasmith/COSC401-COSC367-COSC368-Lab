import math


def max_value(state_tree):
    # check if terminal
    if isinstance(state_tree, int):
        return state_tree

    # initialise v to neg infinity
    v = -math.inf

    for a in range(len(state_tree)):
        v = max(v, min_value(state_tree[a]))

    return v


def min_value(state_tree):
    # check if terminal
    if isinstance(state_tree, int):
        return state_tree

    # initialise v to infinity
    v = math.inf

    # cycles through tree
    for a in range(len(state_tree)):
        v = min(v, max_value(state_tree[a]))
    return v


def terminal_test(state_tree):
    # checks if terminal node
    if isinstance(state_tree, int):
        return True
    return False


def min_action_value(game_tree):

    # check terminal
    if isinstance(game_tree, int):
        return (None, game_tree)

    # goes through root's children
    utilities = []
    for child in range(len(game_tree)):
        # gets the minimum utility for each child
        utilities.append(max_value(game_tree[child]))

    # gets the index of best action
    min_value = min(utilities)
    best_action = utilities.index(min_value)

    return (best_action, min_value)

def max_action_value(game_tree):
    # check terminal
    if isinstance(game_tree, int):
        return (None, game_tree)

    #goes through root's children
    utilities=[]
    for child in range(len(game_tree)):
        #gets the minimum utility for each child
        utilities.append(min_value(game_tree[child]))

    #gets the index of best action
    max_value = max(utilities)
    best_action = utilities.index(max_value)

    return (best_action,max_value)

game_tree = [1, 2, [3]]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)