# Lists Concepts 
"""
1. List is an ordered collection of items , which can have multiple values and different data types 
2. This will support only on Python

"""
# Empty Lists or List Declaration

from itertools import count


my_list = []

# Adding Elements 

my_list.append(20)  # Adding number
my_list.append("hello") # Adding String
my_list.append(True) # Adding Boolean
my_list.append([1,2,3]) # Adding List
my_list.append(23.56) # Adding Float 

print(my_list)

# Inserting An Element

index = 2
object = 45.23

my_list.insert(index,object)
print(my_list)


# Deleting / Removing Elements

my_list.remove(True)
print(my_list)
my_list.pop()
print(my_list)

# Check List 
print(20 in my_list)

# Repetation
print([[my_list]*3])

# Count 
cnt = count(20)
print(cnt)

# Squares of Numbers in List

print([x*x for x in [1,2,3,4,5,6,7]])




























arr = [1,2,4,3,5,6]
newArr = []

for i in arr:
    newArr.append(i*i)
print(newArr)


# Using Brute Force Method 
# Time Complexity ---> O(nlogn) and Space Complexity ---> O(n)
def sortedArr(array)-> any:
    n = len(array)
    result = [0]*n
    for i in range(n):
        result[i] = array[i]**2
    result.sort()
    print(result)

sortedArr(arr)

# Using Two Pointer Approach 
# first = 0, last = len(array) - 1

def sortedSuare(array)-> any:
    n = len(array)
    first = 0
    last = n-1
    arr = [0]*n
    for i in range(n-1,-1,-1):
        if array[first]**2 > array[last]**2:
            arr[i] = array[first] **2
            first = first +1
        else:
            arr[i] = array[last] **2
            last = last -1
    print(arr)

sortedSuare(arr)



