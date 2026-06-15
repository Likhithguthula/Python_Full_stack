'''
Date and Time ---> Python provides the built-in data time module to work with dates and time...
Ex:-

Import datetime
----------------
'''
import datetime
today = datetime.date.today()
now = datetime.datetime.now()
print(today)
print(now)

import datetime
now = datetime.datetime.now()
print(f"Year is: {now.year}")
print(f"Month is: {now.month}")
print(f"Day is: {now.day}")
print(f"Hour is: {now.hour}")
print(f"Minutes is: {now.minute}")
print(f"Second is: {now.second}")

'''
Formatting date and time ---> strftime() is used to formate date and time.
             %d ---> day, %m ---> month, %Y ---> Year, %H ---> Hour, %M ---> min, %S ---> second
Ex:-
'''
import datetime
now = datetime.datetime.now()
print(now.strftime("%d-%m-%y"))
print(now.strftime("%H-%M-%S"))

import datetime
date_1 = datetime.date(2026,6,1)
date_2 = datetime.date(2026,6,15)
differ = date_2 - date_1
print(date_1)
print(date_2)
print(differ)

'''
Timedelta
----------
Ex:-
'''
import datetime
today = datetime.date.today()
future = today + datetime.timedelta(days = 7)
print(future)

import datetime
day = datetime.date.today()
print(day.weekday())

import datetime
day = datetime.date.today()
print(day.ctime())

'''
To print the Calender
-----------------------
Ex:-
'''
import calendar
import datetime
today = datetime.date.today()
year = today.year
month = today.month
print(calendar.month(year,month))

import calendar
year = 2025
month = 7
print(calendar.month(year,month))

import calendar
#year = 2025
print(calendar.calendar(2026))






















