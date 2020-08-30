"""1.Типы данных"""

"""Основные типы данных в Python:
Int - целочисленный тип
Float - тип чисел с плавающей точкой
Str - строка или же набор символов
Bool - логический тип данных"""
a = 4  # int
b = 5.0  # float
s = "abracadabra"  # str
t = True  # bool
f = False  # bool

"""2.Функции print и type"""

"""Функция print используется для того, чтобы вывести какую-либо
информацию на экран, чтобы осуществить отладочную печать и т.п.

Print принимает следующие аргументы:
*values – объект, который нужно вывести * обозначает, что объектов может быть несколько;
sep – разделяет объекты. Значение по умолчанию: ‘ ‘;
end – ставится после всех объектов;
file – ожидается объект с методом write (string). Если значение не задано, для вывода объектов используется файл sys.stdout;
flush – если задано значение True, поток принудительно сбрасывается в файл. Значение по умолчанию: False."""

s1 = "Некоторый текст"
s2 = "Еще текст"
s3 = s1 + s2  # операция конкатенации "abc" + "def" = "abcdef"
print(s3)  # >> Некоторый текстЕще текст

"""При программировании в Python пользуемся правилом:
                    Всё есть объект!"""

"""Функция type() возвращает тип класса аргумента (объекта),
 переданного в качестве параметра. 
 Функция type () в основном используется для целей отладки."""

print(type(True))  # >> <class 'bool'>
print(type(5))  # >> <class 'int'>

"""Арифметические операции"""
num1 = 5
num2 = 4

print(num1 + num2)  # Сложение >> 9
print(num1 - num2)  # Вычитание >> 1
print(num1 * num2)  # Умножение >> 20
print(num1 / num2)  # Деление; возвращает тип float!!! >> 1.25
print(num1 % num2)  # остаток при делении a на b >> 1
print(num1 // num2)  # целочисленное деление >> 1
print(num1 ** num2)  # возведение в степень >> 625

"""Ввод с клавиатуры:
a = input() - считываем строку
a = int(input()) - считываем число (Int)"""

"""ВАЖНАЯ ЗАДАЧА!"""
# a = int(input())  # считываем число
print(type(a))

# 1 Обмен значениями двух переменных
# Есть два числа A и B. Необходимо поменять их значения местами.
# Пример входных данных: 5 7
# Пример выходных данных: 7 5

# Решение:

a = 5
b = 7
tmp = a
a = b
b = tmp

"""Строки.Индексация строк"""
"""Методы работы со строками: длина, срезы и т.д."""

name = 'Ivan'  # Пример строки
first_symbol = name[0]  # Индекс
last_symbol = name[-2]  # Индекс, если мы считаем с конца
print(name[1:])  # Срез >> van
print(last_symbol)  # >> a
length = len(name)  # Длина строки
print(name.upper())  # >> IVAN

print(ord('a'))  # Преобразование символа в код >> 97
print(chr(98))  # Преобразование кода в символ >> b