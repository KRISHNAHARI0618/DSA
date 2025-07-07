print("Peddireddy Hari Vardhan Reddy")

name = "peddireddy hari vardhan reddy"


# Length Function
print(len(name))

# Count Method 
count = 0
for i in name:
    if i:
        count = count +1
print(count)


# Using Count in operator
count = 0
for chr in name:
    count = count + 1
print(count)


# Using Str Count
length = name.count("") - 1
print(length)


# enumerate function
count = 0
for index,value in enumerate(name):
    count = count + 1
print(count)

