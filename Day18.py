# 👉 Python Multiple Inheritance

# A class can be derived from more than one superclass in Python. 
# This is called multiple inheritance.

# Python Multiple Inheritance Syntax
class Superclass1:
    pass
class Superclass2:
    pass
class MultiDerived(Superclass1, Superclass2):
    pass

# Example:
class Superclass1:
    def class1Fun(self):
        print("This is class1fun")
class Superclass2:
    def class2Fun(self):
        print("This is class2fun")
class MultiDerived(Superclass1, Superclass2):
    pass

obj = MultiDerived()
obj.class1Fun()
obj.class2Fun()

# Output:
# This is class1fun
# This is class2fun

# 👉 Python Multilevel Inheritance
# In Python, not only we can derive a class from the superclass but we can also derive a class from the derive class.
# This form of inheritance is known as multilevel inheritance.

# Syntax:
class SuperClass:
    # Super class code here
    pass

class DerivedClass1(SuperClass):
    # Derived class 1 code here
    pass

class DerivedClass2(DerivedClass1):
    # Derived class 2 code here
    pass

# Example:
class SuperClass:

    def super_method(self):
        print("Super Class method called")

# define class that derive from SuperClass
class DerivedClass1(SuperClass):
    def derived1_method(self):
        print("Derived class 1 method called")

# define class that derive from DerivedClass1
class DerivedClass2(DerivedClass1):

    def derived2_method(self):
        print("Derived class 2 method called")

# create an object of DerivedClass2
obj1 = DerivedClass2()

obj1.super_method()  # Output: "Super Class method called"

obj1.derived1_method()  # Output: "Derived class 1 method called"

obj1.derived2_method()  # Output: "Derived class 2 method called"

# 👉 Method Resolution Order (MRO) in Python
# If two superclasses have the same method name and the derived class calls that method, Python uses the MRO to search for the right method to call. 
# For example:

class SuperClass1:
    def info(self):
        print("Super Class 1 method called")

class SuperClass2:
    def info(self):
        print("Super Class 2 method called")

class Derived(SuperClass1, SuperClass2):
    pass

obj2 = Derived()
obj2.info()  

# Output: 
# Super Class 1 method called

# Here, SuperClass1 and SuperClass2 both of these classes define a method info().
# So when info() is called using the obj2 object of the Derived class, Python uses the MRO to determine which method to call.
# In this case, the MRO specifies that methods should be inherited from the leftmost superclass first, so info() of SuperClass1 is called rather than that of SuperClass2.

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 🔵 Python Polymorphism
# The word "ploymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

# 👉 Function Polymorphism
# An example of a Python function that can be used on different objects is the len() function.
# - For String len() returns the number of characters
# - For tuples len() returns the number of items in the tuple
# - For dictionaries len() returns the number of key/value pairs in the dictionary

# 👉 Class Polymorphism
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")
    
class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
    x.move()

# Output:
# Drive!
# Sail!
# Fly!

# Because of polymorphism we can execute the same method for all three classes.

# 👉 Inheritance Class Polymorphism
# If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:
# Example:
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")
    
class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()

# Output:
# Ford
# Mustang
# Move!
# Ibiza
# Touring 20
# Sail!
# Boeing
# 747
# Fly!

# Child classes inherits the properties and methods from the parent class.
# In the example above you can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle.
# The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.
# Because of polymorphism we can execute the same method for all classes.

