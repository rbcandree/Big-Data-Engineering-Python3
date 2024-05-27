"""
Timestamps are important for data preprocessing. Familiarize yourself with Pythons datetime module. 
A decent tutorial can be found here:
https://note.nkmk.me/en/python-datetime-usage/

Solve the exercises:

1. Write a program that prints the following information on screen:
a) You can do certain algebraic operations on datetime objects.
Create 2 separate datetime objects that refer to different points in time and explore the results of following operations:
dt_obj_1 - dt_obj_2
dt_obj_1 < dt_obj_2
What can you tell about the - and < operators for datatime objects?
"""
from datetime import datetime
# 1. a) Solution: 
def solution_1a():
    dt_obj_1 = datetime.now()
    dt_obj_2 = datetime(2024, 1, 1, 00, 00, 00)
    time_delta = dt_obj_1 - dt_obj_2
    print(f"Current datetime is: {dt_obj_1}")
    print(f"The difference (timedelta) between dt_obj_1 and dt_obj_2 is: {time_delta}")

    verification = dt_obj_1 < dt_obj_2
    print(f"Verify if the dt_obj_1 is less than dt_obj_2: {verification}")
# Operator '-' allows to subtract one datetime object from another one and returns a timedelta object.
# Operators '>', '<' compares datetime objects as an integers and returns Boolean values: True or False.
"""
b) Print the current time in epoch format on screen.
What kind of operations are available for time represented in epoch format?
Convert the seconds since epoch to a more human readable format and print that also on the screen.
"""
# 1. b) Solution:
from time import time, ctime
def solution_1b():
    # An example of a time object in epoch format: 1598653800
    epoch_current_time = time()
    print(f"Current time represented in epoch format: {epoch_current_time}")
    
    human_readable_current_time = ctime(epoch_current_time)
    print(f"Current time in human readable format: {human_readable_current_time}")
# Time represented in epoch format is Float, thus operations such as: -, +, *, /, //, %, >, < are available.
"""
2. Given a string "2020-09-28  18:47:50", convert the string into a datetime object. 
Access the objects year, month, day and hour attributes separately and print the results on screen. 
Raise all of these values by one.
Convert the resulting datetime object into a string of format YYYY-mm-dd HH:MM:SS.
Do the same conversion but with the resulting string in format:
"It's year 2021, day 29 of month 10 and it is 19:47:50."
"""
# 2. Solution:
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta 
def solution_2():
    date_as_str = "2020-09-28  18:47:50"
    format_str = "%Y-%m-%d %H:%M:%S"
    date_obj = datetime.strptime(date_as_str, format_str)
    print(f"Converted string to a datetime object: {date_obj}")

    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    hour = date_obj.hour
    print(f"Year: {year}, Month: {month}, Day: {day}, Hour: {hour}")

    date_obj = date_obj + relativedelta(years = 1)
    date_obj = date_obj + relativedelta(months = 1)
    date_obj = date_obj + timedelta(days = 1)
    date_obj = date_obj + timedelta(hours = 1)
    print(f"Datetime object with raised values by one: {date_obj}")

    date_obj_convert = date_obj.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Converted new datetime object to a string: {date_obj_convert}")

    date_obj_convert1 = date_obj.strftime("It's year %Y, day %d of month %m and it is %H:%M:%S.")
    print(date_obj_convert1)
"""
3.
a) Find out programmatically which day of the week was on 1.10.1999
b) Find out programmatically which date (dd.mm.yyyy) is 27 weeks before 1.10.1999
c) Find out programmatically which day of the week is 157 days after 1.10.1999
(hint: strftime() method may help you with these)
"""
# 3. Solution:
def solution_3():
    dt_obj_a = datetime(1999, 10, 1, 0, 0, 0)
    epoch_time = dt_obj_a.timestamp()
    conv = ctime(epoch_time)
    print(f"What day of the week was October 1st, 1999? - It was {conv[0:3]}.")

    dt_obj_b = dt_obj_a - timedelta(weeks = 27)
    weekday = dt_obj_b.strftime('%A')
    day_of_the_month = dt_obj_b.strftime('%d')
    month = dt_obj_b.strftime('%B')
    print(f"Which day was it 27 weeks before October 1st, 1999? - It was {weekday}, {day_of_the_month}th of {month}.")

    dt_obj_c = dt_obj_a + timedelta(days = 157)
    weekday_c = dt_obj_c.strftime('%A')
    print(f"Which day of the week is 157 days after October 1st, 1999? - It is {weekday_c}.")

if __name__ == '__main__':
    solution_1a()
    solution_1b()
    solution_2()
    solution_3()