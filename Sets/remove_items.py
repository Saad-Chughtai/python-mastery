# Python - Remove Set Items

"""
Remove Item
To remove an item in a set, use the remove(), or the discard() method.

Remove "ba" by using the remove() method:
"""
set = {1,2,4,5,3}
set.remove(1)
print(set)

"""
{2, 3, 4, 5}
"""

set = {1,2,4,5,3}
set.discard(5)
print(set)

"""
{1, 2, 3, 4}
"""


"""
If the item to remove does not exist, discard() will NOT raise an error.
You can also use the pop() method to remove an item, but this method will remove a random item, 
so you cannot be sure what item that gets removed.
The return value of the pop() method is the removed item
"""

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

"""
Output:
apple
{'banana', 'cherry'}
"""

# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# clear() method
# The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

"""
Output:
set()
"""

# del keyword
# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset



