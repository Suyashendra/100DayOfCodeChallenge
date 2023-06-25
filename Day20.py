# 🔵 Python Directory and Files Management

# A directory is a collection of files and subdirectories. 
# A directory inside a directory is known as a subdirectory.
# Python has the os module that provides us with many useful methods to work with directories(and files as well).

# 👉 Get Current Directory in Python
# We can get the current directory using the getcwd() method of the os module.
# This method returns the current working directory in the form of a string. 
# For example:
import os 
print(os.getcwd())
# Output:
# C:\Users\Lenovo\Desktop\100DaysCodeChallenge

# 👉 Changing Directory in Python
# In Python, we can change the current working directory by using the chdir() method.
# The new path that we want to change into must be supplied as a string to this method. And we can use both the fordward-slash(/) or backword-slash(\) to separate the path elements.
# For example:
import os
# change directory
os.chdir('C:\\Python3')
print(os.getcwd())
# Output: 
# C:\Python33

# 👉 List Directories and Files in Python
# All files and sub-directories inside a directory can be retrieved using the listdir() method.
# This method takes in a path and returns a list of subdirectories and files in that path.
# If no path is specified, it returns the list of subdirectories and files from the current working directory.
# Example:
import os 
print(os.listdir())
# Output:
# ['.git', 'Day1.py', 'Day10.py', 'Day11.py', 'Day12.py', 'Day13.py', 'Day14.py', 'Day15.py', 'Day16.py', 'Day17.py', 'Day18.py', 'Day19.py', 'Day2.py', 'Day20.py', 'Day3.py', 'Day4.py', 'Day5.py', 'Day6.py', 'Day7.py', 'Day8.py', 'Day9.py', 'README.md']

# 👉 Making a New Directory in Python
# In Python, we can make a new directory using the mkdir() method.
# This method takes in the path of the new directory. If the full path is not specified, the new directory is created in the current working directory.
# Example:
os.mkdir('test')
print(os.listdir())
# Output:
# ['.git', 'Day1.py', 'Day10.py', 'Day11.py', 'Day12.py', 'Day13.py', 'Day14.py', 'Day15.py', 'Day16.py', 'Day17.py', 'Day18.py', 'Day19.py', 'Day2.py', 'Day20.py', 'Day3.py', 'Day4.py', 'Day5.py', 'Day6.py', 'Day7.py', 'Day8.py', 'Day9.py', 'README.md', 'test']

# 👉 Renaming a Directory or a File
# The rename() method can rename a directory or a file.
# For renaming any directory or file, rename() takes in two basic arguments:
# 1. the old name as the first argument
# 2. the new name as the second argument.
# Example:
import os 
os.rename('test','new_one')
print(os.listdir())
# Output:
# ['.git', 'Day1.py', 'Day10.py', 'Day11.py', 'Day12.py', 'Day13.py', 'Day14.py', 'Day15.py', 'Day16.py', 'Day17.py', 'Day18.py', 'Day19.py', 'Day2.py', 'Day20.py', 'Day3.py', 'Day4.py', 'Day5.py', 'Day6.py', 'Day7.py', 'Day8.py', 'Day9.py', 'new_one', 'README.md']

# Here, 'test' directory is renamed to 'new_one' using the rename() method.

# 👉 Removing Directory or File in Python
# In Python, we can use the remove() method or the rmdir() method to remove a file or directory.
# First let's use remove() to delete a file,
import os
# delete "myfile.txt" file
os.remove("myfile.txt")
# Here, we have used the remove() method to remove the "myfile.txt" file.

# Now let's use rmdir() to delete an empty directory,
import os
# delete the empty directory "mydir"
os.rmdir("mydir") 

# In order to remove a non-empty directory, we can use the rmtree() method inside the shutil module.
import shutil
# delete "mydir" directory and all of its contents
shutil.rmtree("mydir")

#It's important to note that these functions permanently delete the files or directories, so we need to careful when using them.

