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

def generate_rest(initial_sequence, expression, length):
    rest = initial_sequence.copy() #gets from initial_sequence to get x and y
    init_length = len(initial_sequence)

    #increment until length of generated sequence
    for leng in range(length):

        #initialise i as length of seq + increment i, get values of y and x
        i = leng+init_length
        y=rest[-1]
        x = rest[-2]

        #bind the values of x and y and operators
        bindings = {'y':y,'x':x,'i':i,'+':operator.add,'-':operator.sub,"*":operator.mul}
        next = evaluate(expression,bindings)
        rest.append(next)
    return rest[init_length:] #return whole sequence starting from end of init sequence


# no particular pattern, just an example expression
initial_sequence = [31, 29, 27, 25, 23, 21]
expression = ['-', 'y', 2]
length_to_generate = 5
print(generate_rest(initial_sequence,
                    expression,
                    length_to_generate))