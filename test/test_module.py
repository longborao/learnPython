import time, datetime, calendar
today = datetime.date.today()
l = list()
for i in range(7):
    i=i+1
    delta_days = datetime.timedelta(i)
    l.append((today-delta_days).strftime('%Y-%m-%d'))
print l[6]