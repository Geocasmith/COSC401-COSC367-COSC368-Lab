import csv
import pandas as pd

dict = {}
with open('lab_3_log.csv', mode='r') as infile:
    for line in csv.reader(infile):
        keyList = line[0].split(' ')
        value = keyList.pop()
        keyList.pop(0)

        keyTuple=tuple(keyList)
        dict[keyTuple]=value
print(dict)