import time

t = time.time()

a = range(100000)
b = [i*2 for i in a]

elapsed_time = time.time() - t
print(elapsed_time)
