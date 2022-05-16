from collections import namedtuple

class ConfusionMatrix(namedtuple("ConfusionMatrix",
                                 "true_positive false_negative "
                                 "false_positive true_negative")):
    pass

def true_positive_rate(confusion_matrix):
    """
    Returns the true positive rate
    """
    return confusion_matrix.true_positive / (confusion_matrix.true_positive + confusion_matrix.false_negative)
def false_positive_rate(confusion_matrix):
    """
    Returns the false positive rate
    """
    return confusion_matrix.false_positive / (confusion_matrix.false_positive + confusion_matrix.true_negative)

def roc_non_dominated(classifiers):
    """
    Returns the classifiers that are non-dominated by the other classifiers.
    """
    # initialise non dominated list
    non_dominated = []

    # iterate through classifiers for classifier compare to other classifiers and not itself
    for classifier in classifiers:
        # for each classifier compare to other classifiers and not itself
        dominated = False
        for other_classifier in classifiers:
            # if the classifier is not itself
            if classifier != other_classifier:
                # if the classifier is dominated by the other classifier
                        if true_positive_rate(other_classifier[1]) > true_positive_rate(classifier[1]) and false_positive_rate(other_classifier[1]) < false_positive_rate(classifier[1]):
                            # add the classifier to the non dominated list
                                        dominated = True
                                        break;
        if not dominated:
            # add the classifier to the non dominated list
            non_dominated.append(classifier)
    return non_dominated


# Example similar to the lecture notes

classifiers = [
    ("Red", ConfusionMatrix(60, 40,
                            20, 80)),
    ("Green", ConfusionMatrix(40, 60,
                              30, 70)),
    ("Blue", ConfusionMatrix(80, 20,
                             50, 50)),
]
print(sorted(label for (label, _) in roc_non_dominated(classifiers)))