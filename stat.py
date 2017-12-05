#Charlie Goodrich
#11/15/17
#stat.py - does statistical analysis of inputted numbers

print("Enter a list of numbers")
print("Enter 'q' when finished")
numbers = []
while True:
    num = input(">>>")
    if num == "q":
        break
    else:
        numbers.append(float(num))
        
numbers.sort()

c = 0
i = 0
for n in numbers:
    while i < len(numbers):
        count = numbers.count(numbers[i])
        if count > c:
            c = count
            mode = numbers[i]
        if c == 1 and len(numbers) > 1:
            mode = "None"
        i += 1

print("Min:", numbers[0])
print("Max:", numbers[-1])
print("Mean:", sum(numbers)/len(numbers))
print("Mode:", mode)

