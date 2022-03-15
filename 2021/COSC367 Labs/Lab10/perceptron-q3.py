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

weights = [2, -4]
bias = 0
perceptron = construct_perceptron(weights, bias)

print(perceptron([1, 1]))
print(perceptron([2, 1]))
print(perceptron([3, 1]))
print(perceptron([-1, -1]))