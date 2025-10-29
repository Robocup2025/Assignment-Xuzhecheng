import math
for i in range(101,200):
    flag=True
    for j in range(2,math.isqrt(i)+1):
        if i%j==0:
            flag=False
            break
    if flag:
        print(i)  

