import math
#Fitts Law

#**************Set variables
A = 800
W = 100
a = 100
b = 100

#calculate ID
ID = math.log2(A/W +1)
MT = a + b * math.log2(A/W+1)

print(" FITTS LAW \n A: "+str(A)+" px"+"\n W: "+str(W)+" px"+"\n ID: "+str(ID)+" bits"+"\n a: "+str(a)+" ms "+"\n b: "+str(b)+" ms/bit"+"\n MT: "+str(MT)+" ms")
print("MT = "+str(a)+" + "+str(b)+" * "+"log2("+str(A)+"/"+str(W)+"+1)")