"""
Psudocode:
1. Take the string or number as input 
2. take two pointers which iterate over
3. compare left pointer with right pointer 
    if it is not same return false\
        skipR,skipL == string[left+1:right+1] 
4. then increment the left and decrement the right 
5. iterate again and true 

"""


def removeCharPalindCheck(s):
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            skipL,skipR = s[left+1:right+1] , s[left:right]
            return (
                skipL == skipL[::-1]
                or
                skipR == skipR[::-1]
            )
        left = left + 1
        right = right - 1
    return True

print(removeCharPalindCheck("aba"))