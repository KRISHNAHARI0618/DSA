import os
import pathlib
import random
import string

print(os.error)

print(os.error(pathlib))

print(os.getcwd())


# Changing the directory
def current_path():
    print(os.getcwd())
    print()

current_path()
os.chdir('../')
current_path()

#Creating the directory
def make_dir():
    os.mkdir('peddireddy')
    return os.getcwd()

result = make_dir()

print("Before Deleting the Peddireddy ")
list1 = os.listdir(os.getcwd())
print(list1)

for i in list1:
    if i == "peddireddy":
        os.removedirs(i)
    if i == "WEB":
        os.rename(i,i.lower())
    if i == "Django-Notes.MD":
        os.stat(os.getcwd())
    if i == "Django":
        os.chdir(i)
        list2 = os.listdir(os.getcwd())
        print(list2)
        for i in list2:
            if i == "Peddireddy":
                os.rename(i,"Peddireddy_Hari_Personal")

print("After deleting the Peddireddy")

list1 = os.listdir(os.getcwd())
print(list1)


directory = "Peddireddy"
parent_dir = os.getcwd()
print(parent_dir)

path = os.path.join(parent_dir,directory)
mode = 0o777
try:
    os.mkdir(path,mode)
    print("Directory '%s' is Created" % directory)
except FileExistsError:
    print("Directory '%s' is Already Exists" % directory)

name1 = string.ascii_letters
print(name1)
name = random.choice(string.ascii_letters)
print(name)

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for i in range(y))

print(random_char(10))

y = 5
j1 = ''
for i in range(y):
    j1 = j1 + j1.join(random.choice(string.ascii_letters))
print(j1)

# random.sample() is differ from random.choice()
random.seed(10)
letters = string.ascii_letters
random_letters = set(random.choices(letters,k = 10)) # gives list as output
print(random_letters)

str = chr(random.randrange(97,97+26))
print(str)

print(chr(98))

print(os.system("pwd"))

print(os.uname())







