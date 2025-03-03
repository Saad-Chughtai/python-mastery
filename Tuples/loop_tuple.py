# Loop Tuples
# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.

tuple = (1,2,3,4,5,6,7)
for x in tuple:
    print(x)

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
Loop Through the Index Numbers
You can also loop through the tuple items by referring to their index number.
Use the range() and len() functions to create a suitable iterable.
"""
tuple = (1,2,3,4,7)
for i in range(len(tuple)):
    print(tuple[i])

"""
Output:
1
2
3
4
7
"""

"""
Using a While Loop
You can loop through the tuple items by using a while loop.
Use the len() function to determine the length of the tuple,
Remember to increase the index by 1 after each iteration.
"""
tuple = (1,2,3,4,5,6,7,8,9,0)
i = 0
while i < len(tuple):
  print(tuple[i])
  i = i + 1

"""
Output:
1
2
3
4
5
6
7
8
9
0
"""