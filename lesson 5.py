import random

# s = 'abcd' #итерируемый объект
#
# for i in range(0, len(s)):
#     print(s[i])
#
#
# index = 0
# while index < len(s):
#     print(s[index])
#     index += 1
#
#
# for symbol in s:
#     print(symbol)


m = []

for i in range(0, 10):  # инициализация массива
    m.append(i)

# print(m)

sum = 0
for i in range(0, 10, 2):  # поиск суммы элементов на четных позициях
    sum += m[i]

# print(sum)

m = [3, 12, 16, 17, 2, 5, 18, 1]

max = -1

for i in range(0, len(m)):
    if m[i] > max:
        max = m[i]

m = [[1, 2, 3], [2, 4, 6]]  # двойный массивы (массивы массивов)

my_tuple = (1, 2, 3, 4, 5, 6)  # tuple (кортеж)

dictionary = {True: 'This is true', False: 0}

# MUST HAVE - BUBBLE SORT (СОРТИРОВКА ПУЗЫРЬКОМ)


def bubble_sort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

def create_array():
    array = []
    for i in range(0, 10):
        array.append(random.randint(1, 100))
    return array




m = create_array()

print(m)
bubble_sort(m)
print(m)

n = create_array()

print(n)
bubble_sort(n)
print(n)



