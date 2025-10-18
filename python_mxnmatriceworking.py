while True:
    try:
        m = int(input("enter ur m value :"))
        n = int(input("enter ur n value :"))
        break
    except:
        print("u entered a alphabet pls enter a number:")
print("enter elements for ur first matrix")
matrix1=[]
for i in range(m):
    count1=i+1
    row=[]
    for j in range(m):
        count2=j+1
        while True:
            try:
                a = int(input("enter ur "+str(count1)+" row "+str(count2)+" element"))
                break
            except:
                print("u cannot enter an alphabet ")
        row.append(a)
    matrix1.append(row)
print("enter elements for ur 2nd matrix ")
matrix2=[]
for i in range(m):
    count3=i+1
    row=[]
    for j in range(n):
        count4=j+1
        while True:
            try:
                a = int(input("enter ur "+str(count3)+" row "+str(count4)+" element"))
                break
            except:
                print("u cannot enter an alphabet")
        row.append(a)
    matrix2.append(row)
print(matrix1)
print(matrix2)
#convering 2nd matrix rows into columns for easier multiplication 
list1=[]
for i in range(m):
    rowx=[]
    for j in range(n):
       b=  matrix2[j][i]
       rowx.append(b)
    list1.append(rowx)
#multiplication
matrixm=[]
for i in range(m):
    rowm=[]
    for j in range(n):
        row1=[]
        for k in range(m):
            mul = matrix1[i][k]*matrix2[k][j]
            row1.append(mul)
        sumt=sum(row1)  
        rowm.append(sumt)  
    matrixm.append(rowm)
print(matrixm)