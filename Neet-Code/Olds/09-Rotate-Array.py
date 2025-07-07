def rotate(nums,k):
    k = k % len(nums)
    print(len(nums)) # This will check how many times it should rotate
    # k = 4 % 5
    print(k) # K == 0 == 5 == 10 == 15 
    print(4%5)
    l,r = 0,len(nums)-1 # l , r = 0,4 
    while l < r : # 0 < 4 
        nums[l] , nums[r] = nums[r],nums[l] # nums[l] = []
        l,r = l+1,r-1
    l,r = 0,k-1
    while l <  r:
        nums[l] ,nums[r] = nums[r],nums[l]
        l,r = l+1,r-1
    l , r = k,len(nums)-1
    while l < r:
        nums[l],nums[r] = nums[r] ,nums[l]
        l,r = l+1,r-1
    print(nums)

arrs = [1,2,3,4,5]
rotate(arrs,4)


## Rotate Some elements

def arrRoate(arr):
    i = 0
    j = len(arr)-1
    while i < j:
        arr[i], arr[j] = arr[j],arr[i]
        i= i + 1
    return arr

nums= [2,3,4,5,6,7]
print(arrRoate(nums)) 


# Using K Elements Rotate 
def RotateKElement(arrs,k):
    n = len(arrs)
    k = k % n
    left = 0
    right = n -1
    while left < right :
        arrs[left],arrs[right] = arrs[right],arrs[left]
        left = left + 1
        right = right - 1
    left = 0 
    right = k - 1
    while left < right:
        arrs[left],arrs[right] = arrs[right],arrs[left]
        left = left + 1
        right = right - 1
    left = k
    right = n-1
    while left < right:
        arrs[left],arrs[right] = arrs[right],arrs[left]
        left = left + 1
        right = right - 1
    return arrs

numbers = [10,20,30,40,50,60,70]
print(RotateKElement(numbers,3))