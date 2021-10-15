def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""

    def perceptron(input):

        #w0(bias)
        value = bias
        #sum of wi*xi
        for i in range(len(input)):
            value = value+(input[i]*weights[i])

        return 1 if value>=0 else 0 # what the perceptron should return

    return perceptron  # this line is fine

def accuracy(perceptron, inputs, targets):
    correct_guesses = 0
    number_of_inputs = len(inputs)

    #cycles through inputs
    for i in range(number_of_inputs):

        #gets a prediction from the perceptron
        prediction = perceptron(inputs[i])
        target = targets[i]

        #compares prediction with target value at same index
        if(prediction==target):
            correct_guesses=correct_guesses+1

    #calculates accuracy
    accuracy = correct_guesses/number_of_inputs
    return accuracy

perceptron = construct_perceptron([-1, 3], 2)
inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
targets = [0, 1, 1, 0]

print(accuracy(perceptron, inputs, targets))