# Python If ... Else

"""
Python Conditions and If statements:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.
"""
a = 23
b = 33
if a != b:
    print("a is not equal to b")

"""
Output:
a is not equal to b
"""

"""
In this example we use two variables, a and b, to check the equality. As a is 23, and b is 33,
we know that 23 is not eqaul to 33, and so we print to screen that "a is not equal to b".
"""

"""
Indentation
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. 
"""

"""
a = 23
b = 33
if a != b:
print("a is not equal to b") # you will get an error
"""

"""
Elif:
    The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
"""
a = "saad"
b = "talha"
if a == b:
    print("They are equal")

elif a < b:
    print("a is less then b")

"""
Output:
a is less then b
"""

"""
In this example a is not equal to b, so the first condition is not true, 
but the elif condition is true, so we print to screen that "a is less then b"
"""

"""
Else:
    The else keyword catches anything which isn't caught by the preceding conditions.
"""

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

"""
Output:
a is greater than b
"""

"""
In this example a is greater than b, so the first condition is not true, also the elif condition is not true, 
so we go to the else condition and print to screen that "a is greater than b".
"""
# You can also have an else without the elif:

a = "saad"
b = "Talha"

if len(a) == len(b):
   print("Length of a is equal to the length of b")

else:
   print("Length of a is not equal to the length of b")

"""
Output:
Length of a is not equal to the length of b
"""

"""
Short Hand If: (Comprehnsion)
    If you have only one statement to execute, you can put it on the same line as the if statement.
"""
# One line if statement:
a = 7
b = 15

if a < b : print("a is less than b")

"""
Output:
a is less than b
"""

"""
Short Hand If ... Else:
    If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
"""

# One line if else statement:

a = 33
b = 22

print("A") if a > b else print("B")

"""
Output:
A
"""

# This technique is known as Ternary Operators, or Conditional Expressions.

# You can also have multiple else statements on the same line:
a = 22
b = 45

print("A") if a > b else print("=") if a == b else print("B")

"""
Output:
B
"""

"""
And:
    The and keyword is a logical operator, and is used to combine conditional statements:
"""

a = 200
b = 33
c = 500

if a > b and c > a:
     print("Both conditions are True")

"""
Output:
Both conditions are True
"""


"""
Or:
    The or keyword is a logical operator, and is used to combine conditional statements:
"""
a = 200
b = 33
c = 500

if a > b or c > a:
   print("At least one of the conditions is True")

"""
At least one of the conditions is True
"""

"""
Not:
    The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
"""
a = 66
b = 543

if not a > b:
   print("a is NOT greater than b")

"""
Output:
a is NOT greater than b
"""


"""
Nested If:
    You can have if statements inside if statements, this is called nested if statements.
"""
a = 44
if a > 10:
   print("a is above the 10")
if a > 20:
      print("a is above the 20")
else:
    print("a is above 30.")

"""
Output:
a is above the 10
a is above the 20
"""

"""
The pass Statement
if statements cannot be empty, but if you for some reason have an if statement with no content, 
put in the pass statement to avoid getting an error.
"""
a = 33
b = 200

if b > a:
  pass

# having an empty if statement like this, would raise an error without the pass statement