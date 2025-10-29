x, y, z=map(int,input().split())
nums = [x,y,z]
nums.sort()
print(nums[0],nums[1],nums[2])

#if x > y:
#    x, y = y, x
#if x > z:
#   x, z = z, x
#if y > z:
#    y, z = z, y