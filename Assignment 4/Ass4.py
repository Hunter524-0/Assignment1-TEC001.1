#Task 1
def course_codes(a):
    if len(a) != 6:
        return False
    if not a[:3].isupper():
        return False
    if not a[3:].isdigit():
        return False
    return True

a = input("Enter course code: ")
if course_codes(a):
    print("Valid")
else:
    print("Invalid")

#Task 2
def hex_codes(b):
    if len(b) != 7:
        return False
    if b[0] != '#':
        return False
    for char in b[1:]:
        if not (char.isdigit() or char.upper() in 'ABCDEF'):
            return False
        return True

b = input("Enter hex code: ")
if hex_codes(b):
    print("Valid")
else:
    print("Invalid")

#Task 3
def sum_nums(text):
    total = 0
    number = ''
    for num in text:
        if num.isdigit():
            number += num
        else:
            if number != '':
                total += int(number)
                number = ''
    if number != '':
        total += int(number)
    return total
paragraph = input("Enter paragraph: ")
print('The sum of all numbers is:', sum_nums(paragraph))

#Task 4
def phone_num(phone):
    phones = phone.split()
    result = []
    for i in phones:
        if i.isdigit() and len(i) == 10:
            result.append('[REDACTED]')
        elif i.startswith('+84') and i[3:].isdigit():
            result.append('[REDACTED]')
        else:
            result.append(i)
    return ' '.join(result)
doc = input("Enter a document: ")
print(phone_num(doc))