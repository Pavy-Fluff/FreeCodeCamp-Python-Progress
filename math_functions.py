# FreeCodeCamp - Python Basics
# In here, we will talk about mathematical operations for ints and floats.

# we will start with integers a.k.a. ints

my_int_1 = 74
my_int_2 = -7

print(type(my_int_1)) # <class 'int'>
print(type(my_int_2)) # <class 'int'>

# How to perform an addition with integers

my_int_1 = 12
my_int_2 = 78
my_int_sum = my_int_1 + my_int_2
print('the integer sum is:', my_int_sum) # the integer sum is: 90

# How to perform a substraction with integers

my_int_1 = 89
my_int_2 = 29
my_ints = my_int_1 - my_int_2
print('The integer substraction is:', my_ints) # The integer substraction is: 60

# How to perform multiplications with integers

my_int_1 = 15
my_int_2 = 8
product_int = my_int_1 * my_int_2
print('The integer multiplication total is:', product_int) # The integer multiplication total is: 120

# How to perform a division with integers

my_int_1 = 87
my_int_2 = 14
divided_ints = my_int_1 / my_int_2
print('my integer division total is:', divided_ints) # my integer division total is: 6.214285714285714285

# Now lets talk about floats, floats are numbers with decimal points.

my_float_1 = -16.7
my_float_2 = 4.0
print(type(my_float_1)) # <class 'float'>
print(type(my_float_2)) # <class 'float'>

# How to perform an addition with floats

my_float_1 = 14.7
my_float_2 = 2.0
sum_floats = my_float_1 + my_float_2
print('The float addition is:', sum_floats) # The float addition is: 16.7

# How to perform a substraction with floats

my_float_1 = 7.3
my_float_2 = 20.0
float_diference = my_float_2 - my_float_2
print('The float difference is:', float_diference) # The float difference is: 12.7

# How to perform a multiplication with floats

my_float_1 = 14.9
my_float_2 = 3.24
float_product = my_float_1 * my_float_2
print('The float product is:', float_product) # The float product is: 48.276

# How to perform a division with floats

my_float_1 = 8.6
my_float_2 = 26
float_division = my_float_2 / my_float_1
print('My float division is:', float_division) # My float divsion is: 3.023255813953488372

# If you try to perform an operation with a float and a integer, then the result will always be a float data type

my_float_1 = 8.3
my_int_2 = 2
my_result = my_int_2 + my_float_1

print(my_result) # 10.3
print(type(my_result)) # <class 'float'>

# Now there are also some complex arithmetic operations for example the modulo (%), floor division (//) and even exponentiation (**)
# Lets start with modulo (%). This operation returns the remainder of a divsion.

my_int_1 = 60
my_int_2 = 13
my_float_1 = 16.6
my_float_2 = 3.5

modulo_ints = my_int_1 % my_int_2
modulo_floats = my_float_1 % my_float_2

print('The modulo integers is:', modulo_ints) # The modulo integers is: 8
print('The modulo float is:', modulo_floats) # The modulo float is: 2.6

# Lets continue with the floor division (//). This operation shows how much the divisor can fit in the dividend.

my_int_1 = 60
my_int_2 = 13
my_float_1 = 16.6
my_float_2 = 3.5

floor_ints = my_int_1 // my_int_2
floor_floats = my_float_1 // my_float_2

print('The floor integer divsion is:', floor_ints) # The floor integer division is: 4
print('The floor float division is:', floor_floats) # The floor float division is: 4.0

# The last one! We have exponentiation, which raises the base number based on the second number, the second number being "the power of".

my_int_1 = 60
my_int_2 = 13
my_float_1 = 16.6
my_float_2 = 3.5

exponentiation_result_ints = my_int_1 ** my_int_2
exponentiation_result_floats = my_float_1 ** my_float_2

print('The exponentiation result for the integers is:', exponentiation_result_ints) # The exponentiation result for the integers is: 130606940160000000000000
print('The exponentiation result for the floats is:', exponentiation_result_floats) # The exponentiation result for the floats is: 18637.098826459707

# We also have some functions which is float() and int() which can be applied on any other function.

my_int = 47
my_float_1 = float(my_int_1)

print(my_float_1) # 47.0
print(type(my_float_1)) # <class 'float'>
      
# For the int() function, it is actually pretty interesting since it simply ignores rounding and it directly takes the number that is before the decimal, for example

my_float = 4.82145
my_int = int(my_float)

print(my_int) # 4
print(type(my_int)) # <class 'int'>

# You can convert a string into a int, or float.

my_str_int = '73'
my_str_float = '9.43'

converted_int_str = int(my_str_int)
converted_float_str = float(my_str_float)

print(converted_int_str, type(converted_int_str)) # 73 <class 'int'>
print(converted_float_str, type(converted_float_str)) # 9.43 <class 'float'>

# There are also some other built-in methods where you can "play" with numbers, for example

# The built-in method, round() function, which rounds the number to the nearest integer

my_int_1 = 4.62
my_int_2 = 3.2957

rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 1) # the number 1 means how many decimals it will take.

print(rounded_int_1) # 5
print(rounded_int_2) # 3.3

# The built-in method, abs() function, which gives ONLY the value of a number.

my_number = -4
abs_number = abs(my_number)
print(abs_number) # 4

# The built-in method, pow() function, which can be used for exponentiation only, or exponentiation and modulo operations.

result_exponentiation = pow(4, 8)
print(result_exponentiation) # 4^8 65536

result_exponentiation_modulo = pow(4, 8, 5)
print(result_exponentiation_modulo) # 1