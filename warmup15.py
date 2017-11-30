#Charlie Goodrich
#11/30/17
#warmup15.py - takes a list of numbers then multiplies them by two

A = []

def doubled():
    while True:
        num = input("Enter a number or stop to end the program: ")
        if num == "stop":
            break
        else:
            A.append(int(num))
    B = []
    for num in A:
        B.append(num*2)
    print(A)
    print(B)
    
doubled()

