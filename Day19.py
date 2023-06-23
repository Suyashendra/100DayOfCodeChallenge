# 🔵 Python File Operation

# A file is a container in computer storage devices used for storing data.

# When we want to read from or write to a file, we need to open it first. 
# When we are done, it needs to be closed so that the resources that are tied with the file are freed.

# Hence, in Python, a file operation takes place in the following order:
# 1. Open a file
# 2. Read or Write(perform operation)
# 3. Close the file

# 👉 Opening Files in Python
# We use the open() method to open files.
# To demonstrate how we open files in Python, let's suppose we have a file named test.txt with the following content.
#  ____test.txt____________________
# | This is test file.             |
# | Hello from the test file.      |
# |________________________________|

# Now, let's try to open data from this file using the open() function.
# open file in current directory
file1 = open("test.txt")

# Here, we have created a file object named file1. This object can be used to work with files and directories.
# By default, the files are open in read mode (cannot be modified). The code above is equivalent to
file1 = open("test.txt","r")
# Here, we have explicitly specified the mode by passing the "r" argument which means file is opened for reading.

# Different Modes to Open a File in Python
# r - Open a file for reading. (default)
# w - Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
# x - Open a file for exclusive creation. If the file already exists, the operation fails.
# a - Open a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
# t - Open in text mode. (default)
# b - Open in binary mode.
# + - Open a file for updating(reading and writing)

# Here's few simple examples of how to open a file in different modes,
file1 = open("test.txt") # equivalent to 'r' or 'rt'
file1 = open("test.test",'w')  # write in text mode
file1 = open("img.bmp",'r+b') # read and write in binary mode

# 👉 Reading Files in Python
# After we open a file, we use the read() method to read its contents. For example,
# open a file 
file1 = open("test.txt","r")
# read the file
read_content = file1.read()
print(read_content)

# Output:
# This is a test file.
# Hello from the test file.

# In the above example, we have read the test.txt file that is available in our current directory.

# 👉 Closing File in Python
# When we are done with performing operations on the file, we need to to properly close the file.
# Closing a file will free up the resources that were tied with the file. 
# It is done using the close() method in Python. For example,
# open a file
file1 = open("test.txt","r")
# read the file
read_content = file1.read()
print(read_content)
# close the file
file1.close()

# Output:
# This is a test file.
# Hello from the test file.

# Here, we have used the close() method to close the file.
# After we perform file operation, we should always close the file; it's a good programming practice.

# 👉 Exception Handling in Files
# If an exception occurs when we are performing some operation with the file, the code exits without closing the file. A safer way is to use a try...finally block.
# Example:

try:
    file1 = open("test.txt", "r")
    read_content = file1.read()
    print(read_content)

finally:
    # close the file
    file1.close()

# Here, we have closed the file in the finally block as finally always executes, and the file will be closed even if an exception occurs.

# 👉 Use of with...open Syntax
# In Python, we can use the with...open syntax to automatically close the file.
# Example:
with open("test.txt","r") as file1:
    read_content = file1.read()
    print(read_content)
# Note: Since we don't have to worry about closing the file, make a habit of using the with...open syntax.

# 👉 Writing to Files in Python

# There are two things we need to remember while writing to a file.

# 1. If we try to open a file that doesn't exist, a new file is created.
# 2. If a file already exists, its content is erased, and new content is added to the file.

# In order to write into a file in Python, we need to open it in write mode by passing "w" inside open() as a second argument.
# Suppose, we don't have a file named test2.txt. Let's see what happens if we write contents to the test2.txt file.
with open('test2.txt','w') as file2:
    # write contents to the test2.txt file
    file2.write('Programming is Fun.')
    file2.write('Program for beginners')

# Here a new test2.txt file is created and this file will have contents specified inside the write() method.

#  ____test2.txt____________________
# | Programming is Fun.             |
# | Program for beginners           |
# |_________________________________|

# 👉 Python File Methods
# There are various methods available with the file object. Some of them have been used in the above examples.

# close() - Closes an opened file. It has no effect if the file is already closed.
# detach() - Separates the underlying binary buffer from the TextIOBase and returns it.
# fileno() - Returns an integer number (file descriptor) of the file.
# flush() - Flushes the write buffer of the file stream.
# isatty() - Returns True if the file stream is interactive.
# read(n) - Reads at most n characters from the file. Reads till end of file if it is negative or None.
# readable() - Returns True if the file stream can be read from.
# readline(n=-1) - Reads and returns one line from the file. Reads in at most n bytes if specified.
# readlines(n=-1) - Reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.
# seek(offset,from=SEEK_SET) - Changes the file position to offset bytes, in reference to from (start, current, end).
# seekable() - Returns True if the file stream supports random access.
# tell() - Returns an integer that represents the current position of the file's object.
# truncate(size=None) - Resizes the file stream to size bytes. If size is not specified, resizes to current location.
# writable() - Returns True if the file stream can be written to.
# write(s) - Writes the string s to the file and returns the number of characters written.
# writelines(lines) - Writes a list of lines to the file.