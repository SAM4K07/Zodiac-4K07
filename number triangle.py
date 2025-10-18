T = int(input("enter the side or ur triangle"))
D1 = 1
D2 = 2 
D3 = 1
for i in range(T):
    row = []
    for j in range(D1,D2+D3-1):
        row.append(j)
    sak = "".join(str(x) for x in row)
    print(sak)
    D1= D1+1+i 
    D2=D2+1
    D3=D3+1+i
print(" ")