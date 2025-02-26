# Global Variables
"""
Variables that are created outside of a function (as in all of the examples in the previous pages) 
are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
"""
x = "Love"

def myfunc():
  print("Coding is " + x)

myfunc()
"""
Output:
Coding is Love
"""

"""
If you create a variable with the same name inside a function, 
this variable will be local, and can only be used inside the function. 
The global variable with the same name will remain as it was, global and with the original value.
"""
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)
# This will use variable  x = "fantastic" (cuz it is locally defined)
myfunc()

print("Python is " + x)
# This will use variable x = "awesome" (cuz it is globally defined and use outside the function)
# Or you can use global key word to make variable to global