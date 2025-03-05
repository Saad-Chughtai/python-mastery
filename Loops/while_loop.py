# Python While Loops

"""
Python Loops:
    Python has two primitive loop commands:
            1.while loops
            2.for loops
"""

"""
The while Loop
With the while loop we can execute a set of statements as long as a condition is true.
"""

i = 1
while i < 6:
  print(i)
  i += 1

"""
Output:
1
2
3
4
5
"""

# Note: remember to increment i, or else the loop will continue forever.
# The while loop requires relevant variables to be ready, so we need to define an indexing variable, i, which we set to 1.

"""
The break Statement
With the break statement we can stop the loop even if the while condition is true:

we use break statement when we want to stop the loop 
"""

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

"""
Output:
1
2
3
"""

"""
The continue Statement:
    With the continue statement we can stop the current iteration, and continue with the next:
    we use continue statement when we want to skip the iteration
"""
i = 0
while i < 5:
  i +=1
  if i == 4:
    continue
  print(i)

"""
Output:
1
2
3
5
"""

"""
The else Statement:
    With the else statement we can run a block of code once when the condition no longer is true:
"""
i = 1
while i < 9:
  print(i)
  i = i+1
else:
  print("i is no longer greater than 9")

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
i is no longer greater than 9
"""