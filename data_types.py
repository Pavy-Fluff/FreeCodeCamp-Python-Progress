my_integer_variable = 10
print(type(my_integer_variable)) # <class 'int'>

my_float_variable = 4.20
print(type(my_float_variable)) # <class 'float'>

my_string_variable = 'hello world!'
print(type(my_string_variable)) # <class 'str'>

my_boolean_variable = True
print(type(my_boolean_variable)) # <class 'bool'>

my_set_variable = {3, 9, 0}
print(type(my_set_variable)) # <class 'set'>

my_dictionary_variable = {'name': 'Tom', 'age': 67}
print(type(my_dictionary_variable)) # <class 'dict'>

my_tuple_variable = (7, 6, 2)
print(type(my_tuple_variable)) # <class 'tuple'>

my_range_variable = range(7)
print(type(my_range_variable)) # <class 'range'>

my_list = [16, 'Hai!', 2.78, True]
print(type(my_list)) # <class 'list'>

my_none_variable = None
print(type(my_none_variable)) # <class 'NoneType'>

# isinstance() is simply gonna check if a variable matches a certain data type by utilizing booleans, for example:

isinstance('Hello world!', str) # True
isinstance(True, bool) # True
isinstance(42, int) # True
isinstance('Tommy', list) # False