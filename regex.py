# Python RegEx

"""
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.

RegEx Module:
Python has a built-in package called re, which can be used to work with Regular Expressions.
"""

# Import the re module:

import re

"""
RegEx in Python:
    When you have imported the re module, you can start using regular expressions:
"""

# Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

"""
Output:
YES! We have a match!
"""

"""
RegEx Functions:
    The re module offers a set of functions that allows us to search a string for a match:

Function	        Description
findall	            Returns a list containing all matches
search	            Returns a Match object if there is a match anywhere in the string
split	            Returns a list where the string has been split at each match
sub	                Replaces one or many matches with a string
"""

"""
Metacharacters:
Metacharacters are characters with a special meaning:

Character	    Description	                                        Example	
[]	            A set of characters	                                "[a-m]"	
\	            Signals a special sequence 
                (can also be used to escape special characters)	    "\d"	
.	            Any character (except newline character)	        "he..o"	
^	            Starts with	                                        "^hello"	
$	            Ends with	                                        "planet$"	
*	            Zero or more occurrences	                        "he.*o"	
+	            One or more occurrences	                            "he.+o"	
?	            Zero or one occurrences	                            "he.?o"	
{}	            Exactly the specified number of occurrences	        "he.{2}o"	
|	            Either or	                                        "falls|stays"	
()	            Capture and group
"""

"""
Special Sequences:
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

Character	            Description	                                                                Example	
\A	                Returns a match if the specified characters 
                    are at the beginning of the string	                                            "\AThe"
\b	                Returns a match where the specified characters 
                    are at the beginning or at the end of a word                                    r"\bain"
                    (the "r" in the beginning is making sure that the string 
                    is being treated as a "raw string")                                             r"ain\b"
\B	                Returns a match where the specified characters are present, 
                    but NOT at the beginning (or at the end) of a word                              r"\Bain"
                    (the "r" in the beginning is making sure that the string is 
                    being treated as a "raw string")                                                r"ain\B"
\d	                Returns a match where the string 
                    contains digits (numbers from 0-9)	                                            "\d"      
\D	                Returns a match where the string DOES NOT contain digits	                    "\D"	
\s	                Returns a match where the string contains a white space character	            "\s"	
\S	                Returns a match where the string DOES NOT contain a white space character	    "\S"	
\w	                Returns a match where the string contains any word characters 
                    (characters from a to Z, digits from 0-9, and the underscore _ character)	    "\w"	
\W	                Returns a match where the string DOES NOT contain any word characters	        "\W"	
\Z	                Returns a match if the specified characters are at the end of the string	    "Spain\Z"     
"""

"""
Sets:
A set is a set of characters inside a pair of square brackets [] with a special meaning:

Set	        Description	
[arn]	    Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	    Returns a match for any lower case character, alphabetically between a and n	
[^arn]	    Returns a match for any character EXCEPT a, r, and n	
[0123]	    Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	    Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	        In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
"""

"""
The findall() Function:
The findall() function returns a list containing all matches.
"""

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

"""
Output:
['ai', 'ai']
"""

"""
The list contains the matches in the order they are found.
If no matches are found, an empty list is returned:
"""
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

"""
Output:
[]
"""

"""
The search() Function
The search() function searches the string for a match, and returns a Match object if there is a match.
If there is more than one match, only the first occurrence of the match will be returned:
"""

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 

"""
Output:
The first white-space character is located in position: 3
"""

# If no matches are found, the value None is returned:
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

"""
Output:
None
"""

"""
The split() Function:
The split() function returns a list where the string has been split at each match:
"""

# Split at each white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

"""
Output:
['The', 'rain', 'in', 'Spain']
"""

# You can control the number of occurrences by specifying the maxsplit parameter:

# Split the string only at the first occurrence:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

"""
Output:
['The', 'rain in Spain']
"""

"""
The sub() Function:
The sub() function replaces the matches with the text of your choice:
"""
# Replace every white-space character with the number 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

"""
Output:
The9rain9in9Spain
"""

# You can control the number of replacements by specifying the count parameter:
# Replace the first 2 occurrences:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

"""
Output:
The9rain9in Spain
"""

"""
Match Object:
A Match Object is an object containing information about the search and the result.

Note: If there is no match, the value None will be returned, instead of the Match Object.
"""

#The search() function returns a Match object:

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) # this will print an object

"""
Output:
<re.Match object; span=(5, 7), match='ai'>
"""

"""
The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""

"""
Print the position (start- and end-position) of the first match occurrence.
The regular expression looks for any words that starts with an upper case "S":
"""

# Search for an upper case "S" character in the beginning of a word, and print its position:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

"""
Output:
(12, 17)
"""

#The string property returns the search string:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

"""
The rain in Spain
"""

"""
Print the part of the string where there was a match.
The regular expression looks for any words that starts with an upper case "S":
"""

#Search for an upper case "S" character in the beginning of a word, and print the word:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

"""
Output:
Spain
"""

# Note: If there is no match, the value None will be returned, instead of the Match Object.