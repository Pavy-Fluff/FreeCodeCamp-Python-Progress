# FreeCodeCamp - Python Basics
# In here we will talk what are boolean operators and how to build more complex decision-making logic in code.

# Boolean operators are "and", "or" and "not" operator

# Lets go and take a look at how the "and" operator works
# The "and" operator is gonna take two data types and check if both are true, if one is falsy, then the result will be in a falsy value, if BOTH are true then it will be a truthy value, for example
# The "and" operator is gonna check from left to right, if the first data type is false, it completely ignores the second data type and gives a falsy value.

is_citizen = True
age = 30
print(is_citizen and age) # 30

# Now lets use this in an if statement

is_citizen = True
age = 23

if is_citizen and age >= 18:
    print("You are eligible to vote") # This one will run
else:
    print("You are NOT eligible to vote") # This one won't run, since BOTH data types are true.

# Lets go and take a look at how the "or" operator works
# This operator will take if at least ONE of the data types is true, this one will not run only if all the data types are false, for example.

is_employed = False
age = 19
print(is_employed or age) # 19

# Now lets use an if statement

is_student = True
age = 19

if is_student or age < 18:
    print("You can get a student discount!") # Runs because is_student has the boolean value set to true
else:
    print("You are not getting a student discount.") # doesn't run since one data type is already true

# We have the last operator, which is the "not" operator.
# This operator reverses the truthy value to a Falsy value and Falsy value to a Truthy value

print(not '') # True
print(not 'Hello') # False
print(not 0) # True
print(not 1) # False
print(not False) # True
print(not True) # False

# Now lets use this operator in an if statement

admin = False

if not admin:
    print("You cannot enter here.") # This one runs, since not admin is the same as not False which results in a truthy value.
else:
    print("Welcome!") # This one doesn't run, since the if statement is true