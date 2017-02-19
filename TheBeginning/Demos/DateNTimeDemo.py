import time
import datetime
print(time.clock())
print(time.gmtime())
print(time.localtime())
print(time.time())
print(time.daylight)
print(datetime.datetime.now())
print(datetime.datetime.now()+datetime.timedelta())
print("Current Time : "+time.strftime("%c"))
print(time.strftime("%x"))
print(time.strftime("%X"))
