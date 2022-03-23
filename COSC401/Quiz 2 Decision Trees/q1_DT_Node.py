class DTNode:
    def __init__(self, decision):
        self.decision = decision
        self.children = []


    def predict(self, input_data):
        if len(self.children) == 0:#leaf node (decision is not a function so just return it)
            return self.decision #return the classifier/regression result if it is a leaf node
        else:
            childNum = self.decision(input_data) #calculates which child to go to based on decision function (is a function if its not a leaf node)
            return self.children[childNum].predict(input_data) #recursively calls predict on the child node


# The following (leaf) node will always predict True
node = DTNode(True)

# Prediction for the input (1, 2, 3):
x = (1, 2, 3)
print(node.predict(x))

# Sine it's a leaf node, the input can be anything. It's simply ignored.
print(node.predict(None))


yes_node = DTNode("Yes")
no_node = DTNode("No")
tree_root = DTNode(lambda x: 0 if x[2] < 4 else 1)
tree_root.children = [yes_node, no_node]

print(tree_root.predict((False, 'Red', 3.5)))
print(tree_root.predict((False, 'Green', 6.1)))