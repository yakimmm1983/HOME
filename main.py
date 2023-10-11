"hello"

def calculate(sign,num1,num2):

    if sign == "+":
        print(num1+num2)
    elif sign == "-":
        print(num1-num2)
    else:
        print("нет такой операции")
while True:
    string = input("введите 0 для выхода\nвведите строку с математическим выражением\nкалькулятор поддерживает только операции - и +\n>>>")
    if string.find("+") !=-1:
        sign = string[string.find("+")]
        num1 = int(string[:string.find("+")])
        num2 = int(string[string.find("+")+1:])
        calculate(sign,num1,num2)
    elif string.find("-") !=-1:
        sign = string[string.find("-")]
        num1 = int(string[:string.find("-")])
        num2 = int(string[string.find("-")+1:])
        calculate(sign,num1,num2)
    elif string.strip() =="0":
        break
    else:
        print("нет такой операции")



import math
def choise():
    while True:
        raschet = input("Как вы хотите посчитать площадь сектора: 1-по длинне дуги или 2-по количеству секторов \nДля выхода нажмите 0\n>>>")
        if raschet == "1":
            print(areaSector1(raschet))
        elif raschet == "2":
            print(areaSector2(raschet))
        elif raschet == "0":
            print("Благодарим за пользование нашей программой!")
            break
        else:
            print("Введите цифру 1 или 2")
def areaSector1(raschet):
    radius = int(input("Введите радиус:  "))
    sector = int(input("Введите длинну дуги:  "))
    drob = 0.5
    result = drob*(radius*sector)
    print(f"Площадь сектора по длинне дуги составит: {result}")
def areaSector2(raschet):
    sektor = int(input("Введите колличество секторов:  "))
    circle = int(input("Введите радиус круга:  "))
    result = math.pi*circle**2/sektor
    print(f"Площадь сектора по их колличеству составит: {result}")
choise()

def sum_range(start, end):

    if start > end:
        start, end = end, start
    s = 0
    for i in range(start, end + 1):
        s += i
    return s
a, b = map(int, input().split())   #ЭТА СТРОЧКА НЕ ПОНЯТНА
print(sum_range(a, b))


persent = 35800 * 20 / 100
print(f"Цена телефона после подорожания составит: {35800+persent} рублей")
