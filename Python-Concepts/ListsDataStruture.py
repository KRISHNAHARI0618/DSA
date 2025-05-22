'''
List: is a Data Stucture that holds an ordered collection of items
- we can store mix of elements of datatypes
- no fixed length
- List inside list is called nested list
- List are mutable data structure
- Time complexity is O(1) for accesing an element
- Space Complexity is O(1) for accessing element
- List Methods --> O(n) Time Complexity
  - insert() --> we can add index and element --> O(n)
  - append() --> at the end it will get add --> O(1)
  - extend() --> we can add another list to mylist --> O(n)
  - pop() --> takes index as element --> O(1)/O(n)
  - Remove() --> O(n)
  - Delete() --> O(n)
  - Linear Search() --> O(n)
'''

from numpy import average, delete
import numpy


Datas = [1,2,"Hari","Vardhan","Chiyyapady",[4,5,6,"chapad","proddatur"]]
print(Datas[5][4])

# Accesing and Traversing
shoppingList = ['Milk','banana','cheese','butter','chillis']
print(shoppingList)
print(shoppingList[1])

try:
    shoppingList[4]
    print('butter' in shoppingList)
    print(shoppingList[::-1])
    for i in shoppingList:
        print(i)
    for i in range(len(shoppingList)):
        print(shoppingList[i])
    shoppingList[1] = 'Custard Apple'
    print(shoppingList)

    shoppingList.insert(3,'lemons')
    print(shoppingList)
except Exception as e:
    print(e)
finally:
    print("Please Mention List ...")

shoppingList.append('brinjals')
print(shoppingList)

list2 = ['curd','chicken','mutton']
shoppingList.extend(list2)
print(shoppingList)

# Deleting an Element
print("Deleting the list ....................*****************")
print(shoppingList[:])

shoppingList.pop()
print(shoppingList)

delete(shoppingList,2)
print(shoppingList)

del shoppingList[2:4]
print(shoppingList)

## Searching An element in list using IN Operator

if "curd" in shoppingList:
    print("Curd is there in list")
else:
    print("Element Not Found...")

def lSearch(list,target):
    for index,value in enumerate(list):
        if value == target:
            print(index)
    print(-1)

lSearch(shoppingList,'buttor')

# Pop metod will delete end of list element when you do not mention index number
# Delete will take list as an iterable
# List Cannot be interpreted as a Integer for --> range(list)
# Update/Insert

a = [1,2,3]
a = a*3
print(a)
print(len(a))
print(max(a))
print(min(a))
print(sum(a))

print(average(a))
print("*********")

## List And Strings
name = 'peddireddy'
Names = list(name)
print(Names)

a = "hari-vardhan-reddy-peddireddy"
delimiter = '-'

b = a.split(delimiter)
print(b)
c= delimiter.join(b)
print(c)

myArray= numpy.array([1,2,3,4,5,6,7,8])
myList = [1,2,3,4,5,6,7,8]

print(myArray/2)

# List Comphrehension
list1 = [10,20,30,40,50,60]
list2 = [(item*2)/2 for item in list1]
print(list2)

# Conditional List Comphrehension

a = [20,40,60,80,101,120]
b = [i for i in a if i %2 == 0]
print(b)

