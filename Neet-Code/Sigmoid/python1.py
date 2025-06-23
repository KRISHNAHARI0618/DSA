# find number of times each word has occured in a sentence excluding punctuations
# Input: The quick brown fox jumps over the lazy dog. The dog, not amused, barked at the fox!

from os import replace


text = "The quick brown fox jumps over the lazy dog. The dog, not amused, barked at the fox!"

text2 = text.lower().replace(',',"").replace('.',"").replace('!',"")

# for i in ",.!":
#     text2 = text2.replace(i,"")

words = text2.split(" ")

word_map = {}
for word in words:
    word_map[word] = word_map.get(word,0)+1
print(word_map)








