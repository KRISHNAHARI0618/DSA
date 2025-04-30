def twoSum(arr:any,target:any)->any:
    prevMap = {}
    for i,n in enumerate(arr):
        # print(i,n)
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff],i]
        prevMap[n] = i
    return

lists = [2,3,5,7]
print(twoSum(lists,9))
