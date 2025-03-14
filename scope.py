"""
Python Scope:
    A variable is only available from inside the region it is created. This is called scope.
"""

"""
Local Scope:
    A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
"""

def name_print():
    x = "Saad"
    print(x)

name_print()

"""
Output:
Saad
"""

# Variable x can't be access out of the function cuz it is locally defined 

"""
Function Inside Function:
    As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:
"""

def print_num():
    x = 15
    def print_num2():   # Inner Function
        print(x)
    print_num2()

print_num()

"""
Output:
15
"""

"""
Global Scope:
    1.A variable created in the main body of the Python code is a global variable and belongs to the global scope.
    2.Global variables are available from within any scope, global and local.
"""

x = 7

def print_num():
    print(x)

print_num() # Function Call

"""
Output:
7
"""

print(x)    # Simple print method

"""
Output:
7
"""

"""
Naming Variables:
    1.If you operate with the same variable name inside and outside of a function, 
    Python will treat them as two separate variables, one available in the global scope (outside the function) 
    and one available in the local scope (inside the function):
"""

x = 12      # Global variable

def print_num():
    x =  30
    print(x)

print_num()

"""
Output:
30
"""
print(x)

"""
Output:
12
"""

"""
Global Keyword:
    If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

The global keyword makes the variable global.
"""

def names():
    global name1
    name1 = "Saad"
    name2 = "Talha"
    name3 = "Atiq"


    print(name1 + ", " + name2 + ", " + name3)

names()

"""
Output:
Saad, Talha, Atiq
"""

print(name1)    # Only name1 is available outside the function 

"""
Output:
Saad
"""

# Also, use the global keyword if you want to make a change to a global variable inside a function.

x = 200

def myfunc():
  global x
  x = 60
  print(x)

myfunc()

"""
Output:
60
"""

print(x)

"""
Output:
60
"""

"""
Nonlocal Keyword:
    The nonlocal keyword is used to work with variables inside nested functions.
    The nonlocal keyword makes the variable belong to the outer function.
"""

def myfunc1():
  x = "Saad"        # x is a local variable in myfunc1()
  
  def myfunc2():
    nonlocal x      # Refers to the x variable from myfunc1(), not a new local variable
    x = "Hello"     # Modifies x in myfunc1()
  
  myfunc2()         # Calls myfunc2(), which changes x to "hello"
  return x          # Returns the modified value of x

print(myfunc1())    

"""
Output:
Hello
"""
