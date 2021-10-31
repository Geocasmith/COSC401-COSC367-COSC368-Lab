import math
#Fitts Law

#**************Set variables
a = 100
b = 100
n = 8

#calculate ID
T = a + b * math.log2(n)

print(" HYMAN EQUALLY PROBABLE N ITEMS \n a: "+str(a)+" ms "+"\n b: "+str(b)+" ms/bit"+"\n N items: "+str(n)+"\n Decision Time: "+str(T)+" ms")