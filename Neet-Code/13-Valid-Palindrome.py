class validPalindrome:
    # Check the given value is valid character or not
    def isAlphanumeric(self,c) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9') )
    
    def palindromeCheck(self,s:str) -> bool:
        l,r = 0,len(s)-1
        while l < r:
            while l < r and not self.isAlphanumeric(s[l]):
                l = l+1
            while r > l and not self.isAlphanumeric(s[r]):
                r = r-1
            if s[l] != s[r]:
                return False
            l,r = l+1, r-1
        return True
# obj = validPalindrome()
# s1 = obj.palindromeCheck("9aba9")
# print(s1)

# Pattern Solution
sum = 0
for i in range(10):
    for j in range(i+1):
        sum = sum + j
    print(sum,end=" ")
        # print(j,end=" ")
    print()


def palindrome(name):
    print(name)
    
    if name[:] == name[::-1]:
        print(f"name is palindrome string {name}")

name = "malayalam"
palindrome(name)


def validPalindrome(s):
    l = 0
    r = len(s)-1
    while l < r:
        if s[l] != s[r]:
            return 1
        l = l+1
        r = r-1
    return 0

d= validPalindrome("abba") 
if d == 0:
    print("The string is palindrome")
else:
    print("The string is Not palindrome")

def IspalindromeRemove(s):
    l = 0
    r = len(s)-1
    while l < r:
        if s[l] != s[r]:  # s[1+1:4+1] s[1:4]
            skipL,skipR = s[l+1:r+1] , s[l:r]
            return (skipL == skipL[::-1] 
                    or skipR == skipR[::-1])
        l = l +1
        r = r -1
    return True

print(IspalindromeRemove("abca"))