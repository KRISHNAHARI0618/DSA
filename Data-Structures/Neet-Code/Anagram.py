from collections import Counter
from syslog import LOG_KERN


class Anagram:
    def anagrams(self,s:str,c:str)-> bool:
        # return Counter(s) == Counter(c)
        countS ,countT = {}, {}
        if len(s) != len(c):
            return False
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[c[i]] = 1 + countT.get(c[i],0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True 
 
sol = Anagram()
res = sol.anagrams("anagram","nagraam")
print(res)

def countChars(n:str):
    dicts = {}
    for i in range(len(n)):
        dicts[n[i]] = 1 + dicts.get(n[i],0)
        print(dicts[n[i]])

result = countChars("peddireddy")


def anagramsCount(s:str,c:str):
    dictS,dictC = {},{}
    if len(s) != len(c):
        return False
    for i in range(len(s)):
        dictS[s[i]] = 1 + dictS.get(s[i],0) # a = 1 b = 1 c = 1 a = 2 b = 2 c = 2
        dictC[c[i]] = 1 + dictC.get(c[i],0) # b = 1 b = 2 c = 1 c = 2 a = 1 a = 2
    for c in dictS:
        if dictS[c] != dictC.get(c,0):
            return False
    return True

print(anagramsCount("abcabc","bbccaa"))

name = "peddireddy"
dictAB = {}
for i in range(len(name)):
    print(name[i])
    dictAB[name[i]] = 1+dictAB.get(name[i],0)
print(dictAB)
