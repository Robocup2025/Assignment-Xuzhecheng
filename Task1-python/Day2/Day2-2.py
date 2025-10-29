a=int(input())
n=int(input())

ans=0
term=0     
for i in range(n):
    term=term*10+a
    ans+=term

print(ans)