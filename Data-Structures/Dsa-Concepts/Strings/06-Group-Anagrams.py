'''
strings = ["cat","act","tac","atc","tca","car","rac","acr","cra","abc","acb"]

sortedlist = [''.join(sorted(i)) for i in strings]
print(sortedlist)
hash= {}
for i in range(len(sortedlist)):
    if sortedlist[i] in hash:
        hash[sortedlist[i]].append(strings[i])
    else:
        hash[sortedlist[i]] = [strings[i]]

print(list(hash.values()))
'''
## Here what and all is used is 

"""
1: Take a list of strings
2: Sort them in alphabetical order
3: using loop iterate over range of sorted list
4: if sorted list is present in hashlist then it will append it to hash map
5: else add as a new key and map

"""

# Declaring List if anagram strings
strings = ["listen", "silent", "enlist", "tinsel", "inlets", "evil", "vile", "live", "veil", "angel"]

sort_list = [''.join(sorted(i)) for i in strings]
print(sort_list)

# Declare Map
hashMap = {} # This is dictionaries

for i in range(len(sort_list)):
    if sort_list[i] in hashMap:
        hashMap[sort_list[i]].append(strings[i]) 
        # Adding HashMap value as list of strings 
    else:
        hashMap[sort_list[i]] = [strings[i]] 
        # for hashmap key adding list of strings
print(list(hashMap.values()))

# Using Hash Map Make a Group of anagrams

strings = ["abc","bac","acb","cab","cba","bca"]

sortedList = ["".join(sorted(i)) for i in strings]
print(sortedList)
hashmap = {}
for i in range(len(sortedList)):
    if sortedList[i] in hashmap:
        hashmap[sortedList[i]].append(strings[i])
    else:
        hashmap[sortedList[i]] = [strings[i]]
print(list(hashmap.values()))


    
