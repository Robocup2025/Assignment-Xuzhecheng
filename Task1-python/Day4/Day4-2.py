arr=list(map(int, input().split()))
num=int(input())

i=0
while i<len(arr) and arr[i]<=num:
    i+=1
arr.insert(i, num)
print(arr)