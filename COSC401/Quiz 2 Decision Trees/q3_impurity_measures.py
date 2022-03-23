#Goes through all the features and gets all classificatoins
# def get_classifications(data):
#     classifications = []
#     for d in data:
#         input_vector=d[0]
#
#         for value in input_vector:
#             if value not in classifications:
#                 classifications.append(value)
#     return classifications
import math


def get_classifications(data):
    """
    Returns a list of all the classifications in the data set.
    """
    classifications = []
    for example in data:
        classification = example[1]
        if classification not in classifications:
            classifications.append(classification)

    return classifications

def get_proportion(data, classification):
    """
    Returns the ratio of the data that is in the classification in the parameter.
    """
    count = 0

    for example in data:
        if example[1] == classification:
            count += 1

    return count / len(data)

def entropy(data):
    """
    Retuns the entropy.Cycles through each clasification and uses the entropy equation to calculate the entropy.
    """
    entropy= 0

    for k in get_classifications(data):
        pmk = get_proportion(data, k)
        entropy += -1 * pmk * math.log(pmk, 2)
    return entropy
def misclassification(data):
    """
    Returns the misclassification error.
    """
    error = 0
    for k in get_classifications(data):
        pmk = get_proportion(data, k)
        if(error < pmk):
            error = pmk
    return 1 - error

def gini(data):
    """
    Returns the gini index. Cycles through each classification and uses the gini equation to calculate the gini index.
    """
    gini = 0
    for k in get_classifications(data):
        pmk = get_proportion(data, k)
        gini += pmk * (1- pmk)
    return gini

data = [
    ((False, False), False),
    ((False, True), True),
    ((True, False), True),
    ((True, True), False)
]
print("{:.4f}".format(misclassification(data)))
print("{:.4f}".format(gini(data)))
print("{:.4f}".format(entropy(data)))