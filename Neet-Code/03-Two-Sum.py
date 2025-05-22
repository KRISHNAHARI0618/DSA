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


def twosum(nums,target):
    hashMap = {}
    for i,n in enumerate(nums):
        diff = target - n # 9-2 9-3 9-4 9-5 9-6 9-7 
        if diff in hashMap:
            return [hashMap[diff],i]
        hashMap[n] = i
    return

arrs = [2,3,4,5,6,7]
print(twosum(arrs,9))


def sumTwo(nums,target):
    n = len(nums)
    left = 0
    right = n - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left,right]
        elif sum < target:
            left = left + 1
        else:
            right = right - 1
    return 

numbers = [2,3,4,5,7]
print(sumTwo(numbers,8))


        
