# Brute Force Method Using for Loops
name="peddireddy"

def nonRepeat(name):
    for i in range(len(name)):
        repeat = False
        for j in range(len(name)):
            if i != j and name[i] == name[j]:
                repeat = True
        if  repeat == False:
            print(name[i],i)
    return None

nonRepeat(name)

## Using Hashing Method

name="Peddireddy"
def NonRepeat(name)-> any:
    dupName = {}
    for i in name:
        if i in dupName:
            dupName[i] = dupName[i] + 1
        else:
            dupName[i] = 1
    print(dupName)

    for i in range(len(name)):
        if dupName[name[i]] > 1:
            print(name[i],i)


NonRepeat(name)

