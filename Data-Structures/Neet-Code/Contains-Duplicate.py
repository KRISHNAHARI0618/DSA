# Contains Duplicate

class solution:
    def containsDuplicate(self,nums:list[int]):
        hashSet = set()
        for i in nums:
            hashSet.add(i)
            if i in hashSet:
                return True                
        return hashSet

obj1 = solution()
arrs = [1,2,3,2,1,3,6,9,7,6,9,5]
numsd = obj1.containsDuplicate(arrs)

print(numsd)


