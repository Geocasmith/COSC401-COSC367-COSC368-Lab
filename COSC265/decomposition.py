#Set variable_sized
R="ABCD"
p="AD,BCD,AC"
F="A-B,B-C,CD-A"

#splits to list
R = R.split()
p = p.split(",")
F = F.split(",")
print()
#Generate tables
Matrix = [[0 for x in range(len(R))] for y in range(len(p))]

#create empty table
for row, P_val in enumerate(p):#for each row
    for col, R_val in enumerate(R):#for each column
        if(row==0 and col>0):#set row headers
            Matrix[row][col]=R_val
        if (row > 0 and col == 0):
            Matrix[row][col] = P_val




print(Matrix)