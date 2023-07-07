#Dates#

from datetime import datetime
now = datetime.now()
print(now.hour)
print(now.minute)
print(now.day)
print(datetime.now())

timestamp = now.timestamp()
print(timestamp)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second) 
    

year_2023= datetime(2023, 1, 1) #definir fecha en especifico

print_date(year_2023)

from datetime import time

current_time= time(21, 6 ,10)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date
current_date= date(2023, 6 ,10)
current_day = date.today()
print(current_date.day)
print(current_date.year)
print(current_date.month)
print(current_day)

current_date = date(current_date.year, current_date.month +1, current_date.day)
print(current_date)

from datetime import timedelta 
time_delta= timedelta()



