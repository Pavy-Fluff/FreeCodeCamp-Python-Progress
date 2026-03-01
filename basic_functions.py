# FreeCodeCamp - Python Basics
# In here lets talk about WHAT functions are in python.

# We have a new basic function, which is input(), this is like... asking the user what the variable should be called, for example

name = input("What is your name? ") # The user types whatever after this question
print("Hello,", name) # Whatever the user typed after the question and presses the enter key, it will print out the print function.

# Another basic function is int() which converts whatever is in the () into an integer, regardless of what data type it is

print(int(3.14)) # 3
print(int('4')) # 4
print(int(True)) # 1
print(int(False)) # 0

# Now lets get into the complex part... you can actually make your OWN functions using the def

def hello():
    print("Hello dude!")

hello() # Hello dude!

# Now you can actually put something in the parantheses of these def, like

def calculate_sum(a, b):
    print(a + b)
calculate_sum(3, 9) # 12

# For the a and b in the parantheses of the calculate_sum() custom function, they are some-kind of variables, if you don't specify what a and b are, it will throw out an TypeError

calculate_sum() # TypeError: missing 2 required positional arguments: 'a' and 'b'

# There is also the return function, which is simply gonna make python "remember" the result for the defined function, if you do not do this then you cannot really do much...

def calculate_sum(a, b):
    print(a + b)
my_result = calculate_sum(4, 7) # 11
print(my_result) # None

# The return function is very useful, since the return function is like multiple other types of functions, here is an example

def calculate_sum(a, b):
    return a + b

my_result = calculate_sum(4, 14)
print(my_result) # 18