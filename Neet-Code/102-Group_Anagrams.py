from ast import List
from collections import defaultdict


words = ["cat","tac","atc","act","red","der","edr"]

def groupAnagrams(words):
    res = defaultdict(list)
    for word in words:
        count = [0]* 26
        for char in word:
            count[ord(char)-ord('a')] = count[ord(char)-ord('a')] + 1
        res[tuple(count)].append(word)
    return res.values()

print(groupAnagrams(words))


# HashMap Usage

nums = [1,2,3,1,3,4,5,6,7]
hashMap = {}
for i in nums:
    hashMap[i] = hashMap.get(i,0) + 1
    
print(hashMap)

