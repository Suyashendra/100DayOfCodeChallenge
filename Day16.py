# Python Classes and Objects

# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# Create a Class
# To create a class, use the keyword class:
# Example: Create a class named MyClass, with a property named x:
class MyClass:
    x = 5

# Create Object
# Now we can use the class named MyClass to create objects:
# Example: Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)

# 👉 The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# Example: Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
    # constructor function 
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John",36)
print(p1.name)
print(p1.age)
# Output:
# John
# 36

# Note: The __init__() function is called automatically every time the class is being used to create a new object.

# 👉 The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:
# Example:
# The string representation of an object WITHOUT the __str__() function:
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
p1 = Person("John",25)
print(p1)
# Output:
# <__main__.Person object at 0x000002B9D8757FD0>

# The string representation of an object WITH the __str__() function:
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"
    
p1 = Person("John",25)
print(p1)
# Output:
# John(25)

# 👉 Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.
# Example: Function that print a greeting, and execute it on the p1 object:
class Person:
    def __init__(self,name):
        self.name = name
    
    def myFun(self):
        print("Hello my name is "+self.name)

p1 = Person("John")
p1.myFun()
# Output:
# Hello my name is John

# Note: The self parameter is a reference to the current instance of the class, and is used to access variable that belong to the class.

# 👉 The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:

# Example: Use the words mysillyobject and abc instead of self:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("Suyash", 36)
p1.myfunc() 
# Output:
# Hello my name is Suyash

# 👉 Modify Object Properties
# You can modify properties on objects like this:
# Example: set the age of p1 to 30
class Person:
    def __init__(self,age):
        self.age = age

p1 = Person(25)
print(p1.age)
p1.age = 30
print(p1.age)
# Output:
# 25
# 30

# 👉 Delete Object Properties:
# You can delete properties on objects by using the del keyword:
# Example:
del p1.age

# 👉 Delete Objects 
# You can delete objects by using the del keyword:
# Example:
del p1

# 👉 The pass Statement
# Class definitions cannot be empty, but if you for some reason have a class definition with no content,
# put in the pass statement to avoid getting an error.
# Example:
class Person:
    pass 

# 👉 Python Encapsulation 

# Encapsulation is one of the key features of object-oriented programming.
# Encapsulation refers to the bundling of attributes and methods inside a single class.
# It prevents outer classes from accessing and changing attributes and methods of a class. 
# This also helps to achieve data hiding.

# In python we denote private attributes using underscore as the prefix i.e single (_) or double (__).
# Example: 
class Computer:
    def __init__(self):
        self.__maxprice = 900
    
    def sell(self):
        print("Selling Price:",self.__maxprice)
    
    def setMaxPrice(self, price):
        self.__maxprice = price
    
c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

# Output
# Selling Price: 900
# Selling Price: 900
# Selling Price: 1000

# In the above program, we defined a Computer class.
# We used __init__() method to store the maximum selling price of Computer. Here, notice the code
# c.__maxprice = 1000
# Here, we have tried to modify the value of __maxprice outside of the class. However, since __maxprice is a private variable, this modification is not seen on the output.
# As shown, to change the value, we have to use a setter function i.e setMaxPrice() which takes price as a parameter.
