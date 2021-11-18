import datetime
import os
import time

iteraciones = 0

while iteraciones < 100:
    dt = datetime.datetime.now()
    print(dt.strftime("%H:%M:%S"))
    time.sleep(2)
    os.system("cls")
    iteraciones += 1