matrix1=[]
for i in range(3):
    row = list(map(int, input().split()))
    matrix1.append(row)

matrix2=[]
for i in range(3):
    row = list(map(int, input().split()))
    matrix2.append(row)
sum1=[]
for i in range(3):
    sum1.append([0]*3)
for i in range(3):
    for j in range(3):
        sum1[i][j]=matrix1[i][j]+matrix2[i][j]

print(sum1)