# Reverse The array Program
"""
list1 = [1,2,3,4,5]
revList = [5,4,3,2,1]

Types of Operations:
1: Slicing 
2: Reverse Method
3: Using Loops
"""

list1 = [1,2,3,4,5]
print(list1)

# Slicing Method

revList = list1[::-1]
print(revList)

# Reverese Method
list1.reverse()
print(list1)

# Using Loops

list2 = []
for i in range(len(list1)-1,-1,-1): # (5)
    list2.append(list1[i])
print(list2)

my_list = [1, 2, 3, 4, 5]
reversed_list = []
for item in my_list:
    reversed_list.insert(0, item)
print(reversed_list)  # Output: [5, 4, 3, 2, 1]