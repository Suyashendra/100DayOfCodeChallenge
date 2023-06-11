# Python Functions

# A function is a block of code that performs a specific task.
# Dividing a complex problem into smaller chunks makes our program easy to understand and reuse.

# 👉 Types of function
# There are two types of function in Python programming:
# Standard library functions - These are built-in functions in Python that are available to use.
# User-defined functions - We can create our own functions based on our requirements.

# 👉 Python Function Declaration 
def function_name(arguments):
    # Function body
    return

# Here,
# def - keyword used to declare a function
# function_name - any name given to the function
# arguments - any value passed to function
# return(optional) - returns value from a function

# Example:
def greet():
    print('Hello World!')

# Calling the function
greet() # To use a function, we need to call it.

# Output:
# Hello World 

# 👉 Python Function Arguments
# A function can also have arguments. 
# An agrument is a value that is accepted by a function.

# Example:
# Function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print('Sum:',sum)

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
add_numbers(a,b)

# 👉 The return Statement in Python 
# A Python function may or may not return a value. 
# If we want our function to return some value to a function call, we use the return statement.
# Syntax:
def add_number():
    ...
    return sum

# Example:
# Function definition
def find_square(num):
    result = num*num
    return result 

square = find_square(3)
print('Square: ',square)

# Output: Square: 9

# 👉 Python Library Function 
# In Python, standard library functions are the built-in functions that can be used directly in our program. 
# Example:
# print() - prints the string inside the quotation marks
# sqrt() - returns the square root of a number
# pow() - return the power of a number

# These library functions are defined inside the module.
# And, to use them we must include the module inside our program.
# for example, sqrt() is defined inside the math module.

# Example: Python Library Function

import math
square_root = math.sqrt(4)
print("Square root of 4 is",square_root)
power = pow(2,3)
print("2 to the power 3 is",power)
# Output:
# Square root of 4 is 2.0
# 2 to the power 3 is 8

# Here, notice the statement,
import math 
# Since sqrt() is defined inside the math module, we need to include it in our program.

# 👉 Benefits of using Functions

# 1. Code Reusable - We can use the same function multiple times in our program which makes our code reusable. 
# Example:
def get_square(num):
    return num*num 

for i in [1,2,3]:
    # function call 
    result = get_square(i)
    print('Square of', i, '=', result)

# Output:
# Square of 1 = 1
# Sqaure of 2 = 4
# Square of 3 = 9

# 2. Code Readability - Functions help us break our code into chunks to make our program readable and easy to understand.

