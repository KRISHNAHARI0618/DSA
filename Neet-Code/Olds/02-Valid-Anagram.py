# from collections import Counter
# from syslog import LOG_KERN


# class Anagram:
#     def anagrams(self,s:str,c:str)-> bool:
#         # return Counter(s) == Counter(c)
#         countS ,countT = {}, {}
#         if len(s) != len(c):
#             return False
#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i],0)
#             countT[c[i]] = 1 + countT.get(c[i],0)
#         for c in countS:
#             if countS[c] != countT.get(c,0):
#                 return False
#         return True 
 
# sol = Anagram()
# res = sol.anagrams("anagram","nagraam")
# print(res)

# def countChars(n:str):
#     dicts = {}
#     for i in range(len(n)):
#         dicts[n[i]] = 1 + dicts.get(n[i],0)
#         print(dicts[n[i]])

# result = countChars("peddireddy")


# def anagramsCount(s:str,c:str):
#     dictS,dictC = {},{}
#     if len(s) != len(c):
#         return False
#     for i in range(len(s)):
#         dictS[s[i]] = 1 + dictS.get(s[i],0) # a = 1 b = 1 c = 1 a = 2 b = 2 c = 2
#         dictC[c[i]] = 1 + dictC.get(c[i],0) # b = 1 b = 2 c = 1 c = 2 a = 1 a = 2
#     for c in dictS:
#         if dictS[c] != dictC.get(c,0):
#             return False
#     return True

# print(anagramsCount("abcabc","bbccaa"))

# name = "peddireddy"
# dictAB = {}
# for i in range(len(name)):
#     print(name[i])
#     dictAB[name[i]] = 1+dictAB.get(name[i],0)
# print(dictAB)


from asyncio.format_helpers import _format_callback_source
from collections import Counter


def vaidAnagram(str1,str2):

    return sorted(str1) == sorted(str2)

    return Counter(str1) == Counter(str2)
    
    if len(str1) != len(str2):
        return False
    countS ,countT = {},{}
    for i in range(len(str1)):
        countS[str1[i]] = 1 + countS.get(str1[i],0)
        countT[str2[i]] = 1 + countT.get(str2[i],0)
    for c in countS:
        if countS[c] != countT.get(c,0):
            return False
    return True


name1 = "hari"
name2 = "rahi"
print(vaidAnagram(name1,name2)) 

## Revisioning Valid Anagram

def validANagram(name1,name2):
    if len(name1) != len(name2):
        return False
    countS = {}
    countT = {}
    for i in range(len(name1)):
        countS[name1[i]] = 1 + countS.get(name1[i],0)
        countT[name2[i]] = 1 + countT.get(name2[i],0)
    for c in countS:
        if countS[c] != countT.get(c,0):
            return False
    return True


nums = [2,5,8,7,9]
def sortingSelect(nums):
    low = 0
    for i in range(1,len(nums)):
        if nums[low] < nums[i]:
            nums[low],nums[i] = nums[i] ,nums[low]
            
        return nums

print(sortingSelect(nums))

string1 = "anagram"
string2= "nagaram"

count1 = {}
count2 = {}

def anagrams():
    if len(string1) != len(string2):
        return False
    for i in range(len(string1)):
        print(i)
        count1[string1[i]] = 1 + count1.get(string1[i],0)
        count2[string2[i]] = 1 + count2.get(string2[i],0)
    for c in count1:
        if count1[c] != count2.get(c,0):
            return False
    return True

obj1 = anagrams()
print(obj1)