# Print All vowels in a string

from collections import Counter
from re import findall


# Using Collections.counter we found the list of vowels and strings
s = "i am learning geeks for geeks"

v = "aeiouAEIOU"

count = Counter([i for i in s if i in v])

print(count)

# Str.Count will found out the list 
s = "i am learning python "
v = "aeiouAEIOU"

count = {i: s.count(i) for i in v if i in s}
print(count)


# Using Regular Expression
s = "python is fun"
v = r"[aeiouAEIOU]"
vowels = findall(v,s) # This is Finding all vowels 
cnt = [{i:vowels.count(i) for i in vowels}] # This is not required here exactly 
print(vowels)
print(cnt)

# Using Filter Meethod
s = "Python is FUN i am learning devops"
v = "aeiouAEIOU"
fv=list(filter(lambda char : char in v,s))
print(fv)
print(set(fv))

cnt = {sv:fv.count(sv) for sv in set(fv)}
print(cnt)


# Using Manual Loop

s = "i am Learning devops and data structures"

v = "aeiouAEIOU"

counts = {}
print(counts.get('a',0))
for i in s:
    print(i,end="")
    if i in v:
        counts[i] = counts.get(i,0)+1
print()
print(counts)

findings = {'a':2,'a': 5}
print(findings.get('a',0))
# New Things Learnt
# str.count() --> Which prints counts in loop of items
# Counter() From Collections which collect all the items 
# Counter([list])
# dictionary.get('char',0) 
print(Counter([1,2,2,1,3,3,4,4]))
