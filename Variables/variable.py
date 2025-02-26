
# Simple variable 
x = 5          # x is of type int
y = "Saad"     # y is of type str
z = 0.5        # z is of type float
print(x)
print(y)
print(z)
"""
Output:
5
Saad
0.5
"""

# Casting
a = str(3)    # x will be '3'
b = int(3)    # y will be 3
c = float(3)  # z will be 3.0
print(a)
print(b)
print(c)
"""
Output:
3
3
3.0
"""

# Type function to check the type of any variable
print(type(a))
print(type(b))
print(type(c))
"""
Output:
<class 'str'>
<class 'int'>
<class 'float'>
"""

# We can write str in double qoutations "" or in single qoutations ''
f = "Saad"
# is the same as
d = 'Saad'
print(d)
print(f)
"""
Output:
Saad
Saad
"""

# Case Sensitive
g = 4
A = "Vicky"
print(g)
print(A)
#A will not overwrite a, create two variables
"""
Output:
4
Vicky
"""