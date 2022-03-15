import math
#Fitts Law

#**************Set variables
a = 200
b = 100
pi = 0.33

#calculate ID
T = a + b * math.log2(1/pi)

print(" STEERING LAW \n a: "+str(a)+" ms "+"\n b: "+str(b)+" ms/bit"+"\n Probability of item i: "+str(pi)+"\n Decision Time: "+str(T)+" ms")
print("T = "+str(a)+" + "+str(b)+" * log2(1/"+str(pi)+")")