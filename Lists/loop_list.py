    # Python - Loop Lists

# There are Four types of loop in list
    # 1. Loop Through a List using for loop 
    # 2. Loop Through the Index Numbers using range() and len()
    # 3. Using a While Loop
    # 4. Looping Using List Comprehension

# 1. Loop Through a List using for loop 
# You can loop through the list items by using a for loop:
# Print all items in the list, one by one:

list = ["Saad", "Jackie", "Talha"]
for x in list:
  print(x)

"""
Output:
Saad
Jackie
Talha
"""

# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable

# Print all items by referring to their index number:
list = [1,2,3,4]
for i in range(len(list)):
  print(list[i])

"""
Output:
1
2
3
4
"""

    # 3. Using a While Loop
"""
You can loop through the list items by using a while loop.
Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
Remember to increase the index by 1 after each iteration.
"""
list = ["why","who","how","whom"]
i = 0
while i < len(list):
  print(list[i])
  i = i+1

"""
Output:
why
who
how
whom
"""

    # 4. Looping Using List Comprehension
#   It offers the shortest syntax for looping through lists:

list = ["Saad", "Jackie", "Talha"]
[print(y) for y in list]

"""
Output:
Saad
Jackie
Talha
"""