import os
import time

hours = time.gmtime().tm_hour + 1
minutes = time.gmtime().tm_min
seconds = time.gmtime().tm_sec

print(hours, ":", minutes, ":", seconds)

time.sleep(300)

os.system("shutdown /s /t 90")