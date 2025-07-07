def productSum(arr):
    n = len(arr)
    productS = [1] *(n)
    for i in range(n-1,-1,-1): #[3,2,1,0]
        productS[i-1] = productS[i] * arr[i] # 

    print(productS)


nums = [1,2,3,4]

productSum(nums)


def ProductSum(arrs):
    n = len(arrs)
    print(n)
    for i in range(n):
        print(i)
    res = [1] * n
    print(res)
    prefix = 1
    for i in range(n): # [ 0, 1, 2, 3 ] 
        res[i] = prefix #a[0] = 1,a[1]=2,a[2]=3,a[3]=4 [ 1,1,2,6]
        prefix = prefix * arrs[i] # arrs[0],arrs[1],arrs[2],arr[3] 
                                      # prefix = [1,1,2,3] , arrs = [1,2,3,4]
    print(res)
    postFix = 1
    for i in range(n-1,-1,-1): # [ 3,2,1,0 ]
        res[i] = res[i] * postFix # [6,2,1,1] * [1,4,3,2] = 
        postFix = postFix * arrs[i] # [1,1,1,1] * [4,3,2,1] = 
    print(res)

nums = [1,2,3,4]
ProductSum(nums)

def sumProduct(nums):
    n = len(nums) # 4
    output = [1]*n # [1,1,1,1]
    prefix = 1
    for i in range(n): # [0,1,2,3]
        # output[0,1,2,3] = [1,1,2,6]
        output[i] = prefix
        # [1,1,2,6] = [1,1,2,]  * nums[0,1,2,3] = 1,2,3,4
        prefix = prefix * nums[i] 
    print(output)
    suffix = 1
    for i in range(n-1,-1,-1): # [3,2,1,0]
        # output[3,2,1,0] = [6,2,1,1] * [1,4,12,24]
        output[i] = output[i] * suffix # [1][4][8][16]
        # [4][8][16] = 1*4,4*3,12*2
        suffix = suffix * nums[i] #[4,3,2,1]
    print(output)


nums = [1,2,3,4]
sumProduct(nums)

# Using Brute Force Approach

nums = [1,2,3,4]
product = [1]*len(nums)
n = len(nums)
for i in range(n): #0,1,2,3
    for j in range(n): #0,1,2,3
        if i!=j:
            product[i] = product[i] * nums[j]
            
print(product) 

            
