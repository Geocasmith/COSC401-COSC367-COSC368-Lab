import random

def random_expression(function_symbols, leaves, max_depth):

    if random.choice(["head", "tail"]) == "head" or max_depth == 0: #50% chance or if at max depth then cant go deeper

        #generate leaf node
        return random.choice(leaves)

    else:

            #generate expression tree
            function = random.choice(function_symbols)
            arg_one = random_expression(function_symbols, leaves, max_depth-1)
            arg_two = random_expression(function_symbols, leaves, max_depth-1)
            return [function,arg_one,arg_two]

function_symbols = ['f', 'g', 'h']
leaves = ['x', 'y', 'i'] + list(range(-2, 3))
max_depth = 4

expressions = [random_expression(function_symbols, leaves, max_depth)
               for _ in range(10000)]
for i in range(100):
    print(expressions[i])