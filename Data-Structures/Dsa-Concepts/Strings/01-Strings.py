# Printing Non Repeasting Characters
# Question 1:Non repeating character - You are given a string consisting of only lower case and upper-case English Alphabets and integers 0 to 9. Write a function that will take this string as Input and return the index of the first character that is non-repeating.

## Pre Conditions
# 1: contains Lower Cases and Upper Cases are Different and alphabets 
# 2: What if it does not contains Non repeating characters
# 3: 
def repeatedChars(name)->any:
    n = len(name)
    for i in range(n):
        repeat = False
        for j in range(n):
            if i != j and name[i] == name[j]:
                repeat = True
        if repeat == False:
            print(name[i],i)
    return None

name = "peddireddy"
repeatedChars(name)



### Ussing Hashing Method Find Repeated Characters

def nonRepeating(name)-> any:
    dupName = {}
    n = len(name)
    for i in name:
        if i in dupName:
            dupName[i] = dupName[i] + 1
        else:
            dupName[i] = 1
    print("Strig Counts : " ,dupName)
    for i in range(n):
        if dupName[name[i]] == 1:
            print(name[i],i)
    return None

nonRepeating("peddireddy")

name = "peddireddy"

print(name[::]==name[::-1])
n = len(name)
for i in name[::]:
    if  i == name[::-1]:
        print(i)
    

            

