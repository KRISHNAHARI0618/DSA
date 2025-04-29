print("peddireddy hari vardhan reddy")

"""
pointer moving right 
another pointer moving left 

i = i+1
j = j-1
s = "malayalam"

i = 0
j = len(s)-1

"""
# Using Two Pointer Approach, we have compared A string as well
s = "abababababa"

i = 0
j = len(s) - 1
print(i)
print(j)
is_palindrome = True
while i < j:
    if s[i] != s[j]:
        is_palindrome = False
        break
    i = i+1
    j = j-1

if is_palindrome:
    print("Yes")
else:
    print("No")

# Using Two Pointer Approach, we have compared a list as well

list1 = [1,2,1]
i = 0
j = len(list1) - 1
print(i)
print(j)
is_palindrome = True
while i < j:
    if list1[i] != list1[j]:
        is_palindrome = False
        break
    i += 1
    j -=1
if is_palindrome:
    print("yes")
else:
    print("Noo Please check again")


class solution:
    def is_palindrome(self,x:int):
        strCov = str(x)
        temp = strCov
        a = 0
        b = len(strCov)-1
        while a < b:
            if strCov == strCov[::-1]:
                return True
        return False

Object1  = solution()
print(Object1.is_palindrome(121))

x = 121
print(str(x))

if x > 1:
    temp = x
    res = 0
    while x > res:
        rem = x %10
        res = res *10 + rem
        x = x//10
    if temp == x:
        print(True)
    else:
        print(False)
else:
    print(False)
