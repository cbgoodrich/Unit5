#Charlie Goodrich
#11/13/17
#middleWord.py - prints the middle word of a list

words = input("Enter some words: ").split()
length = len(words)

if length%2 == 0:
    print(words[length/2-1], words[length/2])
else:
    print(words[length//2])
