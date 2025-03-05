# Python Operators

"""
Python Operators:
    1.Operators are used to perform operations on variables and values.
    2.In the example below, we use the + operator to add together two values:
"""
print(5 + 10)

"""
Ouput:
15
"""

"""
Python divides the operators in the following groups:

    1.Arithmetic operators
    2.Assignment operators
    3.Comparison operators
    4.Logical operators
    5.Identity operators
    6.Membership operators
    7.Bitwise operators
"""

# Python Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:

"""
Operator	  Name	        Example	
+	        Addition	    x + y	
-	      Subtraction	    x - y	
*	     Multiplication 	x * y	
/	        Division	    x / y	
%        	Modulus	        x % y	
**	    Exponentiation  	x ** y	
//	    Floor division  	x // y

"""

# Python Assignment Operators
# Assignment operators are used to assign values to variables:

"""
Operator	    Example	            Same As	
=	            x = 5	            x = 5	
+=	            x += 3	            x = x + 3	
-=	            x -= 3	            x = x - 3	
*=	            *= 3	            x = x * 3	
/=	            x /= 3	            x = x / 3	
%=	            x %= 3	            x = x % 3	
//=	            x //= 3	            x = x // 3	
**=	            x **= 3	            x = x ** 3	
&=	            x &= 3	            x = x & 3	
|=	            x |= 3	            x = x | 3	
^=	            x ^= 3	            x = x ^ 3	
>>=	            x >>= 3	            x = x >> 3	
<<=	            x <<= 3	            x = x << 3	
:=	            print(x := 3)	    x = 3
                                    print(x)

"""

# Python Comparison Operators
# Comparison operators are used to compare two values:

"""
Operator	Name	                    Example	
==	        Equal	                    x == y	
!=	        Not equal	                x != y	
>	        Greater than	            x > y	
<	        Less than	                x < y	
>=	        Greater than or equal to	x >= y	
<=	        Less than or equal to	    x <= y

"""

# Python Logical Operators
# Logical operators are used to combine conditional statements:

"""

Operator	        Description	                                             Example	
and 	    Returns True if both statements are true	                      x < 5 and  x < 10	
or	        Returns True if one of the statements is true	                  x < 5 or x < 4	
not 	Reverse the result, returns False if the result is true	not           (x < 5 and x < 10)

"""

# Python Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

"""
Operator	Description	                                                Example	
is 	        Returns True if both variables are the same object	        x is y	
is not	    Returns True if both variables are not the same object	    x is not y
"""

# Python Membership Operators
# Membership operators are used to test if a sequence is presented in an object:

"""
Operator	                          Description	                                                Example	
in 	         Returns True if a sequence with the specified value is present in the object	        x in y	
not in	     Returns True if a sequence with the specified value is not present in the object	    x not in y
"""

# Python Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:

"""
Operator	Name	            Description	                                                Example	
& 	        AND	                Sets each bit to 1 if both bits are 1	                    x & y	
|	        OR	                Sets each bit to 1 if one of two bits is 1	                x | y	
^	        XOR	                Sets each bit to 1 if only one of two bits is 1	            x ^ y	
~	        NOT	                Inverts all the bits	                                     ~x	
<<	        Zero fill left      Shift left by pushing zeros in from                         x << 2
            shift               the right and let the leftmost bits fall off

>>	        Signed right        Shift right by pushing copies of the leftmost               x >> 2
            shift	            bit in from the left, and let the rightmost bits fall off
"""

"""
Operator Precedence:
    1.Operator precedence describes the order in which operations are performed.
    2.Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
"""
print((1-5)+(10+10))

"""
Output:
16
"""

# Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions:

print(100 + 2 * 3)

"""
Output:
106
"""

# The precedence order is described in the table below, starting with the highest precedence at the top:

"""
Operator	            Description	
()	                    Parentheses	
**	                    Exponentiation	
+x  -x  ~x	            Unary plus, unary minus, and bitwise NOT	
*  /  //  %	            Multiplication, division, floor division, and modulus	
+  -	                Addition and subtraction	
<<  >>	                Bitwise left and right shifts	
&	                    Bitwise AND	
^	                    Bitwise XOR	
|	                    Bitwise OR	
==,  !=,  >,            Comparisons, identity, and membership operators	
>=,  <,  <=,  is,  
is not,  in,  not in 	
not	                    Logical NOT	
and	                    AND	
or	                    OR
"""

# If two operators have the same precedence, the expression is evaluated from left to right.

# Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right:

print(5 + 4 - 7 + 3)

"""
Output:
5
"""