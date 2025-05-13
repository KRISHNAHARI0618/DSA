abc = [1,2,3,4,5,6,7,8,9,11,13,14,15,16]

def even(numbers)-> any:
    if numbers % 2 == 0:
        return numbers

x = filter(even,abc)
y = filter(lambda x : x % 2 == 0,abc)
print(list(x))
print(list(y))

# Symmetrical or Palindrome

s = "abcba"

half = len(s)//2

sym = s[half:] == s[:half] if len(s)%2 == 0 else s[half:] == s[:half+1]

print(sym)

palindrome = s[::] == s[::-1]
print(palindrome)

print(f"{s} is symmetrical" if sym else f"{s} Not Symmetrical")
print(f"{s} is Palindrome" if palindrome else f"{s} Not Palindrome ")


# Using Two Pointers

pal = True
start = 0
end = len(s)-1

while start < end:
    if s[start] != s[end]:
        pal = False
        break
    start = start + 1
    end = end - 1

print(f"{s} is palindrome" if pal else f"{s} is not palindrome")

# Using Two Pointers Symmetrical Found

sym = True
half = len(s) // 2
print(half)

for i in range(len(s)):
    if len(s) % 2 == 0:
        if s[i] != s[i+half]:
            sym = False
            break
        else:
            if s[i] != s[i+half+1]:
                sym = False
                break

print(s[:3])
print(s[2:])


arr = [1,2,3,4,5]
print(arr[-2:])

newArr = arr[-2:]
arr.append(newArr)
print(arr)
