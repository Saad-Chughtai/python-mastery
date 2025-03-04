# Python - Copy Dictionaries

"""
Copy a Dictionary:
    1.You cannot copy a dictionary simply by typing dict2 = dict1, because: 
    dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
    2.There are two ways to make a copy, 
        1.By using the built-in copy() method
        2.By using the dict constructor

"""
# By using the copy() method

dict1 = {
    "name":"saad",
    "age":20,
    "year":2004
}
mydict = dict1.copy()

print(mydict)

"""
Output:
{'name': 'saad', 'age': 20, 'year': 2004}
"""

# By using the dict constructor
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydict = dict(thisdict)
print(mydict)

"""
Output:
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
"""