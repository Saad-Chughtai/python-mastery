# Python - Access List Items

# How can we Access the list items
     # List items are indexed and you can access them by referring to the index number:
     # Indexes starts from 0 (like in array)
        # There are four types of indexing
            # 1.Simple Indexing
            # 2.Negative Indexing
            # 3.Range of Indexes
            # 4.Range of Negative Indexes

# Example of Simple Indexing
list = ["Hello",12,"BYE"]
print(list[1])

"""
Output:
12
"""

# Example of Negative indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.

list = ["Hello",12,"BYE"]
print(list[-1])
"""
Output:
BYE
"""

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included

"""
Output:
['cherry', 'orange', 'kiwi']
"""

fruits = ["apple","banana","orange","Mango","Pineapple","Strawberry"]
print(fruits[2:5])

"""
Output:
['orange', 'Mango', 'Pineapple']
"""
# By leaving out the start value, the range will start at the first item:

fruit = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruit[:4])

#This will return the items from index 0 to index 4.

#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included
"""
Output:
['apple', 'banana', 'cherry', 'orange']
"""

# By leaving out the end value, the range will go on to the end of the list:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#This will return the items from index 2 to the end.
#Remember that index 0 is the first item, and index 2 is the third
"""
Output:
['cherry', 'orange', 'kiwi', 'melon', 'mango']
"""

# Range of negative indexes
# Specify negative indexes if you want to start the search from the end of the list:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Negative indexing means starting from the end of the list.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,
"""
Output:
['orange', 'kiwi', 'melon']
"""

# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
list = [12,10,3,4]
if 12 in list:
    print("Yes 12 is in the list")

"""
Output:
Yes 12 is in the list
"""