import re 

txt = "The spain in water rain"
x = re.findall("ai",txt)
print(x)

name = "peddireddy"
chr_cnt = {}

for char in name:
    chr_cnt[char] = chr_cnt.get(char,0)+1
print(chr_cnt)

for char in name:
    if chr_cnt[char] == 1:
        print(char)
    else:
        print(False)


# Decorators

def decorator(func):
    def wrapper():
        print("Calling Before Decorator Function...")
        func()
        print("Calling After Decorator Function....")
    return wrapper

@decorator
def simple():
    print("Calling Simple Function as Decorator...")


simple()


def func():
    yield 1
    yield 2
    yield 3
    yield 4

for i in func():
    print(i)

sq = (x*x for x in range(1,6))

for i in sq:
    print(i)

numbers = [1,2,3,4,5,6,7]

while (n := len(numbers)) > 0:
    print(numbers.pop())


primeList = []
count = 0
for i in range(1,10):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        primeList.append(i)
print(primeList)
