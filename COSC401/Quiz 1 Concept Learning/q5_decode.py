import itertools
# def decode(four_tuple):
#
#
#     def h(point,tuple=four_tuple):
#         #splits the points up
#         x1, y1, x2, y2 = four_tuple
#         x, y = point
#
#         if(x1<=x2 and y1<=y2):
#             if(x1<=x<x2 and y1<y<y2):
#                 return True
#             return False
#
#         if(x1>=x2 and y1>=y2):
#             if(x1>=x>x2 and y1>y>y2):
#                 return True
#             return False
#         return False
#
#     return h
def decode(four_tuple):


    def h(point,tuple=four_tuple):
        #splits the points up
        x1, y1, x2, y2 = four_tuple
        x, y = point

        if x >= x1 and x <= x2 and y >= y1 and y <= y2:
            return True
        elif (x >= x2 and x <= x1 and y >= y2 and y <= y1):
            return True
        if x >= x2 and x <= x1 and y >= y2 and y <= y1:
            return True
        elif (x >= x1 and x <= x2 and y >= y1 and y <= y2):
            return True
        else:
            return False
    return h

def in_rectangle(x1,y1,x2,y2,x,y):
    if x>=x1 and x<=x2 and y>=y1 and y<=y2:
        return True
    elif(x>=x2 and x<=x1 and y>=y2 and y<=y1):
        return True
    else:
        return False

# h = decode((-1, -1, 1, 1))
#
# for x in itertools.product(range(-2, 3), repeat=2):
#     print(x, h(x))

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
