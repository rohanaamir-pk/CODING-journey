#DATETIME---//DAY-12//

from datetime import  *

#Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38


#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
now = datetime.now()
dt = now.strftime( "%m/%d/%y, %H:%M:%S" )
print(dt)

#Today is 5 December, 2019. Change this time string to time.
date_str = "5 December, 2019"
date_dig = datetime.strptime(date_str, "%d %B, %Y")
print(date_dig)

#Calculate the time difference between now and new year.
new_year = date(year = 2027, month = 1, day = 1)
today = date.today()
time_left = new_year - today
print(time_left)

#Calculate the time difference between 1 January 1970 and now.
old_time = datetime(year = 1970, month=1, day=1, hour=1, minute=23, second=45 )
current_time = datetime.now()
print( current_time - old_time)

