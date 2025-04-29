# Using Slicing Method s[start:end:increment/decrement] s[::-1]
s = "malayalam"
print(s)
if s == s[::-1]:
    print("This is Palindrome")
else:
    print("This is not Palindrome")


for i in s[::-1]:
    print(i)

# List traversing and slicing
list = [1,2,2,1]

for i in list[::-1]:
    print(i)

# Built in method reversed()

s = "malayalam"
print(s)
rev = ''.join(reversed(s))
print(rev)
if s == rev:
    print("This is Palindrome")
else:
    print("This is Not Palindrome")