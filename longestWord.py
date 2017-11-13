#Charlie Goodrich
#11/13/17
#longestWord.py - prints the longest word

words = input("Enter some words, dood: ").split()


l = 0
word = ""
for w in words:
    length = len(w)
    if length > l:
        l = length
        word = w
print("The longest word is", word)