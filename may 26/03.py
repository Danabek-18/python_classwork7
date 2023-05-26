user_fleshka = input("Обьем флешки")
user_fayl = input("Обьем файла")

try:
    fleshka = int (user_fleshka)
    fayl = int (user_fayl)
except ValueError:
    message = "Вы ввели не числа" 
else:
    mb_total = fleshka * 1024
    fayl_total = mb_total// fayl
    message = "Сколько файл %s можно" % fayl_total
    print(message)
