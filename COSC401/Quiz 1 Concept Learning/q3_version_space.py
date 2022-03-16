import itertools

def version_space(H,D):

    VS = set()
    for h in H:
        if(all(h(tup[0]) == tup[1] for tup in D)):#the function must be true for all of the values in the data, not just for one but not the other
            VS.add(h)#then the hypotheesis is in the version space

    return VS



#Gets the power set of the input space (all possible combinations)
def get_power_set(input_space):
   powerset = set()
   input_length= len(input_space)+1
   for i in range(0,input_length):
       for subset in itertools.combinations(input_space, i):
           powerset.add(subset)
   return powerset

#Goes through all of the input space and generates all possible functions (given that input set, what are the functions that can return any combination of true and false
def all_possible_functions(input_space):
   powerset = get_power_set(input_space) # get the power set of the input space
   functions = [] # list of all possible functions

   for subset in powerset:
       def function(input, s=subset):
           return input in s

       functions.append(function)
   functions=list(dict.fromkeys(functions))
   return functions


#Test cases

X = {"green", "purple"} # an input space with two elements
D = {("green", True)} # the training data is a subset of X * {True, False}
F = all_possible_functions(X)
H = F # H must be a subset of (or equal to) F

VS = version_space(H, D)

print(len(VS))

for h in VS:
    for x, y in D:
        if h(x) != y:
            print("You have a hypothesis in VS that does not agree with the D!")
            break
    else:
        continue
    break
else:
    print("OK")

D = {
    ((False, True), False),
    ((True, True), True),
}


def h1(x): return True


def h2(x): return False


def h3(x): return x[0] and x[1]


def h4(x): return x[0] or x[1]


def h5(x): return x[0]


def h6(x): return x[1]


H = {h1, h2, h3, h4, h5, h6}

VS = version_space(H, D)
print(sorted(h.__name__ for h in VS))