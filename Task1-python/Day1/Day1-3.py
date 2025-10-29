a=[0]*21
a[1]=0
a[2]=1
a[3]=1
for i in range(4,21):
    a[i]=a[i-1]+a[i-2]

result=[str(a[i]) for i in range(1, 21)]
print(" ".join(result))