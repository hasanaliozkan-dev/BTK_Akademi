from datetime import datetime
from datetime import timedelta

"""result = dir(datetime.datetime)
result = dir(datetime.date)
result = dir(datetime.time)
şimdi = datetime.now()
result = şimdi.month
result = şimdi.year
result = şimdi.day
result = şimdi.hour
result = şimdi.minute
result = şimdi.second
result = datetime.ctime(şimdi)

result = datetime.strftime(şimdi,"%Y")
result = datetime.strftime(şimdi,"%X")
result = datetime.strftime(şimdi,"%d")
result = datetime.strftime(şimdi,"%A")
result = datetime.strftime(şimdi,"%B")

result = datetime.strftime(şimdi,"%Y %B %A")"""

t = "09 August 2020 hour 21:00:25"
dt = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")

birthday = datetime(1999,6,18)

#result = datetime.timestamp(birthday)
#result = datetime.fromtimestamp(result)
#result = datetime.fromtimestamp(0)

#result = datetime.now()-birthday
#result = result.days
#result = result.seconds
#result = result.microseconds
şimdi = datetime.now()
#result = şimdi + timedelta(days = 10)
result = şimdi - timedelta(days = 10)

print(result)

