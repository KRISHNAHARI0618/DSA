s = "geeks for geeeks"

# Using For Loop Reverse the words
words = s.split()
print(words)
reverse_words = " "
for word in reversed(words):
    reverse_words = reverse_words + word + " "
print(reverse_words)

# Using For Loop Reverse the String
rev_word=" "
for i in reversed(s):
    rev_word = rev_word + i
print(rev_word)

# Reversed Function

wordsStr = s.split()
revWord = " "
for word in wordsStr:
    for i in word:
        revWord = i + revWord +" "
    revWord = revWord + " "
print(revWord)

# Lambda Function - Expression
s1 = "i am hari"
s2 = "hari"

s3 = lambda x,y : "true" if x in y else "false"
print(s3(s2,s1)) 

s3 = list(filter(lambda x :( s2 in s1),s1.split()) )
print(["yes" if s3 else "no"])