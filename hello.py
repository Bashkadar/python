"""
1. Поработайте с переменными, создайте несколько, выведите на экран.
"""

a = 1
b = 'переменная b'
c = '123'
print(f"a: {a}\nb: {b}\nc: {c}")

"""
Запросите у пользователя некоторые числа и строки и сохраните в переменные,
затем выведите на экран.
"""

user_int = int(input("Введите целое число: "))
print("Целое число, введенное пользователем: ", user_int)

user_str = input("Введите текст: ")
print("Строка, введенное пользователем: ", user_str)

"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. 
Используйте форматирование строк.
"""

user_sec = int(input("Введите время в секундах: "))

hours = round(user_sec / 3600)
temp = user_sec - hours * 3600 #промежуточный расчет
minutes = round(temp / 60)
seconds = temp - minutes * 60
print(f"{hours}:{minutes}:{seconds}")

"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

ch = input("Введите число: ")
print("Результат: ", int(ch) + int(ch+ch) + int(ch+ch+ch))

"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
 Для решения используйте цикл while и арифметические операции.
"""

num = input("Введите целое положительное число: ")

i = 0
m = 0
while i < len(num):
    if int(num[i]) > m:
        m = int(num[i])
    i = i + 1

print("Максимальная цифра из введенного пользователем: ", m)

"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма.
Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
Выведите соответствующее сообщение.
"""

if float(input("Введите объем выручки фирмы: ")) > float(input("Введите объем издержки фирмы: ")):
    print("Фирма имеет прибыль")
else:
    print("Фирма терпит убыток")

"""
6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
Это отношение прибыли к выручке.
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
"""

income = float(input("Введите объем выручки фирмы: "))
cost = float(input("Введите объем издержки фирмы: "))

if income > cost:
    print(f"Фирма имеет прибыль, рентабельность выручки равна {round(((income - cost) / income) * 100)}%.")
    emp = int(input("Введите количество сотрудников фирмы: "))
    print(f"Прибыль в расчёте на одного сотрудника равна {round((income - cost) / emp)}")
elif income < cost:
    print("Фирма терпит убыток")
else:
    print("Фирма находится в точке безубыточности")

"""
 7. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
"""

a = int(input("Введите a: "))
b = int(input("Введите b: "))
day = 1
result = 0
while day > 0:
    print(f"{day}-й день: {a}")
    a = round(a + a * 10 / 100, 2)
    day = day+1
    if a >= b:
        print(f"{day}-й день: {a}")
        print(f"На {day}-й день спортсмен достиг результата - не менее {b} км.")
        break