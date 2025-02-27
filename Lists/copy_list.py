    # Python - Copy Lists
# There are several ways to copy the list
         # 1. By using the copy method  { copy() }
         # 2. By using the list method { list() }
         # 3. By using the slice Operator (:)

# 1.Using the copy method  { copy() }
# You can use the built-in List method copy() to copy a list.
rlist = [1,2,3,4,5,6,7]
newlist =rlist.copy()
print(newlist)

"""
Output:
[1, 2, 3, 4, 5, 6, 7]
"""

     # 2. By using the list method { list() }
# Another way to make a copy is to use the built-in method list().

thlist = [1,2,3,4,5,6,7,8,9,10]
mylist = list(thlist)
print(mylist)

"""
Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

         # 3. By using the slice Operator (:)
# You can also make a copy of a list by using the : (slice) operator.

rlist = [1,2,3,4,5,6,7]
newlist =rlist[:]
print(newlist)

"""
Output:
[1, 2, 3, 4, 5, 6, 7]
"""