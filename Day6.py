# Python Flow Control

# 👉 Python if...else Statement
# We use the if statement to run a block code only when a certain condition is met.
# In Python, there are three forms of the if...else statement.
# if statement
# if...else statement
# if...elif...else statement

# Example1:
x = 5
if x == 5:
    print('True')
# Output: True

# Example2:
y = 7
if y == 5:
    print('Inside if')
else:
    print('Inside else')
# Output: Inside else

# Example3:
y = 7
if y == 5:
    print('Inside if')
elif y == 7:
    print('Inside elif')
else:
    print('Inside else')
# Output: Inside elif

# 👉 Python for loop 
# In Python, a for loop is used to iterate over sequences such as lists, tuples, string, etc.

# Example1:
fruit = ['Mango','Apple', 'Banana','Watermelon']
for i in fruit:
    print(i)
# Output: 
# Mango
# Apple
# Banana
# Watermelon

# 👉 Python for Loop with Python range()
# A range is a series of values between two numeric intervals.
# We use Python's built-in function range() to define a range of values. 
# For example,
values = range(4)
# Here, 4 inside range() defines a range containing values 0, 1, 2, 3.
# In Python, we can use for loop to iterate over a range. 
# For example,
values = range(4)
for i in values:
    print(i) 
# Output:
# 0
# 1
# 2
# 3

# If we do not intend to use items of a sequence within the loop, 
# we can write the loop like this:
fruit = ['Mango','Apple', 'Banana','Watermelon']
for _ in fruit:
    print('Hello')
# The _ symbol is used to denote that the elements of a sequence will not be used within the loop body.


# 👉 Python while loop
# Python while loop is used to run a block code until a certain condition is met.

# Example1:
i = 1
n = 5
while i <= n:
    print(i)
    i += 1
# Output:
# 1
# 2
# 3
# 4
# 5

# Example2:
# Program to calculate the sum of numbers until user enter zero.
n = int(input("Enter number: "))
sum = n
while n != 0:
    n = int(input("Enter number: "))
    sum += n 
    print('Sum:', sum)

# 👉 Python break Statement 
# The break statement is used to terminate the loop immediately when it is encountered.

# Example1:
for i in range(5):
    if i == 3:
        break
    print(i)
# Output:
# 0
# 1
# 2

# Example2:
i=0
while i<5:
    if i == 3:
        break
    print(i)
    i+=1
# Output:
# 0
# 1
# 2

# 👉 Python continue Statement
# The continue statement is used to skip the current iteration of the loop and the control flow of the program goes to the next iteration.

# Example1:
for i in range(5):
    if i == 3:
        continue
    print(i)
# Output:
# 0
# 1
# 2
# 4

# Example2:
i=0
while i<5:
    if i == 3:
        continue
    print(i)
    i+=1
# Output:
# 0
# 1
# 2
# 4

# 👉 Python pass Statement
# In Python programming, the pass statement is a null statement which can be used as a placeholder for future code.
# Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future. 
# In such cases, we can use the pass statement.

# Example1:
n = 5 
if 10 > n:
    pass
print('Hello')
# Nothing happens when the pass is executed. 
# It results in no operation (NOP)
# Suppose we didn't use pass or just put a comment as:
n = 5 
if 10 > n:
    # pass
print('Hello')
# Here, we will get an error message: 
# IndentationError: expected an indented block
# Note: The difference between a comment and a pass statement in Python is that while the interpreter ignores a comment entirely, pass is not ignored.
   
# Example2: Use of pass statement inside function or class
# We can do the same thing in an empty function or class as well. 
def function(args):
    pass 

class Example:
    pass


