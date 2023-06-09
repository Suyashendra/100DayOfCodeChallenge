# Python I/O and Python Operators

# Python I/O

# 👉Python Output
# In Python, we can simply use the print() function to print output.
print("Hello World")
# Output: Hello World

# Syntax of print()
# In, above example code, the print() function is taking a single parameter.
# However, the actual syntax of the print function accepts 5 parameters:

# print(object= sep= end= file= flush=)

# Here, 
# object - values to be printed
# sep(optional) - allows us to separate multiple objects inside print().
# end(optional) - allows us to add specific values like new line "\n", tab "\t".
# file(optional) - where the values are printed. It's default value is sys.stdout (screen).
# flush(optional) - boolean specifying if the output is flushed or buffered. Default: False

print("Hello World")
# In the above example, the print() statement only includes the object to be printed. 
# Here, the value for end is not used. Hence, it takes the default value '\n'.

# print() with end parameter:
print('Good Morning!', end=' ')
print('It is rainy today')
# Output: Good Morning! It is rainy today

# print() with sep parameter:
print('Hi','Hai', 'Hey', sep='. ')
# Output: 
# Hi. Hai. Hey

# Output Formating
# Sometimes we would like to format our output to make it look attractive.
# This can be done by using the str.format() method.
# Example:
x = 5
y = 10
print('The value of x is {} and y is {}'.format(x,y))
# Output: The value of x is 5 and y is 10

# Here, the curly bracket {} are used as placeholders. We can specify the order in which they are printed by using numbers(tuple index).

# 👉Python Input
# While programming, we might want to take the input from the user.
# In Python, we can use the input() function.

# Syntax of input()
# input(prompt)
# Here, prompt is the string we wish to display on the screen. It is optional.

# Example:
num = input('Enter a number: ')
print('Entered number:',num)
print('Data type of the num:',type(num))
# Output1:
# Enter a number: Hi
# Entered number: Hi
# Data type of the num: <class 'str'>

# Output2:
# Enter a number: 7
# Entered number: 7
# Data type of the num: <class 'str'>

# It is important to note that the entered value 7 is a string, not a number. 
# So, type(num) returns <class 'str'>.
# To convert user input into a number we can use int() or float()
# Example:
num = int(input('Enter a number: '))

# ----------------------------------------------------------------------------

# Python Operators
# Operators are special symbols that perform operations on variables and values.
# Example:
print(5+6) # 11
# Here, + is an operator that adds two numbers: 5 and 6.

# Types of Python Operators

# 1.Arithmetic operators
# 2.Assignment Operators
# 3.Comparison Operators
# 4.Logical Operators
# 5.Bitwise Operators
# 6.Special Operators

# 1. Arithmetic Operators
# Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc. 
# For example,
sub = 10 - 5 # 5

# Arithmetic Operators in Python
a = 7
b = 2

# addition
print ('Sum: ', a + b)  

# subtraction
print ('Subtraction: ', a - b)   

# multiplication
print ('Multiplication: ', a * b)  

# division
print ('Division: ', a / b) 

# floor division
print ('Floor Division: ', a // b)

# modulo
print ('Modulo: ', a % b)  

# a to the power b
print ('Power: ', a ** b)   

# Output:
# Sum: 9
# Subtraction: 5
# Multiplication: 14
# Division: 3.5
# Floor Division: 3
# Modulo: 1
# Power: 49

# 2. Python Assignment Operators
# Assignment operators are used to assign values to variables. 
# For example,
x = 5

# Here's a list of different assignment operators available in Python.
# = (Assignment Operator) 
# += Addition Assignment
# -= Subtraction Assignment
# *= Multiplication Assignment
# /= Division Assignment
# %= Remainder Assignment
# **= Exponent Assignment    

# Example: Assignment Operators
# assign 10 to a
a = 10

# assign 5 to b
b = 5 

# assign the sum of a and b to a
a += b      # a = a + b

print(a)

# Output: 15

# 3. Python Comparison Operators
# Comparison operators compare two values/variables and return a boolean result: True or False.
# For example,
a = 5
b = 2
print(a>b) #True

# Example: Comparison Operators
a = 5

b = 2

# equal to operator
print('a == b =', a == b)

# not equal to operator
print('a != b =', a != b)

# greater than operator
print('a > b =', a > b)

# less than operator
print('a < b =', a < b)

# greater than or equal to operator
print('a >= b =', a >= b)

# less than or equal to operator
print('a <= b =', a <= b)

# Output:
# a == b = False
# a != b = True
# a > b = True
# a < b = False
# a >= b = True
# a <= b = False

# Note: Comparison operators are used in decision-making and loops.

# 4. Python Logical Operators
# Logical operators are used to check whether an expression is True or False. They are used in decision-making. 
# For example,
a = 5
b = 6
print((a>2) and (b>=6)) #True

# Logical Operators:
# and - True only if both the operands are True
# or - True if at least one of the operands is True
# not - True if the operand is False and vice-versa

# Example: Logical Operators
# logical AND
print(True and True)     # True
print(True and False)    # False

# logical OR
print(True or False)     # True

# logical NOT
print(not True)          # False

# 5. Python Bitwise operators
# Bitwise operators act on operands as if they were strings of binary digits. 
# They operate bit by bit, hence the name.
# For example, 2 is 10 in binary and 7 is 111.

# Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)
# & (Bitwise AND) Eg- x & y = 0 (0000 0000) 
# | (Bitwise OR) x | y = 14 (0000 1110)
# ~ (Bitwise NOT) ~x = -11 (1111 0101)
# ^ Bitwise XOR x ^ y = 14 (0000 1110)
# >> Bitwise right shift x >> 2 = 2 (0000 0010)
# << Bitwise left shift x << 2 = 40 (0010 1000)

# 6. Python Special operators
# Python language offers some special types of operators like the identity operator and the membership operator.
# They are described below with examples:

# 1. Identity operators
# In Python, is and is not are used to check if two values are located on the same part of the memory. 
# Two variables that are equal does not imply that they are identical.

# is - True if the operands are indentical(refer to the same object)
# Example: x is True

# is not - True if the operands are not identical(do not refer to the same object)
# Example: x is not True

# Example: Identity operators in Python
x1 =  5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is y1) # True
print(x1 is not y1) # False
print(x2 is y2) # True
print(x3 is y3) # True

# Here, we see that x1 and y1 are integers of the same values, so they are equal as well as identical. 
# Same is the case with x2 and y2 (strings).
# But x3 and y3 are lists. They are equal but not identical. 
# It is because the interpreter locates them separately in memory although they are equal.

# 2. Membership operators
# In Python, in and not in are the membership operators. 
# They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).
# In a dictionary we can only test for presence of key, not the value.

# in - True if value/variable is found in the sequence 
# Example : 5 in x 

# not in - True if value/variable is not found in the sequence 
# Example: 5 not in x

# Example: Membership operators in Python
x = 'Hello world'
y = {1:'a', 2:'b'}

# check if 'H' is present in x string
print('H' in x)  # prints True

# check if 'hello' is present in x string
print('hello' not in x)  # prints True

# check if '1' key is present in y
print(1 in y)  # prints True

# check if 'a' key is present in y
print('a' in y)  # prints False

