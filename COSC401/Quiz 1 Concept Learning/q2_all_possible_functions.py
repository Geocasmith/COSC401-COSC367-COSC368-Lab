import itertools

def all_possible_functions(input_space):
   powerset = set()
   for i in range(0, len(input_space)+1):
       for subset in itertools.combinations(input_space, i):
           powerset.add(subset)
   return powerset


X = {"green", "purple"} # an input space with two elements
F = all_possible_functions(X)
print(F)
# Let's store the image of each function in F as a tuple
images = set()
for h in F:
   images.add(tuple(h(x) for x in X))

for image in sorted(images):
   print(image)

