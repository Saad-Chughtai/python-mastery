# Python For Loops

"""
Python For Loops:
    1.A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
    2.This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
    3.With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""

ani = ["cat","dog","loin"]
for x in ani:
    print(x)

"""
Output:
cat
dog
loin
"""

# The for loop does not require an indexing variable to set beforehand.

"""
Looping Through a String:
    Even strings are iterable objects, they contain a sequence of characters:
"""
for x in "Mango":
    print(x)

"""
Output:
M
a
n
g
o
"""

"""
The break Statement:
    With the break statement we can stop the loop before it has looped through all the items:
"""
name = ["saad","Talha","jack"]
for x in name:
    print(x)
    if x == "Talha":
        break

"""
Output:
saad
Talha
"""

name = ["saad","Talha","jack"]
for x in name:
  if x == "Talha":
    break
  print(x)

"""
Output:
saad
"""

"""
The continue Statement:
    With the continue statement we can stop the current iteration of the loop, and continue with the next:
"""
name = ["saad","Talha","jack","Mano"]
for x in name:
   if x == "jack":
      continue
print(x)  

"""
Output:
Talha
saad
Mano
"""


"""
The range() Function:
    1.To loop through a set of code a specified number of times, we can use the range() function,
    2.The range() function returns a sequence of numbers, starting from 0 by default, 
    and increments by 1 (by default), and ends at a specified number.
"""

for x in range(8):
   print(x)
print("sssssssssss")
"""
Output:
0
1
2
3
4
5
6
7
"""

"""
Note that range() is not the values of 0 to 8, but the values 0 to 7.

The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 8), 
which means values from 2 to 8 (but not including 8)
"""

for x in range(2,8):
    print(x)

"""
Output:
2
3
4
5
6
7
"""

"""
The range() function defaults to increment the sequence by 1, 
however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

This will starts from 2 untill it reaches the 30 by the increment of 3 after each itreation
"""

for x in range(2,30,3):
   print(x)

"""
Output:
2
5
8
11
14
17
20
23
26
29
"""

"""
Else in For Loop:
    The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
"""

for x in range(6):
   print(x)

else:
   print("Reached the limit")

"""
Output:
0
1
2
3
4
5
Reached the limit
"""

# Note: The else block will NOT be executed if the loop is stopped by a break statement.

for x in range(6):
  if x == 3: break
  print(x)
else:
   print("Reached the limit")

"""
Output:
0
1
2
"""

"""
Nested Loops:
    1.A nested loop is a loop inside a loop.
    2.The "inner loop" will be executed one time for each iteration of the "outer loop":
"""
ani1 = ["Cat","Dog","Loin"]
ani2 = ["Rabbit","Cow","Goat"]
for x in ani1:
   for y in ani2:
      print(x,y)

"""
Output:
Cat Rabbit
Cat Cow
Cat Goat
Dog Rabbit
Dog Cow
Dog Goat
Loin Rabbit
Loin Cow
Loin Goat
"""

"""
The pass Statement:
    1.The pass statement is used as a placeholder when a block of code is required syntactically but you don’t want to execute any instructions.
    2.It helps to avoid syntax errors when you are planning to implement the loop logic later.
"""

for x in range(6):
   pass # Will add logic late

