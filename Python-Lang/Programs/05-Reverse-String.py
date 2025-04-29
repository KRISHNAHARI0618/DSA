# reverse words in a given string in a python

#1 Using Split() abd Join() 

from inspect import stack
from re import split
from shlex import join

s = "Hello my name is hari"
l = s.split()
print(l)
print(l[::-1])

reversed_words = ' '.join(s.split()[::-1])
print(reversed_words)
r = " "
for i in l[::-1]:
    r = r + ''.join(reversed(i)) + ' '
print(r)

# Using Normal for Loop

s = "my name is Hari"
words = s.split()
print(words)
reversed_words = ""

for word in reversed(words):
    reversed_words = reversed_words+word+" "

print(reversed_words)
rev_string = " "
for i in reversed_words[::-1]:
    rev_string = rev_string + i + " "
print(rev_string)


# Using Stack we can do that

s = "Hello world"

words = s.split()
stack = []
for word in words:
    stack.append(word)

reversedWords = ""

while stack:
    reversedWords = reversedWords + stack.pop()+" "

reversedWords = reversedWords.strip()
print(reversedWords)



