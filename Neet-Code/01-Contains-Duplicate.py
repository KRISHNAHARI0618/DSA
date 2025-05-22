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


nums = [1,2,3,4,1]
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