# Python Classes and Objects

"""
Python Classes/Objects:
    1.Python is an object oriented programming language.
    2.Almost everything in Python is an object, with its properties and methods.
    3.A Class is like an object constructor, or a "blueprint" for creating objects.
"""

"""
Create a Class:
    To create a class, use the keyword class
"""

class MyClass:
    num = 5

print(MyClass)

"""
Output:
<class '__main__.my_class'>
"""

"""
Create Object:
    Now we can use the class named MyClass to create objects:
"""

obj = MyClass()
print(obj.num)

"""
Output:
5
"""


"""
The __init__() Function:
    1.To understand the meaning of classes we have to understand the built-in __init__() function.
    2.All classes have a function called __init__(), which is always executed when the class is being initiated.
    3.Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
"""

# Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
   def __init__(self,name,age):
    self.name = name
    self.age = age

obj = Person("Saad",20)

print(obj.name)
print(obj.age)

"""
Output:
Saad
20
"""

# Note: The __init__() function is called automatically every time the class is being used to create a new object.

"""
The __str__() Function:
    1.The __str__() function controls what should be returned when the class object is represented as a string.
    2.If the __str__() function is not set, the string representation of the object is returned:
"""

# The string representation of an object WITHOUT the __str__() function:

class Person:
   def __init__(self,name,age):
      self.name = name
      self.age = age 

obj = Person("Saad",20)

print(obj)

"""
Output:
<__main__.Person object at 0x0000014F691AA7E0>
"""

# The string representation of an object WITH the __str__() function:

class Person:
   def __init__(self,name,age):
    self.name = name
    self.age = age
   def __str__(self):
       return f"{self.name}({self.age})"

obj = Person("Saad",20)

print(obj)

"""
Output:
Saad(20)
"""

"""
Object Methods:
    Objects can also contain methods. Methods in objects are functions that belong to the object.
"""

class Person:
    def __init__(self, name):
        self.name = name

    def my_func(self): 
        print("Hello, my name is " + self.name )

obj = Person("Saad")
obj.my_func()  

"""
Output:
Hello, my name is Saad
"""

# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

"""
The self Parameter:
    1.The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
    2.It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:
"""

class Person:
    def __init__(info, name, age):
      info.name = name
      info.age = age

    def __str__(pers):
       return f"{pers.name}({pers.age})"

obj = Person("Saad",20)

print(obj)

"""
Output:
Saad(20)
"""

"""
Modify Object Properties:
    You can modify properties on objects like this
"""

class Person:
    def __init__(self,name,age):
      self.name = name
      self.age = age
    def __str__(self):
        return "Hello, my name is " + self.name + " and my age is " + str(self.age)

obj = Person("Saad",19)

print(obj) # Before Modify

"""
Output:
Hello, my name is Saad and my age is 19
"""

obj.age = 20

print(obj) # After Modify

"""
Hello, my name is Saad and my age is 20
"""

"""

Delete Object Properties:
    You can delete properties on objects by using the del keyword:
"""

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def my_func(self):
        print("Hello my Name is " + self.name + " And my Age is " + str(self.age))

obj = Person("Saad",20)
obj.my_func() # Before Delete

"""
Output:
Hello my Name is Saad And my Age is 20
"""

del obj.age
obj.my_func() # After Delete

"""
    print("Hello my Name is " + self.name + " And my Age is " + str(self.age))
                                                                    ^^^^^^^^
AttributeError: 'Person' object has no attribute 'age'
"""

"""
Delete Objects:
    You can delete objects by using the del keyword:
"""

class Person:
    def  __init__(self,name):
        self.name = name

    def my_func(self):
       print("Hello my Name is " + self.name)

obj = Person("Saad")
obj.my_func() # Before Delete

"""
Output:
Hello my Name is Saad
"""

del obj
print(obj)

"""
Output:
    print(obj)
          ^^^
NameError: name 'obj' is not defined
"""

"""
The pass Statement:
    1.class definitions cannot be empty, but if you for some reason have a class definition with no content, 
    put in the pass statement to avoid getting an error.
"""

class Person:
   pass

# having an empty class definition like this, would raise an error without the pass statement