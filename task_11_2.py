class Car:
    __mark = None
    __model = None
    __year_of_manufacture = None
    __speed = 0

    def __init__(self, mark, model, year_of_manufacture, speed):
        self.__mark = mark
        self.__model = model
        self.__year_of_manufacture = year_of_manufacture
        self.__speed = speed

    def __str__(self):
        return f'Mark: {self.__mark}, model: {self.__model}, year of manufacture: {self.__year_of_manufacture} '

    @property
    def speed_increase(self):
        self.__speed += 5

    @property
    def speed_reduction(self):
        self.__speed -= 5

    @property
    def stop(self):
        self.__speed = 0

    @property
    def u_turn(self):
        self.__speed = -self.__speed

    @property
    def get_speed(self):
        return f'Speed: {self.__speed}'


car = Car('BMW', '3', 2014, 50)
print(car.get_speed)
car.u_turn
print(car.get_speed)
car.stop
print(car.get_speed)
print(car)
car.speed_increase
car.speed_increase
car.speed_increase
print(car.get_speed)