# Using Two Pointer Approach
name="mala"

first = 0
last = len(name) -1

while first < last:
    is_palindrome = True
    if name[first] != name[last]:
        is_palindrome = False
    first = first + 1
    last = last - 1

if is_palindrome:
    print("yeahh it is palindrome..")
else:
    print("Bad its not palindrome")