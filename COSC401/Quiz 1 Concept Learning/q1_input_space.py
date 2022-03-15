domains = [
{0, 1, 2},
{True, False},
]


def input_space(domains):
   input_space = []
   if len(domains) == 1:
       for element in domains[0]:
           input_space.append(element)
   elif len(domains) == 2:
       for element in domains[0]:
           for element2 in domains[1]:
               input_space.append((element, element2))
   elif len(domains) == 3:
       for element in domains[0]:
           for element2 in domains[1]:
               for element3 in domains[2]:
                   input_space.append((element, element2, element3))

   return input_space

for element in sorted(input_space(domains)):
   print(element)
