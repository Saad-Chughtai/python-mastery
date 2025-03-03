"""
    Python Tuples

Tuple:
Tuples are used to store multiple items in a single variable.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.
"""
mytuple = ("Hi ", "I am ", "saad")
print(mytuple)

"""
Output:
('Hi ', 'I am ', 'saad')
"""


"""
Tuple Items:
    1.Tuple items are ordered, unchangeable, and allow duplicate values.
    2.Tuple items are indexed (like in array)

Ordered:
    1.Tuple items have a defined order, and that order will not change.

Unchangeable:
    1.Tuples are unchangeable, we cannot change, add or remove items after the tuple has been created.

Allow Duplicates:
    1.Since tuples are indexed, they can have items with the same value:
"""

mytuple = (1,2,3,4,1,2,)
print(mytuple)

"""
Output:
(1, 2, 3, 4, 1, 2)
"""

"""
Tuple Length:
    1.To determine the len of a tuple, use the len() function:
"""

mytuple = (1,2,3,4,1,2,)
print(len(mytuple))

"""
Output:
6
"""

"""
Create Tuple With One Item
    If you want to create the tuple only with one item, you have to placed the comma after it,
    otherwise python will not recognize it as a tuple
"""

mytuple = ("saad",)
print(type(mytuple))

"""
Output:
<class 'tuple'>
"""

# Not a tuple

mytuple = ("saad")
print(type(mytuple))

"""
Output:
<class 'str'>
"""

"""
Tuple Items - Data Types
    Tuple items can be of any data type (str, int, bool)
"""
tuple1 = ("Hello", " how", " are"," you?")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

"""
Output:
('Hello', ' how', ' are', ' you?')
(1, 5, 7, 9, 3)
(True, False, False)
"""

# Or it can contain different datatype
mytuple = (1,"Hello",2,True,"Bye")
print(mytuple)

"""
Output:
(1, 'Hello', 2, True, 'Bye')
"""


"""
type():
    1.From Python's perspective, tuples are defined as objects with the data type 'tuple':
"""
mytuple = ("Saad","Talha")
print(type(mytuple))

"""
Output:
<class 'tuple'>
"""

"""
The tuple() Constructor:
    1.We can also use the tuple() constructor to make a tuple.
"""
mytuple = tuple(("saad","talha","Hello"))
print(mytuple)

"""
Output:
('saad', 'talha', 'Hello')
"""