n1 = [9,8,7,6,5,3,2]

n2 = [1,2,3,4,5,6]

hashSet = set()
for i in n1:
    hashSet.add(i)
for j in n2:
    hashSet.add(j)

print(list(hashSet))


def UnionElements(a,b):
    res = []
    n,m = len(a), len(b)
    i ,j= 0,0
    if n >= m:
        while i < n and j < m:
            if i> 0 and a[i-1] == a[i]:
                i= i + 1
                continue
            if j > 0 and b[j-1] == b[j]:
                j = j + 1
                continue
            if a[i] < a[j]:
                res.append(a[i])
                i = i + 1
            elif a[i] > b[j]:
                res.append(b[j])
                j= j + 1
            else:
                res.append(a[i])
                i= i + 1
                j= j + 1
        while i < n:
            if i > 0 and a[i-1] == a[i]:
                i = i + 1
                continue
            res.append(a[i])
            i = i + 1
        while j < n:
            if j > 0 and a[j-1] == a[j]:
                j = j + 1
                continue
            res.append(a[j])
            j = j + 1
    return res

n3 = UnionElements(n1,n2)
print(n3)