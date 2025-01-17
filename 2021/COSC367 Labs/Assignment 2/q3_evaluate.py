import operator

def evaluate(expression, bindings):
    # if string (variable)return number assigned to string
    if isinstance(expression, str):
        if(expression in bindings):
            return bindings[expression]

    # if just an int then return the int
    elif isinstance(expression,int):
        return expression

    # if a list, run recursively on the two args in the list
    elif isinstance(expression,list) and len(expression)==3:
        function_key = expression[0]  #checks if function symbol correct
        if (function_key in bindings):
            #creates the function to be calculated
            function = bindings[function_key]
            arg_one = evaluate(expression[1],bindings) #gets the value of the first arguement recursively
            arg_two = evaluate(expression[2],bindings)
            return (function)(arg_one,arg_two)

    return None #if incorrect format return nothing

bindings = dict(x = 5, y = 10, blah = 15, add = operator.add)
expression = ['add', ['add', 22, 'y'], 'x']
print(evaluate(expression, bindings))