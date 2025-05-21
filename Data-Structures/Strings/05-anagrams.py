# Using Sorted Method

from collections import Counter

s1 = "silent"
s2 = "listen"

if sorted(s1) == sorted(s2):
    print(True)
else:
    print(False)

# Using HashMap

n1 = Counter(s1)
print(n1)
n2 = Counter(s2)
print(n2)

if Counter(s1) == Counter(s2):
    print("Yes")
else:
    print("No")



