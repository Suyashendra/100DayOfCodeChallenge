# 👉 Python Lambda/Anonymous Function

# In Python, a lambda function is a special type of function without the function name
# For example,
lambda : print('Hello World')

# Here, we have created a lambda function that prints 'Hello World'.

# 👉 Python Lambda Function Declaration 
# We use lambda keyword instead of def to create a lambda function.
# Here's the syntax to declare the lambda function:
# lambda argument(s) : expression
# Here,
# argument(s) - any value passed to the lambda function
# expression - expression is executed and returned

# Example:
greet = lambda : print('Hello World')
# Here, we have defined a lambda function and assigned it to the variable named greet

# To execute this lambda function, we need to call it. 
# Here's how we can call the lambda function
# call the lambda
greet()

# Output:
# Hello World

# 👉 Lambda Function with an Argument
# Similar to normal functions, the lambda function can also accept arguments. For example,

# Example:
# Lambda that accepts one argument 
greet_user = lambda name : print('Hey there,',name)
# lambda call
greet_user('Ram')

# Output: Hey there, Ram

# ----------------------------------------------------------------------------------------------

# 👉 Python Variable Scope 

# In Python, we can declare variable in three different scopes : local scope, global
# and nonlocal scope.

# A variable scope specifies the region where we can access a variable.

# Based on the scope, we can classify Python variables into three types:
# 1. Local Variables
# 2. Global Variables 
# 3. Nonlocal Variable

# 👉 Python Local Variables
# When we declare variables inside a function, these variables will have a local scope (within the function). 
# We cannot access them outside the function.
# These types of variables are called local variables.
# Example:
def greet():
    # local variable
    message = 'Hello'
    print('Local',message)

greet()
print(message)

# Output:
# Local Hello
# NameError: name 'message' is not defined

# 👉 Python Global Variables
# In Python, a variable declared outside of the function or in global scope is known as a global variable.
# This means that a global variable can be accessed inside or outside of the function.

# Example:
# declare global variable
message = 'Hello'

def greet():
    # declare local variable
    print('Local', message)

greet()
print('Global', message)

# Output:
# Local Hello
# Global Hello

# 👉 Python Nonlocal Variables
# In Python, nonlocal variables are used in nested functions whose local scope is not defined.
# This means that the variable can be neither in the local nor the global scope.

# Example:
# outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()

# Output:
# inner: nonlocal
# outer: nonlocal

# ----------------------------------------------------------------------------------------------

# 👉 Python Global Keyword

# In Python, the global keyword allows us to modify the variable outside of the current scope.
# It is used to create a global variable and make changes to the variable in a local context.

# 👉 Access and Modify Python Global Variable

# let's try to access a global variable from the inside of a function,
c = 1 # global variable
def add():
    print(c)
add()
# Output: 1

# Here, we can see that we have accessed a global variable from the inside of a function.

# However, if we try to modify the global variable from inside a function as:
c = 1 # global variable
def add():
    c = c + 2
    print(c)
add()
# Output: UnboundLocalError: local variable 'c' referenced before assignment
# This is because we can only access the global variable but cannot modify it from inside the function.
# The solution for this is to use the global keyword.

# Example: Changing Global Variable From Inside a Function using global keyword
c = 1 # global variable
def add():
    global c 
    c = c + 4
    print(c)
add()
# Output: 5

# 👉 Global in Nested Functions
# In Python, we can also use the global keyword in a nested function. 
# Example:
def outer_function():
    num = 20
    def inner_function():
        global num
        num = 25
    print("Before calling inner_function(): ", num)
    inner_function()
    print("After calling inner_function(): ", num)
outer_function()
print("Outside both function: ", num)
# Output:
# Before calling inner_function():  20
# After calling inner_function():  20
# Outside both function:  25

# Inside outer_function(), num has no effect of the global keyword.
# Before and after calling inner_function(), num takes the value of the local variable i.e num = 20.
# Outside of the outer_function() function, num will take the value defined in the inner_function() function i.e num = 25.
# This is because we have used the global keyword in num to create a global variable inside the inner_function() function(local scope).
# So, if we make any changes inside the inner_function() function, the changes appear outside the local scope, i.e. outer_function().

# 👉 Some points for global keyword in Python:
# 1. When we create a variable inside a function, it is local by default.
# 2. When we define a variable outside of a function, it is global by default. You don't have to use the global keyword.
# 3. We use the global keyword to read and write a global variable inside a function.
# 4. Use of the global keyword outside a function has no effect.
