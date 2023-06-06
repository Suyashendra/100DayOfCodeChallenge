# 🔵 Python Variable 

# 👉 Variables are containers for storing data values.
# 👉 Variable is a name that is used to refer to memory location. 
# 👉 Python variable is also known as an identifier and used to hold value.

# 🔵 Creating Variables
# 👉 Python has no command for declaring a variable.
# 👉 A variable is created the moment you first assign a value to it.
# Example1:
x = 5 
y = 7 
print(x)
print(y)
# 👉 Variables do not need to be declared with any particular type, and can even change type after they have been set.
# Example2:
x = 1 # x is a type of int
y = "Hello" # y is a type of str 

# 🔵 Identifier Naming 
# 👉 Variable are the example of identifiers. 
# 👉 An identifier is used to identify the literals used in the program. 

# - Rules to name an identifier are given below:
# 👉 The first character of the variable must be an alphabet or underscore ( _ ).
# 👉 All the characters except the first character may be an alphabet of  lower-case(a-z), upper-case (A-Z), underscore, or digit (0-9).
# 👉 Identifier name must not contain any white-space, or special character (!, @, #, %, ^, &, *).
# 👉 Identifier name must not be similar to any keyword defined in the language.
# 👉 Identifier names are case sensitive; for example, myname, and MyName is not the same.
# 👉 Examples of valid identifiers: a123, _n, n_9, etc.
# 👉 Examples of invalid identifiers: 1a, n%4, n 9, etc.



# 🔵 Declaring Variable and Assigning Values

# 👉 Python does not bind us to declare a variable before using it in the application. It allows us to create a variable at the required time.
# 👉 We don't need to declare explicitly variable in Python. When we assign any value to the variable, that variable is declared automatically.
# 👉 The equal (=) operator is used to assign value to a variable.

# 🔵 Object References

# 👉 It is necessary to understand how the Python interpreter works when we declare a variable. 
# 👉 The process of treating variables is somewhat different from many other programming languages.
# 👉 Python is the highly object-oriented programming language; that's why every data item belongs to a specific type of class. 
# 👉 Consider the following example:
print("Hello")
# Output: Hello
# The Python object creates an String object and displays it to the console.
# We can check the type of it using the Python built-in type() function.
print(type("Hello"))
# Output: <class 'str'>

# 👉 In Python, variables are a symbolic name that is a reference or pointer to an object. 
# 👉 The variables are used to denote objects by that name.

# 🔵 Many Values to Multiple Variables

# 👉 Python allows you to assign values to multiple variables in one line:
# 👉 Example:
x, y, z = "Mango", "Apple", "Banana"
print(x)
print(y)
print(z)

# 🔵 One Value to Multiple Variables

# 👉 We can assign the same value to multiple variables in one line:
# 👉 Example:
x = y = z = "Mango"
print(x)
print(y)
print(z)

# 🔵 Python Variable Types 

# 👉 There are two types of variables in Python - Local variable and Global variable.

# - Local Variable
# 👉Local variables are the variables that declared inside the function and have scope within the function. 
# Example:
# Declaring a function
def add():
    # Defining local variables. They have scope within the function.
    a = 20
    b = 30 
    c = a+b
    print("Sum:",c) 
# Calling a function
add()

# - Global Variables
# 👉 Global variables can be used throughout the program, and its scope is in the entire program.
# 👉 We can use global variables inside or outside the function.
# 👉 A variable declared outside the function is the global variable by default. 
# 👉 Python provides the global keyword to use global variable inside the function. 
# 👉 If we don't use the global keyword, the function treats it as a local variable. 
# Example:
# Declaring a variable and initialize it
x = 101
# Declaring a function
def mainFunction():
    # Global variable in function 
    global x
    # Printing a global variable 
    print(x)
    # Modifing a global variable 
    x = "Hello"
    print(x)

# Calling function 
mainFunction()
print(x)

# Output: 
# 101
# Hello
# Hello

