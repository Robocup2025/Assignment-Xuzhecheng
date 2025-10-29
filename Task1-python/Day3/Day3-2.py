width=7
for i in range(1,8):
    stars=2*min(i,width-i+1)-1
    print(("*"*stars).center(width))