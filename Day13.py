# Python Sets

# A set is a collection of unique data.
# That is, element of a set cannot be duplicate. 
# Example:
# Suppose we want to store information about student IDs. Since student IDs cannot be duplicate, we can use a set.

# 👉 Create a Set in Python 
# In Python, we create sets by placing all the elements inside curly braces {}, separated by comma.
# A set can have any number of items and they may be of different types(integer, float, tuple, string, etc.).
# But a set cannot have mutuable elements like lists, sets or dictionaries as its elements.

# Example:
# create a set of integer type
student_id = {112,114,116,118,115}
print('Student ID', student_id)

# create a set of string type
vowel_letter = {'a','e','i','o','u'}
print('Vowel Letters:', vowel_letter)

# create a set of mixed data types
mixed_set = {'Hello',101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

# Output:
# Student ID: {112, 114, 115, 116, 118}
# Vowel Letters: {'u', 'a', 'e', 'i', 'o'}
# Set of mixed data types: {'Hello', 'Bye', 101, -2}

# Note: When you run this code, you might get output in a different order.
# This is because the set has no particular order

# 👉 Create an Empty Set
# Creating an empty set is a bit tricky. 
# Empty curly braces {} will make an empty dictionary in Python.
# To make a set without any elements, we use the set() function without any argument.
# Example:
empty_set = set()
empty_dictionary = {}
print(type(empty_set))
print(type(empty_dictionary))
# Output:
# <class 'set'>
# <class 'dict'>

# Duplicate Items in a Set
n = {2,4,6,6,2,8}
print(n) # {8,2,4,6}

# 👉 Add and Update Set Items in Python
# Sets are mutable. However, since they are unordered, indexing has no meaning.
# We cannot access or change an element of a set using indexing or slicing. 
# Set data type does not support it.

# 1. Add Items to a Set in Python
# Use the add() method to add an item to a set.
# Example: 
n = {21,34,54,12}
print(n)
n.add(32)
print(n)
# Output:
# {34, 12, 21, 54}
# {32, 34, 12, 21, 54}

# 2. Update Set
# The update() method is used to update the set with items other collection types(lists, tuple, sets, etc).
# Example:
a = {2,4,6}
b = [1,3,5,1]
a.update(b)
print(a)
# Output:
# {1, 2, 3, 4, 5, 6}

# Here, all the unique elements of b are added to the a set. 

# 3. Remove an Element from a Set
# We use the discard() method to remove the specified element from a set. 
# Example:
x = {1,2,3,4,5}
x.discard(3)
print(x)
# Output:
# {1, 2, 4, 5}

# 👉 Built-in Functions with Set
# Some common functions
# 1. all() - Returns True if all elements of the set are true or if the set is empty return false.
# 2. any() - Returns True if any element of the set is true. if the set is empty, returns False.
# 3. enumerate() - Returns an enumerate object. It contains the index and value for all the items of the set as a pair.
# 4. len() - Returns length in the set.
# 5. max() - Returns the largest item in the set.
# 6. min() - Returns the smallest item in the set.
# 7. sorted() - Returns a new sorted list from elements in the set(does not sort the set itself).

# 👉 Iterate Over a Set in Python
fruits = {"Apple","Peach","Mango"}
for i in fruits:
    print(fruits)
# Output:
# Mango
# Peach
# Apple

# 👉 Python Set Operations
# Python Set provides different built-in methods to perform mathematical set operations like
# union, intersaction, subtraction, and symmetric difference.

# 1.Union of Two Sets
# The union of two set A and B include all the elements of set A and B.
# We use the | operator or the union() method to perform the set union operation.
# Example:
a = {1,3,5}
b = {0,2,4}
print(a|b)
print(a.union(b))
# Output:
# {0, 1, 2, 3, 4, 5}
# {0, 1, 2, 3, 4, 5}

# Note: A|B and union() is equivalent to A ⋃ B set operation.

# 2. Set Intersection
# The intersection of two sets A and B include the common elements between set A and B.
# We use the & operator or the intersection() method to perform the set intersection operation. 
# Example:

a = {1,3,5}
b = {1,2,3}
print(a & b)
print(a.intersection(b))
# Output:
# {1, 3}
# {1, 3}

# Note: A&B and intersection() is equivalent to A ⋂ B set operation.

# 3. Difference between Two Sets
# The difference between two sets a and b include elements of set a that are not present on set b.
# We use the - operator or the difference() method to perform the difference between two sets.
a = {2,3,5}
b = {1,2,6}
print(a-b)
print(a.difference(b))
# Output:
# {3, 5}
# {3, 5}

# Note: A - B and A.difference(B) is equivalent to A - B set operation.

# 4. Set Symmetric Difference
# The symmetric difference between two sets A and B includes all elements of A and B without the common elements.
# We use the ^ operator or the symmetric_difference() method to perform symmetric difference between two sets. 
# Example:
a = {2,3,5}
b = {1,2,6}
print(a^b)
print(a.symmetric_difference(b))
# Output:
# {1, 3, 5, 6}
# {1, 3, 5, 6}

# 👉 Check if two sets are equal
# We can use the == operator to check whether two sets are equal or not.
# Example:
a = {1,3,5}
b = {3,5,1}
print(a==b)
# Output:
# True

# Other Python Set Methods
# There are many set methods, some of which we have already used above. 
# Here is a list of all the methods that are available with the set objects.
# 1. add() - Adds an element to the set
# 2. clear() - Removes all elements from the set
# 3. copy() - Returns a copy of the set
# 4. difference() - Returns the difference of two or more sets as a new set
# 5. difference_upload() - Removes all elements of another set from this set
# 6. discard() - Removes an element from the set if it is a member. 
# 7. intersection() - Returns the intersection of two sets as a new set
# 8. intersection_update() - Updates the set with the intersection of itself and another
# 9. isdisjoint() - Returns True if two sets have a null intersection
# 10. issubset() - Returns True if another set contains this set
# 11. issuperset() - Returns True if this set contains another set
# 12. pop() - Removes and returns an arbitrary set element. Raises KeyError if the set is empty
# 13. remove() - Removes an element from the set. If the element is not a member, raises a KeyError
# 14. symmetric_difference() - Returns the symmetric difference of two sets as a new set
# 15. symmetric_difference_update() - Updates a set with the symmetric difference of itself and another
# 16. union() - Returns the union of sets in a new set
# 17. update() - Updates the set with the union of itself and others

