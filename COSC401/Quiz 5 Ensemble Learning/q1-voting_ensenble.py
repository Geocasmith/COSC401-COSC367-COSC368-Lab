def voting_ensemble(classifiers):
    """Gets the output from each of the classifiers for the data point and returns the most common output"""

    def ensemble(data_point):
        votes = []
        # Each output from the classifier is a "vote" on what the output should be
        for c in classifiers:
            votes.append(c(data_point))
        #Return max value in votes In the case of a tie, return the output that sorts lowest (whether this is numeric or lexicographic)
        return max(sorted(set(votes)), key=votes.count)

    return ensemble


classifiers = [
    lambda p: 1 if 1.0 * p[0] < p[1] else 0,
    lambda p: 1 if 0.9 * p[0] < p[1] else 0,
    lambda p: 1 if 0.8 * p[0] < p[1] else 0,
    lambda p: 1 if 0.7 * p[0] < p[1] else 0,
    lambda p: 1 if 0.5 * p[0] < p[1] else 0,
]
data_points = [(0.2, 0.03), (0.1, 0.12),
               (0.8, 0.63), (0.9, 0.82)]
c = voting_ensemble(classifiers)
for v in data_points:
    print(c(v))

classifiers = [lambda x: 0, lambda x: 1]
c1 = voting_ensemble(classifiers)
c2 = voting_ensemble(classifiers[::-1])
print(c1("Hello"))
print(c2("Goodbye"))