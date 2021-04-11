import time


bday = input("Введите дату рождения в формате: dd.mm.YYYY\n")
birth_date = time.strptime(bday,'%d.%m.%Y')
delta = time.time() - time.mktime(birth_date)
n = int(delta / (60 * 60 * 24))
print(f"Вы живете {n} дней")

