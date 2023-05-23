user_input = input("Сколько сейчас часов?")
hours = int(user_input)

user_input = input("Сколько сейчас минут?")
minutes = int(user_input)

hours_remain = 23 - hours 
munites_remain = 60 - minutes

print ("Осталось",hours_remain,"ч",munites_remain,"мин")