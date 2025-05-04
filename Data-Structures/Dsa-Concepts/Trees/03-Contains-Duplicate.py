def Duplicates(nums)-> any:
    seen = set()
    for i in nums:
        if i in seen:
            return seen
        seen.add(i)
    return seen
        
list1 = [1,2,3,4,5,6,7,7,6,5,4,3,2]
list2 = Duplicates(list1)
print(list2)

list3 = set(list1)
print(list3)

name1 = "peddireddy"
name2= set(name1)

print(name2)


def missingNumber(nums,n) -> any:
    for i in range(n):
        if i not in nums:
            return i
        # return i

list1 = [0,1,2,3,5,6,7]
print(missingNumber(list1,8))