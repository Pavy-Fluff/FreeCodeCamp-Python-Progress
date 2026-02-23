# FreeCodeCamp - Python Basics
# How to "slice" strings

# We know that we can identify each character in a string by its index, which starts from 0

str = "Hello world"
print(str[0]) # H
print(str[3]) # l
print(str[-3]) # r

# Str slicing is gonna grab a PORTION of it by using str[start:stop] function, here's an example

welcome = "hello there!"
print(welcome[0:4]) # hell

# What happens if you do not specify the start index? well it will start with an index of 0, for example

welcome = "hello there!"
print(welcome[:8]) # hello th

# What if you do not specify the stop index? Well it will end 'till the end of the string, based on what the start index is, for example

welcome = 'hello there!'
print(welcome[3:]) # lo there!

# This won't alter the original variable

welcome = "hello there!"
print(welcome[:7]) # hello t
print(welcome) # hello there!

# if you do not specify the start index, nor the stop index, but include a colon you will still get the whole str, here's an example

welcome = "hello there!"
print(welcome[:]) # hello there!

# there's also an optional step function which can be written like str[start:stop:step].
# the step function will be determined by the start and stop function and whatever number you put in the step function, it will skip the indexes based on what number is on the step function, here's an example

welcome = "hello there!" 
print(welcome[0:11:2]) # hlotee
print(welcome[0:11:1]) # hello there!
print(welcome[0:11:3]) # hltr

# You can do a funny trick with the step function, that being reverse wording the original str, for example

salutations = "hello world"
print(salutations[::-1]) # dlrow olleh

# Important: the step function cannot be 0!