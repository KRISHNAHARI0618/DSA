nums = [2,3,-1,4,-3,5,-5,7,2,-1]

globalSum = nums[0]
currentSum = 0
for i in nums:
    currentSum = currentSum + i
    if currentSum < 0:
        currentSum = 0
    else:
        globalSum = max(globalSum,currentSum)
print(globalSum)

def preFixSum(nums):
    n = len(nums)
    prefix= [0]*(n+1)
    print(prefix)
    for i in range(n):
        prefix[i+1] = prefix[i] + nums[i]
    return prefix


print(preFixSum(nums))

def prefixFetch(prefixArray):
    left = 0
    right = len(prefixArray)-1
    while left < right:
        if prefixArray[left] < prefixArray[right]:
            left = left+1
            return prefixArray[right]
        else:
            right = right - 1
            return prefixArray[right]

p= preFixSum(nums)
print(prefixFetch(p))


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        