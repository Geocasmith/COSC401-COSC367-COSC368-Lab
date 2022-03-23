from pprint import pprint

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
    


# dataset = [
#   ((True, True), False),
#   ((True, False), True),
#   ((False, True), True),
#   ((False, False), False),
# ]
# f, p = partition_by_feature_value(dataset,  0)
# pprint(sorted(sorted(partition) for partition in p))
#
# partition_index = f((True, True))
# # Everything in the "True" partition for feature 0 is true
# print(all(x[0]==True for x,c in p[partition_index]))
# partition_index = f((False, True))
# # Everything in the "False" partition for feature 0 is false
# print(all(x[0]==False for x,c in p[partition_index]))
#

dataset = [
  (("a", "x", 2), False),
  (("b", "x", 2), False),
  (("a", "y", 5), True),
]
f, p = partition_by_feature_value(dataset, 1)
pprint(sorted(sorted(partition) for partition in p))
partition_index = f(("a", "y", 5))
# everything in the "y" partition for feature 1 has a y
print(all(x[1]=="y" for x, c in p[partition_index]))