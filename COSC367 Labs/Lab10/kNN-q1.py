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
print(euclidean_distance([0, 3, 1, -3, 4.5],[-2.1, 1, 8, 1, 1]))
print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]))
print(majority_element("ababc") in "ab")
