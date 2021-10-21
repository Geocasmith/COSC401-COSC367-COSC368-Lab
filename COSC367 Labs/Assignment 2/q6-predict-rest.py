import operator
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



def evaluate(expression, bindings):
    # if string (variable)return number assigned to string
    if isinstance(expression, str):
        if (expression in bindings):
            return bindings[expression]

    # if just an int then return the int
    elif isinstance(expression, int):
        return expression

    # if a list, run recursively on the two args in the list
    elif isinstance(expression, list) and len(expression) == 3:
        function_key = expression[0]  # checks if function symbol correct
        if (function_key in bindings):
            # creates the function to be calculated
            function = bindings[function_key]

            arg_one = evaluate(expression[1], bindings)  # gets the value of the first arguement recursively
            arg_two = evaluate(expression[2], bindings)
            return (function)(arg_one, arg_two)

    return None  # if incorrect format return nothing


def generate_rest(initial_sequence, expression, length):
    rest = initial_sequence.copy()  # gets from initial_sequence to get x and y
    init_length = len(initial_sequence)

    # increment until length of generated sequence
    for leng in range(length):
        # initialise i as length of seq + increment i, get values of y and x
        i = leng + init_length
        y = rest[-1]
        x = rest[-2]

        # bind the values of x and y and operators
        bindings = {'y': y, 'x': x, 'i': i, '+': operator.add, '-': operator.sub, "*": operator.mul}
        next = evaluate(expression, bindings)
        rest.append(next)
    return rest[init_length:]  # return whole sequence starting from end of init sequence

def predict_rest(sequence):
    #generates random Expressions from the given parameters in question
    function_symbols = ['*', '+', '-']
    leaves = [-2, -1, 0, 1, 2, 'x', 'y', 'i']
    max_depth = 3
    random_expressions = [random_expression(function_symbols, leaves, max_depth)
                   for _ in range(20000)]

    #splits the sequence into learn and test sets
    sequence_length = len(sequence)
    learn = sequence[:sequence_length-3]
    test = sequence[sequence_length - 3:]

    #tries from the random expressions until it finds one that fits and generates the rest of the sequence
    for expression in random_expressions:
        guess = generate_rest(learn, expression, 3)

        #if outputs from the rand expression fit the test outputs, return expression
        if(guess == test):
            return generate_rest(sequence, expression, 5)
    return None
# no particular pattern, just an example expression


sequence = [3, 2, 3, 6, 11, 18, 27, 38]
print(predict_rest(sequence))