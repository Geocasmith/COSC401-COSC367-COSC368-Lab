def DTree(examples, features, criterion):
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

        lowest_missclassification = 9999  # initialize to a high number
        best_node = DTNode()  # initialize best node to empty node
        lowest_impurity = 9999

        # find the best feature to split on
        for f in features:
            # for each feature partition the data
            separator_func, partitions = partition_by_feature_value(examples, f)

            # take smallest g
            # use function as dtnode decision
            # calculates the maximum misclassification error for the partitions
            missclassification = max(misclassification(partitions[i]) for i in range(len(partitions)))
            # TODO REDO SO ITS NOT JUST MISSCLASSIFICATION (needs to find the lowest)
            # if the current feature has the lowest misclassification error, set the best node to the current feature
            if (missclassification < lowest_missclassification or lowest_missclassification == 0):
                lowest_missclassification = missclassification
                best_node = DTNode(separator_func)
                best_feature = f

            # finding the best decision feature
            # initialise lowest impurity to a high number

            best_feature = f

            # part#Creating the tree from best decision
            for v_i in range(len(partitions)):

                # sets partitions to example
                example_i = partitions[v_i]
                # if example_i empty print the most common class in examples
                if len(example_i) == 0:
                    best_node.children.append(DTNode(most_common_class))

                else:
                    # recursively call the decision tree on the partitions
                    best_node.children.append(DTree(partitions[v_i], features.remove(f), criterion))
        return best_node

