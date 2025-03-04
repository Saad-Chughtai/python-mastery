# Python - Add Dictionary Items

"""
Adding Items:
    Adding an item to the dictionary is done by using a new index key and assigning a value to it
"""
dict = {
    "name":"saad",
    "age":20
}

print(dict)

"""
Output:
{'name': 'saad', 'age': 20}
"""
dict["year"] = 2004

print(dict)

"""
Output:
{'name': 'saad', 'age': 20, 'year': 2004}
"""

# Second method is the update () method
# The update() method will update the dictionary with the items from a given argument.
# If the item does not exist, the item will be added.

dict = {
    "name":"saad",
    "age":20
}

print(dict)

"""
Output:
{'name': 'saad', 'age': 20}
"""

dict.update({"year":2004})

print(dict)

"""
Output:
{'name': 'saad', 'age': 20, 'year': 2004}
"""