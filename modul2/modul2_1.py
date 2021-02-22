# variables

number_3 = '3'
print(number_3)
number_three = 3
print(number_three)

# type
response = type(number_3)
print(response)

response = type(number_three)
print(response)

# print(type(3))
# print(type('3'))

# Integers
var1 = 123
result = type(var1)
print('This is an integer:', result)

# Integer base
bin_number = 0b10
print(bin_number)

oct_number = 0o10
print(oct_number)

hex_number = 0x10
print(hex_number)

# Integer Operations
print('Sum of 2+8 is:', bin_number + oct_number)

# add method
print('Sum of 2+8 is:', bin_number.__add__(oct_number))
# print('Sum of 2+8 is:', oct_number.__add__(bin_number))

print('Dif of 8-2 is: ', oct_number - bin_number)
print('Dif of 8-2 is: ', oct_number.__sub__(bin_number))

# mul method
print('multiplication 2 * 8:', bin_number * oct_number)
print('multiplication 2 * 8:', bin_number.__mul__(oct_number))

# ex: 3*3*3
print("Multiplication 3 * 3 * 3:", 3 * 3 * 3)
print("Multiplication 3 * 3 * 3:", (3).__mul__(3).__mul__(3))
print("Multiplication 3 * 3 * 3:", number_three.__mul__(number_three.__mul__(number_three)))

# raise to power
print('Power of:')
number_3 = 3
print(number_3 ** 3)
print(number_3.__pow__(3))
print(pow(number_3, 3))

# division
print('Division')
result = number_3 / 3
print(type(result))
print(result)
print('True div: ', number_3.__truediv__(3))

# ex:
a = 3
b = 4
c = 5
# ex using signs
x = (-b - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
print(x)
print(type(x))

# ex using methods
_4ac = (4).__mul__(a.__mul__(c))
b_sqr = b.__pow__(2)
sqr_result = b_sqr.__sub__(_4ac)
sqrt_result = pow(sqr_result, (1).__truediv__(2))
minus_b = (0).__sub__(b)
# div_up = minus_b.__add__(sqrt_result)
div_up = sqrt_result.__add__(minus_b)
div_down = (2).__mul__(a)
result = div_up.__truediv__(div_down)
print(result)

# Strings:

string1 = 'My String1\nThis is a new line'
print(string1)
string2 = "My String2"
print(string2)
string3 = '''My String3
This is a new line
This is another new line'''
print(string3)

print(type(string1), type(string2), type(string3))

# methods
print(string1 + string2)
print(string1.__add__(string2))

# ex:
# Write: This is my code 100 times on a new line
my_code = 'This is my code\n'
print(my_code * 100)
print(100 * my_code)
print(my_code.__mul__(100))
print((100).__mul__(my_code))  # this is not implemented so it will do my_code.__mul__(100)
print()

# String Types:
formatted_string = f'Start: {string1} End: {string2}'
print(formatted_string)

# ex: Declaratie
# Subsemnatul: Nume Prenume
# Declar: ...
name = 'Craciun'
forename = 'Emanuel'
declaration = '...'
result = f'Subsemnatul: {name} {forename}\nDeclar: {declaration}'
print(result)

print()
raw_string = r'1\nThere is no new line\n2'
print('Raw string:', raw_string)

# String methods
string1 = 'My String: {}'
result = string1.format('String Name')
print('Format method:', result)

# ex: Declaratie
# Subsemnatul: Nume Prenume
# Declar: ...
ful_name = 'Emanuel Craciun'
first_line = 'Subsemnatul: {}\n'
second_line = 'Declar: {}'
result = first_line.format(ful_name) + second_line.format(declaration)
print('\nString format method:\n', result, sep='')

print('\nUsing replace method:')
result = string1.replace('{', '(')
result = result.replace('}', ')')
print(result)
