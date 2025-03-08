# Python Arrays
# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

"""
Arrays:
    Arrays are used to store multiple values in one single variable
"""

car = ["Model","Year","Brand",]
print(car)

"""
Output:
['Model', 'Year', 'Brand']
"""

"""
What is an Array?
    1.An array is a special variable, which can hold more than one value at a time.
    2.If you have a list of items (a list of car specs, for example), storing the specs in single variables could look like this:
"""
specs1 = "Model"
specs2 = "Year"
specs3 = "Brand"

"""
However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?

The solution is an array!
    An array can hold many values under a single name, and you can access the values by referring to an index number.
"""

"""
Access the Elements of an Array:
    You refer to an array element by referring to the index number.
"""

cars = ["BMW","Toyota","Mercedes","Maclern"]
print(cars[2])

"""
Output:
Mercedes
"""

# Or if you want to modify the value
cars = ["BMW","Toyota","Mercedes","Maclern"]
cars[1] = "Ford"
print(cars)

"""
['BMW', 'Ford', 'Mercedes', 'Maclern']
"""

"""
The Length of an Array:
    Use the len() method to return the length of an array (the number of elements in an array).
"""

cars = ["BMW","Toyota","Mercedes","Maclern"]
print(len(cars))

"""
4
"""

# Note: The length of an array is always one more than the highest array index.

"""
Looping Array Elements:
    You can use the for in loop to loop through all the elements of an array.
"""

cars = ["BMW","Toyota","Mercedes","Maclern"]
for x in cars:
    print(x)

"""
BMW
Toyota
Mercedes
Maclern
"""

"""
Adding Array Elements:
    You can use the append() method to add an element to an array.
"""

cars = ["BMW","Toyota","Mercedes","Maclern"]
cars.append("Honda")

print(cars)

"""
Output:
['BMW', 'Toyota', 'Mercedes', 'Maclern', 'Honda']
"""

"""
Removing Array Elements:
    You can use the pop() method to remove an element from the array by indexing.
"""

cars = ["BMW","Toyota","Mercedes","Maclern"]
cars.pop(3)

print(cars)

"""
Output:
['BMW', 'Toyota', 'Mercedes']
"""

# You can also use the remove() method to remove an element from the array.

cars = ["BMW","Toyota","Mercedes","Maclern"]
cars.remove("Toyota")

print(cars)

"""
Output:
['BMW', 'Mercedes', 'Maclern']
"""

# Note: The list's remove() method only removes the first occurrence of the specified value.

"""
Array Methods:
    Python has a set of built-in methods that you can use on lists/arrays.
"""

"""
Method	            Description
append()	        Adds an element at the end of the list
clear()	            Removes all the elements from the list
copy()	            Returns a copy of the list
count()	            Returns the number of elements with the specified value
extend()	        Add the elements of a list (or any iterable), to the end of the current list
index()	            Returns the index of the first element with the specified value
insert()	        Adds an element at the specified position
pop()	            Removes the element at the specified position
remove()	        Removes the first item with the specified value
reverse()	        Reverses the order of the list
sort()	            Sorts the list
"""

# append()

animals = ["Loin","Wolf","Cat"]

print(animals) # Before Adding

"""
Output:
['Loin', 'Wolf', 'Cat']
"""
animals.append("Tiger")

print(animals) # After adding

"""
Output:
['Loin', 'Wolf', 'Cat', 'Tiger']
"""

"""
Definition and Usage:
    The append() method appends an element to the end of the list.

Syntax
    list.append(elmnt)

Parameter Values:

Parameter	        Description
elmnt	            Required. An element of any type (string, number, object etc.)
"""

# clear()

animals = ["Loin","Wolf","Cat"]
animals.clear()

print(animals)

"""
Output:
[]
"""

"""
Definition and Usage:
    The clear() method removes all the elements from a list.

Syntax:
    list.clear()

Parameter Values
    No parameters
"""

# copy()

animals = ["Loin","Wolf","Cat"]
ani = animals.copy()

print(ani)

"""
Output:
['Loin', 'Wolf', 'Cat']
"""

"""
Definition and Usage:
    The copy() method returns a copy of the specified list.

Syntax:
    list.copy()

Parameter Values:
    No parameters
"""

# count()

animals = ["Loin","Wolf","Cat"]

print(animals.count("Cat"))

"""
Output:
1
"""

"""
Definition and Usage:
    The count() method returns the number of elements with the specified value.

Syntax:
    list.count(value)

Parameter Values:

Parameter	    Description
value	        Required. Any type (string, number, list, tuple, etc.). The value to search for.

"""

# extend()

animal1 = ["Loin","Wolf","Cat"]
animal2 = ["Rabbit","Goat"]

animal1.extend(animal2)

print(animal1)

"""
['Loin', 'Wolf', 'Cat', 'Rabbit', 'Goat']
"""

"""
Definition and Usage:
    The extend() method adds the specified list elements (or any iterable) to the end of the current list.

Syntax:
    list.extend(iterable)

Parameter Values:

Parameter	    Description
iterable	    Required. Any iterable (list, set, tuple, etc.)
"""

# index()

animals = ["Loin","Wolf","Cat"]
print(animals.index("Cat"))

"""
Output:
2
"""

"""
Definition and Usage:
    The index() method returns the position at the first occurrence of the specified value.

Syntax:
    list.index(elmnt)

Parameter Values:

Parameter	    Description
elmnt	        Required. Any type (string, number, list, etc.). The element to search for

Note: The index() method only returns the first occurrence of the value.

"""

# inset()

animals = ["Loin","Wolf","Cat"]
animals.insert(3,"Goat")

print(animals)

"""
Output:
['Loin', 'Wolf', 'Cat', 'Goat']
"""

"""
Definition and Usage:
    The insert() method inserts the specified value at the specified position.

Syntax:
    list.insert(pos, elmnt)

Parameter Values:

Parameter	    Description
pos(index)	    Required. A number specifying in which position to insert the value
elmnt	        Required. An element of any type (string, number, object etc.)
"""

# pop()

animals = ["Loin","Wolf","Cat"]
animals.pop(1)

print(animals)

"""
Output:
['Loin', 'Cat']
"""

"""
Definition and Usage:
    The pop() method removes the element at the specified position.

Syntax:
    list.pop(pos)

Parameter Values:

Parameter	    Description
pos	Optional.   A number specifying the position of the element you want to remove, default value is -1, which returns the last item

Note: The pop() method returns removed value.

"""

# remove()

animals = ["Loin","Wolf","Cat"]
animals.remove("Cat")

print(animals)

"""
Output:
['Loin', 'Wolf']
"""

"""
Definition and Usage:
    The remove() method removes the first occurrence of the element with the specified value.

Syntax:
    list.remove(elmnt)

Parameter Values

Parameter	    Description
elmnt	        Required. Any type (string, number, list etc.) The element you want to remove

"""

# reverse()

animals = ["Loin","Wolf","Cat"]
animals.reverse()

print(animals)

"""
Output:
['Cat', 'Wolf', 'Loin']
"""

"""
Definition and Usage:
    The reverse() method reverses the sorting order of the elements.

Syntax:
    list.reverse()

Parameter Values:
    No parameters
"""

# sort()

animals = ["Loin","Wolf","Cat"]

print(animals)

"""
Output:
['Loin', 'Wolf', 'Cat']
"""

animals.sort()

print(animals)

"""
Output:
['Cat', 'Loin', 'Wolf']
"""

"""
Definition and Usage:
    1.The sort() method sorts the list ascending by default.
You can also make a function to decide the sorting criteria(s).

Syntax:
    list.sort(reverse=True|False, key=myFunc)
    
Parameter Values:

Parameter	    Description
reverse	        Optional. reverse=True will sort the list descending. Default is reverse=False
key	            Optional. A function to specify the sorting criteria(s)
"""

# In descending order:

animals = ["Loin","Wolf","Cat"]
animals.sort(reverse=True)

print(animals)

"""
Output:
['Wolf', 'Loin', 'Cat']
"""

# Sort the list by the length of the values:

def my_func(e):
  return len(e)

animals = ["Loin","Wolf","Cat"]

animals.sort(key=my_func)

print(animals)

"""
Output:
['Cat', 'Loin', 'Wolf']
"""

# Sort a list of dictionaries based on the "year" value of the dictionaries:

def my_func(n):
   return len(n)

cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011} 
]

car.sort(key=my_func)

print(cars)

"""
[{'car': 'Mitsubishi', 'year': 2000}, {'car': 'Ford', 'year': 2005}, {'car': 'VW', 'year': 2011}, {'car': 'BMW', 'year': 2019}]
"""

# Sort the list by the length of the values and reversed:

def my_func(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW']

cars.sort(reverse=True, key=my_func)

print(cars)

"""
Output:
['Mitsubishi', 'Ford', 'BMW']
"""

# Note: All these methods are of Lists which can be used instead, cuz python doesn't have built-in support for Arrays