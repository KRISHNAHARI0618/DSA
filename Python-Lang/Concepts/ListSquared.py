# Using normal For loop
ls = [1,2,3,4,5,6,7,8,9]
res = [(n,n**2) for n in ls]
print(res)

# Using Map Function
result = list(map(lambda a: (a,a**2),ls))
print(result)

# Using for loop and appending
res = []
for n in ls:
    res.append((n,n**2))
print(res)

# Closest Pair in Kth Index in tuple

k = 2
temp = sorted(ls)
print(temp)

tuep = tuple(temp[-k:])
print(tuep)

# Closet Pair to Kth index using for loop

k = 2
res = []
temp1 = sorted(ls)
for i , val in enumerate(temp1):
    if i >= len(temp1) - k:
        res.append(val)
print(tuple(res))
