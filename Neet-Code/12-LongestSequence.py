nums = [4,200,1,3,2,201,202]

def longSequence(nums):
    hashSet = set(nums)
    longest = 0
    for n in nums:
        if (n-1) not in hashSet:
            length = 0
            while (n+length) in hashSet:
                length = length + 1
            longest = max(length,longest)
    return longest


print(longSequence(nums))