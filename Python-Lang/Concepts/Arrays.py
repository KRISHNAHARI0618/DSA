import array
import numpy as np

arr1 = array.array('i',[1,2,4,5,6,7])
print(arr1)

np_array = np.array([],dtype=int)

# Arrays is stored in contiguous memory locations
# Should be similar type of values
# How to create an array using array module,numpy package
# Creating an empty array using numpy and array module is O(1)
# New Created array will take O(n)

arr1.append(10) # adds at end 
print(arr1)

arr1.insert(3,200) # adds where ever you require
print(arr1)
print()

print(arr1[::-1])

def travs(arr1):
    for i in arr1:
        print(i)

print()
print()
print()
print(())
print()
print()
print()

print()

def zero():
    for i in range(10):
        print(i)
travs(arr1)

# Create a Two Dimensional Array

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]]) # type: ignore
print(arr2)
newArr2 = np.insert(arr2,0,[1,8,9],axis=1)
print(newArr2)

arr3 = [[1,2,3],[4,5,6],[7,8,9]]
print(arr3)

for i in range(len(arr3)):
    for j in range(len(arr3[0])):
        print(arr3[i][j],end=" ")
    print()

list1 = [2,3,4,5,6,7]
iters = iter(list1)
print(next(iters))
