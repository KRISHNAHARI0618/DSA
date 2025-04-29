print("Congratulations Python Learning Is booming...")

# Prime Number is which is having 1 and itself as a factors
print()

n = int(input("Please Enter The Number .... "))
count = 0
factors_list = []
if n > 1:
    for i in range(1,n+1):
        if n % i == 0:
            count = count + 1
            factors_list.append(i)
    if count == 2:
        print(f"The given number {n} is a Prime Number ..")
    else:
        print(f"The Given number {n} is not a Prime Number...")
print(factors_list)