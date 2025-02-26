# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
"""
Output:
    Orange
    Banana
    Cherry
"""

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
"""
Output:
    Orange
    Orange
    Orange
"""
# Unpack a Collection (Only in List or Tuples)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
"""
Output:
    apple
    banana
    cherry
"""