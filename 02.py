input("Введите строку:")
user_in = input("Сколько раз плвторить")
repeats = int(user_in)

result = string * repeats
templates = "Результат : %s"
message = templates % result
print(message)
