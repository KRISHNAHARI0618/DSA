s= ['1','2','3','4','5','6']
res = map(int ,s)
print(list(res))


def decorator(func):
    def wrapper():
        print("Before Calling the function...")
        func()
        print("After Calling the function...")
    return wrapper

@decorator
def greet():
    print("Hello World...")

greet()

print(abs(-1))

print(abs(3-4j))

list = [1,4,5,9,24,67]
print(all(list))

tpl = (1,9,7,5,3)
print(all(tpl))

# All will check all are true
# any will check if anyone is true
# abs will check and retruns the absolute value


print(ascii("&"))

x = bin(10)
print(x)

a =  "geeks"
b = bytes(a,'utf-8')
print(b)
for i in range(95,122):
    s = chr(i)
    print(s,end=" ")
for i in range(65,90):
    print(chr(i),end=" ")
