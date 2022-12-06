"""
Напишите программу, которая принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным.
Ввод: значение типа <int>
Вывод: единственное значение типа <bool> (True либо False)
Пример:
6
True
7
True
1
False
"""
"""
number = int(input("Введите число дня недели от 1 до 7: "))

if number < 1 or number > 7:
    print('Вы ввели неверное число!;)')
elif number > 5:
    print('Да, этот день выходной!')
else:
    print('Увы, но это рабочий день!')
    """
def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def checkNumber(num):
    if 6 <= num <= 7:
        print("True")
    elif 0 < num < 6:
        print("False")
    else:
        print("число вне пределов 7 дней")


num = InputNumbers("Введите число: ")
checkNumber(num)
