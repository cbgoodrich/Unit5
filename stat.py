#Charlie Goodrich
#11/15/17
#stat.py - does statistical analysis of inputted numbers

print("Type a list of numbers")
print("Enter 'q' when finished")
numbers = []
while True:
    num = input("> ")
    if num == "q":
        break
    else:
        numbers.append(float(num))
        
numbers.sort()

print("Min:", numbers[0])
print("Max:", numbers[-1])
print("Mean:", sum(numbers)/len(numbers))


    