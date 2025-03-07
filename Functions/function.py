# Python Functions

"""
Function:
    1.A function is a block of code which only runs when it is called.
    2.You can pass data, known as parameters, into a function.
    3.A function can return data as a result.

Creating a Function:
    In Python a function is defined using the def keyword
"""

def my_func():
    print("Hello Welcome Home")

my_func()

"""
Output:
Hello Welcome Home
"""

"""
Arguments:
    1.Information can be passed into functions as arguments.
    2.Arguments are specified after the function name, inside the parentheses. 
    3.You can add as many arguments as you want, just separate them with a comma.
"""

def myfunc(names):
    print("Welcome " + names )

myfunc("Saad")
myfunc("Talha")

"""
Output:
Welcome Saad
Welcome Talha
"""

# Arguments are often shortened to args in Python documentations.

"""
Parameters or Arguments?
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:
    A parameter is the variable listed inside the parentheses in the function definition.
    An argument is the value that is sent to the function when it is called.
"""

"""
Number of Arguments:
    1.By default, a function must be called with the correct number of arguments. 
    2.Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
"""

def myfunc(fname , lname):
    print("Welcome Home " + fname + lname)

myfunc("Saad"," Habib")

"""
Output:
Welcome Home Saad Habib
"""

# If you try to call the function with 1 or 3 arguments, you will get an error:


# def myfunc(fname , lname):
#     print("Welcome Home " + fname + lname)

# myfunc("Saad")

"""
Arbitrary Arguments (*args):
    1.If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
    2.This way the function will receive a tuple of arguments, and can access the items accordingly:
"""

def myfunc(*names):
    print("Welcome Home " + names[2])

myfunc("Saad","Atiq","Talha")

"""
Welcome Home Talha
"""

# But if you want to call all the names (complete tuple) use join() method

def myfunc(*names):
    print("Welcome Home " + ",".join(names))

myfunc("Saad","Atiq","Talha")

"""
Output:
Welcome Home Saad,Atiq,Talha
"""

# Arbitrary Arguments are often shortened to *args in Python documentations.

"""
Keyword Arguments: 
    You can also send arguments with the key = value syntax.
    This way the order of the arguments does not matter
"""

def myfunc(name1,name2):
    print("Welcome Home " + name2)

myfunc(name1 = "Saad", name2 = "Talha")

"""
Output:
Welcome Home Talha
"""

# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

"""
Arbitrary Keyword Arguments (**kwargs):
    1.If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
    2.This way the function will receive a dictionary of arguments, and can access the items accordingly:
"""

def myfunc(**names):
    print("Welcome home" + names["name2"])

myfunc(name1 = "Saad", name2 = " Talha")

"""
Output:
Welcome home Talha
"""

# Or if you want to print the dict by function

def myfunc(**names):
    print(names)

myfunc(name1 = "saad", name2 = "Talha")

"""
Output:
{'name1': 'saad', 'name2': 'Talha'}
"""

# Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.

"""
Default Parameter Value:
    If we call the function without argument, it uses the default value
"""

def myfunc(ani = "Cat"):
    print("I likes " + ani)

myfunc("Wolf")
myfunc("Loin")
myfunc()
myfunc("Tiger")

"""
I likes Wolf
I likes Loin
I likes Cat
I likes Tiger
"""

"""
Passing a List as an Argument:
    1.You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
    2.E.g. if you send a List as an argument, it will still be a List when it reaches the function:
"""

def myfunc(country):
    for x in country:
        print(x)

coun = {"Greece","Pakistan","Norway","Germany"}

myfunc(coun)

"""
Output:
Greece
Pakistan
Germany
Norway
"""

"""
Return Values:
    To let a function return a value, use the return statement:
"""

def myfunc(num):
    return 2 * num

print(myfunc(7))
print(myfunc(6))

"""
Output:
14
12
"""

"""
The pass Statement:
    1.Function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
"""

def myfunc():
    pass

"""
Positional-Only Arguments:
    positional-only arguments are function parameters that must be passed using their position and cannot be passed as keyword arguments.
    To specify that a function can have only positional arguments, add , / after the arguments:
"""

def myfunc(a, /):
    print(a)

myfunc("Saad")

"""
Output:
Saad
"""

"""
What's change in Positional-Only Arguments?
    Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
"""

def myfunc(a):
    print(a)

myfunc(a = "Saad")

"""
Output:
Saad
"""

# But when adding the , / you will get an error if you try to send a keyword argument:

"""
def my_function(a, /):
  print(a)

my_function(a = "Saad")
"""


"""
Keyword-Only Arguments:
    1.Keyword-only arguments are function parameters that must be passed using keyword arguments and cannot be passed positionally.
    2.To specify that a function can have only keyword arguments, add *, before the arguments:
"""

def myfunc(* , b):
    print(b)

myfunc(b = "Talha")

"""
Output:
Talha
"""

# Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:

def myfunc(b):
    print(b)

myfunc("Talha")

"""
Output:
Talha
"""

# But with the *, you will get an error if you try to send a positional argument:

"""
def my_function(*, x):
  print(x)

my_function(3)
"""

"""
Combine Positional-Only and Keyword-Only:
    1.You can combine the two argument types in the same function.
    2.Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
"""

def myfunc(a, b, /, *, c, d):
      print(a + b + c + d)

myfunc("Hello"," Welcome", c = " Home", d = " Saad")

"""
Output:
Hello Welcome Home Saad
"""


"""
Recursion: 
    1.Recursion is when a function calls itself to solve a problem. 
    2.Instead of using loops, the function keeps calling itself with a smaller version of the problem until it reaches a stopping point (called the base case).
"""

def recursion(a):
    if a > 0: # base condition
        result = a + recursion(a -1)
        print(result)
        return result

    else:
        return 0 # Base case: Stops recursion when a = 0

print("Recursion Output: ")
recursion(6)

"""
Output:
1
3
6
10
15
21
"""