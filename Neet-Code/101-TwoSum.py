# Two pointer approach --> O(n*log n)
def twosum(nums,target):
    left = 0
    right = len(nums)-1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return left,right,target
        elif sum < target:
            left = left + 1
        else:
            right = right -1
nums = [2,3,4,5]
output = twosum(nums,9)
print(output)


## Using Hash Set method 

def hashSum(nums,target):
    hashSet = set()
    for i in nums:
        sum = target - i
        if sum in hashSet:
            return sum,i,target
        hashSet.add(sum)
    return sum,i,target

print(hashSum(nums,9))

## Using Brute Force Method
target = 9
for i in range(len(nums)):
    for j in range(1,len(nums)):
        sum = nums[i] + nums[j]
        if sum == target:
            print(i,j,sum,target)
    else:
        print(False)

