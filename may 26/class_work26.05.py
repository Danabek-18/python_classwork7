#ДЗ за 19.05.23 калькулятор
user_in1 = input("введите первое число?")
user_in2 = input("введите второе число?")
template = """
Сумма чиссел:    %.2f
Разность чисел:  %.2f
Произведение чисел: %.2f
Частное чисел:   %.2f 
 """
try:
   num1 = float(user_in1)
   num2 = float(user_in2)
  
except ValueError as my_error:
   print(my_error)
   message = "Вы ввели неправильные данные"
except NameError:
   message="Нет такой переменной"   

else:
    sum = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    message = template % (sum, sub, mul, div)

print(message)
