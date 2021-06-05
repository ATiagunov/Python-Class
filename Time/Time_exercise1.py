import time

def count_sec(x):
    if x > 0:
        time.sleep(x)
        x = int(input("Введите число:"))
        return(count_sec(x))
    return


n = int(input("Введите число:"))
print(count_sec(n))
