from pprint import pprint

def partition_by_feature_value(dataset, feature_index):
    partitions = []
    for data in dataset:
        feature_value=data[0][feature_index]
        
        # partitions.setdefault(data[0][feature_index], data)
    print(partitions)


dataset = [
  ((True, True), False),
  ((True, False), True),
  ((False, True), True),
  ((False, False), False),
]
f, p = partition_by_feature_value(dataset,  0)
pprint(sorted(sorted(partition) for partition in p))

partition_index = f((True, True))
# Everything in the "True" partition for feature 0 is true
print(all(x[0]==True for x,c in p[partition_index]))
partition_index = f((False, True))
# Everything in the "False" partition for feature 0 is false
print(all(x[0]==False for x,c in p[partition_index]))