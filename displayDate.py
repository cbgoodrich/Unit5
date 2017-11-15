#Charlie Goodrich
#11/15/17
#displayDate.py - displays today's date

from datetime import date
from calendar import weekday

day = date.today().day
month = date.today().month
year = date.today().year

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


print(weekday(year, month, day))
