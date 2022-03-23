import itertools

def decode(four_tuple):
#get the left x by taking the min, right x by max and same with top and bottom y. Check if it the point is inbetween those

    def h(point,tuple=four_tuple):
        #splits the points up
        x1, y1, x2, y2 = four_tuple
        x, y = point


        leftx = min(x1,x2)
        rightx = max(x1,x2)
        topy = max(y1,y2)
        bottomy = min(y1,y2)

        if leftx <= x <= rightx and bottomy <= y <= topy:
            return True
        return False

    return h





h1 = decode((1, 4, 7, 9))
h2 = decode((7, 9, 1, 4))
h3 = decode((1, 9, 7, 4))
h4 = decode((7, 4, 1, 9 ))


for x in itertools.product(range(-2, 11), repeat=2):
    print(len({h(x) for h in [h1, h2, h3, h4]}))
    if len({h(x) for h in [h1, h2, h3, h4]}) != 1:
        print("Inconsistent prediction for", x)
        break
else:
    print("OK")

