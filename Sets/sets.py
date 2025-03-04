# Python Sets

"""
Set:
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, 
A set is a collection which is unordered, unchangeable*, and unindexed.

Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets.
"""
set = {1,2,3,4,5}
print(set)

"""
Output:
{1, 2, 3, 4, 5}
"""

# Note: Sets are unordered, so you cannot be sure in which order the items will appear.

"""
Set Items:
    Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered:
    Unordered means that the items in a set do not have a defined order.
    Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable:
    Set items are unchangeable, meaning that we cannot change the items after the set has been created.
    Once a set is created, you cannot change its items, but you can remove items and add new items.

Duplicates Not Allowed:
    Sets cannot have two items with the same value.
"""
# If you write the duplicate set will ignored it
thisset = {1,2,3,4,1,5,6,2}
print(thisset)

"""
Output:
{1, 2, 3, 4, 5, 6}
"""

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

set = {"saad",True , 4,1}
print(set)

"""
Output:
{True, 4, 'saad'}
"""

# And values False and 0 are considered the same value in sets, and are treated as duplicates:
set = {"saad",False ,4, 0}
print(set)

"""
Output:
{False, 4, 'saad'}
"""

"""
Get the Length of a Set
To determine how many items a set has, use the len() function
"""

set = {1,2,3,4,5,6,7,8}
print(len(set))

"""
Output:
8
"""

"""
Set Items - Data Types
    1.Set items can be of any data type:
    2.String type, Integar type, boolean type
"""
a = {1,2,3,4,5}
b = {"saad","taha"}
c = {True,False}

print(a)
print(b)
print(c)

"""
Output:
{1, 2, 3, 4, 5}
{'taha', 'saad'}
{False, True}
"""

# OR set can contain different data type

set11 = {"saad",True,3,4,5}
print(set)

"""
Output:
{True, 3, 4, 5, 'saad'}
"""

"""
type()
    sets are defined as objects with the data type 'set':

<class 'set'>
"""
set1 = {1,23,4,5,6}
print(type(set1))

"""
Output:
<class 'set'>
"""

"""
The set() Constructor
    It is also possible to use the set() constructor to make a set.
"""
x = set((1, 2, 3, 4, 6, 8))  
print(x)

"""
Output:
{1, 2, 3, 4, 6, 8}
"""