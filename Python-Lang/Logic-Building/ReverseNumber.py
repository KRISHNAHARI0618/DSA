# Logic Building
# Reverse the Number

number = 12345
rev = 0
while(number > 0):
    a = number % 10
    rev = rev * 10 + a
    number = number // 10
print(rev)

# Using String Reverse Function

number = 5820

stringNumber = str(number)
stringNumber= list(stringNumber)
print(stringNumber)

# reversing
stringNumber.reverse()
stringNumber = ''.join(stringNumber)
numberReversed = int(stringNumber)
print(numberReversed)


print(4 // 2)