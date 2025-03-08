# Python Lambda

"""
Lambda:
    1.A lambda function is a small anonymous function.
    2.A lambda function can take any number of arguments, but can only have one expression.

Syntax:
    lambda arguments : expression
The expression is executed and the result is returned:
"""

x = lambda a: a + 10
print(x(5))

"""
Output:
15
"""

# Lambda functions can take any number of arguments:

x = lambda a, b : a * b
print(x(5, 6))

"""
Output:
30
"""

x = lambda a,b,c: a *b + 10 +c
print(x(5,6,7))

"""
Output:
47
"""

"""
Why Use Lambda Functions?
    1.The power of lambda is better shown when you use them as an anonymous function inside another function.
    2.Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
"""

def my_func(n):
  return lambda a : a * n

# Use that function definition to make a function that always doubles the number you send in:

def my_func(n):
  return lambda a : a * n

my_double = my_func(2)
print(my_double(6))

"""
Output:
12
"""

# Or, use the same function definition to make a function that always triples the number you send in:

def my_func(n):
  return lambda a: a * n

my_triple = my_func(3)

print(my_triple(5))

"""
Output:
15
"""

# Or, use the same function definition to make both functions, in the same program:

def my_func(n):
  return lambda a: a * n

my_double = my_func(2)
my_triple = my_func(3)
my_tetra = my_func(4)

print(my_double(2))
print(my_triple(2))
print(my_tetra(2))

"""
Output:
4
6
8
"""

# Use lambda functions when an anonymous function is required for a short period of time.

