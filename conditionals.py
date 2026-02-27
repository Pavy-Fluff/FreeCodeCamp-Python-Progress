# FreeCodeCamp - Python Basics
# In here we will talk more about how booleans work and how we can use conditions

# We have "Comparison operators" which are special because it can check if the operator is True or False, here are some examples

print(6 == 8) # False
print(8 == 8) # True
print(6 != 8) # True
print(6 > 8) # False
print(6 < 8) # True
print(8 >= 8) # True
print(8 <= 7) # False 

# We have a new syntax which is "if <condition>:". If the condition is True, then it will run the if statement, for example:

age = 16

if age < 18:
    print("You are a minor!") # You are a minor! 

# Lets make something very clear the space before the print() function is NECESSARY, because if you skip the space, then it will throw out an IndentationError.

if age < 18:
print("You are a minor!") # IndentationError: expected an idented block after the "if" statement on line 23

# If we have an if statement and it is false, then NOTHING will be printed in the terminal

age = 16

if age >= 18:
    print("You are an adult") # Nothing prints in the terminal

# The solution to combat this, is to use the else: function, which is gonna run only if the if statement is false, for example

age = 16

if age >= 18:
    print("You are an adult!") # Doesn't run since the if statement is False
else:
    print("You are a minor!") # runs because the if statement is False

# We also have one more new function which is "elif <condition:>". This runs only if the first condition is false, and the condition for the elif function is true, for example

age = 10

if age >= 18:
    print("You are an adult") # Doesn't run
elif age >= 13:
    print("You are a teenager!") # Doesn't run
else:
    print("You are a child... How did you get here...?") # Runs

# You can have infinite amounts of elif statements!

age = 1

if age >= 70:
    print("You are pretty old") # doesn't run
elif age >= 30:
    print("You are an adult in your prime") # doesn't run
elif age >= 20:
    print("You are a young adult") # doesn't run
elif age >= 13:
    print("You are a teenager!") # doesn't run
elif age >= 5:
    print("You are EXTRAORDINARILY young.") # doesn't run
else:
    print("You are an infant") # runs

# Now lets get a little bit more complex, now we can run an if statement, in another if statement, for example

is_citizen = True
age = 23

if is_citizen:
    if age >= 18:
        print("You can legally vote.") # runs
else:
    print("Wait until that time comes.") # doesn't run, only if the is_citizen value False

# We have a lot of "truthy" and "Falsy" values, we can check if data types are considered False, or True values, by using the built-in function bool(), for example

# Falsy values:

print(bool(False)) # False
print(bool(0)) # False
print(bool('')) # False

# Truthy values:

print(bool(True)) # True
print(bool(1)) # True
print(bool("Hai!")) # True