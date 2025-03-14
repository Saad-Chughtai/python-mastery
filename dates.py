# Python DateTima

"""
Python Dates:
    A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
"""
import datetime


x = datetime.datetime.now()
print(x)      # It will print the current time on your machince


"""
Date Output
    1.When we execute the code from the example above the result will be:
        2025-03-14 21:30:39.388848
    2.The date contains year, month, day, hour, minute, second, and microsecond.
    3.The datetime module has many methods to return information about the date object.
"""


x = datetime.datetime.now()

print(x.year)               
print(x.strftime("%A"))  

"""
Output:
2025
Friday
"""

"""
Creating Date Objects:
    1.To create a date, we can use the datetime() class (constructor) of the datetime module.
    2.The datetime() class requires three parameters to create a date: year, month, day.
"""


x = datetime.datetime(2020, 5, 17)
print(x)

"""
Output:
2020-05-17 00:00:00
"""

# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone),
# but they are optional, and has a default value of 0, (None for timezone).

"""
The strftime() Method:
    1.The datetime object has a method for formatting date objects into readable strings.
    2.The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
"""


x = datetime.datetime.now()
print(x.strftime("%B"))

"""
Output:
March
"""


# A reference of all the legal format codes:
"""
Directive	    Description	                    Example	
%a	            Weekday, short version	        Wed	

%A	            Weekday, full version	        Wednesday

%w	            Weekday as a number 0-6, 
                    0 is Sunday	                3	

%d	            Day of month 01-31	            31	

%b	            Month name, short version	    Dec	

%B	            Month name, full version	    December	

%m	            Month as a number 01-12	        12	

%y	            Year, short version, 
                    without century	            25	

%Y	            Year, full version	            2025	

%H	            Hour 00-23	                    17	

%I	            Hour 00-12	                    05	

%p	            AM/PM	                        PM	

%M	            Minute 00-59	                41	

%S	            Second 00-59	                08	

%f	            Microsecond 000000-999999	    548513	

%z	            UTC offset	                    +0100	

%Z	            Timezone	                    CST	

%j	            Day number of year 001-366	    365	

%U	            Week number of year, 
                Sunday as the first             52
                day of week, 00-53	

%W	            Week number of year,        
                Monday as the first             52
                day of week, 00-53	            	

%c	            Local version of date and time	Mon Dec 31 17:41:00 2018	

%C	            Century	                        20	

%x	            Local version of date	        12/31/18	

%X	            Local version of time	        17:41:00	

%%	            A % character	                %	

%G	            ISO 8601 year	                2025	

%u	            ISO 8601 weekday (1-7)	        1	

%V	            ISO 8601 weeknumber (01-53)	    01
"""

"""
Syntax for all these Directive

import datetime
x = datetime.datetime.now() Or
x = datetime.datetime.("Custom date") # For Custom date 

print(x.strftime("Directive"))

"""