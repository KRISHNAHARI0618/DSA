s = "geeks for geeks simple language"

words = s.split()
even_word = []
for word in words:
    if len(word) %2 ==0:
        even_word.append(word)
print(even_word)
even_word = " ".join(reversed(even_word))
print(even_word)


evenWord = filter(lambda x : len(x) %2 == 0,words)
res = " ".join(evenWord)
print(res)