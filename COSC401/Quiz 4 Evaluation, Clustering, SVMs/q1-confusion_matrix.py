from collections import namedtuple

class ConfusionMatrix(namedtuple("ConfusionMatrix",
                                 "true_positive false_negative "
                                 "false_positive true_negative")):

    def __str__(self):
        elements = [self.true_positive, self.false_negative,
                   self.false_positive, self.true_negative]
        return ("{:>{width}} " * 2 + "\n" + "{:>{width}} " * 2).format(
                    *elements, width=max(len(str(e)) for e in elements))

def confusion_matrix(classifier, dataset):
    true_positive, false_negative, false_positive, true_negative = 0, 0, 0, 0

    for i in range(len(dataset)):
        # if classifier positive
        if dataset[i][1]>0 and classifier(dataset[i][0]) >0:
            true_positive += 1
        elif dataset[i][1]<=0 and classifier(dataset[i][0]) <=0:
            true_negative += 1
        elif dataset[i][1]>0 and classifier(dataset[i][0]) <=0:
            false_negative += 1
        elif dataset[i][1]<=0 and classifier(dataset[i][0]) >0:
            false_positive += 1
    return ConfusionMatrix(true_positive, false_negative, false_positive, true_negative)

dataset = [
    ((0.8, 0.2), 1),
    ((0.4, 0.3), 1),
    ((0.1, 0.35), 0),
]
print(confusion_matrix(lambda x: 1, dataset))
print()
print(confusion_matrix(lambda x: 1 if x[0] + x[1] > 0.5 else 0, dataset))