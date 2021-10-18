def is_valid_expression(expression, function_symbols, leaf_symbols):
    function_symbol = expression[0]
    first_arguement = expression[1]
    second_arguement = expression[2]

    #check valid function symbol
    if(function_symbol not in function_symbols):
        return False



function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = ['g', 123, 'x']

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))