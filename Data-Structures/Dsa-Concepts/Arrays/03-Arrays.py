# Reverse the array based on k elements

# Declaring The array
array = [1,2,3,4,5]

# Get K elements
k = 4

# Array will fully rotate for length of array elements
# k = 2 == 7 == 12 == 17 

# Modulus will give reminder hence k will modulus len(array)
k = k%len(array)

# Create a temp array with k elements
temp = array[-k:]

# Printing temp Array
print(temp)

# Iterate over the length 0f array minus k elements
for i in reversed(range(0,len(array)-k)):
    # Reversed = reversed(0,1,2) == (2,1,0) 
    # a[2+2] = a[2] == 3 , a[1+2] = a[1] == 2 , a[0+2] = a[0] == 1
    # length(array) = 5 - 2 == 3 == i = 0 , 1 , 2
    array[i+k] = array[i]  # a[0+2] = a[0] = 1 , a[1+2] = a[2] = 2

for i in range(len(temp)):
    array[i] = temp[i]

print(array) 




