#由于列表具有可变性，故在弹出元素的过程中列表本身发生变化，下一个访问的就是被弹出元素后面第二位的元素，导致无法筛掉所有的奇数。
if __name__ == "__main__":
    nums = list(range(1000))
    nums = [x for x in nums if x % 2 == 0]
    print(nums)