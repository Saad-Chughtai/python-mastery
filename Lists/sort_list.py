# Python - Sort Lists
# There are Five ways to sort the list
    # 1. Sort List Alphanumerically (ascending) use sort() method
    # 2. Sort Descending (use the keyword argument reverse = True)
    # 3. Customize Sort Function
    # 4. Case Insensitive Sort
    # 4. Reverse Order (use reverse() method)

# 1. Sort List Alphanumerically (ascending) use sort() method
    # List have the Builtin function to sort it ascending by default

list = [1,7,12,434,2,5,7,1,88]
list.sort()
print(list)

"""
Output:
[1, 1, 2, 5, 7, 7, 12, 88, 434]
"""

list = ["CR7","Benzema","Marcelo"]
list.sort()
print(list)

"""
Output:
['Benzema', 'CR7', 'Marcelo']
"""

    # 2. Sort Descending 
# To sort descending, use the keyword argument reverse = True:
list = ["CR7","Benzema","Marcelo"]
list.sort(reverse = True)
print(list)

"""
Output:
['Marcelo', 'CR7', 'Benzema']
"""

list = [1,7,12,434,2,5,7,1,88]
list.sort(reverse=True)
print(list)

"""
Output:
[434, 88, 12, 7, 7, 5, 2, 1, 1]
"""

    # 3. Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):

# Sort the list based on how close the number is to 50:

def func(n):
  return abs(n-40)

list = [1,30,20,40,50,100,32]
list.sort(key=func)
print(list)

"""
Output:
[40, 32, 30, 50, 20, 1, 100]
"""

    # 4. Case Insensitive Sort
# By default sort method is case sensitive (resulting in all capital letters being sorted before lower case letters)

# Case sensitive sorting can give an unexpected result:

thislist = ["saad", "Talha", "Jack", "jackie","Zoro"]
thislist.sort()
print(thislist)

"""
Output:
['Jack', 'Talha', 'Zoro', 'jackie', 'saad']

jackie should be place at 2nd position but due case sesitive it priotize capital letters first
"""


# So if you want a case-insensitive sort function, use str.lower as a key function in sort method
list = ["saad", "Talha", "Jack", "jackie","Zoro"]
list.sort(key=str.lower)
print(list)

"""
Output:
['Jack', 'jackie', 'saad', 'Talha', 'Zoro']
"""

    # 5.Reverse Order
# The reverse() method reverses the current sorting order of the elements.

list = ["saad", "Talha", "Jack", "jackie","Zoro"]
list.reverse()
print(list)

"""
Output:
['Zoro', 'jackie', 'Jack', 'Talha', 'saad']
"""