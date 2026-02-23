# FreeCodeCamp - Python basics
# Building more understandings with strings

my_string_1 = 'Hello'
my_string_2 = "Hello"

# They function the same way

# Multi-line strings

my_string_3 = """double
"quoted" 
multi-line"""
my_string_4 = '''single 
'quoted' 
multi-line 
string'''

# When you need to have a long message, you should be careful with what quotes you use, you can't just use only single quotes, nor double quotes.

message = "I'm tired"
specification = 'Are you really being "wordy" today?'

# If you do decide to not be careful with quotation marks, then you can do the following

new_message = "I\'m tired"
new_specification = "Are you really being \"wordy\" today?"

# we can also verify if a variable has certain words or characters, for example

newcomer = "Hello world!"
print("Hello" in newcomer) # True
print("Hai" in newcomer) # False
print("hey" in newcomer) # False
print("o" in newcomer) # True
print("g" in newcomer) # False

# We can use the function len() to figure out how many characters we have in a string, for example

new_comer_2 = "Hello world"
print(len(new_comer_2)) # 11

# Each character in a string has a number, it starts from 0

new_comer_3 = "hey"
print(new_comer_3[0]) # h
print(new_comer_3[2]) # y

# It can be also in reverse!

new_comer_4 = "hello"
print(new_comer_4[-1]) # o
print(new_comer_4[-4]) # e

# If you have 2 variables with the same labels, the print function will "grab" the nearest variable, that being the most recent variable, for example

greeting = 'hi'
greeting = 'hello'
print(greeting) # hello

# You can't put assignments for a variable

greeting = "Hello everyone" # correct
greeting[0] = "Hello everyone" # incorrect