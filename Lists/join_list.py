    # Python - Join Lists
# Three ways to join the list
    # 1.By using the + operator
    # 2.By using the append function
    # 3.By using the sxtend function

# 1.By using the + operator
# while using the + operator you need to create a new list to add two lists

list1 = [1,2,3,4]
list2 = [5,6,7,8,9]
list3 = list1 + list2
print(list3)

"""
Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

    # 2.By using the append function
list1 = ["a","b","c"]
list2 = [5,6,7]

for x in list1:
    list2.append(x)
    print (list2)

"""
Output:
[5, 6, 7, 'a']
[5, 6, 7, 'a', 'b']
[5, 6, 7, 'a', 'b', 'c']
"""

    # 3.By using the sxtend function
# where the purpose is to add elements from one list to another list:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

"""
Output:
['a', 'b', 'c', 1, 2, 3]
"""