# Python - Update Tuples

# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

"""
In order to update the value of tuple or change it , or if you want to add new item in the tuple,
or if you want to del the item from the tuple, you can't perfrom these functions direclty,
because tuple are unchangeable 

For this you have to convert the tuple into list perfrom the function you want the again convert into tuple
"""

# Change Tuple Values

x = (1,2,3,4,5)
y = list(x)
print(y)

"""
Output:
[1, 2, 3, 4, 5]
"""

y[1] = 6
z = tuple(y)
print(z)

"""
Output:
(1, 6, 3, 4, 5)
"""

# Add Items

x = (1,2,3,4)
y = list(x)
y.append(7) # append function add the new item at the end of the list
z = tuple(y)
print(z)

"""
Output:
(1, 2, 3, 4, 7)
"""

# Or if you want to add 2 tuples you can
tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple1 += tuple2
print(tuple1)

"""
Output:
(1, 2, 3, 4, 5, 6)
"""

# Remove item

x = (1,2,3,4,5,6)
y = list(x)
y.remove(3)
z = tuple(y)
print(z)

"""
Output:
(1, 2, 4, 5, 6)
"""

# Or you can delte the compelte tuple
x = (1,23,5,6,7,5)
del x
print(x) # this will raise an error because the tuple no longer exists
