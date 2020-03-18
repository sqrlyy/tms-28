from time import sleep
from random import randint


class Dog:
    def __init__(self, name, age, breed):
        self.__name = name
        self.__age = age
        self.__breed = breed

    def __str__(self):
        return f'Name: {self.__name}, breed: {self.__breed}, age: {self.__age}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, new_breed):
        self.__breed = new_breed

    @property
    def bark(self):
        print('Woof-woof!')

    @property
    def eating(self):
        print('Start eating...')
        sleep(2)
        print('Finished')


class Pistol:
    def __init__(self, fire_rate, armour_penetration, bullets):
        self.__fire_rate = fire_rate
        self.__armour_penetration = armour_penetration
        self.__full_bullets = bullets
        self.__bullets = bullets

    @property
    def fire_rate(self):
        return self.__fire_rate()

    @fire_rate.setter
    def fire_rate(self, value):
        self.__fire_rate = value

    @property
    def armour_penetration(self):
        return self.__armour_penetration()

    @armour_penetration.setter
    def armour_penetration(self, value):
        self.__armour_penetration = value

    @property
    def bullets(self):
        return self.__bullets

    @bullets.setter
    def bullets(self, value):
        self.__bullets = value

    def reloads(self):
        self.__bullets = self.__full_bullets
        return 'Reloaded'

    def shooting(self):
        print('piu!')
        if self.__bullets == 0:
            print('Out of ammo!')
        else:
            self.__bullets -= 1

    def __str__(self):
        return f'Fire rate: {self.__fire_rate}, armour penetration: {self.__armour_penetration}, clip: {self.__full_bullets}'


class Human:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, new_gender):
        self.__gender = new_gender

    def work(self):
        print('Working...')

    def play_casino(self):
        win_number = randint(0, 100)
        if win_number > 50:
            return 'You are win!'
        else:
            return 'You are lose...'

    def __str__(self):
        return f'Name: {self.__name}, age: {self.__age}, gender: {self.__gender}'


class House:
    def __init__(self, street, floors, people):
        self.__street = street
        self.__floors = floors
        self.__people = people

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, new_street):
        self.__street = new_street

    @property
    def floors(self):
        return self.__floors

    @floors.setter
    def floors(self, new_floors):
        self.__floors = new_floors

    @property
    def people(self):
        return self.__people

    @people.setter
    def people(self, new_people):
        self.__people = new_people

    def add_floors(self, value):
        self.__floors += value

    def add_people(self, new_people):
        self.__people += new_people

    def __str__(self):
        return f'Street: {self.__street}, floors: {self.__floors}, people: {self.__people}'


class ElectricScooter:
    def __init__(self, model, color, max_speed):
        self.__model = model
        self.__color = color
        self.__max_speed = max_speed
        self.__engine = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        self.__color = new_color

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, new_max_speed):
        self.__max_speed = new_max_speed

    @property
    def on_engine(self):
        self.__engine = True

    @property
    def off_engine(self):
        self.__engine = False

    @property
    def ride(self):
        if self.__engine is True:
            print('You are riding!')
        else:
            print('You need to turn on the engine!')


dog = Dog('Tom', 3, 'Harrier')
print(dog.name)
dog.name = 'Fill'
print(dog.name)
print(dog.age)
dog.bark
dog.eating
print(dog)

pistol = Pistol(100, 30, 5)
pistol.shooting()
pistol.shooting()
pistol.shooting()
pistol.shooting()
print(pistol.bullets)
pistol.shooting()
pistol.shooting()
print(pistol.reloads())
print(pistol.bullets)

pavel = Human('Pavel', 27, 'm')
print(pavel.play_casino())
print(pavel)

samocat = ElectricScooter('Xiaomi', 'Gray', 35)
samocat.ride
samocat.on_engine
samocat.ride
