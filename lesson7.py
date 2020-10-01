def main():
    print(sum(5, 3)) # Печатаем 8
    print(change_values(5, 6)) # Печатаем 6 5
    print(find_min([3, 1, 2])) # Печатаем 1


def sum(num1, num2):
    return num1 + num2


def change_values(var1, var2):
    tmp = var1
    var1 = var2
    var2 = tmp
    return var1, var2


def find_min(array):
    min = 10000

    for i in range(0, len(array)):
        if array[i] < min:
            min = array[i]
    return min


if __name__ == "__main__":
    main()
