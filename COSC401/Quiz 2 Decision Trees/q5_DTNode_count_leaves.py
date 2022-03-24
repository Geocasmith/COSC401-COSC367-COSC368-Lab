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

n = DTNode(True)
print(n.leaves())