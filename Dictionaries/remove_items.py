# Python - Remove Dictionary Items

"""
Removing Items:
    There are several methods to remove items from a dictionary:
        1. The pop() method removes the item with the specified key name
        2. The popitem() method removes the last inserted item 
        3. The del keyword removes the item with the specified key name
        4. The clear() method empties the dictionary
"""

# The pop() method
car = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
car.pop("model")
print(car)

"""
Output:
{'brand': 'Ford', 'year': 1964}
"""

# The popitem() method
car = {
    "brand":"Toyota",
    "model":"Supra",
    "year":2000,
}
car.popitem()
print(car)

"""
Output:
{'brand': 'Toyota', 'model': 'Supra'}
"""

# The del keyword
bike = {
    "name":"Kawasaki",
    "model":"H2R",
    "year":2025
}

print(bike)

"""
Output:
{'name': 'Kawasaki', 'model': 'H2R', 'year': 2025}
"""

del bike["year"]

print(bike)

"""
Output:
{'name': 'Kawasaki', 'model': 'H2R'}
"""

# Or you can use it to delete the complete dict
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del dict
print(dict) #this will cause an error because "thisdict" no longer exists.

# The clear() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()

print(thisdict)

"""
Output:
{}
"""