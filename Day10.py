# 🔵 Python Module

# As our program grows bigger, it may contain many lines of code.
# Instead of putting everything in a single file, we can use modules to separate codes in separate files as per their functionnality.
# This makes our code organized and easier to maintain.
# Module is a file that contains code to perform a specific task.
# A module may contain variables, functions, classes etc. 
# Example: Let us create a module. 
# Python Module addition 
def add(a,b):
    result = a + b 
    return result
# Save this as example.py 

# 👉 Import modules in Python 
# We can import the definitions inside a module to another module or Python Program.
# We use the import keyword to do this. To import our previously defined module example, we type the following in the Python prompt.
import example

# This does not import the name of the function defined in example directly in the current program.
# It only imports the module name example there.
# Using the module name we can access the function using the dot . operator 
# For example:
example.add(4,5)

# Note: 
# 1. Python has tons of standard modules.
# 2. Standard modules can be imported the same way as we import our user-defined modules.

# 👉 Import Python Standard Library Modules
# The Python standard library contains well over 200 modules. We can import a module according to our needs.
# Suppose we want to get the value of pi, first we import the math module and use math.pi.
# For example,
# import standard math module 
import math
# use math.pi to get value of pi
print("The value of pi is",math.pi)

# Output:
# The value of pi is 3.141592653589793

# 👉 Python import with Renaming
# In Python, we can also import a module by renaming it. 
# For example,
# import module by renaming it
import math as m
print(m.pi)
# We have renamed the math module as m. This can save us typing time in some cases.

# 👉 Python from...import statement
# We can import specific names from a module without importing the module as a whole.
# For example,
# import only pi from math module
from math import pi
print(pi) # 3.141592653589793

# 👉 Import all names
# In Python, we can import all names(definitions) from a module using the following construct:
# import all names from the standard module math
from math import *
print("The value of pi is",pi) 

# Here, we have imported all the definitions from the math module. 
# This includes all names visible in our scope except those beginning with an underscore(private definitions).
# Importing everything with the asterisk (*) symbol is not a good programming practice.
# This can lead to duplicate definitions for an identifier.  It also hampers the readability of our code.

# 👉 The dir() built-in function
# In Python, we can use the dir() function to list all the function names in a module.
# For example, earlier we have defined a function add() in the example module.
# We can use dir in example module in the following way:
dir(example)
['__builtins__',
'__cached__',
'__doc__',
'__file__',
'__initializing__',
'__loader__',
'__name__',
'__package__',
'add']

# Here, we can see a sorted list of names (along with add).
# All other names that begin with an underscore are default Python attributes associated with the module (not user-defined).
# For example, the __name__ attribute contains the name of the module.
import example
# example.__name__
# Output: 'example'

# All the names defined in our current namespace can be found out using the dir() function without any arguments.
# Example:
a = 1
b = "hello"
import math
dir()

['__builtins__', '__doc__', '__name__', 'a', 'b', 'math', 'pyscripter']

# ----------------------------------------------------------------------------------------------------------------------------------

# 🔵 Python Package

# A package is a container that contains various functions to perform specific task.
# For example, the math package includes the sqrt() function to perform the square root of a number.
# While working on big project, we have to deal with a large amount of code, and writing everything together in the same file will make our code look messy.
# Instead, we can separate our code into multiple files by keeping the related code together in packages.
# Now, we can use the package whenever we need it in our projects. This way we can also reuse our code.

# Package Model Structure in Python Programming
# Suppose we are developing a game. One possible organization of packages and modules could be:

#                           Package (Game)
#                                   |
#           _______________________________________________________________
#           |             |                         |                     |
#      __init__.py    Sub-package (Sound)    Sub-package (Image)    Sub-package (Level)
#                         |                         |                     |
#                       __init__.py              __init__.py          __init__.py
#                        load.py                  open.py              start.py
#                        play.py                  change.py            load.py
#                        pause.py                 close.py             over.py

# Note: 
# A directory must contain a file named __init__.py in order for Python to consider it as a package.
# This file can be left empty but we generally place the initialization code for that package in this file.

# 👉 Importing module from a package
# In Python, we can import modules from packages using the dot (.) operator.
# For example, if we want to import the start module in the above example, it can be done as follows:
import Game.Level.start 

# Now, if this module contains a function named select_difficulty(), we must use the full name to reference it.
Game.Level.start.select_difficulty(2)

# 👉 Import Without Package Prefix
# If this construct seems lengthy, we can import the module without the package prefix as follows:
from Game.Level import start
# We can now call the function simply as follows:
start.select_difficult(2)

# 👉 Import Required Functionality Only
from Game.Level.start import select_difficulty
# Now we can directly call this function:
select_difficulty(2)
# Although easier, this method is not recommended.  
# Using the full namespace avoids confusion and prevents two same identifier names from colliding.

# While importing packages, Python looks in the list of directories defined in sys.path, similar as for module search path.

# ----------------------------------------------------------------------------------------------------------------------------------
