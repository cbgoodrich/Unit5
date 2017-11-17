#Charlie Goodrich
#11/17/17
#matrixDemo.py - how to create and use a matrix

board = [["a", "b", "c"],["d", "e", "f"],["g", "h", "i"]]

def printBoard():
    for row in range(0,3):
        for column in range(0,3):
            print(board[row][column], end = " ")
        print()

printBoard()

row = int(input("Enter a row number: "))
column = int(input("Enter a column number: "))

board[row-1][column-1] = "X"

printBoard()