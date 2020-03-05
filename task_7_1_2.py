def inch_to_cm(x):
    return 2.54 * x


def cm_to_inch(x):
    return x / 2.54


def mil_to_km(x):
    return 1.609 * x


def km_to_mil(x):
    return x / 1.609


def pounds_to_kg(x):
    return x / 2.205


def kg_to_pounds(x):
    return x * 2.205


def ounces_to_grams(x):
    return x * 28.35


def grams_to_ounces(x):
    return x / 28.35


def gallons_to_liters(x):
    return x * 3.785


def liters_to_gallons(x):
    return x / 3.785


def pints_to_liters(x):
    return x / 2.113


def liters_to_pints(x):
    return x * 2.113


list_of_numbers = range(0, 13)
while True:
    number = int(input('Enter your choice:\n1)Inches to centimeters 2)Centimeters to Inches 3)Miles to Kilometers'
                       '4)Kilometers to Miles 5)Pounds to kilograms 6)Kilograms to Pounds\n7)Ounces to grams 8)Grams to'
                       'ounce 9)Gallon to liters 10)Liters to Gallons 11)Pints to liters 12)Liters to pints 0)Exit\n'))

    while number not in list_of_numbers:
        number = int(input())
    value = float(input('Enter value: '))
    if number == 1:
        print(f'{inch_to_cm(value)} cm')
    elif number == 2:
        print(f'{cm_to_inch(value)} inches')
    elif number == 3:
        print(f'{mil_to_km(value)} kilometres')
    elif number == 4:
        print(f'{km_to_mil(value)} miles')
    elif number == 5:
        print(f'{pounds_to_kg(value)} kilograms')
    elif number == 6:
        print(f'{kg_to_pounds(value)} pounds')
    elif number == 7:
        print(f'{ounces_to_grams(value)} grams')
    elif number == 8:
        print(f'{grams_to_ounces(value)} ounces')
    elif number == 9:
        print(f'{gallons_to_liters(value)} liters')
    elif number == 10:
        print(f'{liters_to_gallons(value)} gallons')
    elif number == 11:
        print(f'{liters_to_pints(value)} pints')
    elif number == 12:
        print(f'{pints_to_liters(value)} liters')
    else:
        print('Exit...')
        break