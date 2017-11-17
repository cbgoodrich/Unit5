#Charlie Goodrich
#11/16/17
#toDoList.py - makes a to do list that you can add stuff to

toDoList = []
print("Valid commands: add, delete, print, quit")

while True:
    toDo = input("> ")
    if "quit" in toDo:
        break
    elif "print" in toDo:
        for w in toDoList:
            print(w)
    elif toDo[:4] == "add ":
        toDoList.append(toDo[4:])
    elif toDo[:7] == "delete ":
        if toDo[7:] in toDoList:
            toDoList.remove(toDo[7:])
        else:
            print(toDo[7:], "not in list")
    else:
        print("Invalid Command")
        
    
    