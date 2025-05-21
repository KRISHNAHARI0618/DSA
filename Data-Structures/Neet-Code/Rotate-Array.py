def rotate(nums,k):
    k = k % len(nums) # This will check how many times it should rotate
    print(k) # K == 0 == 5 == 10 == 15 
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
rotate(arrs,10)