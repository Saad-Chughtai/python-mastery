# Python - Access Dictionary Items

"""
Accessing Items:
    You can access the items of a dictionary by referring to its key name, inside square brackets:
"""
dict = {"name":"Saad","country":"Pakistan","city":"Lahore"}
print(dict["name"])

"""
Output:
Saad
"""

# There is also a mthod called get(), but it return the value in new varaible

dict = {"name":"Saad","country":"Pakistan","city":"Lahore"}
x = dict.get("country")
print(x)

"""
Output:
Pakistan
"""

"""
Get Keys:
    The keys() method will return a list of all the keys in the dictionary.
"""

dict = {"Name":"Talha","Age":23,"Country":"United Kingdom"}
x = dict.keys()
print(x)

# Add a new item to the original dictionary

dict = {"Name":"Saad"}
print(dict.keys())

"""
Output:
dict_keys(['Name'])
"""

dict["Age"] = "20"
print(dict.keys())

"""
Output:
dict_keys(['Name', 'Age'])
"""

"""
Get Values
The values() method will return a list of all the values in the dictionary.
"""
dict = {"Name":"Talha","Age":"23","Country":"United Kingdom"}
x = dict.values()
print(x)

"""
Output:
dict_values(['Talha', '23', 'United Kingdom'])
"""

# To Change the value in dict
dict = {"Name":"Talha","Age":"23","Country":"United Kingdom"}
x = dict.values()
print(x)

dict["Age"] = 24
print(x)

"""
Output:
dict_values(['Talha', 24, 'United Kingdom'])
"""

# To add a new value

dict = {"Name":"Talha","Age":"23","Country":"United Kingdom"}
x = dict.values()
print(x) # Before the change

"""
Output:
dict_values(['Talha', '23', 'United Kingdom'])
"""

dict["year"] = 1997
print(x) # After the change

"""
Output:
dict_values(['Talha', '23', 'United Kingdom'])
"""

"""
Get Items:
    The items() method will return each item in a dictionary.
"""
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = dict.items()

print(x)

"""
Output:
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
"""

# Make a change in the original dictionary
dict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = dict.items()

print(x) #before the change

"""
Output:
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
"""
dict["year"] = 2020

print(x) #after the change

"""
Output:
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])
"""

# Add a new item to the original dictionary
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

"""
Output:
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
"""
car["color"] = "red"

print(x) #after the change

"""
Output:
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])
"""

"""
Check if Key Exists
To determine if a specified key is present in a dictionary use the in keyword:
"""
dict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
if "model" in dict:
    print("Yes, 'model' is one of the keys in the dict dictionary")