# 🔵 Python Inheritance 

# Like any other OOP languages, Python also supports the concept of class inheritance.
# Inheritance allows us to create a new class from an existing class.
# The new class that is created is known as subclass (child or derived class) and the existing class from which the child class is derived is known as superclass (parent or base class).

# Python Inheritance Syntax:
# define a superclass
class super_class:
    # attributes and method definition
    pass
# inheritance 
class sub_class(super_class):
    # attribute and method of super_class
    # attribute and method of sub_class
    pass

# Here, we are inheriting the sub_class class from the super_class class.

# Example1: Python Inheritance
class Animal:
    # attribute and method of the parent class
    name = ""
    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):
     # new method in subclass
     def display(self):
         # access name attribute of superclass using self 
         print("Dog name is ",self.name)

# create an object of the subclass
labrador = Dog()
# access superclass attribute and method
labrador.name = "Sheru"
labrador.eat()
# call subclass method
labrador.display()
# Output:
# I can eat
# Dog name is Sheru

# In the above example, we have derived a subclass Dog from a superclass Animal.
# Here, we are using labrador (object of Dog) to access name and eat() of the Animal class. This is possible because the subclass inherits all attributes and methods of the superclass.
# Also, we have accessed the name attribute inside the method of the Dog class using self.

# 👉 is-a relationship  
# Inheritance is an is-a relationship. 
# That is, we use inheritance only if there exists an is-a relationship between two classes.
# For example:
# 1. Car is a Vehicle 
# 2. Apple is a Fruit 
# 3. Cat is a Animal
# Here, Car can inherit from Vehicle, Apple can inherit from Fruit, and so on.

# Example2:
# Let's take a look at another example of inheritance 
# A polygon is a closed figure with 3 or more sides.
# Say, we have a class called Polygon defined as follows,
class Polygon:
    def __init__(self,no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
    
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
    
# This class has data attribute to store the number of sides n and magnitude of each side as a list called sides.
# - The inputSides() method takes in the magnitude of each side.
# - The dispSides() method displays these side lengths 

# A triangle is a polygon with 3 sides. So, we can create a class called Triangle which inherits from Polygon.
# This makes all the attributes and methods of Polygon class available to the Triangle class.
# We don't need to define them again(code reusability).
# Triangle can be defined as follows:
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a,b,c = self.sides
        # calculate the semi-perimeter
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

# However, the Triangle class has a new method findArea() to find and print the area of the triangle.
# Now let's see the complete working code of the above example including creating an object.

class Polygon:
    # Initializing the number of sides
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    # method to display the length of each side of the polygon
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    # Initializing the number of sides of the triangle to 3 by 
    # calling the __init__ method of the Polygon class
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides

        # calculate the semi-perimeter
        s = (a + b + c) / 2

        # Using Heron's formula to calculate the area of the triangle
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

# Creating an instance of the Triangle class
t = Triangle()

# Prompting the user to enter the sides of the triangle
t.inputSides()

# Displaying the sides of the triangle
t.dispSides()

# Calculating and printing the area of the triangle
t.findArea()

# Output:

# Enter side 1 : 3
# Enter side 2 : 5
# Enter side 3 : 4
# Side 1 is 3.0
# Side 2 is 5.0
# Side 3 is 4.0
# The area of the triangle is 6.00

# Here, we can see that even though we did not define methods like inputSides() or dispSides() for class Triangle separately, we were able to use them.
# If an attribute is not found in the class itself, the search continues to the base class. This repeats recursively, if the base class is itself derived from other classes.

# 👉 Method Overriding in Python Inheritance
# In the previous example, we see the object of the subclass can access the method of the superclass.
# However, what if the same method is present in both the superclass and subclass?
# The method in the subclass overrides the method in the superclass. The concept is known as method overriding in Python.
# Example: Method Overriding 
class Animal:

    # attributes and method of the parent class
    name = ""
    
    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):

    # override eat() method
    def eat(self):
        print("I like to eat")

# create an object of the subclass
labrador = Dog()

# call the eat() method on the labrador object
labrador.eat()

# Output:
# I like to eat

# In the above example, the same method eat() is present in both the Dog class and the Animal class.
# Now, when we call the eat() method using the object of the Dog subclass, the method of the Dog class is called.
# This is because the eat() method of the Dog subclass overrides the same method of the Animal superclass.

# 👉 The super() Method in Python Inheritance
# Previously we saw that the same method in the subclass overrides the method in the superclass.
# However, if we need to access the superclass method from the subclass, we use the super() method.
# For example:
class Animal:

    name = ""
    
    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):
    
    # override eat() method
    def eat(self):
        
        # call the eat() method of the superclass using super()
        super().eat()
        
        print("I like to eat")

# create an object of the subclass
labrador = Dog()

labrador.eat()

# Output:
# I can eat
# I like to eat

# In the above example, the eat() method of the Dog subclass overrides the same method of the Animal superclass.
# Inside the Dog class, we have used

# call method of superclass
# super().eat()

# to call the eat() method of the Animal superclass from the Dog subclass.
# So, when we call the eat() method using the labrador object

# call the eat() method
# labrador.eat()

# Both the overridden and the superclass version of the eat() method is executed.

# 👉 Uses of Inheritance
# 1. Since a child class can inherit all the functionalities of the parent's class, this allows code reusability.
# 2. Once of functionality is developed, you can simply inherit it. No need to reinvent the wheel. 
# This allows for cleaner code and easier to maintain.
# 3. Since you can also add your own functionalities in the child class, you can inherit only the useful functionalities and define other required features.

