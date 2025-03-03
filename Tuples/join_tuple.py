# Python - Join Tuples

# Join two tuples
# To join two or more tuples you can use the + operator:

tuple1 = (1,2,3,4,5)
tuple2 = (0,9,8,7,6)
tuple1 += tuple2
print(tuple1)

"""
Output:
(1, 2, 3, 4, 5, 0, 9, 8, 7, 6)
"""

# Multiply tuple
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:

tuple = ("saad","Cat","Talha","Wolf")
tuple2 = tuple* 2
print(tuple2)

"""
Output:
('saad', 'Cat', 'Talha', 'Wolf', 'saad', 'Cat', 'Talha', 'Wolf')
"""