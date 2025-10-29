def calculate(*args):
    if not args:
        return (0, [])
    avg=sum(args)/len(args)
    indices = [i for i, val in enumerate(args) if val > avg]
    return (avg, indices)

s=list(map(int,input().split()))
average, indices = calculate(*s)
print(f"Average: {average}")   
print(indices)
