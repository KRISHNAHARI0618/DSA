# Learning Filter and Lambda Method

from functools import reduce


a = [2,4,6,8,9,10,13,14,16,18,3,5,7,9]
# def main(x):
#     return x %2 ==0
# s = filter(main,a)
# print(list(s))
# s= filter(lambda b : b**2 ,a)
# d = map(lambda x : x**2, s )
# print(list(d))

print(a)

c = map(lambda x : x **2 , a)
print(list(c))

f = filter(lambda x:x%2 == 0,a)
print(list(f))