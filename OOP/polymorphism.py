# Python Polymorphism

"""
Polymorphism:
    The word "polymorphism" means "many forms", and in programming it refers to 
    methods/functions/operators with the same name that can be executed on many objects or classes.
"""

"""
Function Polymorphism:
    An example of a Python function that can be used on different objects is the len() function.
"""

"""
String:
    For strings len() returns the number of characters:
"""

string = "Saad"
print(len(string))

"""
Output:
4
"""

"""
Tuple:
    For tuples len() returns the number of items in the tuple:
"""

tuple = ("Saad","Talha")
print(len(tuple))

"""
Output:
2
"""

"""
Dictionary:
    For dictionaries len() returns the number of key/value pairs in the dictionary:
"""

dictionary = {
    "Name":"Saad",
    "Age":20,
    "City":"Lahore"
}
print(len(dictionary))

"""
Output:
3
"""

# The len() method performs same functionality on different objects

"""
Class Polymorphism:
    Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
    For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():
"""

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive")

class Boat:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail")

class Plane:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly")

car1 = Car("Toyota","Supra")
boat1 = Boat("Mercedes","Double tacker")
plane1 = Plane("Emirates","Boieng 737")

for x in (car1,boat1,plane1):
    x.move()

"""
Output:
Drive
Sail
Fly
"""

"""
Inheritance Class Polymorphism:
What about classes with child classes with the same name? Can we use polymorphism there?
Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:
"""

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

class Car(Vehicle):
    def move(self):
        print("Move!")

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

"""
Output:
Ford
Mustang
Move!
Ibiza
Touring 20
Sail!
Boeing
747
Fly!
"""

class Vehicle:
    def max_speed(self):
        return "Speed varies"

class Car(Vehicle):
    def max_speed(self):
        return "Car speed: 180 km/h"

class Bike(Vehicle):
    def max_speed(self):
        return "Bike speed: 120 km/h"

car = Car()
bike = Bike()

print(car.max_speed())  
print(bike.max_speed())

"""
Output:
Car speed: 180 km/h
Bike speed: 120 km/h
"""