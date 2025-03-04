# Python - Join Sets

"""
Join Sets:
    1.There are several ways to join two or more sets in Python.
    2.The union() and update() methods joins all items from both sets.
    3.The intersection() method keeps ONLY the duplicates.
    4.The difference() method keeps the items from the first set that are not in the other set(s).
    5.The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""

# Union
# The union() method returns a new set with all items from both sets.

set1 = {1,2,3,4}
set2 = {5,6,7,8}
set3 = set1.union(set2)

print(set3)

"""
Output:
{1, 2, 3, 4, 5, 6, 7, 8}
"""

# Or you can use | operator instead of union
set1 = {1,2,3,4}
set2 = {5,6,7,8}
set3 = set1 | set2

print(set3)

"""
Output:
{1, 2, 3, 4, 5, 6, 7, 8}
"""

"""
Join Multiple Sets:
    All the joining methods and operators can be used to join multiple sets.
    When using a method, just add more sets in the parentheses, separated by commas:
"""

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"Saad", "Talha"}
set4 = {"Cat", "Wolf", "Loin"}

myset = set1.union(set2,set3,set4)
print(myset)

"""
Output:
{'a', 1, 2, 3, 'Talha', 'Cat', 'Saad', 'Loin', 'Wolf', 'c', 'b'}
"""

# When using the | operator, separate the sets with more | operators:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"Saad", "Talha"}
set4 = {"Cat", "Wolf", "Loin"}

myset = set1 | set2 | set3 | set4

print(myset)

"""
Output:
{'c', 1, 2, 3, 'a', 'Cat', 'Saad', 'Wolf', 'b', 'Talha', 'Loin'}
"""

"""
Join a Set and a Tuple
The union() method allows you to join a set with other data types, like lists or tuples, result will be set
"""

x = (1,2,3,4)
y = {5,6,7,8}

z = y.union(x)
print(z)

"""
Output:
{1, 2, 3, 4, 5, 6, 7, 8}
"""
# The | operator only works to join set with set, not the other datatypes

"""
Update:
    1.The update() method inserts all items from one set into another.
    2.The update() changes the original set, and does not return a new set.
"""

set1 = {1,2,3,4}
set2 = {5,6,7,8}

set1.update(set2)
print(set1)

"""
Output:
{1, 2, 3, 4, 5, 6, 7, 8}
"""

# Note: Both union() and update() will exclude any duplicate items.

"""
Intersection:
    Keep ONLY the duplicate
    The intersection() method will return a new set, that only contains the items that are present in both sets.
"""

set1 = {1,2,4,5,6}
set2 = {2,3,4,6,7,1}

set3 = set1.intersection(set2)
print(set3)

"""
Output:
{1, 2, 4, 6}
"""

# Or you can use the & operator instead of the intersection() method

set1 = {1,2,4,5,6}
set2 = {2,3,4,6,7,1}

set3 = set1 & set2
print(set3)

"""
Output:
{1, 2, 4, 6}
"""

# Note: The & operator only allows you to join sets with sets, and not with other data types

"""
The intersection_update() method will also keep ONLY the duplicates, 
but it will change the original set instead of returning a new set.
"""

set1 = {1,2,3,5,6,7,7,6}
set2 = {1,2,8,7,3,4}

set1.intersection_update(set2)
print(set1)

"""
Output:
{1, 2, 3, 7}
"""

# The values True and 1 are considered the same value. The same goes for False and 0.

# Join sets that contains the values True, False, 1, and 0

set1 = {"loin", 1,  "wolf", 0, "cat"}
set2 = {False, "google", 1, "cat", 2, True}

set3 = set1.intersection(set2)

print(set3)

"""
Oyutput:
{False, 1, 'cat'}
"""

"""
Difference
    The difference () returns a new set that contain only items form first set which are not present in other set
"""
set1 = {"saad","Talha","Jack"}
set2 = {"saad","wolf","Loin"}

set3 = set1.difference(set2)
print(set3)

"""
Output:
{'Talha', 'Jack'}
"""

# Or you can use the - operator instead of the difference() method
set1 = {"saad","Talha","Jack"}
set2 = {"saad","wolf","Loin","Talha"}

set3 = set1 - set2
print(set3)

"""
Output:
{'Jack'}
"""

# Note: The - operator only allows you to join sets with sets, and not with other data types

"""
The difference_update() method will also keep the items from the first set that are not in the other set, 
but it will change the original set instead of returning a new set.
"""

set1 = {1,2,3,4}
set2 = {2,3,5,6}

set1.difference_update(set2)
print(set1)

"""
Output:
{1, 4}
"""

"""
Symmetric Differences:
    The symmetric_difference() method will keep only the elements that are NOT present in both sets.
"""

set1 = {"saad","talha","cat","Wolf"}
set2 = {"saad","Tiger"}

set3 = set1.symmetric_difference(set2)
print(set3)

"""
Output:
{'Wolf', 'cat', 'talha', 'Tiger'}
"""

# Or you can use the ^ operator instead of the symmetric_difference() method,

set1 = {"saad","talha","cat","Wolf"}
set2 = {"saad","Tiger"}

set3 = set1 ^ set2
print(set3)

"""
Output:
{'Tiger', 'talha', 'cat', 'Wolf'}
"""

# The ^ operator only allows you to join sets with sets, and not with other data types

"""
The symmetric_difference_update() method will also keep all but the duplicates,
but it will change the original set instead of returning a new set.
"""

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

"""
Output:
{'google', 'microsoft', 'cherry', 'banana'}
"""