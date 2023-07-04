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
