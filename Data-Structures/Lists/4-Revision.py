def KthMinandMax(nums,k):
    nums.sort()
    print(nums)
    maxNumbers = nums[:k+2:-1]
    minNumbers = nums[:k]

    return maxNumbers,minNumbers


arr = [1,4,5,2,7,8,2,6,3]
minN,maxN = KthMinandMax(arr,3)
print(minN,maxN)

