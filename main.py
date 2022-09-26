
"""
name = input("Введите ваше имя: ")
print("Привет, " + name + "!")
print(10 ** 3)

a = 5
b = 6
c = a + b
print(c)

num1 = input("Введите ваше первое число: ")
num1 = int(num1)
num2 = input("Введите ваше второе число: ")
num2 = int(num2)
print(num1 + num2)

    # Типы_данных
float_var = 3.14
print(bool(float_var))

hour = 19
if hour < 12:
    print("Доброе утро!")
elif hour < 18:
    print("Добрый вечер!")
else:
    print("Спокойной ночи!")


quit_flag = True
match quit_flag:
    case True:
        print("Quitting")
        exit()
    case False:
        print("System is on")
"""

month = int(input("Type the months number: "))
match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("Jule")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("Octomber")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("That number doesn't exist")


from datetime import datetime
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

