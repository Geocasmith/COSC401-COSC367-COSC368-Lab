input = ([1, -1],  0)
weights = [0.5, 0.5]
bias = 0.0
learning_rate = 0.5

#gets values
w1=weights[0]
w2=weights[1]
x1=input[0][0]
x2=input[0][1]
target = input[1]

#calculate perceptron
a=bias+w1*x1+w2*x2
if a>=0:
    a=1
else:
    a=0
print("a= "+str(a))

#calculate bias and weight change
w1=w1+learning_rate*x1*(target-a)
w2=w2+learning_rate*x2*(target-a)
bias = bias + learning_rate*(target-a)
print("w1="+str(w1))
print("w2="+str(w2))
print("bias="+str(bias))