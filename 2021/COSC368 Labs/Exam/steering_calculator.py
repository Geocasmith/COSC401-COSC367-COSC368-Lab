import math
#Fitts Law

#**************Set variables
A = 300
W = 10
a = 200
b = 50

#calculate ID
ID = (A/W)
MT = a + b * (A/W)

print(" STEERING LAW \n A: "+str(A)+" px"+"\n W: "+str(W)+" px"+"\n ID: "+str(ID)+" bits"+"\n a: "+str(a)+" ms "+"\n b: "+str(b)+" ms/unit"+"\n MT: "+str(MT)+" ms")
print("MT = "+str(a)+" + "+str(b)+" * ("+str(A)+"/"+str(W)+")")