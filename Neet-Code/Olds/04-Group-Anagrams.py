# from collections import defaultdict


# def GroupAnagrams(strs):
#     res = defaultdict()
#     for s in strs:
#         count = [0] * 26
#         for c in s:
#             count[ord(c)-ord("a")] += 1
#         res[tuple(count)].append(s)
#     return res.values()
    
# list = ["cat","bat","mat","sat","eat","dat"]
# GroupAnagrams(list)

from collections import defaultdict


print(ord('A')-ord('a'))

def groupAnagrams(strs:list[str]):
    print(strs)
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c)-ord('a')] = count[ord(c)-ord('a')] + 1
        key = tuple(count)
        res[key].append(s)
    return res.values()
             
names = ["eat","tea","ate","tan","nat"]
print(groupAnagrams(names))