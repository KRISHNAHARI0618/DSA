# print("Peddireddy")

# name = "abcdefgh"
# arr = []
# n = len(name)
# for i in range(0,n):
#     for j in range(0,i+1):
#         arr.append(name[j])
# print(arr,end=" ")
# print()

words = "abdcdkjsoruwqetyuo"
mp = {}
for i in range(len(words)):
    if words[i] in mp:
        mp[words[i]] = mp[words[i]] + 1
    else:
        mp[words[i]] = 1
print(mp)