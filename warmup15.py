#Charlie Goodrich
#11/30/17
#warmup15.py - takes a list of numbers then multiplies them by two

A = []

def doubled(A):
    B = []
    for num in A:
        B.append(num*2)
    return B
    
print(doubled([2,4,6,8,10]))
    

