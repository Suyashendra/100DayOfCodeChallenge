# Python Exceptions

# A Python program terminates as soon as it encounters an error.
# In Python, an error can be syntax error or an exception. 

# Exceptions versus Syntax Errors 

# Syntax errors occurs when the parser detects an incorrect statement.
# Example:
print(0/0))
# Output:
#   File "Day4.py", line 10
#     print(0/0))
#               ^
# SyntaxError: unmatched ')'

# The arrow indicates where the parser ran into the syntax error.
# In this example, there was one bracket extra. Remove and run it.
print(0/0)
# Output:
#   File "Day4.py", line 19, in <module>
#     print(0/0)
# ZeroDivisionError: division by zero

# This time we ran into an Exception error.
# This type of error occur at runtime (after passing the syntax test) are called exceptions or logical errors.
# The last line of the message indicate what type of exception error you ran into.
# Instead of showing the message exception error, Python details what type of exception error was encountered.
# In this case, it was a ZeroDivisionError. 
# Python comes with various built-in exceptions as well as the possibility to create self-defined exceptions.

# Raise an Exception
 
# We can use raise to throw an exception if a condition occurs.
# The statement can be complemented with a custom exception.

# If you want to throw an error when a certain condition occurs using raise, we could go about like this:
x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x)) 
# Output:
# Traceback (most recent call last):
#   File "Day4.py", line 40, in <module>
# Exception: x should not exceed 5. The value of x was: 10

# The AssertionError Exception 

# Instead of waiting for a program to crash midway, we can also start by making an assertion in Python.
# We assert that a certain condition is met. If this condition turns out to be True, then that is excellent!
# The program can continue. If the condition turns out to be False, you can have the program throw an AssertionError Exception.
# Example:
import sys
assert ('linux' in sys.platform), "This code runs on Linux only."
# Output: 
# Traceback (most recent call last):
#   File "Day4.py", line 52, in <module>
# AssertionError: This code runs on Linux only.

# In above example, throwing an AssertionError exception is the last thing that the program will do.
# The program will come to halt and will not continue.

# Python Built-in Exceptions

# Illegal operations can raise exceptions. There are plenty of built-in exceptions in python that are raised when corresponding errors occurs.
# We can view all the built-in exceptions using the built-in locals() function as follow:
print(dir(locals()['__builtins__']))
# Here, locals()['__builtins__'] will return a module of built-in exceptions, functions, and attributes and dir allow us to list these attributes as strings.

# Some common built-in exceptions in Python Programming:
# 1. ZeroDivisionError -> Raised when the second operand of division or modulo operation is zero.
# 2. ValueError -> Raised when a funcion gets an argument of correct type but improper value.
# 3. TypeError -> Raised when a function or operation is applied to an object of incorrect type.
# 4. OverflowError -> Raised when the result of an arithmetic operation is too large to be represented.
# 5. MemoryError -> Raised when an operation runs out of memory.
# 6. KeyError -> Raised when a key is not found in a dictionary.
# 7. ImportError -> Raised when the imported module is not found. 
# 8. FloatingPointError -> Raised when a floating point operation fails.
# 9. EOFError -> Raised when the input() function hits end-of-file condition.
# 10. AttributeError -> Raised when attribute assignment or reference fails.
# 11. AssertionError -> Raised when an assert statement fails.

# Python Exception Handling

# We can handle these built-in and user-defined exceptions in Python using try, except and finally statements.

# Python try...except Block
# The try...except block is used to handle exceptions in Python. 
# Syntax of try...except block:
# try:
    # code that may cause exception
# except:
    # code to run when exception occurs

# Here, we have placed the code that might generate an exception inside the try block. 
# Every try block is followed by an except block.
# When an exception occurs, it is caught by the except block. 
# The except block cannot be used without the try block.

# Example:
try: 
    numerator = 10
    denominator = 0
    result = numerator/denominator
    print(result)
except:
    print("Error: Denominator cannot be 0.")

# To handle the exception, we have put the code, result = numerator/denominator inside the try block. 
# Now when an exception occurs, the rest of the code inside the try block is skipped.
# The except block catches the exception and statements inside the except block are executed.
# If none of the statements in the try block generates an exception, the except block is skipped.

# Catching Specific Exceptions in Python

# For each try block, there can be zero or more except blocks.
# Multiple except blocks allow us to handle each exception differently.
# The argument type of each except block indicates the type of exception that can be handled by it. 
# Example:
try:
    even_numbers = [2,4,6,8]
    print(even_numbers[5])
except ZeroDivisionError:
    print("Denominator cannot be 0.")
except IndexError:
    print("Index Out of Bound.")
# Output: Index Out of Bound

# Python try with else clause
# In some situations, we might want to run a certain block of code if the code block inside try runs without any errors. 
# For these cases, you can use the optional else keyword with the try statement.
# Example:
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)

# Output:
# If we pass an odd number:

# Enter a number: 1
# Not an even number!

# If we pass an even number
# Enter a number: 4
# 0.25

# However, if we pass 0, we get ZeroDivisionError as the code block inside else is not handled by preceding except.
# Enter a number: 0
# Traceback (most recent call last):
#   File "Day4.py", line 137, in <module>
#     reciprocal = 1/num
# ZeroDivisionError: division by zero
# Note: Exceptions in the else clause are not handled by the preceding except clauses.

# Python try...finally

# In Python, the finally block is always executed no matter whether there is an exception or not.
# The finally block is optional. And, for each try block, there can be only one finally block.
# Example:
try:
    numerator = 10
    denominator = 0
    result = numerator/denominator
    print(result)
except:
    print("Error: Denominator cannot be 0.")
finally:
    print("This is finally block.")

# Output:
# Error: Denominator cannot be 0.
# This is finally block.