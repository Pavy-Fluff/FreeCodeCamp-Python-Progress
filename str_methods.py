# FreeCodeCamp - Python Basics
# In here, it will be about more ways to "play" with strings

# we have a built-in method which is upper() which makes all letters in a string uppercase, for example

welcoming = "hello world"
uppercased_welcoming = welcoming.upper()
print(uppercased_welcoming) # HELLO WORLD

# we have a built-in method which is lower() which makes all letters in a string lowercase, for example

order = "PIZZA!"
lowercased_order = order.lower()
print(lowercased_order) # pizza!

# we have a built-in method which is strip() which makes the unnecessary spaces get destroyed, for example

salutations = "      hello world     "
trimmed_salutations = salutations.strip()
print(trimmed_salutations) # hello world

# we have a built-in method which is replace(old, new) which we can specify what to replace for the old version with the new version, for example

device = "phone" 
new_device = device.replace("phone", "Iphone")
print(new_device) # Iphone

# we have a built-in method which is split(separator) which we can make the string separate by a specific separator, if no separator is specified, it separates on the space, for example

names = "karl jacob"
separated_names = names.split()
print(separated_names) # ["karl"], ["jacob"]

# we have a built-in method which is join(iterable)... only works with lists, it lets convert a list into a single string, for example

list = ["hello", "markiplier"]
joined_list = "".join(list)
print(joined_list) # hello markiplier

# we have a built-in method which is startswith(prefix) which we can make a boolean specify if the str is in fact a prefix, for example

salutations = "hello world"
starts_with_hello = salutations.startswith("hello")
print(starts_with_hello) # True

# we have the opposite of the previous built-in method which is endswith() which we can make a boolean specify if the str is in fact a suffix, for example

salutations = "hello world"
ends_with_world = salutations.endswith("world")
print(ends_with_world) # True

# we have a built-in method which is find(substring) which means that we can find where the string is by how many characters we have to go over to find it, for example

salutations = "hello world"
find_world = salutations.find("world")
print(find_world) # 6

# we have a built-in method which is count(substring) which will tell you how many letters there are by the specific string you give it, for example

salutations = "hello world"
count_howmany_o = salutations.count("o")
print(count_howmany_o) # 2

# we have a built-in method which is capitalize() which will make the first character in a string (the 0 index) uppercased, for example

salutations = "hello world"
capitalized_salutations = salutations.capitalize()
print(capitalized_salutations) # Hello world

# we have a built-in method which is isupper() which will turn a True value if all the characters are uppercased, if not, then it will turn the boolean value False for example

salutations = "hello world"
isupper_salutations = salutations.isupper()
print(isupper_salutations) # False

# we have a built-in method which is islower() which will turn a True value if all the characters are lowercased, if not, it will turn the boolean value False, for example

salutations = "hello world"
islower_salutations = salutations.islower()
print(islower_salutations) # True

# we have a built-in method which is title() which will turn every single first character word into a capitalized one, for example

salutations = "hello world"
make_title_salutations = salutations.title()
print(make_title_salutations) # Hello World