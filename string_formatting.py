"""
Python String Formatting:
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

Before Python 3.6 we had to use the format() method.
"""

"""
F-Strings
F-string allows you to format selected parts of a string.
To specify a string as an f-string, simply put an f in front of the string literal, like this:
"""
x = f"Hello my name is saad"
print(x)

"""
Output:
Hello my name is saad
"""

"""
Placeholders and Modifiers:
    1.To format values in an f-string, add placeholders {}, 
    a placeholder can contain variables, operations, functions, and modifiers to format the value.
"""
name = "Saad"
x = f"Hello my name is {name} "
print(x)

"""
Output:
Hello my name is Saad
"""

"""
A placeholder can also include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal formatting type, 
like .2f which means fixed point number with 2 decimals:
"""

age = 20
x = f"My Age is {age:.2f} years"
print(x)

"""
Output:
My Age is 20.00 years
"""

# You can also format a value directly without keeping it in a variable:

x = f"The price is {95:.2f} dollars"
print(x)

"""
Output:
The price is 95.00 dollars
"""

"""
Perform Operations in F-Strings:
    You can perform Python operations inside the placeholders.
    You can do math operations:
"""

# Perform a math operation in the placeholder, and return the result:

x = f"The price of appel is {2 * 5} Dollars"
print(x)

"""
Output:
The price of appel is 10 Dollars
"""

# You can perform math operations on variables:

# Add taxes before displaying the price:
price = 20
tax = 0.05

x = f"The total price of appels is {price + (price * tax)} dollars"
print(x)

"""
Output:
The total price of appel is 21.0 dollars
"""

# You can perform if...else statements inside the placeholders:

# Return "Expensive" if the price is over 50, otherwise return "Cheap":

price = 49
x = f"The price of oranges is {price} dollars"
if price > 50:
    print("Expensive")
else:
    print("Cheap")

"""
Cheap
"""

# Or

price = 49
x = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(x)

"""
Output:
It is very Cheap
"""

"""
Execute Functions in F-Strings:
You can execute functions inside the placeholder:
"""

# Use the string method upper()to convert a value into upper case letters:

Name = "Saad"
x = f"My name is {Name.upper()}"
print(x)

"""
Output:
My name is SAAD
"""

# The function does not have to be a built-in Python method, you can create your own functions and use them:

# Create a function that converts feet into meters:

def myconverter(x):
  return x * 0.3048

x = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(x)

"""
Output:
The plane is flying at a 9144.0 meter altitude
"""

"""
More Modifiers
At the beginning of this chapter we explained how to use the .2f modifier to format a number into a fixed point number with 2 decimals.

There are several other modifiers that can be used to format values:
"""

# Use a comma as a thousand separator:

price = 59000
x = f"The price is {price:,} dollars"
print(x)

"""
Output:
The price is 59,000 dollars
"""

"""
Here is a list of all the formatting types.

Formatting      Types
:<		        Left aligns the result (within the available space)
:>		        Right aligns the result (within the available space)
:^		        Center aligns the result (within the available space)
:=		        Places the sign to the left most position
:+		        Use a plus sign to indicate if the result is positive or negative
:-		        Use a minus sign for negative values only
: 		        Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,		        Use a comma as a thousand separator
:_		        Use a underscore as a thousand separator
:b		        Binary format
:c		        Converts the value into the corresponding Unicode character
:d		        Decimal format
:e		        Scientific format, with a lower case e
:E		        Scientific format, with an upper case E
:f		        Fix point number format
:F		        Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		        General format
:G		        General format (using a upper case E for scientific notations)
:o		        Octal format
:x		        Hex format, lower case
:X		        Hex format, upper case
:n		        Number format
:%		        Percentage format
"""

"""
String format():
    Before Python 3.6 we used the format() method to format strings.
    The format() method can still be used, but f-strings are faster and the preferred way to format strings.
    The next examples in this page demonstrates how to format strings with the format() method.
    The format() method also uses curly brackets as placeholders {}, but the syntax is slightly different:
"""

# Add a placeholder where you want to display the price:

price = 20
x = "My Age is {} Years"
print(x.format(price))

"""
My Age is 20 Years
"""

# You can add parameters inside the curly brackets to specify how to convert the value:

price = 49
x = "The price is {:.2f} dollars"
print(x.format(price))

"""
Definition and Usage:
    The format() method formats the specified value(s) and insert them inside the string's placeholder.
    The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.
    The format() method returns the formatted string.
"""

"""
Syntax
string.format(value1, value2...)
"""

"""
Parameter Values
Parameter	        Description
value1, value2...	Required. One or more values that should be formatted and inserted in the string.   
                    The values are either a list of values separated by commas, a key=value list, or a combination of both.

                    The values can be of any data type.
"""

"""
The Placeholders:
    The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.
"""

"""
Formatting Types:
Inside the placeholders you can add a formatting type to format the result:

:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
:b		Binary format
:c		Converts the value into the corresponding unicode character
:d		Decimal format
:e		Scientific format, with a lower case e
:E		Scientific format, with an upper case E
:f		Fix point number format
:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%		Percentage format

"""

"""
Multiple Values:
If you want to use more values, just add more values to the format() method:
"""

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

"""
Output:
I want 3 pieces of item number 567 for 49.00 dollars.
"""

"""
Index Numbers:
    1.You can use index numbers (a number inside the curly brackets {0}) 
    to be sure the values are placed in the correct placeholders:
"""

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

"""
Output:
I want 3 pieces of item number 567 for 49.00 dollars.
"""

# Also, if you want to refer to the same value more than once, use the index number:

age = 20
name = "Saad"
x = "His name is {1}. {1} is {0} years old."
print(x.format(age, name))

"""
Output:
His name is Saad. Saad is 20 years old.
"""

"""
Named Indexes
    1.You can also use named indexes by entering a name inside the curly brackets {car_name}, 
    but then you must use names when you pass the parameter values txt.format(car_name = "Toyota"):
"""
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Supra", model = "Toyota"))

"""
Output:
I have a Supra, it is a Toyota.
"""