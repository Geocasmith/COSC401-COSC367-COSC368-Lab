def is_valid_expression(expression, function_symbols, leaf_symbols):
    if isinstance(expression, str):  # one str
        if(expression in leaf_symbols):
            return True
        else:
            return False
    elif isinstance(expression,int): #one int
        return True
    elif isinstance(expression,list) and len(expression)==3:
        function_symbol = expression[0]  #checks if function symbol correct
        if (function_symbol in function_symbols):
            for i in range(1, 3): #checks if arguements valid
                arguement = expression[i]
                return is_valid_expression(arguement, function_symbols, leaf_symbols)

    return False #doesnt pass valid checks

function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = ['x', 0, 1]

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))