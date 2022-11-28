"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Результат округлить до сотых.

Ввод: четыре значения типа <int>
Вывод: значение типа <float>

Пример:

4 10
11 5
9.22
"""
print("Введите координаты первой точки")
x1 = int(input())
y1 = int(input())
print("Введите координаты второй точки")
x2 = int(input())
y2 = int(input())

distance =((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print("Расстояние между точками = ", round(distance,3)) # три знака после запятой