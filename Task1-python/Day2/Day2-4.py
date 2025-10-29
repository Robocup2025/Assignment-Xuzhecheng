for i in range(101,1000):
    bai=i//100
    shi=(i//10)%10
    ge=i%10
    if i==bai**3+shi**3+ge**3:
        print(i)