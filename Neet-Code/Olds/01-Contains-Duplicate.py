# Contains Duplicate Hash Set Method

from os import dup2

class solution:
    def containsDuplicate(self,nums:list[int]):
        hashSet = set()
        for i in nums:
            if i in hashSet:
                return True                
            hashSet.add(i)
        return hashSet

obj1 = solution()
arrs = [1,2,3,2,1,3,6,9,7,6,9,5]
numsd = obj1.containsDuplicate(arrs)
n = len(arrs)
print(numsd)



def containsduplicate(numbers):
    return numbers != set(numbers)

if containsduplicate(arrs):
    print(True)
else:
    print(False)


nums = [1,2,3,4,1,4]
if nums != set(nums):
    print(True)
else:
    print(False)


print("................")

class duplicates:
    def duplicateArr(self,nums):
        seen = set()
        for i in nums:
            if i in seen:
                print(True)
            seen.add(i)
        print(False)

obj1 = duplicates()
obj1.duplicateArr(arrs)

print("....................")
n = len(nums)
for i in range(n):
    for j in range(i+1,n):
        if nums[i] == nums[j]:
            print(f"{nums[i]}",True)
        else:
            print(False)


## This Will not work like that

def containsDuplicate(nums):
    left = 0
    right = len(nums)-1
    while left < right:
        if nums[left] == nums[right]:
            print(True)
        left = left + 1
        right = right - 1
        print(False)

containsDuplicate(nums)



print("Adidng Hash Set Method")
def DuplicateContains(nums):
    n = len(nums)
    hashSet = set()
    for i in range(n):
        if nums[i] in hashSet:
            print(True)
        hashSet.add(nums[i])
    print(False)

DuplicateContains(nums)



