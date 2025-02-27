    # Python - List Comprehension

"""
List Comprehension:
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:
Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
Without list comprehension you will have to write a for statement with a conditional test inside:
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist =[]
for x in fruits:
    if "a" in x:
        newlist.append(x)
        print(newlist)

"""
Output:
['apple']
['apple', 'banana']
['apple', 'banana', 'mango']
"""

# With list comprehension you can do all that with only one line of code:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

"""
Output:
['apple', 'banana', 'mango']
"""

"""
The Syntax
newlist = [expression for item in iterable if condition == True]
The return value is a new list, leaving the old list unchanged.
"""

# Condition
# The condition is like a filter that only accepts the items that evaluate to True.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
"""
Output:
['banana', 'cherry', 'kiwi', 'mango']
"""

# Iterable
# The iterable can be any iterable object, like a list, tuple, set etc.

# You can use the range() function to create an iterable:

newlist = [x for x in range(10)]
print(newlist)

"""
Output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

# With condition
newlist = [x for x in range(10) if x < 5]
print(newlist)

"""
Output:
[0, 1, 2, 3, 4]
"""

# Expression
# The expression is the current item in the iteration, but it is also the outcome,
# which you can manipulate before it ends up like a list item in the new list:

list = ["saad","talha","jackie"]
newlist = [x.upper() for x in list]
print(newlist)
"""
Output:
['SAAD', 'TALHA', 'JACKIE']
"""

# You can also add conditions 

list = ["saad","talha","jackie"]
newlist = [x if x != "jackie" else "jack" for x in list]
print(newlist)

"""
Output:
['saad', 'talha', 'jack']

"Return the item if it is not jackie, if it is jackie return jack".
"""