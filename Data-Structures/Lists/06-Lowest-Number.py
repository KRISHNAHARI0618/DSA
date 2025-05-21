nums = [1,4,2,3]
n = nums[0]
for i in nums:
    if n > i:
        n= i
print(n)


## bubble sort Time --> O(n2) Space --> O(1)
n = len(nums) # 11 
for i in range(0,n): 
    for j in range(n-i-1): # 11-0-1 ,11-1-1,11-2-1,[0,0] [0,1] [0,2],[0,3] ,[0,4],[0,5] 
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
print(nums)

# Bubble sort using two pointer approach
left = 0
right = len(nums)-1
while left < right:
    if nums[left] > nums[right]:
        nums[left] ,nums[right] = nums[right],nums[left]
    left = left + 1
    right = right - 1

print(nums)

# Swap First and last elements in an array
for i in range(1,len(nums)):
    if nums[i-1] > nums[i]:
        nums[i-1],nums[i] = nums[i],nums[i-1]
print(nums)

#Bubble Sort with while loop

def bubbleSort(arrs):
    n = len(arrs)
    flag = True
    while flag:
        flag= False
        for i in range(1,n):
            if arrs[i-1] > arrs[i]:
                arrs[i-1],arrs[i] = arrs[i],arrs[i-1]
                flag= True
    return arrs
print(bubbleSort(nums))
