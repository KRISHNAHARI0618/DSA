
import re
from traceback import print_exception


def encode(s):
    res = ""
    n = len(s)
    for i in range(n):
        res = res + '#' + s[i] 

    return res

nums = ["hello","world","program"]
res = encode(nums)
print(encode(nums))


name = "peddi#reddy#hari"

i = 0
res = []
n = len(name)-1
while i < n:
    j = i
    while name[j] != '#':
        j = j + 1
    legth = int(str(name[i:j]))
    res.append(name[j+1:j+1+legth])
    i = j + legth + 1

print(res)
