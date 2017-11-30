#Charlie Goodrich
#11/30/17
#warmup15.py - takes a list of numbers then multiplies them by two

A = []

def doubled(A):
    while True:
        num = input("Enter a number, or enter stop to stop: ")
        if num == "stop":
            break
        else:
            A.append(int(num))
    
    for num in A:
        num *= 2
        
    return A
    
print(doubled[2,4,6])
