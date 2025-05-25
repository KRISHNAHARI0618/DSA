nums = [4,200,1,3,2,201,202]

def longestSubsequnec(nums):
    numSet = set(nums)
    longest = 0
    hashSet = set()
    for n in nums:
        if (n-1) not in numSet:
            length = 0
            while (n+length) in numSet:
                length = length + 1
            longest = max(longest,length)
            hashSet.add(longest)
    return longest,hashSet,numSet

print(longestSubsequnec(nums))