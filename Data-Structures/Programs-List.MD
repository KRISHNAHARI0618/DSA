# List Of Programs Youtube

- Longest Palindrome String & SubString
- Min and Max Number in an Array
- Second Largest Number in an Array
- Armstrong Number of an Array
- Contains Duplicates --> Boolean Function
- Valid Anagrams  --> Boolean Function

### Valid Anagram Psudocode

1. Anagram means the characters in the strings should be equal
2. First Check two strings are equal length then only go to next step
3. define two hashmaps hashmap1 = {} hashmap2 = {}
4. add all characters to hashsets/hashmaps using for c in hashmap1
   1. hashmap[c] = hashmap.get(c,0) + 1
5. next iterate over the hashmap1/hashmap2 
   1. check the if hashmap[character] != hashmap.get(c,0) then return false
6. else return true hence the characters are matching
7. Method2 == Counter(str1) == Counter(str2)
8. Method3 == sorted(str1) == sorted(str2)

### Rotate Array by One