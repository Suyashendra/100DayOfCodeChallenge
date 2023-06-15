# Python List

# A list in Python is used to store the sequence of various types of data.
# A list can be defined as a collection of values or items of different types. 
# Python lists are mutable type which implies that we may modify its element after it has been formed.
# The items in the list are separated with the comma (,) and enclosed with the square brackets [].

# Python lists are identical to dynamically scaled arrays that are specified in other languages, such as Java's ArrayList and C++'s vector.

# 👉 List Declaration 
# Example:
list1 = [1,2,"Python","Program", 15.9]
list2 = ["Amy","Ryan","Henry","Emma"]

# printing the list
print(list1)
print(list2)

# printing the type of list
print(type(list1))
print(type(list2))

# Output:
# [1, 2, 'Python', 'Program', 15.9]
# ['Amy', 'Ryan', 'Henry', 'Emma']
# < class ' list ' >
# < class ' list ' >

# 👉 Characteristis of Lists
# - The lists are ordered.
# - The element of the list can access by index.
# - The list are mutable types.
# - A list can store the number of various elements.

# 👉 Ordered list checking
# Example:
a = [1,2,3,4,5]
b = [5,4,3,2,1]  
a==b
# Output:
# False 

# Example:
a = [1,2,3,4,5]
b = [1,2,3,4,5] 
a==b
# Output:
# True

# Lists permanently preserve the element's order.

# 👉 List Accessing - List Indexing and Slicing
# The indexing is processed in the same way as it happens with the strings.
# The elements of the list can be accessed by using the slice operator [].
# The index starts from 0 and goes to length - 1. 
# The first element of the list is stored at the 0th index, the second element of the list is stored at the 1st index, and so on.
# last element is n-1 (here n = number of elements in the list).

# Example:
languages = ['Python', 'C++', 'Java']
print(languages[0])
print(languages[1])
print(languages[2])

# Output:
# Python
# C++
# Java

# Negative Indexing in Python
# The index of -1 refers to the last item, -2 to the second last item and so on.
# Example:
languages = ['Python', 'C++', 'Java']
print(languages[-1])
print(languages[-2])
print(languages[-3])
# Output:
# Java
# C++
# Python

# List Slicing
# We can get the sub-list of the list using slicing
# Syntax:
# list_variable(start:stop:step)

# The start denotes the starting index position of the list.
# The stop denotes the last index position of the list.
# The step is used to skip the nth element within a start:stop

list = ['P','y','t','h','o','n']
print(list[0:])
print(list[0:2])
print(list[:4])
print(list[2:])
print(list[:])
# Output:
# ['P', 'y', 't', 'h', 'o', 'n']
# ['P', 'y']
# ['P', 'y', 't', 'h']
# ['t', 'h', 'o', 'n']
# ['P', 'y', 't', 'h', 'o', 'n']

# negative indexing example:
list = [1,2,3,4,5]
print(list[-4:])
print(list[:-1])
print(list[-3:-1])
#Output:
# [2, 3, 4, 5]
# [1, 2, 3, 4]
# [3,4]

# Note: When we slice lists, the start index is inclusive but the end index is exclusive. 

# 👉 Updating list
# List values can be updated by using the slice and assignment operator.
# Python also provides append() and insert() methods, which can be used to add values to the list.

# Example:
list1 = [1,2,3,4,5,6]
print(list1)
list1[1] = 10
print(list1)
list1[1:3] = [20,30]
print(list1)
list1[-1] = 7
print(list1)
# Output:
# [1, 2, 3, 4, 5, 6]
# [1, 10, 3, 4, 5, 6]
# [1, 20, 30, 4, 5, 6]
# [1, 20, 30, 4, 5, 7]

# 1. Using append()
# The append() method adds an item at the end of the list. 
# Example:
n = [21,34,54,12]
print(n)
n.append(32)
print(n)
# Output:
# [21, 34, 54, 12]
# [21, 34, 54, 12, 32]

# 2. Using extend()
# The extend() method add all items of one list to another. 
# Example:
prime_n = [2,3,5]
even_n = [2,4,6]
prime_n.extend(even_n)
print(prime_n)
# Output:
[2, 3, 5, 2, 4, 6]

# 👉 Remove an Item from a list

# 1. Using del statement
# We use del statement to remove one or more items from a list.
# Example:

p_languages = ['Python','Swift','C++','Java','Rust','R']
del p_languages[1]
print(p_languages)

del p_languages[-1]
print(p_languages)

del p_languages[0:2]
print(p_languages)
# Output:
# ['Python', 'C++', 'Java', 'Rust', 'R']
# ['Python', 'C++', 'Java', 'Rust']
# ['Java', 'Rust', 'R']

# 2. Using remove()
# We can also use the remove() method to delete a list item.
# Example:
p_languages = ['Python','Swift','C++','Java','Rust','R']
p_languages.remove('Python')
print(p_languages)
# Output:
['Swift', 'C++', 'Java', 'Rust', 'R']

# 👉 Some List Operation 

# 1. Repetition 
# The repetition operator (*) enables the list elements to be repeated multiple times.
# Example:
list2 = [12, 14, 16, 18, 20]
l = list2*2
print(l)
# Output:
# [12, 14, 16, 18, 20, 12, 14, 16, 18, 20]

# 2. Concatenation
# Example:
list1 = [12, 14, 16, 18, 20]  
list2 = [9, 10, 32, 54, 86]  
# concatenation operator +  
l = list1 + list2  
print(l)  
# Output:
# [12, 14, 16, 18, 20, 9, 10, 32, 54, 86]

# 3. Length
# It is used to get the length of the list
# Example:
list1 = [12, 14, 16, 18, 20, 23, 27, 39, 40]  
# finding length of the list  
print(len(list1))  
# Output: 9 

# 4. Iteration
# The for loop is used to iterate over the list elements.
# Example:
list1 = [12, 14, 16, 39, 40]  
# iterating  
for i in list1:   
    print(i)  
# Output:
# 12
# 14
# 16
# 39
# 40

# 5. Membership
# It returns true if a particular item exists in a particular list otherwise false.
# Example:
list1 = [100, 200, 300, 400, 500]  
print(300 in list1)  
print(100 in list1)  
print(600 in list1)  
print(700 in list1)  
# Output:
# True
# True
# False
# False

# 👉 Python List Built-in Functions
# len()
# max()
# min()

list1 = [12, 16, 18, 20, 39, 40]  
print(len(list1)) # 6
print(max(list1)) # 40
print(min(list1)) # 12

# 👉 Python List Methods
# append() - add an item to the end of the list
# extend() - add items of lists and other iterables to the end of the list
# insert() - inserts an item at the specified index
# remove() - removes list item
# pop() - returns and removes item present at the given index
# clear() - removes all items from the list
# index() - returns the index of the first matched item
# count() - returns the count of the specified item in the list
# sort() - sort the list in ascending/descending order
# reverse() - reverses the item of the list
# copy() - returns the shallow copy of the list

# 👉 Python List Comprehension 
# List comprehension is a concise and elegant way to create lists.
# A list comprehension consists of an expression followed by the for statement inside square brackets.
# Example: Make a list with each item being increasing by power of 2.
numbers = [x*x for x in range(1,6)]
print(numbers)
# Output: [1, 4, 9, 16, 25]

# it's equivalent code 
numbers = []
for x in range(1,6):
    numbers.append(x*x)
print(numbers) 
# Output: [1, 4, 9, 16, 25]

# 👉 Some List Examples:

# Example1:- Write the program to remove the duplicate element of the list.
list1 = [1,2,2,3,55,98,65,65,13,29]
lis = []
for i in list1:
    if i not in lis:
        lis.append(i)
print(lis)
# Output:
# [1, 2, 3, 55, 98, 65, 13, 29]

# Example2:- Write a program to find the sum of the element in the list.
list1 = [3,4,5,9,10,12,24]    
print(sum(list1))
# Output: 67

# Example3:- Write the program to find the lists consist of at least one common element.
list1 = [1,2,3,4,5,6]    
list2 = [7,8,9,2,10]
lis = []
for i in list1:
    for j in list2:
        if i == j :
            lis.append(i)
print(lis)
# Output: [2]

