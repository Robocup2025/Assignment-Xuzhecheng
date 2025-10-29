count=0
results=[]
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i!=j and j!=k and i!=k:
                num=i*100+j*10+k
                results.append(num)
                count+=1

print(count)
print(results)