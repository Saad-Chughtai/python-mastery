# Python - Tuple Methods

"""
There are only two Built-in Methods for tuple in python
    1.count() Returns the number of times a specified value occurs in a tuple
    2.index() Searches the tuple for a specified value and returns the position of where it was found
"""
# count() method

tuple = (1,2,3,4,5,5,6,6,7,8,9,9,1)
x = tuple.count(5)
print(x)

"""
Output:
2
"""

"""
Definition and Usage:
    1.The count() method returns the number of times a specified value appears in the tuple.

Syntax
tuple.count(value)

Parameter Values:
Parameter	    Description
value	        Required. The item to search for
"""

# index()method

tuple = (1,2,3,4,5,6,7,1,5)
x = tuple.index(5)
print(x)

"""
Output:
4
"""

"""
Definition and Usage:
    1.The index() method finds the first occurrence of the specified value.
    2.The index() method raises an exception if the value is not found.

Syntax:
tuple.index(value)

Parameter Values:
Parameter	    Description
value	        Required. The item to search for
"""