# name = "peddireddy"

# for i in range(len(name)):
#     for j in range(i,len(name)):
#         print(name[i:j])


### Sliding Window Techinique

from sys import maxsize


nums = [10,20,30,40,50,6]
n = len(nums)
k = 2
max_sum = -maxsize
sum_arr = []
for i in range(n-k+1):
    print(nums[i])
    current_sum = 0
    for j in range(k):
        current_sum = current_sum + nums[i+j]
        max_sum = max(max_sum,current_sum)
    sum_arr.append(current_sum)

print(sum_arr)
print(max_sum)


a = [2,3,7,9,5,10,6,8]
              #0,1,2,3,4,5,6,7,8  

left = 0
right = 0
sum = 0
maxValue = 0
k = 12
n = len(a)
while (right < n):
    sum = sum + a[right]
    if sum > k:
        sum = sum - a[right]
        left = left +1
    if sum <= k:
        maxValue = max(maxValue,right-left+1)
    right = right + 1
print(left,right,maxValue,sum)



