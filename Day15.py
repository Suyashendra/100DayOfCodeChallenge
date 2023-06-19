# 👉 Python String
# A string is a sequence of characters

# Example:
str1 = "Python programming"
print(str1)
print(str1[0]) # Accessing first character of str1 string
print(str1[1:4]) # Slicing str1 string

# Output:
# Python programming
# P
# yth

# 👉 Python Strings are immutable
# We cannot change character of a string 
# Example:
msg = "Hola Amigos"
# msg[0] = 'Y' # TypeError: 'str' object does not support item assignment

# Python Muliline String 
# Example:
msg = """
Never gonna give you up
Never gonna let you down
"""
print(msg)

# 👉 Iterate Through a Python String
# Example:
greet = "Hello"
for i in greet:
    print(i)
# Output:
# H
# e
# l
# l
# o

# 👉 Some Methods of Python String
# 1. len() - returns length of the string
# 2. upper() - converts the string to uppercase
# 3. lower() - converts the string to lowercase
# 4. partition() - returns a tuple
# 5. replace() - replaces a substring inside
# 6. find() - returns the index of first occurrence of substring
# 7. rstrip() - removes trailing charcters 
# 8. split() - splits string from left
# 9. startswith() - checks if string starts with the specified string
# 10. isnumeric() - checks numeric charcters
# 11. index() - returns index of substring

# 👉 Escape Sequences in Python 
# The escape sequences is used to escape some of the characters present inside a string.
# For Example: Suppose we need to include both double quote and single quote inside a string.
# str2 = "He said, "What's there?"" # throws error
# Since strings are represented by single or double quotes, the compiler will treat "He said, " as the string. 
# Hence, the above code will cause an error.

# To solve this issue, we use the escape character \ in Python.
# escape double quotes
str2 = "He said, \"What's there?\""
# escape single quotes
str2 = 'He said, "What\'s there?"'

# 👉 List of all the escape sequences supported by Python.
# \\ - Backslash
# \' - Single quote
# \" - Double quote
# \a - ASCII Bell
# \b - ASCII Backspace
# \f - ASCII Formfeed
# \n - ASCII Linefeed
# \r - ASCII Carriage Return
# \t - ASCII Horizontal Tab
# \v - ASCII Vertical Tab
# \ooo - Character with octal value ooo
# \xHH - Character with hexadecimal value HH

# 👉 Python String Formatting(f-Strings)
# Python f-Strings make it really easy to print values and variables. 
name = "Jk"
country = "UK"
print(f'{name} is from {country}') # Jk is from UK

# This new formatting syntax is powerful and easy to use. 

# 1. Evaluate Expressions with Python f-Strings
# As f-Strings are evaluated at runtime, we can evaluate valid Python expressions on the fly.
# Example:
num1 = 7
num2 = 5
print(f"The product of {num1} and {num2} is {num1*num2}")
# Output:
# The product of 7 and 5 is 35

# 2. Conditional statement in f-Strings
# one-line if..else statements
# Syntax -> <true_block> if <condition> else <false_block>

# This is often called the ternary operator in Python as it takes 3 operands in some sense - true block,
# condition, false block.

# Example:
num = 8
print(f"Is num even? {True if num%2==0 else False}") 
# Output:
# Is num even? True

# 3. Calling function inside f-Strings
def fun(x):
    if x%2==0:
        return "is a Even number"
    else:
        return "is a Odd number"

print(f"Given number: {fun(5)}")
# Output:
# Given number: is a Odd number

