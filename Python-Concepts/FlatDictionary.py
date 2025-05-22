import enum

from sklearn.utils import resample


# a = [('name','alice'),('age',25),('subjects','maths'),('city','newyork')]
# print(a)
# print(dict(a))

# print(id(a))

# list = [1,2,7,9,3,5,8,4,5,9,7,2,3,4,5,6,3]
# print(list)
# for i, j in enumerate(list):
#     print(f"{i} : {j}",end=" ")
# print()
# # eumerate will give counter to each iterable enumerate(iterable,start=0)
# for i in enumerate(list,1):
#     print(str(i))

# a = list
# b = enumerate(a)
# nxt_value= next(b)
# print(nxt_value)

# nxt_value = next(b)
# print(nxt_value)

tupe = (3,4,7,9,1,6,8,11,0,5,2)
print(tupe)

k = 1
res = []
list_tupe = list(sorted(tupe))
print(list_tupe)

for id,val in enumerate(list_tupe):
    print(id,val)
    if id < k or id >= len(list_tupe) - k:
        res.append(val)
res = tuple(res)
print(res)


tupe1= tupe
k = 2
lstTupe = list(tupe1)
temp = sorted(lstTupe)
res = tuple(temp[:k]+temp[-k:])
print(res)