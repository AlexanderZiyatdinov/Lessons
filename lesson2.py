"""Вспоминаем строки"""
s = "abracadabra"
print(s[0])

"""Условные операторы и ветвления"""
"""Инструкция, которая символизирует, что программе нужно перейти в другое место
исполнения
Блок if выполняется, если условие после if равно True"""

# if (5 > 3) or (2 > 1):
#     print("This is true block")
#
# """Сначала выполняется end, потом or"""
#
# s2 = "abra"
#
# if s2 in s:
#     print('true')
#
# time = -3

# if (time > 1):
#     print('+')
#
# elif (time > 0 and time <= 1): # else if = elif
#     print('*')
#
# else:
#     print('time <= 0')

# B и T

"""Циклы For и While
i, j, k - индексные переменные, они нужны для ИТЕРИРОВАНИЯ
for и while - одно и то же, по сути. Но For - это синтаксический сахар"""

# sum = 0
# for i in range(1, 11):
#     sum += i
#
# print(sum)
#
#
# sum2 = 0
# # i = 0
# # while i < 11:
# #     sum2 += i
# #     i += 1
# # print(sum2)
#
#
# for symbol in s:
#     print(symbol)

with open("test.txt", 'r+') as f:
    text = f.read()
    f.write("WOW!")
    print(text)

#Задачки B, C, D, E, F, G - для условий
# K - для for, A, B* - для while

