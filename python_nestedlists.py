matrix1=[]
matrix2=[]
matrixt=[]
for i in range(2):
    row =[]
    for j in range(2):
        a = int(input("enter ur "+str(i)+" row "+str(j)+" element"))
        row.append(a)
    matrix1.append(row)
for i in range(2):
    row =[]
    for j in range(2):
        a = int(input("enter ur "+str(i)+" row "+str(j)+" element"))
        row.append(a)
    matrix2.append(row)
print(matrix1)
print(matrix2)

for i in range(2):          # rows of A
    row = []
    for j in range(2):   # columns of B
        sumu = 0
        for k in range(2): # shared dimension (columns in A / rows in B)
            sumu += matrix1[i][k] * matrix2[k][j]
        row.append(sumu)
    matrixt.append(row)
            
       
    


print(matrixt)

        
        