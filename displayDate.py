#Charlie Goodrich
#11/15/17
#displayDate.py - displays today's date

from datetime import date
from calendar import weekday

dayNow = date.today().day
monthNow = date.today().month
yearNow = date.today().year

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

dayOfWeek = weekday(yearNow, monthNow, dayNow)

print("Today is", days[dayOfWeek]+",", months[monthNow-1], dayNow, yearNow)
