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

def missingNumber(arr,n) -> any:
    nums = []
    for i in range(n):
        if i not in arr:
            nums.append(i)
    print(nums)

missingNumber([1,2,3,4,5,6,7],10)

# Hashing Function is going to cgange




