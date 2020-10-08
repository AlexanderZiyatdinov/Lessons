def task1():
    """Вводится 4-х значное число. Программа должна вывести
    сумму первых двух разрядов и вторых двух разрядов
    Наример: Для числа 1423 надо вывести 14+23 = 37"""
    N = int(input())
    print(N % 100)
    print(N // 100)


def task2():
    """Пользователь вводит кол-во минут.
    Программа должна вывести целое кол-во часов, и остатки минут.
    Например, ввели 70. Программа выведет: 1ч. 10 мин."""
    time = int(input())
    h = time // 60
    m = time % 60
    print(h, "ч.", m, "мин.")


def task3():
    """Отрезок задан координатами своих краевых точек.
    Пользователь вводит поочередно х1, х2, у1, у2.
    Надо посчитать длину отрезка."""

    x1 = int(input("x1 "))
    x2 = int(input("x2 "))
    y1 = int(input("y1 "))
    y2 = int(input("y2 "))

    a = abs(x2 - x1)
    b = abs(y2 - y1)

    length = (a ** 2 + b ** 2) ** 0.5
    print(length)


def task4():
    """Сначала вводятся два произвольных числа a и b.
    Потом вводится знак "+", "*", "/" или "-".
    Взависимости от того, какой знак ввели, будем считать a+b или a-b """
    a = int(input())
    b = int(input())
    c = input()

    if c == "+":
        print(a + b)
    elif c == "*":
        print(a * b)
    elif c == "/" and b != 0:
        print(a / b)
    else:
        print(a - b)


def task5():
    """Вася хочет написать такую программу,
    которая могла бы распознать время года по номеру месяца.
    Помоги Васе это сделать
    Например: Вводится: 9, выводится: осень"""

    month = int(input())
    if month == 1 or month == 2 or month == 12:
        print("зима")
    elif month == 3 or month == 4 or month == 5:
        print("весна")
    elif month == 6 or month == 7 or month == 8:
        print("лето")
    elif month == 9 or month == 10 or month == 11:
        print("осень")


def task6():
    """Вася хочет написать такую программу,
    которая могла бы распознать время года по большим числам.
    Помоги Васе это сделать
    Например: Вводится: 57, выводится: осень
    т.к. это 4 года и 9 месяцев"""
    month = int(input()) % 12
    if month == 1 or month == 2 or month == 0:
        print("зима")
    elif month == 3 or month == 4 or month == 5:
        print("весна")
    elif month == 6 or month == 7 or month == 8:
        print("лето")
    elif month == 9 or month == 10 or month == 11:
        print("осень")


def task7():
    """Петя ходит в магазин со списком покупок из трех товаров,
     которые ему нужно купить.
     Далее он смотрит в каталог и ищет ему нужные товары.
     Выведите "Yes", если он может купить ВСЕ нужные ему товары" и "NO,иначе
     Например.
     Входные данные:
     хлеб
     молок
     PS4 Pro 512 GB
     зубная паста, стиральный порошок, яблоки, персики, молоко,
     йогурт, хлеб, вода, рыба, печенье
     Выходные данные:
     NO"""

    product1 = input()
    product2 = input()
    product3 = input()
    list = input()

    if product1 in list and product2 in list and product3 in list:
        print("YES")
    else:
        print("NO")


def task8():
    """Нужно найти в строке:
    "testing for loops testing for loops testing for loops testing for loops"
    количество букв "t" """

    string = "testing for loops testing for loops testing for loops testing for loops"
    count = 0

    for char in string:
        if char == "t":
            count += 1

    print(count)

    # for i in range(0, len(string)):
    #     if string[i] == "t":
    #         count += 1
    #
    # print(count)


def task9():
    """Дан список A = [13, 12, 16, 17, 22, 132, 11, 132, 109, 108].
    Требуется найти кол-во элементов кратных 3 и поделить все эти элементы
    на 3. В конце вывести кол-во таких элементов и измененный список А"""

    A = [13, 12, 16, 17, 22, 132, 11, 132, 109, 108]
    count = 0

    # for elem in A:
    #     if elem % 3 == 0:
    #         elem //= 3
    #         count += 1
    # print(count)
    # print(A)

    for i in range(len(A)):
        if A[i] % 3 == 0:
            A[i] //= 3
            count += 1
    print(count)
    print(A)


def task10():
    """Дан массив из N случайных целых неотрицатльных чисел, которые
    не превосходят 10000. Найти минимальный элемент в массиве.
    Вход: одно число N - кол-во элементов
    Выход: Минимальный элемент
    Например:
    3
    [3,0,1] - пусть сформировался такой массив
    0"""

    import random
    A = []
    N = int(input())

    for i in range(N):
        A.append(random.randint(1, 10000))

    print(A)

    min = 10000

    for i in range(N):
        if A[i] < min:
            min = A[i]

    print(min)


def task11():
    """Передается некоторая строка из английских букв.
    Известно, что ее длина меньше 50. Необходимо посчитать кол-во букв
    "o" или "O" и вывести это кол-во на экран.
    Подсказка можно воспользоваться функциями upper(), lower()"""

    string = input()
    count = 0

    for i in range(len(string)):
        if string[i] == "o" or string[i] == "O":
            count += 1
    print(count)


def task12():
    """Дан некоторый список, состоящий из 7 целых неотрицательных чисел,
    каждое из которых не превосходит 7. Необходимо напечатать элементы списка
    с конца к началу в одной строке через пробел.
    Например, для списка А=[1,2,3,4,5,6,7] надо вывести: 7 6 5 4 3 2 1
    Функция reverse() запрещена"""
    import random
    N = 7
    A = []
    for i in range(N):
        A.append(random.randint(1, 7))

    print(A)
    string = ""
    # N - 1 = 6 ВСЕГДА
    for i in range(N):
        string += str(A[N - 1 - i]) + ' '
    print(string)


def main():
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    # task7()
    # task8()
    # task9()
    # task10()
    # task11()
    task12()


if __name__ == "__main__":
    main()
