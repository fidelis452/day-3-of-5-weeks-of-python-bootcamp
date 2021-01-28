# print today's date
# print yesterday's date
# ask a user to enter a date
# print the date one week from the date entered

from datetime import date, timedelta
from dateutil import parser
today = date.today()
yesterday = today - timedelta(days = 1)
print(today)
print(yesterday)

date = parser.parse(input("Enter date: "))
date = date - timedelta(days = 7)
print(date)