def GroupAnagrams(strs:list[str]) -> list[list[str]]:
    res = {[]}
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c)-ord("a")] += 1
        res[tuple(count)].append(s)
    return res.values()
    
list = ["cat","bat","mat","sat","eat","dat"]
GroupAnagrams(list)

print(ord('A'))