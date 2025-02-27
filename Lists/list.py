"""
Python Lists

List is a collection which is ordered and changeable. Allows duplicate members.

Lists are used to store multiple items in a single variable.
Lists are created using square brackets:
"""
thislist = ["apple", "banana", "cherry"]
print(thislist)
"""
Output:
['apple', 'banana', 'cherry']
"""


"""
List Items:
1. List items are ordered, changeable, and allow duplicate values.
2. List items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.
    Note: There are some list methods that will change the order,
but in general: the order of the items will not change.

Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

Allow Duplicates
Since lists are indexed, lists can have items with the same value:

"""
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

"""
Output:
['apple', 'banana', 'cherry', 'apple', 'cherry']
"""

# List Length
# To determine how many items a list has, use the len() function:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

"""
Output:
3
"""


"""
List Items - Data Types
List items can be of any data type(String, int and boolean) 
"""

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

"""
Output:
['apple', 'banana', 'cherry']
[1, 5, 7, 9, 3]
[True, False, False]
"""


# OR 

# A list can contain different data types:

list1 = ["abc", 34, True, 40, "male"]
print(list1)

"""
Output:
['abc', 34, True, 40, 'male']
"""


# From Python's perspective, lists are defined as objects with the data type 'list':

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

"""
Output:
<class 'list'>
"""


"""
The list() Constructor
It is also possible to use the list() constructor when creating a new list.
"""

# Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry"))
print(thislist)

"""
Output:
['apple', 'banana', 'cherry']
"""