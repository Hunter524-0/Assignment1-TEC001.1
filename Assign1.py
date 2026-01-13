#Task 2
from operator import length_hint

a=input('Nhap ten cua ban: ')
print(f'Hello, {a}!')

#Task 3
import math
radius=float(input('Nhap ban kinh hinh tron: '))
circumference=radius*2*math.pi
print(f'Chu vi hinh tron: {circumference:.2f}')

#Task 4
length=float(input('Chieu dai: '))
width=float(input('Chieu rong: '))
perimeter=(length+width)*2
area=length*width
print(f'Perimeter: {perimeter:.2f}')
print(f'Area: {area:.2f}')

#Task 5
x=int(input('So thu nhat: '))
y=int(input('So thu hai: '))
z=int(input('So thu ba: '))
sum=x+y+z
product=x*y*z
average=sum/3
print(f'Sum: {sum:.2f}')
print(f'Product: {product:.2f}')
print(f'Average: {average:.2f}')

#Task 6
talent=float(input('Talents: '))
pound=float(input('Pounds: '))
lot=float(input('Lots: '))
talent_to_gram=talent*20*32*13.3
pound_to_gram=pound*32*13.3
lot_to_gram=lot*13.3
total_gram=talent_to_gram + pound_to_gram + lot_to_gram
kilogram=int(total_gram/1000)
gram=float(total_gram-kilogram*1000)
print(f'Total weight: {kilogram} kilograms and {gram:.2f} grams.')

#Task 7
import random
b1=random.randint(0,9)
b2=random.randint(0,9)
b3=random.randint(0,9)
print(f'3-digit combination lock: {b1,b2,b3}')
c1=random.randint(1,6)
c2=random.randint(1,6)
c3=random.randint(1,6)
c4=random.randint(1,6)
print(f'4-digit combination lock: {c1,c2,c3,c4}')