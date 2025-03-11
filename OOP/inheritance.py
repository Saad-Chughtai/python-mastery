# Python Inheritance

"""
Python Inheritance:
    Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class:
    Parent class is the class being inherited from, also called base class.

Child class:
    Child class is the class that inherits from another class, also called derived class.
"""

"""
Create a Parent Class:
    Any class can be a parent class, so the syntax is the same as creating any other class:
"""

class Person:
     
    def __init__(self,fname,lname):
        self.fname =  fname
        self.lname =  lname

    def my_func(self):
        print(self.fname + self.lname)

# Use the Person class to create an object, and then execute the my_func method:

obj = Person("Saad"," Habib")
obj.my_func()

"""
Output:
Saad Habib
"""

"""
Create a Child Class:
    1.To create a class that inherits the functionality from another class, 
    send the parent class as a parameter when creating the child class:
"""

class Child(Person):
    pass

# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

# Now the Student class has the same properties and methods as the Person class.

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname   

    def print_func(self):
        print(self.fname + self.lname)

class Student(Person):
    pass

obj = Student("Saad"," Habib")
obj.print_func()

"""
Output:
Saad Habib
"""

"""
Add the __init__() Function:
So far we have created a child class that inherits the properties and methods from its parent.

We want to add the __init__() function to the child class (instead of the pass keyword).

Note: The __init__() function is called automatically every time the class is being used to create a new object.
"""

class Student(Person):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def print_func(self):
        print(self.fname + self.lname)
    
obj = Student("Saad"," Habib")
obj.print_func

"""
It will not show any output because,
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

Note: The child's __init__() function overrides the inheritance of the parent's __init__() function. 
"""

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self,fname,lname)
    
obj = Student("Saad" , "Habib")
obj.printname()

"""
Output:
Saad Habib
"""

# Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.

"""
Use the super() Function
    Python also has a super() function that will make the child class inherit all the methods and properties from its parent
"""

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

obj = Student("Saad", "Habib")
obj.printname()

"""
Output:
Saad Habib
"""

"""
By using the super() function, you do not have to use the name of the parent element, 
it will automatically inherit the methods and properties from its parent.
"""

# Add Properties
# Add a property called Birth year to the Student class:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.birthyear = 2003

obj = Student("Mike", "Olsen")
print(obj.birthyear)

"""
Output:
2003
"""

"""
In the example below, the year 2003 should be a variable, and passed into the Student class when creating student objects. 
To do so, add another parameter in the __init__() function:
"""

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname,year):
    super().__init__(fname, lname)
    self.admissionyear = year

obj = Student("Saad","Habib",2023)
print(obj.admissionyear)

"""
Output:
2023
"""

# Add Methods
#   You can also add a method in child class 

class Person:
    def __init__(self,fname,lname):
       self.fname = fname
       self.lname = lname
    def print_name(self):
       print(self.fname + self.lname)

class Student(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.admissionyear = year
    def wel(self):
       print("Welcome " + self.fname + self.lname + " to the batch of " + str(self.admissionyear))

obj = Student("Saad"," Habib",2023)
obj.wel()

"""
Output:
Welcome Saad Habib to the batch of 2023
"""

# If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.