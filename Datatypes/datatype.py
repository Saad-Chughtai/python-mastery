# Python Data Types
# Built-in Data Types
"""
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:
"""
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""


a = "Hello"
b = 5
c = 5.0
d = 1j
e = ["apple", "banana", "cherry"]
f = ("apple", "banana", "cherry")	
g = range(6)	
h = {"name" : "John", "age" : 36}	
i = {"apple", "banana", "cherry"}	
j = frozenset({"apple", "banana", "cherry"})	
k = True	
l = b"Hello"	
m = bytearray(5)	
n = memoryview(bytes(5))	
o = None	
print(a)
print(type(a))
"""
Output:
Hello
<class 'str'>
"""
print(b)
print(type(b))
"""
Output:
5
<class 'int'>
"""
print(c)
print(type(c))
"""
Output:
5.0
<class 'float'>
"""
print(d)
print(type(d))
"""
Output:
1j
<class 'complex'>
"""
print(e)
print(type(e))
"""
Output:
['apple', 'banana', 'cherry']
<class 'list'>
"""
print(f)
print(type(f))
"""
Output:
('apple', 'banana', 'cherry')
<class 'tuple'>
"""
print(g)
print(type(g))
"""
Output:
range(0, 6)
<class 'range'>
"""
print(h)
print(type(h))
"""
Output:
{'name': 'John', 'age': 36}
<class 'dict'>
"""
print(i)
print(type(i))
"""
Output:
{'banana', 'cherry', 'apple'}
<class 'set'>
"""
print(j)
print(type(j))
"""
Output:
frozenset({'banana', 'cherry', 'apple'})
<class 'frozenset'
"""
print(k)
print(type(k))
"""
Output:
True
<class 'bool'>
"""
print(l)
print(type(l))
"""
Output:
b'Hello'
<class 'bytes'>
"""
print(m)
print(type(m))
"""
Output:
bytearray(b'\x00\x00\x00\x00\x00')
<class 'bytearray'>
"""
print(n)
print(type(n))
"""
Output:
<memory at 0x0000020B343CCE80>
<class 'memoryview'>
"""
print(o)
print(type(o))
"""
Output:
None
<class 'NoneType'>
"""
# Setting the Specific Data Type
#If you want to specify the data type, you can use the following constructor functions:
"""
You need to write the name of variable then euqal sign(=) then write the datatyppe you want
e.g string data type (str) then in paranthesis write the value in this case it will be written
in qoutations marks
"""
x = str("20")
print(x)
print(type(x))
"""
Output:
20
<class 'str'>
"""
y = int(20)
print(y)
print(type(y))
"""
Output:
20
<class 'int'>
"""