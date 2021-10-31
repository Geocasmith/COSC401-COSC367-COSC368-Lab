import math
#Fitts Law

#**************Set variables
rank_n = 4
occurances_of_most_frequent = 1000

#calculater freq
alpha = 1
Pn = rank_n ** (-1*alpha)
occurances_of_n = occurances_of_most_frequent * Pn


print("ZIPFS LAW ")
print("N Rank: " + str(rank_n))
print("Frequency of most common: " + str(occurances_of_most_frequent)+"\n")
print("Pn scaling factor for nth ranked: "+str(Pn))
print("Occurances of n: "+str(occurances_of_n))
print("Pn = "+str(rank_n)+"^-"+str(alpha))