def is_valid_expression(expression, function_symbols, leaf_symbols):

    if(isinstance(expression),int): #1 int
        return True
    elif(isinstance(expression),str): #1 str
        return expression in leaf_symbols
    elif (isinstance(expression,list) and len(expression)==3):
        for i in range(1, 3):
            arguement = expression[i]
            return is_valid_expression(arguement, function_symbols, leaf_symbols)
    #check valid function symbol
    function_symbol = expression[0]  # 1st element in list
    if(function_symbol not in function_symbols):
        return False

    #checks if first and seccond args are correct
    for i in range(1, 3):
        arguement = expression[i]
        #checks first arguement is a list and runs fn recursively on any inner lists
        if isinstance(arguement,list):
            if not (is_valid_expression(arguement,function_symbols, leaf_symbols)):
                return False #inner list has invalid format
        elif isinstance(arguement,str): #arg is a variable
            if arguement not in leaf_symbols:
                return False#arg not in leaf symbols
        elif isinstance(arguement,int): #arg is an int constant
            pass #do nothing
        else:
            return False #arg is wrong type

    return True #all valid
