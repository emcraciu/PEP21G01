# slice
string1 = 'My string'
result = string1[0]
print(result)

result = string1[0:4]
print(result)

result = string1[4:]
print(result)

result = string1[4:8]
print(result)

#  T E X T
#  0 1 2 3
# -4-3-2-1

result = string1[4:-1]
print(result)

result = string1[-5:-1]
print(result)

result = string1[0:8:2]
print(result)

encode = 'My test to encode'

result = encode[::-1]
print('Reverse:', result)
result = result[::-1]
print('Original:', result)

result = encode[5:] + encode[0:5]
print(result)
result = result[-5:] + result[:-5]
print(result)

print()
print(encode[-1:-10:-1])

# chr and ord functions
print(chr(33))
print(ord('!'))

print('Order number is used:', 'abc' > 'abd')

# ex: simple encoding change
encode = 'abc'
print(ord('a'))
print(ord('b'))
print(ord('c'))

result = chr(ord(encode[0]) + 1) + \
         chr(ord(encode[1]) + 1) + \
         chr(ord(encode[2]) + 1)
print(result)

# order number versus cast to integer
print(ord('1'))
print(int('1'))
print(type(int('112')))
# print(int('a')) # characters that care not numbers cannot be cast


# ex: time difference
start_time = '22:30'
end_time = '30:10'
# result is end_time - start_time in seconds

start_time_m = int(start_time[0:2])
start_time_s = int(start_time[3:])
start_time_conv = 60 * start_time_m + start_time_s
end_time_m = int(end_time[0:2])
end_time_s = int(end_time[3:])
end_time_conv = 60 * end_time_m + end_time_s
diff = end_time_conv - start_time_conv
print(diff)

# input function
my_input = input('Enter text here:')
print('You typed: ', my_input)
my_input = float(input('Enter your float number:'))
print('You typed: ', my_input)
my_input = complex(input('Enter your complex number:'))
print('You typed: ', my_input)

# None object
print_result = print('this is an example')
print('Result is:', print_result)
print(type(print_result))
print(None)

# boolean objects
print(True)
print(False)

# these objects have the same ID at any point of script run
print(id(None), id(True), id(False))

# comparison operations
var_1 = float(input("Primul numar: "))
var_2 = float(input("Al doilea numar: "))
print("Primul numar este mai mic:", var_1 < var_2)
print("Primul numar este mai mare", var_1 > var_2)
print("egalitate:", var_1 == var_2)
print("diferenta:", var_1 != var_2)

# comparison for ints and strings
print('Grater of equal 1 >= 0: ', (1).__ge__(0))
print('abc less then abd: ', 'abc'.__lt__('abd'))

# comparison methods
text1 = input('text1:')
text2 = input('text2:')
print(f'{text1} > {text2}:', text1.__gt__(text2))
print(f'{text1} < {text2}:', text1.__lt__(text2))
print(f'{text1} >= {text2}:', text1.__ge__(text2))
print(f'{text1} <= {text2}:', text1.__le__(text2))
print(f'{text1} == {text2}:', text1.__eq__(text2))
print(f'{text1} != {text2}:', text1.__ne__(text2))

# compare equality and identity
var1 = '/abc/\n9'
var2 = '/' + 'a' + 'b' + 'c' + '/\n' + str('9')
print(f'var1 = {var1}, var2={var2}')
print('==', var1 == var2)
print('IS', var1 is var2)
print(id(var1), id(var2))

print('123'.center(8, '_'))
