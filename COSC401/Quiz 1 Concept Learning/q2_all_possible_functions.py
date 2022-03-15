from itertools import chain, combinations

def powerset(input_space):
    s = list(input_space)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

print(list({"green", "purple"}))