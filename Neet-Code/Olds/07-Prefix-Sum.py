def prefixSum(nums):
    n = len(nums)
    prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + nums[i]
    return prefix

numbers = [2,3,4,5,6,7,8]
print(prefixSum(numbers))

# get the sum or 2,5

def prefix_sum(prefix,left,right):
    return prefix[right+1]-prefix[left]

p= prefixSum(numbers)
print(prefix_sum(p,2,5))


def preFixSum(nums):
    n = len(nums)
    prefix = [1] * (n+1)
    print(prefix)
    for i in range(n):
        prefix[i+1] = prefix[i] * nums[i]
    return prefix
numbers = [1,2,3,4,5,6]
print(preFixSum(numbers))


def relativPrefix(prefix,left,right):
    return prefix[right+1] - prefix[left]

p = preFixSum(numbers)
print(relativPrefix(p,2,3))