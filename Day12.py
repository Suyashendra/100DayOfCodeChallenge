# Python Tuple

# A tuple in Python is similar to a list.  
# The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.
# Tuple is immutable.

# 👉 Creating a Tuple 
# A tuple is created by placing all the items (elements) inside parentheses (), separated by commas.
# The parentheses are optional, however, it is a good practice to use them.
# A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.).

# Example:
# Different types of tuple
# Empty tuple
t1 = ()
print(t1)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# Output
# ()
# (1, 2, 3)
# (1, 'Hello', 3.4)
# ('mouse', [8, 4, 6], (1, 2, 3))

# As mentioned earlier, we can also create tuples without using parentheses:
t2 = 1,2,3
t3 = 1,"Hello",3.4
print(type(t2))
print(type(t3))
# Output:
# <class 'tuple'>
# <class 'tuple'>

# Example: 
var1 = ("hello")
print(type(var1))  # <class 'str'>

var1 = ("hello",)
print(type(var1))  # <class 'tuple'>

var3 = "hello",
print(type(var3))  # <class 'tuple'>

# 👉 Access Python Tuple Elements
# Like a list, each element of a tuple is represented by index numbers (0, 1, ...) where the first element is at index 0.

# 1. Indexing
# We can use the index operator [] to access an item in a tuple, where the index starts from 0.
# last element Index is n-1 (where n = total number of element)
# Example:
letters = ("p", "r", "o", "g", "r", "a", "m")
print(letters[0])   # prints "p" 
print(letters[5])   # prints "a"

# 2. Negative Indexing
# Python allows negative indexing for its sequences.
# The index of -1 refers to the last item, -2 to the second last item and so on.
# Example:
letters = ("p", "r", "o", "g", "r", "a", "m")
print(letters[-1])   # prints "m" 
print(letters[-3])   # prints "r"

# 3. Slicing
# We can access a range of items in a tuple by using the slicing operator colon :.
# Example:
# accessing tuple elements using slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm')

# elements 2nd to 4th index
print(my_tuple[1:4])  #  prints ('r', 'o', 'g')

# elements beginning to 2nd
print(my_tuple[:-5]) # prints ('p', 'r')

# elements 8th to end
print(my_tuple[5:]) # prints ('a', 'm')

# elements beginning to end
print(my_tuple[:]) # Prints ('p', 'r', 'o', 'g', 'r', 'a', 'm')

# Note: When we slice lists, the start index is inclusive but the end index is exclusive.

# 👉 Python Tuple Methods
# In Python ,methods that add items or remove items are not available with tuple. 
# Only the following two methods are available.

# Some examples of Python tuple methods:
# Example:
tuple1 = ('a', 'p', 'p', 'l', 'e',)
print(tuple1.count('p')) # 2
print(tuple1.index('l')) # 3

# 👉 Iterating through a Tuple
# We can use the for loop to iterate over the elements of a tuple.
# Example:
languages = ('Python', 'Swift', 'C++')
# iterating through the tuple
for i in languages:
    print(i)
# Output:
# Python
# Swift
# C++

# 👉 Check if an Item Exists in the Python Tuple
# We use the in keyword to check if an item exists in the tuple or not.
languages = ('Python', 'Swift', 'C++')
print('C' in languages)    # False
print('Python' in languages)    # True

# Advantages of Tuple over List in Python

# Since tuples are quite similar to lists, both of them are used in similar situations.
# However, there are certain advantages of implementing a tuple over a list:
# 1. We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
# 2. Since tuples are immutable, iterating through a tuple is faster than with a list. So there is a slight performance boost.
# 3. Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
# 4. If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

