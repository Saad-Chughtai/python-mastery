# Python Iterators

"""
Iterators:
    1.An iterator is an object that contains a countable number of values.
    2.An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
    3.Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
"""

"""
Iterator vs Iterable
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
All these objects have a iter() method which is used to get an iterator:
"""

my_tuple = ("Wolf", "Cat", "Loin")
myit = iter(my_tuple)

print(next(myit))
print(next(myit))
print(next(myit))

"""
Output:
Wolf
Cat
Loin
"""

str = "Saad"
my_it = iter(str)

print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))

"""
Output:
S
a
a
d
"""

"""
Looping Through an Iterator:
    We can also use a for loop to iterate through an iterable object
"""

my_tuple = ("Wolf", "Cat", "Loin")
for x in my_tuple:
    print(x)

"""
Output:
Wolf
Cat
Loin
"""

# Iterate the characters of a string:

str = "Saad"
for x in str:
    print(x)

"""
Output:
S
a
a
d
"""
# The for loop actually creates an iterator object and executes the next() method for each loop.

"""
Create an Iterator:
    1.To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
    2.As we know all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
    3.The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
    4.The __next__() method also allows you to do operations, and must return the next item in the sequence.
"""

class my_numbers:
    def __iter__(self):
        self.a = 1 # Starting condition
        return self
    def __next__(self):
        x = self.a
        self.a += 1 # Next Iteration
        return x
    
my_var = my_numbers()
myiter = iter(my_var)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
"""
Output:
1
2
3
4
5
6
7
"""

"""
StopIteration:
    1.The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
    2.To prevent the iteration from going on forever, we can use the StopIteration statement.
    3.In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
"""

class my_numbers:
    def __iter__(self):
        self.a = 1        # Starting value
        return self
    
    def __next__(self):
        if self.a <= 10:  # Condition to meet
            x = self.a
            self.a +=1    # Value of iteration
            return x
        else:
            raise StopIteration
        
my_var = my_numbers()
myiter = iter(my_var)

for x in myiter:
    print (x)

"""
Output:
1
1
2
3
4
5
6
7
8
9
10
"""

