# Python - Add Set Items

"""
Add Items:
Once a set is created, you cannot change its items, but you can add new items.

To add one item to a set use the add() method.
"""
set = {1,2,3,4}
set.add(100)
print (set)

"""
Output:
{1, 2, 3, 100, 4}
"""

"""
Add Sets:
    To add items from another set into the current set, use the update() method.
"""
set1 = {1,2,3}
set2 = {4,5,6,7,8}

set1.update(set2)
print(set1)

"""
Output:
{1, 2, 3, 4, 5, 6, 7, 8}
"""

"""
Add Any Iterable:
The object in the update() method does not have to be a set, 
it can be any iterable object (tuples, lists, dictionaries etc.)
"""
thisset = {1,2,3,5,6,7,4}
mylist = [8,9,10]
thisset.update(mylist)
print(thisset)

"""
Output:
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
"""