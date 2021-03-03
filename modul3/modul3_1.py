# Recap if statement
n = int(input("Input number: "))
if n < 10:
    print("to small")
elif n > 1:
    print("to big")
else:
    print("just right")

# check if a string can be converted to int (just first letter)
data = input('Enter value:')
if 47 < ord(data[0]):
    if ord(data[0]) <= 57:
        result = int(data)

# check if a string can be converted to int (enhanced)
data = input('Enter value:')
for value in range(len(data)):
    if 48 > ord(data[value]) > 57:
        print(data, f' is {type(data)}')
        break
else:
    result = int(data)
    print(result, f' is {type(result)}')

# True-ish and False-ish
print('values != 0 are True', bool(1 + 0j))
print('values == 0 are False', bool(0))
print('objects with length > 0 are True', bool('string'))
print('objects with length = 0 are False', bool(''))
print('None and False are False', bool(None))
print('True and functions are True', bool(print))

print()
if print:
    print('Functions are True')
if 'string':
    print('Strings that are not empty are True')

# for loops
for value in range(1, 10, 2):
    print(value)
    if value == 2:  # try 2
        break
    print('this will never be printed')
else:
    print('This is in else:', value)

print('This is outside for loop:', value)

# We can iterate a string
print()
for letter in 'my_text':
    print('Letter is: ', letter)

# We cannot use objects that are not iterable in for loops
# for number in 123:
#     print('Number is: ', number)

# Iterable objects
str_iter = 'my_text'.__iter__()
# int_iter = (123).__iter__() # not iterable

print(type(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
# print(next(str_iter)) # StopIteration

# ex: is a number prime
input_number = int(input('Number to check if prime: '))
for number in range(2, input_number):
    if input_number % number == 0:
        print(f'{input_number} is not prime')
        break
else:
    print(f'{input_number} is prime')

# ex: print all primes in a range:
max_prime = int(input("Max prime number: "))
print('Primes are: ', end='')
for number in range(1, max_prime + 1):
    if number < 3:
        print(number, end=', ')
        continue
    for divider in range(2, number):
        if number % divider == 0:
            break
    else:
        print(number, end=', ')
print()

# ex: encode test with given number
encode_data = input('String to encode:')
encode_key = int(input('Encode key:'))
for letter in encode_data:
    letter_ord = ord(letter) + encode_key
    print(chr(letter_ord), end='')
print()

# And operation can be used for any object
a = 'a'
b = 'b'
print('Result:', a and b)
if a:
    print('Result:', b)
else:
    print('Result:', a)

# Or operation can be used for any object
a = 0
b = 1
print('Result:', a or b)
if a:
    print('Result:', a)
else:
    print('Result:', b)

# Discussed pyramid problem
blocks = int(input("Enter the number of blocks: "))

blocks_required = 1
height = 0
while blocks > blocks_required:
    height += 1
    blocks -= blocks_required
    blocks_required += 1

print("The height of the pyramid:", height)
