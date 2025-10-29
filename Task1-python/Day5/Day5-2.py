def getodd(lst):
    return lst[1::2]

s=list(map(int,input().split()))
odd_indices_values = getodd(s)
print(odd_indices_values)