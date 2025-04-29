s = "abaaba"
half = len(s)//2

print(half)
sym = s[:half] == s[half:] if len(s) % 2 == 0 else s[:half] == s[half+1:]
print(sym)
sym2 = s[half+1:]
print(sym2)

palin = s == s[::-1]

print("Symmetrical" if sym else "Not symmetrical")
print("Palindrome" if palin else "Not palidrome")

