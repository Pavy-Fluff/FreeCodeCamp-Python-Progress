# FreeCodeCamp - Python Basics
# Building explanations about augmented assignments

# Augmentend assignments is a way to do certain operations much easier, and the syntax for that is [variable <operator>= value]

my_num_1 = 10
my_num_1 += 6
print(my_num_1) # 16

# This means that we can use all types of operators, lets go for every single operator where you can use augmented assignments, the previous one was addition (+=), now lets do substraction (-=) using augmented assignments

my_num_2 = 80
my_num_2 -= 60
print(my_num_2) # 20

# For multiplication (*=)

my_num_3 = 7
my_num_3 *= 8
print(my_num_3) # 56

# For division (/=)

my_num_4 = 40
my_num_4 /= 10
print(my_num_4) # 4.0

# For floor division (//=)

my_num_5 = 32
my_num_5 //= 5
print(my_num_5) # 6

# For modulo (%=)

my_num_6 = 71
my_num_6 %= 5
print(my_num_6) # 1

# For exponent (**=)

my_num_7 = 10
my_num_7 **= 4
print(my_num_7) # 10000

# Now... you can also use these augmented assignments for strings as well! But not all of them! here are some examples:

greeting = "Hello"
greeting += " world!"
print(greeting) # Hello world!

# You can use the addition to combine 2 strings into one string, but you can also use multiplication to repeat how many times the string is gonna be repeated.

greeting_2 = "Hai!"
greeting_2 *= 2
print(greeting_2) # Hai!Hai!

# Only the addition and the multiplication can work, if you try any other operator it will throw a TypeError.

greeting_fail = "Hello"
greeting_fail -= "lo"
print(greeting_fail) # TypeError: unsupported operand type(s) for -=: 'str' and 'str'

# A note to keep in mind, you don't have to use ++variable or +variable neither +++variable because that is not how it works in python, here's an example of what i mean

my_num = 10
print(+my_num) # 10
print(++my_num) # 10
print(+++my_num) # 10

my_num += 1
print(my_num) # 11