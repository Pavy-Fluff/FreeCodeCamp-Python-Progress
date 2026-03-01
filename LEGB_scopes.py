# FreeCodeCamp - Python Basics
# In here we will learn what LEGB scopes are

# LEGB Stand for the following :(L) Local Scope, (E) Enclosing Scope, (G) Global Scope, (B) Built-in Scope

# Lets start with a Local Scope

def my_func():
    my_var = 15 
    print(my_var)

my_func() # 15

print(my_var) # NameError: name 'my_var' is not defined

# it means that any variable that is in the my_func code block won't be able to be used outside of it.

# Lets get into the Enclosing Scope

def outer_func():
    msg = "Hello!"
    
    def inner_func():
        print(msg)

    inner_func() 
outer_func() # Hello!

# Keep in mind that you cannot use the variable that is in the inner_func inside the outer_func, for example

def outer_funcwrong():
    msg2 = "Hello!"
    print(msg1)
    def inner_funcwrong():
        msg1 = "welcome"
        print(msg2)
    inner_funcwrong()
outer_func() # NameError: name 'msg1' is not defined

# To solve this problem, you should use the nonlocal keyword which will allow you to change the variable in the previous defined function, for example

def outer_funcfixed():
    msg = 'Hello there!'
    msg2 = '' # Declare msg2 as the enclosed scope
    def inner_funcfixed():
        nonlocal msg2 # Rename the msg2 with the following variable in line 47
        msg2 = 'hi'
        print(msg) # Accesses the message from the outet_funcfixed() function
    inner_funcfixed()
    print(msg2) # This is now accessible
outer_funcfixed()

# Output:
# Hello there!
# hi

# Now lets get into what Golbal Scopes are

my_var = 67

def show_num():
    print(my_var)

show_num() # 67
print(my_var) # 67

# we have a function which is the "global" keyword, it makes the variables inside a defined function modified into a global variable, for example

my_var_1 = 60

def show_numbers():
    global my_var_2
    my_var_2 = 7
    print(my_var_1)
    print(my_var_2)

show_numbers() # 60 7

print(my_var_2) # since my_var_2 is now global, it can be used anytime in the program

# You can also modify the global variable, by using the global keyword in a defined code block, for example

my_var = 5

def change_my_var():
    global my_var
    my_var = 10

change_my_var()

print(my_var) # 10

# Finally, we have the built-in scopes... which is pretty much what we've done earlier, these are simple built-in functions, or methods for strings, integers... etc.

print(str(45)) # '45'
print(type(3.6)) # <class 'float'>
print(isinstance('False', bool)) # False
