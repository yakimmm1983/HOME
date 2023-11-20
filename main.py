"hello"
#
# def calculate(sign,num1,num2):
#
#     if sign == "+":
#         print(num1+num2)
#     elif sign == "-":
#         print(num1-num2)
#     else:
#         print("нет такой операции")
# while True:
#     string = input("введите 0 для выхода\nвведите строку с математическим выражением\nкалькулятор поддерживает только операции - и +\n>>>")
#     if string.find("+") !=-1:
#         sign = string[string.find("+")]
#         num1 = int(string[:string.find("+")])
#         num2 = int(string[string.find("+")+1:])
#         calculate(sign,num1,num2)
#     elif string.find("-") !=-1:
#         sign = string[string.find("-")]
#         num1 = int(string[:string.find("-")])
#         num2 = int(string[string.find("-")+1:])
#         calculate(sign,num1,num2)
#     elif string.strip() =="0":
#         break
#     else:
#         print("нет такой операции")



# import math
# def choise():
#     while True:
#         raschet = input("Как вы хотите посчитать площадь сектора: 1-по длинне дуги или 2-по количеству секторов \nДля выхода нажмите 0\n>>>")
#         if raschet == "1":
#             print(areaSector1(raschet))
#         elif raschet == "2":
#             print(areaSector2(raschet))
#         elif raschet == "0":
#             print("Благодарим за пользование нашей программой!")
#             break
#         else:
#             print("Введите цифру 1 или 2")
# def areaSector1(raschet):
#     radius = int(input("Введите радиус:  "))
#     sector = int(input("Введите длинну дуги:  "))
#     drob = 0.5
#     result = drob*(radius*sector)
#     print(f"Площадь сектора по длинне дуги составит: {result}")
# def areaSector2(raschet):
#     sektor = int(input("Введите колличество секторов:  "))
#     circle = int(input("Введите радиус круга:  "))
#     result = math.pi*circle**2/sektor
#     print(f"Площадь сектора по их колличеству составит: {result}")
# choise()
#
# def sum_range(start, end):
#
#     if start > end:
#         start, end = end, start
#     s = 0
#     for i in range(start, end + 1):
#         s += i
#     return s
# a, b = map(int, input().split())   #ЭТА СТРОЧКА НЕ ПОНЯТНА
# print(sum_range(a, b))
#
#
# persent = 35800 * 20 / 100
# print(f"Цена телефона после подорожания составит: {35800+persent} рублей")

#     if start > end:
#         start, end = end, start
#     s = 0
#     for i in range(start, end + 1):
#         s += i
#     return s
# a, b = map(int, input().split())   #ЭТА СТРОЧКА НЕ ПОНЯТНА
# print(sum_range(a, b))



nums = [2, 11, 6, 8, 10]
target=6
def mySort(nums):
    for i in range(1, len(nums)):
        while (i > 0 and nums[i] < nums[i-1]):
            nums[i], nums[i-1] = nums[i-1], nums[i]
            i -= 1
    return nums

print(mySort(nums))

def LinearSearch(nums, target):
    for i in range (len(nums)):
        if nums[i] == 6:
            return i
    return -1
print( LinearSearch(nums, 6))

numbers = [25, 13, 6, 19, 27, 31]
target = 15

def mySort(numbers):
    for i in range(0, len(numbers)):
        for n in range(i+1, len(numbers)):
            if (numbers[n] < numbers[i]):
                numbers[n], numbers[i] = numbers[i], numbers[n]
    return numbers
print(mySort(numbers))

def binary_search(numbers, target):
    l = 0
    r = len(numbers) - 1
    while l<=r:
        m = (l+r)//2
        element = numbers[m]
        if element == target:
            return m
        elif element < target:
            return l == m+1
        else:
            r = l-1
        return -1
print (binary_search(numbers, 15))

array = [11, 28, 4, 20, 9, 15]
target = 20

def mySort(array):
    left = 1
    right = len(array)
    while left<right:
        for i in range(left, right):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
            if array[right-i] < array[right-i-1]:
                array[right-i], array[right-i-1] = array[right-i-1], array[right-i]
        left += 1; right -= 1
    return array

print(mySort(array))

def ternary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        h = (right - left) // 3
        m1 = left + h
        m2 = right - h
        if array[m1] == target:
            return m1
        elif array[m2] == target:
            return m2
        elif array[m1] < target < array[m2]:
            left = m1+1
            right = m2-1
        elif target < array[m1]:
            right = m1-1
        else:
            l = m2+1
    return None
print (ternary_search(array, target))




