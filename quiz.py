#Charlie Goodrich
#12/04/17
#quiz.py - QUIZ!!!!!!

from random import randint

def rand5():
    L = []
    i = 1
    while i <= 5:
        L.append(randint(1,100))
        i += 1
    return L

def lastElement(L):
    return L[-1]

def wordLengths(L):
    A = [] #creating a new list for the lengths of the words
    for word in L:
        A.append(len(word))
    return A

def biggest(L):
    L.sort()
    return L[-1]

print(rand5())
print(lastElement(["cat","dog","rat"]))
print(wordLengths(["the","cat","is","hungry"]))
print(biggest([3,-1,5,-2,7,2,1]))