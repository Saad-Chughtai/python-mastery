# Python JSON

"""
JSON is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation.
"""

"""
JSON in Python:
    Python has a built-in package called json, which can be used to work with JSON data.
"""

"""
Import the json module:
"""
import json

"""
Parse JSON - Convert from JSON to Python:
    If you have a JSON string, you can parse it by using the json.loads() method.

The result will be a Python dictionary.
"""

import json

# some JSON:
x =  '{ "name":"Saad", "age":20, "city":"Lahore"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

"""
Putput:
20
"""

"""
Convert from Python to JSON:
    If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
"""

# a Python object (dict):
x = {
  "name": "Saad",
  "age": 20,
  "city": "Lahore"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

"""
Output:
{"name": "Saad", "age": 20, "city": "Lahore"}
"""

"""
You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None
"""

print(json.dumps({"name":"Saad","age":20}))
print(json.dumps(["Cat","Wolf","Loin"]))
print(json.dumps(("Cat","Wolf")))
print(json.dumps("Hello"))
print(json.dumps(7))
print(json.dumps(15.2))
print(json.dumps(False))
print(json.dumps(None))

"""
Outputs:
{"name": "Saad", "age": 20}
["Cat", "Wolf", "Loin"]
["Cat", "Wolf"]
"Hello"
7
15.2
false
null
"""

# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

"""
Python	        JSON
dict	        Object
list	        Array
tuple	        Array
str	            String
int	            Number
float	        Number
True	        true
False	        false
None	        null
"""

data = {
    "name":"Saad",
    "age":20,
    "married": False,
    "studing": True,
    "hobby":("Gaming","Football"),
    "Pets":"Cat",
    "car": None,
    "bike":[
        {
        "brand":"Honda",
        "Model":"CD70",
        "year":2023,
        },
        {
        "brand":"Honda",
        "Model":"CD70",
        "year":2015
    }
    ]
}
print(json.dumps(data))

"""
Output:
{"name": "Saad", "age": 20, "married": false, "studing": true, "hobby": ["Gaming", "Football"], "Pets": "Cat", "car": null, "bike": [{"brand": "Honda", "Model": "CD70", "year": 2015}]}
"""

"""
Format the Result
The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

The json.dumps() method has parameters to make it easier to read the result:
"""

# Use the indent parameter to define the numbers of indents:

# use four indents to make it easier to read the result:
print(json.dumps(data, indent=4))

"""
Output:
{
    "name": "Saad",
    "age": 20,
    "married": false,
    "studing": true,
    "hobby": [
        "Gaming",
        "Football"
    ],
    "Pets": "Cat",
    "car": null,
    "bike": [
        {
            "brand": "Honda",
            "Model": "CD70",
            "year": 2023
        },
        {
            "brand": "Honda",
            "Model": "CD70",
            "year": 2015
        }
    ]
}
"""

# You can also define the separators, default value is (", ", ": "), 
# which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

# Use the separators parameter to change the default separator:

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:

print(json.dumps(data, indent=4, separators=(". ", " = ")))

"""
Output:
{
    "name" = "Saad".
    "age" = 20.
    "married" = false.
    "studing" = true.
    "hobby" = [
        "Gaming".
        "Football"
    ].
    "Pets" = "Cat".
    "car" = null.
    "bike" = [
        {
            "brand" = "Honda".
            "Model" = "CD70".
            "year" = 2023
        }.
        {
            "brand" = "Honda".
            "Model" = "CD70".
            "year" = 2015
        }
    ]
}
"""

"""
Order the Result
The json.dumps() method has parameters to order the keys in the result:

Use the sort_keys parameter to specify if the result should be sorted or not:
"""

# sort the result alphabetically by keys:

print(json.dumps(x, indent=4, sort_keys=True))

"""
Output:
{
    "name" = "Saad".
    "age" = 20.
    "married" = false.
    "studing" = true.
    "hobby" = [
        "Gaming".
        "Football"
    ].
    "Pets" = "Cat".
    "car" = null.
    "bike" = [
        {
            "brand" = "Honda".
            "Model" = "CD70".
            "year" = 2023
        }.
        {
            "brand" = "Honda".
            "Model" = "CD70".
            "year" = 2015
        }
    ]
}
{
    "age": 20,
    "city": "Lahore",
    "name": "Saad"
}
"""