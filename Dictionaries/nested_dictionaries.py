# Python - Nested Dictionaries

"""
Nested Dictionaries:
    A dictionary can contain dictionaries, this is called nested dictionaries.
"""
animals = {
    "animal1": {"name": "lion", "age": 2},  
    "animal2": {"name": "cat", "age": 5},
    "animal3": {"name": "wolf", "age": 4}
}

print(animals)

"""
Output:
{'animal1': {'name': 'lion', 'age': 2}, 'animal2': {'name': 'cat', 'age': 5}, 'animal3': {'name': 'wolf', 'age': 4}}
"""

# Or, if you want to add three dictionaries into a new dictionary:

animal1 = {
    "name":"cat",
    "age":5
}

animal2 = {
    "name":"loin",
    "age":3
}

animal3 = {
    "name":"wolf",
    "age":4
}

animals = {
    "animal1" : animal1,
    "animal2" : animal2,
    "animal3" : animal3
}

print(animals)

"""
Output:
{'animal1': {'name': 'cat', 'age': 5}, 'animal2': {'name': 'loin', 'age': 3}, 'animal3': {'name': 'wolf', 'age': 4}}
"""

"""
Access Items in Nested Dictionaries:
    To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
"""
fruits = {
    "fruit1" : {
        "name":"Orange",
        "quantity":100
    },
    "fruit2" : {
        "name":"Mango",
        "qunatity":200
    }
}
print(fruits["fruit2"]["name"])

"""
Output:
Mango
"""

"""
Loop Through Nested Dictionaries:
    You can loop through a dictionary by using the items() method like this:
"""

animal1 = {
    "name":"cat",
    "age":5
}

animal2 = {
    "name":"loin",
    "age":3
}

animal3 = {
    "name":"wolf",
    "age":4
}

animals = {
    "animal1" : animal1,
    "animal2" : animal2,
    "animal3" : animal3
}

for x, obj in animals.items():
    print(x)
    for y in obj:
        print(y + ':',obj[y])

"""
Output:
animal1
name: cat
age: 5
animal2
name: loin
age: 3
animal3
name: wolf
age: 4
"""