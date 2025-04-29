# def twosum(nums : list[int],target: int) -> list[int]:
#     dict = {}
#     n = len(nums)
#     for i in range(n-1):
#         for j in range(n-1):
#             if  i == j:
#                 continue
#             if nums[i]+nums[j] == target:
#                 print(i,j)
#                 print(nums[i],nums[j])
#         dict[i] = nums[i]
#     print(dict)
        
# list1 = [2,3,4,5,6,7]
# twosum(list1,8)


# Two Sum Problem
# Array containing Sum with two numbers

def twoSum(nums: list[int],target: int) -> list[int]:
    list = []
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] +nums[j] == target:
                return [i,j]

list1 = [2,3,4,5,6,7]
print(twoSum(list1,8))