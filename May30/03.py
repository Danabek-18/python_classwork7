user_in = input("Введите стоимость покупки")

cost = float(user_in)
if cost<1000:
    print("Скидки нет")
elif cost<2000:
    print("Скидка 2%")
elif cost<5000:
    print("Скидка 5%") 
else:
    print("Скидка 10%") 
print("Конец")              