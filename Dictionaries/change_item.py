# Python - Change Dictionary Items

"""
Change Values:
    You can change the value of a specific item by referring to its key name:
"""
dict = {
    "name":"saad",
    "age":20,
    "year":2004
}
dict["age"] = 21
print(dict)

"""
Output:
{'name': 'saad', 'age': 21, 'year': 2004}
"""

"""
Update Dictionary:
    The update() method will update the dictionary with the items from the given argument.
    The argument must be a dictionary, or an iterable object with key:value pairs.
"""

car = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
car.update({"year":2020})
print(car)

"""
Output:
{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
"""