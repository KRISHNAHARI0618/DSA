from math import sqrt


print("Peddireddy")
n= 36
print(sqrt(n))
adder = []
for i in range(1,int(sqrt(n))+1):
    if n % i == 0:
        adder.append(i)
        if n / i != i:
            adder.append(int(n/i))

print(adder)

## Count the Prime Factors or divisors

n  = 100
count = 0
primes = []
for i in range(1,int(sqrt(n))+1):
    if n % i == 0:
        primes.append(i)
        count = count + 1
        if n / i != i:
            primes.append(int(n/i))

print(primes)
if count == 2:
    print(f"This is a Prime Number {count}")
else:
    print(f"This is not Prime {count}")