# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets:

tuple = ("Saad","Talha","Jack","Jackie","Cat")
print(tuple[1])

"""
Output:
Talha
"""

# Negative indexex

tuple = ("Saad","Talha","Jack","Jackie","Cat")
print(tuple[-2])

"""
Output:
Jackie
"""

# Range of Indexex

tuple = ("Saad","Talha","Jack","Jackie","Cat")
print(tuple[1:3])

"""
Output:
('Talha', 'Jack')
"""

# If you leave the starting value, it starts from 0 index

tuple = (1,2,3,4,5,6,7,8,9)
print(tuple[:6])

"""
Output:
(1, 2, 3, 4, 5, 6)
"""

# If you leave the ending value it will move till end

tuple = (1,2,3,4,5,6,7,8,9)
print(tuple[1:])

"""
Output:
(2, 3, 4, 5, 6, 7, 8, 9)
"""

# Range of negative indexex
# Specify negative indexes if you want to start the search from the end of the tuple:



tuple = ("Saad","Talha","Jack","Jackie","Cat")
print(tuple[-4:-1])

"""
Output:
('Talha', 'Jack', 'Jackie')
"""

# If you leave the starting value, it starts from 0 index

tuple = (1,2,3,4,5,6,7,8,9)
print(tuple[:-6])

"""
Output:
(1, 2, 3)
"""

# If you leave the ending value it will move till end

tuple = (1,2,3,4,5,6,7,8,9)
print(tuple[-1:])

"""
Output:
(9,)
"""

# Check if the item exists
# To check the item we use the keyword (in) 
# Check cat is present in the tuple or not?

tuple = ("Saad","Talha","Jack","Jackie","Cat")
if "Cat" in tuple:
    print("yes")
else:
    print("No")

"""
Output:
yes
"""