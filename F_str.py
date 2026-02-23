# FreeCodeCamp - Python Basics
# Building understandings with F or f strings

# You do not need to concatenate anymore, we now will use curly braces ({}) for each variable, here's an example

name = "Pavy"
age = 16
name_and_age = f"My name is {name} and i am {age}."
print(name_and_age) # My name is Pavy and i am 16.

# we can also put the F-string in a print function. Lets include an addition using variables

number_1 = 73
number_2 = 27
print(f"The first number is {number_1} and the second number is {number_2}. The total is {number_1 + number_2}.") # The first number is 73 and the second number is 27. The total is 100.