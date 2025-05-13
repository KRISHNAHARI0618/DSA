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



