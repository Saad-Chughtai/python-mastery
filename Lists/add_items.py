# There are 3 ways to add an item into List
    # 1. By using the append function { append() }
    # 2. By using the insert function { insert() }
    # 3. By using the extend function { extend() }

# 1. By using the append function { append() }
list = [12,13,14,20]
list.append("Hello")
print(list)
"""
Output:
[12, 13, 14, 20, 'Hello']
"""
 # 2. By using the insert function { insert() }
list = [12,13,14,20]
list.insert(4,"50")
print(list)
"""
Output:
[12, 13, 14, 20, '50']
"""
# 3. By using the extend function { extend() }
# To append elements from another list to the current list, use the extend() method.

List1 = ["hello","bye"]
list2 = [1,2,3]
List1.extend(list2)
print(List1)
"""
Output:
['hello', 'bye', 1, 2, 3]
"""

# We can use extend method to add any itreable object (tuples,set,dictionaries,etc)

tlist = ["hi", "hey", "hlo"]
ttuple = ("bye", "seeya")
tlist.extend(ttuple)
print(tlist)
"""
Output:
['hi', 'hey', 'hlo', 'bye', 'seeya']
"""