# Python Dictionaries

"""
Dictionary:
    1.Dictionaries are used to store data values in key:value pairs.
    2.A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
    3.Dictionaries are written with curly brackets, and have keys and values:
"""
dictt = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dictt)

"""
Output:
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
"""

"""
Dictionary Items:
    1.Dictionary items are ordered, changeable, and do not allow duplicates.
    2.Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
"""
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict1["brand"])

"""
Output:
Ford
"""

"""
Ordered or Unordered?
    1.As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
    2.Dictionaries are ordered, it means that the items have a defined order, and that order will not change.
    3.Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

Changeable:
    Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

Duplicates Not Allowed:
    Dictionaries cannot have two items with the same key:
"""
dict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(dict2)

"""
Output:
{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
"""

"""
Dictionary Length:
    To determine how many items a dictionary has, use the len() function:
"""
dict3 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(dict3))

"""
Output:
3
"""

"""
Dictionary Items - Data Types
The values in dictionary items can be of any data type (str,int,bool)
"""
dict4 = {
    "brand":"Toyota",
    "model": "Supra",
    "year": 1964,
    "electric": False
        }
print(dict4)

"""
Output:
{'brand': 'Toyota', 'model': 'Supra', 'year': 1964, 'electric': False}
"""

"""
type():
    Dictionaries are defined as objects with the data type 'dict':
"""
dict5 = {
    "brand":"Toyota",
    "model": "Supra",
    "year": 1964,
    "electric": False
        }
print(type(dict5))

"""
Output:
<class 'dict'>
"""

"""
The dict() Constructor
It is also possible to use the dict() constructor to make a dictionary.
"""

dict6 = dict(name = "Saad", age = 20, country = "Pakistan")
print(dict6)

"""
Output:
{'name': 'Saad', 'age': 20, 'country': 'Pakistan'}
"""