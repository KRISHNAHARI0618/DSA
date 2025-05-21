n1 = "aabaa"
n2 = n1[::-1]
print(n1 == n2)
dupName = ""
for i in range(len(n1)-1,-1,-1):
    dupName = dupName + n1[i]
print(dupName)

if n1 == dupName:
    print(True)
else:
    print(False)


# Using Arrays Method 

dupArray = []
for i in range(len(n1)-1,-1,-1):
    dupArray.append(n1[i])
print(dupArray)
newName = "".join(dupArray)
print(newName)
if newName == n1 :
    print(True)
else:
    print(False)

# Using Pointers Method

name = "aabaa"
first = 0
last = len(name)-1
while first < last:
    if name[first] != name[last]:
        print(False)
    last = last - 1
    first = first + 1
print(True)
    


