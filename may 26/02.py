user_km = input("Расстояние")
user_time = input ("Время")

try:
    km = int (user_km)
    hours = int(user_time)
    
except ValueError:
    message = "Вы ввели не числа" 
else:
    speeds = km / hours    
    message = "Ваше скорость %s должно быть" % speeds
    print(message)