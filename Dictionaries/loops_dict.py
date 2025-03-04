# Python - Loop Dictionaries

"""
Loop Through a Dictionary:
    1.You can loop through a dictionary by using a for loop.
    2.When looping through a dictionary, the return value are the keys of the dictionary,
    but there are methods to return the values as well.
"""
dict = {
    "name":"saad",
    "age":20
}
for x in dict:
    print(x)

"""
Output:
name
age
"""

# Print all values in the dictionary, one by one:

dict = {
    "name":"saad",
    "age":20
}
for x in dict:
    print(dict[x])

"""
Output:
saad
20
"""

# Or you can also use the values() method to return values of a dictionary:

dict = {
    "name":"saad",
    "age":20
}

for x in dict.values():
    print(x)
    
"""
Output:
saad
20
"""

# Similarly you can use the keys() method to return the keys of a dictionary:
dict = {
    "name":"saad",
    "age":20
}

for x in dict.keys():
    print(x)
    
"""
Output:
name
age
"""

# Or you can Loop through both keys and values, by using the items() method:
dict = {
    "name":"saad",
    "age":20
}

for x in dict.items():
    print(x)

"""
Output:
('name', 'saad')
('age', 20)
"""