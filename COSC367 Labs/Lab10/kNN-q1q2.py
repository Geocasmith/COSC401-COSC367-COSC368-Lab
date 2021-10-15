import heapq

def euclidean_distance(list1,list2):
    #initialise
    length = len(list1)
    inner = 0

    #calculates difference squared and sums
    for i in range(length):
        inner=inner+(list1[i]-list2[i])**2

    #square root
    result = inner**0.5

    return result

def majority_element(list):
    # initialise
    majorityCount=0
    length = len(list)

    #gets distinct elements
    myset = set(list)

    #list of elements and counts

    counts=[]#counts
    elements=[]#elements(same indexes as counts)
    while(len(myset)>0):
        element = myset.pop()#element
        elementcount=0#counter

        #counts occurances
        for i in range(length):
            if list[i]==element:
                elementcount=elementcount+1
        #adds element& count
        elements.append(element)
        counts.append(elementcount)

    #gets max value and returns associated element
    max_index=counts.index(max(counts))
    most_common=elements[max_index]

    return most_common


def knn_predict1(input, examples, distance, combine, k):
    selected = []
    consider = examples[:]

    consider.sort(key = lambda x: distance(input,x[0]))
    print("consider:")
    print(consider)
    last_used = 0
    for i in range(k):
        t  = consider.pop(0)
        selected.append(t[1])
        last_used = t[0]
    while(consider and distance(input,last_used)== distance(input,consider[0][0])):
        t  = consider.pop(0)
        selected.append(t[1])
        last_used = t[0]
    return combine(selected)

def knn_predict(input, examples, distance, combine, k):
    distances = []

    #gets distances from dataset and unknown point
    for e in examples:
        distances.append((distance(e[0],input),e[1]))

    #sort by distances
    distances = sorted(distances)

    #get k nearnest
    selected = distances[:k]
    unselected = distances[k:]


    for i in range(0,100):
        if(len(unselected)>0):
            last_element_dist = selected[-1][0]
            unselected_element_dist = unselected[0][0]

            if(last_element_dist==unselected_element_dist):
                k=k+1
                selected = distances[:k]
                unselected = distances[k:]


    #gets prediction for nearest neighbors by splitting list of tuples
    distance, predictions = zip(*selected)

    prediction = combine(predictions)
    return prediction


# examples = [
#     ([2], '-'),
#     ([3], '-'),
#     ([5], '+'),
#     ([8], '+'),
#     ([9], '+'),
# ]
#
# distance = euclidean_distance
# combine = majority_element
#
# for k in range(1, 6, 2):
#     print("k =", k)
#     print("x", "prediction")
#     for x in range(0,10):
#         print(x, knn_predict([x], examples, distance, combine, k))
#     print()

examples = [
    ([1], 5),
    ([2], -1),
    ([5], 1),
    ([7], 4),
    ([9], 8),
]

def average(values):
    return sum(values) / len(values)

distance = euclidean_distance
combine = average

for k in range(1, 6, 2):
    print("k =", k)
    print("x", "prediction")
    for x in range(0,10):
        print("{} {:4.2f}".format(x, knn_predict([x], examples, distance, combine, k)))
    print()