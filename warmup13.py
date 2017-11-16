#Charlie Goodrich
#11/16/17
#warmup13.py - makes 20 random #'s gives min, max, and sum

from random import randint

numbers = []
i = 2

while i <= 21:
    num = randint(1, i)
    numbers.append(num)
    i += 1
    
numbers.sort()
print("The min is", numbers[0])
print("The max is", numbers[-1])
print("The sum is", sum(numbers))
