# def train_tree(dataset,criterion):
#     """
#     Trains a decision tree using the given dataset and criterion.
#     """
#
#     return 0

"""
Fn from prev questions
"""
def partition_by_feature_value(dataset, feature_index):

    #Create category and partitions list
    categories = []
    partitions=[]

    #Gets all categories
    for example in dataset:
        value = example[0][feature_index] #[0]= input vector
        if value not in categories:
            categories.append(value)

    #Create the partitioned data. For each category, if the value in the feature index matches, add to a list, add that list to a list of lists
    for category in categories:
        feature_partition=[]
        for example in dataset:
            value = example[0][feature_index]
            if(value==category):
                feature_partition.append(example)
        partitions.append(feature_partition)

    #Create the separator function which gets the value at the feature index and returns the values index in categories
    def separator_function(input_vector, f=feature_index, c=categories):
        value=input_vector[f]
        return c.index(value)

    return separator_function,partitions

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

def get_proportion(data, classification):
    """
    Returns the ratio of the data that is in the classification in the parameter.
    """
    count = 0

    for example in data:
        if example[1] == classification:
            count += 1

    return count / len(data)


"""
Other functions
"""

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

class DTNode:
    """
    Decision node
    """

    def __init__(self):
        """
        Initialise node.
        """
        # self.attribute = attribute
        # self.classification = classification
        self.edges = []

    def add_edge(self, edge):
        """
        Adds child
        """
        self.edges.append(edge)


def most_common_class(examples):
    """
    Returns most common class (if tie is one that came first)
    """
    classification = [x[1] for x in examples]
    return max(classification, key=classification.count)

def DTree(examples,features,criterion):
    """
    COnstructs the decision tree
    """
    # base case all examples in one class. dataset[i][-1] is the class label
    if all(dataset[i][-1] == dataset[0][-1] for i in range(len(dataset))):
        return dataset[0][-1]
    # base case set of features is empty
    elif len(features) == 0:
        return most_common_class(examples)
    else:
        #create a new decision node R
        R = DTNode()
        #find the best attribute to split on




dataset = [
  ((True, True), False),
  ((True, False), True),
  ((False, True), True),
  ((False, False), False)
]
print(most_common_class(dataset))
t = train_tree(dataset, misclassification)
print(t.predict((True, False)))
print(t.predict((False, False)))