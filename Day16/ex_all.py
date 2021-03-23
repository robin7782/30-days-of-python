
#Exercise
#Problem 1
from datetime import datetime
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute, timestamp)

#Problem 2
from datetime import datetime
now = datetime.now()
time = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time)

#Problem 3
from datetime import datetime
time_string = "5 December, 2019"
time = datetime.strptime(time_string, "%d %B, %Y")
print(time)

#Problem 4
from datetime import datetime
now = datetime(year = 2021, month = 3, day = 1, hour = 17, minute = 49, second = 0)
new_year = datetime(year = 2022, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = new_year - now
print('Time left for new year:', diff)

#Problem 5
from datetime import date
then = date(day = 1, month = 1, year = 1970)
now = date(day = 1, month = 3, year = 2021)
diff = now - then
print(diff)