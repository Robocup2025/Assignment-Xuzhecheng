def ifleap(year):
    if (year%4==0 and year%100!=0)or(year%400==0):
        return True
    else:
        return False

year=int(input("年: "))
month=int(input("月: "))
day=int(input("日: "))

days_in_month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ans=sum(days_in_month[:month-1])+day

if ifleap(year) and month>2:
    ans+=1
print(ans)


