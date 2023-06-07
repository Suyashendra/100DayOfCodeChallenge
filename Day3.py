# Python Type Casting

# In Programming, type conversion is the process of converting data of one type to another.
# For Example: converting int data to str.

# There are two types of type conversion in Python
# - Implicit Conversion - automatic type conversion
# - Explicit Conversion - manual type conversion 

# 1. Python Implicit Type Conversion

# In certain situations, Python automatically converts one data type to another. 
# This is known as implicit type conversion.

# Example1: let's see an example where Python promotes the conversion of the lower data type(integer) 
# to the higher data type(float) to avoid data loss.
integer_number = 123
float_number = 1.23
new_number = integer_number + float_number
# displaying new value and resulting data type
print("Value:",new_number)
print("Data Type:", type(new_number))
# Output:
# Value: 124.23
# Data Type: <class 'float'>

# We get TypeError, if we try to add str and int.
# For example, '12' + 23. Python is not able to Implicit Conversion in such conditions.
# Python has a solution for these types of situations which is known as Explicit Conversion.
 
# 2. Python Explicit Type Conversion

# In Explicit Type Conversion, users convert the data type of an object to required data type.
# Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.
# We use the built-in constructor functions like int(), float(), str(), etc to perform explicit type conversion.
# This type of conversion also called typecasting because the user casts(changes) the data type of the objects.

# Example2:
# Integers:
x = int(1)   # x will be 1    
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# Floats:
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

# Strings:
x = str("s1") # wil be 's1' 
y = str(2)    # wil be '2'
z = str(3.0)  # wil be '3.0'

# Example3: Addition of string and integer
n_str = '12'
n_int = 23
n_str = int(n_str) #Explicit Conversion 
sum = n_str + n_int
print(sum)
# Output: 35
