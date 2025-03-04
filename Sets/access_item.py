# Python - Access Set Items

"""
Access Items
You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop,
 or ask if a specified value is present in a set, by using the in keyword.
"""

set = {1,23,4,5,6,}
for x in set:
    print(x)

"""
Output:
1
4
5
6
23
"""

set = {1,2,3,4}
if 1 in set:
    print("yes 1 is in the set")
else:
    print("no")

"""
Output:
yes 1 is in the set
"""