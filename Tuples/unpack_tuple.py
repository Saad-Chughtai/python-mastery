# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

tuple =(1,2,3,4,5)

# But, in Python, we can also extract the values back into variables. This is called "unpacking":
(a,b,c,d,e) = tuple
print(a)
print(b)
print(c)
print(d)
print(e)

"""
Output:
1
2
3
4
5
"""

# while unpacking the number of variables should match the no of items,
# if not you must use the asterick to collect the remaining values as a list.

tuple = ("saad","talha","cat")
(n,*m) = tuple
print(n)
print(m)

"""
Output:
saad
['talha', 'cat']
"""

# If you add the asterick to the middle one python will assigned all the values except the last on to that variable
tuple = ("saad","talha", "cat", "loin","wolf")
(a,b,*c,d)  = tuple
print(a)
print(b)
print(c)
print(d)

"""
Output:
saad
talha
['cat', 'loin']
wolf
"""

# If you want to ignore some items you can use (_)
# you can place (_) for each item you want to ignore or use asterick before (_)
tuple = ("saad","talha", "cat", "loin","wolf")
(a, *_,d)  = tuple
print(a)
print(d)

"""
Output:
saad
wolf
"""
