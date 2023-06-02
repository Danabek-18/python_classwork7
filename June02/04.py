user_in = input("Введите первое число")
user_in2 = input("Введите второе  число")
num1 = int(user_in)
num2 = int(user_in2)

def num(n1, n2):
    if n1>n2:
       return n2   
    else:
        return n1 
     

less_number = num(num1, num2)

print("Меньшее число:", less_number)    

