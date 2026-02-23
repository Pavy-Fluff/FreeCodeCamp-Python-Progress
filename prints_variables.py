# FreeCodeCamp - Python Basics
# Lesson: How to use print functions and variables at the same time

my_integer_variable = 10 # integer data type
print('integer:', my_integer_variable) # integer: 10

my_float_variable = 4.23 # float data type
print('float:', my_float_variable) # float: 4.23

my_string_variable = 'Hello bro' # string data type
print('string:', my_string_variable) # string: Hello bro

my_boolean_variable = True # boolean data type
print('boolean:', my_boolean_variable) # boolean: True

my_set_variable = {4, 6 ,7, 2} # set data type
print('set:', my_set_variable) # set: {4, 6, 7, 2}

my_dictionary_variable = {'name':,'Pavy', 'age': 16} # dictionary data type
print('dictionary:', my_dictionary_variable) # dictionary: {name: Pavy, age: 16}

my_tuple_variable = (4, 7, 1) # tuple data type
print('tuple:', my_tuple_variable) # tuple: (4, 7, 1)

my_range_variable = range(0, 5) # range data type
print('range:', my_range_variable) # range: range(0, 5)

my_list = [16, 'Hello world!', 8.92, True] # list data type
print('list:', my_list) # list: [16, Hello world!, 8.92, True]

my_none_variable = None # data type's gone.
print('data type:', my_none_variable) # Data type: None

# We can figure out what type of variable data type is by typing "type()" for example:

my_variable_1 = 'Hello world!'
my_variable_2 = 16

print(type(my_variable_1)) # <class 'str'> str is a string
print(type(my_variable_2)) # <class 'int'> int is a integer