length=int(input())
arr=list(map(int, input().split()))
pos=int(input())

pos=pos%length
for _ in range(pos):
    last=arr.pop()
    arr.insert(0, last)

print(arr)