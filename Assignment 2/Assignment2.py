#Task 1
def zander():
    centimeter = float(input('Enter the zander centimeter: '))
    if centimeter < 42:
        print(f'Your fish has escaped, your zander need to be {42 - centimeter} centimeters longer to catch the fish')
    else:
        print('You successfully catch the fish')
zander()

#Task 2
def cabin():
    cc = input('Enter the cabin class: ')
    if cc == 'LUX':
        print('Upper-deck cabin with a balcony.')
    elif cc == 'A':
        print('Above the car deck, equipped with a window.')
    elif cc == 'B':
        print('Windowless cabin above the car deck.')
    elif cc == 'C':
        print('Windowless cabin below the car deck.')
    else:
        print('Invalid cabin class')
cabin()

#Task 3
def health():
    gender = input('Enter your gender: ')
    hemoglobin = int(input('Enter your hemoglobin: '))
    if gender == 'Male':
        if 134 <= hemoglobin <= 167:
            print('Your hemoglobin is normal')
        elif hemoglobin > 167:
            print('Your hemoglobin is high')
        elif hemoglobin < 134:
            print('Your hemoglobin is low')
    elif gender == 'Female':
        if 117 <= hemoglobin <= 155:
            print('Your hemoglobin is normal')
        elif hemoglobin > 155:
            print('Your hemoglobin is high')
        elif hemoglobin < 117:
            print('Your hemoglobin is low')
    else:
        print('Invalid gender')
health()

#Task 4
def leap():
    year = int(input('Enter a year: '))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('This year is a leap year')
    else:
        print('This year is not a leap year')
leap()

#Task 5
import math

def formula(diameter, price):
    radius = diameter / 2 / 100
    area = math.pi * (radius ** 2)
    return price / area
def pizza():
    d1 = float(input('Enter the 1st pizza diameter: '))
    p1 = float(input('Enter the price: '))
    d2 = float(input('Enter the 2nd pizza diameter: '))
    p2 = float(input('Enter the price: '))
    pizza1 = formula(d1, p1)
    pizza2 = formula(d2, p2)
    if pizza1 < pizza2:
        print('The 1st pizza provide better value for money')
    else:
        print('The 2nd pizza provide better value for money')
pizza()