"""
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
в этой четверти (x и y).

Ввод: значение типа <int>
Вывод: значение типа <str>

Пример:

3
x < 0, y < 0
"""
print("Введите номер четверти от 1 до 4")
num = int(input())
if num >= 1 and num <= 4:
    if num == 1:
        print(' x > 0 and y > 0')
    if num == 2:
        print(' x < 0 and y > 0')
    if num == 3:
        print('x < 0 and y < 0')
    if num == 4:
        print('x > 0 and y < 0')
else:
    print("Введите корректное значение номера четверти")