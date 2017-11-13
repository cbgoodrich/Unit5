#Charlie Goodrich
#11/13/17
#longestWord.py - prints the longest word

words = input("Enter some words: ").split()


l = 0
word = ""
for w in words:
    length = len(w)
    if length > l:
        l = length
        word = w
print("the longest word is",word)