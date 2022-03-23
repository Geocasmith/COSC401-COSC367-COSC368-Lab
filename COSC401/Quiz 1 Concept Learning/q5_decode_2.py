import itertools
def decode(four_tuple):
    """
    Returns a function which returns true if a point is in a rectangle.
    """
    x1, y1, x2, y2 = four_tuple
    def in_rectangle(x, y):
        return x1 <= x <= x2 and y1 <= y <= y2
    return in_rectangle


h = decode((-1, -1, 1, 1))

for x in itertools.product(range(-2, 3), repeat=2):
    print(x, h(x))

h1 = decode((1, 4, 7, 9))
h2 = decode((7, 9, 1, 4))
h3 = decode((1, 9, 7, 4))
h4 = decode((7, 4, 1, 9))


for x in itertools.product(range(-2, 11), repeat=2):
    if len({h(x) for h in [h1, h2, h3, h4]}) != 1:
        print("Inconsistent prediction for", x)
        break
else:
    print("OK")

