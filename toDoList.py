#Charlie Goodrich
#11/16/17
#toDoList.py - makes a to do list that you can add stuff to

toDoList = []
validCommands = "add, delete, print, quit"
print("Valid commands are:", validCommands)

while True:
    toDo = input("> ")
    if toDo[0:2] == "add":
        toDoList.append(toDo[4:])
    elif toDo == "done":
        break
    
print(toDoList[:])
    
    