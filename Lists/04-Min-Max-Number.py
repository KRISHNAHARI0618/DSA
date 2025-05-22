# Get The Minimum and Maximum Number Using Enumerate Function

a = [1,7,3,5,9,2,8]
min_value = max_value = a[0]
min_index = max_index = 0

for index,value in enumerate(a):
    if value > max_value:
        max_value = value
        max_index = index
    if value < min_value:
        min_value = value
        min_index = index
print(min_value,max_value,min_index,max_index)

# Using For Loop instead of enumerate/ index,value == index , a[index] 

# Using Built-in Method min and max

# Using Sorted and find first and last objects 
