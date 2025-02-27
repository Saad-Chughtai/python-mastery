# Python - Change List Items
# Change Item Value
# To change the value of a specific item, refer to the index number:

# Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

"""
Output:
['apple', 'blackcurrant', 'cherry']
"""

# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values, 
# and refer to the range of index numbers where you want to insert the new values:

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

"""
Output:
['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
"""

list = ["apple", "banana", "cherry"]
list[1:2] = ["blackcurrant", "watermelon"]

# This is will change the index 1 and add watermelon but the last index(2) remains same as 
# Note: The length of the list will change when the number of items inserted does not match the number of items replaced.

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
"""
Output:
['apple', 'watermelon']
"""

"""
Why does this happen?
1. Thislist[1:3] = ["watermelon"] means replace elements at index 1 and 2 ("banana", "cherry") with ["watermelon"].
2. The slice 1:3 selects ["banana", "cherry"], which will be replaced entirely by the new list ["watermelon"].
3. Since ["watermelon"] contains only one element, it replaces both "banana" and "cherry", reducing the list size.
"""

# Inset items
"""
To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index:
"""
list = ["apple", "banana", "cherry"]
list.insert(3, "watermelon")
print(list)

"""
Output:
['apple', 'banana', 'cherry', 'watermelon']
"""