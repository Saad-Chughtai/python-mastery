# Python - Remove List Items

# There are Four ways to remove the item from the list
    # 1. By using the remove function { remove() }
    # 2. By using the pop function { pop() }
    # 3. By using the del keyword (del)
    # 4. By using the clear function { clear() }

# 1. By using the remove function { remove() }
list = [1,2,3,4,5]
list.remove(4)
print(list)
"""
Output:
[1, 2, 3, 5]
"""

# If there is duplicate of anything it will del the first occuerence 
list = [1,2,3,4,5,4]
list.remove(4)
print(list)
"""
Output:
1, 2, 3, 5, 4]
"""

# 2. By using the pop function { pop() }
# The pop function use the indexes to del the item

num = [1,2,3,4,5,6]
num.pop(1)
print(num)
"""
Output:
[1, 3, 4, 5, 6]
"""
# If you do not specify the index, the pop() method removes the last item.
num = [1,2,3,4,5,6]
num.pop()
print(num)

"""
Output:
[1, 3, 4, 5, 6]
"""

# 3. By using the del keyword (del)
# del keyword is use to del the complete list

num = [1,2,3,5,6]
del num

# The del keyword can also removes the specified index:

num = [1,2,3,5,6]
del num[0]
print(num)
"""
Output:
[2, 3, 5, 6]
"""

# 4. By using the clear function { clear() }
# The clear() method empties the list.
# The list still remains, but it has no content.

num = [0,9,8,9,]
num.clear()
print(num)

"""
Output:
[]
"""