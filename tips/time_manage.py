import time
import datetime

t = datetime.datetime(2010, 3, 2, 12, 15, 0)
print(t)  # 2010-03-02 12:15:00

diff = datetime.timedelta(days=145, hours=10, minutes=3)

t = t + diff
print(t)

t1 = time.strptime('12:20:52', "%H:%M:%S")
print(t1)
# time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=12,
#                  tm_min=20, tm_sec=52, tm_wday=0, tm_yday=1, tm_isdst=-1)

t2 = time.strptime('12:20:55', "%H:%M:%S")

print(t2 > t1)  # True
