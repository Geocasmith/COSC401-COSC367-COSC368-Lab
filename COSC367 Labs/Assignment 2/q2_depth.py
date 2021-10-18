def depth(expression):
    depth_number = 0
    #expression is a leaf (base case)
    if isinstance(expression, (str,int)):
        return depth_number

    elif isinstance(expression,list) and len(expression)==3:

            depth_number = 1#if its not a leaf then add 1 to the depth
            for i in range(1, 3): #checks if arguements valid
                arguement = expression[i]
                if(depth_number<depth_number+depth(arguement)):
                    depth_number=depth_number+depth(arguement)
    return depth_number

expression = ['+',
               ['*', 2, 'i'],
               ['*',
                 ['*', -3, ['*', -3, 'x']],
                 'x']]

print(depth(expression))