import mymodule
mymodule.greeting("Saad")

"""
Output:
Hello, Saad
"""
# Note: When using a function from a module, use the syntax: module_name.function_name.

import mymodule

a = mymodule.person1["name"]
print(a)

"""
Output:
Saad
"""

"""
Re-naming a Module:
    You can create an alias when you import a module, by using the as keyword:
"""

import mymodule as mx

a = mx.person1["age"]
print(a)

"""
Output:
20
"""

"""
Built-in Modules:
    There are several built-in modules in Python, which you can import whenever you like.
"""

import platform

x = platform.system()
print(x)

"""
Windows
"""

"""
Using the dir() Function:
    There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
"""

# List all the defined names belonging to the platform module:

import platform

x = dir(platform)
print(x)

# Note: The dir() function can be used on all modules, also the ones you create yourself.

# Import only the person1 dictionary from the module:
from mymodule import person1

print (person1["age"])

# Note: When importing using the from keyword, do not use the module name when referring to elements in the module. 
# Example: person1["age"], not mymodule.person1["age"]