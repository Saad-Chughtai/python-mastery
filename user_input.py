# Python User Input

"""
User Input:
Python allows for user input.
That means we are able to ask the user for input.

The method is a bit different in Python 3.6 than Python 2.7.

Python 3.6 uses the input() method.
Python 2.7 uses the raw_input() method.
"""

username = input("Enter username:")
print("Your username is " + username)

# Python stops executing when it comes to the input() function, and continues when the user has given some input.

"""
Syntax:
variable name = input("Instructions / Message")
"""
username = input("Enter username:")
age = input("Enter Your age:")
city = input("Enter your city:")

print("Your username is " + username + ", your age is " + age + " and your city is " + city)

"""
Output:
Your username is Saad, your age is 20 and your city is Lahore
"""