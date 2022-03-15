def depth(expression):
    depth_number = 0
    #expression is a leaf (base case)
    if isinstance(expression, (str,int)):
        return depth_number

    elif isinstance(expression,list) and len(expression)==3:

            depth_number = 1#if its not a leaf then add 1 to the depth

            arg_one_depth = depth_number + depth(expression[1]) #depth of first arguement
            arg_two_depth = depth_number + depth(expression[2]) #depth of seccond arguement
            deepest_depth = max(arg_one_depth,arg_two_depth) #return the deepest tree
            return deepest_depth


    return depth_number

expression = 12
print(depth(expression))