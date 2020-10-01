class Quadrate:

    def __init__(self, side: int):
        self.side = side

    def get_perimeter(self):
        return 4 * self.side

    def get_square(self):
        return self.side * self.side


class Car:
    def __init__(self, name, year, color):
        self.name = name
        self.year = year
        self.color = color


def main():
    my_car = Car("Лада", 1990, "Красный")
    car_of_my_friend = Car("BMWx6", 2019, "Белый")

    print(my_car.color)
    print(car_of_my_friend.year)


if __name__ == "__main__":
    main()
