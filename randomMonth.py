#Charlie Goodrich
#11/13/17
#randomMonth.py - prints a random month

from random import randint

months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

print(months[randint(0,11)])