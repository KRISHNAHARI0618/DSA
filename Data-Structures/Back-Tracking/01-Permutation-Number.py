
def permute(nums):
    n = len(nums)
    res = []
    def helper(index):
        if index == n-1:
            res.append(arr[:])
            return
        for j in range(index,n):
            nums[index],nums[j] = nums[j],nums[index]
            helper(index+1)
            nums[index],nums[j] = nums[j],nums[index]
    helper(0)
    return res

arr = [1,2,3]
permute(arr)

print(permute(arr))


def permutation(nums):
    n = len(nums)
    res = []
    def helper(index):
        if index == n -1: # Base Condition
            res.append(nums[:])
            return
        for i in range(index,n):
            nums[index],nums[i] = nums[i],nums[index]
            helper(index+1)
            nums[index],nums[i] = nums[i],nums[index]
    helper(0)
    return res

arr = [4,5,6]
print(permutation(arr))

