
name="peddireddy"


# Using Two Pointer Method
def isPalindrome(name)-> any:
    first = 0
    last = len(name)-1
    while first < last:
        if name[first] != name[last]:
            return False
        last = last - 1
        first = first + 1
    return True

print(isPalindrome(name))

# Using Brute Force Method
name = "1aba1"
dupName = ""
for i in range(len(name)-1,-1,-1):
    dupName  = dupName + name[i]
print(dupName)

if dupName == name:
    print(True)
else:
    print(False)

# Using Arrays Method 
name = "peddiredd"
nameArr=[]
for i in range(len(name)):
    nameArr.append(name[i])
print(nameArr)

