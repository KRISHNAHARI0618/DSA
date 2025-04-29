from re import sub
from typing import Counter


s = "peddireddy hari vardhan reddy"

sub_s = "hari"

# Using If Method
if sub_s in s:
    print("Yes Found ... ")
else:
    print("Not Found ... ")

# Using in Operator 
# Using split method
# Using Find Method

def check(string,sub_str):
    if(string.find(sub_str) == -1):
        print("Not Found ...")
    else:
        print("Yes Found ... ")

string = "geeks for geeks"
sub_str = "geeks"
check(string,sub_str)

# Using Count Method 

def check(s2,s1):
    if (s2.count(s1)> 0):
        print("Yes Found ...")
    else:
        print("Not Found ...")

s2 = "A geeks in a need is geeks indeed"
s1= "geeks"
check(s2,s1)

# Using Index Method 
s = "geeks for geeks"
s2 = list(filter(lambda s2 : (s2 in s),s.split()))
print(s2)

s=lambda a,b : a *b 
print(s(20,30))

s = "hello my name hello your name hello its name hello the name"

frequency = Counter(s.split())
print(frequency.items())

# Print Frequency of the substring

s = "peddireddy hari vardhan reddy reddy"

freq = {}
for word  in s.split():
    freq[word] = freq.get(word,0) + 1
print(freq)