# input = ([1, -1],  0)
# weights = [0.5, 0.5]
# bias = 0.0
# learning_rate = 0.5
#
# #gets values
# w1=weights[0]
# w2=weights[1]
# x1=input[0][0]
# x2=input[0][1]
# target = input[1]
#
# #calculate perceptron
# a=bias+w1*x1+w2*x2
# if a>=0:
#     a=1
# else:
#     a=0
# print("a= "+str(a))
#
# #calculate bias and weight change
# w1=w1+learning_rate*x1*(target-a)
# w2=w2+learning_rate*x2*(target-a)
# bias = bias + learning_rate*(target-a)


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

def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    new_weight=weights
    new_bias = bias
    training_size=len(training_examples)-1

    counter = 0#iterates through examples
    correct_counter=0
    for x in range(max_epochs):
        #gets values
        target = training_examples[counter][1]
        inputs = training_examples[counter][0]
        x1 = training_examples[counter][0][0]
        x2 = training_examples[counter][0][1]
        w1=new_weight[0]
        w2=new_weight[1]


        # construct perceptron with new weight&bias values
        perceptron = construct_perceptron(new_weight, new_bias)

        #gets perceptron guess output
        perceptron_output = perceptron(inputs)

        #calculate new weight and bias
        if(perceptron_output!=target):
            w1 = w1 + learning_rate * x1 * (target - perceptron_output)
            w2 = w2 + learning_rate * x2 * (target - perceptron_output)
            new_bias = new_bias + learning_rate * (target - perceptron_output)
            new_weight=[w1,w2]
        else:
            correct_counter = correct_counter+1
            print("correct: "+str(correct_counter))


        print(str(x)+":   " + "w1: "+str(new_weight[0])+"  w2: "+str(new_weight[1])+"  bias: "+str(new_bias))
        #updates counter and resets if at end of examples
        if(counter==training_size):
            counter=-1#not 0 because line below increments it to 0
            correct_counter=0
        counter = counter + 1

    return new_weight, new_bias


weights = [2, -4]
bias = 0
learning_rate = 0.5
examples = [
  ((0, 0), 0),
  ((0, 1), 1),
  ((1, 0), 1),
  ((1, 1), 0),
  ]
max_epochs = 50

weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
print(f"Weights: {weights}")
print(f"Bias: {bias}\n")