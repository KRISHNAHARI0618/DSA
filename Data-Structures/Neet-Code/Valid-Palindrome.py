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

obj = validPalindrome()
s1 = obj.palindromeCheck("9aba9")
print(s1)

# Pattern Solution
sum = 0
for i in range(10):
    for j in range(i+1):
        sum = sum + j
    print(sum,end=" ")
        # print(j,end=" ")
    print()