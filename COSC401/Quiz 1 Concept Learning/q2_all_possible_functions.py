import itertools

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


X = {"green", "purple"}
F = get_power_set(X)
print(F)
F = all_possible_functions(X)
print(len(F))
# Let's store the image of each function in F as a tuple
images = set()
for h in F:
   images.add(tuple(h(x) for x in X))#go through each x and get the result from each function and make a tuple

for image in sorted(images):
   print(image)

