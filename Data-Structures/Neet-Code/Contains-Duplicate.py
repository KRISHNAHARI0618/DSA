
from collections.abc import Set
from typing import Any

class solution:
    def containsDuplicate(self,nums: list[int]) -> Any:
        hashSet = Set()
        for i in nums:
            if i in hashSet:
                return True
            hashSet.add(i)
        return False
    
sol = solution()
arr = [2,3,9,8,6,5]
result = sol.containsDuplicate(arr)
print(result)


def containsDuplicates(name: Any)-> Any:
    hashSet = set()
    for i in range(len(name)):
        hashSet.add(name[i])
    return hashSet
        
output = containsDuplicates("peddireddy")
print(output)

def containsDup(arr: Any) -> Any:
    hashSet = set()
    dupSet = set()
    for i in arr:
        if i in hashSet:
            dupSet.add(i)
        else:
            hashSet.add(i)
    return hashSet,dupSet

list1 = [2,3,9,8,6,5,2,3]
result1,result2 = containsDup(list1)
print(result1,result2)

def DuplicateArray(arr : any)-> any:
    hashSet = set()
    for i in arr:
        if i in hashSet:
            return True
        hashSet.add(i)
    return False

list = [2,3,4,9,8,7,4,3,2]
dpar = DuplicateArray(list)
print(dpar)

