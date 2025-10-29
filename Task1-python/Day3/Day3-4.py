t=input().strip()
s=int(t)
ans=""
while(s>0):
    r=s%10
    ans=ans+str(r)
    s=s//10

if t==ans:
    print("Yes")
else:
    print("No")