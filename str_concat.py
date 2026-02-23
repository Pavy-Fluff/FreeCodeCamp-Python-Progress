# FreeCodeCamp - Python basics
# How to combine a variable type <class 'str'> with another

my_string_1 = 'hello,'
my_string_2 = "world"

sentence = my_string_1 + '' + my_string_2
print(sentence) # hello, world

# This only works with str, nothing else! You'll get a TypeError if you insert a different type than str, for example

name = "Pavy"
age = 16

basics_about_me = name + age
print(basics_about_me) # TypeError can only concatenate a str (not "int") to a str

# To fix this you need to use the str() function to the other types of data, for example

name = "Pavy"
age = 16

name_and_age = name + str(age)
print(name_and_age) # Pavy16

# if have 2 variables and you want to convert it into a single variable, you can use the operator (+=) which will append 2 variables or more, for example

name = "Pavy"
age = 16

name_and_age = name # starts with the name
name_and_age += str(age) # continues with the age
print(name_and_age) # Pavy16