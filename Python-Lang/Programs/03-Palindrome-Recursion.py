# Using Recursion Method

def isPalindrome(s,i,j):
    if i >= j:
        return True
    if s[i] != s[j]:
        return False
    return isPalindrome(s,i+1,j-1)

s = "geeks"
i = 0
j = len(s)-1
if isPalindrome(s,i,j):
    print("Yes")
else:
    print("No")

# Using Loop O(n) --> time complexity

s = "peddireddy"
rev = "" # empty p,ep,dep,ddep
for char in s:
    rev = char+rev #p, ep, dep, ddep iddep,riddep,
    print(rev)
if s == rev:
    print("Yes")
else:
    print("No")

# Reverse the string Slicing
name = "peddireddy"
name1 = name[::-1]
print(name,name1)
# Reversed Method
name2 = "peddireddy"
name3 = ''.join(reversed(s))
print(name2,name3)