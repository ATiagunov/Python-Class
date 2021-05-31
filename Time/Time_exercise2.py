import time
import datetime
import os


with open("time_date.txt", 'w') as f:
    t = time.time()

    os.rename('time_date.txt', f'{datetime.datetime.now()}.txt')
    a = range(100000)
    b = [i*2 for i in a]

    f.write(str(time.time() - t))
