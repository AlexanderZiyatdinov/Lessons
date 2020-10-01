# s = "abracadabra"
# m = [1, 2, 3, 4, 5]
# d = {1: "a", 2: "b", 3: "c"}
# t = ([1, 3, 5], [20, 27, 26], [31, 123, 1])
#
# # Используем ЦИКЛЫ
# # for и while (по сути это одно и то же)
#
# for index in range(0, 10):
#     print(index)
#
# for index in range(0, 10):
#     print("Привет, мир!")
#
#
# # Печатаем после цикла
# sum = 0
# for i in range(1,11):
#     sum += i
# print(sum)
#
# sum = 0
# while sum < 40:
#     print("Сумма меньше 40")
#     sum += 10
#
#
# # Индекс ВШИТ в for. For - это просто удобная запись While
# prod = 1
# for index in range(1, 8):
#     prod *= index
# print(prod)
#
# prod = 1
# index = 1
# while index <= 7:
#     prod *= index
#     index += 1
# print(prod)
#
# # Foreach - как аналог в других языках Программирования
# for char in s:
#     print(char)
#
#
# # Команда break - выходит из цикла СРАЗУ ЖЕ
# # Команда continue - переходит к следующей итерации
#
# while True:
#     user_input = input()
#     if user_input.lower() == "привет":
#         print("Привет, я вечный цикл!")
#     elif user_input.lower() == "пока":
#         print("Пока, заканчиваю работу")
#         break
#     else:
#         print("Не знаю такую команду")

# DRY - Don't repeat yourself


def my_sum(x: int, y: int):
    return x + y


def print_message(message):
    print(message)


def max(a, b):
    if a >= b:
        return a
    return b


print(max(True, False))
