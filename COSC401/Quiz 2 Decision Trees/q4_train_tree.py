def train_tree(dataset, criterion):
    """
    Trains a decision tree using the given dataset and criterion.
    """
    features = list(range(0, len(dataset[0][0])))
    return DTree(dataset, features, criterion)

def DTree(examples,features,criterion):
    """
    COnstructs the decision tree
    """
    # base case all examples in one class. dataset[i][-1] is the class label
    if all(examples[i][-1] == examples[0][-1] for i in range(len(examples))):
        #return DTNode where decision is that class
        return DTNode(examples[0][-1])

    # base case set of features is empty
    elif len(features) == 0:
        return DTNode(most_common_class(examples))
    else:


        lowest_impurity = 9999
        best_feature = features[0]# initialise lowest impurity to a high number
        # find the best feature to split on
        for f in features:
            # for each feature partition the data
            separator_func, partitions = partition_by_feature_value(examples, f)

            #init impurity
            impurity= 0
            #for each partition calculate the impurity
            for i in range(len(partitions)):
                impurity += len(partitions[i])/len(examples) * criterion(partitions[i])
            #if the impurity is less than the lowest impurity adjust the feature to be split on and the lowest impurity
            if impurity < lowest_impurity:
                lowest_impurity = impurity
                best_feature = f
                best_node = DTNode(separator_func)


        #Splits the data into partitions based on the best feature
        separator_func, partitions = partition_by_feature_value(examples, best_feature)
        best_node = DTNode(separator_func)
        #Creating the tree from best decision
        for v_i in range(len(partitions)):

            #sets partitions to example
            example_i = partitions[v_i]
            #if example_i empty print the most common class in examples
            if len(example_i) == 0:
                best_node.children.append(DTNode(most_common_class))
                print("empty")
            else:
                    #recursively call the decision tree on the partitions
                updated_features=list(features)
                updated_features.remove(best_feature)

                best_node.children.append(DTree(example_i,updated_features,criterion))
    return best_node


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
    def __init__(self, decision):
        self.decision = decision
        self.children = []


    def predict(self, input_data):
        if len(self.children) == 0:#leaf node
            return self.decision
        else:
            childNum = self.decision(input_data)
            return self.children[childNum].predict(input_data)

    def leaves(self):
        if len(self.children) == 0: #leaf node
            return 1
        else: #recursively call on children
            return sum([child.leaves() for child in self.children])

def most_common_class(examples):
    """
    Returns most common class (if tie is one that came first)
    """
    classification = [x[1] for x in examples]
    return max(classification, key=classification.count)






t = DTNode(True)
f = DTNode(False)
n = DTNode(lambda v: 0 if not v else 1)
n.children = [t, f]
print(n.leaves())