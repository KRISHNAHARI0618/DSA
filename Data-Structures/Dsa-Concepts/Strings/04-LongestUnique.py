name= "peddireddy"
seen = {}
maxLen = 0
start = 0
for i in range(len(name)):
    char = str(i)
    if char in seen:
        start = max(start,seen[char]+1)
    maxLen = max(maxLen,i-start+1)
    seen[char] = i
print(maxLen)
print(seen)