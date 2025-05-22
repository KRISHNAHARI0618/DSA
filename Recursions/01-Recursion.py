print("Peddireddy Hari Vardhan Reddy")

# Print The n factorial numbers

def fact(n)-> any:
    if n == 0: # Base Condition
        return 1
    return abs(n) * fact(abs(n)-1) # Recusion Condition/Call

print(fact(5))

# Using For Loop Print Factorial and Add it in Array

arr = []
for i in range(-5,6):
    arr.append(fact(i))
print(arr)
    